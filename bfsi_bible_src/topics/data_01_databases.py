"""Data · 01 — Databases and the bank's ledger (OLTP, NoSQL, lakehouse)."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="III.1",
        slug="01-databases-and-the-ledger",
        title="Databases and the bank’s ledger — OLTP, NoSQL, and the lakehouse",
        one_liner=(
            "A bank is, fundamentally, a database with a marketing department. "
            "Everything else — channels, branches, cards, regulators — exists to "
            "service or to read from a small set of authoritative tables. This "
            "topic gives you fluency in the data layer: ACID and the relational "
            "world that runs the ledger; NoSQL and key-value stores that run the "
            "channels; the lakehouse that runs analytics and risk; the migration "
            "from Oracle and Db2 to Postgres and to cloud-managed databases; and "
            "the open table formats (Apache Iceberg, Delta Lake, Apache Hudi) "
            "that are quietly rewiring how every bank stores its truth."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("‘Database’ is too small a word for what a bank actually runs. A "
              "tier-1 bank operates 5,000–20,000 distinct databases across 10–"
              "20 engine families, holding everything from a single posting on "
              "a current account to 30 years of trade tickets. The shape of "
              "those engines and the rules they obey are the shape of the "
              "bank’s risk, latency and regulatory posture.")
        )
        + H3("0.1  IT-side anchor — the spreadsheet on your laptop")
        + it_anchor(
            p("Open a spreadsheet. Each <em>row</em> is a record; each <em>"
              "column</em> is a field. If you change a cell, the saved file "
              "is the new truth — there is no ‘old version’ unless you saved "
              "a copy. That is a <strong>relational table</strong> in "
              "miniature, with one major difference: a real database is "
              "<em>multi-user</em>. Two people editing the same cell at the "
              "same time would corrupt your spreadsheet. A database has "
              "rules — <strong>ACID</strong> (Atomicity, Consistency, "
              "Isolation, Durability) — that prevent that. Banks are the "
              "industry that invented and still depends most on those "
              "rules.")
        )
        + H3("0.2  BFSI-side anchor — what your passbook always was")
        + bfsi_anchor(
            p("Your bank passbook is the original ledger: a chronological, "
              "append-only record of debits and credits, with a running "
              "balance. It never erases entries; it only adds new ones. "
              "Modern banks’ ledgers obey the same rule. Every UPI tap, "
              "every salary credit, every card swipe is a new posting. "
              "A statement is a query against the postings; a balance is "
              "an aggregate. The ledger is the system of record; "
              "everything else (mobile app, ATM, internet banking) is a "
              "view on top.")
        )
        + H3("0.3  The four families of database you must recognise")
        + ul([
            "<strong>Relational / SQL — the ledger family.</strong> "
            "Oracle Database, IBM Db2 (LUW and z/OS), Microsoft SQL Server, "
            "PostgreSQL, MySQL / MariaDB. Strong ACID; the home of every "
            "core banking ledger.",
            "<strong>Key-value and document — the channel family.</strong> "
            "Redis, Memcached, MongoDB, Couchbase, Amazon DynamoDB, Azure "
            "Cosmos DB, Google Firestore. Fast, flexible, often used for "
            "session, cache, and customer-360 aggregates.",
            "<strong>Wide-column and time-series — the volume family.</strong> "
            "Apache Cassandra, ScyllaDB, Amazon Keyspaces, InfluxDB, "
            "TimescaleDB, kdb+ (capital markets tick data). Built for "
            "very high write throughput and time-ordered data.",
            "<strong>Analytical — the lakehouse family.</strong> Snowflake, "
            "Databricks (Delta), Google BigQuery, Amazon Redshift, "
            "Microsoft Fabric, Teradata, ClickHouse. Columnar, "
            "massively parallel, optimised for scans of billions of rows.",
        ])
        + H3("0.4  Two more you must recognise on sight")
        + ul([
            "<strong>Graph databases</strong> — Neo4j, Amazon Neptune, "
            "TigerGraph, Memgraph. Used for fraud rings, AML network "
            "analysis, beneficial-ownership graphs.",
            "<strong>Search engines</strong> — Elasticsearch / OpenSearch, "
            "Apache Solr. Used for customer search, transaction search, "
            "case-management, and log analytics.",
        ])
    )
    return TopicSection(
        "0.  Primer — the four families of bank databases",
        "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Why is the data layer the most consequential part of a BFSI "
            "stack to get right?")
        + ol([
            "<strong>The ledger is the bank.</strong> Lose the ledger and "
            "you have no business; corrupt it and you have a regulatory "
            "incident; slow it down and customers leave. Every other "
            "component is replaceable; the ledger is not.",
            "<strong>Regulatory durability.</strong> RBI requires payment "
            "data stored in India for at least the life of the customer + "
            "regulatory retention; SEC Rule 17a-4 requires write-once "
            "storage for broker-dealer records; SOX, MiFID II, EMIR and "
            "the GDPR / DPDP all touch the database.",
            "<strong>Latency budget.</strong> A UPI transaction must be "
            "end-to-end under 30 seconds; a card authorisation under 2 "
            "seconds; an HFT order under 50 microseconds. The database "
            "lives inside that budget.",
            "<strong>Cost.</strong> Oracle and Db2 licences alone cost a "
            "tier-1 bank USD 100M–500M a year. The Postgres / cloud-"
            "managed migration is a generational cost programme.",
            "<strong>AI and analytics.</strong> Every machine-learning "
            "model is only as good as the data it sees. The lakehouse is "
            "now the platform for AI; the conversation has moved from "
            "‘data warehouse’ to ‘AI-ready data platform’.",
        ])
    )
    return TopicSection(
        "1.  Why the data layer dominates BFSI architecture",
        "basic", body)


def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  subgraph "OLTP — Online Transaction Processing"\n'
            '    L["Core ledger<br/>Oracle / Db2 / Postgres"]\n'
            '    A["Account, customer<br/>relational"]\n'
            '    K["Sessions, carts<br/>Redis"]\n'
            '  end\n'
            '  subgraph "Operational data store"\n'
            '    O["Customer 360 / 1-day fresh<br/>Postgres / Mongo"]\n'
            '  end\n'
            '  subgraph "Streaming"\n'
            '    S["Kafka, Pulsar<br/>change events"]\n'
            '  end\n'
            '  subgraph "Lakehouse — analytics"\n'
            '    Lk["Object storage<br/>S3 / ADLS / GCS"]\n'
            '    F["Iceberg / Delta / Hudi<br/>open table format"]\n'
            '    W["Snowflake / Databricks<br/>BigQuery / Redshift"]\n'
            '    M["ML feature store<br/>risk, fraud, marketing"]\n'
            '  end\n'
            '  L -- CDC --> S\n'
            '  A -- CDC --> S\n'
            '  S --> Lk\n'
            '  Lk --> F --> W --> M',
            "How a modern bank’s data flows: OLTP feeds Kafka via Change "
            "Data Capture; the lakehouse rebuilds analytical and ML data "
            "products on open table formats over object storage.")
    )
    return TopicSection(
        "2.  The picture — OLTP, streaming, lakehouse on one wall",
        "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  ACID, in plain words")
        + ul([
            "<strong>Atomicity</strong> — a transaction either entirely "
            "happens or entirely does not. A transfer of ₹10,000 from "
            "you to me debits you <em>and</em> credits me, or neither.",
            "<strong>Consistency</strong> — the database moves from one "
            "valid state to another. Constraints (foreign keys, check "
            "constraints, unique indices) are honoured.",
            "<strong>Isolation</strong> — concurrent transactions appear "
            "to run one after another. Levels: Read Uncommitted, Read "
            "Committed, Repeatable Read, Serializable. Most BFSI ledgers "
            "use Read Committed with row-level locks (Oracle), or "
            "Serializable Snapshot Isolation (Postgres).",
            "<strong>Durability</strong> — once committed, the change "
            "survives a crash. Achieved via write-ahead log (WAL) or "
            "redo log written to durable disk before commit returns.",
        ])
        + H3("3.2  CAP and the consistency-availability trade-off")
        + p("Eric Brewer’s CAP theorem (2000): in a distributed system "
            "you can pick at most two of <strong>Consistency, "
            "Availability, Partition tolerance</strong> when a network "
            "split happens. Banks’ ledgers chose CP — they would rather "
            "stop than lie about your balance. Channel and read-only "
            "systems often choose AP — they prefer to serve a slightly "
            "stale balance than refuse the screen. PACELC (Daniel "
            "Abadi, 2010) extends CAP: ‘<em>else</em>, when there is no "
            "partition, you trade Latency for Consistency’.")
        + H3("3.3  Replication, sharding, and high availability")
        + ul([
            "<strong>Primary–replica replication</strong> — one writer, "
            "many readers; failover promotes a replica. Standard for "
            "Oracle Data Guard, Db2 HADR, SQL Server Always On, Postgres "
            "streaming replication.",
            "<strong>Multi-primary replication</strong> — multiple "
            "writeable nodes. Hard to make correct. Oracle GoldenGate, "
            "Postgres BDR, MySQL Group Replication, CockroachDB.",
            "<strong>Sharding (horizontal partitioning)</strong> — split "
            "the data by key (customer_id, account_id) across many "
            "nodes. Required at very high write volumes. MongoDB, "
            "Cassandra, DynamoDB and YugabyteDB shard natively; "
            "Postgres uses Citus or Vitess.",
            "<strong>Synchronous vs asynchronous replication</strong> — "
            "synchronous: commit waits for the replica. Zero data loss "
            "on failover; latency penalty across regions. Asynchronous: "
            "commit returns immediately; replicas may lag by milliseconds "
            "to seconds. BFSI ledgers run synchronous within a metro, "
            "asynchronous across regions.",
        ])
        + H3("3.4  The Oracle / Db2 incumbency, and the Postgres tide")
        + ul([
            "<strong>Oracle Database</strong> — the dominant BFSI OLTP "
            "engine for 30 years. Real Application Clusters (RAC), Data "
            "Guard, GoldenGate, Exadata. Expensive but battle-tested. "
            "Used by JPM, BoA, Citi, HSBC, Lloyds, SBI, ICICI.",
            "<strong>IBM Db2</strong> — z/OS Db2 sits behind most "
            "mainframe core banks; LUW (Linux/Unix/Windows) Db2 still "
            "common at NatWest, BNP, MUFG. Tightly integrated with COBOL "
            "and IBM MQ.",
            "<strong>Microsoft SQL Server</strong> — strong at "
            "Microsoft-house banks and at vendor platforms (Murex on "
            "SQL Server is common; many treasury systems too).",
            "<strong>PostgreSQL</strong> — the open-source success of "
            "the decade. Used by Goldman Sachs, Capital One, Wise, "
            "Revolut, GXS, Trust, Tonik, Nubank (alongside Datomic). "
            "AWS Aurora Postgres, Azure Database for Postgres, GCP "
            "AlloyDB are the cloud-managed flavours.",
            "<strong>NewSQL — distributed SQL</strong> — CockroachDB, "
            "YugabyteDB, Google Spanner, TiDB. Postgres-compatible, "
            "horizontally scalable, ACID across regions. Increasingly "
            "chosen for greenfield BFSI ledgers (e.g. Form3 on "
            "CockroachDB; SoFi, DoorDash on similar).",
        ])
        + H3("3.5  Mainframe data — IMS, VSAM, IDMS")
        + p("Behind the mainframe core banks of JPM, Wells, Citi, BoA, "
            "Lloyds, BoB, SBI you will still find <strong>IMS</strong> "
            "(Information Management System, hierarchical), <strong>"
            "VSAM</strong> (Virtual Storage Access Method, file-based) "
            "and occasionally CA <strong>IDMS</strong> (network model). "
            "These are not ‘legacy’ in the sense of broken; they handle "
            "tens of thousands of transactions per second per LPAR with "
            "extraordinary reliability. Modernisation programmes (BMC "
            "AMI, IBM z/OS Connect, Precisely Data Integration) wrap "
            "them behind APIs and stream changes to Kafka.")
        + H3("3.6  NoSQL and where it earns its keep")
        + ul([
            "<strong>Redis</strong> — in-memory key-value; sessions, "
            "tokens, rate limits, leaderboards. The most common cache "
            "in BFSI.",
            "<strong>MongoDB / Couchbase</strong> — document; "
            "customer-360 profiles, content / product catalogues, "
            "ad-hoc data with evolving schema.",
            "<strong>Cassandra / ScyllaDB / DynamoDB</strong> — wide-"
            "column / key-value at scale; used for messaging, "
            "notifications, audit logs, time-series at banks like "
            "Monzo, ICICI, ICE, Apple.",
            "<strong>kdb+ / q</strong> — column-store for tick data; "
            "ubiquitous on the trading floor at Goldman, JPM, Morgan "
            "Stanley, Citadel.",
            "<strong>Graph (Neo4j, TigerGraph, Neptune)</strong> — fraud "
            "rings, AML networks, KYC beneficial-ownership graphs.",
        ])
        + H3("3.7  The lakehouse and open table formats")
        + p("From 2010 to 2018 banks invested in <em>data lakes</em> on "
            "Hadoop / HDFS, often Cloudera or Hortonworks. The lakes "
            "got data in cheaply but were hard to query, hard to "
            "govern, and lost ACID guarantees. The <strong>lakehouse</strong> "
            "(Databricks’ name, ~2020) restores ACID, schema "
            "enforcement, time travel and concurrent writers on top of "
            "object storage by adding an <em>open table format</em>:")
        + ul([
            "<strong>Apache Iceberg</strong> — Netflix-origin, "
            "Apache-governed, multi-engine (Snowflake, BigQuery, "
            "Trino, Spark, Flink, Athena, Dremio). The standard most "
            "BFSI vendors are converging on; Snowflake announced "
            "native Iceberg in 2023, AWS S3 Tables in 2024.",
            "<strong>Delta Lake</strong> — Databricks-origin; in 2022 "
            "the spec was open-sourced (Delta UniForm now interoperates "
            "with Iceberg).",
            "<strong>Apache Hudi</strong> — Uber-origin; strong on "
            "incremental ingestion and upserts.",
        ])
        + p("On top sit the warehouse engines: <strong>Snowflake, "
            "Databricks SQL, Google BigQuery, Amazon Redshift, "
            "Microsoft Fabric / Synapse, Teradata, ClickHouse</strong>. "
            "Banks now buy storage once (object store + open table "
            "format) and bring multiple engines to it, instead of "
            "loading the same data three times into three "
            "warehouses.")
    )
    return TopicSection(
        "3.  How databases actually work — ACID, CAP, replication, "
        "sharding, OLTP and lakehouse",
        "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  Region-by-region rules on data")
        + table(
            ["Region", "Key rules touching the database",
             "Practical effect"],
            [
                ["<strong>India</strong>",
                 "RBI Storage of Payment System Data (April 2018), DPDP "
                 "Act 2023, RBI IT Governance MD (Nov 2023), RBI "
                 "Outsourcing of IT Services MD (April 2023).",
                 "Payment data stored within India end-to-end. Cloud "
                 "regions in India exist (AWS Mumbai/Hyderabad, Azure "
                 "Pune/Mumbai/Chennai, GCP Mumbai/Delhi, OCI Mumbai/"
                 "Hyderabad). Strong audit and exit obligations."],
                ["<strong>United States</strong>",
                 "SEC 17a-4(f) WORM (Write-Once Read-Many) for broker-"
                 "dealers; CFTC similar; OCC Heightened Standards; "
                 "GLBA Safeguards Rule; state laws (CCPA / CPRA).",
                 "Trade and order records on WORM-compliant storage; "
                 "encryption-at-rest for customer data."],
                ["<strong>United Kingdom</strong>",
                 "UK GDPR + Data Protection Act 2018; FCA SYSC; PRA "
                 "SS2/21 outsourcing; Operational Resilience policy.",
                 "Personal data export requires Standard Contractual "
                 "Clauses or adequacy; resilience requires defined "
                 "Recovery Point Objective (RPO) per important "
                 "business service."],
                ["<strong>Eurozone</strong>",
                 "EU GDPR; <strong>EU DORA from 17 Jan 2025</strong>; "
                 "EBA Guidelines on Outsourcing; "
                 "EU AI Act 2024.",
                 "Database vendors and cloud providers are ‘ICT third "
                 "parties’; concentration risk monitored. PII (Personally "
                 "Identifiable Information) movements outside EEA "
                 "require Schrems II–compliant transfer mechanisms."],
                ["<strong>Singapore</strong>",
                 "PDPA 2012 + 2020 amendments; MAS TRM Guidelines "
                 "(Cloud annex); MAS Notice 644 / 658.",
                 "Strong audit trails, encryption, key management; "
                 "MAS expects HSM-backed keys for sensitive data."],
                ["<strong>Cross-border</strong>",
                 "Schrems II ruling (2020), EU-US Data Privacy "
                 "Framework (2023), UK-US Data Bridge (2023).",
                 "Personal data flows EU↔US legally re-enabled, but "
                 "subject to legal challenge; many banks still keep "
                 "personal data in-region."],
            ]
        )
        + H3("4.2  Right-to-be-forgotten and the immutable ledger")
        + p("BFSI databases sit at a tension: regulators say keep "
            "everything for 5–10 years; data-protection law says "
            "delete on request. The reconciliation: <em>retention "
            "obligations override the right to erasure</em> for "
            "transactions and regulatory records, but personal data "
            "fields can be tokenised, masked or anonymised. Banks "
            "increasingly separate ‘the ledger’ (immutable, no PII) "
            "from ‘the customer master’ (PII, redactable).")
    )
    return TopicSection(
        "4.  Region by region — what regulators say about your data",
        "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  Encryption — at rest, in transit, in use")
        + ul([
            "<strong>At rest</strong> — Transparent Data Encryption "
            "(Oracle TDE, SQL Server TDE), per-tablespace or per-column "
            "encryption; cloud-managed keys via AWS KMS / Azure Key "
            "Vault / GCP Cloud KMS / OCI Vault; HSM-backed keys for "
            "sensitive data.",
            "<strong>In transit</strong> — TLS 1.2+ for client-database "
            "and replication links; mTLS in regulated environments.",
            "<strong>In use</strong> — confidential-computing enclaves "
            "(AWS Nitro Enclaves, Azure Confidential VMs, GCP "
            "Confidential VMs); cryptographic-erase (delete the key, "
            "the data is gone).",
            "<strong>Tokenisation and Format-Preserving Encryption "
            "(FPE)</strong> — replace card numbers with tokens "
            "(Voltage SecureData, Protegrity, Thales CipherTrust) so "
            "the analytical store never holds Primary Account Numbers "
            "(PANs).",
        ])
        + H3("5.2  HTAP — when one engine tries to do both OLTP and OLAP")
        + p("Hybrid Transactional / Analytical Processing engines "
            "(SAP HANA, Oracle Database In-Memory, MemSQL/SingleStore, "
            "TiDB, AlloyDB, Snowflake Unistore) keep transactional and "
            "analytical workloads on a single engine. Useful for "
            "real-time fraud, real-time customer 360, in-transaction "
            "risk. Trade-off: licence and hardware cost; not yet a "
            "drop-in for the largest core ledgers.")
        + H3("5.3  Change Data Capture — the connective tissue")
        + p("Almost every modern BFSI data flow uses CDC (Change Data "
            "Capture) to publish row-level changes from the OLTP "
            "database to a streaming bus (Kafka, Pulsar). Tools: "
            "<strong>Debezium</strong> (open source, Postgres / MySQL "
            "/ MongoDB / Db2 / Oracle), <strong>Oracle GoldenGate</strong> "
            "(enterprise, ubiquitous), <strong>IBM InfoSphere CDC</strong>, "
            "<strong>AWS Database Migration Service (DMS)</strong>, "
            "<strong>Striim</strong>, <strong>Qlik Replicate</strong>. "
            "CDC is also the technique behind the strangler-fig "
            "migration off the mainframe.")
        + H3("5.4  The data mesh and federated governance")
        + p("Zhamak Dehghani’s <em>data mesh</em> (2019) reframes data "
            "as a product owned by the domain that produces it: "
            "‘Payments owns the payments data product; Cards owns the "
            "cards data product’. The platform team supplies a "
            "self-service data infrastructure. JPM, ABN AMRO, ANZ, "
            "Saxo Bank, ING are public references. The data mesh "
            "sits naturally on a lakehouse with an open table format.")
        + H3("5.5  AI and the database")
        + ul([
            "<strong>Vector databases</strong> — pgvector (Postgres "
            "extension), Pinecone, Weaviate, Milvus, Chroma, Qdrant. "
            "Used for semantic search, retrieval-augmented generation "
            "(RAG), KYC document Q&A, customer-service copilots.",
            "<strong>Feature stores</strong> — Tecton, Feast, "
            "Databricks Feature Store, Vertex AI Feature Store. "
            "Centralise the ML features so model training and "
            "production inference see the same data.",
            "<strong>In-database ML</strong> — Snowflake Cortex, "
            "BigQuery ML, Oracle Machine Learning. Run inference "
            "where the data lives; avoids moving sensitive data.",
        ])
        + H3("5.6  Backups, disaster recovery, and ransomware")
        + ul([
            "<strong>3-2-1 rule</strong> — 3 copies of the data, 2 "
            "different media, 1 off-site. Still the baseline.",
            "<strong>Immutable backups</strong> — object-locked S3, "
            "Cohesity DataLock, Rubrik, Commvault Air Gap. Required "
            "after the 2021–2024 wave of ransomware attacks.",
            "<strong>Cyber recovery vault</strong> — physically and "
            "logically isolated copy with strict access. Mandated in "
            "spirit by DORA and PRA SS1/21.",
            "<strong>Backup is not DR</strong> — backup answers "
            "‘can I get the data back?’; disaster recovery answers "
            "‘can I run the business while I get it back?’.",
        ])
    )
    return TopicSection(
        "5.  Advanced — encryption, HTAP, CDC, data mesh, AI, backups",
        "advanced", body)


def _sec6() -> TopicSection:
    body = (
        H3("6.1  Picking the right engine for the workload")
        + table(
            ["Workload", "Best engine in 2025", "Why"],
            [
                ["Tier-1 core ledger (incumbent)",
                 "Oracle / Db2 z/OS, sometimes SQL Server",
                 "Battle-tested, regulator-comfortable, decades of "
                 "tooling. Migration risk usually outweighs licence "
                 "savings."],
                ["Greenfield digital bank ledger",
                 "PostgreSQL or distributed-SQL (CockroachDB, "
                 "YugabyteDB, Spanner)",
                 "Open, cheap, horizontally scalable, ACID across "
                 "regions. Form3, Wise, Revolut, GXS pattern."],
                ["Customer 360 read store",
                 "Postgres / MongoDB / DynamoDB",
                 "Document or key-value beats relational for "
                 "customer-shaped, mostly-read aggregates."],
                ["Sessions, rate limits, idempotency keys",
                 "Redis (single-region, with persistence)",
                 "Sub-millisecond reads; widely understood."],
                ["Trade tick / market data",
                 "kdb+ or ClickHouse",
                 "Column-oriented, time-series-native, widely "
                 "deployed on the trading floor."],
                ["Fraud rings, AML networks",
                 "Neo4j / TigerGraph / Neptune",
                 "Graph traversals are O(neighbours); "
                 "relational joins are not."],
                ["Regulatory reporting and analytics",
                 "Snowflake / Databricks / BigQuery on Iceberg or "
                 "Delta",
                 "Massively parallel scans; open table format avoids "
                 "vendor lock-in."],
                ["Real-time fraud scoring on live transactions",
                 "Streaming + feature store + ML + Redis",
                 "Latency budget under 100 ms; only an in-memory "
                 "feature store hits the SLA."],
                ["AI / RAG over policies, contracts, KYC docs",
                 "pgvector or specialised vector DB",
                 "Semantic search at the latency of an HR copilot."],
            ]
        )
        + H3("6.2  Buy vs build for the data platform")
        + ul([
            "<strong>Snowflake vs Databricks vs in-house</strong> — "
            "for analytics, the cost of running your own Spark + "
            "Iceberg + governance stack rarely wins below tier-1 "
            "scale. Most banks pick one or both as primary, "
            "differentiating by team skills (SQL-heavy → Snowflake; "
            "ML / Spark-heavy → Databricks).",
            "<strong>Cloud-managed vs self-managed Postgres</strong> — "
            "cloud-managed wins for time-to-value and "
            "operational burden; self-managed wins where extensions, "
            "exotic configurations or air-gapped operations matter.",
            "<strong>Iceberg + multiple engines</strong> is the new "
            "‘right answer’ for greenfield analytical platforms; "
            "buys portability, defers vendor lock-in.",
        ])
    )
    return TopicSection(
        "6.  Decision matrices — engines, build vs buy, lock-in",
        "intermediate", body)


def _sec7() -> TopicSection:
    body = (
        example(
            "JPMorgan Chase — Athena, Onyx, and the data lakehouse",
            ol([
                "JPM Athena (Python on monorepo, internal RPC) is the "
                "trading and risk platform; Phoenix is the asset-"
                "management equivalent.",
                "Athena’s data layer combines kdb+ for tick data, "
                "Postgres / Cassandra for operational data, "
                "Snowflake / Databricks on AWS for analytical scale.",
                "JPM disclosed in 2023 it runs one of the largest "
                "Snowflake estates outside Snowflake itself; "
                "Iceberg is being adopted to keep storage portable.",
                "Onyx is JPM’s blockchain / digital-assets unit; the "
                "JPM Coin ledger uses a permissioned distributed "
                "ledger with deterministic settlement.",
            ])
        )
        + example(
            "Capital One — open-source Postgres at scale",
            ol([
                "After moving to AWS, Capital One standardised on "
                "PostgreSQL (Aurora) for new transactional workloads, "
                "and on Snowflake for analytics.",
                "Built and open-sourced tooling: Cloud Custodian "
                "(policy as code), Data Profiler (PII detection), "
                "Hygieia (DevOps dashboards).",
                "Lesson: a tier-1 US bank can run on open-source-"
                "centric data engines, with cloud-managed services "
                "removing the operational burden.",
            ])
        )
        + example(
            "Form3 — payments-as-a-service on CockroachDB",
            ol([
                "Form3 operates payments rails (CHAPS, SEPA, FPS, "
                "Bacs, Target2) for banks like Lloyds, Nationwide, "
                "ClearBank.",
                "Picked CockroachDB (Postgres-compatible distributed "
                "SQL) for its multi-region active-active operation: "
                "no failover scripts, automatic re-balancing.",
                "Public reference for ‘distributed SQL is real for "
                "regulated payments’.",
            ])
        )
        + example(
            "An Indian incumbent on Finacle — the modern data layer",
            ol([
                "Finacle runs on Oracle (with some banks running it "
                "on Db2). The OLTP database is the source of truth "
                "for accounts, postings, customer master.",
                "GoldenGate / Debezium streams changes to Kafka.",
                "A lakehouse on AWS Mumbai (or Azure Pune) — S3 + "
                "Iceberg + EMR / Glue / Databricks — holds 7+ years "
                "of analytical data for regulatory reporting (RBI "
                "ADF), risk (RBI Basel III), customer analytics.",
                "PII is tokenised in the lake; the tokens are "
                "rehydrated only inside controlled customer-facing "
                "applications.",
                "DPDP Act 2023 obligations are met through "
                "consent-driven data flows and tokenised analytical "
                "stores.",
            ])
        )
        + example(
            "A capital-markets bank on kdb+",
            ol([
                "Goldman Sachs, Morgan Stanley, JPM, Citadel and most "
                "tier-1 trading floors run kdb+ for tick data — "
                "billions of quotes and trades per day.",
                "kdb+ stores data column-wise on disk in date-"
                "partitioned files; the q query language is "
                "famously terse and famously fast.",
                "Modernisation: KX is integrating with Iceberg / "
                "S3, allowing kdb+ data to participate in the "
                "broader lakehouse without re-loading.",
            ])
        )
    )
    return TopicSection(
        "7.  Worked examples — five real BFSI data architectures",
        "intermediate", body)


def _sec8() -> TopicSection:
    return TopicSection(
        "8.  Questions a leader asks in any data architecture review",
        "basic",
        ol([
            "Where is the system of record for each business object "
            "(accounts, customers, postings, trades, claims)? Is "
            "there exactly one for each?",
            "What is the Recovery Point Objective (RPO) and Recovery "
            "Time Objective (RTO) for each critical database, and "
            "when did we last test failover with a real region "
            "outage?",
            "How is data flowing from OLTP to analytics — CDC + "
            "Kafka + lakehouse, or nightly batch? What is the "
            "latency, and is it good enough for the regulator?",
            "Which open table format have we chosen, and is the "
            "storage portable across engines?",
            "How is PII protected in the lake — tokenisation, "
            "masking, row / column-level security, "
            "differential privacy?",
            "What is our key-management posture — cloud-managed, "
            "BYOK, HYOK / EKM? Who can recover plaintext, under what "
            "process?",
            "What is our database licence run-rate, and what is the "
            "savings plan over the next 3 years (Postgres / "
            "distributed SQL / cloud-managed)?",
            "How do we handle the right-to-be-forgotten / DPDP "
            "erasure requests against immutable ledgers?",
            "Are immutable backups in place, and are they air-gapped "
            "from the production identity domain?",
            "How is the lakehouse governed — Unity Catalog, Snowflake "
            "Horizon, Polaris / Glue Data Catalog, Apache Atlas? Is "
            "lineage end-to-end?",
            "Where do AI features live — feature store, vector DB — "
            "and how do we audit what data trained which model?",
            "What is the data-product owner for each domain in the "
            "data mesh, and do they have an SLO with consumers?",
        ]))


def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘We can scale Oracle forever; no need to think about "
            "Postgres.’ — Run-rate licence cost is the most common "
            "reason a 3-year strategy is rewritten 18 months in.",
            "‘We are cloud-native, so we don’t need DR plans.’ — "
            "Cloud regions fail; cross-region failover is a tested "
            "drill, not a button.",
            "‘Our data lake is the warehouse.’ — A lake without a "
            "table format and a catalogue is a swamp. Iceberg / "
            "Delta + Unity / Polaris / Horizon is what makes it a "
            "lakehouse.",
            "‘We’ll just denormalise into Mongo for everything.’ — "
            "Document stores trade flexibility for transactional "
            "guarantees. The ledger is not a Mongo collection.",
            "‘Backups equal disaster recovery.’ — They don’t. Backup "
            "answers ‘can I restore?’; DR answers ‘can I keep "
            "operating?’.",
            "‘Tokenisation gives us GDPR / DPDP compliance.’ — Only "
            "if tokens cannot be reversed in the analytical "
            "environment. Read the threat model; many tokenisation "
            "deployments leak.",
            "‘We don’t need a data catalogue, the engineers know "
            "where data is.’ — Then auditors and AI agents don’t. "
            "Both are now stakeholders.",
            "‘CDC is just for analytics.’ — CDC is also how you do "
            "the strangler-fig from a mainframe and how you build "
            "real-time fraud. Treat it as a first-class platform.",
            "‘We’ll move to a vector DB just for AI.’ — pgvector in "
            "Postgres is enough for most BFSI use cases below "
            "100M vectors. Don’t take on a new operational engine "
            "without a real reason.",
            "‘Schrems II is solved.’ — Cross-border personal-data "
            "transfers remain legally fragile; the safest design "
            "still keeps PII in-region.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("ACID", "Atomicity, Consistency, Isolation, Durability — "
                "the four properties of a reliable transaction."),
            ("CAP / PACELC", "CAP theorem (Brewer 2000): pick 2 of "
                "Consistency, Availability, Partition tolerance under "
                "partition. PACELC adds the latency-vs-consistency "
                "trade-off when there is no partition."),
            ("OLTP / OLAP", "Online Transaction Processing / Online "
                "Analytical Processing — fast small writes vs large "
                "scans."),
            ("HTAP", "Hybrid TP/AP engines that try to do both on one "
                "store (HANA, SingleStore, Unistore, AlloyDB, TiDB)."),
            ("WAL / redo log", "Write-Ahead Log — durability mechanism "
                "in relational databases."),
            ("RAC / Data Guard / GoldenGate", "Oracle clustering, "
                "replication, CDC tooling."),
            ("HADR", "High Availability Disaster Recovery — Db2’s "
                "primary-replica replication."),
            ("NewSQL / distributed SQL", "Horizontally scalable, ACID "
                "SQL databases (CockroachDB, YugabyteDB, Spanner, "
                "TiDB)."),
            ("Sharding", "Horizontal partitioning of data across "
                "nodes by key."),
            ("CDC", "Change Data Capture — emit row-level changes "
                "from a database to a stream."),
            ("Data lake / lakehouse", "Lake = files on object "
                "storage; lakehouse = lake + open table format + "
                "ACID + catalogue."),
            ("Iceberg / Delta / Hudi", "Open table formats that turn "
                "object storage into a transactional store."),
            ("Snowflake / Databricks / BigQuery / Redshift / Fabric",
             "Major analytical engines."),
            ("kdb+ / q", "Column-store and language for tick data; "
                "ubiquitous in capital markets."),
            ("Vector database", "Stores embeddings for similarity "
                "search; pgvector, Pinecone, Weaviate, Milvus, "
                "Chroma, Qdrant."),
            ("Feature store", "Centralised store of ML features "
                "shared between training and inference (Tecton, "
                "Feast, Databricks, Vertex)."),
            ("Tokenisation / FPE", "Replace sensitive values with "
                "tokens / format-preserving encrypted values; "
                "Voltage, Protegrity, Thales CipherTrust."),
            ("WORM", "Write-Once Read-Many storage required by "
                "SEC 17a-4(f) and similar rules."),
            ("3-2-1 backup", "3 copies, 2 media, 1 off-site — "
                "minimum baseline."),
            ("Data mesh", "Domain-aligned ownership of analytical "
                "data products (Dehghani, 2019)."),
            ("Unity Catalog / Polaris / Horizon / Glue Data Catalog",
             "Governance and lineage layers over the lakehouse."),
            ("RPO / RTO", "Recovery Point Objective (data-loss "
                "tolerance) / Recovery Time Objective (downtime "
                "tolerance)."),
            ("Cyber recovery vault", "Isolated, immutable copy of "
                "critical data for ransomware recovery."),
            ("BYOK / HYOK / EKM", "Bring / Hold Your Own Key / "
                "External Key Manager — increasing customer control "
                "of encryption keys."),
            ("Schrems II", "2020 CJEU ruling restricting personal "
                "data flows from EU to non-adequate jurisdictions."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
