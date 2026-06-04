"""Application Stack · 02 — Microservices, monoliths, and Domain-Driven Design."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="II.2",
        slug="02-microservices-monoliths-ddd",
        title="Microservices, monoliths, and Domain-Driven Design",
        one_liner=(
            "Every BFSI ‘modernisation’ programme of the last decade has been an "
            "argument about size and shape: how big should an application be, who "
            "owns it, where do its boundaries fall, and what happens when many of "
            "them must coordinate to make a single payment land? This topic gives "
            "you the vocabulary — monolith, modular monolith, microservice, "
            "Bounded Context, aggregate, saga, outbox, idempotency, strangler "
            "fig — and the judgement to know which shape wins for which "
            "workload."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


# ----------------------------------------------------------------- 0. Primer
def _sec0() -> TopicSection:
    body = (
        primer(
            p("‘Microservices’ has been the fashion word of BFSI engineering for "
              "ten years. It is neither magic nor mandatory. It is one shape of "
              "system among several, with concrete costs and benefits. <strong>"
              "Domain-Driven Design (DDD)</strong> is the discipline that tells "
              "you <em>where</em> to draw the lines between services in the "
              "first place. Get DDD right and the microservices argument mostly "
              "answers itself; get it wrong and you build a distributed "
              "monolith that combines the worst of both worlds.")
        )
        + H3("0.1  IT-side anchor — your phone vs your laptop")
        + it_anchor(
            p("Think of two ways to read a book. <strong>A single big book</strong> "
              "on your bedside table — you carry the whole thing, you skim "
              "easily between chapters, but if you spill coffee on it the "
              "whole book is gone. That is a <em>monolith</em>: one binary, "
              "one database, one deploy. <strong>A bookshelf of paperbacks</strong> "
              "— you pull one volume out, leave the rest untouched; coffee on "
              "Volume 4 doesn’t hurt Volumes 1–3; but you have to remember "
              "which volume covers what, and walking from volume to volume "
              "takes effort. That is <em>microservices</em>: many small "
              "binaries, each with its own data, talking over the network. "
              "Both are correct architectures; which one wins depends on the "
              "book.")
        )
        + H3("0.2  BFSI-side anchor — branches you already use")
        + bfsi_anchor(
            p("Think of your bank branch network. A single ‘universal teller’ "
              "who handles loans, deposits, FX, cards, demat and insurance is "
              "the <em>monolith</em>: simple to deploy, awkward to scale, and "
              "if she calls in sick everything stops. A modern branch has "
              "<em>specialised counters</em>: cash, account opening, loans, "
              "wealth, FX. Each counter has its own ledger book, its own "
              "expert, its own queue. Customers route themselves to the "
              "right counter; the counters coordinate through the branch "
              "manager (the orchestrator) or through a token / form passed "
              "between them (events). That is a <em>microservices</em> bank. "
              "The form is the event; the token is the correlation ID; the "
              "manager is the saga orchestrator. Both branch styles work; "
              "the question is which serves <em>your</em> customer load.")
        )
        + H3("0.3  The four shapes you must recognise")
        + ul([
            "<strong>Monolith</strong> — single deployable unit, single "
            "database, one process. Easiest to reason about; hardest to scale "
            "different parts independently. Most pre-2010 core banking "
            "systems (Temenos T24, FLEXCUBE, Finacle) are monoliths under "
            "the bonnet.",
            "<strong>Modular monolith</strong> — single deploy, but rigorous "
            "internal modules with explicit boundaries, ideally one module "
            "per Bounded Context. <em>Increasingly the default recommendation</em> "
            "for new BFSI systems below very large scale (Shopify, Stack "
            "Overflow, several digital banks).",
            "<strong>Service-Oriented Architecture (SOA)</strong> — coarse-"
            "grained services exchanged through an Enterprise Service Bus "
            "(ESB) like IBM WebSphere Message Broker / IBM Integration Bus, "
            "TIBCO, Software AG webMethods, Oracle SOA Suite. The 2000s "
            "answer; still pervasive at JPM, Wells, Citi, Lloyds, BNP.",
            "<strong>Microservices</strong> — many small, independently "
            "deployable services, each owning its data, talking over HTTP or "
            "events. Popularised by Netflix (2009→) and Amazon (‘two-pizza "
            "teams’).",
        ])
        + H3("0.4  Three words you must internalise from DDD")
        + ul([
            "<strong>Bounded Context</strong> — a region of the business "
            "where words mean exactly one thing. ‘Customer’ in Lending means "
            "borrower with credit score; ‘Customer’ in Cards means cardholder "
            "with credit limit; ‘Customer’ in Wealth means investor with risk "
            "profile. Each is a Bounded Context.",
            "<strong>Aggregate</strong> — a cluster of objects that change "
            "together and live under one consistency rule. An ‘Order’ with "
            "its ‘OrderLines’; an ‘Account’ with its ‘Postings’.",
            "<strong>Ubiquitous Language</strong> — the team and the code "
            "use the <em>same words</em> as the business expert. If the "
            "business says ‘chargeback’, the class is named "
            "<code>Chargeback</code>, not <code>RefundV2</code>.",
        ])
    )
    return TopicSection(
        "0.  Primer — monolith vs microservice, said five different ways",
        "basic", body)


# ----------------------------------------------------------------- 1. Why
def _sec1() -> TopicSection:
    body = (
        p("Why does this topic matter so much for BFSI specifically?")
        + ol([
            "<strong>Independent scale.</strong> A bank’s fraud-scoring service "
            "needs to scale with payment volume; its month-end interest-"
            "accrual job needs to scale once a month. In a monolith both must "
            "scale together, which is wasteful. Microservices let each "
            "scale on its own profile.",
            "<strong>Independent change.</strong> Cards code changes every "
            "week; core ledger code changes every quarter; KYC code changes "
            "every time a regulator publishes a circular. In a monolith every "
            "deploy is a whole-bank deploy; with services, each team ships at "
            "its own cadence.",
            "<strong>Team autonomy and Conway’s Law.</strong> Melvin Conway "
            "(1968): systems mirror the communication structure of the "
            "organisations that build them. Banks deliberately exploit this "
            "(‘inverse Conway manoeuvre’) by organising teams around the "
            "services they should own.",
            "<strong>Vendor / build-vs-buy flexibility.</strong> When the "
            "card-issuance capability is a service with a clean contract, you "
            "can swap an in-house implementation for Marqeta or M2P without "
            "touching the rest of the estate.",
            "<strong>Cloud-native economics.</strong> Container schedulers "
            "(Kubernetes), serverless runtimes (AWS Lambda, Azure Functions, "
            "GCP Cloud Run) and autoscaling all reward small, stateless "
            "services.",
            "<strong>Resilience and blast radius.</strong> A bug in the "
            "rewards-redemption service should not bring down ATM withdrawals. "
            "Process and deployment isolation is the engineering form of that "
            "promise.",
        ])
        + p("All of those are <em>also</em> reasons for a well-modularised "
            "monolith. The honest question for any BFSI architect in 2025 is "
            "not ‘microservices yes/no’ but ‘<em>what is the smallest unit "
            "of independent change my organisation can usefully sustain?</em>’.")
    )
    return TopicSection(
        "1.  Why this is a leader-grade decision, not a fashion choice",
        "basic", body)


# ----------------------------------------------------------------- 2. Picture
def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  subgraph "Channel"\n'
            '    M["Mobile / web BFF"]\n'
            '  end\n'
            '  subgraph "Bounded Context: Payments"\n'
            '    P1["Payment Initiation"]\n'
            '    P2["Payment Processing"]\n'
            '    P3["Payments DB"]\n'
            '    P1 --> P2 --> P3\n'
            '  end\n'
            '  subgraph "Bounded Context: Accounts"\n'
            '    A1["Account Service"]\n'
            '    A2["Accounts DB"]\n'
            '    A1 --> A2\n'
            '  end\n'
            '  subgraph "Bounded Context: Fraud"\n'
            '    F1["Fraud Scoring"]\n'
            '    F2["Fraud DB"]\n'
            '    F1 --> F2\n'
            '  end\n'
            '  subgraph "Bounded Context: Notifications"\n'
            '    N1["Notification Service"]\n'
            '  end\n'
            '  M -->|REST| P1\n'
            '  P2 -->|gRPC| A1\n'
            '  P2 -->|gRPC| F1\n'
            '  P2 -- event: PaymentBooked --> K[("Kafka topic<br/>payment.events")]\n'
            '  K --> N1\n'
            '  K --> L["Ledger Posting"]\n'
            '  K --> R["Regulatory Reporting"]',
            "A small slice of a microservice estate. Each Bounded Context owns "
            "its own database; synchronous calls are gRPC / REST; "
            "cross-context business events flow via Kafka.")
    )
    return TopicSection(
        "2.  The picture — Bounded Contexts, owned data, events between",
        "basic", body)


# ----------------------------------------------------------------- 3. How
def _sec3() -> TopicSection:
    body = (
        H3("3.1  Domain-Driven Design in one page")
        + p("DDD was named by Eric Evans in his 2003 book and re-popularised "
            "by Vaughn Vernon (<em>Implementing Domain-Driven Design</em>, "
            "2013) and by the team-topologies / strategic-DDD writing of "
            "Nick Tune, Eduardo da Silva and others. The pieces:")
        + ul([
            "<strong>Strategic DDD</strong> — figure out the business domain. "
            "Identify <em>subdomains</em> (Core, Supporting, Generic). Map "
            "them onto <em>Bounded Contexts</em>. Draw a <strong>Context "
            "Map</strong> that names the integration pattern between each "
            "pair (Customer-Supplier, Conformist, Anti-Corruption Layer, "
            "Open-Host Service, Published Language, Shared Kernel, Separate "
            "Ways).",
            "<strong>Tactical DDD</strong> — inside a Bounded Context: "
            "Entities (have identity), Value Objects (immutable, no "
            "identity), Aggregates (consistency boundary, one root entity), "
            "Repositories (persist aggregates), Domain Events (something "
            "important happened), Domain Services (operations that don’t "
            "belong on one entity).",
            "<strong>Event Storming</strong> (Alberto Brandolini, 2013) — a "
            "workshop technique where business + engineering put orange "
            "sticky notes (Domain Events) on a wall, then add commands, "
            "actors, aggregates and policies. The cheapest way to discover "
            "Bounded Contexts; widely used at ING, Standard Chartered, "
            "Capital One.",
        ])
        + H3("3.2  Service granularity — how small is small enough?")
        + p("A microservice is sometimes defined as ‘small enough to be "
            "rewritten in two weeks’. That is a heuristic, not a rule. "
            "Sam Newman (<em>Building Microservices</em>, 2nd ed. 2021): aim "
            "for services that align to a Bounded Context, that one team "
            "owns end-to-end, that can be deployed independently, and whose "
            "data is theirs alone. Granularity follows business meaning, "
            "not lines of code.")
        + H3("3.3  Owned data — the rule you cannot bend")
        + p("<strong>Every service owns its own data and exposes it only "
            "through its API.</strong> No other service reads its database. "
            "This is the single most-violated rule in BFSI ‘microservice’ "
            "programmes; a shared database underneath ‘services’ creates "
            "the <em>distributed monolith</em>: all the cost of distribution "
            "with none of the independence.")
        + H3("3.4  Synchronous vs asynchronous communication")
        + ul([
            "<strong>Synchronous (REST / gRPC).</strong> Caller waits for "
            "answer. Good for queries, for ‘is this customer KYC-clear?’. "
            "Bad as a primary integration style across many services — "
            "couples lifecycles and creates cascading failures.",
            "<strong>Asynchronous (events on Kafka / Pulsar / MQ).</strong> "
            "Producer publishes a fact (‘PaymentBooked’); any number of "
            "consumers react. Decouples lifecycles, enables replay, "
            "supports many downstream uses (notification, ledger, "
            "reporting, fraud retro-scoring).",
            "<strong>Choreography vs orchestration.</strong> Choreography: "
            "services react to each other’s events with no central brain. "
            "Orchestration: a coordinator service drives the flow "
            "(Camunda, Temporal, AWS Step Functions, Netflix Conductor). "
            "BFSI typically uses choreography for fan-out, orchestration "
            "for long-running, regulated, audit-heavy flows like "
            "onboarding and lending.",
        ])
        + H3("3.5  The saga pattern — multi-service business transactions")
        + p("Database transactions cannot cross service boundaries (no "
            "distributed two-phase commit in practice). A <em>saga</em> is a "
            "sequence of local transactions, each with a defined "
            "<em>compensating action</em> for rollback. Example: open an "
            "account = create-customer + run-KYC + open-deposit-account + "
            "issue-debit-card + send-welcome-pack. If issue-debit-card fails, "
            "the saga compensates by closing the deposit account and "
            "deleting the customer (or marking them as failed-onboarding for "
            "audit). Tools: Camunda 8, Temporal, AWS Step Functions, "
            "Netflix Conductor, Apache Airflow (for batch), or hand-rolled.")
        + H3("3.6  The outbox pattern — never dual-write")
        + p("The single most common BFSI microservice bug: ‘write to DB, "
            "then publish to Kafka’. If the process crashes between the "
            "two, the database and the topic disagree. The <strong>"
            "transactional outbox</strong> pattern: write the row and the "
            "event-to-publish to the <em>same</em> database transaction "
            "(an <code>outbox</code> table); a separate relay process "
            "(Debezium, Maxwell, or custom Change Data Capture) tails the "
            "table and publishes to Kafka. The database and the broker "
            "agree by construction.")
        + H3("3.7  Idempotency — assume every call happens at-least-once")
        + p("In a distributed system, every call may be retried. Writes "
            "must be safe to repeat. Tools: <em>idempotency keys</em> on "
            "the API surface, <em>conditional updates</em> with version "
            "numbers in the database, <em>dedup tables</em> for events. "
            "‘Exactly-once’ end-to-end is impossible; ‘effectively-once’ "
            "via idempotency is the achievable target.")
        + H3("3.8  Observability — three pillars")
        + ul([
            "<strong>Logs</strong> — structured (JSON), with a "
            "<code>correlation-id</code> propagated across every hop "
            "(W3C Trace Context header).",
            "<strong>Metrics</strong> — Prometheus / OpenTelemetry counters, "
            "histograms, gauges. SLOs computed on these.",
            "<strong>Traces</strong> — OpenTelemetry, sent to Jaeger / "
            "Tempo / Honeycomb / Datadog / Dynatrace. Visualises a single "
            "customer request across all the services it touched.",
        ])
    )
    return TopicSection(
        "3.  How it works — DDD, granularity, owned data, events, sagas",
        "intermediate", body)


# ----------------------------------------------------------------- 4. Region overlay
def _sec4() -> TopicSection:
    body = (
        H3("4.1  Where each shape lives in BFSI today")
        + table(
            ["Estate", "Dominant shape", "Notes"],
            [
                ["<strong>Tier-1 incumbent core banking</strong>",
                 "Monolith (mainframe COBOL or T24 / Finacle / FLEXCUBE)",
                 "JPM, Wells, Citi, Lloyds, NatWest, BNP, SBI, ICICI. "
                 "Modernised <em>around</em> the core via the strangler fig."],
                ["<strong>Channels (mobile, web, partner)</strong>",
                 "Microservices behind a Backend-for-Frontend",
                 "Every major bank by now. BFFs in Node / Kotlin / Go; "
                 "downstreams in Java / .NET / Go."],
                ["<strong>Digital-only banks (greenfield)</strong>",
                 "Microservices on cloud-native cores",
                 "Nubank (Clojure / Kotlin microservices on AWS), Revolut "
                 "(Java/Kotlin), Monzo (Go, 2,800+ services as of 2024), "
                 "Starling, Wise, N26, GXS, Trust, Tymebank."],
                ["<strong>Capital markets risk and pricing</strong>",
                 "Big internal libraries + a handful of services",
                 "Murex, Calypso, Bloomberg AIM — large but not "
                 "microservice-shaped. Risk grids and quant libraries are "
                 "‘macroservices’."],
                ["<strong>Payments hubs and rails</strong>",
                 "Modular monolith or vendor platform",
                 "Volante, Form3, ACI Worldwide, Finastra Global PAYplus, "
                 "FIS Open Payment Framework. Internally modular; deployed "
                 "as a hub."],
                ["<strong>Insurance policy admin</strong>",
                 "Configurable monolith (Guidewire, Duck Creek)",
                 "Highly configurable; microservices appear at the edges "
                 "(quoting, claims FNOL apps)."],
            ]
        )
        + H3("4.2  Geographical flavour")
        + ul([
            "<strong>India</strong> — UPI app estates (PhonePe, Paytm, "
            "Google Pay India, BHIM) are deep microservice architectures; "
            "incumbent banks (HDFC, ICICI, SBI, Axis) operate on Finacle / "
            "FLEXCUBE monoliths with API-fronted microservice perimeters.",
            "<strong>United States</strong> — Capital One, Goldman Marquee, "
            "JPM Athena are microservice-heavy; community and regional "
            "banks largely run vendor monoliths (Jack Henry, Fiserv, "
            "FIS).",
            "<strong>United Kingdom</strong> — Starling, Monzo, Wise: "
            "microservices. NatWest, Lloyds, Barclays: modernising "
            "around a mainframe/T24 core. Standard Chartered ‘nexus’ "
            "and SC Ventures: microservices.",
            "<strong>Eurozone</strong> — ING built one of the most-cited "
            "microservice + DDD transformations (BizDevOps squads, 2015 "
            "onward). BBVA, Santander, KBC, Nordea similar trajectory.",
            "<strong>Singapore + South-East Asia</strong> — DBS digibank "
            "rebuilt on cloud-native microservices; GXS, Trust, MariBank, "
            "Tonik, Aspire — microservice greenfield.",
            "<strong>Brazil</strong> — Nubank is the global reference for "
            "microservices in BFSI (Clojure + Kotlin + Datomic + Kafka, "
            "AWS); Itaú, Bradesco modernising similarly.",
        ])
    )
    return TopicSection(
        "4.  Where each shape lives in the real BFSI estate, geo by geo",
        "intermediate", body)


# ----------------------------------------------------------------- 5. Advanced
def _sec5() -> TopicSection:
    body = (
        H3("5.1  The strangler fig — how monoliths actually die")
        + p("Martin Fowler’s 2004 metaphor: the strangler fig tree grows "
            "around its host until the host rots away inside. In practice, "
            "a BFSI monolith is replaced by:")
        + ol([
            "<strong>Putting a façade</strong> (API gateway or thin proxy) in "
            "front of every call into the monolith.",
            "<strong>Intercepting routes one at a time</strong>: when the "
            "new ‘Cards’ microservice is ready, the façade routes "
            "<code>/cards/*</code> to the microservice; the monolith no "
            "longer handles those.",
            "<strong>Migrating data</strong> by Change Data Capture (CDC) "
            "from the monolith DB to the microservice DB, dual-writing "
            "during the bake period.",
            "<strong>Removing the dead code</strong> in the monolith once "
            "every route is moved.",
        ])
        + p("Done well, this is invisible to the customer; done badly, you "
            "get ‘permanent migration’ — half the routes on each side for "
            "five years.")
        + H3("5.2  CQRS and event sourcing — when to and when not to")
        + ul([
            "<strong>Command Query Responsibility Segregation (CQRS)</strong> "
            "— split the write model (commands) from the read model "
            "(queries). Useful when read and write loads diverge wildly. "
            "Standard in fraud, risk and reporting where reads are "
            "100–1000× writes.",
            "<strong>Event sourcing</strong> — store the sequence of "
            "events as the system of record; derive current state by "
            "replay. Brilliant for ledgers (an account <em>is</em> a "
            "sequence of postings) and audit-heavy domains. Costly when "
            "the team does not understand projections, snapshots and "
            "schema evolution. Used by Nubank, ING Bank, Volante, Thought "
            "Machine Vault Core.",
        ])
        + H3("5.3  Service mesh and platform engineering")
        + p("Once you have more than ~30 services, the connective tissue "
            "becomes a product in its own right. A <strong>service "
            "mesh</strong> (Istio, Linkerd, Consul Connect, AWS App Mesh) "
            "moves cross-cutting concerns — mTLS, retries, circuit "
            "breakers, traffic shifting, observability — out of every "
            "service and into the platform. An <strong>Internal Developer "
            "Platform (IDP)</strong> built with Backstage (Spotify), "
            "Humanitec, Port or Cortex turns ‘create a new service’ from "
            "a multi-day exercise into a self-service template.")
        + H3("5.4  Distributed-data patterns")
        + ul([
            "<strong>Database-per-service</strong> — non-negotiable.",
            "<strong>Change Data Capture (CDC)</strong> — Debezium / "
            "AWS DMS / Oracle GoldenGate / IBM InfoSphere CDC tails the "
            "transaction log and emits events; the canonical way to keep "
            "downstream read-models in sync.",
            "<strong>Data mesh</strong> (Zhamak Dehghani, 2019) — extend "
            "service ownership to analytical data: domains own their "
            "analytical data products as first-class. Increasingly "
            "influential in BFSI data strategies (JPM, ABN AMRO, ANZ).",
            "<strong>Polyglot persistence</strong> — different stores for "
            "different jobs: Postgres / Oracle for OLTP, Cassandra / "
            "DynamoDB for high-volume key-value, Elastic / OpenSearch for "
            "search, Snowflake / Databricks / BigQuery for analytics. "
            "Justify each choice; do not collect databases.",
        ])
        + H3("5.5  Anti-patterns the regulator will eventually find")
        + ul([
            "<strong>Distributed monolith</strong> — services share a "
            "database. Deploys still must be coordinated. Worst of both "
            "worlds.",
            "<strong>Chatty services</strong> — one customer request fans "
            "out into 30+ synchronous calls. Latency budget blown, "
            "blast radius enormous.",
            "<strong>Anaemic services</strong> — every service is a thin "
            "CRUD wrapper over a table; ‘business logic’ lives in the "
            "channel or the BFF. The bank’s rules end up implemented in "
            "JavaScript on the front-end, which auditors will find.",
            "<strong>Shared utility libraries</strong> that become a "
            "second monolith — bumping the version forces all 200 "
            "services to redeploy.",
            "<strong>Premature decomposition</strong> — splitting a "
            "system before the domain is understood, then reorganising "
            "every six months. The cost is borne in incidents.",
        ])
        + H3("5.6  Runtime choices — Java, .NET, Go, Kotlin, Node")
        + ul([
            "<strong>Java (Spring Boot, Quarkus, Micronaut)</strong> — "
            "still the dominant BFSI server-side runtime. Quarkus and "
            "Micronaut + GraalVM native compilation address Java’s old "
            "cold-start weakness for serverless.",
            "<strong>Kotlin</strong> — modern JVM language, popular at "
            "Revolut, Wise, Trust Bank, Standard Chartered.",
            "<strong>.NET 8 / 9</strong> — strong at Microsoft-house "
            "banks; performance with Native AOT now competitive with Go.",
            "<strong>Go</strong> — chosen by Monzo, Wise, Cash App; "
            "small binaries, fast startup, simple concurrency.",
            "<strong>Node.js / TypeScript</strong> — channel and BFF "
            "layer everywhere; rarely the choice for core ledger services.",
            "<strong>Clojure</strong> — Nubank, JUSPAY (parts of); niche "
            "but successful in functional-DDD contexts.",
            "<strong>Python</strong> — analytics, data engineering, ML, "
            "increasingly serverless glue; rarely the OLTP runtime.",
            "<strong>COBOL on z/OS</strong> — still hundreds of billions "
            "of dollars cleared per day. Modernised behind APIs and "
            "z/OS Connect EE.",
        ])
    )
    return TopicSection(
        "5.  Advanced — strangler fig, CQRS, event sourcing, mesh, "
        "data, anti-patterns",
        "advanced", body)


# ----------------------------------------------------------------- 6. Decisions
def _sec6() -> TopicSection:
    body = (
        H3("6.1  When to choose each shape")
        + table(
            ["Situation", "Best shape in 2025", "Why"],
            [
                ["Greenfield digital bank, <2M customers, <50 engineers",
                 "Modular monolith with one DB schema per module",
                 "Faster to build; <em>can</em> be carved into services "
                 "later if a real scaling reason appears. Don’t pay the "
                 "distributed-systems tax up front."],
                ["Greenfield digital bank, scaling fast (Nubank-like)",
                 "Microservices, cloud-native, event-driven core",
                 "Independent scale and team velocity dominate; you can "
                 "afford the platform investment."],
                ["Incumbent retail bank with mainframe core",
                 "Strangler fig — microservices around the core",
                 "Replacement risk on the core is unacceptable; "
                 "modernise the channels and the supporting domains."],
                ["Capital-markets risk engine",
                 "Macroservices + shared library",
                 "Quant libraries are large, change tightly together, "
                 "and run on dedicated grids. Microservicing them "
                 "rarely pays."],
                ["Vendor platform (T24, Finacle, FLEXCUBE, Guidewire)",
                 "Accept the vendor’s shape; surround with services",
                 "Don’t fight the vendor architecture; build the "
                 "ecosystem around it via APIs."],
                ["Regulatory reporting hub",
                 "Pipeline of services + event stream",
                 "High fan-in from many systems; CDC + Kafka + a few "
                 "transformation services beats a monolith here."],
                ["Lending originations end-to-end flow",
                 "Microservices + orchestrator (Camunda / Temporal)",
                 "Long-running, multi-step, regulated, audit-heavy; "
                 "orchestration earns its keep."],
            ]
        )
        + H3("6.2  Build-vs-buy implications")
        + p("Microservices make build-vs-buy <em>granular</em>: you can "
            "buy a card-tokenisation service from a specialist, build "
            "your loyalty service in-house, and rent a fraud service "
            "from Feedzai, all on the same platform. The contract is the "
            "API; the cost is integration discipline.")
    )
    return TopicSection(
        "6.  Decision matrix — which shape, when, why",
        "intermediate", body)


# ----------------------------------------------------------------- 7. Worked examples
def _sec7() -> TopicSection:
    body = (
        example(
            "Monzo — Go microservices at scale",
            ol([
                "Monzo (UK challenger bank, launched 2015) runs on AWS "
                "with thousands of Go microservices behind a custom "
                "service mesh (originally Linkerd, then in-house).",
                "Every service has its own Cassandra keyspace; a "
                "ledger service is the source of truth for balances; "
                "every other service holds a derived view.",
                "Payments flow as events on an internal RPC / queue "
                "system; Monzo publishes detailed engineering blogs on "
                "incidents and on architecture (recommended reading).",
                "Trade-off: extreme service count requires extreme "
                "platform investment. Monzo’s platform team is "
                "proportionally large; the model only works because "
                "the bank treats the platform as a product.",
            ])
        )
        + example(
            "Nubank — DDD-first, event-sourced core",
            ol([
                "Nubank (Brazil, then Mexico, Colombia) built its card-"
                "issuing and banking platform on Clojure microservices, "
                "Datomic (immutable database) and Kafka.",
                "The ledger is event-sourced: every posting is an "
                "immutable fact; balances are derived projections.",
                "Bounded Contexts are explicit, named, and have "
                "team-of-record. Event Storming and DDD reference "
                "books are part of onboarding.",
                "Result: 90M+ customers on a single architecture, "
                "with double-digit-millisecond payment latency.",
            ])
        )
        + example(
            "Standard Chartered ‘nexus’ — banking-as-a-service",
            ol([
                "SC Ventures’ nexus platform was designed to let "
                "non-bank partners (e-commerce, telcos) launch "
                "banking products on Standard Chartered licences.",
                "Architecturally a microservices estate with a "
                "Backend-for-Frontend per partner, on Azure, with "
                "Apigee at the edge.",
                "Pivoted in 2023 toward focused use cases; "
                "engineering patterns continue to inform Standard "
                "Chartered’s ‘aXess’ developer platform.",
            ])
        )
        + example(
            "JPM Athena / Phoenix — internal microservices and the "
            "Python monorepo",
            ol([
                "Athena is JPM’s internal trading and risk platform; "
                "Phoenix is the asset-management equivalent.",
                "Tens of thousands of Python modules in a single "
                "monorepo, with services exposed via internal RPC; "
                "shows that ‘microservices’ does not always mean "
                "‘polyglot’ or ‘decentralised repo’.",
                "Lesson: organisational coherence (one repo, one "
                "platform) can coexist with deployment independence.",
            ])
        )
        + example(
            "An incumbent bank’s strangler-fig journey on a Finacle core",
            ol([
                "Year 1: introduce an API gateway in front of Finacle; "
                "expose retail account and transaction APIs.",
                "Year 2: build a customer-360 microservice that owns "
                "the new ‘customer master’; reads from Finacle via "
                "API; new channels read from customer-360.",
                "Year 3: build a notifications microservice that "
                "subscribes to Kafka events emitted by CDC on the "
                "Finacle DB.",
                "Year 4: extract cards issuance and loyalty into "
                "separate services with their own datastores; cut "
                "channels over.",
                "Year 5: Finacle still owns the deposit and lending "
                "ledger, but most customer-facing change happens in "
                "the surrounding services, deployable on their own "
                "cadence. The bank looks ‘cloud-native’ to its "
                "customers while the regulated core remains unchanged.",
            ])
        )
    )
    return TopicSection(
        "7.  Worked examples — five real BFSI architectures",
        "intermediate", body)


# ----------------------------------------------------------------- 8. Questions
def _sec8() -> TopicSection:
    return TopicSection(
        "8.  Questions a leader asks in any architecture review", "basic",
        ol([
            "What are our Bounded Contexts, and is there a one-page "
            "Context Map? When was it last updated?",
            "Does every service own its own database, with no other "
            "service reading it?",
            "What is the synchronous call depth from a typical channel "
            "request? (More than 4–5 hops is a red flag.)",
            "How do we publish events reliably — outbox + CDC, or "
            "dual-writes? (Dual-writes is the wrong answer.)",
            "Where are our sagas, who owns them, and how are "
            "compensations tested?",
            "Are write APIs idempotent? What is the idempotency-key "
            "policy and retention?",
            "What is our service-to-service authentication — mTLS via "
            "service mesh, signed JWTs, or both? How are credentials "
            "rotated?",
            "Where is the customer journey traced end-to-end? Can we "
            "produce a single trace for a salary credit from FedNow / "
            "SEPA / UPI to mobile notification?",
            "What are the Service-Level Objectives (SLOs) of each "
            "critical service, and what is the error budget burn this "
            "quarter?",
            "What is our strangler-fig progress on each legacy "
            "monolith — percentage of traffic still served by the "
            "monolith, dates for next routes to move?",
            "Do we have a written ‘service template’ and an Internal "
            "Developer Platform, or does each team rebuild the "
            "wheel?",
            "Have we run a chaos / failure-injection exercise on "
            "this estate in the last 6 months — and what did we "
            "learn?",
        ]))


# ----------------------------------------------------------------- 9. Red flags
def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘We’re going microservices because the new digital banks do.’ "
            "— Not a reason. Microservices are a response to scale, team "
            "size and independence pressures. If you do not have those "
            "pressures, you will pay the distributed-systems tax for "
            "nothing.",
            "‘We have 200 services and a single Oracle database underneath.’ "
            "— That is a distributed monolith. Worst of both worlds. "
            "Either consolidate or carve the data.",
            "‘Two-phase commit across services will give us consistency.’ "
            "— In practice, distributed 2PC is a fragility magnet and "
            "every modern broker / database vendor warns against it. "
            "Use sagas + outbox.",
            "‘We use Kafka so our events are reliable.’ — Reliable on the "
            "broker side. The producer-database disagreement is solved by "
            "the outbox pattern, not by the broker.",
            "‘Each team picks any language and any database.’ — Then your "
            "platform team supports n × m combinations. Constrain the "
            "‘paved road’ to 2–3 languages and 2–3 data stores; allow "
            "exceptions with a written justification.",
            "‘We deploy 100× a day, therefore we’re cloud-native.’ — "
            "Deployment frequency is a vanity metric without correlated "
            "Mean Time To Restore (MTTR) and Change Failure Rate. Watch "
            "the DORA metrics together, not in isolation.",
            "‘The mainframe must be replaced before we can modernise.’ — "
            "Almost never true for a tier-1 incumbent. The strangler "
            "fig is the answer; full core replacement is a 7–10 year, "
            "billion-dollar bet that has failed at TSB, Co-op Bank, "
            "Westpac panorama, and others within memory.",
            "‘DDD is academic; we don’t have time.’ — Skipping DDD is the "
            "single biggest predictor of distributed-monolith outcomes. "
            "Two days of Event Storming with the business saves two "
            "years of refactoring.",
            "‘Event sourcing everywhere.’ — Beautiful in the ledger, "
            "painful in catalogue / reference data services. Choose "
            "where it earns its keep.",
            "‘Microservices made our system more resilient.’ — Only "
            "if you have explicit timeouts, retries with jitter, "
            "circuit breakers, bulkheads, and chaos testing. Otherwise "
            "microservices multiply failure modes.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("Monolith", "Single deployable unit, single database, one "
                "process."),
            ("Modular monolith", "Single deploy, with explicit internal "
                "module boundaries; often the right default."),
            ("Microservice", "Small, independently deployable service "
                "aligned to a Bounded Context, with its own data."),
            ("SOA / ESB", "Service-Oriented Architecture / Enterprise "
                "Service Bus — the 2000s integration style; coarse-grained "
                "services through a central bus."),
            ("DDD", "Domain-Driven Design — Eric Evans 2003; the "
                "discipline of modelling software around the business "
                "domain."),
            ("Bounded Context", "A region of the business where each term "
                "has exactly one meaning."),
            ("Aggregate", "A cluster of objects that change together under "
                "one consistency rule, with a root entity."),
            ("Ubiquitous Language", "The shared vocabulary used by "
                "business and code inside a Bounded Context."),
            ("Event Storming", "Workshop technique (Alberto Brandolini) "
                "to discover Bounded Contexts and Domain Events."),
            ("Context Map", "Diagram of how Bounded Contexts integrate, "
                "naming the relationship style."),
            ("Anti-Corruption Layer", "An adapter that translates between "
                "two Bounded Contexts so foreign concepts don’t leak in."),
            ("Saga", "Sequence of local transactions with compensations; "
                "the way multi-service business transactions stay "
                "consistent without 2PC."),
            ("Outbox pattern", "Write business change and outgoing event "
                "to the same database transaction; relay publishes the "
                "event."),
            ("Idempotency key", "Unique key sent with a write request so "
                "retries do not duplicate the effect."),
            ("CQRS", "Command Query Responsibility Segregation — separate "
                "write model from read model."),
            ("Event sourcing", "Store events as the system of record; "
                "derive current state by replay."),
            ("Choreography vs orchestration", "Services react to each "
                "other (choreography) vs a coordinator drives the flow "
                "(orchestration)."),
            ("Strangler fig", "Migration pattern where new services "
                "gradually replace pieces of a legacy monolith (Martin "
                "Fowler, 2004)."),
            ("CDC", "Change Data Capture — tailing the database "
                "transaction log to emit events; Debezium, GoldenGate, "
                "DMS."),
            ("Service mesh", "Platform layer (Istio, Linkerd, Consul) "
                "for mTLS, retries, traffic, observability between "
                "services."),
            ("Internal Developer Platform (IDP)", "Self-service paved "
                "road for engineers: Backstage, Humanitec, Port, Cortex."),
            ("Data mesh", "Domain-aligned ownership of analytical data "
                "as products (Zhamak Dehghani, 2019)."),
            ("Polyglot persistence", "Using different data stores for "
                "different jobs."),
            ("Conway’s Law", "Systems mirror the communication structure "
                "of the organisations that build them (Melvin Conway, "
                "1968)."),
            ("DORA metrics", "DevOps Research and Assessment — "
                "deployment frequency, lead time, MTTR, change failure "
                "rate (note: distinct from EU DORA the regulation)."),
            ("Two-pizza team", "Amazon heuristic: a service team small "
                "enough to be fed by two pizzas (≈ 6–10 people)."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
