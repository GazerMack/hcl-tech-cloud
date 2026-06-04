"""BFSI Domain Platforms · 02 — Payments engines: Volante, Form3, ACI,
Finastra, FIS, Fiserv and the modern payments hub."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="VI.2",
        slug="02-payments-engines",
        title="Payments engines — Volante, Form3, ACI, Finastra, and the modern payments hub",
        one_liner=(
            "A payments engine is the piece of software that turns ‘I want to "
            "pay £100 to my electrician’ into a sequence of authoritative, "
            "regulator-acceptable instructions across the right rails — Faster "
            "Payments, SEPA, FedNow, UPI, SWIFT, RTGS — and back into a "
            "settled, reconciled, reportable transaction. This topic gives you "
            "fluent vocabulary in the major engines (Volante, Form3, ACI, "
            "Finastra, FIS, Fiserv, Temenos Payments Hub, Bottomline, "
            "Montran), the rails they connect to, and the design choices a "
            "techno-functional leader makes when buying, replacing or "
            "modernising one."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("Most BFSI conversations conflate three different things "
              "and call them all ‘payments’. They are very different. "
              "<strong>A scheme</strong> is the rule book and central "
              "infrastructure (UPI, SEPA, Faster Payments, FedNow, "
              "SWIFT). <strong>A rail</strong> is the network and the "
              "messages used to move money on a scheme. <strong>A "
              "payments engine (or hub)</strong> is the software inside "
              "the bank that prepares, validates, signs, sends, "
              "receives, settles and reports those messages. Schemes "
              "and rails are mostly bought-from; engines are "
              "almost always bought (rarely built) from one of "
              "8–10 specialist vendors.")
        )
        + H3("0.1  IT-side anchor — your email is a payments engine in miniature")
        + it_anchor(
            p("When you click ‘Send’ in your email client, the client "
              "doesn’t know how mail will get to the recipient. It "
              "hands the message to a Mail Transfer Agent (your email "
              "provider), which figures out the recipient’s domain, "
              "looks up the right route, formats the message in the "
              "right protocol (SMTP), signs it (DKIM), and tracks "
              "whether it bounced. <em>That</em> is what a payments "
              "engine does for money: a corporate Treasury or a retail "
              "customer presses ‘Pay’; the engine decides which rail "
              "(SEPA Instant? SWIFT? card?), formats the right ISO "
              "20022 or local message, signs it, sends it, tracks the "
              "settlement, and reconciles the response.")
        )
        + H3("0.2  BFSI-side anchor — what happened when your salary landed at 9 a.m.")
        + bfsi_anchor(
            p("On the first of the month a payment file arrives at "
              "your employer’s bank. In India it is a NACH or RTGS "
              "batch; in the UK a Bacs file; in the US an ACH "
              "(Automated Clearing House) NACHA file; in the EU a "
              "SEPA pain.001 message; in cross-border a SWIFT MT103 "
              "(or, increasingly, an ISO 20022 pacs.008). The "
              "employer’s bank validates, screens for sanctions, "
              "decides which rail to use, sends to the scheme, "
              "receives confirmation, debits the employer, credits "
              "the employee’s bank, and notifies all parties — all in "
              "minutes for instant rails, in batch for ACH. The "
              "<strong>payments engine</strong> is the middle of that "
              "story and the part the bank is most likely to have "
              "bought from a specialist vendor.")
        )
        + H3("0.3  The engine, the hub, and the gateway — three words")
        + ul([
            "<strong>Payments engine</strong> — single-rail, focused: "
            "‘the SWIFT engine’, ‘the SEPA engine’, ‘the ACH engine’. "
            "Often a vendor module within a larger suite.",
            "<strong>Payments hub</strong> — multi-rail, single "
            "service: customer-initiated payment goes to one place, "
            "the hub picks the rail, normalises the data, runs the "
            "common controls (sanctions, fraud, AML, limits, "
            "duplicate-check), and routes. The architectural target "
            "of every modernisation programme since ~2015.",
            "<strong>Payments gateway</strong> — usually means a "
            "merchant-side acceptance gateway (Stripe, Razorpay, "
            "Adyen, Worldpay) that consumes cards / wallets / Open "
            "Banking. Different industry, similar word.",
        ])
        + H3("0.4  The seven control points every engine implements")
        + ul([
            "<strong>Validation</strong> — schema, IBAN/BIC checksum, "
            "balance check, beneficiary masterdata.",
            "<strong>Sanctions and watchlist screening</strong> — "
            "OFAC, EU, UK OFSI, India MEA, UN, internal lists.",
            "<strong>Fraud / Authorised Push Payment (APP) "
            "screening</strong> — behavioural risk score, "
            "Confirmation of Payee.",
            "<strong>AML / transaction monitoring</strong> — "
            "real-time and post-event; case generation.",
            "<strong>Limits and authorisation</strong> — customer "
            "limits, bank limits, scheme limits, regulatory limits.",
            "<strong>Routing and message transformation</strong> — "
            "pick the rail, build the message in its dialect.",
            "<strong>Settlement, reconciliation and reporting</strong> "
            "— match what we sent against what cleared; produce "
            "regulatory and customer reports.",
        ])
    )
    return TopicSection(
        "0.  Primer — schemes, rails and engines, said three different ways",
        "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Why is the payments engine the single most-modernised "
            "platform in BFSI in 2024–2026?")
        + ol([
            "<strong>ISO 20022 forced the issue.</strong> Cross-border "
            "SWIFT MT retires <strong>22 November 2025</strong>; "
            "Fedwire migrated 14 March 2025; CHAPS migrated June "
            "2023; SEPA, RTGS-India, FedNow are all ISO 20022 "
            "natively. Old engines built around fixed-format MT "
            "messages cannot carry the rich structured data without "
            "rework.",
            "<strong>Instant payments became mandatory.</strong> EU "
            "Instant Payments Regulation (adopted 2024) made SEPA "
            "Instant mandatory: receive by 9 January 2025, send by "
            "9 October 2025, with Verification of Payee. UPI in "
            "India, FedNow in the US (live July 2023), Faster "
            "Payments in the UK, NPP in Australia, PIX in Brazil, "
            "FAST in Singapore — instant is the new normal.",
            "<strong>Fraud reimbursement changed the maths.</strong> "
            "UK PSR mandatory APP fraud reimbursement since October "
            "2024 splits the cost 50/50 between sending and "
            "receiving PSPs; engines must score in real time and "
            "decide whether to challenge.",
            "<strong>Cloud-native is now table stakes.</strong> "
            "Form3, ACI Enterprise Payments Platform, Volante VolPay "
            "and Temenos Payments Hub all run on Kubernetes; older "
            "monolith deployments are being retired.",
            "<strong>Payments-as-a-Service.</strong> Smaller banks "
            "and fintechs increasingly outsource the engine "
            "entirely (Form3, ClearBank, Banking Circle, Currencycloud).",
            "<strong>AI and agentic payments.</strong> Generative AI "
            "is being applied to investigations, payment-narrative "
            "enrichment, sanctions hit-handling, and exception "
            "operations.",
        ])
    )
    return TopicSection(
        "1.  Why payments engines are the most-modernised BFSI platform",
        "basic", body)


def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  subgraph "Origination channels"\n'
            '    M["Mobile / web<br/>retail and corporate"]\n'
            '    H["Host-to-host<br/>corporate ERP, payroll"]\n'
            '    A["Open Banking PIS<br/>third-party initiation"]\n'
            '  end\n'
            '  subgraph "Payments hub"\n'
            '    R["Receive and normalise<br/>any format in"]\n'
            '    V["Validate, enrich"]\n'
            '    S["Sanctions and fraud screening"]\n'
            '    L["Limits and authorisation"]\n'
            '    Ro["Routing engine"]\n'
            '    T["Translate to scheme dialect<br/>ISO 20022 / MT / NACHA"]\n'
            '    R --> V --> S --> L --> Ro --> T\n'
            '  end\n'
            '  subgraph "Rails"\n'
            '    F["Faster Payments / FedNow / SEPA Instant / UPI"]\n'
            '    W["SWIFT cross-border<br/>CBPR+ ISO 20022"]\n'
            '    Rt["Domestic RTGS / CHAPS / Target2 / Fedwire"]\n'
            '    B["Batch ACH / NACHA / Bacs / SEPA / NACH"]\n'
            '  end\n'
            '  subgraph "Settlement and reporting"\n'
            '    Se["Posting to ledger<br/>core banking"]\n'
            '    Re["Reconciliation"]\n'
            '    Rg["Regulatory reporting"]\n'
            '  end\n'
            '  M --> R\n'
            '  H --> R\n'
            '  A --> R\n'
            '  T --> F\n'
            '  T --> W\n'
            '  T --> Rt\n'
            '  T --> B\n'
            '  F --> Se --> Re --> Rg\n'
            '  W --> Se\n'
            '  Rt --> Se\n'
            '  B --> Se',
            "Reference architecture of a modern bank payments hub: any "
            "format in, normalised, controlled, routed, translated, "
            "settled and reported.")
    )
    return TopicSection(
        "2.  The picture — one hub, many rails",
        "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  The major engines and what they are known for")
        + table(
            ["Engine", "Strength", "Where you’ll see it"],
            [
                ["<strong>Volante VolPay / Volante Payments-as-a-"
                 "Service</strong>",
                 "Strong ISO 20022 lineage, configurable rules, "
                 "cloud-native VolPay-as-a-Service.",
                 "Goldman Sachs Transaction Banking, Standard "
                 "Chartered, BNY Mellon, ANZ, Sumitomo Mitsui, "
                 "various US regionals."],
                ["<strong>Form3</strong>",
                 "Cloud-native Payments-as-a-Service on AWS + "
                 "CockroachDB; multi-region active-active; "
                 "regulator-aware.",
                 "Lloyds Bank for FPS, Nationwide, Mettle (NatWest "
                 "digital), ClearBank, several EU and APAC banks."],
                ["<strong>ACI Worldwide — Enterprise Payments "
                 "Platform / ACI Money Transfer System (MTS)</strong>",
                 "Long-standing high-value and instant capability; "
                 "ACI is the operator of UK Faster Payments scheme "
                 "infrastructure (alongside Pay.UK).",
                 "Many tier-1 US, UK, EU and APAC banks; ACI also "
                 "operates the Faster Payments central "
                 "infrastructure for Pay.UK."],
                ["<strong>Finastra — Global PAYplus, Payments "
                 "Hub, Fusion Payments To Go</strong>",
                 "Broad rail coverage, particularly in Europe and "
                 "for cross-border SWIFT.",
                 "Société Générale, Crédit Agricole, ICBC London, "
                 "Standard Bank South Africa, several Indian "
                 "PSU banks."],
                ["<strong>FIS — Open Payment Framework (OPF), FIS "
                 "Payments One</strong>",
                 "US strength, especially regional and community "
                 "banks; deep ACH and wire heritage; close to "
                 "Federal Reserve services.",
                 "US regional and community banks; some EU "
                 "deployments."],
                ["<strong>Fiserv — Enterprise Payments Platform "
                 "(EPP), Now</strong>",
                 "US ACH and wire dominance; integration with "
                 "Fiserv core platforms (DNA, Premier, Signature).",
                 "Many US banks and credit unions; expanding "
                 "international footprint."],
                ["<strong>Temenos Payments Hub</strong>",
                 "Native to the Temenos Transact / T24 estate; "
                 "single-vendor stack appeal; cloud delivery.",
                 "ABN AMRO, Bank of Sharjah, ING (parts), various "
                 "Asian and African banks."],
                ["<strong>Bottomline — Universal Aggregator, "
                 "Cyfrin, Banker’s Almanac for Compliance</strong>",
                 "Strong corporate-payments and SWIFT-bureau heritage; "
                 "fraud and CoP services in the UK.",
                 "UK building societies, US mid-tier, corporate "
                 "Treasury at large customers."],
                ["<strong>Montran</strong>",
                 "Central-bank-grade RTGS and ACH operator; less "
                 "common at commercial banks.",
                 "Several central banks worldwide for RTGS / ACH "
                 "infrastructure."],
                ["<strong>Pelican AI / IntellectAI iGTB / TCS "
                 "BaNCS Payments / Infosys Finacle Payments</strong>",
                 "AI-led screening and Indian-vendor payments hubs; "
                 "rising in APAC and the Middle East.",
                 "Indian banks (TCS BaNCS for many PSUs; Finacle "
                 "Payments for ICICI, Kotak); Middle East and APAC."],
            ]
        )
        + H3("3.2  The rails and what they expect from your engine")
        + table(
            ["Rail", "Region", "Message", "What the engine must do"],
            [
                ["<strong>SWIFT cross-border (MX / CBPR+)</strong>",
                 "Global",
                 "ISO 20022 pacs.008, pacs.009, camt.054 etc.",
                 "Carry full structured remittance, LEI, purpose "
                 "code; UETR for tracking; SWIFT GPI compliance."],
                ["<strong>Fedwire</strong>",
                 "United States",
                 "ISO 20022 (since 14 Mar 2025)",
                 "Real-time gross settlement; high-value; fee-bearing "
                 "messaging; sanctions screening per FedLine."],
                ["<strong>FedNow</strong>",
                 "United States",
                 "ISO 20022, 24×7",
                 "Instant credit transfer; <20 s end-to-end; "
                 "negative confirmation supported via camt.056."],
                ["<strong>CHIPS</strong>",
                 "United States (high value)",
                 "ISO 20022 (since April 2024)",
                 "Net-settlement clearing for USD high-value; "
                 "screening and queuing."],
                ["<strong>NACHA ACH</strong>",
                 "United States",
                 "Fixed-record NACHA file format",
                 "Same-day ACH (3 windows daily); credit and debit; "
                 "addenda records for remittance."],
                ["<strong>CHAPS</strong>",
                 "United Kingdom",
                 "ISO 20022 (since June 2023)",
                 "RTGS via Bank of England; Confirmation of Payee; "
                 "Purpose codes."],
                ["<strong>Faster Payments (FPS)</strong>",
                 "United Kingdom",
                 "ISO 20022 (NPA migration in train)",
                 "Instant; CoP; PSR APP fraud reimbursement; "
                 "<15 s SLA."],
                ["<strong>Bacs</strong>",
                 "United Kingdom",
                 "Bacstel-IP file",
                 "3-day cycle; Direct Debit and Direct Credit; "
                 "Service User Number (SUN) management."],
                ["<strong>SEPA SCT / SCT Inst / SDD</strong>",
                 "Eurozone + non-euro EU",
                 "ISO 20022 pain / pacs",
                 "SCT batch; SCT Inst <10 s 24×7; mandatory "
                 "Verification of Payee; mandate management for "
                 "Direct Debit."],
                ["<strong>Target2 / T2</strong>",
                 "Eurozone (high value)",
                 "ISO 20022 (since March 2023)",
                 "RTGS for euro; ECB-operated."],
                ["<strong>RTGS / NEFT</strong>",
                 "India",
                 "ISO 20022 (RTGS, since 2021)",
                 "Indian rupee high-value settlement; KYC checks; "
                 "RBI reporting."],
                ["<strong>UPI / IMPS</strong>",
                 "India",
                 "NPCI XML",
                 "Instant; addressing by VPA / mobile / Aadhaar; "
                 "very high TPS; India-resident data."],
                ["<strong>NACH</strong>",
                 "India",
                 "NACH file",
                 "Mandate management; SIP debits; e-mandate via "
                 "AePS / Aadhaar."],
                ["<strong>FAST / PayNow</strong>",
                 "Singapore",
                 "ISO 20022",
                 "Instant SGD; PayNow proxy addressing; UPI ↔ PayNow "
                 "interoperability since 2023."],
                ["<strong>NPP / PayID</strong>",
                 "Australia",
                 "ISO 20022",
                 "Instant AUD; PayID proxy addressing; CDR cross-link."],
                ["<strong>PIX</strong>",
                 "Brazil",
                 "ISO 20022",
                 "BCB-operated instant rail; QR-code initiation; "
                 "very high adoption."],
                ["<strong>HKD CHATS</strong>",
                 "Hong Kong",
                 "ISO 20022",
                 "RTGS; HKMA-operated; FPS retail rail layered "
                 "on top."],
                ["<strong>AANI</strong>",
                 "UAE",
                 "ISO 20022",
                 "Instant AED; CBUAE-operated; UPI ↔ AANI "
                 "interoperability since 2024."],
            ]
        )
        + H3("3.3  Settlement models — the bit the regulator cares about")
        + ul([
            "<strong>RTGS (Real-Time Gross Settlement)</strong> — "
            "each payment settled individually in central-bank money, "
            "typically high-value. Fedwire, CHAPS, Target2, RTGS-"
            "India.",
            "<strong>Net settlement</strong> — payments accumulated "
            "and settled in net positions at intervals. CHIPS, ACH, "
            "Bacs.",
            "<strong>Deferred Net Settlement (DNS) for instant</strong> "
            "— instant rails settle in central-bank money on a net "
            "basis at scheduled cycles (FedNow, FPS, SEPA Instant); "
            "the customer experiences immediacy, the bank "
            "experiences cycles.",
            "<strong>Pre-funded</strong> — participant deposits a "
            "balance with the operator; payments debit that balance "
            "in real-time. Used by some instant rails (FedNow "
            "liquidity model).",
            "<strong>Bilateral</strong> — between two correspondent "
            "banks via nostro / vostro accounts. Cross-border SWIFT "
            "is the canonical example.",
        ])
        + H3("3.4  ISO 20022 — the format that ate the world")
        + p("ISO 20022 messages used by payment engines (memorise "
            "these abbreviations; you will hear them constantly):")
        + kv([
            ("pain (Payment Initiation)", "pain.001 customer credit "
                "transfer, pain.002 status report, pain.008 "
                "customer direct debit."),
            ("pacs (Payment Clearing & Settlement)", "pacs.008 "
                "customer credit transfer, pacs.009 financial-"
                "institution credit transfer, pacs.002 status, "
                "pacs.004 payment return, pacs.028 status request."),
            ("camt (Cash Management)", "camt.052 intraday account "
                "report, camt.053 end-of-day statement, camt.054 "
                "debit/credit notification, camt.056 request for "
                "recall, camt.029 resolution of investigation, "
                "camt.110 / camt.111 case management for fraud."),
            ("acmt (Account Management)", "Account opening, "
                "maintenance."),
            ("admi (Administrative)", "System notifications between "
                "scheme participants."),
        ])
        + H3("3.5  Operational characteristics that distinguish engines")
        + ul([
            "<strong>Throughput</strong> — UPI demands 100k+ TPS at "
            "peak; FedNow, FPS, SEPA Instant typically tens of "
            "thousands; cross-border far less but with stricter "
            "controls.",
            "<strong>Latency</strong> — instant rails require sub-"
            "second engine processing; high-value rails tolerate "
            "more.",
            "<strong>Availability</strong> — instant rails are 24×7×"
            "365; the engine and every dependency must be too.",
            "<strong>Multi-tenancy</strong> — Payments-as-a-Service "
            "vendors (Form3, ClearBank) need strong tenant "
            "isolation; bank-internal hubs need legal-entity "
            "separation.",
            "<strong>Configurability vs code</strong> — most engines "
            "blend a rules engine (Drools, Camunda DMN, in-house) "
            "with code; the more business-rules-as-config, the "
            "faster the change cadence.",
        ])
    )
    return TopicSection(
        "3.  How the engine market actually works — vendors, rails, "
        "settlement, ISO 20022",
        "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  India — UPI is the world’s template")
        + p("India runs the world’s highest-volume retail payments "
            "rail. UPI processed 16+ billion transactions in October "
            "2024, peaking at 500+ million per day. NPCI is the "
            "scheme operator; member banks plug in via NPCI-defined "
            "APIs. Major engines: <strong>Infosys Finacle Payments, "
            "TCS BaNCS Payments, ACI, Nucleus PaySe</strong> for the "
            "PSU banks; in-house engines at HDFC, ICICI; <strong>"
            "Mindgate</strong> is a major UPI infrastructure vendor "
            "behind many bank deployments. RBI Storage of Payment "
            "Data (April 2018) requires the entire payments-data "
            "lifecycle stored in India. UPI also interoperates with "
            "Singapore PayNow (2023), UAE AANI (2024), and several "
            "ASEAN rails through Project Nexus (BIS Innovation Hub).")
        + H3("4.2  United States — FedNow alongside Fedwire, ACH, CHIPS")
        + ul([
            "<strong>FedNow</strong> live since 24 July 2023; 1,000+ "
            "participating financial institutions by end of 2024. "
            "Run by the Federal Reserve.",
            "<strong>Fedwire</strong> migrated to ISO 20022 on 14 "
            "March 2025; CHIPS migrated April 2024.",
            "<strong>ACH</strong> Same Day expanded to 3 windows in "
            "2021; cap raised to USD 1M per transaction in March "
            "2022.",
            "<strong>RTP (Real-Time Payments)</strong> by The "
            "Clearing House (TCH), live since 2017; private-sector "
            "instant rail; coexists with FedNow.",
            "<strong>Engine market</strong>: ACI Worldwide, Fiserv, "
            "FIS dominate the US bank market; Volante and Form3 "
            "growing; many regionals on FedNow via FedLine direct "
            "without a payments hub.",
        ])
        + H3("4.3  United Kingdom — modernisation of FPS, CHAPS, Bacs")
        + ul([
            "<strong>CHAPS</strong> migrated to ISO 20022 in June "
            "2023; Pay.UK and Bank of England are aligned.",
            "<strong>Faster Payments New Payments Architecture "
            "(NPA)</strong> programme is rebuilding the central FPS "
            "infrastructure; engine vendors are aligning their "
            "platforms accordingly.",
            "<strong>Confirmation of Payee (CoP)</strong> mandatory "
            "for the UK’s major banks; smaller PSPs joining through "
            "2024–25.",
            "<strong>UK PSR mandatory APP fraud reimbursement</strong> "
            "since October 2024; engines must score and decide in "
            "seconds.",
            "<strong>Engine market</strong>: Form3 at Lloyds, "
            "Nationwide, Mettle, ClearBank; ACI heritage at HSBC, "
            "Barclays; Bottomline at building societies and many "
            "corporates.",
        ])
        + H3("4.4  Eurozone — SEPA Instant becomes mandatory")
        + ul([
            "<strong>EU Instant Payments Regulation (IPR)</strong> — "
            "adopted 2024; receive obligation 9 January 2025, send "
            "obligation 9 October 2025; SEPA Instant must be priced "
            "no higher than regular SCT.",
            "<strong>Verification of Payee (VoP)</strong> — EU "
            "equivalent of CoP; mandatory by 9 October 2025 for "
            "euro-area PSPs.",
            "<strong>Target2 / TIPS / EURO1</strong> all on ISO "
            "20022 since March 2023.",
            "<strong>Engine market</strong>: Volante (BNY Mellon, "
            "Standard Chartered EU), Finastra (Société Générale, "
            "Crédit Agricole, ICBC London), ACI, Temenos.",
        ])
        + H3("4.5  Singapore, Hong Kong, Australia, Brazil")
        + ul([
            "<strong>Singapore — FAST + PayNow</strong>; MAS-led; "
            "PayNow interoperability with India UPI since February "
            "2023, with Thailand, Malaysia in pilot.",
            "<strong>Hong Kong — FPS + CHATS</strong>; HKMA-operated; "
            "FPS interoperability with Thailand PromptPay; cross-"
            "border QR with Mainland UnionPay and Alipay.",
            "<strong>Australia — NPP + PayID</strong>; PayTo "
            "(equivalent of UK Variable Recurring Payments) live "
            "since 2022 and growing 2024–25; Mastercard is the "
            "scheme operator for NPP.",
            "<strong>Brazil — PIX</strong>; BCB-operated, instant; "
            "now the dominant retail rail in Brazil with hundreds "
            "of millions of users.",
            "<strong>Cross-border</strong>: <strong>Project "
            "Nexus</strong> (BIS Innovation Hub) standardises "
            "instant-payment connections between domestic rails; "
            "live phases through 2025–27 with India UPI, Singapore "
            "PayNow, Malaysia DuitNow, Thailand PromptPay, "
            "Philippines InstaPay.",
        ])
        + H3("4.6  Cross-border — SWIFT GPI, CBPR+, and the alternatives")
        + ul([
            "<strong>SWIFT GPI (Global Payments Innovation)</strong> "
            "— launched 2017; brings tracking (UETR), transparency "
            "and time-bound settlement to cross-border. Now the "
            "default service level.",
            "<strong>CBPR+ (Cross-Border Payments and Reporting "
            "Plus)</strong> — SWIFT’s ISO 20022 cross-border "
            "programme; co-existence with MT ends <strong>22 "
            "November 2025</strong>.",
            "<strong>SWIFT Go</strong> — low-value cross-border "
            "with predictable cost.",
            "<strong>Alternatives</strong> — Wise Platform, Visa "
            "Direct, Mastercard Move, Ripple Payments, Banking "
            "Circle, Currencycloud, Thunes; competitors and partners "
            "to traditional correspondent banking.",
        ])
    )
    return TopicSection(
        "4.  Region by region — engines, rails, regulators, current "
        "as of 2025",
        "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  Inside the engine — the modern reference architecture")
        + p("A modern payments hub looks roughly the same across "
            "vendors:")
        + ul([
            "<strong>Channel adapters</strong> — REST / gRPC / file "
            "/ host-to-host / Open Banking PIS endpoints.",
            "<strong>Canonical message model</strong> — internal "
            "format (often ISO 20022-aligned) into which everything "
            "is normalised.",
            "<strong>Validation and enrichment services</strong> — "
            "schema, IBAN / BIC / account checksum, beneficiary "
            "masterdata, FX rate, purpose code.",
            "<strong>Sanctions and watchlist</strong> — Accuity "
            "World-Check, Dow Jones Risk &amp; Compliance; engines "
            "embed or call via API.",
            "<strong>Fraud and APP screening</strong> — Feedzai, "
            "NICE Actimize, FICO Falcon, BioCatch, Featurespace; "
            "Confirmation / Verification of Payee.",
            "<strong>AML / transaction monitoring</strong> — "
            "real-time and post-event hooks.",
            "<strong>Limits engine</strong> — customer / corporate / "
            "scheme / regulatory limits; quota management for "
            "instant rails.",
            "<strong>Routing engine</strong> — picks the rail "
            "(cheapest, fastest, mandatory) based on amount, "
            "currency, urgency, beneficiary country.",
            "<strong>Format translation</strong> — to scheme-"
            "specific dialect (MT, MX, NACHA, NACH, Bacstel-IP).",
            "<strong>Connectivity</strong> — SWIFT Alliance Access / "
            "Cloud, FedLine, EBA Clearing, NPCI APIs, scheme-"
            "specific gateways.",
            "<strong>Settlement and reconciliation</strong> — "
            "posting to core; nostro / vostro reconciliation; "
            "investigations.",
            "<strong>Reporting</strong> — regulatory "
            "(MiFID II, EMIR, AnaCredit, MAS, RBI), customer "
            "(camt.053 / 054), and operational dashboards.",
        ])
        + H3("5.2  Liquidity and intraday cash management")
        + p("Instant rails are 24×7. The bank’s liquidity must be "
            "available 24×7 too. Modern engines integrate with an "
            "<strong>intraday liquidity manager</strong> "
            "(Bottomline, Smartstream, Volante, Vermeg) to forecast "
            "and shape liquidity through the day. Concepts:")
        + ul([
            "<strong>Pre-funding</strong> at FedNow / Target2 / RTGS-"
            "India; balances held with the central bank.",
            "<strong>Liquidity bridges</strong> — automated movement "
            "between accounts (Target2 ↔ TIPS in the EU).",
            "<strong>Throttling</strong> when liquidity is tight; "
            "queueing rules for high-value vs instant.",
            "<strong>BCBS 248 intraday liquidity reporting</strong> "
            "— Basel monitoring tools; central banks watch.",
        ])
        + H3("5.3  Reconciliation, investigations and exceptions")
        + ul([
            "<strong>Three-way recon</strong> — what we sent, what "
            "the rail confirms, what posted to the ledger.",
            "<strong>Nostro reconciliation</strong> — account "
            "statements from correspondent banks matched against "
            "expected entries; SmartStream TLM is the dominant "
            "vendor.",
            "<strong>Investigations</strong> — recall (camt.056), "
            "rejection (pacs.004), resolution (camt.029); "
            "case-management UIs in NICE Actimize, Pelican AI, "
            "in-house tools.",
            "<strong>Repair and exception STP</strong> — automation "
            "of fixes via rules + AI for messages that fail "
            "validation; classic ROI driver in payments "
            "modernisation.",
        ])
        + H3("5.4  Tokenisation, encryption, key management")
        + ul([
            "<strong>PCI DSS 4.0</strong> — payment-card data "
            "tokenised wherever possible; vault providers "
            "Voltage / Protegrity / CipherTrust.",
            "<strong>HSM-backed signing</strong> for SWIFT, RTGS, "
            "and instant-rail messages; FIPS 140-3 Level 3 "
            "typical.",
            "<strong>Key custody</strong> — BYOK for cloud-managed "
            "deployments; HYOK / EKM where regulator-required.",
        ])
        + H3("5.5  AI and the payments operations function")
        + ul([
            "<strong>Hit handling</strong> — sanctions and AML alerts "
            "triaged by Generative AI assistants; human reviewer "
            "remains in the loop.",
            "<strong>Narrative enrichment</strong> — LLMs translate "
            "unstructured remittance text into structured ISO "
            "20022 fields.",
            "<strong>Fraud explanation</strong> — model outputs "
            "annotated to support reason codes for customers and "
            "regulators.",
            "<strong>Operations copilot</strong> — agentic flows "
            "for repair, cross-system reconciliation, and root-"
            "cause analysis.",
        ])
        + H3("5.6  CBDC, stablecoins and the next rail")
        + ul([
            "<strong>India e₹</strong> — RBI retail and wholesale "
            "Central Bank Digital Currency pilots ongoing.",
            "<strong>Project mBridge</strong> — multi-CBDC "
            "platform with HKMA, Bank of Thailand, CBUAE, PBOC, "
            "Saudi Central Bank.",
            "<strong>ECB Digital Euro</strong> — preparation phase "
            "since November 2023; decision expected 2025.",
            "<strong>Stablecoin payments</strong> — USDC and USDT "
            "rails for cross-border B2B; the EU MiCA regulation in "
            "force from June 2024 brings legal clarity in the EU.",
            "<strong>Engine implications</strong> — engines must "
            "abstract ‘the rail’ enough that adding a CBDC or a "
            "stablecoin rail is a configuration, not a re-write.",
        ])
    )
    return TopicSection(
        "5.  Advanced — reference architecture, liquidity, recon, "
        "AI ops, CBDC",
        "advanced", body)


def _sec6() -> TopicSection:
    body = (
        H3("6.1  Build vs buy vs Payments-as-a-Service")
        + table(
            ["Option", "When it wins", "Watch-outs"],
            [
                ["<strong>Build in-house</strong>",
                 "Very largest banks (JPM, Citi, HSBC, Goldman) "
                 "where the engine is a competitive differentiator "
                 "and the team is large enough.",
                 "Decade-scale investment; only justified by scale "
                 "and strategic intent."],
                ["<strong>Buy a packaged engine (Volante, ACI, "
                 "Finastra, FIS, Fiserv, Temenos)</strong>",
                 "Most tier-1 incumbents; specialist vendor moves "
                 "with regulatory change; plenty of skilled "
                 "implementers (HCLTech, Accenture, TCS, Wipro, "
                 "Infosys, Capgemini).",
                 "Implementation risk; vendor roadmap risk; total "
                 "cost over 10+ years."],
                ["<strong>Payments-as-a-Service (Form3, "
                 "ClearBank, Banking Circle, Currencycloud)</strong>",
                 "Smaller banks, fintechs, neobanks; rapid time-to-"
                 "market; vendor handles scheme certification.",
                 "Concentration risk; regulator wants exit plan; "
                 "tier-1 banks rarely outsource the whole engine."],
                ["<strong>Hybrid (own hub, outsource a corridor)</strong>",
                 "Common at mid-tier banks for cross-border or for "
                 "a new instant rail.",
                 "Integration complexity; reconciliation across "
                 "boundaries."],
            ]
        )
        + H3("6.2  Choosing an engine — the eight-question framework")
        + ol([
            "Which rails do we need on day 1, day 365, day 1,825?",
            "What is our peak transactions-per-second target on the "
            "highest-volume rail?",
            "What ISO 20022 readiness is the vendor offering for "
            "CBPR+, Fedwire, CHAPS, Target2, RTGS?",
            "How configurable is the rules engine vs how much "
            "requires the vendor to deliver a release?",
            "What is the deployment model — single-tenant "
            "containerised, vendor-cloud, on-prem? What is the "
            "regulator-acceptable model in our jurisdiction?",
            "What is the CoP / VoP / fraud / AML integration story?",
            "What is the upgrade cadence and the back-compat record?",
            "Who else in our peer group is on this engine, and "
            "what did their last upgrade cost in time and money?",
        ])
        + H3("6.3  Implementation partner choice")
        + p("Most BFSI engine implementations are delivered with a "
            "global SI: <strong>HCLTech, TCS, Infosys, Wipro, "
            "Capgemini, Accenture, Cognizant, IBM Consulting, "
            "Atos / Eviden</strong>. The choice often follows "
            "existing portfolio relationships; ensure the chosen "
            "partner has practical references on the specific "
            "engine and rail you need.")
    )
    return TopicSection(
        "6.  Decision matrices — build vs buy, engine choice, "
        "partner choice",
        "intermediate", body)


def _sec7() -> TopicSection:
    body = (
        example(
            "Goldman Sachs Transaction Banking on Volante",
            ol([
                "Goldman launched Transaction Banking (TxB) in 2020 "
                "as a greenfield digital cash-management platform.",
                "Built on Volante VolPay-as-a-Service for payments "
                "processing across SWIFT, Fedwire, CHAPS, ACH; "
                "deployed on AWS.",
                "Lessons: greenfield + cloud-native engine + global "
                "rails launched in under three years; the engine is "
                "the productisable piece, not the legacy ledger.",
            ])
        )
        + example(
            "Lloyds Banking Group on Form3 for Faster Payments",
            ol([
                "Lloyds adopted Form3’s Payments-as-a-Service for "
                "Faster Payments processing — believed to be the "
                "first tier-1 UK bank to use a fully-managed cloud "
                "Payments-as-a-Service for a primary rail.",
                "Form3 runs on AWS with active-active CockroachDB "
                "across multiple regions for resilience.",
                "Mettle (NatWest) and Nationwide also Form3 "
                "customers; ClearBank built its own cloud-native "
                "engine in parallel.",
            ])
        )
        + example(
            "An Indian PSU bank on TCS BaNCS Payments + UPI",
            ol([
                "Tier-2 PSU bank runs TCS BaNCS Core, with TCS "
                "BaNCS Payments as the hub for RTGS, NEFT, IMPS, "
                "and a separate Mindgate-based UPI switch.",
                "RBI Storage of Payment Data keeps everything in "
                "Mumbai / Hyderabad regions of an Indian "
                "hyperscaler.",
                "Sanctions screening with Accuity World-Check; "
                "fraud monitoring with NICE Actimize; case "
                "management with in-house tooling.",
                "ISO 20022 readiness for CBPR+ achieved in 2024 in "
                "time for the November 2025 cutover.",
            ])
        )
        + example(
            "Standard Chartered EU on Volante and Finastra",
            ol([
                "Standard Chartered runs Volante for some "
                "cross-border SWIFT and Finastra Global PAYplus for "
                "specific corridors; in-house components handle the "
                "channel layer.",
                "Standardised on Azure for the cloud-native "
                "components; HCLTech is one of the partners "
                "delivering modernisation work.",
                "ISO 20022 cutover for CBPR+ completed across all "
                "active corridors by mid-2025.",
            ])
        )
        + example(
            "FedNow rollout at a US regional bank",
            ol([
                "Tier-2 US regional decided in 2023 to participate "
                "in FedNow as a receive-only participant first.",
                "Connected via FedLine Solution and used existing "
                "core (Fiserv DNA) with a thin Fiserv NOW! engine "
                "for ISO 20022 message handling.",
                "Year 2: enabled send-side; raised limits; "
                "integrated with Fiserv-supplied fraud screening.",
                "Public lessons: instant-rail liquidity management "
                "is the unfamiliar piece; treasury operations "
                "redesigned to support 24×7 funding.",
            ])
        )
    )
    return TopicSection(
        "7.  Worked examples — five real BFSI payments-engine journeys",
        "intermediate", body)


def _sec8() -> TopicSection:
    return TopicSection(
        "8.  Questions a leader asks in any payments-engine review",
        "basic",
        ol([
            "Which rails do we participate in today, and which are "
            "we obligated to add over the next 24 months under "
            "regulator timelines (IPR, NPA, FedNow, CBPR+)?",
            "What is our peak TPS per rail today and our forecast "
            "12 / 24 / 36 months out?",
            "How many distinct engines do we operate, and what is "
            "the consolidation roadmap?",
            "Are we ISO 20022-native end to end, or do we still "
            "downgrade messages somewhere internally?",
            "What is our Confirmation / Verification of Payee "
            "coverage on outbound and inbound payments?",
            "Where do sanctions / AML / fraud sit in the flow, and "
            "what is the time budget per check?",
            "How do we manage 24×7 liquidity for the instant rails, "
            "and have we tested end-of-quarter / FX-volatility "
            "scenarios?",
            "What is our exception / repair STP rate, and what is "
            "the operations FTE cost per million payments?",
            "What is our recovery position if the engine fails — "
            "RTO, RPO, manual fallback documented and rehearsed?",
            "What is our exit plan from each Payments-as-a-Service "
            "vendor, per DORA / RBI / PRA expectations?",
            "Are upgrades and scheme-mandate windows integrated "
            "into our release calendar, with traceability to "
            "regulator deadlines?",
            "Are we ready operationally and from an engine "
            "perspective for CBDC and stablecoin rails when they "
            "go live?",
        ]))


def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘We have one engine for everything.’ — Possible at "
            "mid-tier; rare at tier-1. Most large banks run 2–4 "
            "engines aligned to rail-family or geography; pretending "
            "otherwise hides risk.",
            "‘ISO 20022 is just a format change.’ — Wrong. The data "
            "is richer, the operations are different, and downstream "
            "systems must <em>use</em> the data; otherwise the "
            "migration is wasted.",
            "‘CoP / VoP is a nice-to-have.’ — In the UK and EU, "
            "it is mandatory and tied to APP fraud reimbursement "
            "obligations.",
            "‘Our engine is cloud-native because it runs in a VM in "
            "the cloud.’ — Cloud-native means containerised, "
            "horizontally scalable, observability-first, ISO 20022-"
            "native. Lift-and-shift is not modernisation.",
            "‘We outsourced to a Payments-as-a-Service vendor; "
            "compliance is theirs.’ — The bank remains accountable. "
            "DORA, RBI, PRA all require an exit plan and oversight.",
            "‘Sanctions screening on the file boundary is enough.’ — "
            "For instant rails, screening must be in-line with "
            "sub-second latency. File-boundary screening fits ACH "
            "/ Bacs only.",
            "‘Liquidity is treasury’s problem, not the engine’s.’ — "
            "On instant rails, the engine is the eyes and ears of "
            "the treasurer. Integration must be tight.",
            "‘FedNow is just RTP with a different name.’ — Different "
            "operator (Fed vs TCH), different liquidity model, "
            "different participant onboarding. Both can coexist; "
            "many large banks support both.",
            "‘CBDC won’t affect us for years.’ — India e₹, ECB "
            "Digital Euro preparation, Project mBridge, mainland "
            "China e-CNY, MAS retail CBDC trial — engines need to "
            "be rail-agnostic now.",
            "‘Manual repair is fine, our STP rate is 95%.’ — At "
            "instant volumes 5% manual is unfeasible. The right "
            "answer is automation + AI exception handling, not "
            "more operations FTEs.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("Scheme", "The rule book and central infrastructure of "
                "a payment system (UPI, SEPA, FPS, FedNow, SWIFT)."),
            ("Rail", "The network and message family used to move "
                "money on a scheme."),
            ("Engine / hub", "Bank-side software that prepares, "
                "controls, routes and reconciles payments across "
                "rails."),
            ("ISO 20022", "Global standard for structured financial "
                "messages; pacs / pain / camt / acmt / admi "
                "families."),
            ("CBPR+", "Cross-Border Payments and Reporting Plus — "
                "SWIFT ISO 20022 cross-border programme; cutover "
                "22 November 2025."),
            ("MT vs MX", "Legacy SWIFT MT (free-text fields) vs "
                "modern SWIFT MX (ISO 20022 XML)."),
            ("UETR", "Unique End-to-End Transaction Reference — "
                "SWIFT GPI tracking identifier."),
            ("RTGS / DNS / Net", "Real-Time Gross Settlement / "
                "Deferred Net Settlement / Net settlement models."),
            ("Fedwire / FedNow / CHIPS / ACH / RTP", "Major US "
                "rails operated by the Fed and The Clearing House."),
            ("CHAPS / FPS / Bacs", "Major UK rails."),
            ("SEPA SCT / SCT Inst / SDD", "European credit transfer, "
                "instant credit transfer, direct debit."),
            ("Target2 / TIPS / EURO1", "Euro-area RTGS, instant, "
                "and net-settlement systems."),
            ("RTGS-India / NEFT / IMPS / UPI / NACH", "Indian rails."),
            ("FAST / PayNow / NPP / PayID / PIX / FPS-HK / CHATS / "
             "AANI", "Other major instant or RTGS rails."),
            ("Project Nexus", "BIS Innovation Hub initiative linking "
                "domestic instant rails."),
            ("CoP / VoP", "Confirmation of Payee (UK) / "
                "Verification of Payee (EU); validate beneficiary "
                "name before payment."),
            ("APP fraud", "Authorised Push Payment fraud; UK "
                "mandatory reimbursement since October 2024."),
            ("EU Instant Payments Regulation (IPR)", "Adopted 2024; "
                "mandates SEPA Instant; receive Jan 2025, send Oct "
                "2025."),
            ("PCI DSS 4.0", "Payment Card Industry Data Security "
                "Standard; March 2025 fully in force."),
            ("SWIFT GPI", "Global Payments Innovation; tracking and "
                "transparency for cross-border."),
            ("CBDC / mBridge / e₹ / Digital Euro", "Central Bank "
                "Digital Currency programmes worldwide."),
            ("Stablecoin", "Token pegged to fiat (USDC, USDT); MiCA "
                "regulation in EU since June 2024."),
            ("Volante / Form3 / ACI / Finastra / FIS / Fiserv / "
             "Temenos / Bottomline", "Major payments-engine "
                "vendors."),
            ("Mindgate / Infosys Finacle Payments / TCS BaNCS "
             "Payments / IntellectAI iGTB / Pelican AI", "Indian / "
                "APAC-leaning payments-engine vendors."),
            ("SmartStream TLM", "Dominant nostro and exception-"
                "reconciliation platform."),
            ("BCBS 248", "Basel intraday liquidity monitoring tools."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
