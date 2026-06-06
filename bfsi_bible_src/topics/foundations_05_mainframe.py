"""Foundations · 05 — Mainframe modernisation (COBOL, IBM Z, encapsulation strategies)."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="I.5",
        slug="05-mainframe-modernisation",
        title="Mainframe modernisation — COBOL, IBM Z, and encapsulation strategies",
        one_liner=(
            "The world's largest banks still run their most critical workloads on IBM Z "
            "mainframes, often in COBOL code written decades ago. These systems process "
            "trillions of dollars daily and are not going away. But they are being modernised "
            "— not replaced. This topic teaches you what a mainframe actually is, why it "
            "persists, and the strategies banks use to modernise around it."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


# ------------------------------------------------------------------ 0
def _sec0() -> TopicSection:
    body = (
        primer(
            p("Mainframes are the most misunderstood technology in BFSI. People assume they "
              "are ancient, slow, and obsolete. In reality, modern IBM Z mainframes are the "
              "fastest, most reliable, and most secure commercial computers on earth. A single "
              "z16 can process 300 billion inference operations per day. The challenge is not "
              "performance — it is talent, cost, agility, and integration with modern cloud "
              "ecosystems.")
        )
        + H3("0.1  IT-side anchor — the engine block in a car")
        + it_anchor(
            p("Think of a car that has been running reliably for 40 years. The engine is "
              "perfect — powerful, efficient, never breaks down. But the dashboard is "
              "analogue, the GPS does not exist, and the body is rusting. You have two choices: "
              "buy a new car (risky, expensive, the new engine might be worse) or keep the "
              "engine and modernise everything around it (new dashboard, GPS, body panels). "
              "Most banks choose the second path for their mainframes: keep the core engine, "
              "modernise the interfaces.")
        )
        + H3("0.2  BFSI-side anchor — the ATM you use every day")
        + bfsi_anchor(
            p("When you withdraw cash from a JPMorgan Chase, Wells Fargo, Bank of America, "
              "or State Bank of India ATM, the transaction is processed by a mainframe. When "
              "you swipe your Citi credit card, the authorisation flows through mainframe "
              "code. These are not legacy accidents — they are deliberate architecture "
              "choices. The mainframe handles the transaction volume, the security (pervasive "
              "encryption), and the reliability (99.999%+ uptime) that no distributed system "
              "has yet matched at this scale.")
        )
        + H3("0.3  Scale of mainframe usage in BFSI")
        + ul([
            "<strong>92 of the world's top 100 banks</strong> use IBM Z mainframes.",
            "<strong>$8 trillion+ in daily transactions</strong> flow through mainframes globally.",
            "<strong>~220 billion lines of COBOL</strong> are still in production worldwide.",
            "The US Federal Reserve, DTCC (Depository Trust and Clearing Corporation), "
            "and SWIFT all run critical workloads on mainframes.",
            "In India, SBI's core banking on TCS BaNCS runs partially on IBM Z infrastructure.",
        ])
    )
    return TopicSection("0.  Primer — anchored to things you already know", "basic", body)


# ------------------------------------------------------------------ 1
def _sec1() -> TopicSection:
    body = (
        p("Mainframes persist in BFSI for five reasons that no distributed system has fully "
          "addressed:")
        + ol([
            "<strong>Transactional throughput.</strong> A single IBM z16 processes tens of "
            "thousands of transactions per second with sub-millisecond latency, with hardware "
            "transactional memory ensuring ACID guarantees. Distributed systems achieve "
            "similar throughput but with higher latency variance and more complex failure "
            "modes.",
            "<strong>Reliability.</strong> IBM Z hardware is designed for 99.999% uptime "
            "(5.26 minutes of downtime per year). Hot-swappable components, redundant "
            "processors, and Parallel Sysplex clustering provide continuous availability "
            "that cloud providers approximate but rarely guarantee at the application level.",
            "<strong>Security.</strong> IBM z16 introduced on-chip AI inference for real-time "
            "fraud detection and pervasive encryption (encrypt everything at the hardware "
            "level with no performance penalty). FIPS 140-2 Level 4 certification (the "
            "highest level, requiring physical tamper response) is unique to IBM Z.",
            "<strong>Regulatory trust.</strong> Regulators know mainframes. Decades of audit "
            "history, proven disaster-recovery patterns (GDPS — Geographically Dispersed "
            "Parallel Sysplex), and well-understood operational procedures give regulators "
            "comfort that distributed alternatives must earn.",
            "<strong>Code maturity.</strong> COBOL applications that have run for 30+ years "
            "have had every edge case found and fixed. Rewriting them introduces new bugs "
            "in code that handles trillions of dollars. The risk of rewrite is often higher "
            "than the risk of keeping the mainframe.",
        ])
    )
    return TopicSection("1.  Why mainframes persist — first principles", "basic", body)


# ------------------------------------------------------------------ 2
def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart TB\n'
            '  subgraph "Modern Channels"\n'
            '    MOB["Mobile app"]\n'
            '    WEB["Web banking"]\n'
            '    API["Open Banking APIs"]\n'
            '    UPI["UPI / FedNow / FPS"]\n'
            '  end\n'
            '  subgraph "Integration Layer"\n'
            '    GW["API Gateway"]\n'
            '    MQ["MQ / Kafka bridge"]\n'
            '    CICS["CICS Transaction Server"]\n'
            '  end\n'
            '  subgraph "Mainframe Core"\n'
            '    COB["COBOL business logic"]\n'
            '    DB2["Db2 / IMS databases"]\n'
            '    BAT["Batch: JCL + COBOL"]\n'
            '    SEC["RACF security"]\n'
            '  end\n'
            '  subgraph "Cloud / Distributed"\n'
            '    K8S["Kubernetes workloads"]\n'
            '    DW["Data lake / warehouse"]\n'
            '    AI["AI/ML inference"]\n'
            '    CLD["Cloud-native apps"]\n'
            '  end\n'
            '  MOB --> GW\n'
            '  WEB --> GW\n'
            '  API --> GW\n'
            '  UPI --> GW\n'
            '  GW --> CICS\n'
            '  GW --> MQ\n'
            '  MQ --> K8S\n'
            '  CICS --> COB --> DB2\n'
            '  BAT --> DB2\n'
            '  SEC --> COB\n'
            '  DB2 -->|"CDC / replication"| DW\n'
            '  DW --> AI\n'
            '  K8S --> CLD',
            "The encapsulation pattern: modern channels and cloud workloads wrap around the mainframe core.")
    )
    return TopicSection("2.  The modernisation picture — encapsulate, not replace", "basic", body)


# ------------------------------------------------------------------ 3
def _sec3() -> TopicSection:
    body = (
        H3("3.1  The mainframe technology stack")
        + table(
            ["Component", "What it does", "Modern equivalent (approximate)"],
            [
                ["<strong>COBOL</strong>", "Business logic language. Verbose, decimal-native "
                 "(crucial for financial arithmetic), compiled to highly optimised machine code.",
                 "Java, C#, Go — but none have COBOL's decimal precision by default"],
                ["<strong>PL/I</strong>", "IBM's general-purpose language. Used alongside "
                 "COBOL in many banks.", "C/C++"],
                ["<strong>JCL (Job Control Language)</strong>", "Batch job scheduling and "
                 "execution. Defines what programs to run, in what order, with what data.",
                 "Airflow, Control-M, cron"],
                ["<strong>CICS</strong>", "Online transaction processing monitor. Routes "
                 "incoming requests to COBOL programs, manages transactions.",
                 "Application server (Tomcat, Node.js) + transaction manager"],
                ["<strong>IMS</strong>", "Hierarchical database and transaction manager. "
                 "Very fast for known access patterns.",
                 "MongoDB (hierarchical), though IMS is faster for fixed patterns"],
                ["<strong>Db2 for z/OS</strong>", "Relational database optimised for "
                 "mainframe I/O. Shares memory with COBOL programs for extreme performance.",
                 "PostgreSQL, Oracle — but Db2 z/OS has unique co-location advantages"],
                ["<strong>RACF</strong>", "Resource Access Control Facility. Security and "
                 "identity management for the mainframe.",
                 "Active Directory, IAM — but RACF is more granular at the dataset level"],
                ["<strong>VSAM</strong>", "Virtual Storage Access Method. Flat-file data "
                 "storage used by COBOL programs.",
                 "Key-value stores, but VSAM is tightly integrated with batch processing"],
                ["<strong>MQ (IBM MQ)</strong>", "Message queuing for asynchronous "
                 "communication between mainframe and distributed systems.",
                 "Kafka, RabbitMQ — but MQ has deep CICS/Db2 integration"],
            ]
        )

        + H3("3.2  How a mainframe transaction actually flows")
        + ol([
            "A customer taps 'Transfer ₹10,000' on the mobile app.",
            "The API gateway routes the request to the integration layer.",
            "The integration layer places a message on IBM MQ (or calls CICS directly "
            "via a CICS Transaction Gateway).",
            "CICS receives the message, starts a transaction, and invokes the COBOL "
            "transfer program.",
            "The COBOL program reads the sender's account from Db2, checks the balance, "
            "debits ₹10,000, credits the recipient's account, posts GL entries, and "
            "commits the Db2 transaction.",
            "CICS returns a success response via MQ to the API gateway.",
            "The mobile app shows 'Transfer successful'.",
            "At end of day, batch jobs (JCL + COBOL) accrue interest, generate statements, "
            "and produce regulatory files.",
        ])

        + H3("3.3  The five modernisation strategies")
        + table(
            ["Strategy", "What it means", "Risk / Reward"],
            [
                ["<strong>Encapsulate (API-wrap)</strong>",
                 "Keep COBOL as-is. Expose mainframe functions as REST/gRPC APIs via CICS "
                 "Transaction Gateway, IBM z/OS Connect, or MQ bridges. New channels and "
                 "cloud apps call these APIs.",
                 "Lowest risk. Fastest. Does not reduce mainframe MIPS cost. The default "
                 "strategy for most tier-1 banks."],
                ["<strong>Replatform</strong>",
                 "Move COBOL code off IBM Z to run on x86 Linux using emulation or "
                 "recompilation (Micro Focus, LzLabs, Heirloom). Same code, different hardware.",
                 "Reduces hardware cost but introduces runtime compatibility risk. Batch "
                 "performance often degrades. Suitable for non-critical workloads."],
                ["<strong>Refactor</strong>",
                 "Gradually rewrite COBOL programs in Java, C#, or Go while maintaining "
                 "functional equivalence. Often done module by module.",
                 "High effort, high risk. Requires deep COBOL expertise to ensure functional "
                 "parity. Multi-year programmes. Commonwealth Bank of Australia is the "
                 "most-cited success (moved to SAP on Java over 5 years)."],
                ["<strong>Replace</strong>",
                 "Replace the mainframe application entirely with a modern platform "
                 "(e.g., cloud-native core banking: Thought Machine, 10x, Mambu).",
                 "Highest risk. Only viable for greenfield (new bank, new geography) or "
                 "strangler-fig migration. JPM Chase UK is an example (new geography on "
                 "Vault Core, not a migration of the US mainframe)."],
                ["<strong>AI-assisted conversion</strong>",
                 "Use GenAI to translate COBOL to Java/Python, then human-review. IBM "
                 "Watsonx Code Assistant for Z, AWS Mainframe Modernization (Blu Age), "
                 "Google Cloud Mainframe Modernization.",
                 "Emerging. Reduces manual effort by 30-60% (vendor claims). Translation "
                 "quality varies; critical business logic still requires human validation. "
                 "Best used for understanding and documentation, not blind conversion."],
            ]
        )
    )
    return TopicSection("3.  How it actually works — the stack, the flow, the strategies",
                        "intermediate", body)


# ------------------------------------------------------------------ 4
def _sec4() -> TopicSection:
    body = (
        H3("4.1  Mainframe cost structure — MIPS and MSU")
        + p("Mainframe costs are driven by <strong>MIPS</strong> (Million Instructions Per "
            "Second) or <strong>MSU</strong> (Million Service Units) — IBM's capacity metric. "
            "Banks pay IBM (or third-party lessors) for the hardware capacity they consume. "
            "Software licences (Db2, CICS, MQ, RACF, ISV tools) are also priced by MSU. "
            "A tier-1 bank may spend $200–500M/year on mainframe hardware, software, and "
            "operations combined.")
        + p("This 'MIPS tax' is the primary economic driver of modernisation. Every transaction "
            "that moves off the mainframe reduces MSU consumption and cost. But the fixed costs "
            "(floor space, cooling, staff, licences with minimum commitments) do not drop "
            "proportionally until a significant volume moves off.")

        + H3("4.2  The COBOL talent crisis")
        + p("The average COBOL programmer is over 55 years old. Universities stopped teaching "
            "COBOL decades ago. Banks face a structural talent shortage that will intensify "
            "through the 2030s. This is not hypothetical — it is the single most-cited risk "
            "in mainframe strategy discussions at tier-1 banks.")
        + p("Responses to the talent crisis:")
        + ul([
            "<strong>Internal training programmes</strong> — some banks (e.g., Barclays, BNY "
            "Mellon) have created COBOL academies to train new graduates.",
            "<strong>AI-assisted code understanding</strong> — tools like IBM Watsonx, "
            "GitHub Copilot (trained on COBOL), and vendor-specific analysers help new "
            "engineers understand legacy code faster.",
            "<strong>Managed services</strong> — outsourcing mainframe operations to SIs "
            "(HCLTech, TCS, Infosys, Kyndryl, DXC) who maintain COBOL talent pools.",
            "<strong>Accelerated migration</strong> — converting COBOL to Java/Go reduces "
            "future COBOL dependency, but the conversion itself requires COBOL experts.",
        ])

        + H3("4.3  Mainframe vs cloud — a nuanced comparison")
        + table(
            ["Dimension", "Mainframe (IBM Z)", "Cloud (AWS/Azure/GCP)"],
            [
                ["Throughput", "Tens of thousands TPS, sub-ms latency, hardware ACID",
                 "Similar TPS achievable but higher latency variance, software ACID"],
                ["Availability", "99.999%+ with Parallel Sysplex, GDPS",
                 "99.95–99.99% per region (SLA); multi-region adds complexity"],
                ["Security", "Pervasive encryption, FIPS 140-2 Level 4, RACF",
                 "Envelope encryption, FIPS 140-2 Level 2–3, IAM"],
                ["Cost model", "CapEx + MSU licence; high fixed, low marginal",
                 "OpEx / pay-as-you-go; low fixed, higher marginal at scale"],
                ["Agility", "Waterfall-oriented tooling; CI/CD possible but not native",
                 "DevOps-native; CI/CD, IaC, containers standard"],
                ["Talent", "Shrinking COBOL pool; expensive specialists",
                 "Large, growing pool; competitive hiring market"],
                ["Regulator comfort", "Decades of audit history; well-understood",
                 "Growing but still scrutinised; exit plans required"],
            ]
        )
    )
    return TopicSection("4.  Types and variations — costs, talent, and the cloud comparison",
                        "intermediate", body)


# ------------------------------------------------------------------ 5
def _sec5() -> TopicSection:
    body = (
        H3("5.1  z/OS Connect — the API gateway for the mainframe")
        + p("z/OS Connect is IBM's strategic product for exposing mainframe programs as "
            "RESTful APIs. It sits on the mainframe itself, invokes CICS transactions or "
            "IMS programs, and exposes them as OpenAPI-compliant endpoints. This is the "
            "cornerstone of the 'encapsulate' strategy — it turns every COBOL program into "
            "a callable service without changing a line of COBOL.")

        + H3("5.2  Change Data Capture (CDC) — getting data off the mainframe")
        + p("One of the biggest modernisation challenges is getting mainframe data into cloud "
            "data lakes and warehouses in near-real-time. CDC tools capture changes from Db2 "
            "or VSAM as they happen and stream them to Kafka, S3, or cloud databases.")
        + ul([
            "<strong>IBM InfoSphere Data Replication</strong> — native CDC for Db2 z/OS.",
            "<strong>Precisely Connect (formerly Syncsort)</strong> — widely used for "
            "mainframe-to-cloud data movement.",
            "<strong>Attunity / Qlik Replicate</strong> — supports Db2, IMS, VSAM sources.",
            "<strong>AWS DMS (Database Migration Service)</strong> — supports Db2 z/OS as a source.",
        ])

        + H3("5.3  Batch modernisation — the overnight window problem")
        + p("Many mainframe banks still have a nightly batch window (2–6 hours) during which "
            "online services are degraded or unavailable. Interest accrual, statement "
            "generation, GL posting, regulatory file production, and data warehouse loading "
            "all happen in batch. Modernisation strategies include:")
        + ul([
            "<strong>Batch compression</strong> — optimising JCL job flows, parallelising "
            "independent steps, eliminating unnecessary sorts and copies.",
            "<strong>Micro-batch / streaming</strong> — replacing nightly batch with "
            "continuous processing (CDC + Kafka + streaming consumers).",
            "<strong>Offloading non-critical batch</strong> — moving reporting, analytics, "
            "and data warehouse loading to cloud, keeping only ledger-critical batch on "
            "the mainframe.",
            "<strong>IBM Z Integrated Information Processor (zIIP)</strong> — a specialised "
            "processor that runs Java, XML, and analytics workloads at no MSU cost, reducing "
            "the economic incentive to move these off the mainframe.",
        ])

        + H3("5.4  Parallel Sysplex and GDPS — mainframe resilience at depth")
        + p("Parallel Sysplex is IBM's clustering technology that allows multiple z/OS "
            "images to share data (via a Coupling Facility) and process transactions "
            "simultaneously. GDPS (Geographically Dispersed Parallel Sysplex) extends this "
            "across data centres. Together, they deliver continuous availability and "
            "automated disaster recovery that is the benchmark for mission-critical "
            "systems. Understanding these is essential for any architect working on "
            "mainframe resilience or DR strategy.")
    )
    return TopicSection("5.  Advanced — z/OS Connect, CDC, batch modernisation, resilience",
                        "advanced", body)


# ------------------------------------------------------------------ 6
def _sec6() -> TopicSection:
    body = (
        p("Mainframe strategy is heavily shaped by regulatory expectations around resilience, "
          "audit, and operational risk.")
        + table(
            ["Region", "Mainframe landscape", "Regulator considerations"],
            [
                ["<strong>United States</strong>",
                 "JPM Chase, Wells Fargo, BoA, Citi, BNY Mellon, US Federal Reserve, DTCC "
                 "all run critical workloads on IBM Z. The US is the largest mainframe market.",
                 "OCC/Fed examiners understand mainframes deeply. Modernisation proposals are "
                 "scrutinised for operational risk. FFIEC IT Handbook covers legacy system "
                 "management."],
                ["<strong>India</strong>",
                 "SBI (partial), BoB, Canara Bank have mainframe heritage. Many have migrated "
                 "to Finacle/BaNCS on Unix/Linux, but mainframe components remain for cards, "
                 "payments switching, and certain back-office functions.",
                 "RBI IT Governance MD (Nov 2023) requires banks to address legacy technology "
                 "risk. RBI expects documented modernisation roadmaps for ageing platforms."],
                ["<strong>United Kingdom</strong>",
                 "Lloyds, Barclays, NatWest, HSBC all have significant mainframe estates. "
                 "Lloyds is the most-cited modernisation case (Thought Machine migration).",
                 "PRA Operational Resilience (fully embedded March 2025) requires impact "
                 "tolerance testing that includes mainframe failure scenarios. UK CTP regime "
                 "may designate IBM as a critical third party."],
                ["<strong>Eurozone</strong>",
                 "Deutsche Bank, BNP Paribas, Societe Generale, ING have large mainframe "
                 "estates. European banks tend to favour the encapsulate strategy.",
                 "DORA (January 2025) ICT risk management framework covers legacy systems. "
                 "ECB/SSM expects documented legacy technology strategies."],
                ["<strong>Singapore / APAC</strong>",
                 "DBS, OCBC have modernised away from mainframes (DBS notably moved to "
                 "cloud-native). ANZ, Westpac in Australia retain significant mainframe.",
                 "MAS Technology Risk Management Guidelines expect banks to manage legacy "
                 "technology risk. APRA CPS 230 (July 2025) covers operational risk including "
                 "legacy systems."],
            ]
        )
    )
    return TopicSection("6.  Region-by-region mainframe landscape", "advanced", body)


# ------------------------------------------------------------------ 7
def _sec7() -> TopicSection:
    return TopicSection(
        "7.  Trade-offs and decisions a leader owns", "intermediate",
        table(
            ["Decision", "Trade-offs and considerations"],
            [
                ["<strong>Encapsulate vs replatform vs refactor</strong>",
                 "Encapsulate is safest and fastest but does not reduce MIPS cost. Replatform "
                 "reduces hardware cost but introduces runtime risk. Refactor is highest effort "
                 "but yields the most modern codebase. Most banks use encapsulate as the "
                 "default and selectively refactor high-value modules."],
                ["<strong>AI-assisted COBOL conversion</strong>",
                 "Promising but immature. Use for code comprehension and documentation first. "
                 "For actual conversion, validate every module against regression tests. "
                 "Do not trust blind AI translation for code that moves money."],
                ["<strong>Managed services vs in-house mainframe operations</strong>",
                 "Outsourcing to Kyndryl, HCLTech, TCS, or DXC preserves access to COBOL "
                 "talent and operational expertise. But it creates vendor dependency on a "
                 "shrinking skill set. Negotiate knowledge transfer and documentation clauses."],
                ["<strong>zIIP exploitation vs offloading to cloud</strong>",
                 "zIIP-eligible workloads (Java, analytics, XML) run on the mainframe at no "
                 "MSU cost. Moving them to cloud may increase total cost. Analyse the TCO "
                 "before assuming cloud is cheaper."],
                ["<strong>Batch window reduction vs elimination</strong>",
                 "Reducing the batch window (compression, parallelisation) is low-risk and "
                 "delivers quick wins. Eliminating it entirely (streaming, event sourcing) "
                 "requires re-architecting the posting engine and is a multi-year programme."],
            ]
        )
    )


# ------------------------------------------------------------------ 8
def _sec8() -> TopicSection:
    body = (
        example("Commonwealth Bank of Australia — the most-cited mainframe migration",
            p("CBA replaced its mainframe core banking system with SAP's banking platform "
              "over 5 years (2008–2013), at a cost of ~A$1.5 billion. It is one of the few "
              "tier-1 banks to have completed a full core migration off the mainframe. "
              "Lessons: it required unwavering board commitment, a dedicated programme of "
              "thousands of people, and the willingness to accept short-term operational "
              "risk. CBA's digital leadership in the Australian market is partly attributed "
              "to this decision. But few other tier-1 banks have attempted to replicate it.")
        )
        + example("JPMorgan Chase — encapsulation at scale",
            p("JPMC runs one of the world's largest mainframe estates. Rather than replace, "
              "JPMC has invested heavily in API-wrapping mainframe functions (z/OS Connect, "
              "CICS Transaction Gateway), building a modern cloud layer (internal cloud "
              "platform on AWS and private cloud) that calls mainframe services via APIs. "
              "New products and channels are cloud-native; the mainframe remains the "
              "transaction engine. Lesson: encapsulation works at the largest scale if "
              "the API layer is well-designed and the cloud platform is mature.")
        )
        + example("A bank's COBOL-to-Java conversion goes wrong",
            p("A European bank attempted to convert a COBOL interest-calculation module to "
              "Java using automated tools. The converted code passed unit tests but failed "
              "in production because COBOL's native decimal arithmetic (COMP-3) handled "
              "rounding differently than Java's double-precision floating point. The bank "
              "discovered the discrepancy when GL reconciliation failed on the first month-end. "
              "Lesson: COBOL's decimal arithmetic is not a legacy quirk — it is a feature. "
              "Any conversion must use Java's BigDecimal or equivalent, and must be validated "
              "against production GL reconciliation, not just unit tests.")
        )
        + example("HCLTech mainframe services — the managed services model",
            p("HCLTech manages mainframe operations for multiple global banks, providing "
              "COBOL development, batch operations, capacity planning, and modernisation "
              "advisory. The model works because HCLTech maintains a talent pool of COBOL "
              "and z/OS engineers that individual banks struggle to sustain. Lesson: managed "
              "services are a pragmatic response to the COBOL talent crisis, but banks must "
              "retain enough internal expertise to govern the vendor and make architectural "
              "decisions.")
        )
    )
    return TopicSection("8.  Worked examples — four real mainframe stories",
                        "intermediate", body)


# ------------------------------------------------------------------ 9
def _sec9() -> TopicSection:
    body = (
        H3("Questions a leader asks in any mainframe modernisation review")
        + ol([
            "What is our current MIPS/MSU consumption, and what is the 3-year trend?",
            "What percentage of our mainframe workload is batch vs online?",
            "Do we have a documented inventory of every COBOL program, its business function, "
            "and its last-modified date?",
            "What is our COBOL talent pipeline — internal, vendor, and market availability?",
            "Which mainframe functions have been API-wrapped, and which remain accessible "
            "only via batch or screen-scraping?",
            "What is the TCO comparison: mainframe vs replatformed vs cloud-native, for our "
            "top-5 workloads?",
            "What is our batch window duration, and which jobs are on the critical path?",
            "Do we have CDC in place to stream mainframe data to cloud, or are we still "
            "doing nightly file transfers?",
        ])
        + red_flag(ul([
            "'Let's just rewrite the mainframe in Java.' — COBOL-to-Java rewrites at tier-1 "
            "scale take 5–10 years and cost billions. The risk of introducing bugs in code "
            "that processes trillions of dollars is enormous. Encapsulate first, refactor "
            "selectively.",
            "'Mainframes are obsolete.' — They process more transactions per day than all "
            "public clouds combined. They are the most reliable and secure commercial "
            "computers. 'Obsolete' is a talent and agility problem, not a technology problem.",
            "'We can save money by moving everything to cloud.' — Mainframe cost is heavily "
            "fixed (hardware leases, minimum software commitments). Moving 20% of workload "
            "to cloud may increase total cost if the fixed costs do not drop. Model the TCO "
            "honestly.",
            "'AI can convert our COBOL automatically.' — AI-assisted conversion is a "
            "productivity tool, not a magic wand. Every converted module needs human review, "
            "especially for decimal arithmetic, transaction boundaries, and error handling. "
            "Trust but verify.",
            "'Nobody needs to understand the COBOL — just wrap it in APIs.' — API-wrapping "
            "without understanding the underlying business logic creates a fragile system. "
            "When the COBOL breaks, someone must debug it. Document and understand first.",
            "'The mainframe vendor says we need more MIPS.' — Verify with independent "
            "capacity planning. zIIP exploitation, batch optimisation, and workload "
            "offloading can reduce MIPS growth without hardware upgrades.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("IBM Z / z16", "IBM's current mainframe hardware platform. z16 (2022) "
             "includes on-chip AI inference and quantum-safe cryptography."),
            ("COBOL", "Common Business-Oriented Language — the dominant programming language "
             "on mainframes, designed in 1959 for business applications."),
            ("CICS", "Customer Information Control System — IBM's online transaction "
             "processing monitor for mainframes."),
            ("Db2 z/OS", "IBM's relational database for z/OS, optimised for mainframe I/O "
             "and co-located with COBOL programs."),
            ("IMS", "Information Management System — IBM's hierarchical database and "
             "transaction manager."),
            ("JCL", "Job Control Language — the scripting language for mainframe batch jobs."),
            ("MIPS / MSU", "Million Instructions Per Second / Million Service Units — "
             "mainframe capacity metrics that drive licensing costs."),
            ("RACF", "Resource Access Control Facility — mainframe security and identity "
             "management."),
            ("VSAM", "Virtual Storage Access Method — flat-file storage used by COBOL programs."),
            ("Parallel Sysplex", "IBM's mainframe clustering technology for continuous "
             "availability and horizontal scaling."),
            ("GDPS", "Geographically Dispersed Parallel Sysplex — disaster recovery "
             "technology for cross-site mainframe clustering."),
            ("z/OS Connect", "IBM's API gateway for exposing mainframe programs as "
             "RESTful APIs."),
            ("CDC", "Change Data Capture — technology that captures database changes in "
             "real-time and streams them to downstream systems."),
            ("zIIP", "z Integrated Information Processor — specialised mainframe processor "
             "for Java, XML, and analytics workloads at no MSU cost."),
            ("Encapsulate", "Modernisation strategy: wrap mainframe functions in APIs "
             "without changing the underlying code."),
            ("Replatform", "Modernisation strategy: move mainframe code to x86 Linux "
             "via emulation or recompilation."),
            ("COMP-3", "COBOL packed decimal data type — stores decimal numbers exactly, "
             "critical for financial arithmetic."),
        ])
    )
    return TopicSection("9.  Questions, red flags, and glossary", "basic", body)
