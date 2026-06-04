/* BFSI Bible — Notes & Highlights
 *
 * Features
 *   - Select any text in the main content → popover with 4 highlight colours
 *     and an "Add note" action.
 *   - Notes persist in localStorage per page (key = `bfsi-notes::<path>`).
 *   - Side panel ("Notes") to list / edit / delete / export / import notes
 *     for the current page, plus a global view across pages.
 *   - Keyboard: Ctrl/Cmd+Shift+H toggle the side panel.
 *
 * Persistence model
 *   Each note is anchored by `(text, occurrenceIndex)` — the n-th match of the
 *   selected text inside the main content. This survives minor edits and
 *   never requires storing fragile DOM paths.
 *
 *   {
 *     id:        crypto.randomUUID()-like
 *     text:      string                // exactly the user selection
 *     occIndex:  number                // n-th occurrence of `text` in main
 *     color:     "yellow"|"green"|"blue"|"pink"
 *     note:      string                // optional rich-text-ish (plain text + newlines)
 *     createdAt: ISO string
 *     updatedAt: ISO string
 *   }
 */
(function () {
  "use strict";

  // ----------------------------------------------------------- constants
  const COLORS = [
    { id: "yellow", label: "Yellow", hex: "#E2B548" },
    { id: "green",  label: "Green",  hex: "#6DD3B8" },
    { id: "blue",   label: "Blue",   hex: "#4FB3CF" },
    { id: "pink",   label: "Pink",   hex: "#E07A6B" },
  ];
  const STORE_PREFIX = "bfsi-notes::";
  const STORE_KEY = STORE_PREFIX + location.pathname;

  // ----------------------------------------------------------- storage
  const store = {
    load() {
      try { return JSON.parse(localStorage.getItem(STORE_KEY) || "[]"); }
      catch { return []; }
    },
    save(notes) {
      localStorage.setItem(STORE_KEY, JSON.stringify(notes));
    },
    allPages() {
      const out = {};
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith(STORE_PREFIX)) {
          try { out[k.slice(STORE_PREFIX.length)] = JSON.parse(localStorage.getItem(k) || "[]"); }
          catch { /* ignore */ }
        }
      }
      return out;
    },
  };

  // ----------------------------------------------------------- helpers
  const uid = () =>
    (crypto.randomUUID && crypto.randomUUID()) ||
    "n_" + Date.now().toString(36) + Math.random().toString(36).slice(2, 8);

  const now = () => new Date().toISOString();

  const main = () => document.querySelector("main.content");

  /** Find all occurrences of `text` in main content as Range objects. */
  function findOccurrences(text) {
    const root = main();
    if (!root || !text) return [];
    const ranges = [];
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(n) {
        // Skip script/style and our own UI overlays
        let p = n.parentElement;
        while (p) {
          if (p.classList && (p.classList.contains("bf-skip") ||
              p.tagName === "SCRIPT" || p.tagName === "STYLE")) {
            return NodeFilter.FILTER_REJECT;
          }
          p = p.parentElement;
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    // Build a flat string + index map so we can match across text nodes
    const nodes = [];
    let combined = "";
    while (walker.nextNode()) {
      nodes.push({ node: walker.currentNode, start: combined.length });
      combined += walker.currentNode.nodeValue;
    }
    const norm = s => s.replace(/\s+/g, " ");
    const haystack = norm(combined);
    const needle = norm(text);
    if (!needle) return [];
    let from = 0;
    while (true) {
      const idx = haystack.indexOf(needle, from);
      if (idx === -1) break;
      // Map idx and idx+needle.length back to (node, offset) — careful with
      // whitespace normalisation: walk the original combined string and skip
      // collapsed whitespace counts.
      const range = mapRange(combined, nodes, idx, idx + needle.length);
      if (range) ranges.push(range);
      from = idx + Math.max(needle.length, 1);
    }
    return ranges;
  }

  function mapRange(combined, nodes, normStart, normEnd) {
    // Convert positions in the whitespace-normalised string back to positions
    // in `combined`, then locate text nodes and offsets.
    const back = (target) => {
      let normPos = 0, origPos = 0, lastWasSpace = false;
      while (origPos < combined.length && normPos < target) {
        const ch = combined[origPos];
        if (/\s/.test(ch)) {
          if (!lastWasSpace) { normPos++; lastWasSpace = true; }
        } else {
          normPos++;
          lastWasSpace = false;
        }
        origPos++;
      }
      return origPos;
    };
    const oStart = back(normStart);
    const oEnd = back(normEnd);
    const find = (offset) => {
      for (let i = nodes.length - 1; i >= 0; i--) {
        if (nodes[i].start <= offset) {
          return { node: nodes[i].node, offset: offset - nodes[i].start };
        }
      }
      return null;
    };
    const a = find(oStart), b = find(oEnd);
    if (!a || !b) return null;
    try {
      const r = document.createRange();
      r.setStart(a.node, Math.min(a.offset, a.node.nodeValue.length));
      r.setEnd(b.node, Math.min(b.offset, b.node.nodeValue.length));
      return r;
    } catch { return null; }
  }

  /** Wrap a Range with <mark class="bf-hl bf-hl-<color>"> elements,
   *  splitting across text nodes as needed. Stores `data-id` for click. */
  function paintRange(range, color, id, hasNote) {
    if (range.collapsed) return;
    const root = main();
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const nodesToWrap = [];
    while (walker.nextNode()) {
      const n = walker.currentNode;
      const nodeRange = document.createRange();
      nodeRange.selectNodeContents(n);
      if (range.compareBoundaryPoints(Range.END_TO_START, nodeRange) >= 0) continue;
      if (range.compareBoundaryPoints(Range.START_TO_END, nodeRange) <= 0) break;
      // Compute intersection
      const start = (n === range.startContainer) ? range.startOffset : 0;
      const end   = (n === range.endContainer)   ? range.endOffset   : n.nodeValue.length;
      if (end > start) nodesToWrap.push({ node: n, start, end });
    }
    nodesToWrap.forEach(({ node, start, end }) => {
      const before = node.nodeValue.slice(0, start);
      const middle = node.nodeValue.slice(start, end);
      const after  = node.nodeValue.slice(end);
      const mark = document.createElement("mark");
      mark.className = `bf-hl bf-hl-${color}` + (hasNote ? " bf-hl-noted" : "");
      mark.setAttribute("data-id", id);
      mark.textContent = middle;
      const frag = document.createDocumentFragment();
      if (before) frag.appendChild(document.createTextNode(before));
      frag.appendChild(mark);
      if (after) frag.appendChild(document.createTextNode(after));
      node.parentNode.replaceChild(frag, node);
    });
  }

  function clearAllPaint() {
    main().querySelectorAll("mark.bf-hl").forEach(m => {
      const parent = m.parentNode;
      while (m.firstChild) parent.insertBefore(m.firstChild, m);
      parent.removeChild(m);
      parent.normalize();
    });
  }

  function repaintAll() {
    clearAllPaint();
    const notes = store.load();
    notes.forEach(n => {
      const ranges = findOccurrences(n.text);
      const r = ranges[n.occIndex] || ranges[0];
      if (r) paintRange(r, n.color, n.id, !!n.note);
    });
    refreshPanel();
  }

  // ----------------------------------------------------------- selection toolbar
  let toolbar;
  function buildToolbar() {
    toolbar = document.createElement("div");
    toolbar.className = "bf-skip bf-toolbar";
    toolbar.setAttribute("role", "toolbar");
    toolbar.setAttribute("aria-label", "Highlight selection");
    toolbar.innerHTML = `
      <div class="bf-tb-colors">
        ${COLORS.map(c =>
          `<button type="button" class="bf-tb-color" data-color="${c.id}"
                   style="background:${c.hex}" title="Highlight ${c.label}"
                   aria-label="Highlight ${c.label}"></button>`).join("")}
      </div>
      <button type="button" class="bf-tb-note" title="Add note (highlights yellow + opens note)">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
          <path d="M18.5 2.5a2.121 2.121 0 1 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
        </svg>
        Note
      </button>`;
    document.body.appendChild(toolbar);
    toolbar.addEventListener("mousedown", e => e.preventDefault());
    toolbar.querySelectorAll(".bf-tb-color").forEach(btn =>
      btn.addEventListener("click", () =>
        createFromSelection(btn.dataset.color, false))
    );
    toolbar.querySelector(".bf-tb-note").addEventListener("click", () =>
      createFromSelection("yellow", true)
    );
  }

  function showToolbarFor(rect) {
    const top = window.scrollY + rect.top - toolbar.offsetHeight - 10;
    const left = Math.max(8,
      window.scrollX + rect.left + rect.width / 2 - toolbar.offsetWidth / 2);
    toolbar.style.top  = top + "px";
    toolbar.style.left = left + "px";
    toolbar.classList.add("show");
  }
  function hideToolbar() { toolbar && toolbar.classList.remove("show"); }

  // ----------------------------------------------------------- create note from selection
  let lastSelection = null;  // {text, occIndex}

  function captureSelectionRange() {
    const sel = window.getSelection();
    if (!sel || sel.isCollapsed) return null;
    const text = sel.toString().trim();
    if (text.length < 2) return null;
    // Make sure selection is inside main content
    const range = sel.getRangeAt(0);
    if (!main().contains(range.commonAncestorContainer)) return null;
    // Determine which occurrence this is
    const all = findOccurrences(text);
    let occIndex = 0;
    for (let i = 0; i < all.length; i++) {
      if (rangesEquivalent(all[i], range)) { occIndex = i; break; }
    }
    return { text, occIndex, rect: range.getBoundingClientRect() };
  }

  function rangesEquivalent(a, b) {
    return a.startContainer === b.startContainer &&
           a.endContainer   === b.endContainer   &&
           a.startOffset    === b.startOffset    &&
           a.endOffset      === b.endOffset;
  }

  function createFromSelection(color, openNote) {
    const cap = captureSelectionRange() || lastSelection;
    if (!cap) return;
    const id = uid();
    const note = {
      id, text: cap.text, occIndex: cap.occIndex || 0,
      color, note: "", createdAt: now(), updatedAt: now()
    };
    const all = store.load();
    all.push(note);
    store.save(all);
    repaintAll();
    hideToolbar();
    window.getSelection().removeAllRanges();
    if (openNote) openNoteEditor(id);
  }

  // ----------------------------------------------------------- side panel
  let panel;
  function buildPanel() {
    panel = document.createElement("aside");
    panel.className = "bf-skip bf-panel";
    panel.setAttribute("aria-label", "Notes panel");
    panel.innerHTML = `
      <header class="bf-panel-head">
        <h3>Notes & Highlights</h3>
        <div class="bf-panel-actions">
          <button type="button" class="bf-btn-ghost" data-action="export"
                  title="Export all notes as JSON">Export</button>
          <button type="button" class="bf-btn-ghost" data-action="import"
                  title="Import notes from JSON">Import</button>
          <button type="button" class="bf-btn-close" aria-label="Close panel">×</button>
        </div>
      </header>
      <div class="bf-panel-tabs">
        <button class="bf-tab active" data-scope="page">This page</button>
        <button class="bf-tab" data-scope="all">All pages</button>
      </div>
      <div class="bf-panel-list" role="list"></div>
      <input type="file" class="bf-import" accept="application/json" hidden>
      <footer class="bf-panel-foot">
        <span class="bf-foot-hint">Tip — select any text to highlight or add a note. Press
        <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>H</kbd> to toggle this panel.</span>
      </footer>`;
    document.body.appendChild(panel);

    panel.querySelector(".bf-btn-close").addEventListener("click", togglePanel);
    panel.querySelectorAll(".bf-tab").forEach(t =>
      t.addEventListener("click", () => {
        panel.querySelectorAll(".bf-tab").forEach(x => x.classList.remove("active"));
        t.classList.add("active");
        refreshPanel();
      }));
    panel.querySelector('[data-action="export"]').addEventListener("click", exportNotes);
    panel.querySelector('[data-action="import"]').addEventListener("click",
      () => panel.querySelector(".bf-import").click());
    panel.querySelector(".bf-import").addEventListener("change", importNotes);

    // Floating launcher
    const launcher = document.createElement("button");
    launcher.type = "button";
    launcher.className = "bf-skip bf-launcher";
    launcher.setAttribute("aria-label", "Open notes panel");
    launcher.title = "Notes (Ctrl+Shift+H)";
    launcher.innerHTML = `
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
           stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14 2 14 8 20 8"/>
        <line x1="9" y1="13" x2="15" y2="13"/>
        <line x1="9" y1="17" x2="13" y2="17"/>
      </svg>
      <span class="bf-launcher-count">0</span>`;
    launcher.addEventListener("click", togglePanel);
    document.body.appendChild(launcher);
  }

  function togglePanel() { panel.classList.toggle("open"); }

  function refreshPanel() {
    if (!panel) return;
    const scope = panel.querySelector(".bf-tab.active").dataset.scope;
    const list = panel.querySelector(".bf-panel-list");
    list.innerHTML = "";
    const pageNotes = store.load();
    document.querySelector(".bf-launcher-count").textContent = pageNotes.length;

    let groups;
    if (scope === "page") {
      groups = [{ path: location.pathname, notes: pageNotes }];
    } else {
      const all = store.allPages();
      groups = Object.keys(all).sort().map(p => ({ path: p, notes: all[p] }));
    }
    let any = false;
    groups.forEach(({ path, notes }) => {
      if (!notes.length) return;
      any = true;
      if (scope === "all") {
        const h = document.createElement("div");
        h.className = "bf-grp-head";
        h.textContent = path;
        list.appendChild(h);
      }
      notes.forEach(n => list.appendChild(noteCard(n, path)));
    });
    if (!any) {
      list.innerHTML = `<div class="bf-empty">No notes yet on this
        ${scope === "page" ? "page" : "site"}. Select text in the content area
        to start.</div>`;
    }
  }

  function noteCard(n, path) {
    const card = document.createElement("article");
    card.className = "bf-card";
    card.setAttribute("role", "listitem");
    card.dataset.id = n.id;
    const onThisPage = path === location.pathname;
    card.innerHTML = `
      <div class="bf-card-bar bf-hl-${n.color}"></div>
      <div class="bf-card-body">
        <blockquote class="bf-card-quote">${escapeHtml(n.text)}</blockquote>
        <textarea class="bf-card-note" placeholder="Write a note…"
          rows="${Math.max(2, (n.note || '').split('\n').length)}"
          ${onThisPage ? "" : "disabled"}>${escapeHtml(n.note || "")}</textarea>
        <div class="bf-card-meta">
          <span class="bf-card-time">${formatTime(n.updatedAt)}</span>
          ${!onThisPage ? `<a class="bf-card-link" href="${path}">Open page →</a>` : ""}
          <span class="bf-card-actions">
            ${onThisPage ? `
              <button type="button" data-action="scroll" title="Scroll to highlight">↗</button>
              <button type="button" data-action="recolor" title="Cycle colour">●</button>
              <button type="button" data-action="delete" title="Delete">🗑</button>
            ` : `<button type="button" data-action="delete-other" title="Delete">🗑</button>`}
          </span>
        </div>
      </div>`;

    if (onThisPage) {
      const ta = card.querySelector(".bf-card-note");
      ta.addEventListener("input", () => updateNote(n.id, { note: ta.value }));
      card.querySelector('[data-action="scroll"]').addEventListener("click",
        () => scrollToHighlight(n.id));
      card.querySelector('[data-action="recolor"]').addEventListener("click",
        () => cycleColor(n.id));
      card.querySelector('[data-action="delete"]').addEventListener("click",
        () => deleteNote(n.id));
    } else {
      card.querySelector('[data-action="delete-other"]').addEventListener("click",
        () => deleteNoteOnPage(path, n.id));
    }
    return card;
  }

  function escapeHtml(s) {
    return (s || "").replace(/[&<>"']/g, c =>
      ({ "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;" }[c]));
  }
  function formatTime(iso) {
    try {
      const d = new Date(iso);
      return d.toLocaleString(undefined,
        { dateStyle: "medium", timeStyle: "short" });
    } catch { return ""; }
  }

  // ----------------------------------------------------------- mutations
  function updateNote(id, patch) {
    const all = store.load();
    const i = all.findIndex(n => n.id === id);
    if (i < 0) return;
    all[i] = { ...all[i], ...patch, updatedAt: now() };
    store.save(all);
    // Update the noted-state class without full repaint to preserve textarea focus
    const mark = main().querySelector(`mark.bf-hl[data-id="${id}"]`);
    if (mark) mark.classList.toggle("bf-hl-noted", !!all[i].note);
    document.querySelector(".bf-launcher-count").textContent = all.length;
  }
  function deleteNote(id) {
    const all = store.load().filter(n => n.id !== id);
    store.save(all);
    repaintAll();
  }
  function deleteNoteOnPage(path, id) {
    const k = STORE_PREFIX + path;
    try {
      const arr = JSON.parse(localStorage.getItem(k) || "[]").filter(n => n.id !== id);
      localStorage.setItem(k, JSON.stringify(arr));
    } catch {}
    refreshPanel();
  }
  function cycleColor(id) {
    const all = store.load();
    const n = all.find(x => x.id === id);
    if (!n) return;
    const idx = COLORS.findIndex(c => c.id === n.color);
    n.color = COLORS[(idx + 1) % COLORS.length].id;
    n.updatedAt = now();
    store.save(all);
    repaintAll();
  }
  function scrollToHighlight(id) {
    const m = main().querySelector(`mark.bf-hl[data-id="${id}"]`);
    if (!m) return;
    m.scrollIntoView({ behavior: "smooth", block: "center" });
    m.classList.add("bf-hl-flash");
    setTimeout(() => m.classList.remove("bf-hl-flash"), 1500);
  }
  function openNoteEditor(id) {
    if (!panel.classList.contains("open")) togglePanel();
    refreshPanel();
    const card = panel.querySelector(`.bf-card[data-id="${id}"]`);
    if (card) {
      card.scrollIntoView({ block: "nearest" });
      const ta = card.querySelector(".bf-card-note");
      if (ta) ta.focus();
    }
  }

  // ----------------------------------------------------------- import / export
  function exportNotes() {
    const data = {
      exportedAt: now(),
      schema: "bfsi-bible-notes/1",
      pages: store.allPages(),
    };
    const blob = new Blob([JSON.stringify(data, null, 2)],
      { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `bfsi-bible-notes-${new Date().toISOString().slice(0,10)}.json`;
    document.body.appendChild(a); a.click(); a.remove();
    URL.revokeObjectURL(a.href);
  }
  function importNotes(e) {
    const file = e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const data = JSON.parse(reader.result);
        if (!data.pages) throw new Error("not a notes file");
        if (!confirm("Merge imported notes with existing notes?")) return;
        Object.entries(data.pages).forEach(([path, notes]) => {
          const k = STORE_PREFIX + path;
          const existing = JSON.parse(localStorage.getItem(k) || "[]");
          const seen = new Set(existing.map(n => n.id));
          notes.forEach(n => { if (!seen.has(n.id)) existing.push(n); });
          localStorage.setItem(k, JSON.stringify(existing));
        });
        repaintAll();
        alert("Imported.");
      } catch (err) {
        alert("Could not import: " + err.message);
      }
    };
    reader.readAsText(file);
    e.target.value = "";
  }

  // ----------------------------------------------------------- click on highlight
  function onMarkClick(e) {
    const m = e.target.closest("mark.bf-hl");
    if (!m) return;
    const id = m.getAttribute("data-id");
    if (!id) return;
    if (!panel.classList.contains("open")) togglePanel();
    refreshPanel();
    setTimeout(() => {
      const card = panel.querySelector(`.bf-card[data-id="${id}"]`);
      if (card) {
        card.scrollIntoView({ block: "nearest" });
        card.classList.add("bf-card-flash");
        setTimeout(() => card.classList.remove("bf-card-flash"), 1200);
        const ta = card.querySelector(".bf-card-note");
        if (ta) ta.focus();
      }
    }, 50);
  }

  // ----------------------------------------------------------- selection events
  function onSelectionChange() {
    const cap = captureSelectionRange();
    if (!cap) { hideToolbar(); return; }
    lastSelection = cap;
    showToolbarFor(cap.rect);
  }

  // ----------------------------------------------------------- bootstrap
  function init() {
    if (!main()) return;
    buildToolbar();
    buildPanel();

    document.addEventListener("mouseup", () => setTimeout(onSelectionChange, 1));
    document.addEventListener("touchend", () => setTimeout(onSelectionChange, 1));
    document.addEventListener("selectionchange", () => {
      // Hide toolbar when selection collapses
      const sel = window.getSelection();
      if (!sel || sel.isCollapsed) hideToolbar();
    });
    document.addEventListener("scroll", hideToolbar, { passive: true });
    main().addEventListener("click", onMarkClick);

    document.addEventListener("keydown", e => {
      if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key.toLowerCase() === "h") {
        e.preventDefault(); togglePanel();
      }
      if (e.key === "Escape") { hideToolbar(); }
    });

    repaintAll();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
