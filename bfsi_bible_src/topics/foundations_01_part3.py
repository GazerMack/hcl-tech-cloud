"""Sections 6–10 of Foundations · 01."""
from __future__ import annotations

from ..site import (
    H3, p, ul, ol, kv, callout, example, red_flag, table,
)


def sec6_body() -> str:
    return (
        p("Every technology choice above is constrained by regulation. A leader must know the key "
          "rules verbatim in every region the client operates. The matrix below maps each concern "
          "to its principal rule in India, the United States, the United Kingdom, the Eurozone, "
          "and Singapore.")
        + table(
            ["Concern", "India", "United States", "United Kingdom", "Eurozone", "Singapore"],
            [
                ["Payment data localisation",
                 "RBI Storage of Payment System Data (Apr 2018) — full payment data lifecycle "
                 "stored only in India",
                 "No general localisation; some state laws and OFAC restrictions",
                 "UK GDPR with international transfer mechanisms",
                 "EU GDPR — Schrems II constraints on transfers to the US",
                 "PDPA + MAS technology risk guidelines"],
                ["Customer data privacy",
                 "DPDP Act 2023 — consent, purpose limitation, breach notification, Significant "
                 "Data Fiduciary obligations",
                 "Sectoral — GLBA for finance, HIPAA for health, state laws (CCPA/CPRA, Virginia, "
                 "Colorado)",
                 "UK GDPR, Data Protection Act 2018",
                 "EU GDPR",
                 "PDPA"],
                ["Cybersecurity baseline",
                 "RBI Cybersecurity Framework, SEBI CSCRF 2024, RBI IT Governance MD Nov 2023",
                 "NIST CSF, NYDFS Part 500, FFIEC IT Examination Handbook",
                 "PRA SS1/21, FCA operational-resilience policy",
                 "EU DORA effective Jan 2025, NIS2 directive",
                 "MAS TRM and Notice 655"],
                ["Outsourcing / cloud",
                 "RBI Outsourcing of IT Services MD Apr 2023",
                 "OCC Bulletin 2023-17, Fed SR 23-4 on TPRM",
                 "PRA SS2/21",
                 "EBA outsourcing guidelines",
                 "MAS Outsourcing Guidelines"],
                ["Card data protection",
                 "RBI CoFT Jul 2022 — merchants cannot store PAN",
                 "PCI DSS 4.0; Reg E for liability",
                 "PCI DSS 4.0; SCA under PSR rules",
                 "PCI DSS 4.0; PSD2 SCA",
                 "PCI DSS; MAS payment-card guidelines"],
                ["AML / KYC / CFT",
                 "PMLA 2002 + amendments; RBI MD KYC; FIU-IND reports (CTR, STR)",
                 "BSA, Patriot Act, FinCEN reporting (CTR, SAR)",
                 "MLR 2017, JMLSG Guidance",
                 "AMLD6 + EU AML package 2024",
                 "MAS Notice 626, CDSA"],
                ["Sanctions screening",
                 "MHA UAPA, RBI alert lists, MEA lists",
                 "OFAC SDN, sectoral lists",
                 "OFSI consolidated list under HMT",
                 "EU consolidated sanctions list",
                 "MAS targeted financial sanctions"],
                ["Operational resilience",
                 "RBI BCP-DR MD, IRDAI BCP guidelines",
                 "OCC heightened standards, FFIEC handbook",
                 "PRA / FCA / BoE Operational Resilience policy (impact tolerances, important "
                 "business services)",
                 "EU DORA — ICT risk, incident reporting, threat-led pen testing",
                 "MAS Notice 658 on BCM"],
                ["Customer liability / protection",
                 "RBI Limited Liability framework 2017 — zero liability if reported within 3 days",
                 "Reg E, Reg Z, Reg DD",
                 "FCA APP fraud reimbursement rules (mandatory from Oct 2024)",
                 "PSD2 / PSD3 proposal",
                 "MAS Shared Responsibility Framework"],
            ]
        )
        + H3("6.1  How to read a regulator circular like a leader")
        + ul([
            "Identify the <em>scope</em> first (which entities, which transactions, which dates).",
            "Find the <em>obligations</em> (must do, must not do, must report).",
            "Find the <em>timelines</em> (effective date, transition window, reporting cadence).",
            "Find the <em>penalties</em> (monetary fines, business restrictions, individual "
            "liability — SMCR in the UK, SR & CCB roles in the US, MAS Senior Manager regime in "
            "Singapore).",
            "Translate each obligation to a layer in the seven-layer model (channel, app, data, "
            "platform, security, etc.) — that is where the engineering change happens.",
        ])
    )


def sec7_body() -> str:
    return table(
        ["Decision", "Option A", "Option B", "When A wins", "When B wins"],
        [
            ["Sync vs async rail",
             "Sync (UPI / IMPS / RTGS / FedNow / FPS / RTP / SCT Inst)",
             "Async (NEFT / ACH / BACS / SEPA SCT / SWIFT)",
             "Customer-facing, low value, retry-tolerant",
             "Bulk, scheduled, high value with stronger investigation"],
            ["Gross vs net settlement",
             "Gross (RTGS, Fedwire, CHAPS, TARGET2, TIPS, FedNow)",
             "Net (UPI, ACH, BACS, FPS, SEPA SCT)",
             "Systemic risk material; large value",
             "High volume, low value, liquidity-efficient"],
            ["Push vs pull",
             "Push (credit transfer, RTP, FPS, SCT Inst, UPI P2P)",
             "Pull (mandate, card, NACH, BACS DD, SEPA SDD)",
             "Funds must move only on payer consent each time",
             "Recurring, merchant-initiated, subscription"],
            ["Build vs use scheme",
             "Build proprietary closed-loop",
             "Use rail (UPI, scheme, FPS, RTP)",
             "Closed ecosystem (metro card, captive wallet)",
             "Interoperability, network effects, regulator coverage"],
            ["Reversibility design",
             "Hard final (instant rails, RTGS)",
             "Soft final + chargeback (cards) or recall (SWIFT)",
             "Low-value, retry-cheap, fraud rare",
             "High dispute volume, consumer-protection regulator pressure"],
            ["On-prem vs cloud for rail core",
             "On-prem / private cloud",
             "Public cloud (regulator-approved region)",
             "Sovereignty, lowest-latency, strict data localisation (India)",
             "Elastic scale (UPI volumes), faster innovation, lower TCO (Wells RTP modernisation, "
             "Citi cloud migrations)"],
        ]
    )


def sec8_body() -> str:
    return (
        example("India — UPI P2M of ₹250 at a kirana shop",
            ol([
                "Customer scans the merchant QR; payer app constructs intent: VPA "
                "<code>kiranabest@hdfc</code>, amount ₹250, MCC 5411 (grocery).",
                "Customer enters UPI PIN. PIN block is encrypted using the NPCI common library "
                "with a session key derived from the device’s registered key.",
                "Payer PSP (e.g. PhonePe) sends ReqPay to the NPCI UPI Switch over mTLS, with "
                "device fingerprint and risk signals.",
                "NPCI routes a debit-auth to the payer bank (HDFC). The core checks balance, "
                "daily limit (₹1 lakh default), MCC restrictions, beneficiary cooling-off, "
                "fraud score.",
                "Payer core debits the customer’s account in its ledger and returns success.",
                "NPCI sends credit instruction to the payee bank (e.g. ICICI). Payee bank credits "
                "the merchant settlement account.",
                "Both PSPs return success; both apps show 'Paid'; merchant POS beeps; customer "
                "SMS arrives within seconds.",
                "End-of-day, NPCI computes net positions and sends settlement files to RBI; the "
                "actual funds move in the next settlement window. The kirana shop sees the ₹250 "
                "in their account immediately for usage, but the bank itself is settled later.",
            ]))
        + example("United States — Standard Chartered NY pays a vendor USD 750,000 via Fedwire",
            ol([
                "Treasury operations initiates Fedwire from the wire-room application.",
                "Authentication: two-person approval, PKI-signed authorisation tokens; mTLS into "
                "the FedLine Direct gateway.",
                "Authorisation: limit checks, OFAC sanctions screening on beneficiary and "
                "originator, internal AML score.",
                "Validation: ISO 20022 <code>pacs.009</code> well-formed; beneficiary Routing "
                "Number / account verified; LEI present.",
                "Routing: message sent over FedLine to the Federal Reserve.",
                "Clearing and Settlement: Fedwire is RTGS — the Fed simultaneously debits "
                "Standard Chartered NY’s reserve account and credits the beneficiary bank’s "
                "reserve account at the Fed. Final.",
                "Notify: <code>pacs.002</code> status returns; internal ledger posts; SWIFT gpi "
                "tracker shows 'credited' within minutes if downstream rails are clean.",
            ]))
        + example("United Kingdom — Barclays pays a salary of £4,500 via FPS",
            ol([
                "Employer sends a payroll file or API call to Barclays Business Banking.",
                "Confirmation of Payee runs against the beneficiary name and sort code to prevent "
                "APP fraud.",
                "Barclays sends FPS message to Pay.UK; the Pay.UK FPS Central Infrastructure "
                "routes to the beneficiary bank.",
                "Beneficiary bank credits the employee; both banks’ positions move at the Bank of "
                "England at the next FPS settlement cycle.",
                "Employee receives the £4,500 within seconds, even on a Sunday night.",
            ]))
        + example("Eurozone — Deutsche Bank pays a supplier €120,000 via SEPA SCT Inst",
            ol([
                "Corporate client submits <code>pain.001</code> file via Deutsche Bank Corporate "
                "Cash Management portal.",
                "Deutsche performs sanctions screening (EU consolidated, OFAC if any US nexus, "
                "German national list).",
                "Message <code>pacs.008</code> sent to TIPS via the Eurosystem.",
                "TIPS atomically debits Deutsche’s pre-funded TIPS account and credits the "
                "beneficiary bank’s TIPS account at the ECB.",
                "Beneficiary bank credits the supplier; <code>pacs.002</code> returns confirmed.",
                "Total elapsed: under 10 seconds, 24×7. Mandatory across the euro area under the "
                "2024 Instant Payments Regulation (IPR).",
            ]))
        + example("Cross-border — Citi New York to Standard Chartered Hong Kong, USD 50,000",
            ol([
                "Indian or US remitter initiates USD 50,000 via Citi cash management.",
                "ISO 20022 <code>pacs.008</code> is constructed (post-Nov 2025 cutover), with "
                "ordering customer, beneficiary, charges (OUR/SHA/BEN), purpose code, LEI.",
                "Sanctions screening at Citi against OFAC SDN, UN, UK HMT lists. A fuzzy match → "
                "manual review by compliance.",
                "Message routes via Citi’s correspondent network; CHIPS used for the USD leg if "
                "the ultimate beneficiary bank holds USD with a CHIPS member.",
                "Standard Chartered HK receives the message, performs its own AML / sanctions, "
                "credits the beneficiary in HKD after FX conversion.",
                "Customer’s account was debited at initiation but the USD only fully settles at "
                "the correspondent next business day — the <em>float</em> is a real treasury P&amp;L "
                "line.",
                "SWIFT gpi tracks the entire chain end-to-end; both banks see status timestamps.",
            ]))
        + example("Why a ₹3,00,000 ‘instant’ transfer fails on UPI but succeeds on RTGS",
            p("Customer tries to pay ₹3,00,000 on UPI. Payer PSP returns a per-transaction limit "
              "error because UPI P2P is capped at ₹1 lakh (₹2–5 lakh for select MCCs per NPCI "
              "circulars). The same ₹3,00,000 on RTGS succeeds because RTGS has a ₹2 lakh "
              "<em>minimum</em> and no upper cap, settles gross at RBI in real time, and has "
              "stronger AML controls (LEI mandatory ≥ ₹50 cr). A leader should know this without "
              "checking — limits and rails are policy, not engineering."))
    )


def sec9_body() -> str:
    return ol([
        "Which exact rail does this user journey use, and what is its per-transaction limit, "
        "cut-off time, and reversibility model?",
        "Where is the idempotency key generated, where is it stored, and what is its TTL?",
        "If clearing succeeds but our internal posting fails, what compensating transaction "
        "fires, and how soon?",
        "What is our reconciliation lag with the scheme / switch and what is the dispute SLA?",
        "Which fields of the message carry PII or PAN, and where do they get tokenised?",
        "Are we using ISO 20022 native fields or are we still mapping from MT? What information "
        "do we lose in that mapping?",
        "What happens to in-flight transactions when the rail’s switch is down — do we queue, "
        "fail-fast, or fall back to a different rail?",
        "How do we prove to the regulator, after the fact, that a specific transaction was "
        "authorised by the customer?",
        "Where in the eight phases is our highest p99 latency, and is it network, compute, or DB?",
        "What is our blast radius if NPCI / SWIFT / the scheme is down for an hour?",
        "Across geographies — for the same client, are our resilience postures (DORA in EU, "
        "PRA / FCA in UK, RBI in India, OCC in US) all tested with the same rigour, or have we "
        "let one drift?",
    ])


def sec10_body() -> str:
    return (
        red_flag(ul([
            "‘We’ll just retry on timeout.’ Without an idempotency key this duplicates money.",
            "‘Reconciliation is a back-office problem, not ours.’ Engineering owns recon design "
            "or operations carry the loss.",
            "‘We store the PAN encrypted, that’s enough.’ Encrypted PAN is still in PCI scope; "
            "tokenisation is the answer.",
            "‘UPI is just like a wallet.’ UPI is a rail; a wallet is a stored-value instrument. "
            "Different limits, different regulators, different KYC.",
            "‘Chargebacks don’t apply to us.’ If you accept cards anywhere in the chain, they do.",
            "‘ISO 20022 is just a format change.’ It changes data semantics — downstream "
            "analytics, AML rules, and screening logic must adapt.",
            "‘We don’t need to localise data, our customers don’t mind.’ RBI, MAS, and a growing "
            "set of regulators do. This is not negotiable for payment data.",
            "‘Our resilience plan is the same across regions.’ DORA (EU) demands threat-led pen "
            "testing; FCA demands impact tolerances; RBI demands BCP-DR drills with regulator "
            "involvement. They are not interchangeable.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("PSP", "Payment Service Provider — the app or bank a customer interacts with on a rail."),
            ("VPA", "Virtual Payment Address — UPI handle like <code>alice@hdfc</code>."),
            ("Idempotency key", "Client-generated unique ID that lets a server safely retry "
             "without duplicating effects."),
            ("Nostro / Vostro", "‘Our account at a foreign bank’ / ‘your account with us’ — the "
             "plumbing for cross-border settlement."),
            ("LEI", "Legal Entity Identifier — 20-char ISO 17442 code mandatory for ≥ ₹50 cr "
             "RTGS / NEFT and most cross-border."),
            ("CoFT", "Card-on-File Tokenisation — RBI rule replacing stored PAN with a "
             "merchant-specific token."),
            ("pacs.008 / pacs.009", "ISO 20022 customer / financial-institution credit-transfer "
             "messages replacing SWIFT MT103 / MT202."),
            ("MCC", "Merchant Category Code — 4-digit ISO 18245; controls limits, fraud rules, "
             "interchange, rewards."),
            ("Float", "Money the bank effectively holds during the clearing-to-settlement gap; "
             "earns interest in treasury."),
            ("Settlement risk (Herstatt)", "Risk that you pay your leg but the counterparty fails "
             "before paying theirs."),
            ("PvP", "Payment versus Payment — both legs of an FX trade settle simultaneously or "
             "not at all (CLS does this)."),
            ("Saga", "Sequence of local transactions with compensating actions on failure; "
             "replaces 2-phase commit across services."),
            ("Outbox pattern", "Write business change and an outbox row in one DB transaction; a "
             "relay publishes to the broker — solves the dual-write problem."),
            ("HSM", "Hardware Security Module — tamper-resistant device holding cryptographic "
             "keys; FIPS 140-2 Level 3+ in BFSI."),
            ("DUKPT", "Derived Unique Key Per Transaction — PIN-encryption scheme that uses a "
             "fresh derived key for every transaction."),
            ("CHIPS", "Clearing House Interbank Payments System — large-value USD private "
             "settlement at The Clearing House."),
            ("FedNow", "US Federal Reserve instant-payments service launched July 2023."),
            ("FPS / BACS / CHAPS", "UK rails: instant, batch, large-value RTGS respectively."),
            ("SEPA / TIPS / TARGET2", "Eurozone: pan-European credit/direct debit, instant "
             "settlement, large-value RTGS."),
            ("DORA", "Digital Operational Resilience Act — EU regulation effective Jan 2025 "
             "covering ICT risk in financial services."),
        ])
    )
