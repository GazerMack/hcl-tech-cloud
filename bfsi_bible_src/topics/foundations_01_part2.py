"""Sections 4 and 5 of Foundations · 01 — split out for token-budget reasons."""
from __future__ import annotations

from ..site import (
    H3, H4, p, ul, ol, kv, callout, analogy, table, mermaid,
)


def sec4_body() -> str:
    return (
        p("Each rail is a different answer to the same eight-phase problem, optimised for a "
          "different combination of latency, value size, reversibility, geography, and regulator. "
          "A leader must know the headline of each by heart, in all the major geographies HCLTech "
          "serves.")
        + H3("4.1  India — the rails HCLTech engineers see daily")
        + table(
            ["Rail", "Operator", "Latency / window", "Value", "Settlement",
             "Reversibility", "Use cases"],
            [
                ["<strong>UPI</strong> (Unified Payments Interface)", "NPCI",
                 "≈ 2–5 sec, 24×7", "Per-txn ₹1 lakh (₹2–5 L select MCCs)",
                 "Net at RBI, multi-cycle daily", "No reversal; refund as new txn",
                 "P2P, P2M, autopay, recurring"],
                ["<strong>IMPS</strong> (Immediate Payment Service)", "NPCI",
                 "≈ 5–30 sec, 24×7", "Up to ₹5 lakh", "Net at RBI", "No reversal",
                 "P2P / A2A, NEFT-off-hours fallback"],
                ["<strong>NEFT</strong> (National Electronic Funds Transfer)", "RBI",
                 "Half-hourly batches, 24×7 since Dec 2019", "No floor, no cap",
                 "Net per batch at RBI", "Possible until processed",
                 "Salary, vendor, scheduled credits"],
                ["<strong>RTGS</strong> (Real-Time Gross Settlement)", "RBI",
                 "Seconds, 24×7 since Dec 2020", "Min ₹2 lakh, no upper cap",
                 "Real-time gross at RBI", "Effectively no",
                 "Large-value B2B, treasury, settlements"],
                ["<strong>NACH</strong>", "NPCI",
                 "Mandate setup minutes; debit cycle T+1 typical", "Mandate-defined",
                 "Net at NPCI / RBI", "Mandate-based reversal",
                 "EMIs, dividends, salary, SIPs"],
                ["<strong>RuPay / Visa / Mastercard</strong>", "Scheme network",
                 "Auth ≈ 1–3 sec; clearing T+1, settlement T+1 / T+2",
                 "Issuer / acquirer rules", "Net at scheme settlement bank",
                 "Chargeback 120 days", "POS, e-com, recurring, cards-in-app"],
                ["<strong>CTS</strong> (Cheque Truncation System)", "NPCI",
                 "T+1 typically", "Any value, declining usage", "Net at RBI",
                 "Possible until cleared", "Legacy, government, courts, some B2B"],
                ["<strong>e₹</strong> (Digital Rupee CBDC pilot)", "RBI",
                 "Seconds, 24×7", "Programmable", "On RBI ledger directly",
                 "Programmable refunds", "Pilot retail and wholesale"],
            ]
        )
        + H3("4.2  United States — Citi, JPM, Wells, BoA territory")
        + table(
            ["Rail", "Operator", "Latency", "Value", "Settlement", "Use cases"],
            [
                ["<strong>ACH</strong>", "FedACH (Federal Reserve) and EPN (The Clearing House)",
                 "Same-day or next-day batches", "No statutory cap; per-rule limits",
                 "Net at the Fed", "Payroll, bill pay, B2B, mortgage"],
                ["<strong>Fedwire</strong>", "Federal Reserve", "Seconds, business hours",
                 "Any value; large-value default", "Real-time gross at the Fed",
                 "High-value B2B, securities settlement, FX legs"],
                ["<strong>CHIPS</strong> (Clearing House Interbank Payments System)",
                 "The Clearing House", "Seconds, business hours",
                 "Large-value USD, often cross-border", "Real-time final net at end of day",
                 "Correspondent USD settlement, FX, cross-border wires"],
                ["<strong>RTP</strong> (Real-Time Payments)", "The Clearing House",
                 "Seconds, 24×7", "Up to USD 1 M (raised in 2024)",
                 "Real-time gross via pre-funded position at the Fed",
                 "Instant B2B, payroll, gig payouts"],
                ["<strong>FedNow</strong>", "Federal Reserve (public)", "Seconds, 24×7",
                 "USD 500K default; banks may lower", "Real-time gross at the Fed",
                 "Instant retail and business since July 2023"],
                ["<strong>Zelle</strong>", "Early Warning Services (consortium of US banks)",
                 "Seconds, 24×7", "Per-bank limits, often USD 1K–10K daily",
                 "Behind the scenes uses ACH or RTP",
                 "Consumer P2P, US-domestic only"],
                ["<strong>Visa / Mastercard / Amex / Discover</strong>", "Card networks",
                 "Auth seconds, settlement T+1 / T+2",
                 "Network and issuer rules", "Net at scheme settlement bank",
                 "POS, e-com, recurring"],
            ]
        )
        + H3("4.3  United Kingdom — Barclays, HSBC, NatWest, Standard Chartered")
        + table(
            ["Rail", "Operator", "Latency", "Value", "Settlement", "Use cases"],
            [
                ["<strong>FPS</strong> (Faster Payments Service)", "Pay.UK",
                 "Seconds, 24×7", "Up to £1 million per txn",
                 "Net at Bank of England with intraday cycles",
                 "Retail and business instant payments"],
                ["<strong>BACS</strong> (Bankers’ Automated Clearing Services)", "Pay.UK",
                 "Three-day cycle", "No statutory cap", "Net at Bank of England",
                 "Salary, Direct Debit, supplier payments"],
                ["<strong>CHAPS</strong> (Clearing House Automated Payment System)",
                 "Bank of England", "Seconds, business hours",
                 "Any value; large-value default", "Real-time gross at BoE",
                 "House purchases, large B2B, treasury"],
                ["<strong>Cheque & Credit Clearing (ICS)</strong>", "Pay.UK",
                 "Image-based, T+1", "Any", "Net at BoE", "Legacy cheques"],
                ["<strong>Confirmation of Payee (CoP)</strong>", "Pay.UK",
                 "Pre-payment name-check across all rails", "—", "—",
                 "Mandatory under PSR rules to fight Authorised Push Payment (APP) fraud"],
                ["<strong>Open Banking payments (PISP)</strong>",
                 "Banks under FCA / OBL standards",
                 "Seconds (uses FPS underneath)", "FPS limit", "Via FPS",
                 "Account-to-account e-commerce, bill pay"],
            ]
        )
        + H3("4.4  Eurozone and wider Europe — Deutsche, BNP Paribas, ING, Santander")
        + table(
            ["Rail", "Operator", "Latency", "Value", "Settlement", "Use cases"],
            [
                ["<strong>SEPA SCT</strong> (Credit Transfer)",
                 "EBA Clearing (STEP2) and national CSMs", "Next business day",
                 "No statutory cap", "Net at TARGET2",
                 "Standard EUR credit transfers across 36 SEPA countries"],
                ["<strong>SEPA SCT Inst</strong> (Instant)",
                 "TIPS, RT1 (EBA), national instant systems",
                 "≤ 10 seconds, 24×7", "Up to €100,000 (rising under the EU IPR)",
                 "Real-time gross at TARGET / TIPS",
                 "Instant retail and business; mandatory for euro-area banks under the 2024 IPR"],
                ["<strong>SEPA SDD</strong> (Direct Debit)",
                 "EBA Clearing and national CSMs", "Pre-notified pull",
                 "Mandate-defined", "Net at TARGET2",
                 "Recurring bills, B2B mandates"],
                ["<strong>TARGET2</strong>",
                 "Eurosystem (ECB + national central banks)", "Seconds, business hours",
                 "Any; large-value default", "Real-time gross at the ECB",
                 "Wholesale EUR, monetary-policy operations"],
                ["<strong>TIPS</strong> (TARGET Instant Payment Settlement)",
                 "Eurosystem", "Seconds, 24×7", "€100K typical cap",
                 "Real-time gross in central-bank money",
                 "Pan-European instant settlement layer"],
                ["<strong>T2S</strong> (TARGET2-Securities)", "Eurosystem", "Real-time",
                 "Securities + cash", "Delivery vs Payment in central-bank money",
                 "Pan-European securities settlement"],
            ]
        )
        + H3("4.5  Cross-border — SWIFT and beyond")
        + p("Cross-border payments still travel mostly over <strong>SWIFT</strong>, which is a "
            "<em>messaging</em> network, not a settlement network. Settlement happens via "
            "correspondent banks holding <strong>nostro accounts</strong> ('our account at a "
            "foreign bank') and <strong>vostro accounts</strong> ('your account at us').")
        + table(
            ["Mechanism", "What it is", "Use case"],
            [
                ["<strong>SWIFT MT</strong> (Message Type)",
                 "Colon-delimited legacy messages, e.g. MT103 (customer credit transfer), "
                 "MT202 (financial-institution transfer)",
                 "Being retired across cross-border by Nov 2025; still used elsewhere"],
                ["<strong>SWIFT MX / ISO 20022</strong>",
                 "XML-structured messages: <code>pacs.008</code> replaces MT103, "
                 "<code>pacs.009</code> replaces MT202, <code>pacs.002</code> for status",
                 "The new global standard; carries LEI, structured remittance, purpose codes"],
                ["<strong>SWIFT gpi</strong> (Global Payments Innovation)",
                 "End-to-end tracking, fee transparency, same-day finality across correspondent chains",
                 "Modern cross-border wires"],
                ["<strong>CLS</strong> (Continuous Linked Settlement)",
                 "FX settlement for 18 currencies with PvP (Payment versus Payment)",
                 "Eliminates Herstatt risk in major-currency FX trades"],
                ["<strong>Wise / Revolut / Airwallex multi-currency rails</strong>",
                 "Fintech-operated multi-rail networks that arbitrage local rails to cut cost",
                 "Retail and SME cross-border"],
                ["<strong>Project mBridge, Project Nexus</strong>",
                 "Central-bank multi-CBDC platforms in pilot",
                 "Future of low-friction cross-border, especially in Asia"],
            ]
        )
        + H3("4.6  Other regions you will encounter")
        + ul([
            "<strong>Singapore.</strong> FAST (instant), GIRO (batch), MEPS+ (RTGS), PayNow "
            "(proxy service over FAST). Cross-border instant linkages: PayNow ↔ UPI, "
            "PayNow ↔ PromptPay (Thailand).",
            "<strong>Hong Kong.</strong> FPS (HKICL), CHATS (Clearing House Automated Transfer "
            "System) for RTGS in HKD / USD / EUR / RMB.",
            "<strong>UAE.</strong> UAEFTS for RTGS, IPP (Instant Payment Platform launched 2023), "
            "Aani for retail instant payments.",
            "<strong>Australia.</strong> NPP (New Payments Platform) for instant via the Reserve "
            "Bank of Australia’s Fast Settlement Service, BECS for batch, RITS for RTGS.",
            "<strong>Brazil.</strong> PIX (instant, operated by Banco Central do Brasil) — the "
            "world’s most-used instant-payment rail by retail transaction count.",
        ])
        + analogy(
            p("If money were physical: <em>UPI / FPS / RTP / PIX / SCT Inst</em> are dropping "
              "cash through a slot to the neighbour — instant, small. <em>RTGS / Fedwire / CHAPS "
              "/ TARGET2</em> are armoured vans delivering crores directly between bank vaults — "
              "gross, immediate, big. <em>ACH / BACS / NACH / SEPA SCT</em> are the morning "
              "postal van picking up everyone’s envelopes and sorting at noon. <em>SWIFT</em> is "
              "courier across borders with three handlers in between. <em>Cards</em> are signing "
              "an IOU at a shop — the shopkeeper trusts the network to pay him in two days. "
              "<em>CBDC (e₹, eCNY, digital euro pilot)</em> is the central bank giving you a "
              "wallet directly — no commercial bank in the middle.")
        )
    )


def sec5_body() -> str:
    return (
        p("Senior engineers and architects spend their careers on these seven mechanisms. A "
          "leader does not have to implement them, but must know the words and the trade-offs "
          "precisely enough to push back, estimate, and triage.")
        + H3("5.1  Message format and schema")
        + ul([
            "<strong>SWIFT MT</strong> — colon-delimited text fields, e.g. <code>:50K:</code> "
            "ordering customer, <code>:71A:</code> charge bearer. Being retired across "
            "cross-border by Nov 2025.",
            "<strong>ISO 20022</strong> — XML schemas with rich structure: <code>pacs.008</code> "
            "for customer credit transfers, <code>pacs.009</code> for financial-institution "
            "transfers, <code>camt.053</code> for end-of-day statements, <code>pain.001</code> "
            "for customer-to-bank payment initiation. Carries LEI, structured remittance, "
            "ultimate debtor / creditor, purpose code — far richer than MT.",
            "<strong>ISO 8583</strong> — binary card-network format used by Visa, Mastercard, "
            "RuPay, Amex between issuer and acquirer.",
            "<strong>NPCI UPI common library</strong> — XML / JSON with NPCI doing PIN block "
            "encryption and message signing on the device.",
            "<strong>NACH / SFMS</strong> in India, <strong>NACHA file format</strong> in the "
            "US, <strong>Bacstel-IP</strong> in the UK, <strong>SEPA pain / pacs</strong> in "
            "the EU — each batch rail has its own schema.",
        ])
        + callout("Why ISO 20022 matters and is not 'just a format change'",
            p("ISO 20022 carries structured data SWIFT MT could not. AML and sanctions screening "
              "engines can now read fields directly instead of parsing free text. LEI becomes "
              "first-class. Purpose codes are explicit. Remittance information is structured "
              "(ideal for invoice reconciliation in corporate banking). Downstream analytics, "
              "screening, regulatory reporting, and customer experience all change — not just the "
              "wire format. HCLTech has live ISO 20022 migration programmes at multiple clients."),
            "info")
        + H3("5.2  Identity and addressing across rails")
        + table(
            ["Rail / region", "How an account or party is identified"],
            [
                ["UPI (India)",
                 "VPA (Virtual Payment Address, e.g. <code>alice@hdfc</code>) mapped internally "
                 "to IFSC + account number"],
                ["NEFT / RTGS / IMPS (India)", "IFSC (11-char) + account number"],
                ["ACH (US)", "Routing number (9-digit ABA / RTN) + account number"],
                ["Fedwire / CHIPS", "ABA + account or UID; CHIPS UID for participants"],
                ["FPS / BACS / CHAPS (UK)",
                 "Sort code (6-digit) + account number; Confirmation of Payee adds name-match"],
                ["SEPA",
                 "IBAN (International Bank Account Number, up to 34 chars, country-prefixed) + "
                 "BIC where required"],
                ["Cards",
                 "PAN (Primary Account Number, 16–19 digits) + CVV + expiry, tokenised after the "
                 "RBI CoFT and global PCI / network token services"],
                ["SWIFT", "BIC (Bank Identifier Code, 8 or 11 chars) + IBAN where applicable"],
                ["PIX (Brazil)", "PIX keys (CPF / CNPJ / email / phone / random)"],
            ]
        )
        + H3("5.3  Cryptography on the wire")
        + ul([
            "Transport security: TLS 1.2 minimum, TLS 1.3 preferred. mTLS between bank internal "
            "services and between bank and rail switch.",
            "Payload signing: <strong>JWS</strong> (JSON Web Signature) for API payloads; "
            "<strong>XMLDSig</strong> for SWIFT MX and NPCI common library; PKCS#7 / CMS for files.",
            "Key custody: <strong>HSM</strong> (Hardware Security Module) holds private keys in "
            "tamper-resistant hardware; FIPS 140-2 Level 3 minimum, Level 4 for the most "
            "sensitive (PIN-related) flows.",
            "PIN block encryption: rotating session keys derived from a master under "
            "<strong>DUKPT</strong> (Derived Unique Key Per Transaction) so a compromised key "
            "reveals at most one transaction.",
            "Post-quantum readiness: NIST published final standards in 2024 (ML-KEM, ML-DSA, "
            "SLH-DSA). BFSI is in inventory-and-plan phase; major banks have started crypto-"
            "agility programmes so they can swap algorithms without re-architecting.",
        ])
        + H3("5.4  Clearing houses by region")
        + table(
            ["Region", "Clearing house(s)"],
            [
                ["India", "NPCI (UPI, IMPS, NACH, RuPay, CTS), RBI (NEFT, RTGS)"],
                ["United States",
                 "FedACH and EPN for ACH, CHIPS for large-value, Fedwire for RTGS, FedNow for "
                 "instant, RTP at The Clearing House"],
                ["United Kingdom", "Pay.UK (BACS, FPS, ICS), Bank of England (CHAPS RTGS)"],
                ["Eurozone",
                 "EBA Clearing (STEP2 for SEPA SCT/SDD, RT1 for instant), Eurosystem (TARGET2, "
                 "TIPS, T2S), national CSMs in each country"],
                ["Singapore", "BCS (FAST, GIRO), MAS (MEPS+ RTGS)"],
                ["Cards globally",
                 "Visa, Mastercard, American Express, JCB, Discover, RuPay, UnionPay — act as "
                 "both clearing and rail"],
            ]
        )
        + H3("5.5  Settlement risk (Herstatt) and how the industry contains it")
        + p("Named after Bankhaus Herstatt, a German bank that failed in 1974 mid-day after "
            "taking in Deutsche Marks but before paying out US Dollars — counterparties lost the "
            "dollar leg. The lesson re-shaped FX settlement forever.")
        + ul([
            "<strong>RTGS</strong> for high-value: each leg settles atomically at the central "
            "bank; no exposure window.",
            "<strong>CLS</strong> for FX in 18 currencies: both legs settle simultaneously or not "
            "at all (Payment versus Payment).",
            "<strong>Default funds and margins</strong> at the clearing house so a member failure "
            "does not cascade.",
            "<strong>Loss-sharing rules</strong> in the rail rulebook (UPI, NACH, RTP, BACS all "
            "have detailed rulebooks).",
            "<strong>Sponsored access / pre-funding</strong> for instant rails (RTP, FedNow, SEPA "
            "Inst) — participants pre-fund a position so settlement is always covered.",
        ])
        + H3("5.6  Idempotency, sagas, and the outbox pattern")
        + p("Inside a bank, a single transaction usually crosses 5–15 services and 2–5 databases. "
            "Three patterns are mandatory; if your team is not using them, retries will eventually "
            "duplicate money.")
        + ul([
            "<strong>Idempotency key</strong> — client-generated unique ID per request. The first "
            "call performs the action and stores (key → result). Any retry with the same key "
            "returns the stored result. Standard TTL: 24 hours. Stripe popularised this for APIs; "
            "every payment switch in the world now uses it internally.",
            "<strong>Saga</strong> — replaces the impossible cross-service 'two-phase commit'. "
            "Each step is a local transaction with a defined compensating action. If step 4 "
            "fails, steps 1–3 are reversed. Used for transfers spanning multiple core banking "
            "systems (very common at Citi, JPM, Standard Chartered which have many legacy cores).",
            "<strong>Outbox pattern</strong> — write the business change <em>and</em> an 'outbox' "
            "row in the same database transaction; a relay process later reads the outbox and "
            "publishes to the messaging system. Solves 'did we crash before sending the event' "
            "without a distributed transaction.",
        ])
        + mermaid(
            'sequenceDiagram\n'
            '  autonumber\n'
            '  participant C as Customer App\n'
            '  participant G as API Gateway\n'
            '  participant T as Transfer Service\n'
            '  participant L as Ledger DB\n'
            '  participant Q as Event Bus Kafka\n'
            '  C->>G: POST /transfer (Idempotency-Key ABC123)\n'
            '  G->>T: forward (mTLS, signed)\n'
            '  T->>L: BEGIN tx, debit, insert outbox row, COMMIT\n'
            '  L-->>T: ok\n'
            '  T-->>G: 202 Accepted\n'
            '  G-->>C: 202 Accepted\n'
            '  Note over T,Q: separate relay, runs continuously\n'
            '  T->>Q: publish OutboxEvent\n'
            '  Q-->>T: ack and mark outbox row sent',
            "Idempotency key + outbox + asynchronous event publish — the BFSI baseline pattern.",
        )
        + H3("5.7  Reconciliation in detail")
        + p("At end of day every external counterparty (NPCI, RBI, Fed, Pay.UK, EBA, scheme "
            "networks, correspondent banks, SWIFT) sends files. The bank’s reconciliation engine "
            "matches each external record to internal postings and produces three buckets: "
            "matched, missing on our side, missing on their side. Each unmatched item ('break') "
            "has an SLA for investigation.")
        + p("Tools commonly seen in HCLTech engagements: <strong>Intellect Quantum SmartRecon"
            "</strong>, <strong>Oracle FCC</strong> (Financial Crime Compliance suite), "
            "<strong>FIS IntelliMatch</strong>, <strong>SmartStream TLM</strong>, and a long "
            "tail of in-house engines.")
    )
