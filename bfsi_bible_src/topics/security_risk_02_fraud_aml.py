"""Security, Risk & Compliance · 02 — Fraud, AML, and sanctions in operational depth."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="V.2",
        slug="02-fraud-aml-sanctions",
        title="Fraud, AML, and sanctions in operational depth",
        one_liner=(
            "Behind every clean transaction is a silent, real-time battle against "
            "financial crime. This topic demystifies the technical systems and "
            "operational pipelines that banks use to fight fraud, detect money "
            "laundering (AML), and enforce international sanctions. We explore the "
            "mechanisms of real-time fraud scoring, rule engines, transaction monitoring, "
            "Know Your Customer (KYC) identity resolution, and sanction screening "
            "without slowing down payments for legitimate customers."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(), _sec5(),
                  _sec6(), _sec7(), _sec8(), _sec9(), _sec10()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("Financial Crime Compliance (FCC) is a bank’s license to operate. "
              "It covers three distinct but related domains: <strong>Fraud Prevention</strong> "
              "(stopping bad actors from stealing money from customers or the bank), "
              "<strong>Anti-Money Laundering (AML)</strong> (stopping bad actors from "
              "running dirty money through the bank), and <strong>Sanctions &amp; Terrorist "
              "Financing Screening</strong> (stopping bad actors or rogue states from using the "
              "financial system at all). Operating these at scale requires a delicate balance "
              "between security, compliance cost, and user friction.")
        )
        + H3("0.1  IT-side anchor — your email inbox’s spam and phishing filter")
        + it_anchor(
            p("Think about your email inbox. You receive hundreds of messages a day. "
              "Most are legitimate, some are marketing newsletters you subscribed to, "
              "and some are malicious phishing attempts or junk spam. To keep your inbox "
              "clean, your email provider runs a silent filter in the background. "
              "It uses <em>rules</em> (e.g. 'if the sender email is from a brand-new domain "
              "and contain words like \"VIAGRA\" or \"URGENT TRANSFER\", flag it as spam') "
              "and <em>machine learning</em> (e.g. an algorithm trained on millions of "
              "emails to recognize the patterns of a phishing scam, even if the words are "
              "slightly altered). Sometimes it makes mistakes: a legitimate email lands in "
              "the spam folder (a <strong>false positive</strong>), or a phishing email slips "
              "into your main inbox (a <strong>false negative</strong>). The email filters "
              "at Gmail or Outlook are functionally identical to the real-time transaction "
              "filters a bank uses to scan incoming and outgoing payments.")
        )
        + H3("0.2  BFSI-side anchor — the sudden 'Unusual Activity' text message")
        + bfsi_anchor(
            p("Imagine you are traveling in Singapore on holiday. You land, walk to a "
              "local convenience store, and tap your credit card to buy a bottle of "
              "water. Instantly, your transaction is approved. You then go to a high-end "
              "watch shop and try to tap your card to buy a $15,000 Rolex. "
              "This time, your card is declined, and your phone buzzes with an SMS or app "
              "notification from your bank: 'Did you just attempt a transaction of $15,000 "
              "at Rolex SG? Reply YES to authorize or NO to freeze your card.' "
              "How did the bank approve the $2 bottle of water but block the $15,000 watch "
              "within milliseconds? Behind the scenes, the bank's fraud engine evaluated "
              "your transaction against hundreds of parameters: your historical spending "
              "limit, geographical distance from your last transaction (did you fly "
              "or is it physically impossible?), the merchant's category, and your device "
              "telemetry. That instant evaluation is <strong>real-time fraud scoring</strong>.")
        )
        + H3("0.3  The three pillars of financial crime operations")
        + ul([
            "<strong>Fraud Detection and Prevention</strong> — real-time or near-real-time "
            "intervention; focused on stopping immediate monetary loss. Uses behavioral "
            "analytics, device fingerprinting, and risk-based step-up authentication.",
            "<strong>Anti-Money Laundering (AML) &amp; Transaction Monitoring</strong> — "
            "primarily batch-oriented, retrospective analysis; focused on detecting patterns of "
            "placement, layering, and integration over days, weeks, or months. Feeds "
            "directly into regulatory filings like Suspicious Activity Reports (SARs).",
            "<strong>Sanctions &amp; Watchlist Screening</strong> — mandatory, real-time blocking "
            "of transactions, individuals, or entities named on international watchlists "
            "(e.g. OFAC (Office of Foreign Assets Control), UN, EU, UK, MAS, RBI lists). "
            "A single slip can result in multi-billion dollar regulatory fines.",
        ])
        + callout("Related topics in this bible",
            ul([
                "<a href='01-security-identity-regulators.html'><strong>V.1 — Security &amp; identity</strong></a> "
                "— the broader security stack that Fraud/AML operates within.",
                "<a href='../bfsi-platforms/02-payments-engines.html'><strong>VI.2 — Payments engines</strong></a> "
                "— every payment passes through sanctions and fraud screening.",
                "<a href='../bfsi-platforms/05-cards-and-switches.html'><strong>VI.5 — Cards &amp; switches</strong></a> "
                "— card fraud, chargebacks, and 3DS2 authentication.",
                "<a href='../bfsi-platforms/03-lending-and-originations.html'><strong>VI.3 — Lending</strong></a> "
                "— KYC and AML screening are mandatory in every loan origination flow.",
            ]),
            "info")
    )
    return TopicSection(
        "0.  Primer — the spam filter of the global financial system",
        "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Why do fraud, AML, and sanctions compliance occupy the top spot on any "
          "bank board’s risk agenda?")
        + ol([
            "<strong>Uncapped regulatory penalties.</strong> "
            "Under international frameworks, failure to prevent money laundering or "
            "the facilitation of sanctions evasion is treated as a criminal offense, not "
            "just a civil infraction. HSBC’s $1.9B fine (2012), BNP Paribas’s $8.9B fine "
            "(2014), and Danske Bank’s €2B settlement (2022) prove that regulators "
            "will happily threaten a bank's operational charter if its systems are porous.",
            "<strong>Mandatory Authorized Push Payment (APP) fraud liability.</strong> "
            "Historically, if a customer was tricked into sending money to a scammer (an "
            "authorized payment), the customer bore the loss. Under the UK FCA’s (Financial "
            "Conduct Authority) mandatory APP fraud reimbursement rules (effective October 2024), "
            "sending and receiving banks must split the reimbursement cost 50:50, capped at "
            "£85,000 per claim. The EU’s Instant Payments Regulation (adopted 2024) mirrors "
            "this by holding banks liable if they fail to offer robust 'Confirmation of Payee' "
            "checks. Fraud is now a direct balance-sheet liability.",
            "<strong>The velocity of instant payment rails.</strong> "
            "With the global rise of real-time settlement networks (India’s UPI (Unified "
            "Payments Interface), US FedNow, UK Faster Payments, Singapore's FAST (Fast and "
            "Secure Transfers), Europe's SEPA (Single Euro Payments Area) Instant), money "
            "clears and settles in under 10 seconds. In the legacy era, a bank had hours "
            "or days to reverse a suspicious wire. Today, once money leaves, it is gone "
            "forever in seconds. Real-time screening is the only line of defense.",
            "<strong>Systemic reputation risk.</strong> "
            "A bank accused of facilitating drug cartel money or Russian sanctions evasion "
            "finds itself instantly cut off from the USD clearing network (the correspondent "
            "banking system). This 'death sentence' means the bank cannot clear USD, losing "
            "every corporate client overnight.",
            "<strong>The cost of false positives.</strong> "
            "Legacy compliance engines generate over 95% false positives. This means for "
            "every 100 alerts flag by an AML system, 95 are legitimate customers. Banks must "
            "employ armies of manual investigators (often outsourced to firms like HCLTech) "
            "to clear these cases. Using AI and advanced graph databases to reduce false "
            "positives is a multi-million-dollar operational imperative.",
        ])
    )
    return TopicSection(
        "1.  Why Fraud and AML are board-level, system-critical concerns",
        "basic", body)


def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart TB\n'
            '  subgraph "The Customer Action"\n'
            '    Tx["Transaction Initiated<br/>Card tap, UPI, API, Wire"]\n'
            '    Dev["Device & Session<br/>IP address, Device ID, Keystroke biometrics"]\n'
            '  end\n'
            '  subgraph "In-Flight: The Real-Time Gateway (under 100ms)"\n'
            '    Rule["Rule Engine (Flink)<br/>Is amount > limit?<br/>Is location impossible?"]\n'
            '    ML["ML Model (Sagemaker)<br/>Anomaly score vs profile"]\n'
            '    Sanc["Sanctions Filter (Elastic)<br/>Fuzzy match of Beneficiary against OFAC/UK"]\n'
            '    Tx --> Rule\n'
            '    Tx --> ML\n'
            '    Tx --> Sanc\n'
            '    Dev -.-> ML\n'
            '  end\n'
            '  subgraph "The Gatekeeper Decision"\n'
            '    Score{"Scoring Engine"}\n'
            '    Rule --> Score\n'
            '    ML --> Score\n'
            '    Sanc --> Score\n'
            '    Approve["Approve & Settle"]\n'
            '    StepUp["Step-Up (MFA)<br/>FaceID, SMS OTP, Call"]\n'
            '    Block["Block & Log Incident"]\n'
            '    Score -- low risk --> Approve\n'
            '    Score -- medium/uncertain --> StepUp\n'
            '    Score -- match / high risk --> Block\n'
            '  end\n'
            '  subgraph "Post-Flight: Retrospective Batch (Overnight)"\n'
            '    Lake["Data Lakehouse<br/>Spark, Snowflake"]\n'
            '    Graph["AML Graph Analytics<br/>Neo4j, AWS Neptune"]\n'
            '    Case["Case Management<br/>Actimize, Oracle FCCM, Symphony Ayasdi"]\n'
            '    SAR["Regulator SAR Filing<br/>FinCEN, FIU-IND, FCA"]\n'
            '    Approve --> Lake\n'
            '    Lake --> Graph --> Case --> SAR\n'
            '  end',
            "The Operational Financial Crime Stack: In-flight real-time screening (under 100ms) "
            "working in concert with retrospective batch transaction monitoring (overnight).")
    )
    return TopicSection(
        "2.  The picture — real-time fraud scoring vs. retrospective AML",
        "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  The Real-Time Fraud Lifecycle")
        + p("Fraud detection must occur during the critical window between transaction initiation "
            "and final authorization. In card networks (Visa, Mastercard), this budget is "
            "<strong>under 100 milliseconds</strong>. In modern instant payment rails (UPI, FedNow), "
            "the budget is <strong>under 500 milliseconds</strong>. The lifecycle consists of "
            "three phases:")
        + ol([
            "<strong>Ingest &amp; Enrich:</strong> The payment payload is captured. Device "
            "fingerprints, behavioral biometrics (e.g. how fast the user is typing, swipe pressure), "
            "geographic IP coordinates, and merchant history are instantly appended to the payload.",
            "<strong>Evaluate &amp; Score:</strong> The enriched payload is evaluated in parallel "
            "by two distinct architectures: <em>Deterministic Rule Engines</em> (which run hard "
            "criteria, e.g. 'if card is physically swiped in Singapore 30 minutes after being "
            "swiped in New York, block') and <em>Probabilistic Machine Learning Models</em> (which "
            "generate an anomaly score based on historical cohort spending habits).",
            "<strong>Decision &amp; Action:</strong> The score triggers one of three paths: "
            "approve, deny, or step-up (requesting Multi-Factor Authentication (MFA) via a push "
            "notification to confirm identity)."
        ])
        + H3("3.2  The Retrospective AML Lifecycle")
        + p("Unlike fraud, which aims to stop individual losses, AML transaction monitoring "
            "aims to identify coordinated criminal operations. The standard money laundering "
            "cycle consists of three classic phases: <strong>Placement</strong> (putting illegal "
            "cash into the financial system), <strong>Layering</strong> (hiding the source of cash "
            "via complex webs of transactions), and <strong>Integration</strong> (reintroducing "
            "the cleaned money into the legitimate economy).")
        + ol([
            "<strong>Batch Extraction:</strong> At the end of each business day, all transactions "
            "are extracted from the bank's operational ledgers (OLTP) into a data lakehouse.",
            "<strong>Scenario Analysis:</strong> Over the weekend or overnight, batch jobs "
            "run heuristic scenarios (e.g. 'Rapid Movement of Funds' — account receives 10 distinct "
            "deposits and immediately transfers 99% of the sum out to a foreign jurisdiction "
            "within 2 hours; or 'Structuring / Smurfing' — dividing a single large transaction "
            "just below the reporting limit, like $9,950 to avoid the $10,000 threshold).",
            "<strong>Alert Generation &amp; Triage:</strong> Scenarios exceeding thresholds generate "
            "alerts inside a Case Management system (e.g. NICE Actimize, Oracle Financial Services "
            "Analytical Applications (OFSAA)). Level 1 investigators clear or escalate. "
            "Escalated cases require Level 2 analysts to compile a Suspicious Activity Report (SAR) "
            "and submit it to national Financial Intelligence Units (FIUs)."
        ])
        + H3("3.3  Sanctions and Watchlist Screening")
        + p("Sanction screening must block transaction settlement if either the sender, the "
            "beneficiary, or any intermediary institution is named on a governmental blacklist. "
            "This screening runs <strong>in-flight</strong> before settlement. The challenge is "
            "linguistic identity resolution. If a list contains 'Vladimir Putin', but a transaction "
            "names 'Wladimir Poetin' or 'V. Putin', simple string matching fails. Banks use "
            "<strong>Fuzzy Matching Algorithms</strong> (Levenshtein distance, Jaro-Winkler, Soundex) "
            "to catch variations while keeping false positives manageable.")
    )
    return TopicSection(
        "3.  How it actually works — real-time scoring and AML batch pipelines",
        "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  Taxonomy of Modern Financial Crimes")
        + p("A techno-functional leader must understand the precise mechanism of each criminal vector "
            "to evaluate the corresponding systems. The table below outlines the major variations:")
        + table(
            ["Crime Type", "The Mechanism", "Primary Defense Technology", "Regulatory Focus"],
            [
                ["<strong>Authorized Push Payment (APP) Fraud</strong>",
                 "The customer is socially engineered (phishing, vishing, fake investments) into "
                 "voluntarily transferring funds to a scammer.",
                 "Confirmation of Payee (CoP), behavioral biometrics, inbound payee monitoring.",
                 "UK FCA (Oct 2024 liability rule), EU Instant Payments Regulation (2024)."],
                ["<strong>Account Takeover (ATO)</strong>",
                 "Bad actors compromise user credentials (credential stuffing, session hijacking, SIM swap) "
                 "and empty the bank account.",
                 "Device fingerprinting, IP geolocational analysis, risk-based step-up MFA.",
                 "NIST SP 800-63 Digital Identity Guidelines, MAS TRM."],
                ["<strong>Money Mule Networks</strong>",
                 "Legitimate-looking accounts are opened (often using synthetic IDs) or rented from "
                 "vulnerable individuals to channel and split dirty funds.",
                 "Graph analytics (Neo4j, Amazon Neptune) to map transaction loops and shared device footprints.",
                 "FATF Guidance on Digital Identity, RBI AML Guidelines."],
                ["<strong>Structuring / Smurfing</strong>",
                 "Breaking down a large cash deposit into multiple small transactions below the regulatory "
                 "reporting limit ($10,000 / ₹10,00,000).",
                 "Overnight batch scenario detection, cumulative multi-account rolling window evaluation.",
                 "US Bank Secrecy Act (BSA), EU AMLD6."],
                ["<strong>Sanction Evasion</strong>",
                 "Using shell companies, front entities, or complex correspondent bank routes to transfer "
                 "funds to sanctioned jurisdictions.",
                 "Name screening fuzzy engines, Ultimate Beneficial Owner (UBO) registry resolution.",
                 "US OFAC, UK OFSI, EU Sanctions Guidelines."]
            ]
        )
        + H3("4.2  Geographic Regulatory Variance")
        + p("Compliance is highly nationalized. Let's compare the operational requirements "
            "across regions:")
        + table(
            ["Jurisdiction", "Key Regulator", "Core AML Regulation", "Reporting Threshold", "Instant Payment Mandate"],
            [
                ["<strong>United States</strong>",
                 "FinCEN (Financial Crimes Enforcement Network)",
                 "Bank Secrecy Act (BSA), USA PATRIOT Act, Corporate Transparency Act (CTA)",
                 "CTR (Currency Transaction Report): >$10,000; SAR: >$5,000 for suspicious activity.",
                 "FedNow (real-time screen recommended, no mandatory customer reimbursement yet)."],
                ["<strong>India</strong>",
                 "FIU-IND (Financial Intelligence Unit - India), RBI",
                 "Prevention of Money Laundering Act (PMLA), 2002; RBI Master Directions on KYC",
                 "CTR: >₹10,00,000; STR (Suspicious Transaction Report): No floor limit.",
                 "UPI (real-time risk checks, RBI Digital Lending Guidelines and 2024 UPI limits)."],
                ["<strong>United Kingdom</strong>",
                 "FCA (Financial Conduct Authority)",
                 "Proceeds of Crime Act 2002 (POCA), Money Laundering Regulations 2017",
                 "SAR (Suspicious Activity Report) filed via NCA (National Crime Agency). No fixed floor.",
                 "Faster Payments (Mandatory 50/50 split liability for APP fraud up to £85k)."],
                ["<strong>Eurozone</strong>",
                 "EBA (European Banking Authority), AMLA (Anti-Money Laundering Authority)",
                 "EU 6th Anti-Money Laundering Directive (AMLD6), Transfer of Funds Regulation (TFR)",
                 "Thresholds vary by member state (typically €10,000).",
                 "SEPA Instant (adopted 2024: Confirmation of Payee mandatory by Oct 2025)."],
                ["<strong>Singapore</strong>",
                 "MAS (Monetary Authority of Singapore)",
                 "Corruption, Drug Trafficking and Other Serious Crimes Act (CDSA)",
                 "STR submitted to STRO (Suspicious Transaction Reporting Office). Threshold SGD 20,000.",
                 "FAST (Shared liability framework being established for phishing scams)."]
            ]
        )
    )
    return TopicSection(
        "4.  Types and variations — crime taxonomies and geo-balanced regulations",
        "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  The Architecture of Real-Time Fraud Engines")
        + p("To achieve sub-100ms response times, real-time fraud scoring engines abandon traditional "
            "relational database queries. They use <strong>In-Memory Event Stream Processing (ESP)</strong> "
            "architectures:")
        + ul([
            "<strong>Apache Flink / Apache Kafka Streams:</strong> Transactions flow in as continuous streams. "
            "Flink maintains stateful windows (e.g. 'sum of transactions in the last 10 minutes from this device') "
            "in ultra-fast memory (using RocksDB as the state backend) to check rules instantly.",
            "<strong>Redis / Aerospike as Feature Stores:</strong> A machine learning model requires historical "
            "context (e.g. 'average transaction size for user 123 over the last 90 days'). Rather than querying "
            "an SQL ledger, this context is updated asynchronously overnight and stored in high-throughput NoSQL "
            "caches, allowing the ML model to fetch the features in < 2ms.",
            "<strong>Asynchronous ML Model Inference:</strong> The transaction request is parsed, "
            "features are gathered, and an API call is made to an inference cluster (e.g. Triton, TorchServe, "
            "AWS SageMaker) running an XGBoost or deep learning fraud model. The model returns a probability score "
            "from 0.0 to 1.0."
        ])
        + H3("5.2  Advanced AML: Graph Databases and Entity Resolution")
        + p("Money launderers hide their footprint by passing money through multiple intermediary accounts "
            "(layering). In relational databases (RDBMS), detecting a loop like 'A → B → C → D → A' requires "
            "complex, deeply nested SQL <code>JOIN</code> operations that crash under production scale. "
            "Modern AML systems use <strong>Graph Databases</strong> (Neo4j, Amazon Neptune, TigerGraph):")
        + ul([
            "<strong>Graph Model:</strong> Accounts are represented as <em>nodes (vertices)</em>; "
            "transactions, shared phone numbers, or identical IP addresses are represented as <em>edges (links)</em>.",
            "<strong>Cycle and Loop Detection:</strong> Graph query languages (Cypher, Gremlin) can search "
            "depths of 5 or 6 levels in milliseconds to find circular transfers or layered money mule rings.",
            "<strong>Entity Resolution:</strong> Criminals open accounts with variations of their names or "
            "stolen IDs. Entity resolution systems use probabilistic record linkage to merge nodes if "
            "they share a high probability of being the same human (e.g. identical DOB and IP address, "
            "even if names differ)."
        ])
        + H3("5.3  The Math of Fuzzy Matching")
        + p("Fuzzy matching for sanctions screening relies on mathematical string-distance algorithms:")
        + ul([
            "<strong>Levenshtein Distance:</strong> Measures the minimum number of single-character "
            "edits (insertions, deletions, substitutions) required to change one word into another. "
            "For example, Levenshtein distance between 'Putin' and 'Poetin' is 2 (sub 'u' with 'oe').",
            "<strong>Jaro-Winkler Distance:</strong> Measures character matches and transpositions. "
            "It gives higher ratings to strings that match from the beginning. A score of 1.0 is an exact "
            "match; banks typically screen using a threshold of ≥ 0.85.",
            "<strong>Phonetic Algorithms (Double Metaphone, Soundex):</strong> Converts words into "
            "codes based on how they sound in English. 'Stephen' and 'Steven' resolve to the exact same "
            "phonetic key, catching auditory spelling tricks."
        ])
    )
    return TopicSection(
        "5.  Advanced — stateful streaming engines, graph analytics, and fuzzy math",
        "advanced", body)


def _sec6() -> TopicSection:
    body = (
        H3("6.1  Regulatory Triggers and Operational Resiliency")
        + p("Regulators globally have pivoted from simple periodic reporting to demanding real-time "
            "monitoring and instant operational resilience. If a bank’s screening engine or transaction "
            "monitoring system suffers an outage, the bank must either stop processing transactions (halting "
            "the payments network and breaching availability SLOs) or process them 'blind' (violating anti-money "
            "laundering laws and courting multi-million dollar fines). This is a direct board-level trade-off.")
        + H3("6.2  Ultimate Beneficial Owner (UBO) & PEP Screening")
        + p("Modern AML requires finding the actual human who controls an account, even if it is owned "
            "by nested shells. For instance, the <strong>Corporate Transparency Act (CTA)</strong> in the US "
            "(effective January 2024) and the EU’s <strong>6th Anti-Money Laundering Directive (AMLD6)</strong> "
            "mandate the identification of any individual holding a ≥ 25% ownership stake or significant control.")
        + ul([
            "<strong>Politically Exposed Persons (PEPs):</strong> Individuals who hold prominent public functions "
            "(e.g. heads of state, senior politicians, judges, military officials) and their close family members. "
            "They present a higher risk of corruption, requiring mandatory <strong>Enhanced Due Diligence (EDD)</strong> "
            "and ongoing transaction monitoring.",
            "<strong>Sanction Screening Rules:</strong> Standard matching includes checking for individuals or entities "
            "listed under major regimes (OFAC, UK HM Treasury, EU consolidated lists, MAS, RBI/FIU-IND). "
            "Under the OFAC <strong>50% Rule</strong>, any entity owned 50% or more, in the aggregate, by one or more "
            "sanctioned persons is automatically blocked, even if that entity itself is not explicitly listed.",
        ])
        + H3("6.3  Global Intelligence Sharing & Privacy Trade-offs")
        + p("Fighting international financial crime requires cross-border collaboration, but this runs "
            "directly into data localization laws (e.g. India's DPDP (Digital Personal Data Protection) Act 2023, "
            "the EU's GDPR (General Data Protection Regulation), and Singapore's PDPA (Personal Data Protection Act)). "
            "Technologies like <strong>Federated Learning</strong> and <strong>Homomorphic Encryption</strong> "
            "are emerging as a solution, allowing banks to share risk patterns and machine learning models without "
            "exchanging the underlying personal customer data.")
    )
    return TopicSection(
        "6.  BFSI / domain regulatory overlay — PEP, UBO, and international standards",
        "advanced", body)


def _sec7() -> TopicSection:
    body = (
        H3("7.1  The Architecture Decision Matrix")
        + p("Techno-functional leaders must continuously weigh compliance costs, system latency, and customer friction. "
            "The following matrix summarizes the critical architectural levers and decisions:")
        + table(
            ["Technology Choice", "Pros", "Cons", "Optimal Use Case"],
            [
                ["<strong>Heuristic Rule Engines (Flink / Drools)</strong>",
                 "Deterministic, 100% auditable, easy to explain to regulators, executes in sub-10ms.",
                 "High false-positive rate, easily bypassed by adaptive criminals, requires constant manual tuning.",
                 "First-line sanity checks (limits, velocity, simple geo-distance matching)."],
                ["<strong>Machine Learning Models (XGBoost / Deep Learning)</strong>",
                 "Finds complex, multi-dimensional correlations; adapts automatically; significantly lowers false positives.",
                 "Black-box nature (harder to explain to auditors), requires clean and massive training datasets.",
                 "Complex behavioral fraud detection, device profiling, transaction anomaly scoring."],
                ["<strong>Graph Databases (Neo4j / Amazon Neptune)</strong>",
                 "Uncovers circular transfer networks and smurfing structures instantly; maps shared device networks.",
                 "High memory footprint; hard to run fully in-flight; usually runs as near-real-time asynchronous batch.",
                 "Mule network identification, ultimate beneficial owner (UBO) resolution."],
                ["<strong>Managed SaaS Compliance (Feedzai / NICE Actimize Cloud)</strong>",
                 "Speed to market, pre-built regulatory templates, lower in-house infrastructure burden.",
                 "High licensing cost, vendor lock-in, limited customizability for unique regional products.",
                 "Mid-tier banks or rapid market entries where custom engineering headcount is limited."]
            ]
        )
        + H3("7.2  Friction vs. Compliance: The Product Owner's Paradox")
        + p("A high-performance fraud engine can run so hot that it declines every transaction that deviates "
            "even 1% from normal. While this drops fraud losses to zero, it ruins the customer experience (CX). "
            "Conversely, letting everything slide increases customer satisfaction but leads to crippling APP fraud losses. "
            "Leaders manage this by aligning their <strong>Step-Up Authentication</strong> rules. If a card tap is "
            "high-risk, do not decline it; instead, trigger a face-scan or push notification challenge in the mobile app. "
            "This converts a destructive block into a mild, secure customer nudge.")
    )
    return TopicSection(
        "7.  Trade-offs and decisions a leader owns — rules vs. models, SaaS vs. build",
        "intermediate", body)


def _sec8() -> TopicSection:
    body = (
        example(
            "Authorized Push Payment (APP) Scam — UK Faster Payments (£50,000 Loss)",
            ol([
                "<strong>The Scenario:</strong> A customer in London receives a call from a scammer posing "
                "as an HSBC fraud investigator. The scammer claims the customer's account is compromised "
                "and directs them to move £50,000 to a 'safe haven account' at NatWest.",
                "<strong>The Real-Time Failure:</strong> The customer initiates the £50,000 transfer. HSBC's "
                "system prompts a 'Confirmation of Payee' (CoP) check. The name entered is 'NatWest Safe Haven', "
                "but the actual account holder name registered at NatWest is 'John Doe' (a money mule). "
                "The system displays a 'Match Warning: Name does not match'.",
                "<strong>The Resolution & split liability:</strong> The socially engineered customer bypasses "
                "the warning and authorizes the transfer. Under the UK's October 2024 APP fraud rules, "
                "since the fraud warning failed to prevent the transfer, and NatWest (the receiving bank) "
                "failed to flag John Doe's rapid cash movement, both HSBC and NatWest must split the "
                "reimbursement cost 50:50, paying £25,000 each back to the customer."
            ])
        )
        + example(
            "Real-Time Fraud Detection at an Indian Private Bank (UPI Scale)",
            ol([
                "<strong>The Scenario:</strong> A UPI transaction is initiated on a smartphone in Mumbai "
                "for ₹1,00,000 ($1,200). The transaction must be processed and scored in under 300 milliseconds.",
                "<strong>The In-flight Pipeline:</strong> The transaction hits an API gateway. The API passes "
                "the user payload to a stateful Flink engine. Flink checks rocksDB in-memory store and notices "
                "that the user's phone fingerprint has changed (new IMEI), the IP address matches a proxy "
                "network, and the user tried 3 failed PIN attempts 5 minutes ago. Simultaneously, an XGBoost model "
                "compares this ₹1,00,000 transfer against the user's average UPI size of ₹1,500.",
                "<strong>The Decisive Action:</strong> The composite risk score is 0.92 (extremely high). "
                "The transaction is instantly declined, the mobile session is invalidated, and an SMS alert "
                "is dispatched to the customer's registered phone to re-verify identity via biometric video KYC."
            ])
        )
        + example(
            "Sanctions Screening at a US Investment Bank (Correspondent Clearing)",
            ol([
                "<strong>The Scenario:</strong> A corporate client in Frankfurt attempts to send $12,000,000 "
                "via SWIFT to an export firm in Dubai. The payment clears through JP Morgan in New York.",
                "<strong>The Screen Gate:</strong> Before clearing the USD transaction, JP Morgan's fuzzy matching "
                "engine screens the SWIFT MT103 payload. The beneficiary is listed as 'Al-Mansoor Trading'. "
                "The engine flags a 0.88 Jaro-Winkler match against 'Al-Mansour General Trading', a sanctioned "
                "front entity on the OFAC Specially Designated Nationals (SDN) list.",
                "<strong>The Decisive Action:</strong> The payment is automatically paused. A ticket is created in "
                "the bank's case management system. An L2 investigator in New York reviews the case, confirms that "
                "the Dubai address matches the OFAC target address, blocks the $12M, and files an OFAC blocking "
                "report within the mandatory 10-day window."
            ])
        )
        + example(
            "Retrospective Money Laundering Cycle (Placement, Layering, Integration)",
            ol([
                "<strong>Placement:</strong> A criminal network deposits cash into 15 distinct accounts "
                "at branches across Chicago, keeping each deposit at $9,500 to stay below the $10,000 CTR reporting "
                "threshold (structuring / smurfing).",
                "<strong>Layering:</strong> Overnight, the Chicago accounts transfer the funds to 5 shell "
                "companies in Delaware. The Delaware accounts then consolidate the funds and transfer them to "
                "an offshore bank in the Cayman Islands.",
                "<strong>Integration:</strong> The Cayman Island bank lends the consolidated 'clean' funds "
                "as a legitimate real-estate development loan to a luxury hotel developer in Miami.",
                "<strong>How the Bank Caught It:</strong> An overnight batch AML scenario detects the structuring "
                "pattern (15 accounts with identical IP footprints depositing near-identical amounts within "
                "48 hours). A graph query uncovers the common beneficial ownership of the 5 Delaware companies. "
                "A Suspicious Activity Report (SAR) is compiled and submitted to FinCEN."
            ])
        )
    )
    return TopicSection(
        "8.  Worked examples — numbers, split-liability, and transaction paths",
        "intermediate", body)


def _sec9() -> TopicSection:
    body = (
        ol([
            "What is our transaction false-positive rate? For every 1,000 alerts generated by our compliance engine, "
            "how many represent real financial crime?",
            "What is the average latency of our real-time fraud scoring pipeline? Does it fit comfortably within our "
            "card network (<100ms) or real-time rails (<300ms) budgets?",
            "How do our systems handle the OFAC 50% Rule? Do we resolve Ultimate Beneficial Owners (UBOs) or just "
            "direct entity names?",
            "Under the UK FCA APP fraud or EU SEPA Instant rules, what is our projected financial liability "
            "exposure for split reimbursement this fiscal year?",
            "Are we using rule engines (heuristics) or ML models for fraud scoring? What is our explainability framework "
            "when we decline a customer's transaction?",
            "How do we perform entity resolution? Do we use graph databases (Neo4j, Neptune) to map shared user networks, "
            "or do we rely on relational SQL queries?",
            "What Jaro-Winkler or Levenshtein distance thresholds do we use for sanctions screening? How do we audit "
            "the system to prevent leakage of blacklisted names?",
            "Is our financial crime data centralized in a modern lakehouse, or is it scattered across siloed core banking "
            "and credit card ledgers?",
            "How long does it take an Level 1 investigator to triage an alert? What is our backlog of unresolved compliance alerts?",
            "What is our strategy for PEP (Politically Exposed Persons) classification? Do we perform Enhanced Due Diligence (EDD) "
            "manually or through automated workflows?",
        ])
    )
    return TopicSection(
        "9.  Questions a leader asks in any Fraud or AML review",
        "basic", body)


def _sec10() -> TopicSection:
    body = (
        red_flag(ul([
            "‘We have a 0% fraud rate, so our systems are world-class.’ — A 0% fraud rate typically means your "
            "fraud scoring is running so hot that you are declining millions of dollars of legitimate customer "
            "transactions. Monitor customer checkout friction and declined cart rates alongside fraud losses.",
            "‘Our sanctions engine uses exact string matching.’ — This is a critical regulatory risk. Exact matching "
            "misses simple spelling variations, translations, and phonetic bypasses. Fuzzy engines are mandatory.",
            "‘We don’t need machine learning; we have 2,000 business rules.’ — Rules act like house of cards. They "
            "conflict, latency climbs, and they cannot adapt to shifting criminal methods. Move to a hybrid model of "
            "high-velocity rules and probabilistic machine learning.",
            "‘We only screen the sender, not the beneficiary.’ — Under international sanctions frameworks, screening "
            "must cover every actor in a transaction ledger. Failing to screen the receiver exposes you to systemic "
            "facilitation charges.",
            "‘We clear alerts in batch at the end of the week.’ — Real-time payment rails make delayed compliance "
            "obsolete. Once money settles, it is unrecoverable. Screening must be inline, and alerts triaged with "
            "strict timelines.",
            "‘We rely on the customer to spot scams.’ — Regulation is shifting. APP split-liability and consumer duty "
            "regimes hold banks financially accountable. Banks must design proactive, 'Confirmation of Payee' and "
            "friction-based controls.",
            "‘We use SQL to find layering loops.’ — Deeply nested SQL JOINs do not scale. If your network has "
            "hundreds of thousands of transactions, querying circular flows via SQL will exhaust database memory. "
            "Migrate to graph databases.",
            "‘Our AI model explains itself automatically.’ — Regulators expect algorithmic transparency. If an AI "
            "decision declines a loan or blocks a payment, you must be able to prove the specific factors used, or "
            "face discrimination and non-compliance charges.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("AML", "Anti-Money Laundering — the legal and technical framework "
                "designed to prevent criminals from disguising the origin of dirty funds."),
            ("KYC", "Know Your Customer — the mandatory process of identifying and "
                "verifying a customer's identity at onboarding and periodically throughout the relationship."),
            ("APP Fraud", "Authorized Push Payment Fraud — a social engineering scam where "
                "the customer is tricked into voluntarily sending money to a fraudulent account."),
            ("OFAC", "Office of Foreign Assets Control — the US Department of the Treasury agency "
                "that administers and enforces economic and trade sanctions."),
            ("Sanctions Screening", "The in-flight process of matching sender, receiver, and "
                "intermediaries against global blacklists (OFAC, UN, EU, UK, MAS, RBI)."),
            ("Fuzzy Matching", "An algorithmic technique used to find strings that match "
                "approximately rather than exactly, to catch spelling variations or phonetic alternatives."),
            ("Jaro-Winkler Distance", "A mathematical string distance algorithm widely used in "
                "compliance to score name match similarity between 0.0 and 1.0."),
            ("Levenshtein Distance", "The minimum number of character edits needed to change "
                "one string to another; used in fuzzy matching."),
            ("Structuring / Smurfing", "The practice of breaking down a large cash deposit "
                "into multiple small transactions below regulatory currency reporting thresholds."),
            ("UBO", "Ultimate Beneficial Owner — the natural person who ultimately owns or "
                "controls a corporate entity (usually holding ≥ 25% ownership stake)."),
            ("PEP", "Politically Exposed Person — an individual holding a prominent public function "
                "who presents a higher risk of corruption, requiring Enhanced Due Diligence (EDD)."),
            ("False Positive", "A transaction or account incorrectly flagged as suspicious "
                "by a compliance engine, generating unnecessary operational overhead and friction."),
            ("False Negative", "A fraudulent or money laundering transaction that goes undetected "
                "by a compliance engine, representing direct financial or regulatory risk."),
            ("Correspondent Banking", "A financial network where banks provide services "
                "to each other across borders, critical for clearing foreign currencies (like USD)."),
            ("SAR / STR", "Suspicious Activity Report / Suspicious Transaction Report — a mandatory "
                "filing submitted by banks to national Financial Intelligence Units (FIUs) when suspicious activity is detected."),
            ("Placement", "The first stage of money laundering: introducing dirty cash into the "
                "legitimate financial system."),
            ("Layering", "The second stage of money laundering: shifting funds through multiple accounts "
                "and shell corporations to obscure the audit trail."),
            ("Integration", "The final stage of money laundering: reintroducing the cleaned funds "
                "into the economy as legitimate investments."),
            ("Graph Database", "A database that uses nodes and edges to represent data, optimal "
                "for mapping financial networks and tracing money laundering loops."),
            ("Confirmation of Payee (CoP)", "A regulatory-backed system that verifies if the recipient's "
                "name matches the account details before an electronic payment is sent, reducing fraud."),
        ])
    )
    return TopicSection("10.  Red flags + topic glossary", "basic", body)
