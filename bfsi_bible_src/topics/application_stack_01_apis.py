"""Application Stack · 01 — APIs and integration: REST, gRPC, GraphQL, ISO 20022,
Open Banking and Account Aggregator."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="II.1",
        slug="01-apis-and-integration",
        title="APIs and integration — REST, gRPC, GraphQL, ISO 20022, Open Banking",
        one_liner=(
            "Modern banks are not single applications; they are <em>networks</em> of "
            "applications. The wires between those applications are Application "
            "Programming Interfaces (APIs) and message standards. This topic gives you "
            "a working vocabulary — REST, gRPC, GraphQL, webhooks, event streams, ISO "
            "20022, SWIFT MT, FIX, FpML — plus the regulator-driven schemes that have "
            "made APIs a board-level conversation: PSD2/PSD3 in Europe, Open Banking in "
            "the United Kingdom, the Financial Data Exchange (FDX) in the United "
            "States, the Account Aggregator (AA) framework in India, and the Singapore "
            "Financial Data Exchange (SGFinDex)."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


# ----------------------------------------------------------------- 0. Primer
def _sec0() -> TopicSection:
    body = (
        primer(
            p("Almost every BFSI conversation about ‘digital’, ‘Open Banking’, "
              "‘embedded finance’, ‘ISO 20022’, ‘core modernisation’ or ‘ecosystem "
              "play’ is, underneath, an API conversation. An <strong>API "
              "(Application Programming Interface)</strong> is simply a "
              "<em>contract</em> between two pieces of software: <em>‘if you send me "
              "this, I will send you that, and here are the rules’</em>. The rest of "
              "this topic is variations on that one idea — different transports, "
              "different shapes, different governance, different regulators.")
        )
        + H3("0.1  IT-side anchor — every app on your laptop is already an API consumer")
        + it_anchor(
            p("Open the weather widget on your phone. It does not have weather data "
              "of its own; it asks a server, <code>GET /forecast?lat=…&lon=…</code>, "
              "and gets back a small bundle of JavaScript Object Notation (JSON) — "
              "a few numbers and strings — which it draws as a sun or a cloud. That "
              "is a <strong>Representational State Transfer (REST) API</strong>. The "
              "‘Add to Calendar’ button on a flight confirmation email calls a "
              "different API on your calendar service. The ‘Sign in with Google’ "
              "button is a third API (Google’s OAuth 2.0 / OpenID Connect). You "
              "have been using APIs for years — you just didn’t see the wires.")
        )
        + H3("0.2  BFSI-side anchor — what you already trigger as a customer")
        + bfsi_anchor(
            p("When you tap a Unified Payments Interface (UPI) icon in PhonePe, "
              "PhonePe is not your bank. PhonePe calls UPI APIs at the National "
              "Payments Corporation of India (NPCI), which calls APIs at your bank "
              "to debit you and at the merchant’s bank to credit them. When you "
              "open a budgeting app like Emma in the United Kingdom and link your "
              "Barclays account, Emma is calling Barclays’ Open Banking APIs under "
              "Payment Services Directive 2 (PSD2) rules. When you authorise a "
              "lending app in India to read your bank statements through an "
              "Account Aggregator, that too is APIs all the way down. When a "
              "salary credit appears in your account at 9 a.m. on the first of "
              "the month, your bank received an ISO 20022 <code>pacs.008</code> "
              "credit-transfer message over a payment rail. Every one of these is "
              "an API call (or an API-shaped message) you authorise without "
              "seeing.")
        )
        + H3("0.3  The four families of APIs you must recognise")
        + ul([
            "<strong>Synchronous request / response</strong> — caller waits for an "
            "answer. REST, gRPC, GraphQL, SOAP. Used for ‘what is this customer’s "
            "balance right now?’.",
            "<strong>Asynchronous messaging / events</strong> — caller fires and "
            "moves on; a message broker delivers later. Apache Kafka, IBM MQ, "
            "RabbitMQ, AWS Simple Notification Service / Simple Queue Service "
            "(SNS/SQS), Azure Service Bus. Used for ‘a payment has been booked, "
            "tell every interested system’.",
            "<strong>Webhooks</strong> — server <em>calls back</em> the client at a "
            "URL the client registered. Used by Stripe, PayPal, Razorpay, GoCardless "
            "for payment status updates.",
            "<strong>File transfers</strong> — yes, still. Bulk SWIFT MT940 / "
            "MT942 statement files, NACHA / Bacs / SEPA batch files, regulator "
            "returns. The ‘API’ here is a file format and a Secure File Transfer "
            "Protocol (SFTP) drop. Do not laugh; trillions of dollars still flow "
            "this way every day.",
        ])
        + H3("0.4  The two ‘shapes’ of API conversation")
        + ul([
            "<strong>Resource-oriented</strong> — ‘nouns over verbs’. <em>GET "
            "/accounts/123</em>, <em>POST /payments</em>. The Hypertext Transfer "
            "Protocol (HTTP) verbs do the work. REST and most Open Banking APIs "
            "follow this.",
            "<strong>Action / RPC-oriented</strong> — ‘call this function’. "
            "<em>TransferFunds(from, to, amount)</em>. gRPC, SOAP, and many "
            "internal core-banking APIs follow this.",
        ])
    )
    return TopicSection(
        "0.  Primer — what an API is, said five different ways", "basic", body)


# ----------------------------------------------------------------- 1. Why
def _sec1() -> TopicSection:
    body = (
        p("APIs exist because banks are, at heart, <em>integration problems</em>. A "
          "single retail customer journey — say, opening an account on a phone — "
          "touches, in a typical tier-1 bank, between 15 and 40 internal systems: "
          "core banking, customer master, Know-Your-Customer (KYC), credit bureau, "
          "fraud, sanctions, document management, card issuance, mobile banking, "
          "notifications, regulatory reporting. None of those was built by the same "
          "team or in the same decade. APIs are the only way the bank gets to "
          "behave as one institution to its customer.")
        + p("Five forces have made APIs the centre of the BFSI conversation in the "
            "2020s:")
        + ol([
            "<strong>Open finance regulation.</strong> PSD2 (Europe, 2018), Open "
            "Banking (UK, 2018), the Account Aggregator framework (India, 2021), "
            "FDX standardisation (US, 2018→), Consumer Data Right (Australia, "
            "2020), SGFinDex (Singapore, 2020), Open Finance Brazil (2021), and "
            "the upcoming PSD3 / Payment Services Regulation (2026+) make APIs "
            "<em>mandatory</em>, with response-time and reliability obligations.",
            "<strong>Embedded finance and Banking-as-a-Service (BaaS).</strong> "
            "Apple Pay, Apple Cash, Apple Card, Amazon ‘Buy Now Pay Later’, Shopify "
            "Capital, Uber driver bank accounts — none of these are banks; they are "
            "API consumers of banks (Goldman Sachs, Green Dot, Cross River, "
            "Solarisbank, Stripe Treasury, Railsbank/Railsr, M2P, Decentro).",
            "<strong>Cloud-native architecture.</strong> Microservices only work if "
            "the contract between them is explicit. APIs are that contract.",
            "<strong>Payments modernisation.</strong> The global migration from "
            "SWIFT MT to <strong>ISO 20022</strong> messages (cross-border "
            "co-existence ends 22 November 2025) is the largest single API-style "
            "rewiring in banking history.",
            "<strong>AI agents.</strong> Large Language Model (LLM) agents act on "
            "the world only through tools — and tools are APIs. The clean, "
            "well-described API estate of 2025 is, accidentally, the foundation of "
            "the agentic banking of 2027.",
        ])
    )
    return TopicSection(
        "1.  Why APIs are now a board-level topic — first principles",
        "basic", body)


# ----------------------------------------------------------------- 2. Picture
def _sec2() -> TopicSection:
    body = (
        p("A modern bank’s API estate has four concentric rings. The closer to the "
          "outside, the more eyes (and regulators) watching.")
        + mermaid(
            'flowchart LR\n'
            '  subgraph "Ring 1 — Internal APIs"\n'
            '    A["Core banking<br/>balances, postings"]\n'
            '    B["Customer master<br/>KYC, addresses"]\n'
            '    C["Cards, lending<br/>fraud, AML"]\n'
            '  end\n'
            '  subgraph "Ring 2 — Channel APIs"\n'
            '    D["Mobile / web BFF<br/>Backend-for-Frontend"]\n'
            '    E["Branch teller, ATM"]\n'
            '  end\n'
            '  subgraph "Ring 3 — Partner APIs"\n'
            '    F["Aggregators<br/>Plaid, MX, Tink, Yodlee"]\n'
            '    G["Embedded finance<br/>Stripe, Razorpay, Marqeta"]\n'
            '    H["Fintech ecosystem<br/>Wise, Revolut, Nubank"]\n'
            '  end\n'
            '  subgraph "Ring 4 — Regulator-mandated open APIs"\n'
            '    I["PSD2 / Open Banking UK"]\n'
            '    J["FDX (US)"]\n'
            '    K["Account Aggregator (India)"]\n'
            '    L["SGFinDex, CDR Australia, Open Finance Brazil"]\n'
            '  end\n'
            '  A --> D\n'
            '  B --> D\n'
            '  C --> D\n'
            '  D --> F\n'
            '  D --> G\n'
            '  D --> H\n'
            '  D --> I\n'
            '  D --> J\n'
            '  D --> K\n'
            '  D --> L',
            "Four concentric rings of a modern bank API estate. Each ring has its "
            "own governance, security model and Service-Level Agreement (SLA).")
    )
    return TopicSection(
        "2.  The picture — four concentric rings of a bank API estate",
        "basic", body)


# ----------------------------------------------------------------- 3. How
def _sec3() -> TopicSection:
    body = (
        H3("3.1  REST — the lingua franca of channel and partner APIs")
        + p("REST is an architectural style on top of HTTP, defined by Roy Fielding "
            "in 2000. ‘RESTful’ APIs use HTTP verbs (<code>GET</code>, "
            "<code>POST</code>, <code>PUT</code>, <code>PATCH</code>, "
            "<code>DELETE</code>) on URLs that name <em>resources</em> "
            "(<code>/accounts/123/transactions</code>), exchange JSON, and use "
            "HTTP status codes (<code>200 OK</code>, <code>201 Created</code>, "
            "<code>404 Not Found</code>, <code>409 Conflict</code>, <code>429 Too "
            "Many Requests</code>, <code>5xx</code> server errors). Almost every "
            "Open Banking, FDX, Account Aggregator, and partner API is REST + "
            "JSON, described in <strong>OpenAPI 3.x</strong> (formerly Swagger).")
        + H3("3.2  gRPC — internal, fast, strongly typed")
        + p("gRPC was open-sourced by Google in 2015. It uses HTTP/2 as the "
            "transport, <strong>Protocol Buffers (protobuf)</strong> as the "
            "schema and binary wire format, and supports unary, server-streaming, "
            "client-streaming and bidirectional-streaming calls. Inside a "
            "microservices estate, gRPC is typically 5–10× faster than REST + "
            "JSON, with stronger typing and code generation in 11+ languages. "
            "Used heavily inside Goldman Sachs (Marquee, Atlas), JPM (Athena "
            "graph), Wise, Nubank, Stripe.")
        + H3("3.3  GraphQL — one endpoint, the client picks the fields")
        + p("GraphQL was open-sourced by Facebook in 2015. The client sends a "
            "query that names exactly the fields it wants, often across multiple "
            "resources at once (<code>customer { name accounts { iban balance } "
            "}</code>). One endpoint, one round-trip, no over-fetching. Strong "
            "fit for mobile and web Backend-for-Frontend (BFF) layers where "
            "screens differ. Used by Standard Chartered (SC Ventures, Mox), "
            "Trust Bank Singapore, parts of HSBC and PayPal. Trade-off: caching "
            "and rate-limiting are harder than with REST.")
        + H3("3.4  SOAP and XML — still everywhere underneath")
        + p("Simple Object Access Protocol (SOAP) over HTTP, with payloads in "
            "Extensible Markup Language (XML) and contracts in Web Services "
            "Description Language (WSDL), was the dominant integration style "
            "from about 2000 to 2012. It is verbose but rigorous: built-in "
            "transactions, security (WS-Security), reliability (WS-"
            "ReliableMessaging). You will still meet SOAP at the boundary of "
            "Temenos T24, Finastra, Oracle FLEXCUBE, FIS, mainframe COBOL "
            "wrappers, regulators (e.g. parts of EBA reporting), payment "
            "schemes, and many capital-markets vendors. Modernisation programmes "
            "usually wrap SOAP behind a REST or gRPC façade.")
        + H3("3.5  Webhooks and event streams — async by design")
        + p("A webhook is an inverted API: <em>you</em> register a URL with a "
            "provider, and the provider <code>POST</code>s an event to it when "
            "something happens. Used by every modern payment processor — Stripe, "
            "Razorpay, Adyen, GoCardless, Worldpay — for ‘payment captured’, "
            "‘charge failed’, ‘dispute opened’ events. Event streams take this "
            "further: a durable, ordered log (Apache Kafka, Amazon Kinesis, "
            "Azure Event Hubs, Google Pub/Sub, IBM MQ Streaming Queues, RabbitMQ "
            "Streams) over which many consumers can replay history. Banks use "
            "event streams for everything from real-time fraud (Standard "
            "Chartered, Wells, JPM) to data-lake ingestion to activity feeds.")
        + H3("3.6  Schemas and contracts — OpenAPI, AsyncAPI, protobuf, Avro")
        + ul([
            "<strong>OpenAPI 3.x</strong> — describes REST endpoints, request / "
            "response schemas, security, examples. The single most important "
            "artefact in modern API estates; tooling generates servers, clients, "
            "mocks, tests, documentation and gateway configurations from it.",
            "<strong>AsyncAPI 3.x</strong> — sister specification for "
            "event-driven and message APIs (Kafka, AMQP, MQTT, WebSocket).",
            "<strong>Protocol Buffers (protobuf)</strong> — schema language and "
            "wire format for gRPC and many event streams.",
            "<strong>Apache Avro</strong> — schema-evolved JSON/binary format, "
            "the default for Kafka in regulated environments because it pairs "
            "with the <strong>Confluent Schema Registry</strong> to enforce "
            "backward / forward compatibility on every produced event.",
            "<strong>JSON Schema</strong> — the schema language inside OpenAPI "
            "and AsyncAPI; also used standalone.",
        ])
        + H3("3.7  Identity, authorisation, and consent on the wire")
        + ul([
            "<strong>OAuth 2.0</strong> — the framework for delegated "
            "authorisation. The customer authorises the third party; the bank "
            "issues an access token; the third party calls the bank with that "
            "token. Defined in RFC 6749 + a family of extensions.",
            "<strong>OpenID Connect (OIDC)</strong> — identity layer on top of "
            "OAuth 2.0; how the customer is authenticated.",
            "<strong>Financial-grade API (FAPI) 1.0 Advanced and FAPI 2.0</strong> "
            "— OpenID Foundation profiles that lock down OAuth 2.0 for banking. "
            "Mutual Transport Layer Security (mTLS), signed requests (JWS), "
            "Pushed Authorisation Requests (PAR), Demonstration of "
            "Proof-of-Possession (DPoP). Mandated by UK Open Banking, Brazil "
            "Open Finance, Australia Consumer Data Right (CDR); strongly "
            "recommended by Berlin Group NextGenPSD2 and FDX.",
            "<strong>Mutual TLS (mTLS)</strong> — both the client and the server "
            "present X.509 certificates. Standard in PSD2, Open Banking UK, FDX. "
            "Certificates are issued by qualified providers (in PSD2: <strong>"
            "QWAC and QSealC</strong> certificates from a Qualified Trust Service "
            "Provider under the EU eIDAS regulation).",
            "<strong>API keys</strong> — fine for internal or low-risk public "
            "APIs; never sufficient on their own for regulated open finance.",
        ])
        + H3("3.8  Rate limits, idempotency, retries — the boring bits that bite")
        + ul([
            "<strong>Idempotency keys</strong> — a unique key the client sends "
            "with a write request so that retries do not double-charge. Stripe "
            "popularised this; every modern payments API now supports it.",
            "<strong>Rate limits</strong> — typically per consumer, per route, "
            "with token-bucket or leaky-bucket algorithms; <code>HTTP 429 Too "
            "Many Requests</code> with <code>Retry-After</code> header.",
            "<strong>Backoff and jitter</strong> — exponential backoff with "
            "randomisation; without jitter, clients synchronise into thundering "
            "herds after an outage.",
            "<strong>Circuit breakers</strong> — when a downstream is failing, "
            "stop calling it for a while. Resilience4j, Polly, Hystrix-pattern.",
            "<strong>Pagination, filtering, sorting</strong> — cursor-based "
            "(<code>?cursor=…</code>) is preferred over page-number for large, "
            "changing datasets like transactions.",
            "<strong>Versioning</strong> — URL-based "
            "(<code>/v1/accounts</code>), media-type (<code>application/"
            "vnd.bank.v1+json</code>), or header (<code>API-Version: 1</code>). "
            "URL-based is most common in BFSI public APIs.",
        ])
    )
    return TopicSection(
        "3.  How APIs actually work — REST, gRPC, GraphQL, SOAP, events",
        "intermediate", body)


# ----------------------------------------------------------------- 4. Region overlay
def _sec4() -> TopicSection:
    body = (
        H3("4.1  United Kingdom — Open Banking, the original")
        + p("Born from the Competition and Markets Authority (CMA) ‘Retail Banking "
            "Market Investigation’ remedies of 2016, Open Banking went live in "
            "January 2018. The CMA9 (Barclays, HSBC, Lloyds, Nationwide, NatWest, "
            "Santander, Bank of Ireland, Allied Irish Banks, Danske) were "
            "obligated to expose standardised APIs. The standards body is the "
            "<strong>Open Banking Implementation Entity (OBIE)</strong>, "
            "transitioning to a long-term entity now called <strong>Open Banking "
            "Limited</strong>, with a future home being designed by the Joint "
            "Regulatory Oversight Committee (JROC) of FCA + PSR + HMT + CMA. "
            "Standards: Account Information Service (AIS), Payment Initiation "
            "Service (PIS), Confirmation of Payee (CoP), Variable Recurring "
            "Payments (VRP) — pioneered for ‘sweeping’ (moving a customer’s own "
            "money), expanding to commercial VRP. Security profile: FAPI 1.0 "
            "Advanced. By volume the UK has the largest production Open Banking "
            "estate in the world — over 11 million active users, 14 billion+ "
            "API calls per year by 2024.")
        + H3("4.2  Eurozone — PSD2 today, PSD3 / Payment Services Regulation tomorrow")
        + p("The Revised Payment Services Directive (PSD2, EU 2015/2366) came "
            "into force in January 2018, with Strong Customer Authentication "
            "(SCA) under the Regulatory Technical Standards (RTS) effective "
            "September 2019 and migrated to mandatory by 31 December 2020. PSD2 "
            "creates two licensed third-party roles: Account Information Service "
            "Provider (AISP) and Payment Initiation Service Provider (PISP). "
            "Three coexisting API standards: <strong>Berlin Group NextGenPSD2</strong> "
            "(by far the most adopted in the EU), <strong>STET</strong> (France), "
            "and the UK Open Banking standard (used by some EU banks).")
        + p("In 2023 the European Commission proposed <strong>PSD3 (Directive)</strong> "
            "and a new <strong>Payment Services Regulation (PSR)</strong>, plus "
            "the <strong>Financial Data Access (FIDA) regulation</strong> "
            "extending open finance from payments to savings, mortgages, "
            "pensions and non-life insurance. Trilogue agreement on PSD3/PSR is "
            "expected in 2025 with application around 2026–2027. PSD3 tightens "
            "API performance requirements, addresses fraud reimbursement, and "
            "deals with PSD2 implementation issues exposed by the European "
            "Banking Authority (EBA) reports of 2022–2024.")
        + p("In parallel, the <strong>EU Instant Payments Regulation</strong> "
            "(adopted 2024) makes SEPA Instant <em>mandatory</em> for "
            "Payment Service Providers in the euro area: receive by 9 January "
            "2025, send by 9 October 2025, with no surcharge over a regular "
            "credit transfer and a Confirmation of Payee–style ‘Verification of "
            "Payee’ service. This is API work for every European bank in 2025.")
        + H3("4.3  India — Account Aggregator + UPI APIs + DPI")
        + p("India runs the most ambitious public-API stack in the world — the "
            "‘India Stack’. Four pillars matter for BFSI:")
        + ul([
            "<strong>UPI APIs</strong> at NPCI — over 16 billion transactions per "
            "month in 2024, peaking at 500+ million per day. UPI 2.0 added "
            "mandates and overdrafts; UPI Lite enables small-value offline-style "
            "payments; UPI Circle (2024) supports delegated payments. UPI is "
            "interoperable with Singapore PayNow (since 2023), UAE AANI, "
            "Bhutan, Mauritius, Sri Lanka and others.",
            "<strong>Account Aggregator (AA) framework</strong> — RBI Master "
            "Direction since September 2021. A licensed AA (e.g. Finvu, OneMoney, "
            "Anumati, NeSL Asset Data, Setu, Yodlee India, Phocket) acts as a "
            "consent-broker between Financial Information Providers (FIPs — your "
            "banks, mutual funds, insurance companies, GST data) and Financial "
            "Information Users (FIUs — lenders, advisers). Customer consent is "
            "machine-readable (the <strong>ReBIT</strong> consent artefact). "
            "Over 100 million consents processed by mid-2024.",
            "<strong>Open Credit Enablement Network (OCEN)</strong> — protocol "
            "for credit; standardises the API contracts between borrowers, Loan "
            "Service Providers (LSPs) and lenders.",
            "<strong>Digital Public Infrastructure (DPI) wider stack</strong> — "
            "Aadhaar e-KYC, e-Sign, DigiLocker, ONDC (Open Network for Digital "
            "Commerce), and the upcoming Unified Lending Interface (ULI) "
            "announced by RBI in 2024 — all are API-first.",
        ])
        + H3("4.4  United States — FDX, the de-facto standard")
        + p("The US has no general open-banking mandate (yet). The de-facto "
            "standard is <strong>Financial Data Exchange (FDX)</strong>, an "
            "industry consortium owned by FS-ISAC; FDX 6.0 was published in "
            "2024. The Consumer Financial Protection Bureau (CFPB) finalised "
            "the <strong>Personal Financial Data Rights rule under §1033 of the "
            "Dodd-Frank Act in October 2024</strong>, with phased compliance "
            "from April 2026 (largest banks) to April 2030 (smallest). The rule "
            "essentially requires API-based, fee-free, secure data sharing and "
            "is closely aligned with FDX. Major aggregators: <strong>Plaid, MX, "
            "Finicity (Mastercard), Yodlee (Envestnet)</strong>; the "
            "screen-scraping era is now ending.")
        + H3("4.5  Singapore — SGFinDex, the consent-led model")
        + p("<strong>SGFinDex</strong>, launched 2020, is run by the Monetary "
            "Authority of Singapore (MAS) with the Smart Nation Group. It "
            "leverages SingPass (national digital identity) for consent, then "
            "calls participating banks’ APIs for retail account information. "
            "Extended to investments and insurance from 2022. Singapore is "
            "remarkable for combining national identity, consent and APIs in a "
            "single citizen-facing flow.")
        + H3("4.6  Brazil, Australia, Hong Kong — and the cross-border picture")
        + ul([
            "<strong>Brazil — Open Finance Brasil</strong>, run by the Banco "
            "Central do Brasil with phased rollout 2021–2023; payments + "
            "investments included from 2022. FAPI 1.0 Advanced, mandatory for "
            "all retail banks.",
            "<strong>Australia — Consumer Data Right (CDR)</strong>, banking "
            "live since 2020; energy and (slowly) other sectors. ACCC + Treasury "
            "as joint regulators, OAIC for privacy. FAPI-based.",
            "<strong>Hong Kong — Open API Framework</strong>, four-phase HKMA "
            "programme, mainly read-only product information and account "
            "information so far.",
            "<strong>Cross-border</strong> — Project Nexus (BIS Innovation Hub) "
            "links instant-payment systems via standardised APIs; pilot with "
            "India UPI, Singapore PayNow, Malaysia DuitNow, Thailand PromptPay, "
            "Philippines InstaPay; live phases through 2025–2027.",
        ])
    )
    return TopicSection(
        "4.  Region by region — the regulator-mandated open-API estate",
        "intermediate", body)


# ----------------------------------------------------------------- 5. Advanced
def _sec5() -> TopicSection:
    body = (
        H3("5.1  ISO 20022 — the message standard the whole world is moving to")
        + p("<strong>ISO 20022</strong> is not a protocol; it is a methodology "
            "and a library of XML (and now JSON) messages for financial services. "
            "Where SWIFT MT was free-text fields with cryptic numeric tags "
            "(MT103 for a customer credit transfer, MT202 for a bank-to-bank "
            "transfer), ISO 20022 messages are richly structured and named "
            "(<code>pacs.008</code> for customer credit transfer, "
            "<code>pacs.009</code> for financial institution transfer, "
            "<code>pain.001</code> for customer payment initiation, "
            "<code>camt.053</code> for bank-to-customer statement, "
            "<code>camt.054</code> for debit/credit notification). Far more "
            "data fits — full remittance information, structured creditor / "
            "debtor identification, purpose codes, regulatory reporting fields.")
        + p("Migration timeline you should know:")
        + ul([
            "<strong>SWIFT cross-border</strong> — co-existence period started "
            "March 2023, ends <strong>22 November 2025</strong>; from then "
            "MT cross-border messages are retired in favour of ISO 20022 "
            "(via SWIFT MX / Cross-Border Payments and Reporting Plus, CBPR+).",
            "<strong>Eurozone</strong> — Target2 / TIPS / EURO1 already on "
            "ISO 20022 (March 2023). SEPA was natively ISO 20022 from launch.",
            "<strong>UK</strong> — CHAPS migrated to ISO 20022 in June 2023 "
            "(Bank of England Renewed Real-Time Gross Settlement programme).",
            "<strong>US</strong> — Fedwire migrated 14 March 2025 to ISO "
            "20022; CHIPS already migrated in April 2024; FedNow was "
            "ISO 20022 from launch (July 2023).",
            "<strong>India</strong> — RTGS migrated to ISO 20022 in 2021; "
            "NEFT and the IFSC-Based payment systems aligning. UPI uses its "
            "own XML schema but with ISO 20022-compatible elements.",
            "<strong>APAC</strong> — Singapore MEPS+, Hong Kong CHATS, Australia "
            "RITS / NPP, Japan Zengin all migrated or migrating.",
        ])
        + H3("5.2  Other vertical message standards you must recognise")
        + ul([
            "<strong>SWIFT MT</strong> — the legacy free-text family. MT103 "
            "(customer credit transfer), MT202 / MT202COV (bank credit transfer "
            "and cover payment), MT940 / MT942 (statement / interim report), "
            "MT700 (letter of credit). Still pervasive inside banks even when "
            "the cross-border wire is MX.",
            "<strong>FIX (Financial Information eXchange) Protocol</strong> — "
            "the standard for equities, FX, listed derivatives and increasingly "
            "fixed income; 4.4 is the workhorse, 5.0SP2 the modern, FIX over "
            "TLS, FIXatdl for algorithmic trading. Used by every major exchange "
            "and broker.",
            "<strong>FpML (Financial products Markup Language)</strong> — XML "
            "for over-the-counter (OTC) derivatives, used heavily for ISDA "
            "documentation, regulatory reporting (SFTR, EMIR, CFTC Part 43/45), "
            "and trade affirmation.",
            "<strong>FHIR (Fast Healthcare Interoperability Resources)</strong> "
            "— not BFSI itself, but referenced because health insurance "
            "platforms use it; Guidewire and Duck Creek integrate to FHIR for "
            "claims.",
            "<strong>ACORD</strong> standards — insurance industry XML / JSON "
            "standards (ACORD AL3, ACORD XML).",
            "<strong>NACHA, Bacs, BSB, SEPA</strong> — country-specific batch "
            "file formats for the local Automated Clearing House / direct "
            "debit and credit rails.",
        ])
        + H3("5.3  API gateways, service meshes, and API management")
        + p("In any large bank, no API is exposed naked. Three layers of "
            "infrastructure mediate every call:")
        + ul([
            "<strong>API gateway</strong> — outermost point. Authentication, "
            "authorisation, rate limiting, schema validation, request "
            "transformation, mTLS termination, audit logging, threat protection "
            "(OWASP API Top 10). Vendors: Apigee (Google), AWS API Gateway, "
            "Azure API Management, Kong, Tyk, MuleSoft Anypoint, IBM API "
            "Connect, Software AG webMethods, Axway, WSO2.",
            "<strong>Service mesh</strong> — innermost layer. Mutual TLS, "
            "retries, circuit breakers, observability between microservices "
            "<em>inside</em> the cluster. Istio, Linkerd, AWS App Mesh, "
            "Consul Connect.",
            "<strong>Developer portal and API catalogue</strong> — the "
            "shop window: documentation, sandboxes, key issuance, usage "
            "dashboards. SwaggerHub, Backstage (Spotify open source, now "
            "the de-facto internal developer platform at many banks), Apigee "
            "Developer Portal, Postman API Network.",
        ])
        + H3("5.4  Event-driven architecture — the outbox, the saga, exactly-once illusion")
        + p("Asynchronous integration is the only sane way to fan out updates "
            "across a microservice estate, but it has its own discipline:")
        + ul([
            "<strong>Outbox pattern</strong> — a service writes its database "
            "change and the event-to-publish in the <em>same database "
            "transaction</em>; a separate process tails the outbox and "
            "publishes to Kafka. Eliminates the dual-write problem.",
            "<strong>Saga pattern</strong> — multi-service business transaction "
            "modelled as a sequence of local transactions and compensating "
            "actions; orchestration (a coordinator service) or choreography "
            "(events trigger the next step). Standard for cross-system payment "
            "and onboarding flows.",
            "<strong>Exactly-once semantics</strong> — strictly speaking, "
            "impossible end-to-end; in practice <em>effectively-once</em> via "
            "idempotent consumers + deduplication keys. Kafka Transactions "
            "give exactly-once <em>within</em> the Kafka boundary.",
            "<strong>Schema evolution</strong> — every event has a schema; the "
            "schema registry enforces backward / forward compatibility so "
            "producers and consumers can roll forward independently.",
        ])
        + H3("5.5  Security — beyond OAuth")
        + ul([
            "<strong>JSON Web Token (JWT) + JSON Web Signature (JWS) / "
            "Encryption (JWE)</strong> — signed (and optionally encrypted) "
            "tokens; the access token in OAuth 2.0 is most often a JWT.",
            "<strong>Pushed Authorisation Requests (PAR)</strong> — the client "
            "sends the authorisation request to a back-channel endpoint first; "
            "no parameters in the browser URL. Required by FAPI 2.0.",
            "<strong>Demonstration of Proof-of-Possession (DPoP)</strong> — "
            "binds an access token to a key the client holds; stolen tokens "
            "without the key are useless.",
            "<strong>Mutual TLS (mTLS)</strong> with eIDAS QWAC / QSealC "
            "certificates for PSD2; with Open Banking Directory certificates "
            "for UK; with FDX-issued certs in the US.",
            "<strong>Threat model</strong> — OWASP API Security Top 10 (2023): "
            "Broken Object Level Authorization (BOLA), Broken Authentication, "
            "Excessive Data Exposure, Lack of Resources & Rate Limiting, Broken "
            "Function Level Authorization, Mass Assignment, Security "
            "Misconfiguration, Injection, Improper Assets Management, "
            "Insufficient Logging & Monitoring. Memorise BOLA — it is the most "
            "common and the most expensive in BFSI.",
        ])
        + H3("5.6  AI agents, Model Context Protocol, and the next API generation")
        + p("In 2024–25, Anthropic open-sourced the <strong>Model Context "
            "Protocol (MCP)</strong>, a standard for exposing tools (read: "
            "APIs) to Large Language Model agents. The OpenAI ‘function "
            "calling’ + ‘assistants’ APIs and Google’s tooling for Gemini are "
            "the same idea via different routes. Banks are already cataloguing "
            "their internal APIs as MCP / function-calling tools to enable "
            "agentic workflows for KYC, fraud investigation, and customer "
            "service. The implication for governance is large: every tool a "
            "model can call needs explicit allow-listing, a clear blast radius, "
            "and observability a regulator will accept.")
    )
    return TopicSection(
        "5.  Advanced — ISO 20022, FIX, gateways, event patterns, agentic APIs",
        "advanced", body)


# ----------------------------------------------------------------- 6. Decision matrix
def _sec6() -> TopicSection:
    body = (
        H3("6.1  Choosing the right API style")
        + table(
            ["Use case", "Best style", "Why"],
            [
                ["Public partner / regulator-mandated API",
                 "REST + JSON + OpenAPI + OAuth 2.0 / FAPI",
                 "Standard, broadly understood, every regulator’s baseline; "
                 "tooling and documentation maturity."],
                ["Internal microservice-to-microservice, high throughput",
                 "gRPC + protobuf",
                 "Binary, HTTP/2, generated clients in 11+ languages, 5–10× "
                 "throughput vs REST/JSON."],
                ["Mobile / web Backend-for-Frontend with many screens",
                 "GraphQL",
                 "Client picks fields, fewer round-trips, screens evolve "
                 "without backend changes."],
                ["Cross-system business event (payment booked, account opened)",
                 "Event on Kafka with Avro schema",
                 "Decouples producers from consumers, enables replay and audit, "
                 "fits saga pattern."],
                ["Third-party processor notifications (Stripe, Razorpay, etc.)",
                 "Webhooks with signed payloads",
                 "Provider pushes; you only need to host an idempotent endpoint."],
                ["Cross-border payment, statements, reporting",
                 "ISO 20022 over SWIFT / market infrastructure",
                 "Mandated; richer data than MT; aligned with global "
                 "modernisation."],
                ["Equities / derivatives trading",
                 "FIX over TLS",
                 "Industry standard; every venue and broker speaks it."],
                ["Bulk inter-bank settlements, regulator returns",
                 "File transfer (SFTP) with strict schema",
                 "Auditable, batch-friendly, regulator-acceptable; not glamorous "
                 "but durable."],
                ["LLM agentic workflow",
                 "Function-calling / MCP wrapper over existing APIs",
                 "Reuses governed APIs; adds tool-allow-listing and audit."],
            ]
        )
        + H3("6.2  Choosing the right gateway / management vendor")
        + table(
            ["Vendor", "Where it shines", "Watch-outs"],
            [
                ["<strong>Apigee (Google)</strong>",
                 "Strong analytics, monetisation, mature developer portal; "
                 "popular at HSBC, Deutsche, ICICI.",
                 "Moving entirely to Apigee X (cloud-native); legacy Apigee "
                 "Edge contracts ending."],
                ["<strong>AWS API Gateway + AWS WAF + Cognito</strong>",
                 "Native fit when the estate is on AWS; cheap at low volumes.",
                 "Less mature developer-portal experience; pair with Backstage "
                 "or third-party for serious portals."],
                ["<strong>Azure API Management</strong>",
                 "Native fit on Azure (Standard Chartered, NatWest, Lloyds); "
                 "good policy expression engine.",
                 "Single-tenant model can be expensive at scale; consumption "
                 "tier limits in production."],
                ["<strong>Kong</strong>",
                 "Open source + enterprise; multi-cloud; strong plugin "
                 "ecosystem; popular at digital banks.",
                 "Self-managed control plane needs operational maturity."],
                ["<strong>MuleSoft Anypoint (Salesforce)</strong>",
                 "Strong inside Salesforce-heavy estates; good legacy adapters.",
                 "Licensing complexity; lock-in if you adopt the runtime "
                 "deeply."],
                ["<strong>IBM API Connect + DataPower</strong>",
                 "Mainframe and existing IBM stack integration; strong in "
                 "regulated EU banks (BNP, MUFG).",
                 "Ageing user experience; many banks migrating away."],
                ["<strong>Tyk, WSO2</strong>",
                 "Open-source-leaning, lower TCO for greenfield API estates.",
                 "Smaller install bases; check skill availability."],
            ]
        )
    )
    return TopicSection(
        "6.  Decision matrices — which style, which vendor, when",
        "intermediate", body)


# ----------------------------------------------------------------- 7. Worked examples
def _sec7() -> TopicSection:
    body = (
        example(
            "A PSD2 Account Information Service call across a German bank",
            ol([
                "A customer of Deutsche Bank uses a budgeting app that is a "
                "licensed AISP under PSD2 in Germany (BaFin-registered).",
                "The app redirects the customer to Deutsche’s authorisation "
                "endpoint with a Pushed Authorisation Request (PAR). The "
                "customer authenticates with Strong Customer Authentication "
                "(SCA) — typically the bank’s mobile app push or a hardware "
                "token.",
                "Deutsche issues an OAuth 2.0 access token bound by mTLS to the "
                "AISP’s eIDAS Qualified Website Authentication Certificate "
                "(QWAC).",
                "The AISP calls <code>GET /v1/accounts</code> on Deutsche’s "
                "Berlin Group NextGenPSD2 endpoint; the bank returns the list of "
                "accounts the customer consented to.",
                "The AISP then calls <code>GET /v1/accounts/{id}/transactions"
                "?dateFrom=…</code>; the bank streams transactions in JSON.",
                "The whole flow is logged on both sides; the EBA Performance and "
                "Availability indicators are reported quarterly.",
                "Under PSD3 / Payment Services Regulation (expected 2026–27), "
                "the response-time and uptime obligations tighten and the "
                "‘fallback interface’ contingency disappears.",
            ])
        )
        + example(
            "An Account Aggregator consent flow in India",
            ol([
                "A customer applies for a loan through an Non-Banking Financial "
                "Company (NBFC) lending app. The app, registered as a "
                "Financial Information User (FIU), redirects to a Reserve Bank "
                "of India–licensed Account Aggregator (e.g. Finvu).",
                "The customer authenticates on the AA, picks accounts (banks, "
                "mutual funds, GST), and digitally signs a machine-readable "
                "consent artefact (purpose, fields, frequency, expiry — all in "
                "the ReBIT consent specification).",
                "The AA stores the consent and issues a consent handle to the "
                "FIU. <em>The AA itself never sees the financial data — it only "
                "brokers consent and routes encrypted payloads.</em>",
                "The FIU asks the AA for the data; the AA forwards the request "
                "to each Financial Information Provider (FIP — the customer’s "
                "banks, mutual fund houses).",
                "Each FIP returns the data encrypted to the FIU’s public key; "
                "the AA simply relays bytes; the FIU decrypts.",
                "The FIU runs underwriting; if approved, sanction letters and "
                "credit decisions are returned in seconds. The whole consented "
                "data flow takes 30–90 seconds and replaces what used to be a "
                "10-day process of asking customers for bank statements.",
            ])
        )
        + example(
            "An ISO 20022 cross-border credit transfer (pacs.008) in the CBPR+ era",
            ol([
                "A customer of HSBC Hong Kong instructs a payment of USD "
                "750,000 to a beneficiary at JPMorgan New York. HSBC builds a "
                "<code>pacs.008</code> message in ISO 20022, including "
                "structured remittance information, Legal Entity Identifier "
                "(LEI) for both parties, and purpose code.",
                "The message goes via SWIFT — but as MX (ISO 20022) under "
                "CBPR+, not legacy MT103 (post 22 November 2025).",
                "Correspondent banks along the chain (e.g. a US "
                "correspondent of HSBC) read the ISO 20022 fields directly; "
                "screening for sanctions and AML uses the structured data, "
                "which improves match precision and reduces false positives.",
                "JPMorgan New York receives the <code>pacs.008</code>, posts "
                "to the beneficiary’s account, and sends a "
                "<code>camt.054</code> credit notification back through the "
                "same rail.",
                "Reconciliation at HSBC matches the original payment to the "
                "<code>camt.054</code> by Unique End-to-End Transaction "
                "Reference (UETR) — a SWIFT GPI invention.",
                "If any of the corridors are still on legacy MT during the "
                "transition, SWIFT’s in-network translation downgrades the "
                "message; banks lose data fidelity at those hops, which is "
                "why the cutover deadline matters.",
            ])
        )
        + example(
            "A FedNow instant payment in the United States",
            ol([
                "A small business in Texas pays USD 4,200 to a supplier in "
                "Ohio at 9 p.m. on a Saturday using their bank’s mobile app. "
                "The originating bank submits a <code>pacs.008</code> over "
                "FedNow.",
                "The Federal Reserve’s FedNow service does an instant net-zero "
                "settlement between the two banks’ Master Accounts, returns a "
                "<code>pacs.002</code> response within seconds.",
                "The receiving bank credits the supplier and sends a "
                "<code>camt.054</code> notification.",
                "If the originator suspects fraud, they can flag the payment "
                "via FedNow’s ‘Request for Return of Funds’ (an ISO 20022 "
                "<code>camt.056</code>) but the funds are already with the "
                "beneficiary; they may or may not be returned.",
                "FedNow’s 24×7×365 model is identical in spirit to UPI, India; "
                "PIX, Brazil; FAST, Singapore; and SEPA Instant, Eurozone. The "
                "differences are in caps, fraud-rules and ISO 20022 fields.",
            ])
        )
    )
    return TopicSection(
        "7.  Worked examples — four real BFSI API journeys",
        "intermediate", body)


# ----------------------------------------------------------------- 8. Questions
def _sec8() -> TopicSection:
    return TopicSection(
        "8.  Questions a leader asks in any API design review", "basic",
        ol([
            "What is the OpenAPI (or AsyncAPI / protobuf) spec, and is it the "
            "<em>source of truth</em> from which servers, clients and gateway "
            "policies are generated?",
            "Which of our APIs are <em>regulator-mandated</em>, and what are "
            "the response-time, availability and uptime obligations? When did "
            "we last miss them?",
            "What is the authentication and authorisation profile (OAuth 2.0, "
            "FAPI 1.0 Advanced, FAPI 2.0, mTLS, eIDAS / Open Banking "
            "certificates), and is it consistent across the estate?",
            "How do we handle idempotency on write APIs? What is the retry, "
            "backoff and circuit-breaker policy for callers?",
            "What is the rate-limit per consumer; do we have noisy-neighbour "
            "protection?",
            "What is our schema-evolution discipline? Is there a schema "
            "registry; do we enforce backward / forward compatibility?",
            "Where is data exposed by the API? Are we leaking more fields than "
            "the use case needs (Excessive Data Exposure / OWASP API #3)?",
            "How do we audit every API call — inputs, outputs, identity, "
            "consent reference — and how long do we keep the logs (regulator "
            "expects 5–7 years for many flows)?",
            "What is our consent model — is it customer-revocable, "
            "machine-readable, expiry-bounded, and is the audit trail "
            "tamper-evident?",
            "How are partner / fintech onboarding, certificate issuance, "
            "secret rotation and kill-switch automated?",
            "What is the dependency map: if this API is down for 30 minutes, "
            "which customer journeys and which regulatory obligations "
            "fail?",
            "Are we ready for ISO 20022 in every relevant rail (SWIFT, local "
            "RTGS, instant-payments)? Have we tested with rich data end to "
            "end?",
        ]))


# ----------------------------------------------------------------- 9. Red flags
def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘We will just expose our internal APIs to partners.’ — Internal "
            "APIs almost always leak fields, lack rate limits, lack consent, "
            "and have authorisation rules tuned for trusted callers. Always "
            "build a separate Ring 3 / Ring 4 façade.",
            "‘REST is old, let’s standardise on GraphQL for everything.’ — "
            "GraphQL is brilliant for BFFs and aggregation; it is poor for "
            "rate-limited, regulator-mandated public APIs. Use the right tool "
            "for the ring.",
            "‘ISO 20022 is just a format change; the data is the same.’ — No. "
            "ISO 20022 carries 5–10× more structured data, and downstream "
            "systems must <em>use</em> that data (sanctions screening, "
            "remittance posting, reconciliation) or you waste the migration.",
            "‘We don’t need a schema registry — events are simple.’ — Without "
            "a registry your producers and consumers will silently drift, "
            "and a Friday-night deploy will discover it on Monday morning.",
            "‘FAPI is overkill for our APIs.’ — If your APIs touch payments "
            "or account information and you are in the UK, EU, Brazil or "
            "Australia, FAPI is mandated. Even where it is not, it is the "
            "correct security baseline.",
            "‘Webhooks don’t need signing because they are HTTPS.’ — Always "
            "sign webhooks (HMAC over body + timestamp). Otherwise an "
            "attacker who learns your endpoint can replay or forge events.",
            "‘Screen-scraping with credentials is fine, the customer "
            "consented.’ — In the UK, EU, Brazil, Australia and (post-§1033) "
            "the United States, screen-scraping is being explicitly phased "
            "out in favour of API-based consent. Build for the regulated "
            "future, not the unregulated past.",
            "‘API gateway will save us — it does authn, authz, rate limit, "
            "everything.’ — A gateway is necessary, not sufficient. The "
            "common breaches in BFSI APIs (BOLA, mass assignment, missing "
            "object-level authorisation) all happen <em>past</em> the "
            "gateway, in the application code.",
            "‘We can swap our API gateway later, it’s just a proxy.’ — In "
            "practice, gateway-specific policies (transformations, JWT "
            "validators, rate-limit definitions) accumulate and become a "
            "lock-in surface. Plan for portability; keep policies in "
            "spec-driven config.",
            "‘Open Banking has not delivered the volumes we hoped.’ — In the "
            "UK, volumes are now meaningful (14B+ calls/year) and Variable "
            "Recurring Payments are reframing direct-debit. In India, AA + "
            "UPI are at unprecedented scale. Don’t under-invest because "
            "early-stage take-up was slow.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("API", "Application Programming Interface — a contract between "
                "two pieces of software."),
            ("REST", "Representational State Transfer — resource-oriented "
                "architectural style on HTTP; the lingua franca of public "
                "BFSI APIs."),
            ("gRPC", "Google Remote Procedure Call — binary, HTTP/2-based, "
                "schema-first RPC framework using Protocol Buffers."),
            ("GraphQL", "Query language for APIs; one endpoint, client picks "
                "fields. Strong fit for Backend-for-Frontend."),
            ("SOAP / WSDL", "Simple Object Access Protocol over XML, with "
                "Web Services Description Language. Legacy-but-everywhere."),
            ("OpenAPI / AsyncAPI", "Specifications for describing REST and "
                "event APIs respectively; the source of truth for tooling."),
            ("Avro / protobuf", "Binary schema languages and wire formats; "
                "used with Kafka and gRPC."),
            ("OAuth 2.0 / OIDC", "Delegated authorisation framework / "
                "identity layer on top of it."),
            ("FAPI", "Financial-grade API — OpenID Foundation security "
                "profile (1.0 Advanced, 2.0) for banking-grade OAuth 2.0."),
            ("mTLS", "Mutual Transport Layer Security — both ends present "
                "X.509 certificates."),
            ("eIDAS QWAC / QSealC", "Qualified Website Authentication "
                "Certificate / Qualified electronic Seal Certificate, "
                "issued under EU eIDAS for PSD2."),
            ("PSD2 / PSD3 / PSR / FIDA", "EU payment services directives and "
                "regulation; FIDA extends open finance beyond payments."),
            ("AISP / PISP", "Account Information Service Provider / Payment "
                "Initiation Service Provider — PSD2 licensed roles."),
            ("Open Banking UK", "CMA-mandated UK API regime live since "
                "January 2018; managed by Open Banking Limited."),
            ("FDX", "Financial Data Exchange — US industry consortium; "
                "FDX 6.0 (2024); aligned with the CFPB §1033 rule."),
            ("CFPB §1033", "US Personal Financial Data Rights rule, "
                "finalised October 2024; phased compliance from April 2026."),
            ("Account Aggregator", "RBI-licensed consent broker between "
                "Financial Information Providers and Users in India."),
            ("OCEN", "Open Credit Enablement Network — protocol for credit "
                "marketplaces in India."),
            ("ULI", "Unified Lending Interface — RBI initiative announced "
                "2024 to do for credit what UPI did for payments."),
            ("SGFinDex", "Singapore Financial Data Exchange — MAS + Smart "
                "Nation Group; uses SingPass for consent."),
            ("CDR", "Consumer Data Right — Australia’s open-banking-and-"
                "beyond regime."),
            ("Open Finance Brasil", "BCB-mandated open finance; FAPI-based; "
                "live since 2021."),
            ("ISO 20022", "Global standard for structured financial messages "
                "(<code>pacs</code>, <code>pain</code>, <code>camt</code>, "
                "<code>acmt</code>, etc.)."),
            ("CBPR+", "Cross-Border Payments and Reporting Plus — SWIFT’s "
                "ISO 20022 cross-border programme; cutover 22 November 2025."),
            ("Berlin Group NextGenPSD2", "The most-adopted PSD2 API standard "
                "in the EU."),
            ("STET", "French PSD2 API standard."),
            ("FIX", "Financial Information eXchange protocol — equities, FX, "
                "derivatives messaging."),
            ("FpML", "Financial products Markup Language — XML for OTC "
                "derivatives and ISDA workflows."),
            ("UETR", "Unique End-to-End Transaction Reference — SWIFT GPI "
                "tracking identifier for cross-border payments."),
            ("Outbox / Saga", "Patterns for reliable event publication and "
                "multi-service business transactions."),
            ("BOLA", "Broken Object Level Authorization — OWASP API Top 10 "
                "#1; the most common BFSI API vulnerability."),
            ("MCP", "Model Context Protocol — open standard from Anthropic "
                "for exposing tools (APIs) to LLM agents."),
            ("BaaS", "Banking-as-a-Service — distributing licensed banking "
                "capabilities to non-bank brands via APIs."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
