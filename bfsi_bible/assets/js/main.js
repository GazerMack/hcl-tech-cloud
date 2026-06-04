// BFSI Bible — boot script (dark theme)
(function () {
  // ---------- Mermaid: dark theme tuned to the site palette ----------
  if (window.mermaid) {
    window.mermaid.initialize({
      startOnLoad: true,
      theme: "base",
      securityLevel: "loose",  // allow raw textContent parsing of our trusted, self-authored diagrams
      themeVariables: {
        background:            "#141A22",
        primaryColor:          "#1B232D",
        primaryTextColor:      "#E6ECF3",
        primaryBorderColor:    "#4FB3CF",
        lineColor:             "#6DD3B8",
        secondaryColor:        "#232D38",
        tertiaryColor:         "#1B232D",
        textColor:             "#E6ECF3",
        nodeBorder:            "#4FB3CF",
        clusterBkg:            "#1B232D",
        clusterBorder:         "#4FB3CF",
        edgeLabelBackground:   "#141A22",
        labelTextColor:        "#E6ECF3",
        actorBkg:              "#1B232D",
        actorBorder:           "#4FB3CF",
        actorTextColor:        "#E6ECF3",
        actorLineColor:        "#4FB3CF",
        signalColor:           "#6DD3B8",
        signalTextColor:       "#E6ECF3",
        labelBoxBkgColor:      "#1B232D",
        labelBoxBorderColor:   "#4FB3CF",
        loopTextColor:         "#E6ECF3",
        noteBkgColor:          "#232D38",
        noteTextColor:         "#E6ECF3",
        noteBorderColor:       "#4FB3CF",
        fontFamily:            "Inter, system-ui, sans-serif",
        fontSize:              "14px",
      },
      flowchart:  { htmlLabels: true, curve: "basis", padding: 18, useMaxWidth: true },
      sequence:   { actorMargin: 60, boxMargin: 10, noteMargin: 12, useMaxWidth: true },
      gantt:      { useMaxWidth: true },
      er:         { useMaxWidth: true },
    });
  }

  // ---------- Right-side mini-TOC ----------
  const main = document.querySelector(".content");
  const tocHost = document.querySelector(".toc-right");
  if (main && tocHost) {
    const headers = main.querySelectorAll("h2, h3");
    headers.forEach(h => {
      if (!h.id) h.id = h.textContent.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
      const a = document.createElement("a");
      a.href = "#" + h.id;
      a.textContent = h.textContent.replace(/^\d+(\.\d+)?\s*[\.\u2014\u00B7]?\s*/, "").trim();
      a.className = h.tagName.toLowerCase();
      tocHost.appendChild(a);
    });

    const links = tocHost.querySelectorAll("a");
    const obs = new IntersectionObserver(entries => {
      entries.forEach(en => {
        if (en.isIntersecting) {
          links.forEach(l => l.classList.remove("active"));
          const id = en.target.id;
          const link = tocHost.querySelector(`a[href="#${id}"]`);
          if (link) link.classList.add("active");
        }
      });
    }, { rootMargin: "0px 0px -70% 0px" });
    headers.forEach(h => obs.observe(h));
  }

  // ---------- Sidebar search ----------
  const search = document.querySelector(".sidebar .search");
  if (search) {
    search.addEventListener("input", e => {
      const q = e.target.value.trim().toLowerCase();
      const links = document.querySelectorAll(".sidebar nav a");
      links.forEach(a => {
        const matches = !q || a.textContent.toLowerCase().includes(q);
        a.style.display = matches ? "" : "none";
      });
      document.querySelectorAll(".sidebar nav .part").forEach(p => {
        let next = p.nextElementSibling, hasVisible = false;
        while (next && !next.classList.contains("part")) {
          if (next.style.display !== "none") { hasVisible = true; break; }
          next = next.nextElementSibling;
        }
        p.style.display = hasVisible ? "" : "none";
      });
    });
  }

  // ---------- Highlight active page in sidebar ----------
  const here = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".sidebar nav a").forEach(a => {
    const href = a.getAttribute("href") || "";
    if (href.endsWith(here)) a.classList.add("active");
  });
})();
