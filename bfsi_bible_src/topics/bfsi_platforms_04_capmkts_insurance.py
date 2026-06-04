"""BFSI Domain Platforms · 04 — Capital markets and insurance platforms."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="VI.4",
        slug="04-capmkts-and-insurance",
        title="Capital markets and insurance platforms — trading, post-trade, asset management, P&C, life",
        one_liner=(
            "Two adjacent BFSI worlds, often run by the same enterprise, "
            "with very different software estates. Capital markets is the "
            "world of trading, risk and post-trade — Murex, Calypso, "
            "Summit, Aladdin, Charles River, Bloomberg AIM, FIS Front "
            "Arena, ION, Adenza, Broadridge. Insurance is the world of "
            "policy admin, claims, actuarial and reinsurance — Guidewire, "
            "Duck Creek, Sapiens, EIS, Majesco, FINEOS, Prophet, AXIS. "
            "This topic gives you fluent vocabulary across both, the "
            "regulators that shape them, and the design choices a "
            "techno-functional leader makes when modernising either."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("Capital markets and insurance share a common parent — "
              "they manage long-tail financial promises — but their "
              "software estates evolved separately and look very "
              "different. A trading floor runs on millisecond-grade "
              "platforms talking to exchanges and clearing houses. An "
              "insurance back-office runs on multi-year policy and "
              "claims systems talking to actuarial models, reinsurers "
              "and regulators. Both are now under heavy modernisation "
              "pressure for similar reasons: cloud, AI, and a "
              "regulator stack that has rewritten itself in the last "
              "three years.")
        )
        + H3("0.1  IT-side anchor — two factories with different cycle times")
        + it_anchor(
            p("A factory that builds smartphones runs on minute-by-"
              "minute discipline; a factory that builds aircraft "
              "runs on month-by-month discipline. Both are "
              "factories, both have inventory and quality control "
              "and supply chains, but you don’t buy one set of "
              "software for both. <strong>Capital markets is the "
              "smartphone factory</strong>: high frequency, low "
              "latency, every millisecond visible. <strong>Insurance "
              "is the aircraft factory</strong>: 30-year contracts, "
              "actuarial reserves, regulator-blessed assumptions. "
              "Same company can own both; you still buy two "
              "different stacks.")
        )
        + H3("0.2  BFSI-side anchor — the trade and the policy")
        + bfsi_anchor(
            p("When a hedge fund buys £10m of a UK gilt, the trade "
              "passes through an Order Management System (OMS), an "
              "Execution Management System (EMS), an exchange or "
              "RFQ venue, a clearing house, a custodian, and dozens "
              "of risk and reporting steps inside the bank — all in "
              "seconds. When you buy a 25-year term life policy, "
              "the application passes through a quote engine, an "
              "underwriting platform, a policy admin system, an "
              "actuarial reserving engine, a reinsurance platform "
              "and a claims system over decades. Both stories live "
              "inside the same multi-line BFSI group.")
        )
        + H3("0.3  Capital markets in five product blocks")
        + ul([
            "<strong>Equities</strong> — cash equities, ETFs, "
            "single-stock derivatives.",
            "<strong>Fixed income</strong> — government and "
            "corporate bonds, repo, money markets.",
            "<strong>FX and rates</strong> — spot, forwards, swaps, "
            "options.",
            "<strong>Credit and structured</strong> — credit "
            "derivatives, securitised products, structured notes.",
            "<strong>Commodities</strong> — energy, metals, "
            "agricultural; physical and financial.",
        ])
        + H3("0.4  Insurance in three lines of business")
        + ul([
            "<strong>Property &amp; Casualty (P&amp;C, also "
            "‘General Insurance’)</strong> — auto, home, "
            "commercial, marine, aviation, cyber.",
            "<strong>Life &amp; Annuities (L&amp;A)</strong> — "
            "term life, whole life, universal life, annuities, "
            "savings products with insurance wrappers.",
            "<strong>Health and reinsurance</strong> — health "
            "insurance, group benefits, and the reinsurers (Munich "
            "Re, Swiss Re, Hannover Re, Lloyd’s syndicates) that "
            "back the primary insurers.",
        ])
    )
    return TopicSection(
        "0.  Primer — capital markets and insurance, said briefly",
        "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Why are both estates being modernised right now?")
        + ol([
            "<strong>Regulator pressure on resilience.</strong> EU "
            "DORA covers both; UK FCA Operational Resilience and "
            "PRA SS2/21 outsourcing apply equally; Solvency II "
            "(insurance) and FRTB / Basel 3.1 (banks) require new "
            "data depth.",
            "<strong>T+1 settlement.</strong> US, Canada, Mexico "
            "moved to T+1 on 28 May 2024; UK and EU are "
            "coordinating a <strong>T+1 migration on 11 October "
            "2027</strong>; India already T+1, moving to T+0. "
            "Post-trade systems must be faster.",
            "<strong>Insurance accounting upheaval.</strong> "
            "<strong>IFRS 17</strong> took effect 1 January 2023 "
            "globally (US uses LDTI under US GAAP). It rewrote "
            "every insurer’s reserving and reporting architecture.",
            "<strong>Cloud-native modernisation.</strong> Murex "
            "MX.3 on cloud, Calypso (now Adenza) on cloud, "
            "Aladdin on Azure, Guidewire Cloud, Duck Creek "
            "OnDemand all push the industry off on-prem.",
            "<strong>AI on long-tail data.</strong> Insurance "
            "claims and underwriting are perfect AI use cases; "
            "capital-markets risk and surveillance are increasingly "
            "ML-driven.",
            "<strong>Crypto and tokenised assets.</strong> "
            "BlackRock BUIDL, JPM Onyx, HSBC Orion, Goldman GS "
            "DAP, Citi Token Services — capital-markets infrastructure is "
            "preparing for tokenised cash and securities.",
        ])
    )
    return TopicSection(
        "1.  Why both estates are under heavy modernisation",
        "basic", body)


def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  subgraph "Capital markets — trade lifecycle"\n'
            '    O["OMS<br/>Charles River, Bloomberg AIM, Aladdin"]\n'
            '    E["EMS<br/>FlexTrade, Bloomberg EMSX, ION"]\n'
            '    V["Venues<br/>exchanges, MTFs, RFQ, dark pools"]\n'
            '    Cl["Clearing and settlement<br/>CCP / custodian / DTCC / Euroclear"]\n'
            '    R["Risk and PnL<br/>Murex, Calypso, Summit"]\n'
            '    Re["Regulatory reporting<br/>EMIR, MiFID II, CAT"]\n'
            '    O --> E --> V --> Cl --> R --> Re\n'
            '  end\n'
            '  subgraph "Insurance — policy and claims lifecycle"\n'
            '    Q["Quote and underwriting<br/>Guidewire, Duck Creek"]\n'
            '    P["Policy admin<br/>PolicyCenter, OnDemand, FINEOS"]\n'
            '    B["Billing"]\n'
            '    Cm["Claims<br/>ClaimCenter, OnDemand Claims"]\n'
            '    Ac["Actuarial and reserving<br/>Prophet, AXIS, MoSes"]\n'
            '    Rn["Reinsurance<br/>SICS, ImageRight, in-house"]\n'
            '    Q --> P --> B\n'
            '    P --> Cm\n'
            '    Cm --> Ac\n'
            '    P --> Ac --> Rn',
            "Two parallel architectures — capital-markets trade "
            "lifecycle and insurance policy/claims lifecycle.")
    )
    return TopicSection(
        "2.  The picture — two lifecycles on one diagram",
        "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  Capital markets — front office (OMS, EMS)")
        + ul([
            "<strong>Order Management System (OMS)</strong> — the "
            "buy-side / sell-side system that holds positions, "
            "cash, and orders. <strong>Charles River IMS</strong> "
            "(SS&amp;C-State Street), <strong>BlackRock "
            "Aladdin</strong>, <strong>Bloomberg AIM</strong>, "
            "<strong>SimCorp Dimension</strong>, <strong>FactSet "
            "Portfolio Lifecycle Management</strong>, <strong>SS&amp;C "
            "Eze Eclipse</strong>, <strong>Enfusion</strong>.",
            "<strong>Execution Management System (EMS)</strong> — "
            "the trader-facing system for execution. "
            "<strong>FlexTrade</strong>, <strong>Bloomberg "
            "EMSX</strong>, <strong>ION Fidessa</strong>, "
            "<strong>Virtu Triton</strong>, <strong>TS Imagine</strong>.",
            "<strong>FIX protocol</strong> — Financial Information "
            "eXchange; the universal language between OMS, EMS, "
            "venues and brokers.",
            "<strong>Algo trading and SOR</strong> — Smart Order "
            "Routing chooses the best venue; algo strategies "
            "(VWAP, TWAP, POV, IS) implemented in C++/Java with "
            "tight latency budgets.",
        ])
        + H3("3.2  Capital markets — middle office and risk")
        + table(
            ["Platform", "Primary use", "Where you’ll see it"],
            [
                ["<strong>Murex MX.3</strong>",
                 "Cross-asset trading, risk and post-trade for sell-"
                 "side and corporate banking; rates, FX, credit, "
                 "commodities, equities.",
                 "BNP Paribas, Standard Chartered, Mizuho, Nomura, "
                 "many tier-1 sell-sides; cloud delivery via "
                 "MX.3 SaaS on AWS."],
                ["<strong>Calypso (now Adenza, owned by "
                 "Nasdaq)</strong>",
                 "Cross-asset capital markets and treasury; "
                 "strong in derivatives and clearing.",
                 "ING, RBC, Mizuho, Lloyds; Adenza merged Calypso "
                 "with AxiomSL in 2021; Nasdaq acquired Adenza "
                 "in 2023."],
                ["<strong>Finastra Summit, Kondor</strong>",
                 "Treasury and capital markets; strong in tier-2 "
                 "European and APAC banks.",
                 "Many tier-2 European banks, several Indian "
                 "banks for treasury."],
                ["<strong>FIS Front Arena, FIS Cleared "
                 "Derivatives, FIS Securities Finance</strong>",
                 "Trading, post-trade, securities finance; broad "
                 "capability across product silos.",
                 "Many sell-side and asset managers; FIS bought "
                 "SunGard 2015 and consolidated several "
                 "platforms."],
                ["<strong>ION (Wall Street Systems, "
                 "Openlink, Fidessa, Allegro)</strong>",
                 "Treasury, FX, commodities, equities; ION "
                 "consolidated many vendors over a decade.",
                 "Tier-1 banks for treasury and FX; ION "
                 "ransomware Jan 2023 was a wake-up call on "
                 "concentration risk."],
                ["<strong>Broadridge</strong>",
                 "Post-trade, proxy services, securities "
                 "processing; Distributed Ledger Repo (DLR) is a "
                 "production tokenised-repo platform.",
                 "Most US broker-dealers for post-trade; growing "
                 "in EU; DLR live with major banks."],
                ["<strong>Bloomberg AIM</strong>",
                 "Buy-side OMS / IBOR; deep integration with the "
                 "Bloomberg Terminal.",
                 "Asset managers, hedge funds, insurance "
                 "investment teams."],
                ["<strong>BlackRock Aladdin</strong>",
                 "End-to-end investment platform — OMS, risk, "
                 "operations; the dominant buy-side platform.",
                 "BlackRock plus 200+ external clients (Allianz, "
                 "Vanguard, MEAG, Prudential, Mitsubishi UFJ "
                 "Asset, AustralianSuper)."],
                ["<strong>SS&amp;C Advent / Eze / Black "
                 "Diamond</strong>",
                 "Wealth and asset management portfolio "
                 "accounting and OMS.",
                 "Mid-market asset managers; family offices."],
                ["<strong>State Street Alpha (incl. Charles "
                 "River)</strong>",
                 "Front-to-back asset-management platform; "
                 "competes with Aladdin.",
                 "State Street custody clients, several large "
                 "asset managers."],
            ]
        )
        + H3("3.3  Capital markets — post-trade and clearing")
        + ul([
            "<strong>Central Counterparties (CCPs)</strong> — "
            "<strong>LCH</strong> (LSEG), <strong>ICE Clear</strong>, "
            "<strong>CME Clearing</strong>, <strong>Eurex "
            "Clearing</strong>, <strong>DTCC FICC / NSCC</strong>, "
            "<strong>JSCC</strong>, <strong>NSCCL / ICCL "
            "(India)</strong>.",
            "<strong>CSDs (Central Securities Depositories)</strong> "
            "— <strong>DTCC</strong> (US), <strong>Euroclear</strong> "
            "and <strong>Clearstream</strong> (EU), <strong>"
            "CDSL / NSDL</strong> (India), <strong>HKSCC</strong>.",
            "<strong>Custodians</strong> — State Street, BNY "
            "Mellon, JPM, Citi, Northern Trust, BNP Paribas, "
            "HSBC; provide safekeeping, corporate actions, "
            "settlement.",
            "<strong>Trade repositories</strong> for derivatives "
            "(EMIR, Dodd-Frank, MAS / ASIC equivalents).",
            "<strong>SWIFT messaging</strong> — securities messages "
            "(MT 5xx, ISO 20022 sese / semt / seev).",
        ])
        + H3("3.4  Capital-markets reporting regimes you must know")
        + ul([
            "<strong>MiFID II / MiFIR (EU + UK)</strong> — best "
            "execution, transaction reporting, transparency; "
            "MiFIR refit in EU 2024 raises bar.",
            "<strong>EMIR / EMIR REFIT (EU)</strong> — derivatives "
            "trade reporting; EMIR REFIT applied 29 Apr 2024.",
            "<strong>SFTR (EU/UK)</strong> — Securities Financing "
            "Transactions Regulation.",
            "<strong>Dodd-Frank Title VII (US)</strong> — swaps "
            "reporting to SDRs (DTCC, ICE).",
            "<strong>CAT (Consolidated Audit Trail, US)</strong> — "
            "every order, route, modification, execution.",
            "<strong>FRTB (Fundamental Review of the Trading "
            "Book)</strong> — Basel III.1 trading-book capital "
            "framework; in force in EU 1 Jan 2025 (revised 2025), "
            "UK 1 Jan 2026, US delayed.",
            "<strong>SEC Rule 17a-4</strong> — broker-dealer "
            "record-keeping; WORM storage.",
        ])
        + H3("3.5  Insurance — the eight platforms an insurer runs")
        + table(
            ["Platform", "Primary use", "Where you’ll see it"],
            [
                ["<strong>Guidewire InsuranceSuite (PolicyCenter, "
                 "ClaimCenter, BillingCenter)</strong>",
                 "P&amp;C policy admin, claims, billing; cloud "
                 "delivery via Guidewire Cloud since 2020.",
                 "Allianz, Zurich, AIG, Liberty Mutual, AXA, "
                 "Generali, Tokio Marine, Suncorp, ICICI Lombard."],
                ["<strong>Duck Creek (Duck Creek "
                 "OnDemand)</strong>",
                 "P&amp;C policy, billing, claims; cloud-native; "
                 "Vista is the legacy on-prem.",
                 "Geico, Berkshire Hathaway, AIG, Munich Re US, "
                 "Aviva."],
                ["<strong>Sapiens IDIT, Sapiens "
                 "ALIS / CoreSuite</strong>",
                 "P&amp;C and L&amp;A policy admin; strong in EU "
                 "and APAC.",
                 "Allianz, AXA, Generali, several Indian "
                 "insurers."],
                ["<strong>EIS (EIS Group)</strong>",
                 "Cloud-native P&amp;C and L&amp;A core insurance "
                 "platform.",
                 "Esure, RAC, Zurich UK, several mid-market US "
                 "insurers."],
                ["<strong>Majesco</strong>",
                 "P&amp;C and L&amp;A SaaS core insurance; strong "
                 "in US mid-market.",
                 "Many US carriers; Mphasis is parent."],
                ["<strong>FINEOS</strong>",
                 "Group life, disability and absence; integrated "
                 "claims.",
                 "Major US group-benefits carriers (MetLife, "
                 "Prudential US group, MassMutual)."],
                ["<strong>Prophet (FIS), AXIS (Moody’s), MG-ALFA, "
                 "MoSes, GGY-AXIS</strong>",
                 "Actuarial modelling and reserving; IFRS 17 / "
                 "LDTI engines.",
                 "Most large life insurers and reinsurers."],
                ["<strong>Sapiens ReinsuranceMaster, SICS "
                 "(SICS — Eurotech), in-house reinsurance "
                 "ledgers</strong>",
                 "Reinsurance accounting, treaty / facultative "
                 "tracking, cession management.",
                 "Munich Re, Swiss Re, Hannover Re, large "
                 "primary insurers’ ceded books."],
            ]
        )
        + H3("3.6  Insurance — accounting and reporting regimes")
        + ul([
            "<strong>IFRS 17 Insurance Contracts</strong> — in "
            "effect from 1 January 2023 globally (ex-US); "
            "rewrote reserving, contractual service margin, "
            "transition methods. Engines like FIS Prophet "
            "Enterprise, Moody’s AXIS, RNA Analytics R3S, SAS "
            "for IFRS 17.",
            "<strong>US LDTI (Long-Duration Targeted "
            "Improvements)</strong> — ASU 2018-12; in effect "
            "since 2023 for SEC filers.",
            "<strong>Solvency II (EU/UK)</strong> — risk-based "
            "capital regime; UK Solvency UK reforms (effective "
            "2024–25); EU Solvency II Review adopted 2024.",
            "<strong>RBC (US Risk-Based Capital)</strong>, "
            "<strong>BCAR (Best’s)</strong>, <strong>SAM (South "
            "Africa)</strong>, <strong>ICS (IAIS Insurance "
            "Capital Standard)</strong> from 2026.",
            "<strong>India IRDAI Risk-Based Capital</strong> "
            "transition under preparation; current regime is "
            "factor-based.",
            "<strong>NAIC Model Audit Rule</strong>, <strong>SOX "
            "for insurers</strong>, <strong>EIOPA "
            "Guidelines</strong> in EU.",
        ])
    )
    return TopicSection(
        "3.  How both estates actually work — vendors, regimes, "
        "data flows",
        "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  United States — capital markets and insurance")
        + ul([
            "<strong>SEC, FINRA, CFTC</strong> regulate "
            "broker-dealers, swap dealers, exchanges; <strong>"
            "Reg NMS, Reg ATS, Reg SCI</strong> shape exchange "
            "and ATS technology.",
            "<strong>T+1 since 28 May 2024</strong>; T+0 voluntary "
            "for some products.",
            "<strong>Insurance is state-regulated</strong> via "
            "<strong>NAIC</strong> + 50 state insurance "
            "departments; federal exposure via FIO and Treasury.",
            "<strong>Climate disclosure</strong> — SEC climate rule "
            "stayed pending litigation (2024); California SB 253 "
            "/ 261 effective 2026.",
        ])
        + H3("4.2  United Kingdom and Eurozone")
        + ul([
            "<strong>FCA / PRA / Bank of England</strong> for "
            "banks; <strong>PRA</strong> for insurers; "
            "<strong>Solvency UK reforms</strong> reduce risk-"
            "margin and ease capital for insurers (2024–25).",
            "<strong>EU MiFID II / MiFIR Refit (2024)</strong>, "
            "<strong>EMIR REFIT (Apr 2024)</strong>, <strong>EU "
            "Solvency II Review (2024)</strong>.",
            "<strong>EU CSDR</strong> (penalties for settlement "
            "fails); <strong>EU AI Act</strong> for life pricing "
            "and credit-life products.",
            "<strong>UK + EU T+1 target 11 October 2027</strong>.",
            "<strong>EU FiDA</strong> (Financial Data Access) — "
            "Open Insurance proposal in trilogue 2024–25.",
        ])
        + H3("4.3  India and APAC")
        + ul([
            "<strong>SEBI</strong> regulates capital markets; T+1 "
            "fully in force since Jan 2023; T+0 same-day "
            "settlement live in beta from Mar 2024.",
            "<strong>NSE / BSE</strong> exchanges; <strong>NSCCL "
            "/ ICCL</strong> clearing; <strong>NSDL / "
            "CDSL</strong> depositories.",
            "<strong>IRDAI</strong> regulates insurance; "
            "<strong>Bima Sugam</strong> insurance marketplace "
            "launching 2025; risk-based capital framework "
            "consultation ongoing.",
            "<strong>Singapore MAS</strong> for both; <strong>"
            "Hong Kong SFC + HKEX + HKIA</strong>; <strong>JFSA "
            "+ JPX</strong>; <strong>ASIC + APRA + ASX</strong>.",
        ])
        + H3("4.4  The vendor consolidation that matters")
        + ul([
            "<strong>Nasdaq + Adenza (2023)</strong> brought "
            "Calypso and AxiomSL under Nasdaq alongside "
            "SMARTS surveillance.",
            "<strong>LSEG + Refinitiv (2021)</strong> created the "
            "second-biggest financial-data platform after "
            "Bloomberg.",
            "<strong>SS&amp;C + Advent / Eze / Black "
            "Diamond</strong> consolidated wealth and asset-"
            "management technology.",
            "<strong>FIS + Worldpay split (2024)</strong>; FIS "
            "kept the capital-markets and banking businesses.",
            "<strong>Broadridge + Itiviti (2021)</strong> brought "
            "front-office trading workflow into Broadridge.",
            "<strong>ICE bought Black Knight (2023)</strong> for "
            "mortgage; capital-markets effect via MERSCORP and "
            "ICE Mortgage data.",
            "<strong>Insurance: Roper sold ConstructConnect; "
            "Sapiens privatised by Advent (2024) "
            "consultation</strong>; Duck Creek went private with "
            "Vista 2023.",
        ])
    )
    return TopicSection(
        "4.  Region by region and vendor consolidation",
        "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  Risk technology — the engines behind the dashboards")
        + ul([
            "<strong>Market risk</strong> — VaR, ES (Expected "
            "Shortfall under FRTB), historical simulation, "
            "Monte Carlo; engines inside Murex, Calypso, FIS, "
            "Numerix, in-house C++/Python grids.",
            "<strong>Credit risk</strong> — counterparty CVA / "
            "DVA / FVA; xVA desks run grids the size of small "
            "banks; Quantifi, Numerix, Murex are common.",
            "<strong>Liquidity risk</strong> — Basel LCR / NSFR; "
            "intraday liquidity via SmartStream, Bottomline, "
            "Vermeg.",
            "<strong>Operational risk</strong> — RCSA, "
            "scenario analysis; Archer, OpenPages, MetricStream, "
            "ServiceNow IRM.",
            "<strong>Insurance risk</strong> — Solvency II "
            "internal model or standard formula; ORSA; "
            "actuarial valuation engines.",
        ])
        + H3("5.2  Surveillance, e-comms and conduct risk")
        + ul([
            "<strong>Trade surveillance</strong> — Nasdaq SMARTS, "
            "NICE Actimize Markets, Eventus Validus, b-next, "
            "Trillium / TLX.",
            "<strong>Communications surveillance</strong> — "
            "Behavox, Smarsh, Global Relay, NICE Comms, Veritone "
            "Voice; massive growth post the 2021–24 SEC and "
            "CFTC fines on off-channel comms (>USD 3B in fines "
            "across the industry).",
            "<strong>Best execution analytics</strong> — Big xyt, "
            "LiquidMetrix, IHS Markit / S&amp;P TCA.",
        ])
        + H3("5.3  Insurance — claims AI and digital underwriting")
        + ul([
            "<strong>FNOL automation</strong> — First Notice of "
            "Loss via mobile, with vision LLMs assessing damage "
            "for motor and home claims.",
            "<strong>Straight-through claims</strong> — low-"
            "complexity claims paid in minutes (Lemonade is the "
            "well-known fintech example; incumbents are "
            "catching up).",
            "<strong>Risk pricing</strong> — telematics for motor, "
            "wearables for life, IoT for property; ML pricing "
            "models replacing GLM-only books.",
            "<strong>Fraud detection</strong> — Shift Technology, "
            "FRISS, FICO Insurance Fraud, in-house ML.",
            "<strong>Underwriting copilots</strong> — Generative "
            "AI surfacing relevant clauses, prior claims, market "
            "data; speeds up commercial / specialty underwriting "
            "(Liberty Mutual, AXA XL public references).",
        ])
        + H3("5.4  Tokenised assets and the next capital-markets rail")
        + ul([
            "<strong>Tokenised money-market funds</strong> — "
            "BlackRock BUIDL on Ethereum (March 2024) — USD 500M+ "
            "AUM by end of 2024; Franklin Templeton OnChain US "
            "Government Money Fund.",
            "<strong>Tokenised repo</strong> — Broadridge DLR "
            "settling tens of trillions notional cumulatively; "
            "JPM Onyx, HSBC Orion, Goldman GS DAP.",
            "<strong>Project Agorá</strong> (BIS, 2024) — multi-"
            "central-bank tokenised wholesale settlement.",
            "<strong>EU MiCA</strong> in force since 30 Dec 2024; "
            "<strong>UK Digital Securities Sandbox</strong> "
            "operational from 2024; <strong>Singapore MAS Project "
            "Guardian</strong> tokenisation pilots; <strong>India "
            "RBI wholesale CBDC pilot</strong> for G-Sec settlement.",
            "<strong>Implication for platforms</strong> — Murex, "
            "Calypso, Aladdin, Broadridge are all building "
            "tokenised-asset workflows so that the capital-markets "
            "estate can route tokens like any other instrument.",
        ])
    )
    return TopicSection(
        "5.  Advanced — risk engines, surveillance, AI in insurance, "
        "tokenisation",
        "advanced", body)


def _sec6() -> TopicSection:
    body = (
        H3("6.1  Choosing a capital-markets platform")
        + table(
            ["Need", "Best fit in 2025", "Why"],
            [
                ["End-to-end sell-side cross-asset",
                 "Murex MX.3 (cloud) or Adenza Calypso",
                 "Mature, regulator-comfortable, broad coverage."],
                ["Buy-side end-to-end",
                 "Aladdin (large), Charles River (large), "
                 "SimCorp Dimension (EU-leaning), Bloomberg AIM "
                 "(mid)",
                 "Different shapes for different scales; Aladdin "
                 "concentration risk has become a board topic."],
                ["Treasury",
                 "ION (Wallstreet Suite, Reval), FIS Quantum, "
                 "Calypso treasury, in-house",
                 "Tier-1 banks blend ION + in-house; ION "
                 "concentration risk after Jan 2023 ransomware "
                 "incident now scrutinised."],
                ["Post-trade and securities processing",
                 "Broadridge for US broker-dealers; Tata "
                 "BaNCS Market Infrastructure; SmartStream TLM "
                 "for reconciliation",
                 "Broadridge is the de-facto US standard."],
                ["Surveillance",
                 "Nasdaq SMARTS for trade; Behavox / Smarsh / "
                 "Global Relay for comms",
                 "Buy-side and sell-side both need both."],
            ]
        )
        + H3("6.2  Choosing an insurance core platform")
        + table(
            ["Need", "Best fit in 2025", "Why"],
            [
                ["P&amp;C policy / claims / billing — large carrier",
                 "Guidewire Cloud (PolicyCenter, ClaimCenter, "
                 "BillingCenter)",
                 "Dominant share in tier-1 P&amp;C; vibrant "
                 "implementer market (HCLTech, EY, Capgemini, "
                 "Cognizant, Wipro)."],
                ["P&amp;C — US mid-market and personal lines",
                 "Duck Creek OnDemand or Majesco",
                 "SaaS economics and faster deployment."],
                ["Life &amp; Annuities",
                 "Sapiens ALIS / CoreSuite, FINEOS for group, "
                 "Equisoft Oracle, in-house at very large "
                 "insurers",
                 "Long policy life pushes tier-1 carriers to "
                 "stable, configurable platforms."],
                ["Actuarial / IFRS 17 / LDTI",
                 "FIS Prophet, Moody’s AXIS, RNA Analytics R3S, "
                 "SAS",
                 "Most carriers run Prophet or AXIS at the core; "
                 "RNA growing share in EU."],
                ["Reinsurance",
                 "Sapiens ReinsuranceMaster, SICS, in-house",
                 "Few specialists; many tier-1 reinsurers run "
                 "in-house ledgers."],
            ]
        )
        + H3("6.3  Build vs buy — capital markets vs insurance")
        + ul([
            "<strong>Capital markets</strong> — buy the trading "
            "and risk platform; build the differentiating algo "
            "and analytics layer; integrate via FIX / "
            "ISO 20022 / files.",
            "<strong>Insurance</strong> — buy the policy, claims "
            "and billing platforms; build the digital channels, "
            "underwriting analytics and AI claims layer.",
            "Both estates: standardise on cloud (Azure or AWS), "
            "OpenTelemetry, GitOps, OPA — see IV.1.",
        ])
    )
    return TopicSection(
        "6.  Decision matrices — platform choice for capital markets "
        "and insurance",
        "intermediate", body)


def _sec7() -> TopicSection:
    body = (
        example(
            "BlackRock Aladdin — the buy-side platform of record",
            ol([
                "Aladdin started as BlackRock’s internal portfolio "
                "and risk platform; opened to external clients "
                "in 1999.",
                "200+ external clients with USD 20T+ in assets "
                "under platform; Allianz, MEAG, Prudential, "
                "AustralianSuper, Mitsubishi UFJ Asset.",
                "Major Azure migration ongoing; eFront integration "
                "for private markets; Aladdin Climate for "
                "climate-risk analytics.",
                "Concentration-risk discussion: regulators "
                "(FSB, ESMA) are watching; some clients now run "
                "challenger systems on the most critical "
                "controls.",
            ])
        )
        + example(
            "ION January 2023 — concentration risk made visible",
            ol([
                "Lockbit ransomware against ION Cleared Derivatives "
                "(Trading Technologies / FIS / SunGard heritage) "
                "took down derivatives back-office at dozens of "
                "tier-1 banks for over a week.",
                "Trades had to be processed manually; CFTC "
                "Commitment of Traders report was delayed for the "
                "first time in modern memory.",
                "Lessons: critical-third-party risk in capital "
                "markets is real; DORA designations of CTPs were "
                "tightened in response.",
            ])
        )
        + example(
            "Allianz — Guidewire Cloud at global scale",
            ol([
                "Allianz is rolling out Guidewire Cloud "
                "(PolicyCenter, ClaimCenter, BillingCenter) across "
                "European P&amp;C operations under the ‘Allianz "
                "Customer Model’ programme.",
                "Implementation partners include EY, Capgemini, "
                "Accenture, HCLTech across geographies.",
                "Lessons: tier-1 carrier global rollout is multi-"
                "year; configuration discipline and partner "
                "ecosystem dominate the success curve.",
            ])
        )
        + example(
            "An Indian life insurer on Sapiens ALIS + Prophet for "
            "IFRS 17",
            ol([
                "Mid-tier Indian life insurer runs Sapiens ALIS "
                "for policy admin; Prophet Enterprise for "
                "actuarial reserving; integrated to Oracle GL.",
                "IFRS 17 implementation 2021–23 with HCLTech / "
                "Mastek as integrators; CSM (Contractual Service "
                "Margin) tracked from 1 Jan 2023.",
                "IRDAI risk-based-capital transition prep "
                "underway 2024–25.",
            ])
        )
        + example(
            "Standard Chartered Treasury — modernising on Calypso "
            "(Adenza)",
            ol([
                "SC consolidated treasury and capital-markets risk "
                "on Calypso (now Adenza, Nasdaq) over 2018–24; "
                "Murex retained for some businesses.",
                "Move to AWS deployment for Calypso; HCLTech is "
                "one of the partners for application services.",
                "FRTB readiness completed for EU 1 Jan 2025 "
                "go-live; UK 1 Jan 2026 in flight.",
            ])
        )
    )
    return TopicSection(
        "7.  Worked examples — five real BFSI capital-markets and "
        "insurance journeys",
        "intermediate", body)


def _sec8() -> TopicSection:
    return TopicSection(
        "8.  Questions a leader asks in any capital-markets or "
        "insurance review",
        "basic",
        ol([
            "What instruments / lines of business does each "
            "platform cover, and where are the duplicates?",
            "What is our T+1 readiness — UK/EU 11 Oct 2027 — and "
            "are post-trade systems ready to settle in 24 hours?",
            "What is our FRTB programme status (EU live 2025, UK "
            "2026), and how is it integrated with our risk "
            "platform?",
            "Where are we on IFRS 17 / LDTI run state — is it "
            "production-stable or still firefighting close cycles?",
            "What is our Aladdin / Murex / Calypso / ION "
            "concentration risk, and is there a credible "
            "challenger / exit plan per DORA?",
            "What surveillance coverage do we have on trade and "
            "comms, and is e-comms covered to the standard the "
            "SEC is fining on?",
            "How are we adopting Guidewire Cloud / Duck Creek "
            "OnDemand / Sapiens cloud, and have we tested DR for "
            "the SaaS deployment?",
            "What is our claims-AI roadmap and what fraud savings "
            "have we measured?",
            "What is our tokenised-assets roadmap — BUIDL-style "
            "MMF, repo, secondary trading?",
            "How are we using EU MiCA / UK DSS / Singapore "
            "Project Guardian / India CBDC pilots to learn "
            "before scaling?",
            "What is our reinsurance ceded-book accounting "
            "platform, and is it ready for IFRS 17 PAA / GMM?",
            "Are conduct risk and best-execution analytics "
            "running on data the regulator finds defensible?",
        ]))


def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘Capital markets and insurance can share one core "
            "platform.’ — They cannot. Lifecycle, latency and "
            "regulators are different. Share data, not core "
            "systems.",
            "‘Aladdin / Murex / Calypso is too big to fail.’ — "
            "ION January 2023 says otherwise. Plan for a TLPT-"
            "level outage.",
            "‘IFRS 17 is finished.’ — Year-1 close is finished. "
            "Reserving granularity, transition hangovers and "
            "audit fine-tuning are still 2–3 years of work.",
            "‘FRTB is just a model upgrade.’ — It is also a "
            "data-quality, sensitivity-collection, and IPV "
            "(Independent Price Verification) overhaul.",
            "‘T+1 is just a SLA change.’ — It is a global "
            "post-trade re-engineering: matching, FX funding, "
            "stock-loan recall, all faster.",
            "‘Surveillance covers our floor.’ — Off-channel "
            "comms (WhatsApp, Signal, Telegram) cost the "
            "industry >USD 3B in SEC + CFTC fines from 2021–"
            "24. Coverage must be device-level, not just "
            "approved-channel.",
            "‘Claims AI replaces adjusters.’ — It augments "
            "them. Loss-of-control complaints under FCA "
            "Consumer Duty, EU AI Act high-risk for life "
            "pricing — keep a human in the loop.",
            "‘Tokenisation is a sandbox toy.’ — BUIDL crossed "
            "USD 500M AUM in 9 months; Broadridge DLR settles "
            "real repo. The integration question is now "
            "‘when’, not ‘if’.",
            "‘Reinsurance is the reinsurer’s problem.’ — "
            "Ceded-book accounting and bordereaux quality are "
            "the cedent’s problem; bad data costs basis points "
            "every quarter.",
            "‘Solvency II is settled in the EU.’ — The 2024 "
            "Solvency II Review and UK Solvency UK reforms "
            "rewrite parts of the regime; engines and reports "
            "need updating in 2025–26.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("OMS / EMS", "Order / Execution Management System."),
            ("FIX", "Financial Information eXchange protocol."),
            ("CCP / CSD", "Central Counterparty / Central "
                "Securities Depository."),
            ("DTCC / Euroclear / Clearstream / NSDL / CDSL",
             "Major CSDs by region."),
            ("LCH / ICE Clear / CME Clearing / Eurex / NSCCL",
             "Major CCPs."),
            ("MiFID II / MiFIR / EMIR / SFTR / CAT / Dodd-Frank",
             "Capital-markets reporting regimes."),
            ("FRTB", "Fundamental Review of the Trading Book — "
                "Basel trading-book capital framework; EU 2025, "
                "UK 2026, US delayed."),
            ("CSDR", "EU Central Securities Depositories "
                "Regulation; settlement-fail penalties."),
            ("xVA", "CVA / DVA / FVA / KVA / MVA — derivatives "
                "valuation adjustments."),
            ("VaR / ES", "Value-at-Risk / Expected Shortfall."),
            ("Aladdin / Charles River / SimCorp / Bloomberg AIM",
             "Major buy-side OMS / IBOR platforms."),
            ("Murex / Calypso / Summit / FIS Front Arena / ION",
             "Major sell-side trading and risk platforms."),
            ("Broadridge", "Major US post-trade platform; "
                "Distributed Ledger Repo (DLR) live."),
            ("Guidewire / Duck Creek / Sapiens / EIS / Majesco / "
             "FINEOS", "Major insurance core platforms."),
            ("Prophet / AXIS / R3S / MoSes / GGY-AXIS",
             "Actuarial modelling engines."),
            ("IFRS 17", "Insurance Contracts standard; effective "
                "1 Jan 2023 globally."),
            ("LDTI", "US GAAP Long-Duration Targeted "
                "Improvements; ASU 2018-12."),
            ("Solvency II / Solvency UK / RBC / SAM / ICS",
             "Insurance capital regimes."),
            ("CSM", "Contractual Service Margin — IFRS 17 "
                "concept for unearned profit."),
            ("ORSA", "Own Risk and Solvency Assessment under "
                "Solvency II."),
            ("FNOL", "First Notice of Loss — start of the "
                "claims process."),
            ("BUIDL / Onyx / Orion / GS DAP / DLR",
             "Major tokenised-asset platforms."),
            ("Project Agorá / Project Guardian / DSS",
             "Tokenisation initiatives — BIS, MAS, Bank of "
                "England."),
            ("MiCA", "EU Markets in Crypto-Assets regulation; "
                "in force 30 Dec 2024."),
            ("Trade repository / SDR", "Holds derivatives "
                "trade reports for regulators."),
            ("IBOR / ABOR", "Investment Book of Record / "
                "Accounting Book of Record."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
