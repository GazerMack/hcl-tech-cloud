"""BFSI Domain Platforms · 03 — Lending and originations platforms."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="VI.3",
        slug="03-lending-and-originations",
        title="Lending and originations platforms — LOS, LMS, decisioning, collections",
        one_liner=(
            "Lending is where a bank turns deposits into earning assets and "
            "where most of its credit risk is born. The technology that "
            "supports it is split across four platforms: a Loan Origination "
            "System (LOS) that captures and decisions an application; a Loan "
            "Management System (LMS) that services the loan over its life; a "
            "decisioning engine that scores risk; and a collections platform "
            "that handles delinquency. This topic gives you fluent vocabulary "
            "in the major vendors — Newgen, Nucleus FinnOne, Pega, Black "
            "Knight Empower, ICE Mortgage Encompass, FIS ACBS, Unisys "
            "Financial Services System (UFSS), Finastra Fusion "
            "Loan IQ, Temenos, nCino, Blend, Provenir, Experian PowerCurve, "
            "FICO Origination Manager — and the design choices a "
            "techno-functional leader makes across retail, SME, mortgage, "
            "corporate and embedded lending."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("‘Lending platform’ is shorthand for at least four "
              "different systems working together. Knowing which is "
              "which is the difference between a sensible vendor "
              "review and an expensive misunderstanding.")
        )
        + H3("0.1  IT-side anchor — three desks at the bank branch")
        + it_anchor(
            p("Imagine a small branch with three desks. Desk 1 takes "
              "the application, asks for documents, and sends it for "
              "approval — that is the <strong>Loan Origination "
              "System (LOS)</strong>. Desk 2 keeps the loan’s books "
              "for the next 5, 10, 30 years — interest accrual, "
              "EMIs, prepayments, statements — that is the <strong>"
              "Loan Management System (LMS)</strong>. Desk 3 chases "
              "the borrower if they stop paying — that is "
              "<strong>collections</strong>. Behind all three sits a "
              "quiet manager who decides ‘yes / no / how much / what "
              "rate’ — the <strong>decisioning engine</strong>.")
        )
        + H3("0.2  BFSI-side anchor — what happens when you apply for a personal loan")
        + bfsi_anchor(
            p("You tap ‘Apply’ in your bank app. The LOS captures "
              "your details, pulls your bureau report (CIBIL / "
              "Experian / Equifax / TransUnion), pulls bank "
              "statements via Account Aggregator or Open Banking, "
              "evaluates affordability, runs KYC, and asks the "
              "decisioning engine for a verdict — typically inside "
              "3–10 minutes. If approved, the loan is booked in the "
              "LMS, which schedules EMIs and posts to the core "
              "ledger. Months later, if you miss two EMIs, the "
              "collections platform takes over. The four systems are "
              "distinct but must hand off cleanly.")
        )
        + H3("0.3  The four platforms in one paragraph each")
        + ul([
            "<strong>LOS — Loan Origination System</strong>. Captures "
            "the application, runs KYC / AML, pulls bureau and bank-"
            "statement data, calculates eligibility, prices the "
            "loan, generates the agreement, books the loan into the "
            "LMS. Examples: Newgen NewgenONE LOS, Nucleus FinnOne "
            "Neo, ICE Encompass, Black Knight Empower, nCino, Blend, "
            "Pega Smart Dispute, Temenos Origination, Finastra "
            "Fusion Originate, FIS Loan Origination, Lentra, "
            "CloudBankin.",
            "<strong>LMS — Loan Management / Servicing System</strong>. "
            "Schedules EMIs, accrues interest, handles prepayments / "
            "restructuring / charge-off, generates statements, "
            "posts to the GL, supports IFRS 9 / CECL provisioning. "
            "Examples: Nucleus FinnOne Neo LMS, Finastra Fusion "
            "Loan IQ (corporate), Loan IQ on the AWS Cloud, FIS "
            "ACBS, Black Knight MSP, Sagent, ICE / MSP, FinacleCustomer "
            "Loans, BaNCS Loans, Mambu, Thought Machine Vault, "
            "Pennant LSP.",
            "<strong>Decisioning engine</strong>. Runs the rules "
            "and ML models that decide approval, limit, price, and "
            "pricing tier. Examples: FICO Origination Manager / "
            "Decision Modeller, Experian PowerCurve, Provenir, SAS "
            "Real-Time Decision Manager, Pega Customer Decision "
            "Hub, Equifax InterConnect, in-house Python / Spark "
            "stacks at the largest banks.",
            "<strong>Collections platform</strong>. Manages "
            "delinquent accounts, dialler integration, "
            "restructuring, legal escalation, recovery agency "
            "workflows. Examples: FICO Debt Manager / TRIAD, CGI "
            "CACS, Tallyman (Experian), Pega Collections, Indus "
            "Collections, in-house at large banks.",
        ])
    )
    return TopicSection(
        "0.  Primer — four platforms, one customer journey",
        "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Why is lending technology now under heavy modernisation?")
        + ol([
            "<strong>Digital lending growth.</strong> India digital "
            "lending crossed USD 350B disbursed by 2024; UK "
            "consumer-credit fintechs (Zopa, Monzo Loans, "
            "ClearScore) materially shifted share; US mortgage "
            "tech consolidated under ICE (Black Knight) and "
            "Stavvy.",
            "<strong>Regulatory tightening.</strong> RBI Digital "
            "Lending Guidelines (Sept 2022, amended 2024) prescribe "
            "data flow, fee transparency and grievance redress; FCA "
            "Consumer Duty (July 2023) raises the bar on outcomes; "
            "EU Consumer Credit Directive 2 (CCD2, 2023, applies "
            "from November 2026) widens the definition of regulated "
            "credit; CFPB and OCC enforce fair-lending in the US.",
            "<strong>Open Banking and Account Aggregator.</strong> "
            "Bank-statement analysis is now a one-API-call "
            "exercise; that breaks legacy LOS workflows that "
            "assumed paper.",
            "<strong>BNPL and embedded lending.</strong> Klarna, "
            "Affirm, Afterpay, ZestMoney, LazyPay, Capital Float, "
            "Razorpay LOS-as-a-Service: lending is now embedded "
            "into checkouts, payroll, B2B invoicing.",
            "<strong>IFRS 9 / CECL provisioning.</strong> Forward-"
            "looking expected-credit-loss models drive a constant "
            "feedback loop between collections, LMS and risk; data "
            "must flow cleanly.",
            "<strong>AI in underwriting and collections.</strong> "
            "Generative AI for document understanding (KYC, salary "
            "slips, GST returns); ML for behavioural scoring; "
            "agentic flows for collections triage.",
        ])
    )
    return TopicSection(
        "1.  Why lending tech is under heavy modernisation",
        "basic", body)


def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  subgraph "Origination — LOS"\n'
            '    A["Application capture<br/>mobile / branch / partner"]\n'
            '    K["KYC and identity<br/>Aadhaar eKYC / SingPass / GOV.UK / Onfido"]\n'
            '    D["Data pull<br/>bureau, AA, Open Banking, GST"]\n'
            '    E["Eligibility and pricing"]\n'
            '    Ag["Agreement and e-sign"]\n'
            '  end\n'
            '  subgraph "Decisioning"\n'
            '    R["Rules engine<br/>policy + scorecards"]\n'
            '    M["ML models<br/>PD, LGD, EAD"]\n'
            '    F["Fraud and AML"]\n'
            '  end\n'
            '  subgraph "Servicing — LMS"\n'
            '    B["Booking to GL"]\n'
            '    S["EMI schedule, accruals"]\n'
            '    P["Prepayment, restructure, foreclosure"]\n'
            '  end\n'
            '  subgraph "Collections and recovery"\n'
            '    C["Bucket-wise treatment"]\n'
            '    Di["Dialler / digital outreach"]\n'
            '    L["Legal and recovery"]\n'
            '  end\n'
            '  A --> K --> D --> E\n'
            '  E --> R\n'
            '  E --> M\n'
            '  E --> F\n'
            '  R --> Ag\n'
            '  M --> Ag\n'
            '  F --> Ag\n'
            '  Ag --> B --> S --> P\n'
            '  S --> C --> Di --> L',
            "Reference flow of a lending platform: LOS captures and "
            "scores; decisioning approves; LMS services; collections "
            "handles delinquency.")
    )
    return TopicSection(
        "2.  The picture — LOS, decisioning, LMS, collections",
        "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  Loan products you must recognise on sight")
        + ul([
            "<strong>Retail unsecured</strong> — personal loan, "
            "credit-card EMI, salary advance.",
            "<strong>Retail secured</strong> — auto loan, gold "
            "loan, loan against property, loan against securities.",
            "<strong>Mortgage</strong> — home loan; long tenor; "
            "specialised servicing (escrow, taxes, insurance in "
            "the US; LTV monitoring everywhere).",
            "<strong>SME / MSME</strong> — working-capital loan, "
            "term loan, invoice / supply-chain finance, "
            "GST-based credit.",
            "<strong>Corporate / wholesale</strong> — bilateral "
            "term loan, syndicated loan, revolving credit "
            "facility (RCF), trade finance, ECA-backed.",
            "<strong>Specialised</strong> — credit card, BNPL, "
            "education, student, microfinance, agricultural, "
            "embedded.",
        ])
        + H3("3.2  The major LOS / LMS vendors and where they win")
        + table(
            ["Vendor / platform", "Strength", "Where you’ll see it"],
            [
                ["<strong>Newgen NewgenONE LOS</strong>",
                 "BPM-based, configurable workflows; strong in "
                 "Indian retail and SME LOS; strong document "
                 "management.",
                 "Many Indian PSU and private banks (SBI, BoB, "
                 "Canara, ICICI components), Middle East and "
                 "South-East Asian banks."],
                ["<strong>Nucleus FinnOne Neo (LOS + LMS)</strong>",
                 "End-to-end retail and SME lending; strong in "
                 "India and emerging markets; cloud-deployable.",
                 "HDFC Bank components, Bajaj Finserv, Tata Capital, "
                 "SBI Card, several Indonesian and African banks."],
                ["<strong>ICE Mortgage Technology Encompass</strong>",
                 "Dominant US mortgage LOS; integrated with ICE "
                 "MSP servicing post-Black Knight acquisition.",
                 "Most mid- and large US mortgage lenders."],
                ["<strong>Black Knight MSP / Empower</strong>",
                 "MSP is the dominant US mortgage servicing "
                 "platform (>60% market share); Empower is the "
                 "LOS partner.",
                 "Most US mortgage servicers; bought by ICE in 2023."],
                ["<strong>nCino</strong>",
                 "Salesforce-native commercial-loan LOS; strong in "
                 "US community and mid-tier banks; expanding to "
                 "EU and APAC.",
                 "Mid-tier US banks, several UK / EU banks, ANZ-"
                 "region community banks."],
                ["<strong>Blend</strong>",
                 "Consumer-lending LOS for US banks; mortgage and "
                 "consumer credit; cloud-native.",
                 "Wells Fargo home-lending, US Bank, M&amp;T, "
                 "Truist."],
                ["<strong>Pega</strong>",
                 "BPM and decisioning combined; case management "
                 "for mortgage and corporate workflows; strong "
                 "Customer Decision Hub.",
                 "Citi Consumer, Bank of America, ANZ, Lloyds, "
                 "many EU banks."],
                ["<strong>Finastra Fusion Loan IQ</strong>",
                 "Dominant corporate / syndicated-loan servicing "
                 "platform; rich agency and participation "
                 "support.",
                 "Most tier-1 syndicated-loan agents (JPM, Citi, "
                 "BofA, BNP, HSBC, Barclays use components)."],
                ["<strong>FIS Commercial Lending Suite (ACBS)</strong>",
                 "Long-standing commercial-loan servicing; deep "
                 "in US and EU corporate banks.",
                 "Many US regionals, EU corporate banks."],
                ["<strong>Temenos Origination + Loans</strong>",
                 "Native to Temenos Transact estate; cloud "
                 "delivery via Temenos Banking Cloud.",
                 "ABN AMRO, Bank of Sharjah, several APAC "
                 "and African banks."],
                ["<strong>TCS BaNCS Loans, Infosys Finacle "
                 "Lending</strong>",
                 "Indian-origin suites used widely in Indian PSUs "
                 "and across APAC, Middle East, Africa.",
                 "SBI, BoB, Canara, ICICI, Axis, AU SFB."],
                ["<strong>Mambu, Thought Machine Vault, "
                 "Pennant LSP</strong>",
                 "Cloud-native lending engines; product-builder "
                 "approach; popular at neobanks and digital "
                 "lenders.",
                 "Tonik, Tyme, N26 (parts), Standard Chartered "
                 "Mox, JPM Chase UK (Vault), Lloyds (Thought "
                 "Machine), GXS / Trust Singapore."],
                ["<strong>Lentra, CloudBankin, FinBox, "
                 "Yubi</strong>",
                 "Indian fintech-platform LOS / decisioning "
                 "providers; rapidly adopted by NBFCs and SFBs.",
                 "Many Indian NBFCs, small-finance banks, and "
                 "fintech lenders."],
                ["<strong>Sagent, MSP, Servicing Director, "
                 "FICS</strong>",
                 "US mortgage servicing platforms; ICE-MSP "
                 "dominates, Sagent is the cloud-native "
                 "challenger.",
                 "US mortgage servicers."],
            ]
        )
        + H3("3.3  Decisioning engines — rules + scorecards + ML")
        + ul([
            "<strong>FICO Origination Manager / Decision Modeller "
            "/ Blaze Advisor</strong> — rules + scorecards; "
            "ubiquitous in retail.",
            "<strong>Experian PowerCurve</strong> — origination, "
            "customer management, collections; deep bureau "
            "integration.",
            "<strong>Provenir</strong> — cloud-native decisioning "
            "with marketplace integrations to data providers; "
            "strong at fintech lenders.",
            "<strong>SAS Real-Time Decision Manager</strong> — "
            "enterprise rules + analytics for tier-1 banks.",
            "<strong>Pega Customer Decision Hub</strong> — next-"
            "best-action and credit decisioning combined.",
            "<strong>Equifax InterConnect, TransUnion DecisionEdge, "
            "CRIF Strategy One</strong> — bureau-anchored "
            "decisioning suites.",
            "<strong>In-house Python / Spark / Databricks</strong> "
            "— at the very largest banks (JPM, Capital One, HDFC, "
            "Goldman Marcus) for ML scoring and "
            "challenger-model deployment.",
        ])
        + H3("3.4  KYC, identity and data sources")
        + ul([
            "<strong>India</strong> — Aadhaar e-KYC and Aadhaar-"
            "based authentication via UIDAI, Video KYC "
            "(RBI 2020 amendment), CKYC central KYC registry, "
            "DigiLocker for document fetch, Account Aggregator "
            "for bank-statement and GST data, GSTN for business "
            "data, NSDL / CDSL for securities, CIBIL / Experian "
            "/ Equifax / CRIF Highmark bureaus.",
            "<strong>UK / EU</strong> — Open Banking AISP for "
            "transaction data, Onfido / Jumio / Veriff / "
            "iProov for ID verification, Experian / Equifax / "
            "TransUnion bureaus, Companies House for corporate "
            "data, eIDAS QTSPs for qualified e-sign.",
            "<strong>US</strong> — Plaid / MX / Yodlee / Finicity "
            "for bank-statement aggregation, LexisNexis Risk, "
            "Equifax / Experian / TransUnion FICO bureaus, "
            "Verification of Employment (TheWorkNumber).",
            "<strong>Singapore / HK / AUS</strong> — SingPass "
            "MyInfo, HKID, Australian Document Verification "
            "Service (DVS), iAM Smart in HK, illion / Equifax "
            "AU bureaus.",
        ])
        + H3("3.5  Servicing concerns — what an LMS must handle")
        + ul([
            "<strong>Schedule and accrual</strong> — equated, "
            "stepped, balloon, bullet; daily vs monthly accrual; "
            "day-count conventions (30/360, ACT/365).",
            "<strong>Repricing</strong> — fixed, floating, "
            "reset frequency; benchmark migration (LIBOR → SOFR, "
            "EONIA → €STR, MIBOR-OIS, SONIA, TONA).",
            "<strong>Prepayment, partial prepayment, foreclosure</strong> "
            "— with regulatory caps on charges in many markets.",
            "<strong>Restructuring and moratorium</strong> — "
            "COVID-era moratoria, RBI restructuring frameworks "
            "(MSME, retail), CFPB loss mitigation rules.",
            "<strong>Charge-off, write-off, NPL classification</strong> "
            "— stage 1 / 2 / 3 under IFRS 9; substandard / "
            "doubtful / loss under RBI; expected vs incurred "
            "loss.",
            "<strong>Provisioning</strong> — IFRS 9 ECL, US CECL "
            "(in force since Jan 2020 for SEC filers), "
            "RBI standardised approach, Basel IRB.",
            "<strong>Statements and disclosures</strong> — "
            "Truth-in-Lending (US Reg Z), CCA (UK), Key Fact "
            "Statement (RBI), ESIS (EU MCD).",
        ])
        + H3("3.6  Collections — the operational front line")
        + ul([
            "<strong>Buckets</strong> — DPD (days past due) 1–30, "
            "31–60, 61–90, 90+; treatment differs per bucket.",
            "<strong>Channels</strong> — IVR, SMS, email, "
            "WhatsApp / RCS, dialler, field agent, legal notice; "
            "regulated by RBI Recovery Code, FCA CONC, US FDCPA.",
            "<strong>Skip tracing</strong> — locating borrowers "
            "who have moved or changed numbers.",
            "<strong>Restructuring vs charge-off vs sale</strong> "
            "— ARC / NPL sales (India), securitisation, NPL "
            "platforms (intrum, Cerberus, Lone Star) in EU.",
            "<strong>Vendor platforms</strong> — FICO Debt Manager "
            "/ TRIAD, CGI CACS, Tallyman (Experian), Pega "
            "Collections, Indus Collections, Spinwheel, Symend, "
            "Katabat, TrueAccord.",
        ])
        + H3("3.7  HCLTech BA field guide — Loan IQ, ACBS, UFSS, nCino and Finastra")
        + primer(
            p("In an HCLTech BFSI Business Analyst role, these names usually appear in transformation, "
              "migration, support, testing or integration programmes. Do not memorise them as random "
              "vendor names. Place each app in the lending value chain: nCino usually sits near front-office "
              "origination and relationship-manager workflow; Loan IQ and ACBS usually sit in commercial-loan "
              "servicing and agency operations; UFSS is typically a legacy Unisys core or mortgage/savings "
              "platform in UK building-society style estates; Finastra is the vendor family, not one single "
              "application.")
        )
        + mermaid(
            'flowchart LR\n'
            '  A["Relationship manager or customer"] --> B["nCino or LOS workflow"]\n'
            '  B --> C["Credit decision and approvals"]\n'
            '  C --> D["Facility setup"]\n'
            '  D --> E["Loan IQ or ACBS servicing"]\n'
            '  D --> U["UFSS or legacy core for some estates"]\n'
            '  E --> F["General ledger and accounting"]\n'
            '  E --> G["Payments and notices"]\n'
            '  E --> H["Risk, covenants and reporting"]\n'
            '  U --> F\n'
            '  U --> G',
            "Where these applications usually sit: origination captures and approves; servicing runs the loan after booking; legacy cores may still hold product, account or mortgage truth."
        )
        + table(
            ["App / vendor name", "What it is in plain English", "Where it sits", "What a BA must understand"],
            [
                ["<strong>Finastra Loan IQ</strong>", "A commercial and syndicated-loan servicing platform. It manages facilities, drawdowns, rollovers, repayments, interest, fees, lender shares, agent-bank activity, notices and accounting events.", "Middle and back office for corporate, syndicated, bilateral, commercial real-estate, private-credit and specialised lending.", "Facility and tranche structure, agency vs participant role, repricing, fee schedules, rate benchmarks, accounting, notices, covenants, interfaces to GL, payments, risk and data warehouse."],
                ["<strong>FIS ACBS</strong>", "A long-standing commercial-loan servicing system, commonly expanded as Advanced Commercial Banking System. It is often seen in corporate banks and regional banks that have mature commercial-loan books.", "Commercial-loan servicing, loan operations, agency, participation and back-office processing.", "How ACBS product setup maps to client lending products, how balances and accruals reconcile, what batch jobs and interfaces feed downstream risk, finance, regulatory and customer-notice systems."],
                ["<strong>UFSS — Unisys Financial Services System</strong>", "A legacy Unisys financial-services/core-banking platform, publicly associated with UK building societies and mortgage/savings estates. In projects, the exact acronym can be client-specific, so confirm the client glossary on day one.", "Legacy core, mortgage, savings or servicing layer in older UK-style mutual/building-society estates.", "Current-state process discovery, data extraction, product mapping, account and customer master mapping, batch dependencies, retirement/upgrade scope and risk around legacy screens and reports."],
                ["<strong>nCino</strong>", "A Salesforce-native cloud banking platform used heavily for commercial loan origination, relationship-manager workflow, credit memo, document collection, approvals and portfolio monitoring.", "Front office and middle office, before the loan is booked into a servicing system such as Loan IQ, ACBS or a core lending engine.", "Salesforce objects, workflow stages, credit memo fields, approval routes, document checklist, spreading/financial analysis, covenant tracking, integration to servicing/core, and user adoption for relationship managers."],
                ["<strong>Finastra</strong>", "A financial-software vendor, not one product. In lending, the relevant products can include Loan IQ, Fusion Originate, LaserPro and other lending components; in other domains Finastra also appears in payments, treasury, trade and universal banking.", "Vendor estate across lending, payments, treasury, trade finance and core/universal banking depending on client.", "Always ask which Finastra product is in scope. ‘Finastra issue’ is too vague for requirements, testing or defect triage."],
            ]
        )
        + H3("3.8  The commercial-loan vocabulary behind Loan IQ and ACBS")
        + p("Loan IQ and ACBS are difficult for new BAs because corporate lending is not like a simple personal "
            "loan. One large borrower may have a facility of USD 500 million, split into tranches, with multiple "
            "lenders, different currencies, floating rates, commitment fees, utilisation fees, covenants and "
            "agent-bank notices. The application is not just storing ‘loan amount and EMI’. It is running a "
            "multi-party contract over years.")
        + table(
            ["Term", "Meaning", "Example"],
            [
                ["Facility", "The overall credit agreement or limit.", "A corporate borrower gets a USD 500 million revolving credit facility."],
                ["Tranche", "A slice of the facility with specific terms.", "USD tranche and EUR tranche under the same facility."],
                ["Drawdown / utilisation", "Borrower actually takes money from the available facility.", "Borrower draws USD 75 million for 90 days."],
                ["Rollover", "A maturing drawdown is renewed for another interest period.", "USD 75 million rolls from one-month SOFR to three-month SOFR."],
                ["Syndicated loan", "Multiple lenders share one large loan.", "JPM acts as agent, ten banks each hold a share."],
                ["Agent bank", "Bank that administers the facility for the syndicate.", "Calculates interest, sends notices, distributes payments to lenders."],
                ["Participant / lender share", "Each lender's percentage of exposure.", "Bank A owns 20%, Bank B owns 15%."],
                ["Covenant", "Contractual promise the borrower must maintain.", "Debt-to-EBITDA must stay below 3.5x."],
                ["Fee schedule", "Commitment, arrangement, agency, utilisation or amendment fees.", "0.35% annual commitment fee on undrawn amount."],
                ["Rate benchmark and margin", "Reference rate plus agreed spread.", "SOFR + 225 basis points."],
            ]
        )
        + example("A syndicated-loan servicing flow in numbers",
            ol([
                "A borrower signs a USD 500 million revolving credit facility with five lenders.",
                "Citi is the agent bank. Each lender has a share: Citi 30%, Barclays 25%, HSBC 20%, Deutsche Bank 15%, NatWest 10%.",
                "The borrower draws USD 100 million for 90 days at SOFR 5.30% plus margin 2.00%, so annual rate is 7.30%.",
                "Approximate 90-day interest on ACT/360 is USD 100,000,000 × 7.30% × 90 ÷ 360 = USD 1,825,000.",
                "The servicing system calculates the borrower receivable, allocates lender shares, raises notices, posts accounting entries and feeds risk exposure.",
                "If the borrower repays USD 40 million and rolls USD 60 million, the app must update balances, accruals, limits, lender positions and GL postings without breaking reconciliation.",
            ])
        )
        + H3("3.9  How nCino connects to servicing platforms")
        + p("nCino is often closer to the relationship manager and credit officer than to the loan-operations "
            "team. It helps capture opportunity details, financial spreads, credit memo, approval workflow, "
            "document checklist and covenant monitoring. Once approved, the booked loan may be handed off to "
            "Loan IQ, ACBS, a core banking system or another LMS for servicing. The BA risk is assuming that "
            "the nCino approval data automatically matches the servicing-system booking fields. It rarely does "
            "without careful mapping.")
        + table(
            ["nCino object or process", "Servicing-system equivalent", "BA mapping question"],
            [
                ["Relationship / account", "Borrower, obligor, customer master.", "Which system owns legal customer identity and hierarchy?"],
                ["Opportunity or loan request", "Facility or loan setup instruction.", "Which fields become contractual terms versus sales pipeline fields?"],
                ["Credit memo", "Approval and policy evidence.", "Which approved terms must be locked before booking?"],
                ["Collateral record", "Collateral or security module.", "How are valuations, lien priority and release rules represented downstream?"],
                ["Covenant tracking", "Covenant schedule and monitoring alerts.", "Does nCino monitor covenants, or does servicing/risk own them after booking?"],
                ["Document checklist", "Document repository and conditions precedent.", "Which documents block drawdown and which are post-closing follow-ups?"],
                ["Approval workflow", "Booking authorisation and maker-checker.", "Does servicing require a separate maker-checker even after nCino approval?"],
            ]
        )
        + H3("3.10  What HCLTech expects from a BA on these apps")
        + table(
            ["BA responsibility", "What it means on these platforms", "Concrete output"],
            [
                ["Current-state discovery", "Sit with relationship managers, credit officers, loan operations, finance, risk and technology to document how the loan really moves today.", "Process maps, pain-point log, application inventory, screen/report catalogue."],
                ["Requirement elicitation", "Translate business needs into system behaviour across nCino, Loan IQ, ACBS, UFSS, Finastra modules and downstream systems.", "Business Requirement Document, user stories, acceptance criteria, non-functional requirements."],
                ["Product and data mapping", "Map facility, tranche, customer, collateral, covenant, fee, rate, GL and notice fields across source and target systems.", "Data dictionary, source-to-target mapping, transformation rules, data-quality rules."],
                ["Gap analysis", "Compare package capability with client process and decide configure, customise, integrate, change process or de-scope.", "Fit-gap matrix with disposition, priority, owner and regulatory impact."],
                ["Interface analysis", "Understand feeds to core, GL, payment hub, document store, data lake, risk, regulatory reporting and customer communications.", "Interface catalogue, message/file specification, event list, reconciliation controls."],
                ["Testing and UAT", "Write test scenarios for drawdown, rollover, repayment, fee accrual, covenant breach, rate reset, notice generation, GL posting and migration reconciliation.", "System Integration Testing scripts, User Acceptance Testing scripts, defect triage notes, evidence pack."],
                ["Migration support", "Move open facilities, balances, accruals, customer data, documents, limits, covenants and historical records from legacy to target.", "Migration scope, mock-run plan, reconciliation report, cutover checklist."],
                ["Operations readiness", "Make sure users can run day-1 operations after go-live.", "Standard operating procedures, training deck, role matrix, maker-checker controls, runbook."],
            ]
        )
        + H3("3.11  BA interview and project language you should be able to speak")
        + callout("What to say in an HCLTech BFSI conversation",
            ul([
                "‘nCino is usually upstream origination and workflow; Loan IQ or ACBS is usually downstream servicing. My first task is to confirm system-of-record boundaries.’",
                "‘For Loan IQ or ACBS, I will ask about facility, tranche, drawdown, rollover, repricing, fee, covenant, lender-share, accounting and notice flows.’",
                "‘For UFSS, I will not assume a universal meaning. I will confirm whether the client means Unisys Financial Services System or a client-specific acronym, then map its products, batch jobs, interfaces and reports.’",
                "‘For Finastra, I will ask which product is in scope: Loan IQ, Fusion Originate, LaserPro, Essence, Global PAYplus, Trade Innovation, Summit or another module.’",
                "‘My BA artefacts would include process maps, fit-gap, source-to-target mapping, interface catalogue, test scenarios, migration reconciliation and UAT evidence.’",
            ]),
            "info")
    )
    return TopicSection(
        "3.  How lending tech actually works — products, vendors, "
        "decisioning, servicing, collections",
        "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  India — RBI Digital Lending and the AA stack")
        + ul([
            "<strong>RBI Digital Lending Guidelines</strong> "
            "(Sept 2022, amended 2024) — disbursal directly to "
            "borrower’s account, no pass-through wallets; all "
            "fees disclosed in a Key Fact Statement; cooling-off "
            "period; cap on default loss guarantee (DLG) at 5% "
            "from June 2023.",
            "<strong>Account Aggregator (AA)</strong> ecosystem "
            "is now mainstream — RBI-licensed AAs (CAMSFinServ, "
            "OneMoney, NeSL, Yodlee, Finvu, Perfios) provide "
            "bank-statement data with consent. AA is the death "
            "of paper-statement underwriting.",
            "<strong>Open Credit Enablement Network (OCEN)</strong> "
            "— protocol for embedded credit; 2024–25 saw rapid "
            "adoption for cash-flow lending to MSMEs.",
            "<strong>Unified Lending Interface (ULI)</strong> — "
            "RBI-led platform launched in 2024 to standardise "
            "data exchange across banks, NBFCs and data "
            "providers; analogous to UPI for credit.",
            "<strong>Bureau and data</strong> — CIBIL, Experian, "
            "Equifax, CRIF Highmark; GSTN-based MSME lending; "
            "ITR via Income Tax Department portal.",
        ])
        + H3("4.2  United States — mortgage, CRA, fair-lending")
        + ul([
            "<strong>TILA / RESPA / TRID</strong> — disclosure "
            "regimes for consumer credit and mortgages.",
            "<strong>CFPB</strong> — Consumer Financial Protection "
            "Bureau supervises consumer-lending conduct; "
            "Section 1071 small-business lending data collection "
            "rule finalised 2023.",
            "<strong>Fair-lending</strong> — Equal Credit "
            "Opportunity Act (ECOA, Reg B), Fair Housing Act, "
            "Community Reinvestment Act; intense regulator "
            "focus on disparate-impact testing of ML models.",
            "<strong>CECL</strong> — Current Expected Credit "
            "Loss; in force for SEC filers since Jan 2020.",
            "<strong>Mortgage stack</strong> — ICE Encompass + "
            "MSP dominates post-2023; Sagent is the cloud-"
            "native challenger to MSP.",
        ])
        + H3("4.3  United Kingdom and Eurozone")
        + ul([
            "<strong>FCA Consumer Duty</strong> (July 2023) — "
            "outcomes-based regulation; LOS and decisioning must "
            "evidence fair value and customer understanding.",
            "<strong>FCA CONC</strong> — Consumer Credit "
            "sourcebook; affordability assessment.",
            "<strong>FCA BNPL regulation</strong> — coming "
            "into scope under HM Treasury draft 2024; expected "
            "in force 2026.",
            "<strong>UK Mortgage Charter</strong> (2023) — "
            "voluntary forbearance options for borrowers in "
            "rate stress.",
            "<strong>EU Consumer Credit Directive 2 (CCD2)</strong> "
            "— adopted 2023; applies from <strong>20 November "
            "2026</strong>; widens scope to BNPL and small "
            "loans; mandates affordability assessment and "
            "early-repayment rights.",
            "<strong>EU Mortgage Credit Directive (MCD)</strong> "
            "— ESIS disclosure, 7-day reflection period.",
            "<strong>EU AI Act</strong> — credit scoring is "
            "‘high risk’; conformity assessment, post-market "
            "monitoring required.",
        ])
        + H3("4.4  Singapore, Australia, Brazil")
        + ul([
            "<strong>MAS</strong> — Total Debt Servicing Ratio "
            "(TDSR), Mortgage Servicing Ratio (MSR) policies; "
            "MAS FEAT for AI in credit.",
            "<strong>Australia APRA APS 220</strong> Credit Risk "
            "Management; Responsible Lending Obligations under "
            "the National Consumer Credit Protection Act; "
            "Banking Code of Practice.",
            "<strong>Brazil Open Finance</strong> mandates data "
            "portability that powers lending; rapid growth of "
            "embedded credit and PIX-anchored lending.",
        ])
    )
    return TopicSection(
        "4.  Region by region — regulators and ecosystem, current "
        "as of 2025",
        "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  Affordability and responsible lending")
        + p("Affordability assessment is now an outcomes test, not "
            "a checkbox. UK FCA CONC, EU CCD2, RBI Digital Lending "
            "Guidelines, Australian Responsible Lending and US "
            "ATR/QM all require evidence that the borrower can "
            "repay without undue hardship. Engines must:")
        + ul([
            "Pull income evidence (payslips, AA statements, "
            "tax returns, GST).",
            "Compute disposable income net of essential "
            "expenditure (UK ONS-aligned categories or local "
            "equivalents).",
            "Apply stress (rate +3 ppt, expense +10%) before "
            "approving.",
            "Document the decision so it can be reproduced and "
            "audited 7 years later.",
        ])
        + H3("5.2  Model risk management — SR 11-7, PRA SS1/23, "
             "RBI 2024")
        + ul([
            "<strong>US Fed SR 11-7</strong> (2011) — the "
            "canonical model-risk reference: development, "
            "validation, governance, ongoing monitoring.",
            "<strong>UK PRA SS1/23</strong> (2023) — modernised "
            "model-risk framework; explicit AI/ML coverage.",
            "<strong>RBI Discussion Paper on Model Risk</strong> "
            "(2024) — direction of travel for Indian banks.",
            "<strong>EU AI Act + EBA Guidelines</strong> — "
            "specific obligations for ML in credit "
            "decisioning.",
            "<strong>Champion-challenger</strong> — production "
            "model (champion) vs alternative (challenger); "
            "monitor population stability, characteristic "
            "stability, and Gini / KS performance over time.",
            "<strong>Explainability</strong> — SHAP, LIME, "
            "EBM; reason codes mandatory under ECOA / FCRA "
            "/ RBI / EU AI Act.",
        ])
        + H3("5.3  IFRS 9 and CECL — the provisioning machine")
        + ul([
            "<strong>IFRS 9 stages</strong> — stage 1 (12-month "
            "ECL), stage 2 (lifetime ECL, no default yet), "
            "stage 3 (lifetime ECL, defaulted).",
            "<strong>PD, LGD, EAD</strong> — Probability of "
            "Default, Loss Given Default, Exposure At Default; "
            "the three drivers of expected credit loss.",
            "<strong>Significant Increase in Credit Risk "
            "(SICR)</strong> — moves an asset from stage 1 to "
            "stage 2; trigger logic must be defined and "
            "evidenced.",
            "<strong>Forward-looking macroeconomic overlays</strong> "
            "— ECL must reflect plausible future scenarios.",
            "<strong>CECL</strong> (US) — lifetime ECL from "
            "day 1 for all loans; no staging; effective "
            "since Jan 2020 for SEC filers.",
        ])
        + H3("5.4  Embedded lending and BNPL")
        + ul([
            "<strong>Buy Now Pay Later</strong> — Klarna, "
            "Affirm, Afterpay (Block), Zip; LazyPay, Simpl, "
            "ZestMoney, Snapmint in India.",
            "<strong>Merchant-embedded</strong> — checkout "
            "lending integrated via SDK; risk decisioned in "
            "<200 ms.",
            "<strong>Payroll-embedded</strong> — earned-wage "
            "access (DailyPay, Wagestream, Refyne).",
            "<strong>B2B embedded</strong> — invoice finance, "
            "supply-chain finance via Razorpay Capital, "
            "Liberis, C2FO.",
            "<strong>Regulatory tightening</strong> — UK FCA "
            "BNPL 2026, EU CCD2 BNPL inclusion 2026, RBI "
            "FLDG cap 2023, US CFPB 2024 interpretive rule "
            "treating BNPL as credit cards.",
        ])
        + H3("5.5  AI in lending — ten things changing right now")
        + ul([
            "<strong>Document understanding</strong> — extract "
            "data from payslips, ITRs, GST returns, bank "
            "statements with vision LLMs.",
            "<strong>Cash-flow underwriting</strong> — replace "
            "or augment bureau-only scoring with transaction-"
            "level analysis.",
            "<strong>Conversational origination</strong> — "
            "WhatsApp / chat-based application capture in "
            "vernacular languages.",
            "<strong>Voice-bot collections</strong> — "
            "conversational reminders and arrangements at "
            "scale.",
            "<strong>Personalised offers</strong> — pre-"
            "approved-offer engines fed by behavioural data.",
            "<strong>Explainable scorecards</strong> — EBM and "
            "monotonic GBMs for regulator-acceptable models.",
            "<strong>Model monitoring</strong> — drift detection, "
            "fairness metrics, automated alerts.",
            "<strong>Synthetic data</strong> — for testing and "
            "model development without exposing PII.",
            "<strong>Agentic operations</strong> — exception "
            "handling and case routing in collections.",
            "<strong>Vendor consolidation</strong> — Provenir, "
            "Datrics, Zest AI, Taktile competing on full "
            "decisioning stack.",
        ])
    )
    return TopicSection(
        "5.  Advanced — affordability, model risk, IFRS 9 / CECL, "
        "embedded lending, AI",
        "advanced", body)


def _sec6() -> TopicSection:
    body = (
        H3("6.1  Choosing an LOS / LMS — eight-question framework")
        + ol([
            "Which products in scope on day 1, day 365, day 1,825 — "
            "retail, SME, mortgage, corporate, BNPL?",
            "What is the integration with our core banking, "
            "payments engine, GL, bureaus and AA / Open Banking?",
            "Is the decisioning embedded or pluggable? Can we "
            "deploy challenger ML models without a vendor "
            "release?",
            "Cloud-native containers, vendor-cloud SaaS, or on-"
            "prem only? Does our regulator accept the model?",
            "Configurability of products and pricing — can a "
            "business analyst change a parameter without code?",
            "Document and e-sign integration — DigiLocker, "
            "DocuSign, Adobe Sign, Aadhaar e-sign, eIDAS "
            "qualified.",
            "What is the audit and explainability story for "
            "model-driven decisions?",
            "What is the upgrade cadence, the back-compat "
            "record, and the reference-customer experience on "
            "the last major upgrade?",
        ])
        + H3("6.2  Build, buy, or platform-as-a-service")
        + table(
            ["Option", "When it wins", "Watch-outs"],
            [
                ["<strong>Buy a packaged LOS + LMS</strong>",
                 "Most incumbents; tight regulator alignment; "
                 "deep skill pool of implementers (HCLTech, TCS, "
                 "Infosys, Wipro, Capgemini, Accenture).",
                 "Customisation cost; vendor lock-in; upgrade "
                 "windows."],
                ["<strong>Cloud-native lending engine "
                 "(Mambu, Thought Machine Vault, Pennant "
                 "LSP)</strong>",
                 "Greenfield digital banks and new product "
                 "launches; product-as-config; rapid time-to-"
                 "market.",
                 "Less out-of-the-box for legacy product "
                 "shapes; enterprise integration takes work."],
                ["<strong>Lending-as-a-Service "
                 "(Lentra, CloudBankin, FinBox, Zoot, "
                 "Provenir)</strong>",
                 "Smaller banks, NBFCs, fintechs without 24×7 "
                 "ops; regulator increasingly comfortable.",
                 "Concentration risk; exit plan required."],
                ["<strong>Build in-house</strong>",
                 "Very large banks where lending is the "
                 "differentiator (Capital One, Goldman Marcus, "
                 "Nubank).",
                 "Decade-scale investment; staffing and "
                 "regulator burden you must own."],
            ]
        )
        + H3("6.3  Decision matrix — decisioning engine choice")
        + table(
            ["Choice", "When it wins", "Watch-outs"],
            [
                ["<strong>FICO / Experian / SAS / Pega — "
                 "incumbent decisioning</strong>",
                 "Deep regulator and bureau ties; mature "
                 "scorecards; broad implementer pool.",
                 "Run-rate licence cost; ML deployment can be "
                 "vendor-paced."],
                ["<strong>Provenir, Taktile, Zest AI, "
                 "Datrics</strong>",
                 "Cloud-native; data-marketplace integrations; "
                 "rapid challenger-model deployment.",
                 "Younger; verify regulator references in your "
                 "jurisdiction."],
                ["<strong>In-house Python / Spark / "
                 "Databricks</strong>",
                 "Largest banks; fully customised; integrates "
                 "with bank-wide MLOps.",
                 "Real engineering and governance "
                 "responsibility you must staff."],
            ]
        )
    )
    return TopicSection(
        "6.  Decision matrices — LOS/LMS choice, build vs buy, "
        "decisioning",
        "intermediate", body)


def _sec7() -> TopicSection:
    body = (
        example(
            "HDFC Bank — Xpress Personal Loans on a modern stack",
            ol([
                "HDFC offers ‘10-second loan’ pre-approved personal "
                "loans to existing customers; salaried instant "
                "loans for new-to-bank under 30 minutes.",
                "Stack combines Finacle / in-house core, Newgen / "
                "Nucleus components for LOS, in-house decisioning "
                "with bureau (CIBIL) and Account Aggregator data, "
                "Aadhaar e-KYC for identity, e-sign for agreement.",
                "Public lessons: pre-approved offers + real-time "
                "decisioning + AA bank-statement pull turns a "
                "branch process into a tap.",
            ])
        )
        + example(
            "Goldman Sachs Marcus — what a tier-1 in-house build "
            "looks like",
            ol([
                "Marcus launched in 2016 as a digital consumer-"
                "lending platform; in-house LOS/LMS on AWS; "
                "cloud-native from day one.",
                "Acquired Clarity Money (2018) and Honest Dollar; "
                "later integrated Apple Card servicing.",
                "Strategic pivot from 2022 — consumer-lending "
                "ambitions scaled back; assets sold to "
                "GreenSky and others; Apple Card servicing "
                "transitioning out by 2025.",
                "Lesson: tier-1 in-house build is feasible, but "
                "strategic commitment matters as much as "
                "technology choice.",
            ])
        )
        + example(
            "Lloyds Banking Group on Thought Machine Vault — "
            "core + lending modernisation",
            ol([
                "Lloyds invested in Thought Machine and is "
                "progressively migrating products to Vault — "
                "smart-contract-based core that supports "
                "lending products as configuration.",
                "Phased migration (savings first, lending "
                "products following) is a textbook strangler-"
                "fig from incumbent core.",
                "Public lessons: cloud-native lending engine "
                "delivered at incumbent scale is achievable, "
                "but slow and rigorously governed.",
            ])
        )
        + example(
            "An Indian NBFC on Lentra + Provenir — fast launch",
            ol([
                "Mid-sized NBFC needed to launch consumer "
                "durable + personal-loan products in 90 days.",
                "Picked Lentra for LOS, Provenir for "
                "decisioning, AA for bank-statement data, "
                "DigiLocker + Aadhaar e-KYC for identity, in-"
                "house LMS on a Mambu-style cloud engine.",
                "Time-to-first-disbursal: 14 weeks. Year-1 "
                "disbursals: ₹600 Cr.",
                "Lesson: the fintech-platform stack reaches "
                "production faster than packaged suites, "
                "subject to regulator comfort.",
            ])
        )
        + example(
            "ICE Encompass + MSP at a US mortgage lender",
            ol([
                "Mid-tier US mortgage lender uses ICE Encompass "
                "for origination and ICE-MSP (ex-Black "
                "Knight) for servicing; CECL provisioning runs "
                "on a Snowflake + Databricks stack fed by MSP.",
                "Post-2023 ICE acquisition of Black Knight "
                "tightened the integration; rate-volatility "
                "stress 2022–24 drove heavy investment in "
                "loss-mitigation workflows.",
                "Lesson: US mortgage tech is now an "
                "ICE-anchored ecosystem; build the rest of "
                "your data and AI stack around it.",
            ])
        )
    )
    return TopicSection(
        "7.  Worked examples — five real BFSI lending journeys",
        "intermediate", body)


def _sec8() -> TopicSection:
    return TopicSection(
        "8.  Questions a leader asks in any lending platform review",
        "basic",
        ol([
            "Which products and channels are on which platform, "
            "and where are the duplicates we should consolidate?",
            "What is our time-to-decision and time-to-disburse per "
            "product, end-to-end? What is the customer-friction "
            "cost of each manual step?",
            "How are decisioning rules and ML models governed — "
            "SR 11-7, PRA SS1/23, EU AI Act, RBI 2024?",
            "How do we evidence affordability and Consumer "
            "Duty / RBI / CCD2 outcomes?",
            "What is our IFRS 9 / CECL pipeline — does the LMS "
            "feed the risk lake at the right grain and "
            "frequency?",
            "How is the LOS / LMS integrated with the core, "
            "payments, GL, bureaus, AA / Open Banking?",
            "What is our model-monitoring posture — drift, "
            "fairness, performance — and how often do we "
            "retrain?",
            "What is our collections strategy by bucket, by "
            "channel, by segment? What is recovered cost vs "
            "outsourced cost?",
            "How are we handling embedded / BNPL credit, and "
            "what is our exposure to FLDG and partner-fintech "
            "concentration risk?",
            "What is the upgrade plan for our LOS / LMS, and "
            "how aligned is it with our regulator deadlines?",
            "Where do we keep the audit trail of every "
            "decision, and can we reproduce a 5-year-old "
            "decision on demand?",
            "What is the credible exit plan from each "
            "Lending-as-a-Service vendor?",
            "If the estate uses nCino plus Loan IQ or ACBS, which "
            "system owns the approved credit terms, which owns "
            "the booked loan, and where is the reconciliation "
            "between them?",
            "If UFSS or another legacy platform is in scope, what "
            "does the acronym mean in this client, which products "
            "does it hold, and what batch jobs, reports and "
            "interfaces depend on it?",
            "When someone says ‘Finastra’, which exact Finastra "
            "product is meant — Loan IQ, Fusion Originate, "
            "LaserPro, Essence, Global PAYplus, Trade Innovation, "
            "Summit, or another module?",
            "For syndicated lending, can we trace a facility from "
            "approval to booking to drawdown to rollover to GL "
            "posting to lender-share accounting to notices?",
        ]))


def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘LOS and LMS are the same thing.’ — They are not. "
            "LOS books the loan; LMS services it for years. "
            "Conflating them produces vendor RFPs that nobody "
            "can answer cleanly.",
            "‘Our scorecard is FICO, so we’re fine on fair "
            "lending.’ — Bureau scores are inputs; the bank’s "
            "policy and ML models on top are what regulators "
            "actually test for disparate impact.",
            "‘BNPL is not regulated credit.’ — It is in the "
            "EU from Nov 2026, in the UK from 2026, "
            "increasingly in the US under CFPB. Treat it as "
            "credit now.",
            "‘Affordability is a checkbox.’ — Outcomes-based "
            "regulation makes affordability evidence part of "
            "every individual decision; checkbox approaches "
            "fail Consumer Duty and CCD2.",
            "‘We do AI underwriting; we just don’t document "
            "it.’ — EU AI Act, PRA SS1/23, SR 11-7, RBI 2024 "
            "all require lifecycle documentation. Undocumented "
            "ML in credit is now a finding waiting to happen.",
            "‘Our LMS doesn’t need to know about IFRS 9 / "
            "CECL.’ — It does — staging triggers and ECL "
            "drivers are largely LMS data. Disconnects "
            "produce material misstatements.",
            "‘Collections is a vendor problem.’ — Regulators "
            "hold the bank accountable for recovery agency "
            "behaviour; documented governance is non-"
            "negotiable.",
            "‘FLDG covers our partner risk.’ — RBI cap of 5% "
            "from June 2023 means it covers a sliver, not "
            "the tail.",
            "‘We can switch off paper next year.’ — Maybe. "
            "Local-language wet signatures and physical "
            "verifications still apply for some products and "
            "regions; plan for hybrid for years.",
            "‘Our model is explainable because it is logistic "
            "regression.’ — Explainability is about reason "
            "codes communicable to customers, not the "
            "algorithm. Document either way.",
            "‘nCino approval means Loan IQ / ACBS booking is "
            "automatic.’ — Approval data must still map cleanly "
            "to servicing fields, accounting, conditions "
            "precedent, covenants and maker-checker controls.",
            "‘UFSS means the same thing everywhere.’ — It does "
            "not. Confirm the client glossary. Publicly it is "
            "often used for Unisys Financial Services System in "
            "legacy UK-style estates, but projects may use "
            "client-specific meanings.",
            "‘Finastra is one application.’ — Finastra is a "
            "vendor family. Always name the exact product and "
            "module before writing requirements or defects.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("LOS", "Loan Origination System — captures and "
                "decisions a loan application."),
            ("LMS", "Loan Management / Servicing System — "
                "services a loan over its life."),
            ("Decisioning engine", "Rules + scorecards + ML "
                "that produce the approve / decline / price "
                "decision."),
            ("Collections platform", "Manages delinquent "
                "accounts, dialler, restructuring, recovery."),
            ("PD / LGD / EAD", "Probability of Default / Loss "
                "Given Default / Exposure At Default — drivers "
                "of expected credit loss."),
            ("IFRS 9 stages", "Stage 1 (12-month ECL), Stage 2 "
                "(lifetime ECL, no default), Stage 3 "
                "(defaulted)."),
            ("CECL", "Current Expected Credit Loss — US "
                "lifetime-ECL standard, in force Jan 2020."),
            ("SICR", "Significant Increase in Credit Risk — "
                "stage-1-to-stage-2 trigger under IFRS 9."),
            ("DPD", "Days Past Due — collections bucket "
                "definition."),
            ("ECL", "Expected Credit Loss — provisioning "
                "amount."),
            ("FCA Consumer Duty", "UK outcomes-based regulation "
                "(July 2023)."),
            ("CCD2", "EU Consumer Credit Directive 2 — applies "
                "from 20 November 2026."),
            ("RBI Digital Lending Guidelines", "RBI rules on "
                "digital lending; 2022 + 2024 amendments."),
            ("FLDG", "First Loss Default Guarantee — partner-"
                "fintech credit-enhancement; RBI capped at 5% "
                "from June 2023."),
            ("Account Aggregator (AA)", "RBI-licensed framework "
                "for consent-based financial-data sharing in "
                "India."),
            ("OCEN", "Open Credit Enablement Network — Indian "
                "protocol for embedded credit."),
            ("ULI", "Unified Lending Interface — RBI-led data "
                "platform for credit; 2024."),
            ("KFS", "Key Fact Statement — fee-and-term "
                "disclosure required by RBI."),
            ("ESIS", "European Standardised Information Sheet "
                "for mortgages."),
            ("TILA / RESPA / TRID", "US disclosure regimes for "
                "consumer credit and mortgage."),
            ("ECOA / Reg B", "US Equal Credit Opportunity "
                "Act."),
            ("CFPB Section 1071", "US small-business lending "
                "data-collection rule (2023)."),
            ("APR / APRC", "Annual Percentage Rate / Annual "
                "Percentage Rate of Charge."),
            ("LTV / DSCR / DTI", "Loan-to-Value / Debt Service "
                "Coverage Ratio / Debt-to-Income."),
            ("BNPL", "Buy Now Pay Later — short-tenor split-"
                "payment credit."),
            ("ICE / Black Knight / Encompass / MSP / Sagent",
             "US mortgage origination and servicing platforms."),
            ("Newgen / Nucleus FinnOne / Pega / nCino / Blend",
             "Major LOS / LMS vendors."),
            ("Loan IQ", "Finastra commercial and syndicated-loan "
                "servicing platform used for facilities, tranches, "
                "drawdowns, rollovers, agency, participation, "
                "fees, notices, accounting and portfolio servicing."),
            ("ACBS", "Advanced Commercial Banking System — FIS "
                "commercial-loan servicing platform commonly seen "
                "in corporate and regional-bank loan operations."),
            ("UFSS", "Usually Unisys Financial Services System in "
                "public UK building-society / legacy banking "
                "context, but confirm the client-specific meaning "
                "on every engagement."),
            ("nCino", "Salesforce-native cloud banking platform "
                "often used for commercial loan origination, "
                "relationship-manager workflow, credit memo, "
                "document collection and approvals."),
            ("Finastra", "Financial-software vendor family. In "
                "lending, common products include Loan IQ, Fusion "
                "Originate and LaserPro; in other domains Finastra "
                "also appears in payments, treasury, trade finance "
                "and universal banking."),
            ("Facility / tranche / drawdown / rollover", "Core "
                "commercial-lending concepts: an approved credit "
                "line, a slice of that line, an actual borrowing "
                "under it, and renewal of a maturing borrowing."),
            ("Agent bank / participant bank", "In a syndicated "
                "loan, the agent administers the facility and "
                "participant banks hold shares of the exposure."),
            ("Covenant", "Borrower promise in the loan agreement, "
                "such as maintaining debt-to-EBITDA below a "
                "specified threshold."),
            ("FICO / Experian PowerCurve / Provenir / SAS / "
             "Pega CDH / Equifax InterConnect", "Major "
                "decisioning platforms."),
            ("Mambu / Thought Machine Vault / Pennant LSP / "
             "Temenos Loans / TCS BaNCS Loans / Finacle "
             "Lending", "Cloud-native and incumbent lending "
                "engines."),
            ("Lentra / CloudBankin / FinBox / Yubi", "Indian "
                "fintech-platform LOS / decisioning vendors."),
            ("FICO Debt Manager / TRIAD / CGI CACS / Tallyman / "
             "Pega Collections", "Collections platforms."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
