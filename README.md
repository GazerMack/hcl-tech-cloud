# BFSI Techno-Functional Leader Bible

A self-contained reference taking an MBA-Finance professional from zero IT background to fluent senior techno-functional leader in BFSI (Banking, Financial Services, Insurance). Built specifically for HCLTech BFSI engagements (Citi, Standard Chartered, Deutsche Bank, Barclays, NatWest, JPM, etc.).

## Folder layout

```
hcl tech cloud/
  bfsi_bible/            # generated HTML site — this is the bible itself
  bfsi_bible_src/        # Python generator
    topics/              # one module per topic (foundations_01_*.py …)
    site.py              # HTML helpers and page shell
    generate.py          # orchestrator entry point
  README.md
```

## Read the bible

Open `bfsi_bible/index.html` in any modern browser. Works fully offline — Mermaid, CSS, and JS are vendored.

### Highlight & take notes
- Select any text in the content area → a popover offers four highlight colours and an **Add Note** button.
- Click any highlight to jump to its note in the side panel.
- Click the floating notebook icon (bottom-right) or press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>H</kbd> to open the panel.
- Notes persist locally in the browser (via `localStorage`, scoped per page).
- Use the panel's **Export** / **Import** buttons to back up or move your notes between machines.
- Highlights are kept (in yellow) when you Print → Save as PDF; the notes UI is hidden.

### Print to PDF
Open any page in Chrome / Edge → Print → Save as PDF. The print stylesheet flips to a clean white layout and hides navigation.

## Current coverage

The core curriculum is complete, and stretch Topic I.4 is included:

- **Foundations:** transactions, seven-layer model, cloud/hybrid infrastructure, network fundamentals.
- **Application stack:** APIs/integration, microservices/monoliths/Domain-Driven Design.
- **Data:** databases and the bank's ledger.
- **Infrastructure & operations:** cloud-native operations, Kubernetes, observability, Site Reliability Engineering, FinOps.
- **Security, risk & compliance:** identity, cryptography, regulators, operational resilience.
- **BFSI platforms:** core banking, payments engines, lending/originations, capital markets and insurance.
- **Leadership lenses:** architecture decision frameworks, vendor management and programme delivery.

## Regenerate

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" -m bfsi_bible_src.generate
```

Re-run after editing any topic module under `bfsi_bible_src/topics/`.

## Dependencies

Python 3.12 only. No third-party Python packages required for the HTML build. Mermaid is vendored in `bfsi_bible/assets/vendor/`.
