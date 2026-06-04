"""BFSI Domain Platforms · 01 — Core banking platforms (the engines that hold the money)."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="VI.1",
        slug="01-core-banking-platforms",
        title="Core banking platforms — the engines that hold the money",
        one_liner=("Every retail and commercial bank in the world runs a Core Banking System "
                   "(CBS) — the single source of truth for accounts, balances, products and "
                   "general ledger postings. Five vendor families dominate the global market "
                   "and three cloud-native challengers are reshaping the next decade. After "
                   "this topic you can name them, place them, and read any vendor pitch."),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("If a bank had only one piece of software, it would be the core banking system. "
              "It is the ledger plus the product catalogue plus the daily-batch engine. Any "
              "BFSI architect who cannot name the major core banking platforms loses "
              "credibility in week one.")
        )
        + H3("0.1  IT-side anchor — the laptop’s ‘Files’ app")
        + it_anchor(
            p("Imagine your laptop’s file system: it tracks what files exist, who owns them, "
              "their size, when they were modified. A core banking system tracks the same "
              "things for accounts: which accounts exist, who owns them, what is the balance, "
              "when was the last transaction. Every other app on the laptop ultimately reads "
              "and writes through the file system. Every other system in the bank ultimately "
              "reads and writes through the core banking system.")
        )
        + H3("0.2  BFSI-side anchor — what you already see")
        + bfsi_anchor(
            p("When you log in to HDFC NetBanking and see your balance — that number was just "
              "fetched from Finacle (HDFC’s core banking system, made by Infosys). When you "
              "see your Citi balance — Citi runs a mix including FIS Profile and an internal "
              "platform. When you see your Standard Chartered balance — eBBS, a custom-built "
              "core globally being rationalised. The number you see is the core banking "
              "system’s answer.")
        )
    )
    return TopicSection("0.  Primer — anchored to things you already know", "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("A core banking system answers four questions, all the time:")
        + ol([
            "<strong>Who owns the money?</strong> The customer master and account master.",
            "<strong>How much is there?</strong> The balance, derived from the ledger of "
            "every debit and credit ever posted, plus interest accruals.",
            "<strong>What product is this?</strong> Savings, current, fixed deposit, recurring "
            "deposit, loan, credit card, NRO, NRE, FCNR, mortgage — each with its own rules "
            "for interest, fees, taxes, dormancy, statement cycles.",
            "<strong>What did we book to the General Ledger (GL)?</strong> Each transaction "
            "produces GL entries that roll up to the bank’s P&amp;L and balance sheet daily.",
        ])
        + p("Everything else — channels, fraud, AML, payments rails, lending workflows, "
            "analytics — orbits around the core. That is why migrating a core takes 3–10 "
            "years and is the highest-risk programme any bank ever runs.")
    )
    return TopicSection("1.  What a core banking system actually does", "basic", body)


def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart TB\n'
            '  subgraph Channels\n'
            '    M[Mobile / Internet] --> API\n'
            '    BR[Branch / ATM] --> API\n'
            '    P[Partners / UPI] --> API\n'
            '  end\n'
            '  API[API & integration layer] --> CBS\n'
            '  subgraph CBS["Core Banking System"]\n'
            '    CM[Customer master]\n'
            '    AM[Account master]\n'
            '    PM[Product engine]\n'
            '    TX[Transaction & posting]\n'
            '    GL[General Ledger]\n'
            '    EOD[End-of-day batch]\n'
            '  end\n'
            '  CBS --> RAILS[Payments rails]\n'
            '  CBS --> RISK[Risk, fraud, AML]\n'
            '  CBS --> DW[Data warehouse]\n'
            '  CBS --> REG[Regulatory reporting]',
            "What sits around a core banking system.")
    )
    return TopicSection("2.  The shape of any CBS deployment", "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  The five global incumbents")
        + table(
            ["Vendor / product", "Origin", "Sweet spot", "Notable customers"],
            [
                ["<strong>Finacle</strong> (Infosys / EdgeVerve)", "India",
                 "Universal banking at scale, especially India and Asia; one of the world’s "
                 "most-deployed cores.",
                 "ICICI, Axis, IDBI, IDFC FIRST, RBL, EmiratesNBD, ANZ in parts; ~100 country "
                 "deployments."],
                ["<strong>Flexcube</strong> (Oracle)", "India / Citicorp Overseas (i-flex)",
                 "Strong in MENA and Asia; tightly integrated with Oracle Database; modular.",
                 "HDFC (legacy parts), Yes Bank, several Citi entities; many tier-2 banks."],
                ["<strong>TCS BaNCS</strong>", "India",
                 "Banking + capital markets + insurance suite; strength in custody and "
                 "securities; extending into payments.",
                 "SBI (the world’s largest CBS deployment by accounts), BoB, RBI’s e-Kuber, "
                 "many central banks."],
                ["<strong>Temenos T24 / Transact</strong>", "Switzerland",
                 "International tier-1 and tier-2; broadest functionality; strong in Europe, "
                 "Africa, LATAM; growing cloud (Temenos Banking Cloud).",
                 "HSBC parts, Standard Chartered parts, Nedbank, Itaú parts, EFG, ADIB."],
                ["<strong>FIS Profile / FIS Modern Banking Platform</strong>", "United States",
                 "Strong in US mid-tier and credit unions; FIS also owns IST/Switch (cards), "
                 "ACH and many other engines.",
                 "Hundreds of US community / regional banks; some tier-1 wholesale."],
            ]
        )
        + H3("3.2  The cloud-native challengers (next-gen cores)")
        + table(
            ["Vendor", "Origin / year", "Differentiator"],
            [
                ["<strong>Mambu</strong>", "Germany / 2011",
                 "True SaaS, API-first composable; popular for BNPL, fintech, neobanks "
                 "(N26 launched on Mambu, GXS Bank Singapore, Western Union ‘Digital Bank’)."],
                ["<strong>Thought Machine — Vault Core</strong>", "United Kingdom / 2014",
                 "Smart-contract-based product engine; deployed at Lloyds, Standard Chartered "
                 "Mox (Hong Kong) / Trust (Singapore), JPM Chase UK, ING."],
                ["<strong>10x Banking</strong>", "United Kingdom / 2016",
                 "Cloud-native; chosen by Westpac (Australia), Chase (UK launch), Bank of "
                 "London."],
                ["<strong>FIS Modern Banking Platform</strong>", "United States / 2018",
                 "FIS’s cloud-native answer alongside the legacy Profile; targeted at digital "
                 "challengers and regional banks."],
                ["<strong>Tuum, Vilja, SaaScada, Five Degrees</strong>", "Europe (various)",
                 "Smaller cloud-native cores; growing among European tier-3 and embedded-"
                 "finance plays."],
            ]
        )
        + H3("3.3  The mainframe holdouts")
        + p("Several US tier-1 banks and a few internationals run core banking on IBM Z "
            "mainframes with internally maintained applications, often written in COBOL and "
            "PL/I, married to IBM Db2 or IMS for the data layer. JPM Chase, Wells Fargo, BoA, "
            "Citi (parts), BoB India, SBI, Lloyds (parts), and others. Modernisation here "
            "rarely means ‘replace’; it means ‘encapsulate behind APIs and surround’.")
    )
    return TopicSection("3.  The vendor landscape — current as of 2025",
                        "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  Architecture — monolith with batch heart vs cloud-native composable")
        + p("Older cores (Flexcube, Finacle, T24, FIS Profile) are typically large monoliths "
            "with a strong relational database (Oracle, Db2) and a heavy <strong>End-of-Day "
            "(EOD) batch</strong>: every night, the system stops accepting new business for "
            "30–120 minutes while it accrues interest, computes statements, posts GL entries, "
            "and prepares regulatory files. Cloud-native cores remove the ‘offline batch’ in "
            "favour of continuous processing and event sourcing.")
        + H3("4.2  Data architecture")
        + ul([
            "<strong>Customer master</strong> — single record per customer, often hub-and-"
            "spoke with a separate Master Data Management (MDM) tool (Reltio, Informatica MDM, "
            "Stibo).",
            "<strong>Account master</strong> — one record per account; an account is always "
            "owned by exactly one product.",
            "<strong>Transaction store</strong> — append-only ledger of debits / credits with "
            "value date, posting date, channel, narrative.",
            "<strong>GL</strong> — chart of accounts and daily roll-up; consumed by Finance "
            "and regulator reporting.",
        ])
        + H3("4.3  Modularity and the ‘composable banking’ shift")
        + p("Modern cores expose every product as a smart contract or service: ‘savings "
            "account v3.4’ is a deployable unit you can A/B test. This is the core idea "
            "behind Thought Machine Vault and 10x. Composable banking lets banks ship a new "
            "deposit product in weeks instead of quarters; the price is a steeper "
            "engineering culture and operational maturity bar.")
        + H3("4.4  Real-time and 24×7")
        + p("Until 2015, almost all core banking systems had nightly downtime. Today the "
            "expectation — driven by UPI, FedNow, FPS, SCT Inst, NPP, PIX — is 24×7 with "
            "online posting. The ‘instant payments revolution’ has forced incumbent cores to "
            "split EOD work into rolling micro-batches, decouple GL posting, and hold hot "
            "balances in memory caches. RBI’s 24×7 NEFT (Dec 2019) and 24×7 RTGS (Dec 2020) "
            "specifically forced Indian banks down this path.")
    )
    return TopicSection("4.  How a CBS is actually built — architecture",
                        "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  Core migration — the most-feared programme in BFSI")
        + p("Replacing a core is the highest-risk thing a bank can do. Every successful "
            "migration uses one of three patterns:")
        + ul([
            "<strong>Big bang</strong> — flip the switch on a weekend. Almost never used at "
            "tier-1 today; reserved for very small institutions.",
            "<strong>Phased by branch / portfolio</strong> — migrate a region or a product at "
            "a time. Used by SBI for the BaNCS deployment, by Bank of Baroda after merger.",
            "<strong>Strangler fig (the modern default)</strong> — stand up a new core, route "
            "new accounts and new products there, leave legacy accounts on the old core, "
            "migrate them over months / years. Used by JPM Chase UK (Thought Machine), "
            "Lloyds, Standard Chartered Mox / Trust.",
        ])
        + H3("5.2  Reconciliation and dual-running")
        + p("During migration, a bank runs two cores in parallel and reconciles balances and "
            "GL postings every night. The dual-run period is typically 6–18 months for the "
            "initial cohort; for stragglers (dormant accounts, old loans), it can be years.")
        + H3("5.3  Cloud and the regulator")
        + p("Putting the CBS on public cloud is the single most-scrutinised cloud decision a "
            "bank makes. Regulators commonly require: in-country region, exit plan, BYOK or "
            "EKM for keys, dual-region resilience, audit rights to the cloud provider, and "
            "evidence of TLPT / TIBER-EU testing. Singapore’s GXS and Trust banks are good "
            "case studies (CBS on cloud from day one); JPM Chase UK is the best big-bank case "
            "study (Vault Core on the public cloud, MAS / FCA / OCC alignment).")
        + H3("5.4  AI in the core")
        + p("Generative AI is creeping into the periphery (developer copilots, customer-"
            "service summarisation, document understanding for KYC) but not into the posting "
            "engine itself — model risk frameworks (Fed SR 11-7, RBI’s 2024 draft, EU AI Act) "
            "do not yet permit non-deterministic decisioning of debits and credits. Expect "
            "this to remain so for years.")
    )
    return TopicSection("5.  Advanced — the things senior architects argue about",
                        "advanced", body)


def _sec6() -> TopicSection:
    body = (
        p("CBS choice is heavily shaped by regulator expectations and local talent pools.")
        + table(
            ["Region", "Typical CBS landscape", "Regulator angles"],
            [
                ["India",
                 "Finacle, BaNCS, Flexcube dominate. New small finance banks and digital banks "
                 "experimenting with Mambu, FIS, Thought Machine.",
                 "RBI Master Direction on IT Governance Nov 2023, Storage of Payment Data Apr "
                 "2018, Outsourcing of IT Services Apr 2023, Digital Lending 2022 + 2024 "
                 "amendment."],
                ["United States",
                 "Tier-1: in-house mainframe + FIS / Fiserv. Tier-2: Jack Henry, FIS, Fiserv. "
                 "Digital: FIS Modern, Mambu, Q2.",
                 "OCC heightened standards, FFIEC IT Handbook, NYDFS Part 500, Reg E."],
                ["United Kingdom",
                 "Lloyds and Chase UK on Thought Machine; HSBC parts on Temenos; legacy "
                 "challengers on Mambu / Thought Machine / 10x.",
                 "PRA SS1/21, FCA SYSC, Operational Resilience policy fully embedded Mar 2025, "
                 "CTP regime under FSMA 2023."],
                ["Eurozone",
                 "Temenos and Avaloq prevalent; Sopra Banking Software and FIS in parts; "
                 "Mambu / Thought Machine for neobanks.",
                 "ECB SSM, EBA outsourcing guidelines, DORA from 17 Jan 2025."],
                ["Singapore / SE Asia",
                 "Strong cloud-native posture: Mambu (GXS), Thought Machine (Trust), Temenos. "
                 "Incumbents on TCS BaNCS / Flexcube.",
                 "MAS Outsourcing Guidelines, MAS Notice 658 BCM, MAS TRM."],
            ]
        )
    )
    return TopicSection("6.  Region-by-region CBS landscape", "advanced", body)


def _sec7() -> TopicSection:
    return TopicSection(
        "7.  Decision matrix — choosing or replacing a CBS", "intermediate",
        table(
            ["Situation", "Recommended direction"],
            [
                ["Greenfield digital bank, single market",
                 "Cloud-native (Mambu / Thought Machine / 10x). Fastest go-live, lowest TCO."],
                ["Tier-1 incumbent, multi-country, complex products",
                 "Strangler-fig migration. Buy a cloud-native core for new products and "
                 "geographies, surround the legacy with APIs, migrate cohorts over years."],
                ["Tier-2 retail bank, single country",
                 "A modern instance of an incumbent vendor (Finacle / BaNCS / T24) on cloud or "
                 "private cloud is usually the safest pragmatic choice."],
                ["US community bank or credit union",
                 "Jack Henry, FIS, or Fiserv as a hosted offering. Cloud-native is gaining but "
                 "ecosystem and rail integration favour incumbents."],
                ["Niche product launch (BNPL, gig payouts, embedded finance)",
                 "Mambu or 10x layered atop the existing core; do not re-platform the core for "
                 "a niche."],
                ["Insurance or capital markets, not retail banking",
                 "Different vendors entirely (Guidewire, Sapiens for P&amp;C; Murex / Calypso "
                 "for capital markets; Avaloq / Temenos Wealth for wealth)."],
            ]
        )
    )


def _sec8() -> TopicSection:
    body = (
        example("JPMorgan Chase UK — launching on Vault Core",
            p("Chase UK launched September 2021 on Thought Machine’s Vault Core, running on "
              "AWS. Within two years it had > 1 million customers and £15 bn in deposits "
              "(reported figures). Lessons: greenfield + cloud-native + smart-contract product "
              "engine compresses time-to-market; but operational scale brings new "
              "reconciliation and capacity-planning challenges that the incumbent stack had "
              "decades to learn.")
        )
        + example("HDFC Bank — Finacle modernisation",
            p("HDFC has been running Finacle for two decades; outage events in 2020–2021 "
              "drew RBI scrutiny and led to a multi-year tech-transformation programme. "
              "The pattern is incumbent (Finacle) at the core with selective cloud-native "
              "modernisation around it — channels, data, fraud, lending workflows — rather "
              "than a core replacement.")
        )
        + example("Standard Chartered — Mox (Hong Kong) and Trust (Singapore)",
            p("Both launched on cloud-native stacks distinct from SCB’s global eBBS legacy. "
              "Mox uses Thought Machine; Trust runs on Mambu + AWS in Singapore. Pattern: "
              "use greenfield licences to learn cloud-native operations on a small scale, "
              "then export the playbook to the mothership. HCLTech is among the partners "
              "delivering parts of SCB’s broader cloud-first programme.")
        )
        + example("SBI — TCS BaNCS at maximum scale",
            p("State Bank of India runs TCS BaNCS over hundreds of millions of accounts — "
              "by transaction volume one of the largest CBS deployments on earth. Architecture "
              "lessons: aggressive sharding, near-line caches for hot balances, separation of "
              "channel front from posting engine, very mature batch operations. ‘Cloud-native’ "
              "in this context means running BaNCS on private cloud and OCI, not replacing it.")
        )
    )
    return TopicSection("8.  Worked examples — four real CBS journeys",
                        "intermediate", body)


def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘Let’s replace the core — it’s the root cause of everything slow.’ — In 9 cases "
            "out of 10, the slowness is in channels, integration, or reporting. Replacing the "
            "core is a 5–10 year, 9-figure programme; it must be justified by product and "
            "geographic strategy, not by a recent incident.",
            "‘Cloud-native cores are unproven.’ — Vault Core, Mambu, 10x have meaningful "
            "production scale at JPM, ING, Chase UK, Westpac, GXS, Trust. They are no longer "
            "experimental.",
            "‘We can do EOD-less by adding a cache.’ — A read-side cache does not eliminate "
            "EOD; only re-architecting the posting engine and GL does.",
            "‘Composable banking means microservices.’ — It means contractually separable "
            "products with their own lifecycles. Microservices are an implementation choice; "
            "composability is a product design principle.",
            "‘The CBS vendor’s sales deck shows X TPS, so we are fine.’ — Vendor benchmarks "
            "are clean-sheet. Real production performance under your transaction mix is "
            "typically 30–60% of benchmark; insist on a Proof of Value (PoV) on your data.",
            "‘We don’t need to talk to the regulator until we go live.’ — RBI, MAS, FCA, ECB, "
            "OCC all expect early engagement on any CBS replacement; surprising them at UAT "
            "is a guaranteed delay.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("CBS", "Core Banking System — the central ledger, customer master, account "
             "master, product engine and GL posting engine of a bank."),
            ("EOD batch", "End-of-day batch — historic nightly window during which the core "
             "accrues interest, posts GL, and produces files. Modern cores compress or "
             "eliminate this."),
            ("GL", "General Ledger — the bank’s chart of accounts; every transaction in the "
             "core posts to one or more GL accounts."),
            ("MDM", "Master Data Management — keeping a single, consistent customer / party / "
             "product master across the bank."),
            ("Composable banking", "Architecture where each product is a separately deployable "
             "service or smart contract, allowing rapid product launches."),
            ("Strangler fig", "Migration pattern where new functionality is built outside the "
             "legacy and gradually replaces it; named by Martin Fowler."),
            ("Vault Core", "Thought Machine’s cloud-native core; uses smart contracts to "
             "express products."),
            ("Mambu", "German cloud-native core widely adopted by neobanks and lenders."),
            ("BaNCS", "TCS’s integrated banking + capital-markets + insurance product."),
            ("Finacle", "Infosys (EdgeVerve) universal core banking platform."),
            ("Flexcube", "Oracle’s core banking product, originally from i-flex."),
            ("Profile / Modern Banking Platform", "FIS’s legacy and cloud-native cores."),
            ("PoV", "Proof of Value — a time-boxed pilot against your real data and use cases; "
             "always require one before a multi-year CBS commitment."),
            ("Mainframe", "IBM Z (or older System z) hardware running COBOL / PL/I and Db2 / "
             "IMS; still hosting tier-1 cores at JPM, BoA, Wells, Citi parts, SBI parts."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
