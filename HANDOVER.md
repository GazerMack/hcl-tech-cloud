# BFSI Techno-Functional Leader Bible — Handover

**Purpose of this file.** Drop this into any new chat session (with the same workspace) and the next assistant should be able to continue building the bible at the same quality, with no back-and-forth, and without re-discovering decisions or known traps.

**Last updated:** v1.14 — **Core curriculum complete, stretch V.2 (Fraud, AML & sanctions deep) shipped.** All Foundations (I.1–I.4) + Application Stack (II.1–II.2) + Data (III.1–III.2) + Infra & Ops (IV.1–IV.2) + Security, Risk & Compliance (V.1–V.2) + BFSI Platforms (VI.1–VI.4) + Leadership Lenses (VII.1–VII.2). I.1 deep rewrite complete. I.4, III.2, IV.2, V.2 stretch topics complete. Mermaid syntax stable; notes/highlights feature shipped.

---

## 1. Mission & success criteria

Build a **self-contained dark-mode HTML "bible"** that takes an MBA-Finance professional with **zero IT background** to a fluent senior **techno-functional leader in BFSI** (Banking / Financial Services / Insurance). Tailored to **HCLTech BFSI engagements** — Citi, Standard Chartered, Deutsche Bank, Barclays, NatWest, JPMorgan, Wells Fargo, HSBC, etc.

**Success criteria for every topic**
- Easy to **study** — clean dark UI, strong hierarchy, callouts, tables, diagrams.
- Easy to **remember** — analogies, dual-anchor primers, worked examples with real numbers, glossaries.
- Easy to **apply in real life** — decision matrices, "questions to ask in any review" lists, red-flag callouts ("push back if you hear this"), HCLTech client context.
- **Latest information only** — verify dates, vendor positions, regulator rules are current as of late 2024 / early 2025.

---

## 2. Locked pedagogy (do not change without user sign-off)

This is the user's preferred format. It is also stored as a Cascade memory titled **"Study-material pedagogy & format preference"** — keep both in sync.

### 2.1 Non-negotiable rules

1. **Zero-assumption start.** Reader is intelligent (MBA-Finance) but has no prior IT background.
2. **Dual-anchor primer.** Section 0 of every topic has TWO anchor lanes:
   - **IT-side anchor** — start from a thing they already physically use (laptop, phone).
   - **BFSI-side anchor** — start from a thing they already do (UPI tap, swiping a card, EMI mandate).
3. **Geographic balance.** Equal weight to **India + United States + United Kingdom + Eurozone + Singapore**. Add Brazil / UAE / Australia / Hong Kong where relevant. Never India-only.
4. **Abbreviation discipline.** Every TLA / acronym is expanded on first use ("CPU (Central Processing Unit)"), then short form thereafter. Never assume the reader knows it.
5. **Latest information only.** Verify rules and dates. Cite reputable sources (regulators, central banks, NIST, ISO, vendor docs).
6. **HCLTech client context** when relevant — Citi, Standard Chartered, Deutsche, Barclays, NatWest, JPM, Wells, HSBC.

### 2.2 Standard topic structure (use these exact section headings)

```
0.  Primer — anchored to things you already know   [Basic]
    0.1  IT-side anchor (your laptop / phone)
    0.2  BFSI-side anchor (your UPI / card / loan)
    0.3+ further primer subsections as needed

1.  Why X exists at all — first principles          [Basic]
2.  The core concept in one picture                 [Basic]   (with a Mermaid diagram)
3.  How it actually works — phase by phase          [Intermediate]
4.  Types & variations                              [Intermediate] (geo-balanced tables)
5.  Advanced — the mechanisms underneath            [Advanced]
6.  BFSI / domain regulatory overlay                [Advanced] (matrix table by region)
7.  Trade-offs and decisions a leader owns          [Intermediate] (decision matrix)
8.  Worked examples — numbers and decisions         [Intermediate] (3–5 worked examples across geos)
9.  Questions a leader asks in any review           [Basic]
10. Red flags + topic glossary                      [Basic]
```

Every H2 must have a **difficulty pill**: `Basic` / `Intermediate` / `Advanced`.

### 2.3 Callout types in use (visually distinct)

- `primer(...)` — "read this even if you think you know it"
- `it_anchor(...)` — "From what you already know — your laptop"
- `bfsi_anchor(...)` — "From what you already know — your bank account"
- `analogy(...)`
- `example(title, body)` — "Worked example — …"
- `red_flag(...)` — "Red flag — push back if you hear this"
- `callout(label, body, kind="info")` — generic info / note

### 2.4 Length guidance

- **Each topic: 5,000–15,000 words.** ≈ 20–60 KB rendered HTML. Topics under 15 KB are too thin.
- A topic file in Python is typically 400–700 lines.

### 2.5 What the user explicitly does NOT want

- Tiny intros that stop after one section.
- Indian-only treatment for global concepts.
- Unexpanded abbreviations.
- "Coming soon" stubs — write the topic for real or don't add it to navigation.
- Any output that hasn't been mentally validated against renderer quirks (especially Mermaid).
- Asking permission for every small decision — proceed and inform.

---

## 3. Repo layout

```
hcl tech cloud/
├── README.md                          # user-facing readme
├── HANDOVER.md                        # this file
├── bfsi_bible/                        # generated HTML site (the deliverable)
│   ├── index.html
│   ├── glossary.html
│   ├── foundations/
│   │   ├── index.html
│   │   ├── 01-transactions.html       # 196.5 KB, generated from May 2026 v2 rewrite sections 0–9
│   │   ├── 02-seven-layers.html       # 27.5 KB
│   │   ├── 03-cloud-and-infra.html    # 27.9 KB
│   │   └── 04-network-fundamentals.html  # 41.3 KB
│   ├── bfsi-platforms/
│   │   ├── index.html
│   │   ├── 01-core-banking-platforms.html  # 24.6 KB
│   │   ├── 02-payments-engines.html        # 45.0 KB
│   │   ├── 03-lending-and-originations.html  # 56.7 KB
│   │   └── 04-capmkts-and-insurance.html     # 38.6 KB
│   ├── application-stack/
│   │   ├── index.html
│   │   ├── 01-apis-and-integration.html    # 51.2 KB
│   │   └── 02-microservices-monoliths-ddd.html  # 39.2 KB
│   ├── data/
│   │   ├── index.html
│   │   ├── 01-databases-and-the-ledger.html  # 36.5 KB
│   │   └── 02-streaming-data-event-driven-architecture.html  # 213.7 KB
│   ├── infra-ops/
│   │   ├── index.html
│   │   └── 01-cloud-native-operations.html   # 37.3 KB
│   ├── security-risk/
│   │   ├── index.html
│   │   └── 01-security-identity-regulators.html  # 47.1 KB
│   ├── leadership/
│   │   ├── index.html
│   │   ├── 01-architecture-decision-frameworks.html  # 31.8 KB
│   │   └── 02-vendor-management-and-programme-delivery.html  # 36.1 KB
│   └── assets/
│       ├── css/style.css              # dark theme + notes UI + print stylesheet
│       ├── js/main.js                 # mermaid init, right-rail TOC, sidebar search
│       ├── js/notes.js                # highlight + notes feature
│       └── vendor/mermaid.min.js      # 3.3 MB vendored copy
└── bfsi_bible_src/                    # Python generator
    ├── __init__.py
    ├── site.py                        # HTML helpers + page shell + writer
    ├── generate.py                    # orchestrator entry point
    └── topics/
        ├── __init__.py
        ├── foundations_01_transactions.py  # older complete I.1 source retained
        ├── foundations_01_transactions_v2.py  # active May 2026 deep rewrite, sections 0–10 complete
        ├── foundations_01_part2.py    # sections 4 & 5 of I.1 (split for token budget)
        ├── foundations_01_part3.py    # sections 6–10 of I.1 (split for token budget)
        ├── foundations_02_seven_layers.py
        ├── foundations_03_cloud.py
        ├── foundations_04_network.py
        ├── application_stack_01_apis.py
        ├── application_stack_02_microservices.py
        ├── data_01_databases.py
        ├── data_02_streaming.py
        ├── infra_ops_01_cloud_native.py
        ├── security_risk_01_security_identity.py
        ├── bfsi_platforms_01_core_banking.py
        ├── bfsi_platforms_02_payments_engines.py
        ├── bfsi_platforms_03_lending.py
        ├── bfsi_platforms_04_capmkts_insurance.py
        ├── leadership_01_architecture_decisions.py
        └── leadership_02_vendor_programme.py
```

**Naming convention.** `<part_folder>_<NN>_<slug>.py`, e.g. `application_stack_01_apis.py`. Use a single file per topic unless it would exceed the assistant's per-message token budget — only then split into `_part2.py`, `_part3.py` (see I.1 for the pattern).

---

## 4. How to build & run

```powershell
# Regenerate the site (from the project root)
python -m bfsi_bible_src.generate

# Serve locally for browser preview
python -m http.server 8765 --directory bfsi_bible
# Then open http://localhost:8765
```

**Python 3.12.** No third-party Python deps. Mermaid is vendored at `bfsi_bible/assets/vendor/mermaid.min.js`.

**Note on this Windows machine:** the bare `python` / `python3` aliases route to the Microsoft Store stub. The real interpreter is at
`C:\Users\gazer\AppData\Local\Programs\Python\Python312\python.exe`. Use that explicitly, e.g.
`& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" -m bfsi_bible_src.generate`.

---

## 5. Site features (current state)

### 5.1 Visual / UX
- **Dark theme**, palette in CSS variables at top of `style.css`.
- **Three-column layout** at ≥1500 px — sidebar (with search), content, right-rail mini-TOC.
- Difficulty pills on every H2.
- Glossary terms render as `<span class="term" data-tip="…">` with hover tooltips.
- Mermaid diagrams in a custom dark theme matching the palette.

### 5.2 Notes & highlights (`notes.js`)
- Select any text in the content area → floating popover with **4 highlight colours + Add Note**.
- Click any highlight to jump to its note in the side panel.
- Side panel toggle: floating bottom-right button or **Ctrl+Shift+H**.
- Per-card actions: scroll-to-highlight ↗, cycle colour ●, delete 🗑.
- **Export / Import** all notes as JSON, schema-versioned (`bfsi-bible-notes/1`).
- Persistence model: `localStorage` key `bfsi-notes::<path>`, anchor by `(text, occurrenceIndex)` so notes survive minor content edits.
- **Highlights survive print** (rendered in light yellow); the rest of the notes UI is hidden in print.

### 5.3 Print to PDF
The print stylesheet flips to a white background, hides nav and notes UI. Chrome/Edge → Print → Save as PDF gives a clean handout.

---

## 6. Critical decisions and lessons learned

### 6.1 Mermaid renderer quirks (high-stakes)

- **Never put `;` inside sequenceDiagram message text.** Mermaid treats `;` as a statement terminator. Use commas or "and". Caught this after two rounds of "Syntax error in text".
- **Never put `( )` inside `participant X as <alias>` aliases.** Sequence-diagram parser breaks.
- Always emit Mermaid blocks as `<div class="mermaid">…</div>` (Mermaid's documented selector). Avoid `<pre>` — same content, more whitespace edge cases.
- **Do not HTML-escape Mermaid source.** Mermaid reads `textContent`, escaping introduces ambiguities with arrows and brackets.
- The helper `mermaid(code, caption)` in `site.py` already does the right thing. Just don't wrap it in things that escape.

### 6.2 Other technical decisions

- **No templating engine.** Composable Python helper functions emit HTML. Keeps everything trivially debuggable and one-file-per-topic.
- **Output is a static site.** No JS framework, no build step beyond `python -m bfsi_bible_src.generate`.
- **Sidebar is rendered statically per page** with the right `root_rel` for the depth — see `page_shell()` in `site.py`.
- **Notes feature is self-contained**, no dependencies, defers to `localStorage`. Don't replace with a server backend without explicit ask — the user values offline portability.

### 6.3 Pitfalls to avoid in the Python source

- **Trailing commas in `body = ( ... )` blocks turn `body` into a 1-tuple** and crash `to_html()` with `expected str instance, tuple found`. Triple-check every section's closing parenthesis.
- The Python helpers in `site.py` (`p, ul, ol, kv, table, callout, primer, ...`) all return strings; chain them with `+`.
- `mermaid()` does NOT escape its input; treat input as trusted author-controlled.
- `escape()` from `html` module IS called in `H2()`, `H3()`, `term()`, table cells via `escape()`, and similar — don't double-escape.

### 6.4 Build / generator decisions

- Topic files live under `bfsi_bible_src/topics/<file>.py` and export a single `build() -> TopicPage`.
- `generate.py` imports each topic, registers it in `build_index()` (sidebar) and in `main()` (output path + prev/next links).
- When a topic file would exceed an assistant's single-message budget, split into `*_part2.py`, `*_part3.py` and call them from the main file (see I.1 pattern).

---

## 7. Status — what's done and what's next

### 7.1 Done at full depth (locked pedagogy, geographic balance, latest info)

| Code  | Topic                                                  | Status        |
|-------|--------------------------------------------------------|---------------|
| I.1   | How a digital banking transaction actually flows       | ✅ v2 rewrite complete, 230.6 KB |
| I.2   | The seven-layer mental model of any digital bank       | ✅ 27.5 KB    |
| I.3   | Cloud, on-prem, and hybrid for BFSI                    | ✅ 27.9 KB    |
| I.4   | Network fundamentals for BFSI (TLS, mTLS, zero trust)  | ✅ 41.3 KB    |
| II.1  | APIs and integration — REST, gRPC, GraphQL, ISO 20022  | ✅ 51.2 KB    |
| II.2  | Microservices, monoliths, and Domain-Driven Design     | ✅ 39.2 KB    |
| III.1 | Databases and the bank's ledger (OLTP + lakehouse)     | ✅ 36.5 KB    |
| III.2 | Streaming data & event-driven architecture (Kafka, Flink) | ✅ complete, 213.7 KB |
| IV.1  | Cloud-native operations — K8s, observability, SRE, FinOps | ✅ 37.3 KB    |
| IV.2  | DevOps + SRE deeper — CI/CD, IaC, platform engineering, DORA | ✅ complete |
| V.1   | Security, identity, and the global regulator landscape | ✅ 47.1 KB    |
| V.2   | Fraud, AML, and sanctions in operational depth       | ✅ complete |
| VI.1  | Core banking platforms                                 | ✅ 24.1 KB    |
| VI.2  | Payments engines — Volante, Form3, ACI, Finastra      | ✅ 44.6 KB    |
| VI.3  | Lending & originations — LOS, LMS, decisioning, collections | ✅ 56.7 KB, includes HCLTech BA app field guide |
| VI.4  | Capital markets & insurance platforms                  | ✅ 38.6 KB    |
| VII.1 | Architecture decision frameworks                       | ✅ 31.8 KB    |
| VII.2 | Vendor management & large-programme delivery           | ✅ 36.1 KB    |

### 7.2 Planned next — core complete, stretch in progress

All originally planned core topics (I.1–III.1, IV.1, V.1, VI.1–VI.4, VII.1–VII.2) have shipped at least once. Stretch topics I.4 (network), III.2 (streaming), IV.2 (DevOps/SRE deep), and V.2 (Fraud/AML/sanctions deep) are now complete. The next recommended work item is **start stretch topic VI.5 — Cards & switches (Visa/Mastercard/RuPay flows in depth)**.

### 7.3 Stretch (after the above core)

- IV.2 — DevOps + SRE deeper.
- V.2 — Fraud, AML, and sanctions in operational depth.
- VI.5 — Cards & switches (Visa/Mastercard/RuPay flows in depth).
- VII.3 — Communicating with regulators and boards.

---

## 8. Latest-information cross-check (current as of late 2024 / early 2026)

When writing new topics, verify these and add anything newer the model knows:

- **EU DORA** — in force from **17 January 2025**.
- **EU AI Act** — in force **August 2024**, phased applicability to **August 2026**.
- **EU Cyber Resilience Act** — adopted 2024.
- **NIS2 directive** — applies from October 2024.
- **NIST CSF 2.0** — published Feb 2024.
- **NIST PQC final standards** — ML-KEM, ML-DSA, SLH-DSA published Aug 2024.
- **UK Critical Third Parties (CTP) regime** under FSMA 2023 — active.
- **UK FCA Consumer Duty** — Jul 2023; Operational Resilience fully embedded Mar 2025.
- **UK FCA APP fraud reimbursement** — mandatory from Oct 2024.
- **AWS European Sovereign Cloud** — Brandenburg, online 2025.
- **Broadcom-VMware** licensing changes — 2024 onwards.
- **SWIFT MT → ISO 20022** cross-border cutover — November 2025 for cross-border CBPR+.
- **EU Instant Payments Regulation (IPR)** — adopted 2024.
- **FedNow** — live since July 2023.
- **RBI IT Governance MD** — Nov 2023.
- **RBI Outsourcing of IT Services MD** — Apr 2023.
- **RBI Digital Lending Guidelines** — Sep 2022, amendment 2024.
- **RBI Storage of Payment Data** — Apr 2018 (still in force, often re-emphasised).
- **DPDP Act 2023** (India) — rules being notified through 2024–25.
- **India CBDC (e₹)** — retail and wholesale pilots ongoing.
- **MAS FEAT principles** for AI in finance.
- **Singapore GXS / Trust** — operational; **JPM Chase UK** on Vault Core.

If the model knows of something newer, prefer the newer fact.

---

## 9. How to continue in a fresh chat — exact handover script

Paste this verbatim at the start of a new chat with the workspace open:

> Continue building the BFSI Tech Bible. Read `HANDOVER.md` at the project root; it has the locked pedagogy, the file layout, build commands, the Mermaid quirks I learned the hard way, and the planned next-work list. Pick up at section 7.2: start stretch topic VI.5 — Cards & switches (Visa/Mastercard/RuPay flows in depth) — at the same zero-assumption, geographically balanced pedagogy as the completed deep topics. Build the new topic in two-section increments, wire it into `generate.py` and the sidebar, regenerate, and confirm the build is green. Do not ask permission for small decisions — implement and inform.

Then for each turn just say **"continue"**.

---

## 10. Cascade memory note

A persistent Cascade memory titled **"Study-material pedagogy & format preference"** (corpus: `c:/Users/gazer/Downloads/hcl tech cloud`) carries the same pedagogy in semi-formal form. New chats with the same workspace should auto-load it. **This file is the source of truth** if there is any conflict — it is human-readable and version-controllable.

---

## 11. Open questions for the user (parked, not blocking)

These can be addressed when convenient; they do not block continuing topic production.

1. **Search across notes.** Should the side-panel search the *content* of saved notes too?
2. **Topic-level reading-time estimate.** Show "≈ 18 min read" near the H1?
3. **Anki-style flashcard export.** Auto-generate flashcards from each topic's glossary?
4. **Single-file PDF.** Generate one combined PDF of the whole bible for offline reading?
5. **Self-test quiz at end of each topic.** 5–10 multiple-choice questions auto-graded in the browser?

If any of these become a priority, they slot cleanly into the current architecture.
