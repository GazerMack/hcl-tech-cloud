"""BFSI Domain Platforms · 06 — Wealth management platforms (Avaloq, Temenos Wealth, Aladdin).

Covers private banking, wealth management, family-office and robo-advisory
technology across India, US, UK, EU, Singapore, UAE, Hong Kong.
"""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="VI.6",
        slug="06-wealth-management-platforms",
        title="Wealth management platforms — private banking, advisory, and robo",
        one_liner=(
            "When a High-Net-Worth Individual (HNWI) sits across from a Relationship "
            "Manager at a Swiss private bank, or when a millennial opens a robo-advisory "
            "account from their phone, a specialised technology stack is at work — portfolio "
            "management, order routing, suitability engines, tax-lot accounting, consolidated "
            "reporting, and regulatory compliance. This topic maps that stack vendor by vendor, "
            "region by region, and decision by decision."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


# ------------------------------------------------------------------ sec 0

def _sec0() -> TopicSection:
    body = (
        primer(
            p("Wealth management sits at the intersection of banking, capital markets, "
              "and insurance. A private bank like Julius Baer, UBS, or Citi Private Bank "
              "needs all the capabilities of a retail bank (accounts, payments, cards) "
              "plus all the capabilities of an asset manager (portfolio construction, "
              "execution, risk) plus advisory capabilities unique to wealthy individuals "
              "(estate planning, tax optimisation, multi-generational structuring). "
              "The technology that powers this is different from core banking, different "
              "from a trading floor, and increasingly different from simple retail "
              "investment platforms.")
        )
        + H3("0.1  IT-side anchor — a personalised dashboard that hides enormous complexity")
        + it_anchor(
            p("Think of a modern smart-home control panel. One screen shows your "
              "heating, lighting, cameras, locks, music, and appliances — each made by "
              "a different manufacturer, each speaking a different protocol. The panel's "
              "job is to present a unified view and let you set rules ('if temperature "
              "drops below 18°C, turn on heating'). A wealth management platform does "
              "the same for money: it shows the Relationship Manager (RM) or the client "
              "a single view across equities, bonds, funds, structured products, "
              "insurance wrappers, real estate, private equity, crypto — held at "
              "multiple custodians in multiple currencies — and lets them set rules "
              "('if the portfolio's equity weight rises above 60%, rebalance').")
        )
        + H3("0.2  BFSI-side anchor — your mutual fund SIP and the private banker's world")
        + bfsi_anchor(
            p("If you invest ₹10,000 per month in a mutual fund Systematic Investment "
              "Plan (SIP) on Zerodha or Groww, the platform picks one fund, places one "
              "order, and shows one balance. Now imagine a client with USD 50 million "
              "across three custodians in Zurich, Singapore, and New York, holding "
              "400 positions in equities, bonds, alternatives, a family trust, a "
              "charitable foundation, and a life-insurance wrapper in Liechtenstein. "
              "The RM needs a platform that consolidates all of this into a single "
              "view, checks suitability for every trade against the client's risk "
              "profile and local regulations, generates a proposal the client signs "
              "digitally, routes orders to the right venue, and produces quarterly "
              "performance reports — in the client's preferred currency and language. "
              "That is what a wealth management platform does.")
        )
        + H3("0.3  The three operating models you must know")
        + ul([
            "<strong>Discretionary Portfolio Management (DPM)</strong> — the bank "
            "manages the client's money according to an agreed mandate. The RM does "
            "not call the client before every trade. The platform must enforce "
            "mandate compliance (investment guidelines) automatically.",
            "<strong>Advisory</strong> — the bank recommends trades but the client "
            "must approve each one. The platform must perform a suitability check "
            "per MiFID II / RIA rules / MAS guidelines before the RM can even show "
            "the recommendation.",
            "<strong>Execution-only</strong> — the client decides; the bank just "
            "executes. Lighter regulation but the platform still records "
            "appropriateness checks where required.",
        ])
        + H3("0.4  Client segments in wealth management")
        + table(
            ["Segment", "Typical AUM", "Service model"],
            [
                ["<strong>Mass affluent</strong>",
                 "USD 100K – 1M",
                 "Digital-first, robo or hybrid advisory, standardised model portfolios."],
                ["<strong>High Net Worth (HNW)</strong>",
                 "USD 1M – 30M",
                 "Dedicated RM, advisory or discretionary, tailored portfolios."],
                ["<strong>Ultra-High Net Worth (UHNW)</strong>",
                 "USD 30M – 500M+",
                 "Multi-RM team, multi-custodian, family office services, "
                 "alternatives, tax structuring."],
                ["<strong>Family office</strong>",
                 "USD 100M+",
                 "Own investment team, consolidated reporting across entities, "
                 "generational planning, philanthropy."],
            ]
        )
    )
    return TopicSection(
        "0.  Primer — anchored to things you already know", "basic", body)


# ------------------------------------------------------------------ sec 1

def _sec1() -> TopicSection:
    body = (
        p("Wealth management platforms exist because no general-purpose core "
          "banking system or trading system solves the wealth problem well:")
        + ol([
            "<strong>Consolidated multi-custodian view.</strong> Wealthy clients "
            "hold assets at multiple banks and custodians. The platform must "
            "aggregate positions, transactions, and valuations from external "
            "sources — custodian feeds, SWIFT MT 535/536/537, market data.",
            "<strong>Suitability and mandate compliance.</strong> Regulators "
            "worldwide (MiFID II in the EU, SEC/FINRA in the US, MAS in "
            "Singapore, SEBI in India) require that every recommendation or "
            "discretionary trade is suitable for the client's risk profile, "
            "investment horizon, knowledge, and objectives.",
            "<strong>Proposal and advisory workflow.</strong> The RM needs to "
            "create an investment proposal, run a suitability check, show the "
            "impact on the portfolio, get client approval (digitally or on "
            "paper), and then route orders.",
            "<strong>Performance and attribution reporting.</strong> Clients "
            "expect to see time-weighted and money-weighted returns, benchmark "
            "comparison, asset-class attribution, currency effects, fee "
            "transparency — in their base currency, in their language.",
            "<strong>Regulatory reporting.</strong> MiFID II cost and charges "
            "disclosure, PRIIPs KID (Key Information Document) generation, "
            "UK Consumer Duty fair-value assessment, FATCA/CRS reporting, "
            "cross-border tax documentation.",
            "<strong>Lifecycle management.</strong> Client onboarding (KYC/AML), "
            "risk profiling, investment policy statement, periodic review, "
            "succession planning, estate events.",
        ])
    )
    return TopicSection(
        "1.  Why wealth management needs its own platform — first principles",
        "basic", body)


# ------------------------------------------------------------------ sec 2

def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart TB\n'
            '  subgraph "Client layer"\n'
            '    CP["Client portal and mobile app"]\n'
            '    RM["RM workstation and CRM"]\n'
            '  end\n'
            '  subgraph "Advisory and portfolio engine"\n'
            '    SC["Suitability and compliance engine"]\n'
            '    PM["Portfolio management and rebalancing"]\n'
            '    PR["Proposal and reporting"]\n'
            '  end\n'
            '  subgraph "Execution and operations"\n'
            '    OMS["Order management"]\n'
            '    CU["Custodian connectivity"]\n'
            '    TA["Tax-lot accounting"]\n'
            '    RC["Reconciliation"]\n'
            '  end\n'
            '  subgraph "Foundation"\n'
            '    CB["Core banking (accounts, cash, FX)"]\n'
            '    MD["Market data"]\n'
            '    KYC["KYC / AML / onboarding"]\n'
            '    REG["Regulatory reporting"]\n'
            '  end\n'
            '  CP --> SC\n'
            '  RM --> SC\n'
            '  SC --> PM\n'
            '  PM --> PR\n'
            '  PM --> OMS\n'
            '  OMS --> CU\n'
            '  CU --> TA\n'
            '  TA --> RC\n'
            '  CB --> PM\n'
            '  MD --> PM\n'
            '  KYC --> SC\n'
            '  REG --> PR',
            "The wealth management technology stack — four layers from client "
            "touchpoint to regulatory foundation."
        )
        + p("The diagram shows why wealth management is hard to retrofit onto a "
            "retail core: the advisory and portfolio engine in the middle is the "
            "differentiator, and it must integrate upward to client channels and "
            "downward to execution, custody, and regulatory infrastructure.")
    )
    return TopicSection(
        "2.  The core concept in one picture", "basic", body)


# ------------------------------------------------------------------ sec 3

def _sec3() -> TopicSection:
    body = (
        H3("3.1  Phase 1: Client onboarding and risk profiling")
        + p("The client completes a KYC (Know Your Customer) process — identity "
            "verification, source of wealth, tax residency (FATCA/CRS), and a "
            "suitability questionnaire. The questionnaire captures investment "
            "objectives, time horizon, risk tolerance, knowledge and experience, "
            "and financial situation. The platform assigns a risk profile — "
            "typically on a scale like 'Conservative / Moderate / Growth / "
            "Aggressive' — which becomes the constraint for all future advisory "
            "and discretionary activity.")
        + H3("3.2  Phase 2: Investment policy and mandate setup")
        + p("For advisory clients, the RM and client agree on an investment "
            "policy statement (IPS) — asset-class ranges, currency preferences, "
            "exclusions (e.g., no tobacco, no fossil fuels for ESG mandates), "
            "benchmark. For discretionary clients, the IPS becomes a legally "
            "binding mandate with hard limits (e.g., 'max 65% equity, min 10% "
            "cash, no single position > 5% of AUM'). The platform encodes these "
            "as rules that the suitability engine enforces pre-trade.")
        + H3("3.3  Phase 3: Portfolio construction and proposal")
        + p("The RM (or the robo engine) builds a model portfolio or selects from "
            "the bank's approved product shelf. The platform runs a pre-trade "
            "suitability check: does this trade comply with the client's risk "
            "profile and mandate? What is the impact on concentration, liquidity, "
            "and risk metrics? If compliant, the system generates a proposal — a "
            "document or digital record the client reviews and approves.")
        + H3("3.4  Phase 4: Order routing and execution")
        + p("Approved trades flow to the order management system (OMS), which "
            "routes to the appropriate venue — exchange, OTC desk, fund transfer "
            "agent, structured-product issuer. For discretionary mandates, the "
            "platform may execute block orders across multiple client accounts "
            "and then allocate fills pro rata (block trading and allocation).")
        + H3("3.5  Phase 5: Post-trade — settlement, reconciliation, tax-lot accounting")
        + p("Executed trades settle with the custodian(s). The platform reconciles "
            "positions and cash daily against custodian statements (SWIFT "
            "MT 535/536 or proprietary feeds). Tax-lot accounting tracks the cost "
            "basis of each position for capital-gains tax purposes — FIFO "
            "(First In First Out), LIFO (Last In First Out), specific-lot, or "
            "average-cost depending on the jurisdiction.")
        + H3("3.6  Phase 6: Reporting and ongoing monitoring")
        + p("The platform produces periodic reports — monthly or quarterly — "
            "showing performance (time-weighted return, money-weighted/IRR), "
            "attribution (how much came from asset allocation vs. security "
            "selection), fee disclosure (MiFID II cost and charges), and "
            "portfolio analytics (risk contribution, duration, credit quality). "
            "The discretionary engine continuously monitors mandates for "
            "breaches — if a position drifts outside its allowed range, it "
            "triggers a rebalancing alert or auto-rebalances.")
    )
    return TopicSection(
        "3.  How it actually works — phase by phase", "intermediate", body)


# ------------------------------------------------------------------ sec 4

def _sec4() -> TopicSection:
    body = (
        H3("4.1  The platform vendors — wealth management's Big Five and beyond")
        + table(
            ["Vendor / Platform", "Headquarters", "Strength", "Notable clients"],
            [
                ["<strong>Avaloq (NEC Group)</strong>",
                 "Switzerland",
                 "End-to-end wealth-management and private-banking platform. "
                 "Core banking for private banks plus portfolio management, "
                 "advisory workflow, regulatory reporting. SaaS (Avaloq.one) "
                 "and on-prem. NEC acquired Avaloq in 2020 for CHF 2.05B.",
                 "Barclays Wealth (UK), DBS Private Banking (Singapore), "
                 "Julius Baer, Vontobel, Deutsche Bank Wealth (EU), "
                 "LGT, Bank Safra Sarasin, many Swiss and Liechtenstein banks."],
                ["<strong>Temenos Wealth (WealthSuite / Multifonds)</strong>",
                 "Switzerland",
                 "Front-to-back wealth: advisor workbench, portfolio management, "
                 "fund accounting (Multifonds), compliance, client lifecycle. "
                 "Integrates with Temenos Transact core banking. T24 heritage.",
                 "ABN AMRO (NL), EFG International, BBVA (ES), "
                 "Standard Chartered Wealth (selected markets), "
                 "National Australia Bank, several Gulf private banks."],
                ["<strong>BlackRock Aladdin Wealth</strong>",
                 "United States",
                 "Extension of the Aladdin ecosystem for wealth managers and "
                 "RIAs. Risk analytics, model portfolio construction, "
                 "rebalancing, proposal generation, compliance. Leverages "
                 "the same risk engine as institutional Aladdin.",
                 "Morgan Stanley Wealth Management (major deployment), "
                 "UBS (global), Wells Fargo Advisors (US), "
                 "several large RIA aggregators."],
                ["<strong>Additiv (DFS — Digital Finance Suite)</strong>",
                 "Switzerland",
                 "API-first, cloud-native wealth orchestration layer. "
                 "Designed to sit on top of existing core banking systems "
                 "and provide advisory, portfolio management, robo, and "
                 "hybrid services. Banking-as-a-Service approach.",
                 "Standard Chartered (nexus for wealth-as-a-service in ASEAN), "
                 "Mashreq (UAE), Bank of Singapore, EFG, Julius Baer (pilot)."],
                ["<strong>Objectway (Wealth Management Suite)</strong>",
                 "Italy / United Kingdom",
                 "Portfolio management, order management, client reporting, "
                 "compliance. Strong in UK and continental Europe. "
                 "Private equity owned (Accel-KKR).",
                 "Brooks Macdonald (UK), Quilter (UK), Cazenove Capital, "
                 "several Italian and UK discretionary managers."],
                ["<strong>SS&amp;C Advent / Black Diamond / Axys</strong>",
                 "United States",
                 "Portfolio accounting, performance reporting, client "
                 "reporting, CRM. Dominant in US RIA (Registered Investment "
                 "Advisor) market. Axys for smaller RIAs, APX for larger, "
                 "Black Diamond for turnkey.",
                 "Thousands of US RIAs, family offices, mid-market "
                 "wealth managers."],
                ["<strong>Envestnet / Tamarac / MoneyGuide</strong>",
                 "United States",
                 "Unified managed accounts (UMA), model marketplace, "
                 "financial planning, portfolio analytics, data aggregation. "
                 "Powers much of the US independent-advisor ecosystem.",
                 "Over 107,000 US advisors on the Envestnet platform, "
                 "major broker-dealers, several banks' wealth divisions."],
                ["<strong>SEI Wealth Platform (SWP)</strong>",
                 "United States",
                 "Outsourced wealth processing — portfolio accounting, "
                 "trust accounting, performance, compliance. The bank "
                 "outsources its middle and back office to SEI.",
                 "Several UK private banks (incl. past Coutts), "
                 "US trust companies, Canadian wealth firms."],
                ["<strong>Finantix (now part of InvestCloud)</strong>",
                 "United Kingdom / United States",
                 "Client lifecycle management, suitability, advisory "
                 "workflow, CRM for wealth. InvestCloud merged with "
                 "Tegra118 and Finantix (2021) to create a combined "
                 "digital wealth platform.",
                 "UBS (CRM layer), HSBC, BNP Paribas Wealth, "
                 "Lombard Odier, several European private banks."],
                ["<strong>SimCorp (now Deutsche Boerse Group)</strong>",
                 "Denmark",
                 "SimCorp Dimension / One for institutional asset managers "
                 "and large wealth firms. Front-to-back investment "
                 "management. Deutsche Boerse acquired SimCorp 2023.",
                 "Large European asset managers, pension funds, "
                 "insurance investment teams."],
            ]
        )
        + H3("4.2  Robo-advisory and hybrid platforms")
        + table(
            ["Platform", "Market", "Model"],
            [
                ["<strong>Betterment</strong>", "US", "B2C and B2B (Betterment for Advisors). "
                 "Goal-based, tax-loss harvesting, automated rebalancing."],
                ["<strong>Wealthfront</strong>", "US", "B2C. Direct indexing, tax-loss "
                 "harvesting, automated financial planning. Acquired by UBS 2022 (deal later "
                 "terminated), now independent."],
                ["<strong>Nutmeg (JPMorgan)</strong>", "UK", "B2C. ETF-based model portfolios, "
                 "ISA and pension wrappers. JPMorgan acquired 2021."],
                ["<strong>Scalable Capital</strong>", "Germany / EU", "B2C and B2B. Robo and "
                 "broker. EUR 20B+ AUM by 2024."],
                ["<strong>StashAway</strong>", "Singapore / APAC", "B2C. Economic regime-based "
                 "allocation. MAS-licensed."],
                ["<strong>Groww / Zerodha / Kuvera / Scripbox</strong>", "India",
                 "B2C. Mutual fund distribution, direct equity. SEBI-registered. "
                 "Groww crossed 10M+ transacting users by 2024."],
                ["<strong>Syfe / Endowus</strong>", "Singapore",
                 "B2C and B2B. CPF/SRS investment, goal-based, advisory."],
            ]
        )
        + H3("4.3  Specialised components in the wealth stack")
        + kv([
            ("Financial planning engines",
             "MoneyGuide (Envestnet), eMoney (Fidelity), RightCapital, Voyant "
             "(used in UK and EU), Conquest Planning (Canada). Used to model "
             "retirement, education funding, estate scenarios."),
            ("Client reporting / data aggregation",
             "Addepar (USD 6T+ assets on platform, UHNW and family offices), "
             "Canopy (by Ernst & Young), Masttro, PCR (Private Client "
             "Resources), Asset Vantage (India)."),
            ("Rebalancing and model management",
             "Orion Portfolio Solutions, 55ip (JPMorgan-owned, tax-smart), "
             "Vestmark (VISE), Parametric (Morgan Stanley-owned, direct "
             "indexing)."),
            ("Digital onboarding and KYC",
             "Appway (now FNZ), Fenergo, Jumio, Onfido, DigiLocker-based "
             "eKYC (India)."),
        ])
    )
    return TopicSection(
        "4.  Types and variations — the vendor landscape", "intermediate", body)


# ------------------------------------------------------------------ sec 5

def _sec5() -> TopicSection:
    body = (
        H3("5.1  Multi-custodian aggregation — the hardest data problem in wealth")
        + p("A UHNW client holds assets at UBS in Zurich, Citi in Singapore, and "
            "JPMorgan in New York. Each custodian sends position and transaction "
            "data in different formats (SWIFT MT 535/536/537, proprietary CSV, "
            "FIX, ISO 20022 semt messages). The wealth platform must:")
        + ol([
            "Normalise instrument identifiers (ISIN, CUSIP, SEDOL, Bloomberg "
            "ticker, RIC) — a single bond might have six different identifiers.",
            "Handle corporate actions (splits, mergers, dividends, rights issues) "
            "from each custodian with different processing timelines.",
            "Reconcile cash across currencies with different value dates.",
            "Map external account structures to the platform's internal hierarchy "
            "(client → entity → account → sub-account → portfolio).",
            "Produce a unified NAV (Net Asset Value) and performance calculation "
            "that handles inflows, outflows, fees, and FX correctly.",
        ])
        + p("This is why platforms like Avaloq and Temenos built their own "
            "core-banking foundation — they wanted control over the book of "
            "record. Overlay platforms like Aladdin Wealth or Additiv assume "
            "custody sits elsewhere and aggregate via feeds.")
        + H3("5.2  The suitability engine — regulatory logic at scale")
        + p("MiFID II (EU/UK) requires that every investment recommendation is "
            "suitable for the client considering their knowledge and experience, "
            "financial situation, investment objectives, risk tolerance, and "
            "ability to bear losses. The US equivalent is FINRA Rule 2111 "
            "(suitability) and the SEC's Regulation Best Interest (Reg BI, "
            "effective June 2020). Singapore MAS Notice FAA-N16 sets similar "
            "requirements. India's SEBI has suitability guidance for portfolio "
            "managers under the PMS (Portfolio Management Services) regulations.")
        + p("The suitability engine pre-trade checks every proposed transaction "
            "against these rules — product complexity vs. client knowledge, "
            "concentration limits, liquidity requirements, cost impact. If a "
            "check fails, the trade is blocked or escalated. Audit trails must "
            "be retained for 5–10 years depending on jurisdiction.")
        + H3("5.3  Discretionary mandate engine — investment guidelines enforcement")
        + p("A discretionary mandate specifies hard and soft limits:")
        + table(
            ["Constraint type", "Example", "Enforcement"],
            [
                ["Asset-class range", "Equity 30–65%, Fixed Income 20–50%, "
                 "Cash 5–15%", "Hard limit — breach blocks the trade."],
                ["Single-name concentration", "No single equity > 5% of AUM",
                 "Hard limit — pre-trade check."],
                ["Credit quality", "Min average rating A-",
                 "Soft limit — breach triggers alert; RM can override with reason."],
                ["Duration", "Portfolio duration 3–7 years",
                 "Soft limit — monitored post-trade with rebalancing trigger."],
                ["ESG exclusions", "No tobacco, no controversial weapons",
                 "Hard limit — blocked at product level."],
                ["Currency exposure", "Max 20% non-base-currency unhedged",
                 "Hard limit — FX hedge auto-triggered."],
            ]
        )
        + p("The platform continuously monitors the live portfolio against "
            "these constraints. Market movements can cause passive breaches "
            "(e.g., equity rises above 65% because the market rallied). The "
            "system generates breach reports and rebalancing proposals.")
        + H3("5.4  Tax-lot accounting and tax optimisation")
        + p("In the US, capital gains tax depends on which specific lot of "
            "shares you sell (FIFO, LIFO, specific identification, average "
            "cost for mutual funds). Tax-loss harvesting — selling a losing "
            "position to realise a loss that offsets gains elsewhere — is a "
            "major value-add in US wealth management (Betterment and "
            "Wealthfront popularised it). Direct indexing (owning individual "
            "stocks instead of an ETF to harvest losses at the single-stock "
            "level) is the premium version. In the UK, CGT is per tax year "
            "with a £3,000 annual exemption (2024–25). In India, LTCG on "
            "equity is 12.5% above ₹1.25 lakh (Union Budget 2024). Each "
            "jurisdiction's rules must be encoded in the platform.")
        + H3("5.5  Model portfolio management and rebalancing algorithms")
        + p("Most wealth platforms offer model portfolios — pre-built "
            "allocations (e.g., 'Moderate Growth: 50% equity, 30% fixed "
            "income, 10% alternatives, 10% cash'). When the bank updates "
            "the model, the platform can automatically rebalance all client "
            "accounts linked to that model — a critical feature at scale. "
            "Rebalancing algorithms must handle tax efficiency (minimise "
            "realised gains), transaction costs (minimum trade size), and "
            "cash flow timing (pending contributions or withdrawals).")
    )
    return TopicSection(
        "5.  Advanced — the mechanisms underneath", "advanced", body)


# ------------------------------------------------------------------ sec 6

def _sec6() -> TopicSection:
    body = (
        p("Wealth management is regulated at multiple levels: conduct of "
          "business (suitability, disclosure), prudential (capital), product "
          "(PRIIPs, MiFID product governance), and cross-border (tax, "
          "sanctions, data protection).")
        + table(
            ["Region", "Key regulations for wealth management"],
            [
                ["<strong>European Union</strong>",
                 "MiFID II / MiFIR — suitability, best execution, cost and charges "
                 "disclosure, product governance, inducement rules (ban on "
                 "third-party commissions for independent advice). PRIIPs KID — "
                 "Key Information Document for packaged products. EU Retail "
                 "Investment Strategy (RIS) — proposed 2023, tightens inducement "
                 "rules further. SFDR (Sustainable Finance Disclosure Regulation) "
                 "— ESG product classification (Article 6/8/9). GDPR — client "
                 "data handling. EU DORA — operational resilience for "
                 "wealth-management tech."],
                ["<strong>United Kingdom</strong>",
                 "FCA Conduct of Business Sourcebook (COBS) — suitability, "
                 "appropriateness. FCA Consumer Duty (Jul 2023) — fair value, "
                 "consumer understanding, consumer support. SDR (Sustainability "
                 "Disclosure Requirements) and anti-greenwashing rule (Nov 2024). "
                 "SMCR (Senior Managers and Certification Regime). UK "
                 "MiFID-equivalent regime post-Brexit. FCA review of advice/"
                 "guidance boundary (2024)."],
                ["<strong>United States</strong>",
                 "SEC Regulation Best Interest (Reg BI, Jun 2020) for "
                 "broker-dealers. Investment Advisers Act 1940 — fiduciary "
                 "standard for RIAs (Registered Investment Advisors). FINRA "
                 "Rule 2111 (suitability). SEC Marketing Rule (Nov 2022) — "
                 "modernised advertising rules. DOL Fiduciary Rule — retirement "
                 "advice; re-proposed 2023, vacated by courts 2024 (uncertain "
                 "status). SEC custody rule amendments. State-level fiduciary "
                 "rules (e.g., Massachusetts)."],
                ["<strong>Singapore</strong>",
                 "MAS Notice FAA-N16 — suitability, client knowledge assessment. "
                 "MAS Guidelines on Fair Dealing. SFA (Securities and Futures "
                 "Act). MAS Notice on Technology Risk Management (TRM). "
                 "Variable Capital Company (VCC) framework for fund structuring. "
                 "MAS Guidelines on Individual Accountability and Conduct (IAC)."],
                ["<strong>India</strong>",
                 "SEBI PMS (Portfolio Management Services) Regulations 2020 — "
                 "minimum ticket ₹50 lakh, suitability, disclosure. SEBI AIF "
                 "(Alternative Investment Fund) Regulations. SEBI Mutual Fund "
                 "Regulations — distributor vs. direct plans. RBI and SEBI KYC "
                 "norms, CKYC. IRDAI for insurance-linked investment products "
                 "(ULIPs). AMFI guidelines for mutual fund distribution."],
                ["<strong>UAE / Middle East</strong>",
                 "DFSA (Dubai Financial Services Authority) — wealth management "
                 "in DIFC. ADGM FSRA — Abu Dhabi. CBUAE for onshore banking. "
                 "Growing hub for UHNW clients; family-office regulations "
                 "being formalised."],
                ["<strong>Hong Kong</strong>",
                 "SFC Code of Conduct — suitability. HKMA guidelines for "
                 "private banking. Enhanced suitability regime for complex "
                 "products. Hong Kong is a major booking centre for Asian "
                 "wealth."],
            ]
        )
        + H3("6.1  Cross-border complexity — the wealth-specific challenge")
        + p("A client domiciled in India, with a trust in Singapore, assets "
            "booked in Zurich, and a US brokerage account triggers four "
            "different suitability regimes, FATCA and CRS reporting for "
            "three jurisdictions, withholding-tax treaties, and potentially "
            "the EU's DAC6 (Directive on Administrative Cooperation) for "
            "reportable cross-border arrangements. The platform must know "
            "which regime applies to which relationship and which booking "
            "entity — this is the 'cross-border rules engine' that "
            "differentiates serious wealth platforms from simple portfolio "
            "trackers.")
    )
    return TopicSection(
        "6.  BFSI / domain regulatory overlay", "advanced", body)


# ------------------------------------------------------------------ sec 7

def _sec7() -> TopicSection:
    body = (
        table(
            ["Decision", "Option A", "Option B", "Key trade-off"],
            [
                ["<strong>Build on a wealth-native platform vs. extend "
                 "core banking</strong>",
                 "Avaloq, Temenos WealthSuite — integrated core + wealth",
                 "Additiv / Objectway / Aladdin Wealth on top of existing core "
                 "(Temenos Transact, Finacle, TCS BaNCS)",
                 "Integrated is cleaner but forces a core-banking migration. "
                 "Overlay preserves the existing core but adds integration risk."],
                ["<strong>Discretionary engine: in-platform vs. "
                 "best-of-breed</strong>",
                 "Use Avaloq/Temenos built-in mandate compliance",
                 "Plug in Aladdin Wealth or SimCorp for portfolio management",
                 "In-platform is simpler; best-of-breed is stronger for "
                 "complex multi-asset mandates."],
                ["<strong>Client reporting: in-house vs. outsource</strong>",
                 "Build reports in the wealth platform (Avaloq, Objectway)",
                 "Outsource to Addepar, SEI, or a BPO provider",
                 "In-house gives control; outsourcing reduces cost for "
                 "mid-tier firms."],
                ["<strong>Robo-advisory: build vs. buy vs. white-label</strong>",
                 "Build custom robo on own tech stack",
                 "White-label from Additiv, InvestCloud, ETFmatic, Scalable "
                 "Capital B2B",
                 "Building is expensive and slow but fully differentiated. "
                 "White-label is fast but commoditised."],
                ["<strong>On-prem vs. SaaS</strong>",
                 "Avaloq on-prem / private cloud (traditional Swiss banks)",
                 "Avaloq.one SaaS, Temenos SaaS, Additiv cloud-native",
                 "On-prem gives data sovereignty (Swiss banking secrecy); "
                 "SaaS reduces TCO but raises data-residency questions."],
                ["<strong>Single-custodian vs. multi-custodian</strong>",
                 "Only aggregate assets held at the bank",
                 "Aggregate across external custodians (Addepar, Canopy, "
                 "Masttro)",
                 "Multi-custodian is the UHNW expectation but dramatically "
                 "increases data-quality and reconciliation complexity."],
                ["<strong>Advisor-led vs. hybrid vs. pure robo</strong>",
                 "Full RM-led advisory for all segments",
                 "Hybrid: robo for mass-affluent, RM for HNW+",
                 "Hybrid is the emerging consensus — it scales the mass-affluent "
                 "segment profitably while preserving the RM relationship "
                 "for HNW/UHNW."],
            ]
        )
    )
    return TopicSection(
        "7.  Trade-offs and decisions a leader owns", "intermediate", body)


# ------------------------------------------------------------------ sec 8

def _sec8() -> TopicSection:
    body = (
        example(
            "Morgan Stanley × Aladdin Wealth — the largest US wealth deployment",
            p("Morgan Stanley's 16,000+ Financial Advisors (FAs) manage "
              "approximately USD 4.6 trillion in client assets (2024). "
              "The firm deployed BlackRock's Aladdin Wealth as its core "
              "portfolio construction and risk analytics platform, integrated "
              "with Morgan Stanley's proprietary Next Best Action engine. "
              "Aladdin Wealth provides: (1) risk analytics on every client "
              "portfolio using the same models that manage BlackRock's own "
              "USD 10T+ AUM, (2) model portfolio construction and rebalancing, "
              "(3) tax-efficient transition management (moving a new client's "
              "legacy portfolio to a target model while minimising tax events). "
              "The challenge: Morgan Stanley simultaneously competes with "
              "BlackRock in asset management, creating a complex vendor "
              "dynamic where the platform provider is also a competitor.")
        )
        + example(
            "DBS Private Banking on Avaloq — a Singapore success story",
            p("DBS, Southeast Asia's largest bank, runs its private banking "
              "and wealth management on Avaloq. The platform handles "
              "portfolio management, advisory suitability (MAS FAA-N16), "
              "discretionary mandate compliance, and client reporting for "
              "DBS Private Bank clients across Singapore, Hong Kong, and "
              "other Asian markets. DBS was an early adopter of Avaloq's "
              "SaaS model (Avaloq.one). Key metrics: the implementation "
              "consolidated three legacy systems into one platform, reduced "
              "time-to-market for new structured products from weeks to days, "
              "and enabled DBS to scale its wealth AUM from SGD 200B to "
              "SGD 300B+ between 2019 and 2024 without proportionally "
              "scaling operations headcount.")
        )
        + example(
            "Standard Chartered × Additiv — wealth-as-a-service in ASEAN",
            p("Standard Chartered partnered with Additiv to launch a digital "
              "wealth offering across ASEAN markets using Additiv's DFS "
              "(Digital Finance Suite). The API-first architecture allows "
              "SC to embed wealth capabilities (robo-advisory, goal-based "
              "investing, digital portfolio management) into its mobile "
              "banking app without replacing its existing core banking "
              "stack. The platform serves the mass-affluent segment "
              "(USD 100K–1M AUM) that traditional RM-led models struggle "
              "to serve profitably. Unit economics: a traditional RM serves "
              "50–100 clients; the digital model via Additiv serves "
              "thousands at a fraction of the cost per client.")
        )
        + example(
            "A UK discretionary fund manager on Objectway",
            p("A UK-based discretionary fund manager (DFM) with GBP 15 billion "
              "AUM runs Objectway for portfolio management, order management, "
              "and client reporting. The platform enforces investment mandates "
              "per FCA COBS rules and produces MiFID II cost-and-charges "
              "disclosures automatically. When the FCA's Consumer Duty came "
              "into force (July 2023), the firm used Objectway's reporting "
              "to demonstrate fair-value assessments across fee tiers. "
              "Integration: Objectway connects to the London Stock Exchange, "
              "Bloomberg EMSX for execution, and six custodians via SWIFT "
              "for settlement and reconciliation. Annual platform cost: "
              "approximately GBP 2M — roughly 1.3 basis points on AUM, "
              "well within the industry benchmark of 1–3 bps for "
              "mid-tier DFMs.")
        )
        + example(
            "An Indian PMS provider — building wealth tech on SEBI rails",
            p("A SEBI-registered Portfolio Management Service (PMS) provider "
              "in India manages ₹8,000 crore (approximately USD 950M) across "
              "3,000 HNW clients with a minimum ticket of ₹50 lakh (the SEBI "
              "PMS minimum). The firm uses a combination of in-house Python-"
              "based portfolio analytics, a third-party order management "
              "system connected to NSE/BSE via broker APIs, and Asset Vantage "
              "for consolidated client reporting. Key regulatory constraints: "
              "(1) SEBI mandates monthly portfolio disclosure to clients, "
              "(2) LTCG on equity is 12.5% above ₹1.25 lakh per the 2024 "
              "Union Budget, making tax-lot tracking essential, (3) CKYC "
              "norms require unified KYC across banking and securities, "
              "(4) SEBI's new PMS stewardship code requires ESG disclosure "
              "from 2025. Total technology spend: ₹4 crore/year — "
              "approximately 0.5 bps on AUM.")
        )
    )
    return TopicSection(
        "8.  Worked examples — numbers and decisions", "intermediate", body)


# ------------------------------------------------------------------ sec 9

def _sec9() -> TopicSection:
    body = (
        H3("9.1  Questions a leader asks in any review")
        + ol([
            "What is our wealth-platform strategy — single integrated (Avaloq, "
            "Temenos) or best-of-breed overlay (Aladdin Wealth, Additiv)?",
            "How are we handling multi-custodian aggregation, and what is the "
            "reconciliation-break rate?",
            "Is our suitability engine configured for every jurisdiction we "
            "operate in (MiFID II, Reg BI, MAS FAA-N16, SEBI PMS)?",
            "What is our rebalancing frequency for discretionary mandates, and "
            "how does it handle tax efficiency?",
            "Are we compliant with MiFID II cost-and-charges disclosure and "
            "FCA Consumer Duty fair-value assessment?",
            "What is our client-to-RM ratio by segment, and at what threshold "
            "does the economics break?",
            "Do we have a robo/hybrid offering for mass-affluent, and what is "
            "the cost per client vs. RM-led?",
            "How are we integrating ESG — SFDR Article 8/9 classification, "
            "UK SDR labels, exclusion screening in mandates?",
            "What is our data-residency posture for Swiss banking secrecy, "
            "GDPR, PDPA (Singapore), DPDP Act (India)?",
            "How do we handle alternatives (private equity, real estate, "
            "structured products) — NAV sourcing, valuation frequency, "
            "liquidity locks?",
            "What is our succession-planning and estate-event workflow, and "
            "has it been tested end-to-end?",
            "Are we prepared for DAC6/DAC7/FATCA/CRS cross-border reporting "
            "changes in 2025–26?",
        ])
        + H3("9.2  Red flags")
        + red_flag(ul([
            "'Our core banking system can handle wealth management.' — It "
            "cannot. Core banking manages accounts and transactions; wealth "
            "management needs portfolio analytics, suitability, mandate "
            "compliance, multi-custodian aggregation, and advisory workflow.",
            "'We'll build suitability in Excel.' — This invites regulatory "
            "enforcement. Suitability must be automated, auditable, and "
            "integrated into the order flow.",
            "'We don't need multi-custodian — clients should consolidate with "
            "us.' — UHNW clients will never consolidate. Failing to aggregate "
            "is a competitive disadvantage.",
            "'Robo-advisory is just a rebalancing algorithm.' — It is also "
            "suitability, tax optimisation, client communication, regulatory "
            "disclosure, and ongoing monitoring. Treating it as a simple "
            "algorithm underestimates the compliance burden.",
            "'Our RMs can serve mass-affluent manually.' — Below USD 500K "
            "AUM, the economics of RM-led service typically do not work. "
            "The RM's time costs 30–50 bps but the revenue on mass-affluent "
            "is 40–80 bps. Digital/hybrid is the only profitable model.",
            "'Swiss banking secrecy means we can ignore GDPR.' — Swiss banks "
            "with EU clients must comply with GDPR. Swiss DPA (revDSG, "
            "September 2023) independently imposes similar requirements.",
            "'ESG screening is a nice-to-have.' — Under SFDR, MiFID II "
            "sustainability preferences, and UK SDR, ESG preference capture "
            "and product classification are mandatory for EU/UK distributors.",
            "'We'll migrate the wealth platform over a weekend.' — Wealth "
            "platform migrations are typically 18–36 month programmes with "
            "parallel running. Weekend cutovers are for individual markets, "
            "not the full estate.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("AUM", "Assets Under Management — the total market value of assets "
             "a firm manages on behalf of clients."),
            ("DPM", "Discretionary Portfolio Management — the manager trades on "
             "the client's behalf within agreed mandate limits."),
            ("IPS", "Investment Policy Statement — the document governing a "
             "client's investment objectives, constraints, and preferences."),
            ("Suitability", "The regulatory requirement that every investment "
             "recommendation matches the client's risk profile, knowledge, "
             "financial situation, and objectives."),
            ("MiFID II", "Markets in Financial Instruments Directive II — the EU "
             "framework governing investment services, including suitability, "
             "best execution, cost disclosure, and product governance."),
            ("Reg BI", "SEC Regulation Best Interest — the US broker-dealer "
             "standard for recommendations to retail customers."),
            ("RIA", "Registered Investment Advisor — a US firm registered with "
             "the SEC or state regulators, held to a fiduciary standard."),
            ("PRIIPs KID", "Packaged Retail and Insurance-based Investment "
             "Products Key Information Document — EU-mandated product "
             "disclosure."),
            ("SFDR", "Sustainable Finance Disclosure Regulation — EU "
             "classification of financial products by ESG characteristics "
             "(Article 6/8/9)."),
            ("Tax-loss harvesting", "Selling a losing position to realise a "
             "capital loss that offsets gains elsewhere, reducing the client's "
             "tax bill."),
            ("Direct indexing", "Owning individual securities (instead of an "
             "ETF) to enable stock-level tax-loss harvesting."),
            ("UMA", "Unified Managed Account — a single account structure "
             "that holds multiple investment strategies (models, ETFs, "
             "direct indexing) managed by different sub-advisors."),
            ("Model portfolio", "A pre-built asset allocation that clients "
             "or advisors adopt; changes to the model cascade to all "
             "linked accounts."),
            ("Block trading", "Aggregating orders across multiple client "
             "accounts into a single market order, then allocating fills "
             "pro rata."),
            ("FATCA", "Foreign Account Tax Compliance Act — US law requiring "
             "foreign financial institutions to report US-person accounts."),
            ("CRS", "Common Reporting Standard — the OECD multilateral "
             "automatic exchange of tax information framework."),
            ("NAV", "Net Asset Value — the per-unit or per-share value of a "
             "fund or portfolio."),
            ("HNW / UHNW", "High Net Worth / Ultra-High Net Worth — "
             "client segments defined by investable assets."),
            ("Family office", "A private entity managing the wealth and "
             "affairs of one or a few ultra-wealthy families."),
        ])
    )
    return TopicSection(
        "9.  Questions, red flags, and glossary", "basic", body)
