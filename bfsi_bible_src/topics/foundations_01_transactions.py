"""Foundations · 01 — How a digital banking transaction actually flows."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, term, TopicPage, TopicSection,
)


def _phase(name: str, body: str, *, key_terms=None) -> str:
    out = [H3(name), p(body)]
    if key_terms:
        out.append(H4("Key terms introduced here"))
        out.append(kv(key_terms))
    return "\n".join(out)


def build() -> TopicPage:
    s: list[TopicSection] = []
    s.append(_sec0())
    s.append(_sec1())
    s.append(_sec2())
    s.append(_sec3())
    s.append(_sec4())
    s.append(_sec5())
    s.append(_sec6())
    s.append(_sec7())
    s.append(_sec8())
    s.append(_sec9())
    s.append(_sec10())
    return TopicPage(
        code="I.1",
        slug="01-transactions",
        title="How a digital banking transaction actually flows",
        one_liner=("Banks do exactly two things in software: change a number in a ledger, and "
                   "convince every counterparty that the change is real, irreversible, and authorised. "
                   "Everything you will ever learn in BFSI tech is a tax paid for those two guarantees. "
                   "This topic starts from your laptop and your UPI app, then climbs all the way to "
                   "what a senior architect at Citi or Standard Chartered debates in design reviews."),
        sections=s,
    )


def _sec0() -> TopicSection:
    return TopicSection("0.  Primer — anchored to things you already know", "basic", _PRIMER_HTML)


def _sec1() -> TopicSection:
    body = (
        p("Strip a bank to its essence and it does two things in software: "
          "<strong>(1) it changes a number in a ledger</strong>, and "
          "<strong>(2) it convinces every counterparty that the change is real, irreversible, and "
          "authorised</strong>. Every protocol, gateway, switch, queue, regulation and acronym you "
          "will ever encounter is a tax paid for those two guarantees in a world that is "
          "asynchronous, hostile, and regulated.")
        + p("Hold this lens and the entire stack stops being a zoo of three-letter acronyms and "
            "becomes a single problem solved many ways at different latencies, value sizes, and "
            "trust levels.")
        + callout("The five hard problems any transaction system must solve",
            ol([
                "<strong>Authenticity</strong> — is this really the customer asking, and is the "
                "message they sent exactly what they signed?",
                "<strong>Authorisation</strong> — even if it is them, are they allowed to do this "
                "right now (limits, KYC tier, sanctions, fraud, regulator-defined rules)?",
                "<strong>Atomicity</strong> — either the whole transfer happens or none of it does; "
                "no half-state ever survives a crash, network drop, or server reboot.",
                "<strong>Finality</strong> — once we say ‘done’, neither side can quietly undo it; "
                "the counterparty must be able to rely on it.",
                "<strong>Auditability</strong> — years later, a regulator or court must be able to "
                "reconstruct exactly what happened and why.",
            ]),
            "info")
    )
    return TopicSection("1.  Why a transaction system exists at all — first principles", "basic", body)


def _sec2() -> TopicSection:
    body = (
        p("Every digital banking transaction — UPI in India, Faster Payments in the UK, FedNow in "
          "the United States, SEPA Instant in Europe, an MT103 wire from Citi New York to Standard "
          "Chartered Hong Kong — follows the same eight-phase skeleton. Each rail just compresses, "
          "parallelises, or outsources some phases. None of them skip a phase; they only hide it.")
        + mermaid(
            'flowchart LR\n'
            '  A["1 Initiate"] --> B["2 Authenticate"]\n'
            '  B --> C["3 Authorise"]\n'
            '  C --> D["4 Validate"]\n'
            '  D --> E["5 Route"]\n'
            '  E --> F["6 Clear"]\n'
            '  F --> G["7 Settle"]\n'
            '  G --> H["8 Notify & Reconcile"]',
            "The universal eight-phase transaction skeleton. Memorise this.",
        )
        + analogy(
            p("Compare to a paper cheque: you fill it (initiate), sign it (authenticate), the bank "
              "checks balance and that you are not blocked (authorise / validate), drops it in the "
              "clearing pouch (route), the bank exchanges it at the clearing house (clear), the "
              "money moves between bank accounts at the central bank (settle), you both see it on "
              "your statement (notify / reconcile). UPI just compresses the same eight steps from "
              "three days to three seconds. The phases never disappear.")
        )
    )
    return TopicSection("2.  The core concept in one picture", "basic", body)


def _sec3() -> TopicSection:
    body = (
        _phase("Phase 1 — Initiate",
            "Someone or something expresses an intent: a customer taps Pay, a salary file is "
            "uploaded, an API call fires. The intent is captured as a structured message and "
            "tagged with a unique <strong>idempotency key</strong> — a client-generated identifier "
            "that lets a server safely repeat the request without doing the work twice. This single "
            "pattern is the most important in payments engineering.",
            key_terms=[
                ("Idempotency key", "Unique ID on each request. If the server has seen the same "
                 "key before, it returns the previous result instead of duplicating the effect. "
                 "Standard time-to-live (TTL): 24 hours."),
                ("Channel", "The surface that captured the intent: mobile app, web, ATM, branch "
                 "teller, IVR (Interactive Voice Response), API, file upload."),
            ])
        + _phase("Phase 2 — Authenticate",
            "Prove the initiator is who they claim. Methods stack from weakest to strongest: "
            "password, OTP (One-Time Password) by SMS, OTP by authenticator app, biometric "
            "(face / fingerprint), device binding, hardware token, mTLS for system-to-system, "
            "digitally signed JWTs (JSON Web Tokens) for API consumers, digital signatures on "
            "payment files. Higher-value or higher-risk transactions trigger <em>step-up "
            "authentication</em> — a regulatory principle in PSD2 (Europe), the RBI 2-factor "
            "mandate (India), and Reg E (United States).",
            key_terms=[
                ("MFA", "Multi-Factor Authentication — two or more of {something you know, "
                 "something you have, something you are}."),
                ("mTLS", "Mutual TLS — both client and server present cryptographic certificates "
                 "before talking. Standard for system-to-system traffic inside banks."),
                ("JWT", "JSON Web Token — compact signed token carrying identity and claims; "
                 "verifiable without calling back to the issuer."),
                ("PSD2 SCA", "Second Payment Services Directive (Europe) Strong Customer "
                 "Authentication — mandates 2FA for most electronic payments inside the EU."),
            ])
        + _phase("Phase 3 — Authorise",
            "Different from authentication. Even if it really is the customer, are they "
            "<em>allowed</em> to do this transaction right now? Checks include: per-transaction "
            "limit, daily / monthly limits, KYC tier, beneficiary cooling-off (24 h for new UPI "
            "payees above ₹2,000), sanctions screening against OFAC / UN / Ministry of Home "
            "Affairs lists, AML (Anti-Money Laundering) rules, real-time fraud score, MCC "
            "(Merchant Category Code) restrictions for cards, country / currency restrictions for "
            "cross-border.",
            key_terms=[
                ("Sanctions screening", "Matching customer or beneficiary names against lists "
                 "(OFAC SDN in the US, UN consolidated, EU consolidated, HMT in the UK, MHA UAPA "
                 "in India). A potential match parks the transaction for compliance review."),
                ("KYC tier", "Different transaction limits apply based on the depth of identity "
                 "verification — min-KYC, full-KYC, video-KYC."),
                ("MCC", "Merchant Category Code — 4-digit ISO 18245 code on every card payment; "
                 "controls limits, fraud rules, interchange fees, rewards eligibility."),
            ])
        + _phase("Phase 4 — Validate",
            "Mechanical checks: is the message well-formed against its schema, is the account "
            "active and not frozen, is the balance sufficient including overdraft, are mandatory "
            "regulatory fields present (LEI for ≥ ₹50 cr Indian RTGS, purpose code for cross-"
            "border, beneficiary name confirmation under the UK Confirmation of Payee scheme).")
        + _phase("Phase 5 — Route",
            "Pick a rail and the next hop on it. Inside a single rail there is still routing: for "
            "UPI the payer PSP (Payment Service Provider) routes to NPCI, NPCI routes to the "
            "payee bank by IFSC (Indian Financial System Code, the 11-character branch identifier); "
            "for SWIFT the message hops correspondent → correspondent → beneficiary bank. Routing "
            "is where rail-specific business logic lives, including least-cost routing across card "
            "networks and dynamic rail selection (e.g. fall back from FPS to BACS at UK cut-off).")
        + _phase("Phase 6 — Clear",
            "A neutral third party records the obligation between the two banks. The clearing "
            "house is the single most under-appreciated piece by outsiders. Each region has its "
            "own; we map them all in Section 4 and 5.")
        + _phase("Phase 7 — Settle",
            "Real money moves between bank accounts at the central bank. Two flavours:")
        + ul([
            "<strong>Real-Time Gross Settlement (RTGS)</strong> — each transaction settles "
            "individually, immediately, at full value, at the central bank. Eliminates "
            "<em>Herstatt risk</em> (paying your leg while the counterparty fails before paying "
            "theirs). Examples: India RTGS (RBI), Fedwire (US), CHAPS (UK), TARGET2 (Eurozone).",
            "<strong>Deferred Net Settlement (DNS)</strong> — many transactions are summed into a "
            "single net obligation per pair of banks per window, and only the net amount moves. "
            "Cheap and efficient at scale but creates a gap. Examples: UPI / IMPS / NEFT / NACH "
            "(India), ACH (US), BACS / FPS (UK), SEPA SCT (Europe).",
        ])
        + _phase("Phase 8 — Notify and Reconcile",
            "Push notification, SMS, email, merchant POS beep, audit log row, regulator report "
            "queue. At end of day every party exchanges files (NPCI MIS in India, SWIFT MT940 / "
            "MT950 statements globally, scheme network EOD files for cards, ACH return files in "
            "the US, BACS return file in the UK) and the bank’s reconciliation engines match "
            "counts and amounts. Mismatches are <em>operational risk</em> under Basel III and "
            "reportable under every region’s master directions.",
            key_terms=[
                ("Reconciliation", "Matching internal records to external counterparty and scheme "
                 "records. A bank that cannot reconcile cleanly has a regulatory problem long "
                 "before it has a customer problem."),
            ])
        + callout("The single most important sentence in this topic",
            p("<strong>Clearing is not the same as settlement.</strong> Clearing records who owes "
              "whom. Settlement is the actual cash movement at the central bank. The gap between "
              "them is where credit risk, treasury float, and most reconciliation work live."),
            "info")
    )
    return TopicSection("3.  How it actually works — phase by phase", "intermediate", body)


# Sections 4–10 follow in next files / appended later for token-budget reasons.
def _sec4() -> TopicSection:
    from .foundations_01_part2 import sec4_body
    return TopicSection("4.  Types & variations — the rails that move money worldwide",
                        "intermediate", sec4_body())


def _sec5() -> TopicSection:
    from .foundations_01_part2 import sec5_body
    return TopicSection("5.  Advanced — the seven mechanisms underneath every rail",
                        "advanced", sec5_body())


def _sec6() -> TopicSection:
    from .foundations_01_part3 import sec6_body
    return TopicSection("6.  BFSI overlay — what changes because it is a regulated bank, worldwide",
                        "advanced", sec6_body())


def _sec7() -> TopicSection:
    from .foundations_01_part3 import sec7_body
    return TopicSection("7.  Trade-offs and decisions a leader owns", "intermediate", sec7_body())


def _sec8() -> TopicSection:
    from .foundations_01_part3 import sec8_body
    return TopicSection("8.  Worked examples — numbers and decisions", "intermediate", sec8_body())


def _sec9() -> TopicSection:
    from .foundations_01_part3 import sec9_body
    return TopicSection("9.  Questions to ask the team in any design review", "basic", sec9_body())


def _sec10() -> TopicSection:
    from .foundations_01_part3 import sec10_body
    return TopicSection("10.  Red flags + topic glossary", "basic", sec10_body())


# ============================================================
# Section 0 primer (longest — kept inline so it loads first)
# ============================================================
_PRIMER_HTML = (
    primer(
        p("This bible assumes you have an MBA in Finance and no IT background. Before we touch "
          "banking transactions we build a tiny shared vocabulary from two anchors: "
          "<strong>(1)</strong> the laptop in front of you, and <strong>(2)</strong> the banking "
          "apps you already use. Every later concept scales up from one of those two anchors. "
          "Spend ten minutes here.")
    )
    + H3("0.1  The IT side — starting from your laptop")
    + it_anchor(
        p("Your laptop has four pieces. A bank’s data centre has the same four pieces, just "
          "thousands of times bigger and arranged for round-the-clock survival. If you know your "
          "laptop, you already know the shape of a bank’s tech estate.")
        + ul([
            "<strong>CPU</strong> — Central Processing Unit, the chip that runs instructions. "
            "Your laptop has maybe 8 cores. A bank server has 64–192 cores; a rack has dozens of "
            "those servers; a region has many racks.",
            "<strong>RAM</strong> — Random-Access Memory, fast temporary workspace that loses "
            "everything when power goes off. Your laptop has 8–32 GB. A bank server has 256 GB to "
            "4 TB. RAM is heavily used for caching the most-asked questions ('what is account X’s "
            "balance right now?').",
            "<strong>SSD</strong> — Solid-State Drive, persistent storage; survives power off. "
            "Your laptop has 256 GB to 2 TB. A bank uses Storage Area Networks (SAN) or Network "
            "Attached Storage (NAS), with terabytes to petabytes, mirrored to a second data centre "
            "before any write is considered safe.",
            "<strong>Network card / Wi-Fi</strong> — how your laptop talks to other computers. A "
            "bank server uses 10–100 gigabit-per-second cables and connects via switches and "
            "routers in a private network. Same idea, much faster, much more redundant.",
        ])
    )
    + p("Three more ideas you must know:")
    + ul([
        "A <strong>server</strong> is just a computer that is always on, always reachable, "
        "dedicated to answering requests. Your phone is a <strong>client</strong> talking to "
        "servers. Digital banking is clients (your phone, an ATM, a branch terminal) talking to "
        "servers (the bank’s computers).",
        "A <strong>data centre</strong> is a building full of servers, with backup power, fire "
        "suppression, biometric access, 24×7 staff. Banks operate two of them in different cities "
        "so an earthquake or fire never takes everything down.",
        "<strong>Cloud</strong> means renting computers from a provider — Amazon Web Services "
        "(AWS), Microsoft Azure, Google Cloud Platform (GCP), Oracle Cloud Infrastructure (OCI) — "
        "instead of buying your own. The provider runs the building and the servers; you rent by "
        "the hour or by the request. Banks use cloud for elastic scale and faster innovation but "
        "keep the most sensitive ledgers in regulator-approved cloud regions or in their own "
        "data centres.",
    ])
    + H3("0.2  The network — how messages move")
    + it_anchor(
        p("When you open a banking app, a message travels: phone → home Wi-Fi router → Internet "
          "Service Provider (ISP) → many routers across the internet → bank’s edge firewall → "
          "bank’s internal network → app server → database. Each hop is a different machine "
          "inspecting and forwarding your message. Round trip is typically 50–200 ms in India, "
          "80–250 ms London-to-Mumbai, 200–300 ms New York-to-Mumbai."),
        title="From what you already know — opening a banking app on Wi-Fi",
    )
    + p("Three rules of the network you must remember, because they explain everything later:")
    + ul([
        "The network can <em>lose, duplicate, delay or reorder</em> messages. So banks design "
        "every transaction so that a lost or duplicated message never causes a double debit. "
        "This rule alone justifies half the patterns in this bible.",
        "The network is <em>public</em> — anyone could listen. So all banking traffic is "
        "<em>encrypted</em> in transit using TLS (Transport Layer Security), which is what the "
        "lock icon in your browser means.",
        "Reaching a server <em>takes time</em>. That latency directly limits how snappy a digital "
        "experience can feel. Within India ≈ 20–100 ms; intercontinental 150–300 ms; "
        "Mumbai-to-Mumbai inside one data centre under 1 ms.",
    ])
    + H3("0.3  Software, applications, and APIs")
    + p("<strong>Software</strong> is just instructions a computer can read. <strong>Applications"
        "</strong> are big bundles of software for one purpose (your mobile banking app, the "
        "bank’s loan-origination system, the core banking system). An <strong>API</strong> "
        "(Application Programming Interface) is the contract by which one piece of software calls "
        "another.")
    + analogy(
        p("An API is like a printed form at a bank counter. The form has named fields ('Account "
          "No.', 'Amount', 'Beneficiary IFSC'). If you fill it correctly and submit at the right "
          "counter, the bank promises a specific response. APIs are those forms, exchanged "
          "between machines instead of humans.")
    )
    + p("When PhonePe shows your HDFC balance, PhonePe is calling an API at HDFC. When Citi "
        "exposes commercial-banking services to its corporate clients (CitiConnect APIs), it does "
        "so via APIs. The whole movement called <strong>Open Banking</strong> — PSD2 in Europe, "
        "the CMA Order in the UK, the Account Aggregator framework in India — is regulators "
        "forcing banks to expose APIs so other fintechs can build on top.")
    + H3("0.4  Databases and the ledger")
    + p("A <strong>database</strong> is software that stores facts in tables and lets other "
        "software ask questions of those facts very quickly. The most important database in any "
        "bank is the <strong>ledger</strong> — a giant table where every row is a debit or "
        "credit. Almost everything in BFSI ends with 'update the ledger' or 'read the ledger'.")
    + analogy(
        p("If your laptop had a notebook app where every line is dated and either says ‘+ ₹500’ "
          "or ‘− ₹500’ and the running balance is always derivable by summing — that is a ledger. "
          "The bank’s ledger is the same idea, billions of rows long, with iron-clad guarantees "
          "that no row is ever lost or secretly altered.")
    )
    + p("Two database properties matter throughout this bible:")
    + ul([
        "<strong>Transactional</strong> — the database can be told 'do all of these changes "
        "together or none of them'. This is what stops a transfer from debiting one account but "
        "failing to credit the other when power flickers. The technical word for this guarantee "
        "is <strong>ACID</strong> (Atomicity, Consistency, Isolation, Durability).",
        "<strong>Durable</strong> — once it says 'done', the data survives a power cut. Banking "
        "ledgers are obsessively durable; data is written to disk and copied to a backup data "
        "centre before the database admits success.",
    ])
    + H3("0.5  Synchronous vs asynchronous communication")
    + it_anchor(
        p("On your laptop: opening a web page is <em>synchronous</em> — you click, you wait, the "
          "page loads, you proceed. Email is <em>asynchronous</em> — you send and walk away; the "
          "recipient reads when they want. Both styles exist inside a bank, often in the same "
          "transaction."),
        title="From what you already know — clicking a link vs sending an email",
    )
    + p("Synchronous (request-reply) is used when the customer is waiting: tap-to-pay, balance "
        "check, login. Asynchronous (messaging or event-driven) is used for the audit log, the "
        "SMS, the fraud check, the regulatory report — anything that does not need to block the "
        "customer.")
    + H3("0.6  Encryption and keys")
    + p("<strong>Encryption</strong> scrambles data with a secret <strong>key</strong> so only "
        "someone with the matching key can read it. Every byte of banking traffic is encrypted "
        "in motion using TLS; almost all data is also encrypted at rest using algorithms such as "
        "AES-256 (Advanced Encryption Standard with a 256-bit key). Encryption keys themselves "
        "live in tamper-resistant hardware called an <strong>HSM</strong> (Hardware Security "
        "Module), certified at FIPS 140-2 Level 3 or 4 (US Federal Information Processing Standard).")
    + H3("0.7  The BFSI side — starting from things you already do")
    + bfsi_anchor(
        p("You already use a bank, so you already understand the user side of every concept in "
          "this bible. We just need to translate from the customer’s view to the engineering view.")
        + ul([
            "When you tap to send ₹500 on Google Pay you used <strong>UPI</strong> (Unified "
            "Payments Interface). Engineering view: PhonePe → NPCI (National Payments Corporation "
            "of India) → your bank’s core → NPCI → recipient’s bank.",
            "When you swipe a debit card at Starbucks you used the <strong>card network</strong> "
            "(Visa, Mastercard, RuPay). Engineering view: terminal → acquirer bank → card network "
            "→ issuer bank (your bank) → back to terminal — under three seconds.",
            "When you transfer ₹5 lakh to a friend in another city you probably used "
            "<strong>RTGS</strong> (Real-Time Gross Settlement). Engineering view: your bank → "
            "RBI → friend’s bank. RBI is the settlement bank.",
            "When you set up an automatic monthly EMI for a loan you authorised a "
            "<strong>NACH</strong> mandate (National Automated Clearing House). Each month NPCI "
            "pulls the EMI from your account and credits the lender.",
            "When you check your <strong>CIBIL</strong> score on a fintech app, that app called "
            "CIBIL’s API (after you consented). The consent itself flowed through the "
            "<strong>Account Aggregator</strong> framework regulated by RBI.",
        ])
    )
    + p("Now consider the same patterns abroad. HCLTech serves Citi, Standard Chartered, Deutsche "
        "Bank, Barclays, NatWest, JPMorgan, Wells Fargo, and many more — so global rails matter "
        "as much as Indian ones.")
    + bfsi_anchor(
        ul([
            "<strong>United States.</strong> Pay a contractor: <strong>ACH</strong> (Automated "
            "Clearing House) via FedACH (Federal Reserve) or EPN (The Clearing House). Pay rent "
            "instantly: <strong>Zelle</strong> for retail, <strong>RTP</strong> (Real-Time "
            "Payments by The Clearing House) for B2B, or <strong>FedNow</strong> (launched 2023) "
            "for any participant. Wire a large amount: <strong>Fedwire</strong> (RTGS at the Fed) "
            "for domestic, <strong>CHIPS</strong> for cross-border USD via The Clearing House.",
            "<strong>United Kingdom.</strong> Pay a bill: <strong>Faster Payments Service "
            "(FPS)</strong>, 24×7, instant, up to £1 million per transaction. Bulk salaries: "
            "<strong>BACS</strong> (Bankers’ Automated Clearing Services). Large value: "
            "<strong>CHAPS</strong> (Clearing House Automated Payment System) at the Bank of "
            "England — the UK RTGS.",
            "<strong>Eurozone.</strong> Send €500 to Berlin: <strong>SEPA Credit Transfer "
            "(SCT)</strong> next-business-day, or <strong>SEPA Instant (SCT Inst)</strong> in "
            "seconds. Direct debits: <strong>SEPA SDD</strong>. Large value: "
            "<strong>TARGET2</strong> at the European Central Bank (ECB); instant central-bank "
            "settlement: <strong>TIPS</strong> (TARGET Instant Payment Settlement).",
            "<strong>Singapore.</strong> <strong>FAST</strong> for instant, <strong>GIRO</strong> "
            "for batch, <strong>MEPS+</strong> at the Monetary Authority of Singapore (MAS) for "
            "RTGS.",
            "<strong>Cross-border.</strong> Most international wires still travel over "
            "<strong>SWIFT</strong> (Society for Worldwide Interbank Financial Telecommunication) "
            "— actually a messaging network, not a settlement network. Settlement happens through "
            "correspondent banks’ <strong>nostro / vostro</strong> accounts.",
        ])
    )
    + H3("0.8  The regulators in this story")
    + p("Every country has regulators whose rules constrain every technology choice the bank "
        "makes. You must know the principal ones by heart.")
    + table(
        ["Region", "Banking", "Securities", "Insurance", "Data protection"],
        [
            ["India", "RBI (Reserve Bank of India)",
             "SEBI (Securities and Exchange Board of India)",
             "IRDAI (Insurance Regulatory and Development Authority of India)",
             "MeitY under DPDP Act 2023"],
            ["United States",
             "Fed, OCC (Office of the Comptroller of the Currency), FDIC, CFPB, state regulators",
             "SEC, FINRA, CFTC for derivatives",
             "State insurance commissioners (NAIC)",
             "Sectoral — GLBA for finance, HIPAA for health, state laws (CCPA/CPRA, Virginia, etc.)"],
            ["United Kingdom",
             "BoE, PRA (Prudential Regulation Authority), FCA (Financial Conduct Authority)",
             "FCA", "FCA / PRA", "ICO under UK GDPR"],
            ["Eurozone", "ECB, EBA, national central banks", "ESMA", "EIOPA",
             "National DPAs under EU GDPR"],
            ["Singapore", "MAS — single integrated regulator", "MAS", "MAS",
             "PDPC under PDPA"],
        ]
    )
    + p("All of them, regardless of country, ultimately enforce the same six concerns: "
        "<em>solvency, consumer protection, anti-money laundering, data protection, operational "
        "resilience, and systemic stability</em>. The detail differs; the spirit does not.")
)
