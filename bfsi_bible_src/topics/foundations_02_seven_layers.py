"""Foundations · 02 — The seven-layer mental model of any digital bank."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="I.2",
        slug="02-seven-layers",
        title="The seven-layer mental model of any digital bank",
        one_liner=("Every bank in the world — Citi, JPM, Standard Chartered, Barclays, HDFC, "
                   "DBS — runs on the same seven layers, in the same order. Once you can name "
                   "those seven layers and what lives on each, you can place any product, any "
                   "vendor, any new buzzword, and any regulatory rule onto the right shelf in "
                   "under ten seconds. That is the single most useful map in BFSI tech."),
        sections=[
            _sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
            _sec5(), _sec6(), _sec7(), _sec8(), _sec9(),
        ],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("In Topic I.1 we walked through what happens when one transaction moves through a "
              "bank. In this topic we zoom out: regardless of <em>which</em> transaction you are "
              "looking at — a card swipe, a salary payment, a loan disbursal, a mutual-fund SIP — "
              "the bank is built as the same stack of seven layers. Memorising those seven labels "
              "is the single highest-leverage thing you can do in your first month.")
        )
        + H3("0.1  IT-side anchor — your laptop is also a seven-layer stack")
        + it_anchor(
            p("Your laptop already has the same shape, just smaller. Compare:")
            + ul([
                "<strong>Hardware</strong> — chassis, screen, keyboard, charger.",
                "<strong>OS (Operating System)</strong> — Windows / macOS / Linux that controls "
                "the hardware.",
                "<strong>Filesystem and apps installed</strong> — Word, Excel, browser, the data "
                "saved on disk.",
                "<strong>The app you are using right now</strong> — Word, with a document open.",
                "<strong>The way you interact</strong> — keyboard, mouse, voice assistant.",
                "<strong>Security around it</strong> — login password, antivirus, full-disk "
                "encryption (BitLocker, FileVault).",
                "<strong>Rules outside it</strong> — your employer’s policy, the country’s laws.",
            ])
            + p("A bank has exactly the same seven shelves; the boxes on each shelf are larger, "
               "but the shelves are the same.")
        )
        + H3("0.2  BFSI-side anchor — the journey of one banking app tap")
        + bfsi_anchor(
            p("Tap to send ₹500 on Google Pay (GPay). Watch where each piece of work happens:")
            + ol([
                "Your finger hits the screen — that is the <strong>Channel</strong> layer "
                "(GPay app).",
                "GPay packages the request and calls the bank — that is the <strong>API / "
                "Integration</strong> layer (UPI APIs).",
                "Inside the bank, software computes balance, applies limits, posts a debit "
                "— that is the <strong>Application</strong> layer (the core banking system).",
                "The new balance is written to a database — that is the <strong>Data</strong> "
                "layer (the ledger).",
                "All of this software runs on servers in a data centre or a cloud region — "
                "that is the <strong>Infrastructure</strong> layer.",
                "Every step is encrypted, identity-checked, fraud-scored — that is the "
                "<strong>Security</strong> layer.",
                "And the rules that say what limits apply, where data can be stored, how long "
                "logs must be kept — that is the <strong>Governance / Compliance</strong> layer.",
            ])
        )
    )
    return TopicSection("0.  Primer — anchored to things you already know", "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Why bother with a layer model at all? Because complexity in any large bank — 20–60 "
          "million customers, 5,000+ applications, multiple time zones, dozens of regulators — "
          "is unmanageable unless you have a shared mental shelf. Without it every conversation "
          "becomes free-association: 'we need observability — wait, do you mean fraud monitoring "
          "or infra alerting?'. With it, you say 'observability lives on Layer 5 (Infra), fraud "
          "monitoring on Layer 3 (App)' and the room moves on.")
        + callout("The leader’s test",
            p("If a teammate uses any new word — <em>tokenisation</em>, <em>service mesh</em>, "
              "<em>DPDP</em>, <em>Volante</em>, <em>Kafka</em>, <em>FedNow</em>, <em>Splunk</em>, "
              "<em>SBOM</em> — you should be able to name which of the seven layers it lives on "
              "before the next sentence. If you can’t, ask. After two weeks of practice you will."),
            "info")
    )
    return TopicSection("1.  Why a layer model at all", "basic", body)


def _sec2() -> TopicSection:
    body = (
        p("Read top to bottom. Each layer rests on the ones below; each layer is constrained by "
          "the regulations sitting alongside.")
        + mermaid(
            'flowchart TB\n'
            '  L1["1 · Channel & Experience<br/>mobile, web, branch, ATM, IVR, partner apps"]\n'
            '  L2["2 · API & Integration<br/>REST, gRPC, ISO 20022, file gateways, messaging"]\n'
            '  L3["3 · Application & Domain<br/>core banking, lending, payments, wealth, claims"]\n'
            '  L4["4 · Data<br/>OLTP ledgers, OLAP warehouses, data lakes, AI features"]\n'
            '  L5["5 · Infrastructure & Platform<br/>cloud, on-prem, containers, observability"]\n'
            '  L6["6 · Security & Identity<br/>IAM, crypto, HSMs, fraud, sanctions, AML"]\n'
            '  L7["7 · Governance, Risk & Compliance<br/>regulators, audit, BCP-DR, model risk"]\n'
            '  L1 --> L2 --> L3 --> L4 --> L5\n'
            '  L6 -.cuts across.-> L1\n'
            '  L6 -.cuts across.-> L5\n'
            '  L7 -.cuts across.-> L1\n'
            '  L7 -.cuts across.-> L5',
            "The seven-layer mental model. Layers 6 and 7 are cross-cutting concerns.")
    )
    return TopicSection("2.  The model in one picture", "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("Layer 1 — Channel & Experience")
        + p("Where the human or the partner system actually touches the bank. Mobile apps "
            "(SBI YONO, HDFC MobileBanking, Citi Mobile, Chase, Barclays, Lloyds, DBS digibank), "
            "internet banking, branch teller terminals, ATMs / CDMs, IVR (Interactive Voice "
            "Response) call centres, RM (Relationship Manager) tablets, partner apps (PhonePe, "
            "GPay), wearables. Tech: Android / iOS / Flutter / React Native / Swift / Kotlin "
            "for mobile; React / Angular / Vue for web; Genesys / Avaya / Amazon Connect for "
            "IVR; ATM software stacks like NCR, Diebold Nixdorf, FIS Vynamic.")
        + H3("Layer 2 — API & Integration")
        + p("How the channel talks to the rest of the bank, and how the bank talks to other "
            "banks. Internal: REST / gRPC, GraphQL for some; ESB (Enterprise Service Bus) like "
            "MuleSoft, IBM Integration Bus, Tibco; iPaaS like Boomi, Workato, Azure Logic Apps. "
            "External: ISO 20022 over SWIFT, ISO 8583 for cards, NPCI common library for UPI, "
            "PSD2 / Open Banking APIs in the UK and EU, Account Aggregator framework in India, "
            "FDX (Financial Data Exchange) in the US. Async messaging: Apache Kafka, IBM MQ, "
            "RabbitMQ, AWS SQS / SNS, Azure Service Bus, Google Pub/Sub, Solace.")
        + H3("Layer 3 — Application & Domain")
        + p("Where the actual business logic lives. By function:")
        + ul([
            "<strong>Core banking system (CBS)</strong> — Finacle (Infosys), Flexcube (Oracle), "
            "TCS BaNCS, Temenos T24/Transact, FIS Profile / Modern Banking Platform, Mambu (cloud "
            "native), Thought Machine Vault Core, 10x Banking. Holds account masters, balances, "
            "interest accrual, deposits, GL postings.",
            "<strong>Loan origination & servicing</strong> — Newgen, Nucleus FinnOne, Pega, "
            "ICE Encompass, Black Knight Empower (US mortgage).",
            "<strong>Payments hub & rails</strong> — Volante VolPay, ACI Worldwide, Form3, FIS "
            "OPF, Finastra GPP, Bottomline, Montran. Card switches: Euronet, BPC SmartVista, "
            "FIS IST/Switch, ACI BASE24.",
            "<strong>Capital markets & wealth</strong> — Murex, Calypso (Adenza), Misys / "
            "Finastra Kondor+, Charles River, BlackRock Aladdin, Avaloq, Temenos WealthSuite.",
            "<strong>Insurance</strong> — Guidewire (P&amp;C), Duck Creek, Sapiens, FINEOS, "
            "EXLerator, LIC’s in-house Jeevan-Anant in India.",
            "<strong>Fraud, AML, KYC</strong> — SAS AML, NICE Actimize, FICO Falcon, Oracle FCC, "
            "Featurespace, Refinitiv World-Check, LexisNexis Bridger.",
            "<strong>CRM and customer data</strong> — Salesforce Financial Services Cloud, "
            "Microsoft Dynamics, Pega, Adobe Experience Platform.",
        ])
        + H3("Layer 4 — Data")
        + p("Where the truth lives. Three kinds of data, three kinds of system.")
        + ul([
            "<strong>OLTP (Online Transaction Processing)</strong> — for live transactional "
            "writes. Oracle Exadata, IBM Db2 (mainframe and LUW), SQL Server, PostgreSQL "
            "(rising fast), CockroachDB / YugabyteDB / Spanner for distributed ACID.",
            "<strong>OLAP / warehouse / lakehouse</strong> — for analytics and regulatory "
            "reporting. Snowflake, Databricks, Google BigQuery, Microsoft Fabric, Amazon "
            "Redshift, Teradata. Open table formats: Apache Iceberg, Delta Lake, Apache Hudi.",
            "<strong>Streaming and operational data</strong> — Apache Kafka, Confluent, Apache "
            "Flink, Apache Pulsar; in-memory grids like Hazelcast, Redis, GridGain for hot "
            "balances and risk views.",
            "<strong>AI / ML</strong> — feature stores (Tecton, Feast), model platforms "
            "(Databricks ML, SageMaker, Vertex AI, Azure ML), governance (Collibra, Alation), "
            "and increasingly LLM platforms (OpenAI, Azure OpenAI, AWS Bedrock, Anthropic) for "
            "customer service and document understanding.",
        ])
        + H3("Layer 5 — Infrastructure & Platform")
        + p("Where the software actually runs. Cloud: AWS, Microsoft Azure, Google Cloud "
            "Platform (GCP), Oracle Cloud Infrastructure (OCI), IBM Cloud — banks are usually "
            "multi-cloud with a primary plus a secondary for resilience and bargaining power. "
            "On-prem: VMware (now Broadcom), Red Hat OpenShift, IBM Z mainframe (still very "
            "much alive at JPM, Wells, Citi, BoA, BoB). Containers and orchestration: "
            "Kubernetes (K8s), Docker, Helm, Argo CD, Crossplane. Service mesh: Istio, Linkerd. "
            "Observability: Splunk, Datadog, Dynatrace, New Relic, Prometheus + Grafana + Loki, "
            "OpenTelemetry as the open standard.")
        + H3("Layer 6 — Security & Identity (cross-cutting)")
        + p("Touches every layer above. IAM (Identity & Access Management): Microsoft Entra ID "
            "(formerly Azure AD), Okta, Ping Identity, ForgeRock, SailPoint for governance, "
            "CyberArk and BeyondTrust for privileged access. Cryptography: TLS 1.3, AES-256, "
            "RSA-4096 / ECC, post-quantum (NIST ML-KEM / ML-DSA / SLH-DSA finalised 2024); HSMs "
            "from Thales, Entrust, Utimaco, AWS CloudHSM, Azure Dedicated HSM. AppSec: SAST "
            "(Checkmarx, Veracode, Fortify, Snyk Code), DAST, SBOM (Software Bill of Materials), "
            "container scanning (Snyk, Aqua, Prisma Cloud, Wiz). Fraud / sanctions / AML overlap "
            "with Layer 3 but are conceptually security.")
        + H3("Layer 7 — Governance, Risk & Compliance (cross-cutting)")
        + p("The rules and the people enforcing them. Regulators (RBI, SEBI, IRDAI, Fed, OCC, "
            "FCA, PRA, ECB, EBA, ESMA, MAS, FINMA, ASIC, APRA). Internal: enterprise risk, "
            "operational risk, model risk, compliance, internal audit. Tooling: GRC platforms "
            "(MetricStream, ServiceNow GRC, OneTrust, Archer), model-risk platforms "
            "(SR 11-7 in the US, RBI Master Direction on Model Risk), regulatory reporting "
            "(AxiomSL, Wolters Kluwer OneSumX, Vermeg COLLINE / AGILE).")
    )
    return TopicSection("3.  Each layer in detail — what it is, what runs on it",
                        "intermediate", body)


def _sec4() -> TopicSection:
    return TopicSection(
        "4.  Where common buzzwords land — the placement table",
        "basic",
        table(
            ["Word you’ll hear", "Layer", "What it actually is"],
            [
                ["UPI", "2 (Integration) + 3 (App)",
                 "Payment rail (NPCI). API contract on L2, switch logic on L3."],
                ["Kafka", "2 (async messaging) and 4 (streaming data)",
                 "Distributed event log. Used both for inter-service messaging and as the spine "
                 "of streaming analytics."],
                ["Microservices", "3 (App) and 5 (Platform)",
                 "An application style where the app is many small services; runs on Kubernetes "
                 "(L5)."],
                ["Snowflake / Databricks", "4 (Data)",
                 "Cloud data warehouse / lakehouse for analytics and regulatory reporting."],
                ["Kubernetes", "5 (Platform)",
                 "Container orchestrator. Where the apps run."],
                ["DORA / RBI Outsourcing MD", "7 (GRC)",
                 "Regulations that constrain how Layers 5 and 6 must be operated."],
                ["DPDP / GDPR", "7 with effects on 4 and 6",
                 "Data-protection law. Drives encryption, masking, retention on L4 and L6."],
                ["Tokenisation (RBI CoFT)", "6 (Security) with effects on 3 and 4",
                 "Replaces PAN with a merchant-specific token; impacts card flows on L3 and "
                 "stored data on L4."],
                ["Service mesh / Istio", "5 (Platform) with effects on 6",
                 "Provides mTLS, observability and traffic policy between microservices."],
                ["LLM / Generative AI", "4 (Data, including model platform) with surfaces in 1",
                 "Models live on L4; chat surfaces appear on L1; risk controls on L7."],
                ["FedNow / RTP / SEPA Inst", "2 (rail integration) and 3 (payments engine)",
                 "Instant-payment rails."],
                ["Volante / Form3 / ACI", "3 (App)", "Payments-engine vendors."],
                ["Splunk / Datadog / Dynatrace", "5 (Platform — observability)",
                 "Logs / metrics / traces / APM."],
                ["Okta / Microsoft Entra ID", "6 (Security — IAM)",
                 "Identity provider for workforce and customer."],
                ["Salesforce FSC", "3 (App — CRM)",
                 "Customer relationship and case management."],
                ["Mainframe (IBM Z, COBOL)", "3 + 5",
                 "Old core-banking workloads still running at JPM, Wells, BoA, Citi, BoB."],
                ["SBOM", "5 with reporting to 7",
                 "Software Bill of Materials — list of every open-source component, required "
                 "by US Executive Order 14028 and EU Cyber Resilience Act."],
                ["Confidential computing", "5 (Platform) with effects on 6",
                 "TEEs (Trusted Execution Environments) like Intel SGX, AMD SEV-SNP, AWS Nitro "
                 "Enclaves — protect data in use."],
            ]
        ),
    )


def _sec5() -> TopicSection:
    body = (
        p("Senior architects spend their time on three sub-questions inside this seven-layer "
          "model. Knowing the questions is more useful than knowing today’s buzzword answer.")
        + H3("5.1  Where do we cut, and at which boundary do we govern?")
        + p("Boundaries are where contracts (APIs, schemas, SLAs) live. The most common cut for "
            "a modern bank: <em>customer experience platform</em> on L1+L2 (often cloud), "
            "<em>product platforms</em> on L3 (often hybrid — older cores stay on-prem, newer "
            "ones move to cloud), <em>analytics / regulatory reporting</em> on L4 (cloud "
            "lakehouse), <em>operations</em> on L5 (Kubernetes-based platform engineering team).")
        + H3("5.2  How do we keep Layers 6 and 7 from degenerating into a bottleneck?")
        + p("The classic anti-pattern is a security or risk team that has no automation and "
            "becomes a slow approver of every release. The modern answer is <em>policy as "
            "code</em> (Open Policy Agent / Rego, AWS Service Control Policies, Azure Policy), "
            "<em>guardrails over gates</em> (let teams move fast inside guardrails, escalate "
            "only on violations), and <em>shift-left</em> (SAST, SBOM, IaC scanning in the CI "
            "pipeline). HCLTech’s engagements with Citi and Standard Chartered have all moved "
            "to this model.")
        + H3("5.3  Where does AI live, and what governance does it need?")
        + p("AI models conceptually sit on L4 (data + model platform) but their <em>outputs</em> "
            "land on L1 (assistants, copilots, voice IVR) and L3 (credit decisions, fraud "
            "scores, claims triage). They also create new L7 obligations: model risk management "
            "(Fed SR 11-7 since 2011, RBI’s draft Framework for AI/ML in 2024), the EU AI Act "
            "(in force from Aug 2024 with phased applicability through Aug 2026), Singapore "
            "MAS FEAT principles (Fairness, Ethics, Accountability, Transparency), and the "
            "NIST AI RMF (Risk Management Framework, US, Jan 2023). Generative AI sub-rules "
            "are being added quickly — track them as a moving regulatory front.")
    )
    return TopicSection("5.  Advanced — three questions a senior architect actually argues about",
                        "advanced", body)


def _sec6() -> TopicSection:
    body = (
        p("Each layer has its principal regulator concerns in each region. This matrix is "
          "useful when you join a new client and need to know whose rule constrains which "
          "shelf.")
        + table(
            ["Layer", "India", "United States", "United Kingdom", "Eurozone", "Singapore"],
            [
                ["1 — Channel",
                 "RBI Digital Banking, IT Governance MD",
                 "Reg E, CFPB UDAAP",
                 "FCA Consumer Duty (Jul 2023)",
                 "PSD2 / PSD3, EAA accessibility",
                 "MAS Notice 655"],
                ["2 — Integration / APIs",
                 "Account Aggregator framework, NPCI tech specs",
                 "FDX, NACHA rules",
                 "Open Banking standard (OBL)",
                 "PSD2 / PSD3 APIs, Berlin Group",
                 "MAS API governance, SGFinDex"],
                ["3 — Application",
                 "Master Directions on each product (KYC, Credit Card, Digital Lending 2022)",
                 "OCC heightened standards, SR 11-7 model risk",
                 "PRA SS1/23 model risk, FCA SYSC",
                 "EBA guidelines, MiFID II for trading",
                 "MAS Notice 626 AML, MAS Securities & Futures Act"],
                ["4 — Data",
                 "DPDP Act 2023, RBI Storage of Payment Data Apr 2018",
                 "GLBA, state laws (CCPA / CPRA, Virginia, Colorado)",
                 "UK GDPR, ICO codes",
                 "EU GDPR, EU Data Act 2024",
                 "PDPA"],
                ["5 — Infra",
                 "RBI Outsourcing of IT Services Apr 2023, MeitY rules",
                 "OCC Bulletin 2023-17 on TPRM, FFIEC IT Handbook",
                 "PRA SS2/21",
                 "EU DORA Jan 2025, NIS2",
                 "MAS Outsourcing Guidelines, MAS Notice 658 BCM"],
                ["6 — Security",
                 "RBI Cybersecurity Framework, SEBI CSCRF 2024",
                 "NIST CSF 2.0 (Feb 2024), NYDFS Part 500",
                 "PRA SS1/21",
                 "DORA, NIS2, EU Cyber Resilience Act 2024",
                 "MAS TRM, MAS Notice 655"],
                ["7 — GRC",
                 "RBI / SEBI / IRDAI master directions, board-level governance",
                 "OCC, Fed, FDIC, CFPB; SOX for listed entities",
                 "BoE, PRA, FCA, SMCR for senior managers",
                 "ECB SSM, EBA, ESMA, EIOPA",
                 "MAS as integrated regulator, Senior Manager regime"],
            ]
        )
    )
    return TopicSection("6.  Regulatory overlay by layer", "advanced", body)


def _sec7() -> TopicSection:
    return TopicSection(
        "7.  Trade-offs leaders own at each layer", "intermediate",
        table(
            ["Layer", "Recurring trade-off", "Recommended default"],
            [
                ["1 — Channel",
                 "Native app vs cross-platform (Flutter, React Native)",
                 "Native for the flagship app where every millisecond matters; cross-platform "
                 "for partner / SME apps."],
                ["2 — Integration",
                 "ESB / iPaaS vs lightweight microservices + Kafka",
                 "For greenfield: skip the heavy ESB; use REST + Kafka + a thin API gateway. "
                 "Keep ESB for legacy integration only."],
                ["3 — Application",
                 "Buy a vendor core vs build composable",
                 "Buy for commodity (KYC, AML, payments rail). Build / compose for differentiating "
                 "experience (lending journeys, customer 360)."],
                ["4 — Data",
                 "Single warehouse vs lakehouse vs data mesh",
                 "Lakehouse on open table format (Iceberg / Delta) for centralised; mesh only "
                 "if the bank truly has > 5 data domains with strong domain teams."],
                ["5 — Infra",
                 "Single cloud vs multi-cloud",
                 "Primary on one hyperscaler, secondary on another for the most critical "
                 "workloads to satisfy DORA / RBI concentration risk. Avoid shallow multi-cloud."],
                ["6 — Security",
                 "Best-of-breed point tools vs single platform (Microsoft, Palo Alto, Wiz)",
                 "Single platform for SOC and posture; best-of-breed only where there is a "
                 "clear capability gap."],
                ["7 — GRC",
                 "Spreadsheet-based controls vs GRC platform",
                 "Move to a GRC platform (ServiceNow GRC, MetricStream, Archer) the moment you "
                 "have > 50 distinct controls; otherwise it becomes unauditable."],
            ]
        )
    )


def _sec8() -> TopicSection:
    body = (
        example("Place every word in this sentence onto a layer",
            p("‘We need to migrate the UPI switch off the on-prem ESB onto Kafka, expose it via "
              "an API gateway with mTLS and OAuth2, post events to Snowflake for the regulator "
              "report, and run the whole thing on Kubernetes in OCI Mumbai region.’")
            + ul([
                "<strong>UPI switch</strong> → Layer 3 (App). Operated by NPCI; bank integrates.",
                "<strong>On-prem ESB</strong> → Layer 2 (Integration) and Layer 5 (Infra).",
                "<strong>Kafka</strong> → Layer 2 (async messaging) and Layer 4 (streaming).",
                "<strong>API gateway, mTLS, OAuth2</strong> → Layer 2 + Layer 6.",
                "<strong>Snowflake</strong> → Layer 4 (data warehouse).",
                "<strong>Regulator report</strong> → Layer 7 (GRC) — drives the requirement.",
                "<strong>Kubernetes</strong> → Layer 5 (Platform).",
                "<strong>OCI Mumbai region</strong> → Layer 5 (Infra) + Layer 7 (data "
                "localisation requirement under RBI April 2018).",
            ])
        )
        + example("Reading a regulator circular through the layers",
            p("RBI’s Digital Lending Guidelines (September 2022, latest amendment 2024) hits "
              "<em>at least</em> these layers: L1 (in-app disclosures, key fact statement, "
              "cooling-off), L3 (LSP / LSP-Bank governance, FLDG arrangements), L4 (data only "
              "with consent, no contact list scraping), L6 (encryption, India-only storage), "
              "L7 (board policy, customer grievance redress).") )
    )
    return TopicSection("8.  Worked examples — placing real sentences onto the model",
                        "intermediate", body)


def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘That’s an infra problem, not ours.’ — In a regulated bank, infra problems become "
            "compliance problems within days. Treat L5 incidents as L7 issues by default.",
            "‘We use Kafka, so we’re event-driven.’ — Owning Kafka is not the same as designing "
            "events. Without contracts and the outbox pattern (see I.1 §5.6) you have a faster "
            "way to lose money.",
            "‘We’re cloud-native because we run on Kubernetes.’ — Kubernetes is L5 only. "
            "Cloud-native means rethinking L3 and L4 too.",
            "‘Security signs off at the end.’ — DORA, RBI, MAS, OCC all require security "
            "embedded from design. End-of-cycle sign-off is a finding waiting to be written.",
            "‘AI models don’t need governance, they’re just tools.’ — Fed SR 11-7 and RBI’s "
            "draft framework explicitly say otherwise; the EU AI Act adds civil liability.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("Layer", "One of the seven shelves used to place every component of a bank."),
            ("Cross-cutting concern", "A concern (security, GRC) that touches every other "
             "layer rather than living on one."),
            ("ESB", "Enterprise Service Bus — a centralised middleware integration pattern; "
             "being replaced by API + event-driven approaches."),
            ("iPaaS", "Integration Platform as a Service — cloud-hosted integration (Boomi, "
             "Workato, MuleSoft Anypoint, Azure Logic Apps)."),
            ("CBS", "Core Banking System — the central ledger and product engine of a bank."),
            ("OLTP / OLAP", "Online Transaction Processing (write-heavy) / Online Analytical "
             "Processing (read-heavy analytics)."),
            ("Lakehouse", "Architecture combining data-lake storage (cheap, open formats) with "
             "warehouse-like SQL performance and ACID; e.g. Databricks, Snowflake, Microsoft "
             "Fabric."),
            ("Service mesh", "Sidecar-based platform that gives microservices mTLS, retries, "
             "traffic shaping, observability without code changes (Istio, Linkerd)."),
            ("SBOM", "Software Bill of Materials — machine-readable inventory of all components "
             "in a piece of software; mandatory under US EO 14028 and EU CRA."),
            ("Confidential computing", "Hardware-enforced protection for data while in use "
             "(Intel SGX, AMD SEV-SNP, AWS Nitro Enclaves)."),
            ("Policy as code", "Codifying compliance rules as Rego / Cedar / OPA so they are "
             "machine-evaluable in CI and at runtime."),
            ("EU AI Act", "EU regulation in force Aug 2024, phased applicability through Aug "
             "2026; risk-tiered obligations on AI providers and deployers."),
            ("NIST AI RMF", "Voluntary US framework for managing AI risk (Jan 2023)."),
            ("MAS FEAT", "Singapore Monetary Authority’s Fairness, Ethics, Accountability, "
             "Transparency principles for AI in financial services."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
