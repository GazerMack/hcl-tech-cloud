"""Data · III.2 — Streaming data and event-driven architecture, deep rewrite."""
from __future__ import annotations

from ..site import (
    H3, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    sections: list[TopicSection] = [
        _sec0(),
        _sec1(),
        _sec2(),
        _sec3(),
        _sec4(),
        _sec5(),
        _sec6(),
        _sec7(),
        _sec8(),
        _sec9(),
        _sec10(),
    ]
    return TopicPage(
        code="III.2",
        slug="02-streaming-data-event-driven-architecture",
        title="Streaming data and event-driven architecture — Kafka, Flink, and real-time BFSI",
        one_liner=(
            "A bank used to learn what happened yesterday by reading yesterday's batch files. "
            "Modern BFSI platforms increasingly need to react while the event is still warm: a card "
            "swipe needs fraud scoring in 150 milliseconds, a UPI failure needs instant customer "
            "status, a sanctions alert must hold a payment before release, and a risk desk needs a "
            "market move before the close. This topic builds streaming from zero — events, logs, "
            "Kafka, Flink, exactly-once claims, event-driven architecture, operational risk, and the "
            "questions a BFSI leader asks before trusting real-time pipelines. <em>This topic is now "
            "complete across Sections 0–10.</em>"
        ),
        sections=sections,
    )


def _wip_banner() -> str:
    return callout(
        "Deep-build complete",
        p("You are reading Topic III.2 with Sections 0 through 10 complete at the new depth bar. "
          "The topic was intentionally built in batches so each concept could be taught slowly "
          "rather than keyword-crammed."),
        "info")


def _sec0() -> TopicSection:
    body = (
        _wip_banner()
        + primer(
            p("Before naming Kafka, Flink, Pulsar, Kinesis or event sourcing, start with the problem. "
              "A bank is not one computer. It is hundreds or thousands of systems trying to keep up "
              "with facts that happen all day: a customer logs in, a card is authorised, a payment is "
              "debited, an ATM runs low on cash, a market price changes, a fraud model raises a score, "
              "a branch uploads a Know Your Customer document, a regulator asks for evidence. If every "
              "system waits for tomorrow's file, the bank is always late. Streaming data is the discipline "
              "of carrying those facts across the bank while they are still useful.")
        )
        + H3("0.1  IT-side anchor — your phone notifications")
        + it_anchor(
            p("Think about a food-delivery app. You do not refresh a spreadsheet every morning to learn "
              "that your order moved from accepted to cooking to out for delivery. The restaurant app, "
              "delivery partner app, payment system and your phone all react to small facts as they happen. "
              "Those facts are <strong>events</strong>: order accepted, rider assigned, payment captured, "
              "rider reached gate. An event is not a database table and not a screen. It is a message saying "
              "something meaningful happened at a particular time.")
        )
        + analogy(
            p("A traditional batch system is like a school noticeboard updated once at 5 p.m. Everyone "
              "learns the day's news together, but too late to act during the day. A streaming system is "
              "like the school bell plus classroom announcements: small signals go out immediately to the "
              "people who need them. The bell does not replace the official register, but it lets the school "
              "coordinate in real time.")
        )
        + table(
            ["Everyday thing", "Streaming equivalent", "Why it matters"],
            [
                ["Your phone receives a payment notification", "A payment event was published to interested systems", "Fraud, customer service and analytics can react without waiting for a batch."],
                ["A delivery app changes order status", "An event records a state change", "Many screens and services stay aligned without every service owning the whole database."],
                ["A stock-price ticker updates", "A continuous stream of market events", "Risk systems can revalue positions while the market is moving."],
                ["A smoke alarm rings immediately", "A high-priority event triggers action", "Some events are valuable only if acted on before damage spreads."],
            ]
        )
        + H3("0.2  BFSI-side anchor — why yesterday's file is no longer enough")
        + bfsi_anchor(
            p("Imagine a customer uses a debit card in London at 10:00:00 for £92.50. By 10:00:01, the "
              "card processor, fraud engine, core account system, mobile-notification service, merchant "
              "acquirer and customer-support system may all need to know something happened. If the bank "
              "waits until a 2 a.m. batch file, fraud may be gone, the customer may see stale balance, and "
              "support may say ‘we cannot see it yet’. Real-time banking starts when important facts are "
              "published as events close to the moment they occur.")
        )
        + example("One debit-card authorisation as events",
            ol([
                "At 10:00:00.000, a customer taps a card for £92.50 at a supermarket terminal.",
                "At 10:00:00.040, the acquirer sends an authorisation request through the card network.",
                "At 10:00:00.090, the issuing bank receives the request and creates an internal event: <code>card_authorisation_requested</code> with card token, amount, merchant category and location.",
                "At 10:00:00.120, the fraud service consumes the event, checks device and spending history, and returns a risk score of 18 out of 100.",
                "At 10:00:00.150, the account service places a £92.50 hold and emits <code>available_balance_reserved</code>.",
                "At 10:00:00.180, the bank approves the transaction and emits <code>card_authorisation_approved</code>.",
                "At 10:00:00.250, the mobile app notification service consumes the approval event and sends ‘Card purchase £92.50 at GreenMart’. Customer support can now see the pending authorisation.",
            ])
        )
        + H3("0.3  The first vocabulary: event, stream, topic and consumer")
        + p("Four words carry most of the topic. An <strong>event</strong> is one fact that happened. "
            "A <strong>stream</strong> is many events over time. A <strong>topic</strong> is a named lane "
            "where similar events are placed, such as <code>payments.authorised</code> or "
            "<code>cards.fraud-alerts</code>. A <strong>consumer</strong> is a system that reads events "
            "from a topic and does something: update a screen, score fraud, write to a lakehouse, send a "
            "notification, or create a case.")
        + mermaid(
            "flowchart LR\n"
            "  A[Card transaction happens] --> B[Event created]\n"
            "  B --> C[Topic cards authorisations]\n"
            "  C --> D[Fraud consumer]\n"
            "  C --> E[Notification consumer]\n"
            "  C --> F[Customer support view]\n"
            "  C --> G[Lakehouse ingestion]",
            "Figure 0.1 — One event can serve many consumers without each consumer calling the card system directly."
        )
        + H3("0.4  What streaming is not")
        + red_flag(
            ul([
                "<strong>Streaming is not automatically correct.</strong> A fast wrong event is still wrong. If amount, account, timestamp or customer state is inaccurate, speed only spreads the defect faster.",
                "<strong>Streaming is not a replacement for the ledger.</strong> The ledger remains the authoritative money truth. Streams distribute facts and trigger reactions, but the bank still needs controlled posting, reconciliation and audit.",
                "<strong>Streaming is not always better than batch.</strong> End-of-day regulatory reports, interest accrual, monthly statements and archive loads may still be batch because the business problem does not require second-by-second reaction.",
                "<strong>Streaming is not just a tool choice.</strong> Buying Kafka does not create event-driven architecture. The hard work is event design, ownership, schema governance, ordering, replay, privacy, operations and accountability.",
            ])
        )
        + H3("0.5  Where streaming sits in the BFSI technology map")
        + p("Streaming usually sits between operational systems and consumers that need fresh facts. It may "
            "read changes from a ledger through Change Data Capture, receive native events from payment "
            "services, ingest market ticks from exchanges, or collect telemetry from digital channels. It "
            "then fans those events out to fraud engines, risk systems, customer notifications, operational "
            "dashboards, data lakes and machine-learning features.")
        + mermaid(
            "flowchart TB\n"
            "  subgraph Sources\n"
            "    A[Core ledger]\n"
            "    B[Payment hub]\n"
            "    C[Card processor]\n"
            "    D[Market data feed]\n"
            "    E[Mobile and web channels]\n"
            "  end\n"
            "  subgraph Streaming platform\n"
            "    K[Event log such as Kafka or Pulsar]\n"
            "    P[Stream processing such as Flink]\n"
            "  end\n"
            "  subgraph Consumers\n"
            "    F[Fraud and AML]\n"
            "    R[Risk and treasury]\n"
            "    N[Notifications]\n"
            "    L[Lakehouse]\n"
            "    O[Operations dashboard]\n"
            "  end\n"
            "  A --> K\n"
            "  B --> K\n"
            "  C --> K\n"
            "  D --> K\n"
            "  E --> K\n"
            "  K --> P\n"
            "  K --> F\n"
            "  P --> R\n"
            "  K --> N\n"
            "  K --> L\n"
            "  P --> O",
            "Figure 0.2 — Streaming is the real-time nervous system between systems of record and systems of action."
        )
        + H3("0.6  The geography lens from day one")
        + table(
            ["Region", "Common real-time BFSI need", "Design pressure"],
            [
                ["India", "UPI, IMPS, card tokenisation, payment-data storage and fast fraud response.", "High retail volume, low ticket sizes, strong localisation expectations, NPCI and RBI rule sensitivity."],
                ["United States", "Card authorisation, ACH modernisation, FedNow, RTP, market surveillance and sanctions screening.", "Fragmented rails, strong OFAC screening, legacy batch coexistence and high vendor footprint."],
                ["United Kingdom", "Faster Payments, Confirmation of Payee, APP fraud monitoring and Open Banking events.", "Customer reimbursement, operational resilience and clear customer-status evidence."],
                ["Eurozone", "SEPA Instant, TIPS, DORA operational resilience, market and payments monitoring.", "Cross-border euro reach, strict resilience expectations and GDPR-driven data governance."],
                ["Singapore", "FAST, PayNow, digital banks, MAS technology-risk controls and regional treasury hubs.", "Always-on payments, outsourcing governance, data access controls and regional integration."],
            ]
        )
        + callout("Section 0 takeaway",
            ul([
                "Streaming means moving meaningful facts quickly to the systems that need them.",
                "An event is a fact, a stream is facts over time, a topic is a named lane, and a consumer is a system that reacts.",
                "The ledger remains the money truth. Streaming spreads and processes facts around that truth.",
                "Real-time design is not only technical. It changes fraud, operations, customer promises, evidence, privacy and regulatory posture.",
            ]),
            "info")
    )
    return TopicSection("0.  Primer — from phone notifications to real-time banking", "basic", body)


def _sec1() -> TopicSection:
    body = (
        primer(
            p("Streaming exists because time has become part of the product. A bank that notices fraud "
              "tomorrow has not protected the customer today. A risk platform that sees liquidity stress "
              "after markets close has not helped treasury manage the day. A mobile app that shows stale "
              "payment status creates duplicate attempts and complaints. Section 1 explains why streaming "
              "and event-driven architecture exist at all, before we name the tools.")
        )
        + H3("1.1  The old model — move files, then reconcile later")
        + p("For decades, banks were built around batch files. Branches closed, files were collected, "
            "mainframes processed postings, reports were printed, and exceptions were handled the next "
            "day. Batch remains important because it is efficient, controllable and easy to reconcile. "
            "But batch has one weakness: the business learns late. When the world was branch-led and "
            "business-hours-led, late was often acceptable. In 24×7 digital banking, late can be harmful.")
        + table(
            ["Business moment", "Batch answer", "Streaming answer"],
            [
                ["Customer sends ₹25,000 to a new beneficiary", "Fraud review may happen after the day's file.", "Risk signals are evaluated before or during payment release."],
                ["Merchant sees card approval", "Settlement and analytics arrive later.", "Approval event updates customer app, merchant risk, operations and data platform quickly."],
                ["Corporate submits payroll file", "Exceptions are found after batch processing.", "Item-level validation events show accepted, rejected and pending salary credits during processing."],
                ["Market price jumps 3%", "Risk report refreshes in the next scheduled cycle.", "Position and limit calculations update as ticks arrive."],
                ["Cloud service degrades", "Incident report is reconstructed afterwards.", "Telemetry events trigger alerts, failover and customer-impact analysis during the incident."],
            ]
        )
        + H3("1.2  The real first principle: separate recording from reacting")
        + p("A bank must both record truth and react to truth. Recording truth is the job of systems of "
            "record: ledgers, core banking, card ledgers, trade stores and case-management systems. Reacting "
            "to truth is the job of many other systems: fraud, sanctions, customer messaging, analytics, "
            "operations, regulatory reporting and machine-learning features. Event-driven architecture exists "
            "because one recorded fact may need many reactions, and those reactions should not require every "
            "system to be tightly coupled to the system of record.")
        + analogy(
            p("Think of a hospital. The doctor writes the official prescription in the medical record. "
              "But the pharmacy, billing desk, nurse station and insurance desk all need to react. The doctor "
              "should not personally call every desk and explain the prescription each time. A controlled "
              "notification system carries the fact to authorised teams. The medical record remains truth; "
              "the notifications make the hospital move.")
        )
        + mermaid(
            "flowchart LR\n"
            "  A[System of record writes truth] --> B[Event published]\n"
            "  B --> C[Fraud reaction]\n"
            "  B --> D[Customer notification]\n"
            "  B --> E[Operations dashboard]\n"
            "  B --> F[Lakehouse copy]\n"
            "  B --> G[Regulatory evidence]\n"
            "  C --> H[Decision or case]\n"
            "  D --> I[Customer action]",
            "Figure 1.1 — Event-driven design separates recording the fact from the many reactions to that fact."
        )
        + H3("1.3  Why point-to-point integration breaks at bank scale")
        + p("Without an event backbone, teams often build direct integrations. The card system calls fraud, "
            "calls notifications, calls rewards, calls analytics, calls operations. Then the payment hub does "
            "the same. Then the mobile app does the same. At small scale this feels simple. At bank scale it "
            "creates a mesh of fragile dependencies: one new consumer means another API, another timeout path, "
            "another data contract, another outage mode and another support conversation.")
        + example("The fan-out problem with numbers",
            p("Suppose 8 source systems each need to inform 12 consuming systems. Point-to-point integration "
              "can create up to 96 integration paths. If each path has its own authentication, schema, retry, "
              "timeout, monitoring and change process, every new product becomes a coordination programme. "
              "With an event backbone, the 8 source systems publish controlled events to topics, and the 12 "
              "consumers subscribe. Complexity does not disappear, but it moves into governed topics, schemas, "
              "consumer groups, access controls and operational monitoring.")
        )
        + table(
            ["Design", "What happens", "Risk"],
            [
                ["Point-to-point APIs", "Each source calls each consumer directly.", "Tight coupling, timeout chains, duplicated contracts and hard change management."],
                ["Shared database reads", "Consumers read source database tables directly.", "Breaks ownership, creates security risk and couples consumers to internal table design."],
                ["Nightly files", "Sources write files for consumers to pick up later.", "Simple but slow, with late fraud, stale balances and delayed operations."],
                ["Event backbone", "Sources publish events and authorised consumers subscribe.", "Better decoupling, but requires schema governance, ordering, replay and operations maturity."],
            ]
        )
        + H3("1.4  Why Kafka became the default conversation")
        + p("Apache Kafka became central because it solved a specific bank-scale problem: many producers "
            "and many consumers need a durable, ordered, replayable log of events. Kafka is not just a queue. "
            "A queue usually hands a message to one worker and then removes it. Kafka stores events in a log "
            "for a retention period, lets many consumer groups read at their own pace, and lets consumers replay "
            "history if they need to rebuild state. That replay ability is why Kafka is common in payment hubs, "
            "fraud platforms, data ingestion and operational telemetry.")
        + table(
            ["Concept", "Plain-English meaning", "BFSI example"],
            [
                ["Producer", "System that writes events.", "Payment hub publishes <code>payment_status_changed</code>."],
                ["Topic", "Named stream of similar events.", "<code>upi.payments.status</code> or <code>cards.authorisations</code>."],
                ["Partition", "A topic lane that allows scale and ordering by key.", "All events for one account can be keyed to preserve order."],
                ["Consumer group", "One logical application reading events with many workers.", "Fraud service reads card events using 20 workers but acts as one consumer group."],
                ["Offset", "A consumer's position in the log.", "Analytics job knows it has processed events up to position 18,420,199."],
                ["Retention", "How long the log keeps events.", "Seven days for operational replay, longer for selected audit topics if policy allows."],
            ]
        )
        + H3("1.5  Why Flink enters the picture")
        + p("Kafka carries and stores event streams. Apache Flink processes streams continuously. If Kafka "
            "is the moving belt of events, Flink is the machine that watches the belt, groups events, joins "
            "streams, calculates windows, detects patterns and writes results. A fraud rule such as ‘three "
            "failed logins followed by a new-payee transfer above ₹50,000 within ten minutes’ is not just "
            "message movement. It is stateful stream processing: remembering what happened for that customer "
            "over a time window and acting when a pattern appears.")
        + example("A simple stream-processing rule",
            ol([
                "A login stream receives <code>login_failed</code> and <code>login_success</code> events.",
                "A payment stream receives <code>new_payee_added</code> and <code>payment_initiated</code> events.",
                "Flink keys both streams by customer ID, so all events for one customer meet in the same logical state.",
                "For each customer, Flink keeps a 10-minute window of recent events.",
                "If it sees at least three failed logins, then a successful login from a new device, then a ₹75,000 new-payee transfer, it emits <code>high_risk_payment_pattern_detected</code>.",
                "The payment orchestration service can step up authentication, hold the payment, or route the case to fraud operations depending on policy.",
            ])
        )
        + H3("1.6  The BFSI reasons streaming exists")
        + table(
            ["Reason", "What streaming enables", "What can go wrong if unmanaged"],
            [
                ["Fraud and scam prevention", "Detect suspicious sequences while the payment can still be stopped or challenged.", "False positives block legitimate customers; false negatives create loss and reimbursement exposure."],
                ["Customer status", "Show fresh payment, card, loan or claim state in apps and support tools.", "Wrong status can cause duplicate attempts, complaints and evidence gaps."],
                ["Operational resilience", "Detect degradation, stuck transactions and backlog while services are still running.", "Alert floods and weak runbooks create noise rather than action."],
                ["Risk and treasury", "Update positions, liquidity and exposures as events arrive.", "Poor ordering or late data can misstate risk."],
                ["Data platform freshness", "Feed lakehouse, feature stores and dashboards without waiting for nightly batch.", "Uncontrolled duplication or schema drift corrupts analytics."],
                ["Regulatory evidence", "Preserve event trails for decisions, customer communications and incidents.", "Retention, privacy and access rules may be breached if events are treated as casual logs."],
            ]
        )
        + H3("1.7  The first leadership warning: real time changes accountability")
        + red_flag(
            p("Push back if a team says, ‘Streaming is only a faster pipe.’ A faster pipe changes the "
              "business control model. Fraud decisions move earlier. Customer promises become more immediate. "
              "Operations must monitor continuously. Data privacy applies to more copies. Reconciliation needs "
              "event IDs and lineage. Resilience must handle backlog and replay. A streaming programme is a "
              "control-design programme, not merely a middleware upgrade."))
        + H3("1.8  Section 1 takeaway")
        + callout("Why streaming exists",
            ul([
                "Batch is still useful, but many BFSI decisions lose value if the bank learns too late.",
                "Event-driven architecture separates recording truth from reacting to truth.",
                "Kafka became important because it provides a durable, replayable event log for many producers and consumers.",
                "Flink became important because many real-time decisions require stateful processing across time windows and streams.",
            ]),
            "info")
    )
    return TopicSection("1.  Why streaming exists at all — first principles", "basic", body)


def _sec2() -> TopicSection:
    body = (
        primer(
            p("Section 2 puts the whole idea on one wall. Do not start by memorising product names. "
              "Start with the shape. A streaming architecture has systems that create facts, a durable "
              "event log that remembers facts, rules that describe the shape of those facts, processors "
              "that calculate new facts, and consumers that act. The safest mental model is not ‘Kafka in "
              "the middle’. It is a controlled nervous system: facts enter once, are preserved with order "
              "and identity, then are read many times by authorised parts of the bank.")
        )
        + H3("2.1  The core picture")
        + mermaid(
            "flowchart LR\n"
            "  subgraph Producers\n"
            "    A[Mobile app]\n"
            "    B[Payment hub]\n"
            "    C[Card processor]\n"
            "    D[Core ledger CDC]\n"
            "    E[Market data feed]\n"
            "  end\n"
            "  subgraph Event backbone\n"
            "    S[Schema registry]\n"
            "    K[Durable event log]\n"
            "    P[Partitions by key]\n"
            "    R[Replication and retention]\n"
            "  end\n"
            "  subgraph Stream processing\n"
            "    F[Filter and enrich]\n"
            "    J[Join streams]\n"
            "    W[Window and aggregate]\n"
            "    X[Detect patterns]\n"
            "  end\n"
            "  subgraph Consumers\n"
            "    G[Fraud decisions]\n"
            "    H[Customer notifications]\n"
            "    I[Operations dashboard]\n"
            "    L[Lakehouse]\n"
            "    M[Regulatory evidence]\n"
            "  end\n"
            "  A --> K\n"
            "  B --> K\n"
            "  C --> K\n"
            "  D --> K\n"
            "  E --> K\n"
            "  S --> K\n"
            "  K --> P --> R\n"
            "  R --> F --> J --> W --> X\n"
            "  R --> G\n"
            "  R --> H\n"
            "  X --> I\n"
            "  R --> L\n"
            "  R --> M",
            "Figure 2.1 — Streaming architecture is a controlled path from facts to reactions, not just a pipe."
        )
        + H3("2.2  The six boxes in the picture")
        + table(
            ["Box", "Plain-English job", "BFSI example", "Failure if misunderstood"],
            [
                ["Producer", "Creates or publishes an event when something meaningful happens.", "Payment hub publishes <code>payment_accepted</code> after validating a transfer request.", "Producer emits vague or duplicate events, so consumers cannot trust the stream."],
                ["Schema", "Defines the fields, meanings and allowed evolution of an event.", "Card authorisation event defines amount, currency, merchant category, token, timestamp and risk attributes.", "A field changes from paise to rupees and fraud thresholds silently break."],
                ["Event log", "Stores events durably so many consumers can read and replay them.", "Kafka topic keeps seven days of payment-status events for operational replay.", "Events vanish after one consumer reads them, so later consumers cannot rebuild state."],
                ["Partition key", "Chooses which ordered lane receives an event.", "Key by account ID when account order matters, or by card token when card sequence matters.", "Wrong key causes out-of-order state for one customer or hot partitions for popular merchants."],
                ["Stream processor", "Continuously calculates, joins, aggregates or detects patterns.", "Flink joins login events and payment events to detect account takeover.", "A simple consumer is asked to do stateful logic and loses context on restart."],
                ["Consumer", "Reads events and acts, stores, alerts or serves a view.", "Notification service sends payment status to the customer app.", "Consumer side effects happen twice because retries were not designed."],
            ]
        )
        + H3("2.3  One event, many reactions")
        + p("The power of the architecture is that one well-designed event can serve many needs without "
            "forcing the source system to know every future use. A payment hub should not need to know "
            "the internal details of fraud dashboards, lakehouse ingestion jobs, customer notification "
            "templates and regulatory evidence stores. It should publish a clear payment event. Authorised "
            "consumers then decide how to use it.")
        + example("A £4,500 salary credit event fan-out",
            ol([
                "Employer payroll processing credits an employee with £4,500 and the account ledger commits the posting.",
                "The ledger or payment hub emits <code>salary_credit_posted</code> with account ID, amount, currency, employer reference, value date and event ID.",
                "The mobile-notification consumer sends ‘Salary credited: £4,500’.",
                "The customer-support view updates so an agent can answer if the employee calls.",
                "The lakehouse ingestion consumer stores the event for analytics and financial reporting.",
                "A financial-wellness consumer may update budgeting insights, if the customer consent and product rules allow it.",
                "A fraud or mule-monitoring consumer may watch for rapid onward transfers after the salary credit.",
            ])
        )
        + H3("2.4  Why the log is different from a queue")
        + table(
            ["Question", "Traditional queue answer", "Durable event log answer"],
            [
                ["Who reads a message?", "Usually one worker receives and removes it.", "Many consumer groups can read the same event independently."],
                ["Can a new consumer read old events?", "Usually no, unless messages were copied elsewhere.", "Yes, if events are still within retention and access policy."],
                ["What is the unit of progress?", "Message acknowledgement.", "Consumer offset, meaning position in the log."],
                ["What is it best for?", "Work distribution, task execution, command handling.", "Fact distribution, replay, rebuilding views and multi-consumer integration."],
                ["BFSI example", "Send one statement-generation job to one worker.", "Keep payment-status events so support, fraud and lakehouse consumers read at their own pace."],
            ]
        )
        + analogy(
            p("A queue is like a stack of claim forms on a desk: one clerk takes a form and it leaves the "
              "pile. A log is like a timestamped CCTV recording: many authorised reviewers can watch the "
              "same recording, pause at different places, and rewatch from an earlier point if they need to "
              "reconstruct what happened. BFSI needs both. Do not force one pattern to do every job.")
        )
        + H3("2.5  The three kinds of time")
        + p("Streaming systems are hard because they must reason about time. In ordinary conversation, "
            "‘time’ sounds simple. In real-time data platforms, there are at least three clocks.")
        + table(
            ["Clock", "Meaning", "Example", "Why it matters"],
            [
                ["Event time", "When the business fact actually happened.", "Customer tapped card at 10:00:00.000.", "Fraud windows and risk calculations should usually use event time."],
                ["Ingestion time", "When the event entered the streaming platform.", "Card event reached Kafka at 10:00:00.090.", "Operational monitoring uses this to detect upstream delay."],
                ["Processing time", "When a processor handled the event.", "Flink rule evaluated it at 10:00:00.140.", "Processor backlogs and failover can shift processing time."],
            ]
        )
        + red_flag(
            p("Push back if a dashboard says ‘real time’ but cannot tell you which clock it uses. A payment "
              "event that happened at 10:00 but was processed at 10:07 may look current by processing time "
              "and late by event time. For fraud, liquidity and customer status, that distinction matters.")
        )
        + H3("2.6  Event identity, ordering and replay")
        + p("Three design decisions decide whether the picture is safe. First, every event needs a stable "
            "identity, usually an event ID plus business keys such as payment ID, account ID or card token. "
            "Second, events that must be read in order need a partition key that keeps related events together. "
            "Third, consumers must be able to replay events without creating duplicate side effects. Replay is "
            "a superpower only if the bank knows what can safely be repeated.")
        + table(
            ["Design question", "Weak answer", "Strong answer"],
            [
                ["What identifies the event?", "Timestamp plus amount.", "Globally unique event ID plus business ID, producer name, version and event time."],
                ["What order matters?", "All events should be ordered globally.", "Only specific business streams need order, such as one payment ID or one account ID."],
                ["What is the partition key?", "Random or default key.", "Chosen from the business entity whose sequence must be preserved."],
                ["Can we replay?", "Yes, Kafka can replay.", "Yes for idempotent consumers; no or controlled for consumers that send money, SMS or external messages."],
                ["How do we prove lineage?", "Look at logs.", "Preserve event ID, schema version, source system, offsets, processing job and sink write reference."],
            ]
        )
        + H3("2.7  The role of schema governance")
        + p("A schema is the contract for an event. It says which fields exist, what they mean, which are "
            "mandatory, which are optional, what units they use, and how the event may change over time. "
            "Without schema governance, a streaming platform becomes a fast rumour network. With governance, "
            "it becomes a controlled language the bank can trust.")
        + example("A small schema mistake with large impact",
            p("A card event originally sends amount in minor units: £92.50 is sent as 9250. A new producer "
              "team changes the field to major units and sends 92.50 without versioning the schema. A fraud "
              "rule looking for purchases above £500 now reads some large transactions as tiny, while another "
              "consumer may multiply incorrectly. No database table was corrupted, but the event contract was. "
              "Schema compatibility checks exist to prevent exactly this class of defect.")
        )
        + H3("2.8  Topic naming and ownership")
        + p("Topic names should teach the architecture. A topic called <code>data1</code> or <code>events</code> "
            "tells nobody what it carries. A useful name signals domain, entity and event family, such as "
            "<code>payments.status.changed</code>, <code>cards.authorisations.requested</code> or "
            "<code>risk.positions.valued</code>. Ownership matters just as much. Every event needs a producer "
            "owner, schema owner, data owner, operational owner and consumer access process.")
        + table(
            ["Topic design choice", "Bad smell", "Better pattern"],
            [
                ["Name", "<code>topic_a</code>, <code>events</code>, <code>kafka_payments</code>.", "<code>payments.status.changed</code> or <code>cards.authorisations.approved</code>."],
                ["Granularity", "One giant topic for every payment fact.", "Separate topics by domain and lifecycle where consumers need different contracts."],
                ["Ownership", "Created by platform team, nobody owns business meaning.", "Business domain owns event semantics; platform owns shared infrastructure."],
                ["Access", "Any team can subscribe if they know the name.", "Access approved by data classification, purpose, geography and least privilege."],
                ["Documentation", "Ask the developer who built it.", "Schema registry, event catalogue, sample payloads, service-level expectations and lineage."],
            ]
        )
        + H3("2.9  Section 2 takeaway")
        + callout("Core picture recap",
            ul([
                "A streaming architecture starts with meaningful facts, not tools.",
                "The durable event log lets many authorised consumers read and replay the same facts independently.",
                "Partitions give scale and local ordering, but only if the key matches the business ordering need.",
                "Stream processors such as Flink turn raw events into new derived facts using state, windows, joins and pattern detection.",
                "Schema, identity, ownership, access and replay rules are part of the architecture, not paperwork after the build.",
            ]),
            "info")
    )
    return TopicSection("2.  The core concept in one picture", "basic", body)


def _sec3() -> TopicSection:
    body = (
        primer(
            p("Section 3 walks through the mechanics. Imagine one payment event travelling through the "
              "architecture. It begins as a business fact, becomes a structured event, is written by a "
              "producer, appended to a durable log, replicated, read by consumers, processed into derived "
              "facts, written to sinks, monitored, and sometimes replayed. Each phase has a different owner "
              "and a different failure mode.")
        )
        + H3("3.1  The lifecycle at a glance")
        + mermaid(
            "flowchart LR\n"
            "  A[Business fact occurs] --> B[Event is designed]\n"
            "  B --> C[Producer publishes]\n"
            "  C --> D[Broker appends to partition]\n"
            "  D --> E[Replicas acknowledge]\n"
            "  E --> F[Consumers read by offset]\n"
            "  F --> G[Processor enriches or aggregates]\n"
            "  G --> H[Sinks and side effects]\n"
            "  H --> I[Monitor reconcile replay]\n"
            "  I --> F",
            "Figure 3.1 — The streaming lifecycle from business fact to replayable evidence."
        )
        + H3("3.2  Phase 1 — the business fact occurs")
        + p("Nothing starts with Kafka. It starts with a business fact. A customer taps a card, a payment "
            "changes status, a loan application moves to approved, a market price ticks, a sanctions case is "
            "opened, or a Kubernetes pod restarts. The first design question is whether the fact is important "
            "enough to publish. Publishing everything creates noise, cost and privacy risk. Publishing too "
            "little leaves the bank blind.")
        + table(
            ["Fact", "Should it usually be an event?", "Reason"],
            [
                ["Payment accepted for processing", "Yes", "Fraud, support, operations and customer status may all need it."],
                ["Mouse moved on a web page", "Usually no for core banking stream", "Too noisy unless part of a specific behavioural analytics product with consent."],
                ["Ledger posting committed", "Yes, with strong controls", "This is a money-state fact and may feed reconciliation, finance and notifications."],
                ["A developer debug line", "No as a business event", "Observability logs are useful but should not be mixed with business events."],
                ["Market price changed", "Yes for trading and risk", "Risk, valuation and limit systems may need immediate recalculation."],
            ]
        )
        + H3("3.3  Phase 2 — the event is designed")
        + p("The event must say what happened, not what another system should do. This difference is subtle "
            "and important. <code>send_customer_sms</code> is a command to one system. "
            "<code>payment_status_changed</code> is a fact many systems can use. Good events are named in the "
            "past tense because they record something that already happened.")
        + table(
            ["Design element", "Question", "Payment example"],
            [
                ["Event name", "What happened?", "<code>payment_status_changed</code>."],
                ["Event ID", "How do we identify this exact event?", "UUID or bank-standard unique ID."],
                ["Business key", "Which business object changed?", "Payment ID, debtor account, creditor account, rail reference."],
                ["Event time", "When did the fact happen?", "Timestamp from payment hub when status changed."],
                ["Schema version", "Which contract describes this event?", "Version 1.2 of payment-status schema."],
                ["Payload", "What fields do authorised consumers need?", "Old status, new status, amount, currency, rail, reason code."],
                ["Classification", "How sensitive is it?", "Payment data, personal data and possible bank secrecy data."],
            ]
        )
        + red_flag(
            p("Push back if event design starts from a consumer's screen requirement only. A consumer may "
              "need a screen today, but the event will outlive that screen. Design the event around the "
              "business fact, then let consumers build screens, alerts and reports from it.")
        )
        + H3("3.4  Phase 3 — the producer publishes safely")
        + p("A producer is the application that writes the event. The dangerous moment is when the producer "
            "updates its own database and publishes an event. If it writes the database but crashes before "
            "publishing, the bank has truth with no event. If it publishes but the database write rolls back, "
            "the bank has an event for a fact that did not happen. This is called the dual-write problem.")
        + mermaid(
            "flowchart TB\n"
            "  A[Payment service receives request] --> B[Write payment state]\n"
            "  B --> C{Publish event}\n"
            "  C -->|crash before publish| D[Database says changed but no event]\n"
            "  C -->|publish then rollback| E[Event says changed but database disagrees]\n"
            "  D --> F[Consumer blind spot]\n"
            "  E --> G[False downstream action]",
            "Figure 3.2 — The dual-write problem is why safe event publication needs a pattern, not hope."
        )
        + H3("3.5  Two common publication patterns — outbox and Change Data Capture")
        + table(
            ["Pattern", "How it works", "BFSI use", "Trade-off"],
            [
                ["Transactional outbox", "Application writes business row and outbox row in the same database transaction. A relay publishes the outbox row to the event log.", "Payment hub changes status and writes matching event record atomically.", "Very reliable, but needs outbox table, relay, cleanup and monitoring."],
                ["Change Data Capture", "A CDC tool reads database logs and converts committed changes into events.", "Ledger changes are captured from Oracle, Db2, Postgres or SQL Server logs.", "Good for legacy systems, but raw table changes may not equal clean business events."],
                ["Direct publish", "Application sends event directly to broker after business processing.", "Simple telemetry or low-risk non-money events.", "Can be unsafe for money-state events unless failure handling is carefully designed."],
            ]
        )
        + example("Outbox with a payment-status change",
            ol([
                "Payment service receives instruction <code>PAY123</code> for ₹25,000.",
                "In one database transaction, it updates payment status to <code>ACCEPTED</code> and inserts an outbox row with event ID <code>EVT789</code>.",
                "The transaction commits. Now the database truth and the pending event record are atomic.",
                "An outbox relay reads <code>EVT789</code> and publishes it to <code>payments.status.changed</code>.",
                "After broker acknowledgement, the relay marks the outbox row as published.",
                "If the relay crashes, it restarts and republishes or resumes safely using event ID and idempotency.",
            ])
        )
        + H3("3.6  Phase 4 — the broker appends, partitions and replicates")
        + p("When the event reaches the streaming platform, the broker appends it to a partition. Think of "
            "a partition as an ordered notebook page for a subset of events. Kafka assigns each event an "
            "offset, which is like a line number on that page. For resilience, partitions are replicated "
            "across brokers. A producer may wait for acknowledgements before considering the write successful.")
        + table(
            ["Broker concept", "Plain-English explanation", "Why a bank cares"],
            [
                ["Partition", "One ordered lane inside a topic.", "Keeps related payment events in sequence if keyed correctly."],
                ["Offset", "The event's position in a partition.", "Consumers and auditors can say how far processing reached."],
                ["Replication factor", "How many broker copies hold the partition.", "A broker failure should not lose payment-status events."],
                ["Acknowledgement", "Producer waits for broker confirmation.", "Stronger acknowledgement lowers loss risk but can add latency."],
                ["Retention", "How long events remain available.", "Replay and evidence need retention, but privacy and cost limit it."],
            ]
        )
        + H3("3.7  Phase 5 — consumers read and commit progress")
        + p("Consumers do not usually receive events as a push that vanishes forever. In Kafka-style systems, "
            "consumers read from the log and track their offsets. If a fraud consumer has processed up to "
            "offset 1,000,000, it can restart from 1,000,001. If it needs to rebuild a view, it may reset to "
            "an earlier offset. This is powerful but dangerous if processing has side effects.")
        + table(
            ["Consumer action", "Safe example", "Danger example"],
            [
                ["Read event", "Fraud service reads <code>payment_status_changed</code>.", "Consumer reads personally sensitive fields without approved purpose."],
                ["Process event", "Updates internal fraud state for that payment.", "Uses stale schema and interprets status incorrectly."],
                ["Commit offset", "Commits after durable processing succeeds.", "Commits before writing result, then crashes and loses work."],
                ["Retry", "Retries with same event ID and idempotent write.", "Sends duplicate SMS, duplicate case or duplicate external request."],
                ["Replay", "Rebuilds dashboard from past events.", "Replays customer notifications and alarms customers again."],
            ]
        )
        + H3("3.8  Phase 6 — stream processing adds state, windows and joins")
        + p("Simple consumers handle one event at a time. Stream processors handle patterns over time. They "
            "remember state, group by key, join streams and calculate windows. A ten-minute fraud window, a "
            "five-second market-price aggregation, or a per-account liquidity summary cannot be solved by "
            "looking at one event alone.")
        + example("Windowed fraud detection in numbers",
            p("A bank receives 2,000 login events per second and 800 payment-initiation events per second. "
              "The fraud rule needs to find customers with at least three failed logins followed by a new-payee "
              "payment above ₹50,000 within ten minutes. A stream processor keys events by customer ID, keeps "
              "the last ten minutes of login and payment state, and emits a high-risk event when the pattern "
              "appears. If the processor falls five minutes behind, the rule is still logically correct but "
              "operationally late; the payment may already have gone.")
        )
        + table(
            ["Stream-processing idea", "Plain-English meaning", "BFSI example"],
            [
                ["Keyed state", "Memory kept per entity such as customer, account or card.", "Recent failed logins per customer."],
                ["Window", "A bounded time period for calculation.", "Payments in the last ten minutes."],
                ["Join", "Combining related events from different streams.", "Join device-risk events with payment-initiation events."],
                ["Aggregation", "Summarising many events.", "Total outgoing value per account in one hour."],
                ["Watermark", "A processor's estimate of how complete event-time data is.", "Allows late card events without waiting forever."],
            ]
        )
        + H3("3.9  Phase 7 — sinks, side effects and idempotency")
        + p("A sink is where processed output goes: a database, lakehouse table, case-management system, SMS "
            "gateway, fraud decision engine, alerting tool or another topic. The risky sinks are those with "
            "side effects outside the streaming platform. Writing a dashboard row twice may be fixable. Sending "
            "two scam warnings, opening two cases, or calling an external payment hold API twice may harm customers "
            "and operations. Idempotency is therefore as important in streaming as it is in payment APIs.")
        + table(
            ["Sink", "Side-effect risk", "Control"],
            [
                ["Lakehouse table", "Duplicate rows or wrong partitions.", "Event ID deduplication, merge strategy, schema checks."],
                ["Customer notification", "Duplicate or contradictory messages.", "Notification ID, status check, replay guard."],
                ["Fraud case system", "Duplicate cases and analyst overload.", "Case key based on event ID plus customer plus scenario."],
                ["Payment hold API", "Repeated holds or inconsistent release.", "Idempotency key and state lookup before action."],
                ["Operations dashboard", "Wrong count or stale alert.", "Offset tracking, freshness metric, late-event handling."],
            ]
        )
        + H3("3.10  Phase 8 — observe, reconcile and replay")
        + p("Streaming does not remove reconciliation. It changes what must be reconciled. Leaders should ask: "
            "Did every expected source event arrive? Did every consumer process it? Did any consumer lag beyond "
            "its service-level objective? Did derived counts match ledger or scheme truth? Were any events sent "
            "to a dead-letter topic? Can the team replay safely from a chosen offset and prove the outcome?")
        + table(
            ["Operational metric", "What it tells you", "Example threshold"],
            [
                ["Producer error rate", "Whether source systems are failing to publish.", "Less than 0.01% failed publishes for payment-status events."],
                ["Consumer lag", "How far a consumer is behind the latest event.", "Fraud consumer less than 2 seconds behind during peak."],
                ["End-to-end latency", "Time from business fact to consumer action.", "Card alert delivered within 500 milliseconds at p95."],
                ["Dead-letter count", "Events that could not be processed normally.", "Zero untriaged payment events older than 15 minutes."],
                ["Replay success", "Whether the platform can rebuild state after failure.", "Dashboard rebuilt from offsets with counts matching source totals."],
                ["Reconciliation break", "Whether event-derived truth matches system-of-record truth.", "Payment-status event count equals payment-hub status changes for the cycle."],
            ]
        )
        + H3("3.11  Worked flow — India UPI status event")
        + example("UPI payment status propagation",
            ol([
                "Customer initiates a ₹1,250 UPI payment at 19:30:00.000.",
                "The payment orchestration service records internal status <code>INITIATED</code> and writes an outbox event.",
                "After payer-bank debit confirmation, status changes to <code>DEBIT_CONFIRMED</code>, producing another event for the same payment ID.",
                "The event backbone partitions by payment ID, so all status changes for this payment stay in order.",
                "A customer-notification consumer reads <code>DEBIT_CONFIRMED</code> but does not yet say final success if beneficiary credit is not confirmed.",
                "A support-view consumer updates the case screen to show debit confirmed and rail response pending.",
                "A stream processor watches for payments stuck in debit-confirmed state for more than 90 seconds and emits <code>payment_status_delayed</code>.",
                "Operations dashboard shows the stuck count by payer bank, payee bank and rail reason code.",
                "When beneficiary credit confirmation arrives, <code>CREDIT_CONFIRMED</code> is published and the notification service sends final success wording.",
                "At end-of-cycle, reconciliation compares payment-hub state changes, event counts, NPCI or bank reports, and ledger postings.",
            ])
        )
        + H3("3.12  Common failure modes by phase")
        + table(
            ["Phase", "Failure", "Customer or bank impact", "Control"],
            [
                ["Fact selection", "Important status is not published.", "Support and fraud are blind.", "Event catalogue review for critical lifecycle states."],
                ["Schema", "Field meaning changes silently.", "Consumers make wrong decisions.", "Schema compatibility checks and versioning."],
                ["Producer", "Database updated but event not published.", "Downstream systems miss truth.", "Outbox or CDC with monitoring."],
                ["Broker", "Hot partition from poor key.", "Lag for high-volume customers or merchants.", "Partition-key design and load testing."],
                ["Consumer", "Offset committed before processing.", "Event is skipped after crash.", "Commit after durable success."],
                ["Processor", "Late events ignored incorrectly.", "Fraud or risk result is wrong.", "Watermarks, late-event policy and test data."],
                ["Sink", "Replay repeats side effects.", "Duplicate messages, cases or holds.", "Idempotency and replay guards."],
                ["Operations", "Dead-letter queue not monitored.", "Broken events age silently.", "SLA, owner, ageing dashboard and runbook."],
            ]
        )
        + H3("3.13  Section 3 takeaway")
        + callout("Phase-by-phase recap",
            ul([
                "Streaming begins with a business fact, not with a broker.",
                "Good events describe facts in past tense, carry identity, business keys, event time, schema version and classification.",
                "Outbox and Change Data Capture exist because the database update and event publish must not disagree.",
                "Brokers append events to partitions, assign offsets, replicate data and retain events for replay within policy.",
                "Consumers must process, commit offsets, retry and replay with idempotency and side-effect controls.",
                "Stream processors add the hard part: state, windows, joins, late events and derived facts.",
                "Operations must monitor lag, latency, dead-letter events, replay and reconciliation, not just server uptime.",
            ]),
            "info")
    )
    return TopicSection("3.  How it actually works — phase by phase", "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        primer(
            p("Section 4 prevents a common mistake: treating ‘streaming’ as one product and one pattern. "
              "In real BFSI estates, streaming appears in several forms. A card authorisation flow, a market "
              "data feed, a customer notification stream, a fraud feature pipeline, a ledger Change Data "
              "Capture feed and an event-sourced wallet may all use event technology, but they do not have the "
              "same correctness rules. A leader must recognise the type before judging the design.")
        )
        + H3("4.1  The first split — commands, events and queries")
        + p("Three message shapes get confused in design reviews. A command asks a system to do something. "
            "An event states that something already happened. A query asks for current information. The words "
            "sound academic, but the difference changes ownership. If a payment service receives a command to "
            "hold a payment, it owns the decision. If it publishes an event saying a payment was held, consumers "
            "must not pretend they caused that decision. If a customer-support screen asks for latest status, "
            "that is a query and should not be hidden inside an event stream.")
        + table(
            ["Shape", "Plain-English test", "BFSI example", "Design warning"],
            [
                ["Command", "‘Please do this.’", "<code>hold_payment</code> sent to a payment orchestration service.", "Needs one accountable handler, validation, authorisation and a clear success or rejection response."],
                ["Event", "‘This happened.’", "<code>payment_held</code> published after policy decision.", "Should be past tense and safe for many authorised consumers to observe."],
                ["Query", "‘Tell me the current answer.’", "Support screen asks current UPI payment state.", "Do not force request-response lookups through Kafka just to say the estate is event driven."],
            ]
        )
        + analogy(
            p("In a restaurant, ‘please cook table 12’s order’ is a command. ‘Table 12’s order is cooked’ is an "
              "event. ‘What is table 12’s current status?’ is a query. If the waiter confuses these, the kitchen "
              "may cook twice, the cashier may bill too early, or the customer may be told the wrong status. "
              "Banking systems have the same problem, only with money, fraud and evidence.")
        )
        + H3("4.2  Event notification versus event-carried state transfer")
        + p("A small event can simply notify consumers that something changed. A richer event can carry enough "
            "state for consumers to update their own views without calling the source system. Both are useful. "
            "The choice is a trade-off between payload size, privacy exposure, source-system load and consumer "
            "independence.")
        + table(
            ["Variation", "What the event carries", "When it fits", "BFSI risk"],
            [
                ["Event notification", "Mostly identity and change signal.", "<code>loan_application_status_changed</code> tells consumers to fetch details if authorised.", "If every consumer calls back immediately, the source system gets a thundering herd during peaks."],
                ["Event-carried state transfer", "The useful state needed by consumers.", "<code>card_authorisation_approved</code> includes amount, currency, merchant category, token and approval code.", "Payload may spread personal or payment data beyond the minimum necessary."],
                ["Delta event", "Only fields that changed.", "Address line 2 changed on a customer profile.", "Consumers need previous state or a compacted view to understand the full record."],
                ["Snapshot event", "Full current representation at a point in time.", "End-of-day account summary for analytics or support cache.", "Can become large and expensive, and may include fields many consumers do not need."],
            ]
        )
        + example("Choosing payload size for a card event",
            p("Assume a bank emits 25 million card authorisation events per day. If each event is 1 KB, daily "
              "raw event volume is about 25 GB before replication, indexes and downstream copies. If a team adds "
              "a 20 KB merchant-enrichment block because one analytics consumer wants it, the same stream becomes "
              "about 500 GB per day. With replication factor 3 and two lakehouse copies, cost and privacy exposure "
              "multiply. A better design may publish the core authorisation event and a separate merchant-enrichment "
              "event with stricter access.")
        )
        + H3("4.3  Domain events, integration events and data-change events")
        + p("Not every event is equally meaningful. A domain event speaks the language of the business. An "
            "integration event is shaped for cross-system consumption. A data-change event is often a low-level "
            "database change captured from a table or log. The closer an event is to business language, the easier "
            "it is for risk, operations and product teams to reason about it.")
        + table(
            ["Type", "What it sounds like", "Strength", "Weakness"],
            [
                ["Domain event", "<code>beneficiary_credit_confirmed</code>.", "Business meaning is clear to payment, operations and support teams.", "Requires domain modelling and ownership, not just technical capture."],
                ["Integration event", "<code>payment_status_changed</code> with a stable external contract.", "Good shared contract across many systems.", "May hide some internal detail that one specialist consumer wants."],
                ["Data-change event", "<code>PAYMENT_TABLE row updated column STATUS from A to C</code>.", "Easy to generate from legacy systems using Change Data Capture.", "Consumers must infer business meaning and may couple to table design."],
                ["Technical event", "<code>pod_restarted</code> or <code>api_latency_threshold_breached</code>.", "Useful for observability and operations.", "Should not be mixed with business-money events in the same governance lane."],
            ]
        )
        + red_flag(
            p("Push back if a team says, ‘The database log is our business event model.’ Change Data Capture is "
              "valuable, especially around legacy cores, but a table update may not explain why a payment moved "
              "from pending to rejected. For critical flows, enrich raw changes into named business events before "
              "asking downstream teams to make decisions.")
        )
        + H3("4.4  Streaming ingestion, stream processing and event-driven applications")
        + p("A bank may say it has ‘streaming’ when it is only loading data faster into a lakehouse. That is "
            "useful, but it is not the same as event-driven operations. Separate three layers: ingestion moves "
            "events, processing calculates new events, and applications use events to change business behaviour.")
        + table(
            ["Layer", "Main job", "Example", "Success measure"],
            [
                ["Streaming ingestion", "Move fresh data from sources to storage or consumers.", "Core ledger CDC into a lakehouse every few seconds.", "Completeness, freshness, schema stability and cost."],
                ["Stream processing", "Continuously calculate, join, aggregate or detect patterns.", "Flink detects three failed logins plus new-payee transfer within ten minutes.", "Correctness under late data, low latency and recoverable state."],
                ["Event-driven application", "Business service reacts to events as part of its behaviour.", "Fraud system emits a hold recommendation consumed by payment orchestration.", "Clear accountability, idempotent actions and customer-safe outcomes."],
                ["Streaming analytics", "Dashboards and models use near-real-time facts.", "Operations view shows delayed payments by rail and bank.", "Useful freshness without overstating regulatory truth."],
            ]
        )
        + H3("4.5  Event sourcing and Command Query Responsibility Segregation")
        + p("Event sourcing is a stronger pattern than ordinary event publishing. In event sourcing, the events "
            "are the source of truth for an entity. The current state is rebuilt by replaying all past events. "
            "For a wallet, for example, the balance can be derived from events such as opened, credited, debited, "
            "hold placed and hold released. Command Query Responsibility Segregation, often shortened to CQRS, "
            "separates the model that accepts writes from the model that serves reads. These patterns can be "
            "powerful, but they raise the bar for replay, correction, privacy and operational maturity.")
        + mermaid(
            "flowchart LR\n"
            "  A[Command validate transfer] --> B[Append business event]\n"
            "  B --> C[Event store]\n"
            "  C --> D[Project account balance view]\n"
            "  C --> E[Project support status view]\n"
            "  C --> F[Project audit timeline]\n"
            "  D --> G[Mobile balance query]\n"
            "  E --> H[Agent query]\n"
            "  F --> I[Audit query]",
            "Figure 4.1 — In event sourcing, events are not just notifications. They are the stored history from which views are rebuilt."
        )
        + table(
            ["Pattern", "What changes", "Good fit", "Be careful when"],
            [
                ["Ordinary event publishing", "System of record stores state and also emits events.", "Most payment, card, loan, case and notification integrations.", "Teams assume replayed integration events can fully rebuild legal truth."],
                ["Event sourcing", "Event log is the authoritative history for the entity.", "Digital wallets, workflow histories, some trading and case-timeline designs.", "Regulators, finance or operations require correction semantics the team has not designed."],
                ["CQRS", "Write model and read model are separated.", "High-read customer status views fed by controlled write events.", "Read model becomes stale and nobody communicates freshness to users."],
            ]
        )
        + example("Event-sourced wallet in numbers",
            ol([
                "Wallet opened with balance ₹0.",
                "Customer loads ₹2,000, creating <code>wallet_credited</code> for ₹2,000.",
                "Customer pays merchant ₹450, creating <code>wallet_debited</code> for ₹450.",
                "A refund of ₹100 arrives, creating another credit event.",
                "The current balance view is rebuilt as ₹0 + ₹2,000 - ₹450 + ₹100 = ₹1,650.",
                "If a bug corrupts the balance table, the bank can replay events to rebuild the view, but only if event ordering, correction events and idempotency were designed correctly.",
            ])
        )
        + H3("4.6  Queue, log, pub-sub and stream processor — do not substitute blindly")
        + table(
            ["Technology pattern", "Plain-English job", "BFSI examples", "Wrong-use smell"],
            [
                ["Queue", "Distribute work to one of many workers.", "Statement generation, document OCR tasks, outbound email jobs.", "Used as a long-term audit log even though messages disappear after acknowledgement."],
                ["Publish-subscribe topic", "Broadcast messages to multiple subscribers.", "Customer event notifications to multiple internal services.", "No retention or replay plan for consumers that join later."],
                ["Durable event log", "Store ordered events for many consumer groups and replay.", "Kafka topic for payment status or card authorisations.", "Used for synchronous request-response where an API would be clearer."],
                ["Stream processor", "Continuously compute from one or more streams.", "Fraud patterns, market aggregations, stuck-payment detection.", "Used for simple routing that could be handled by a lightweight consumer."],
                ["Workflow engine", "Track long-running business process state.", "Loan origination, claims handling, trade exception workflow.", "Replaced by scattered events with no single view of process ownership."],
            ]
        )
        + H3("4.7  Platform variations — Kafka, Pulsar, cloud streams and managed services")
        + p("Tool names matter, but only after the pattern is clear. Kafka is the common reference point because "
            "many banks standardised on it for durable logs. Apache Pulsar separates serving and storage and "
            "has native multi-tenancy features. Redpanda offers a Kafka-compatible broker with a different "
            "implementation model. Cloud services such as Amazon Kinesis, Amazon Managed Streaming for Apache "
            "Kafka, Azure Event Hubs, Google Pub/Sub and managed Confluent Cloud reduce infrastructure work but "
            "raise questions about data residency, network isolation, encryption, operational control and exit.")
        + table(
            ["Platform family", "Typical attraction", "BFSI due-diligence question"],
            [
                ["Self-managed Kafka", "Maximum control, familiar ecosystem, on-prem or private-cloud deployment.", "Can the bank operate brokers, upgrades, quotas, certificates, disaster recovery and capacity safely at 24×7 scale?"],
                ["Managed Kafka or Confluent Cloud", "Kafka ecosystem with less broker operations burden.", "Which regions, keys, logs, support access and subcontractors touch regulated data?"],
                ["Apache Pulsar", "Compute-storage separation, multi-tenancy and geo-replication features.", "Does the bank have enough skills and vendor support for production incident recovery?"],
                ["Redpanda", "Kafka API compatibility with simplified operations claims.", "Are compatibility, performance and support proven for the bank's exact workload and governance controls?"],
                ["Amazon Kinesis", "Native Amazon Web Services integration and serverless-style scaling.", "Is the workload committed to AWS, and do shard limits, ordering and retention fit the use case?"],
                ["Azure Event Hubs", "Azure-native event ingestion with Kafka endpoint options.", "Does it meet the bank's Kafka expectations or is it primarily an ingestion service for Azure workloads?"],
                ["Google Pub/Sub", "Global managed pub-sub with cloud-native scaling.", "Are ordering, replay, region controls and data-governance requirements aligned with the BFSI use case?"],
                ["IBM MQ and enterprise messaging", "Mature transactional messaging in many banks.", "Is the need work distribution and assured delivery, or a replayable event-log architecture?"],
            ]
        )
        + H3("4.8  Geography and regulatory variation")
        + p("The same event pattern feels different by market because rails, regulators, residency expectations "
            "and customer-protection rules differ. A global bank should avoid designing an India-only or "
            "US-only event model and then discovering that the United Kingdom, Eurozone or Singapore needs "
            "different evidence and data-handling controls.")
        + table(
            ["Region", "Streaming-heavy BFSI use cases", "Variation a leader should expect"],
            [
                ["India", "UPI status, IMPS, card tokenisation, fraud monitoring, high-volume notifications.", "Very high transaction counts and payment-data localisation expectations make partitioning, local retention and cost discipline central."],
                ["United States", "Card authorisation, FedNow and RTP monitoring, ACH modernisation, OFAC screening, broker-dealer market surveillance.", "Legacy batch and vendor estates coexist with real-time rails, so CDC, mainframe integration and sanctions evidence are recurring themes."],
                ["United Kingdom", "Faster Payments, Confirmation of Payee, Open Banking, authorised push payment fraud monitoring.", "Customer-status evidence, reimbursement workflows and operational resilience push teams to prove event timing and decision lineage."],
                ["Eurozone", "SEPA Instant, TIPS, PSD2-style access, DORA resilience, General Data Protection Regulation controls.", "Cross-border euro reach and privacy obligations require clear data minimisation, retention and third-party oversight."],
                ["Singapore", "FAST, PayNow, digital-bank telemetry, regional treasury and MAS technology-risk controls.", "Regional hub patterns create cross-border access questions even when latency and resilience targets are high."],
                ["Brazil", "Pix instant payments, Open Finance, fraud monitoring.", "Large instant-payment volumes make event-driven fraud controls and customer notifications key design areas."],
                ["Australia and Hong Kong", "New Payments Platform, Faster Payment System, open banking and regional wealth platforms.", "Local outsourcing, resilience and data-access rules shape whether managed cloud streaming can be used directly."],
            ]
        )
        + H3("4.9  Variation by BFSI domain")
        + table(
            ["Domain", "Common event streams", "Distinct design pressure"],
            [
                ["Retail payments", "Payment initiated, accepted, debit confirmed, credit confirmed, failed, reversed.", "Customer-visible status must be timely but not overpromise finality before rail confirmation."],
                ["Cards", "Authorisation requested, approved, declined, cleared, chargeback raised.", "Latency budgets are tight and fraud decisions sit inside the approval path."],
                ["Lending", "Application submitted, document received, score calculated, offer accepted, disbursal posted.", "Workflow and evidence matter more than sub-second throughput in many stages."],
                ["Capital markets", "Market ticks, orders, executions, allocations, margin calls, risk limit updates.", "Ordering, timestamp precision, replay and regulatory surveillance are critical."],
                ["Insurance", "Quote requested, policy bound, claim submitted, document classified, payout approved.", "Long-running workflows need event timelines but also strong case ownership."],
                ["Operations and technology", "Service degraded, queue depth high, pod restarted, batch delayed.", "Technical events should correlate with business impact, not flood teams with noise."],
            ]
        )
        + H3("4.10  Choosing the right variation")
        + table(
            ["If the need is", "Prefer", "Reason"],
            [
                ["One worker must perform a job once.", "Queue.", "Work distribution and acknowledgement are the centre of the problem."],
                ["Many systems need to know a fact happened.", "Event log or pub-sub.", "Consumers should be decoupled from the producer."],
                ["New consumers may need historical events.", "Durable event log with retention and access controls.", "Replay and independent offsets matter."],
                ["A dashboard needs current status quickly.", "CQRS read model fed by events.", "Queries stay fast without overloading the source system."],
                ["A business entity's history is the truth.", "Event sourcing, only with mature controls.", "State is derived from the event history."],
                ["A pattern spans time or multiple streams.", "Stream processor.", "State, windows, joins and late-event handling are required."],
            ]
        )
        + H3("4.11  Section 4 takeaway")
        + callout("Types and variations recap",
            ul([
                "Commands ask a system to act, events state that something happened, and queries ask for an answer.",
                "Small notification events and rich state-carrying events solve different problems and create different privacy and load risks.",
                "Domain events, integration events and raw data-change events are not interchangeable.",
                "Streaming ingestion, stream processing and event-driven applications should be judged by different success measures.",
                "Event sourcing and CQRS are powerful patterns, but they require stronger replay, correction, evidence and operational controls.",
                "Platform choice should follow business semantics, geography, data residency, resilience and operating capability.",
            ]),
            "info")
    )
    return TopicSection("4.  Types and variations — queues, logs, pub-sub, event sourcing and cloud streams", "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        primer(
            p("Section 5 goes underneath the dashboard. This is the section that helps a leader challenge "
              "architecture slides that say ‘Kafka gives exactly once’ or ‘Flink handles late data’. Those "
              "phrases hide mechanisms. Mechanisms are what decide whether a real bank loses events, duplicates "
              "side effects, blocks a customer, misses fraud, violates residency or fails to recover during an "
              "incident.")
        )
        + H3("5.1  Partitioning — scale by choosing the right lane")
        + p("A topic can be split into partitions. Each partition is an ordered log. Partitioning gives scale "
            "because different brokers and consumers can handle different partitions. The catch is that order is "
            "only guaranteed within one partition, not across the whole topic. Therefore, the partition key is a "
            "business decision disguised as a technical setting.")
        + example("Partition-key choice for payment status",
            p("Suppose a payment-status topic has 24 partitions and receives 12,000 events per second at peak. "
              "If events are evenly spread, each partition handles about 500 events per second. If the key is "
              "bad and 40% of events go to one partition, that one partition must handle 4,800 events per second "
              "while others are underused. Consumer lag appears even though the cluster has spare capacity. If "
              "ordering must be preserved per payment, keying by payment ID is sensible. If ordering must be "
              "preserved per account across many payments, account ID may be needed, but it can create hot "
              "accounts for large corporates. The right answer depends on the business invariant.")
        )
        + table(
            ["Key choice", "Preserves order for", "Risk"],
            [
                ["Payment ID", "All lifecycle events of one payment.", "Does not order all payments for the same account."],
                ["Account ID", "All account events if every producer uses the same key.", "Large corporate or suspense accounts can become hot partitions."],
                ["Customer ID", "Customer-level journeys across products.", "Too broad for high-volume customers and may mix unrelated domains."],
                ["Merchant ID", "Merchant-level card activity.", "Large merchants can create severe hotspots."],
                ["Random key", "Nothing meaningful.", "Good distribution but no business ordering guarantee."],
            ]
        )
        + red_flag(
            p("Push back if a team says, ‘We need total order for the whole bank.’ Total order across all events "
              "is usually unnecessary and expensive. Ask which entity needs order: one payment, one account, one "
              "card, one customer, one trade, or one case. Design for that invariant.")
        )
        + H3("5.2  Replication, leaders and in-sync replicas")
        + p("A broker failure must not lose critical events. Kafka-style systems replicate partitions across "
            "brokers. One replica acts as leader for reads and writes, while followers copy it. An in-sync replica "
            "is a follower that has kept up enough to be trusted for failover. Producer acknowledgement settings "
            "decide whether a write is considered successful after only the leader stores it or after enough "
            "replicas confirm it.")
        + table(
            ["Setting or concept", "Plain-English meaning", "BFSI implication"],
            [
                ["Replication factor 3", "Three broker copies of the partition exist.", "A common minimum for important topics, but not a substitute for disaster recovery."],
                ["Leader replica", "Broker currently accepting writes for that partition.", "If the leader fails, another in-sync replica should take over."],
                ["In-sync replica", "Replica that has not fallen too far behind.", "Protects against electing a stale copy that missed payment events."],
                ["Acknowledgement all", "Producer waits for required replicas to confirm.", "Lower loss risk, higher latency than fire-and-forget."],
                ["Minimum in-sync replicas", "Required number of healthy replicas for accepting writes.", "Prevents accepting writes when durability is below policy."],
            ]
        )
        + analogy(
            p("Think of a bank branch cash ledger copied by three clerks. If the head clerk writes a page and "
              "two other clerks copy it before the transaction is considered recorded, the branch can survive one "
              "clerk falling ill. If the head clerk alone scribbles and leaves, the branch may not know whether "
              "the page was official. Replication acknowledgements are the digital version of that control.")
        )
        + H3("5.3  Delivery semantics — at most once, at least once and exactly once")
        + p("Delivery semantics describe what can happen during failure. At most once means an event may be lost "
            "but will not be processed twice. At least once means an event should not be lost but may be processed "
            "more than once. Exactly once sounds ideal, but in distributed systems it is usually scoped: exactly "
            "once within a specific platform boundary, with specific transactional sinks, not a universal promise "
            "that no customer ever receives a duplicate SMS.")
        + table(
            ["Semantic", "Failure behaviour", "Where it fits", "BFSI warning"],
            [
                ["At most once", "Process may skip events after crash.", "Low-value telemetry where loss is acceptable.", "Dangerous for payment, ledger or fraud events."],
                ["At least once", "Events are retried and duplicates may occur.", "Most business event pipelines with idempotent consumers.", "Every sink must deduplicate by event ID or business key."],
                ["Exactly once within stream processing", "Input offsets and output writes are coordinated inside supported boundaries.", "Kafka-to-Kafka processing with transactions, or Flink with checkpointed state and transactional sinks.", "Does not automatically make external APIs, emails, SMS or case systems exactly once."],
            ]
        )
        + example("Why duplicate-safe design matters",
            p("A fraud consumer reads event <code>EVT100</code> and opens case <code>CASE77</code>, then crashes "
              "before committing its offset. On restart, it reads <code>EVT100</code> again. Without idempotency, "
              "it opens <code>CASE78</code> too. Analysts now see two cases for one payment and may contact the "
              "customer twice. With idempotency, the case system uses a key such as scenario plus customer plus "
              "event ID, sees that <code>CASE77</code> already exists, and returns the existing case.")
        )
        + H3("5.4  Producer idempotence and transactions")
        + p("Producer idempotence prevents duplicate records caused by producer retries. If a producer sends a "
            "batch, times out, and retries, the broker can recognise that the retry is the same producer sequence "
            "rather than a new event. Transactions go further by allowing a producer to write to multiple partitions "
            "and commit them as one unit, or to coordinate consumed offsets with produced outputs. These features "
            "are powerful but require correct configuration, monitoring and compatible consumers.")
        + table(
            ["Mechanism", "What it protects", "What it does not protect"],
            [
                ["Idempotent producer", "Duplicate appends from producer retry to the same topic partition.", "Duplicate business events created by application logic before the producer call."],
                ["Transactional producer", "Atomic writes across selected topic partitions.", "External database, SMS gateway or payment rail unless integrated through a transaction-aware pattern."],
                ["Read committed isolation", "Consumers avoid reading uncommitted transactional messages.", "Consumers that call external systems still need idempotent side effects."],
                ["Outbox event ID", "Business-level duplicate detection across producer restarts.", "Bad event design or wrong business semantics."],
            ]
        )
        + H3("5.5  Consumer offsets, rebalancing and lag")
        + p("A consumer group is one logical application made of one or more consumer instances. Partitions are "
            "assigned across the instances. If an instance dies or a new one joins, the group rebalances and "
            "partitions move. This is normal, but it can pause consumption. Offsets record progress. Lag measures "
            "how far behind the consumer is from the latest event. In BFSI, lag is not just a technical number; it "
            "is customer and risk exposure.")
        + table(
            ["Consumer concept", "Plain-English meaning", "Operational question"],
            [
                ["Offset", "The next line in the partition notebook that the consumer will read.", "Is the offset committed only after durable processing succeeds?"],
                ["Consumer group", "Many workers acting as one logical application.", "Does scaling add throughput or are there more workers than partitions?"],
                ["Rebalance", "Partitions are reassigned after membership changes.", "Can the application tolerate pauses without missing latency objectives?"],
                ["Lag", "Distance between latest event and consumer progress.", "How many seconds of fraud or status delay does this represent at current volume?"],
                ["Backpressure", "Downstream cannot keep up, so upstream processing slows.", "Is the bottleneck broker, processor, sink database, external API or network?"],
            ]
        )
        + example("Turning lag into business language",
            p("If a fraud consumer handles 5,000 card events per second and lag is 250,000 events, the consumer "
              "is roughly 50 seconds behind at that rate. If card authorisation decisions must happen inside "
              "150 milliseconds, that consumer is not in the approval path anymore; it is doing late detection. "
              "A dashboard that shows only ‘lag 250,000’ is less useful than one that says ‘fraud stream is "
              "50 seconds behind peak input, high-risk holds may be late’.")
        )
        + H3("5.6  Flink state, checkpoints and savepoints")
        + p("Flink and similar processors keep state: recent logins per customer, running totals per account, "
            "latest market price per instrument, open cases per scenario. If a processor fails, it must recover "
            "that state and resume from consistent input positions. A checkpoint is an automatic consistent "
            "snapshot of state and stream positions. A savepoint is usually an operator-triggered snapshot used "
            "for upgrades, migrations or planned changes.")
        + mermaid(
            "flowchart LR\n"
            "  A[Kafka input offsets] --> B[Flink operators]\n"
            "  B --> C[Keyed state per customer]\n"
            "  B --> D[Output topic]\n"
            "  B --> E[Checkpoint storage]\n"
            "  E --> F[Recover job after failure]\n"
            "  F --> B",
            "Figure 5.1 — Stateful stream processing survives failure by restoring both processing state and input positions."
        )
        + table(
            ["Mechanism", "Plain-English meaning", "BFSI example"],
            [
                ["Keyed state", "Memory stored per key.", "Failed-login count per customer ID."],
                ["Checkpoint", "Automatic recovery snapshot.", "Fraud job restarts without forgetting the last ten minutes of events."],
                ["Savepoint", "Controlled snapshot for planned operations.", "Upgrade a risk aggregation job while preserving per-instrument state."],
                ["State backend", "Where large state is stored and managed.", "Millions of customer windows stored outside heap to avoid memory failure."],
                ["Checkpoint interval", "How often snapshots are taken.", "Shorter intervals reduce recovery loss window but increase overhead."],
            ]
        )
        + H3("5.7  Event time, watermarks and late data")
        + p("Event time is when the business fact happened. Processing time is when the processor sees it. A "
            "watermark is the processor's estimate that it has probably seen all events up to a certain event "
            "time. Late data is an event that arrives after the processor has advanced past the window where the "
            "event belongs. This is not rare. Mobile networks, payment gateways, card networks, market feeds and "
            "legacy batch bridges can all delay events.")
        + example("Late payment event",
            p("A stream processor calculates payments above ₹1,00,000 per account in ten-minute event-time "
              "windows. At 10:10, it closes the 10:00–10:10 window after allowing two minutes of lateness. At "
              "10:13, a delayed payment event arrives with event time 10:07. The processor must choose a policy: "
              "drop it, send it to a late-event side output, update the previous result, or trigger a correction "
              "event. The right policy depends on whether the result drives a customer action, regulatory report, "
              "risk alert or dashboard.")
        )
        + table(
            ["Late-data policy", "What it does", "Use with care when"],
            [
                ["Drop after allowed lateness", "Ignores events that arrive too late.", "Fraud, sanctions or regulatory evidence cannot tolerate silent drops."],
                ["Side output", "Routes late events to a separate stream.", "Teams must monitor and resolve the side output, not leave it as a graveyard."],
                ["Update result", "Recomputes a previous aggregate.", "Downstream consumers must handle corrections and revised numbers."],
                ["Correction event", "Publishes a named adjustment.", "Business teams need clear language for what changed and why."],
            ]
        )
        + H3("5.8  Windowing — tumbling, sliding and session windows")
        + p("A window turns an endless stream into a bounded calculation. Tumbling windows do not overlap. "
            "Sliding windows overlap. Session windows group activity separated by inactivity. The window choice "
            "changes fraud sensitivity, risk numbers and alert volume.")
        + table(
            ["Window type", "How it works", "BFSI example", "Trade-off"],
            [
                ["Tumbling", "Fixed non-overlapping blocks.", "Count failed logins per customer every 5 minutes.", "Simple, but a pattern split across boundary may be missed."],
                ["Sliding", "Fixed size, advances by smaller step.", "10-minute card-spend window updated every 1 minute.", "More sensitive, more computation and possible duplicate alerts."],
                ["Session", "Groups events until inactivity gap.", "Customer digital session from login to 15 minutes of inactivity.", "Useful for journeys, but session gaps must match real behaviour."],
                ["Global with triggers", "Keeps accumulating and emits when trigger fires.", "Intraday liquidity total with periodic updates.", "Needs strong memory and correction handling."],
            ]
        )
        + H3("5.9  Schema evolution under pressure")
        + p("Schema evolution is the discipline of changing event contracts without breaking consumers. Backward "
            "compatibility means new producers can be read by old consumers. Forward compatibility means old "
            "events can be read by new consumers. Full compatibility usually means both. In a bank, schema change "
            "is a production-risk process, not a casual developer convenience.")
        + table(
            ["Change", "Usually safer", "Usually dangerous"],
            [
                ["Add field", "Add optional field with default and documentation.", "Add mandatory field with no default and break old producers."],
                ["Rename field", "Add new field, deprecate old field, migrate consumers.", "Rename directly and expect every consumer to update instantly."],
                ["Change units", "Create new version or new field such as amountMinorUnits.", "Change amount from paise to rupees in place."],
                ["Change meaning", "Create a new event or explicit version.", "Keep same name while business semantics change."],
                ["Remove field", "Deprecate only after usage evidence shows no consumers need it.", "Remove because the producer team no longer uses it."],
            ]
        )
        + red_flag(
            p("Push back if event schemas are versioned only in a wiki. The enforcement point should be in the "
              "pipeline: schema registry, compatibility checks, automated tests, sample payloads and consumer "
              "contract validation. A wiki can explain a contract; it cannot stop a bad deployment.")
        )
        + H3("5.10  Dead-letter topics, poison pills and replay lanes")
        + p("A poison-pill event is one malformed or unexpected event that repeatedly crashes a consumer. A "
            "dead-letter topic receives events that cannot be processed after defined attempts. This protects "
            "the main flow from permanent blockage, but it creates a new operational duty: somebody must inspect, "
            "fix, replay or formally close those events.")
        + table(
            ["Lane", "Purpose", "Control"],
            [
                ["Main topic", "Normal business event flow.", "Strong schema and producer validation."],
                ["Retry topic", "Temporary failures such as sink timeout.", "Backoff, attempt count and alerting."],
                ["Dead-letter topic", "Events that failed normal processing.", "Owner, ageing SLA, classification and replay tool."],
                ["Quarantine store", "Sensitive or corrupt payloads needing manual analysis.", "Strict access, audit logging and data-retention rules."],
                ["Replay topic", "Controlled reprocessing after fix.", "Change ticket, dry run, idempotency checks and reconciliation."],
            ]
        )
        + example("Dead-letter ageing as operational risk",
            p("If 0.02% of 10 million daily payment-status events go to a dead-letter topic, that is 2,000 events "
              "per day. If nobody triages them for a week, 14,000 payment facts are unresolved. The percentage "
              "looked tiny; the customer and reconciliation impact may be large. A leader should ask for dead-letter "
              "ageing by event type, rail, customer impact and owner, not just a total count.")
        )
        + H3("5.11  Security — identity, encryption, access and field-level controls")
        + p("Streaming platforms often become high-value data intersections. They may contain account identifiers, "
            "payment references, device fingerprints, merchant data, location signals, sanctions hits and fraud "
            "scores. Therefore, security controls must be designed at producer, broker, topic, schema, consumer "
            "and sink levels. Transport encryption is only one layer.")
        + table(
            ["Control", "What it protects", "BFSI design question"],
            [
                ["Mutual Transport Layer Security", "Producer and consumer connections to brokers.", "Are both sides authenticated with managed certificates and rotation?"],
                ["Topic-level authorisation", "Who can read or write each topic.", "Is access based on purpose, data classification, geography and least privilege?"],
                ["Encryption at rest", "Broker disks, backups and managed-service storage.", "Who controls keys and can support staff access plaintext?"],
                ["Field minimisation", "Reduces sensitive data inside events.", "Can token, hash or reference replace raw account or card data?"],
                ["Audit logging", "Evidence of access and admin actions.", "Can the bank prove who granted access and who consumed sensitive streams?"],
                ["Secret rotation", "Credentials and certificates over time.", "Does rotation avoid outages for 24×7 consumers?"],
            ]
        )
        + H3("5.12  Multi-region, disaster recovery and residency")
        + p("A streaming platform inside one data centre is not enough for a critical bank flow. But copying every "
            "event everywhere may violate privacy, residency or cost constraints. Multi-region design must balance "
            "latency, data sovereignty, Recovery Time Objective, Recovery Point Objective, consumer restart "
            "complexity and duplicate risk.")
        + table(
            ["Pattern", "How it behaves", "Use when", "Risk"],
            [
                ["Active-passive replication", "Primary region handles traffic, secondary receives replicated events.", "Clear failover model and strong residency control are needed.", "Failover runbook may be slow or untested."],
                ["Active-active by geography", "Each region handles local events and shares selected streams.", "Global bank needs local latency and local data control.", "Conflict resolution and duplicate detection become harder."],
                ["Central analytics copy", "Operational events remain local, selected data flows to central lakehouse.", "Global risk or finance reporting needs consolidated view.", "Central copy may breach minimisation or residency if not filtered."],
                ["No cross-region raw event copy", "Only aggregates or anonymised outputs leave region.", "Regulations or policy restrict personal/payment data movement.", "Global fraud model may lose detail and need local feature generation."],
            ]
        )
        + H3("5.13  Compaction, retention and deletion")
        + p("Retention decides how long events remain in the log. Compaction keeps the latest value per key for "
            "selected topics, useful for rebuilding current state. Deletion and privacy are harder because event "
            "logs are designed to preserve history. BFSI teams must decide which streams are operational logs, "
            "which are audit records, which are derived data, and which contain personal data subject to deletion "
            "or minimisation duties.")
        + table(
            ["Topic policy", "Meaning", "Example"],
            [
                ["Time retention", "Keep events for a defined period.", "Payment-status events kept 14 days for operational replay."],
                ["Size retention", "Keep until topic reaches storage cap.", "Low-value telemetry capped by cost."],
                ["Log compaction", "Keep latest event per key, remove older overwritten values.", "Customer preference current-state topic."],
                ["Tiered storage", "Move older log segments to cheaper storage.", "Longer replay window for analytics without expensive broker disks."],
                ["Tombstone event", "Marker that a key should be deleted in compacted topics.", "Delete customer preference projection when legally required."],
            ]
        )
        + red_flag(
            p("Push back if someone says, ‘Kafka is append-only, so deletion rules do not apply.’ Append-only "
              "engineering does not remove privacy, bank-secrecy, payment-data or retention obligations. It means "
              "the architecture must be explicit about minimisation, encryption, access, compaction, tombstones, "
              "derived copies and legal holds.")
        )
        + H3("5.14  Observability of the streaming platform itself")
        + p("Streaming observability has two layers. Platform observability watches brokers, partitions, storage, "
            "network, certificates and quotas. Business-flow observability watches whether the right business "
            "events arrived, were processed and produced expected outcomes. A green broker dashboard can coexist "
            "with a broken payment-status flow if the wrong schema was deployed or a consumer silently dropped "
            "late events.")
        + table(
            ["Signal", "Platform or business", "What to ask"],
            [
                ["Broker CPU, disk and network", "Platform", "Is infrastructure near saturation before peak windows?"],
                ["Under-replicated partitions", "Platform", "Are durability promises weakened right now?"],
                ["Consumer lag by group", "Both", "Which business action is late and by how many seconds?"],
                ["End-to-end event latency", "Business", "From event time to customer or risk action, not just broker ingestion."],
                ["Event count reconciliation", "Business", "Do produced, consumed, sink and ledger counts match by cycle?"],
                ["Schema rejection count", "Both", "Which producer deployed incompatible or invalid events?"],
                ["Dead-letter age", "Business", "Which customer-impacting events are unresolved beyond SLA?"],
            ]
        )
        + H3("5.15  Advanced section takeaway")
        + callout("Mechanisms underneath recap",
            ul([
                "Partition keys encode business ordering decisions. Wrong keys create hot partitions or broken order.",
                "Replication and acknowledgement settings decide event durability during broker failure.",
                "Exactly-once claims are scoped. External side effects still require idempotency and replay guards.",
                "Flink-style processors rely on state, checkpoints, savepoints, watermarks and late-data policy.",
                "Schema evolution must be enforced in tooling, not only documented in a wiki.",
                "Dead-letter topics, replay lanes and correction events are operational controls, not dumping grounds.",
                "Security, residency, retention and observability must be designed at event level because streams carry regulated business facts.",
            ]),
            "info")
    )
    return TopicSection("5.  Advanced — partitions, delivery semantics, state, replay and resilience underneath", "advanced", body)


def _sec6() -> TopicSection:
    body = (
        primer(
            p("Streaming looks like a technology topic until a regulator, internal audit team or operational "
              "risk committee asks a simple question: ‘Prove what happened, who saw it, where the data went, "
              "and whether the customer was harmed.’ Section 6 maps the regulatory overlay. The point is not "
              "to memorise rule numbers. The point is to see how privacy, resilience, outsourcing, payment "
              "finality, model governance and record retention change the design of event streams.")
        )
        + H3("6.1  The regulatory lens — what changes when events are regulated facts")
        + p("A bank event is rarely neutral. A payment event may contain account identifiers, payee details, "
            "merchant information, location, fraud score and customer status. A credit event may contain "
            "income, affordability and model reason codes. A trading event may contain order, execution and "
            "timestamp evidence. Once an event carries regulated facts, the streaming platform becomes part "
            "of the bank's control environment.")
        + table(
            ["Regulatory concern", "What it means for streaming", "Design evidence a leader should ask for"],
            [
                ["Privacy and data protection", "Events may contain personal data, payment data or bank-secrecy data.", "Data classification, field minimisation, masking/tokenisation, lawful basis, consent where needed, retention schedule."],
                ["Operational resilience", "Streaming may be in the critical path for fraud, payments, status, risk or regulatory evidence.", "Impact tolerance, failover design, backlog recovery, tested disaster recovery, runbooks and incident evidence."],
                ["Outsourcing and third-party risk", "Managed Kafka, cloud streams, schema tools, observability and support vendors may touch critical services.", "Vendor inventory, exit plan, subcontractor list, support-access controls, data-residency proof."],
                ["Audit and record retention", "Events may be evidence of customer communication, trade timing, fraud decision or operational incident.", "Immutable evidence store where needed, lineage, offsets, schema versions, processing job versions and retention policy."],
                ["Model and decision governance", "Fraud, credit and AML streams may feed automated or assisted decisions.", "Reason-code capture, model version, input data snapshot, monitoring, drift alerts and human-review workflow."],
                ["Financial correctness", "Event-derived dashboards must reconcile to ledger, scheme, clearing or trade-store truth.", "Daily reconciliation, exception ageing, dead-letter SLA, replay controls and sign-off trail."],
            ]
        )
        + analogy(
            p("Think of a hospital blood sample. Moving the sample quickly through a pneumatic tube is useful, "
              "but the hospital still needs patient identity, chain of custody, temperature control, authorised "
              "access and test-result audit. A bank event is similar. Speed is valuable only if custody and "
              "meaning are controlled.")
        )
        + H3("6.2  India — RBI, NPCI, DPDP and payment-data localisation")
        + p("In India, streaming often appears around UPI, IMPS, card alerts, Account Aggregator flows, fraud "
            "monitoring, digital lending and operational telemetry. The design pressure is high volume plus "
            "strong control over payment data, outsourcing and customer protection.")
        + table(
            ["India rule or expectation", "Streaming impact", "BA / architect questions"],
            [
                ["RBI Storage of Payment System Data circular, 2018", "Payment data for Indian payment systems is expected to be stored in India, with strict handling of copies and processing evidence.", "Which topics contain payment data? Are broker logs, backups, dead-letter topics, lakehouse copies and observability payloads stored in approved locations?"],
                ["RBI IT Governance Master Direction, 2023", "Banks need governance over critical information systems, change, risk and audit.", "Is the streaming platform classified as critical? Who approves schema changes, access grants, retention changes and replay operations?"],
                ["RBI Outsourcing of IT Services Master Direction, 2023", "Cloud-managed streaming, vendor support and third-party monitoring may be outsourcing arrangements.", "Which vendors can access logs, metadata or payloads? Is there an exit plan and audit right?"],
                ["Digital Personal Data Protection Act, 2023", "Event payloads containing personal data need purpose limitation, security safeguards and retention discipline.", "Can we explain why each personal field is in the event and when it is deleted or minimised?"],
                ["NPCI UPI operating expectations", "UPI status and reconciliation events must support customer status, dispute handling and operational investigation.", "Can we trace a UPI payment from initiation to debit, credit, reversal, customer notification and reconciliation?"],
                ["RBI Digital Lending Guidelines", "Loan events around consent, Key Fact Statement, disbursal and repayments may be evidence.", "Does the event trail prove consent, direct disbursal, fee disclosure, cooling-off and grievance handling?"],
            ]
        )
        + example("India payment-data localisation trap",
            p("A bank keeps its UPI payment topic in an Indian region but exports Kafka consumer logs to a global "
              "observability tool. The logs include full payer Virtual Payment Address, payee Virtual Payment "
              "Address, amount and failure reason. The main event store is local, but the copied logs may still "
              "create a localisation and privacy problem. A good design masks sensitive fields before logs leave "
              "the controlled zone and treats dead-letter topics and observability as regulated data paths.")
        )
        + H3("6.3  United States — GLBA, FFIEC, OFAC, CFPB, FedNow and market evidence")
        + p("In the United States, streaming controls are shaped by privacy, bank supervision, sanctions, fair "
            "lending, real-time payments, broker-dealer records and operational resilience. The estate is often "
            "fragmented: mainframes, vendor cores, card processors, ACH, RTP, FedNow, loan platforms and data "
            "warehouses coexist.")
        + table(
            ["US rule or expectation", "Streaming impact", "BA / architect questions"],
            [
                ["GLBA Safeguards Rule and bank privacy obligations", "Customer financial information in events needs access control, encryption and monitoring.", "Which consumer groups can read customer financial data and what is their approved business purpose?"],
                ["FFIEC technology and cyber guidance", "Event platforms are part of supervised technology risk management.", "Are monitoring, incident response, backup, recovery and access reviews documented?"],
                ["OFAC sanctions screening", "Payment and customer events may trigger sanctions decisions before release.", "Can we prove which sanctions list version, input fields, match score and decision were used for a held payment?"],
                ["CFPB and fair-lending obligations", "Credit decision streams may carry model features and reason codes.", "Can declined or priced credit decisions be reproduced with model version, data inputs and adverse-action reasons?"],
                ["FedNow and RTP real-time payments", "Fraud and status events must act within much shorter windows than legacy batch rails.", "Which decisions are synchronous in the payment path and which are post-event monitoring only?"],
                ["SEC and CFTC recordkeeping for trading", "Order, execution and market-data events may be records requiring retention and searchability.", "Are trading event timestamps, sequence, clock sync and replay evidence retained according to policy?"],
           ]
        )
        + H3("6.4  United Kingdom — FCA Consumer Duty, operational resilience and APP fraud")
        + p("In the United Kingdom, customer outcomes and operational resilience are central. Faster Payments, "
            "Open Banking, Confirmation of Payee and authorised push payment fraud controls make event timing "
            "and decision evidence especially important.")
        + table(
            ["UK rule or expectation", "Streaming impact", "BA / architect questions"],
            [
                ["FCA Consumer Duty, July 2023", "Customer communications and decisions must support good outcomes.", "Does the event-driven status shown to the customer reduce confusion, duplicate payments and complaint risk?"],
                ["UK operational resilience rules, fully embedded March 2025", "Important business services need impact tolerances and tested recovery.", "If the streaming platform fails, can Faster Payments status, fraud controls and customer support stay within impact tolerance?"],
                ["APP fraud reimbursement rules from October 2024", "Fraud-warning, Confirmation of Payee, payment-hold and reimbursement evidence become critical.", "Can we reconstruct what warning was shown, what risk score fired, what customer action followed and whether delay changed liability?"],
                ["Open Banking and data-sharing governance", "Events may be generated from account-information and payment-initiation flows.", "Are consent, scope, expiry and data minimisation carried through event consumers?"],
                ["PRA and FCA outsourcing and third-party risk", "Cloud streaming and managed services require governance and exit.", "Which parts of the event platform are outsourced and how quickly can the bank recover or exit?"],
            ]
        )
        + H3("6.5  Eurozone — DORA, GDPR, Instant Payments Regulation and SEPA Instant")
        + p("The Eurozone overlay combines strict privacy with a major resilience regime. DORA, the Digital "
            "Operational Resilience Act, applies from 17 January 2025 and pushes banks to treat Information and "
            "Communication Technology resilience, third-party risk and incident reporting as board-level control "
            "topics. GDPR, the General Data Protection Regulation, shapes what fields can be copied, retained "
            "and reused. SEPA Instant and the EU Instant Payments Regulation increase real-time payments pressure.")
        + table(
            ["EU rule or expectation", "Streaming impact", "BA / architect questions"],
            [
                ["DORA, applicable from 17 January 2025", "Streaming platforms supporting important services need resilience testing, incident classification and third-party governance.", "Is Kafka, Pulsar, Flink or cloud streaming in the important-service dependency map and DORA testing scope?"],
                ["GDPR", "Personal-data events require lawful basis, minimisation, access control, retention and data-subject-right handling.", "Can the bank locate every topic, dead-letter queue, replay copy and derived store containing a customer's personal data?"],
                ["EU Instant Payments Regulation, adopted 2024", "Euro instant payments increase pressure for real-time screening, fraud detection and customer status.", "Can screening and fraud controls act before release without breaching payment service-level expectations?"],
                ["SEPA Instant and TIPS", "Payment events need clear status, timestamp and reconciliation across participants.", "Which event is customer-visible finality versus internal processing state?"],
                ["EU AI Act, in force 2024 with phased obligations", "Credit scoring and some fraud models may be high-risk or tightly governed.", "Do event features and decisions preserve model version, input lineage, human oversight and monitoring evidence?"],
                ["NIS2 and Cyber Resilience Act", "Critical digital-service and software-supply-chain controls affect platform operations.", "Are dependencies, vulnerabilities and supplier controls visible for the streaming stack?"],
            ]
        )
        + H3("6.6  Singapore — MAS technology risk, outsourcing and real-time rails")
        + p("Singapore is often a regional hub for global banks, so the question is not only ‘does the stream "
            "work in Singapore?’ It is also ‘which regional teams, vendors and countries can see the data?’ MAS "
            "technology-risk and outsourcing expectations make access, resilience and control evidence central.")
        + table(
            ["Singapore rule or expectation", "Streaming impact", "BA / architect questions"],
            [
                ["MAS Technology Risk Management Guidelines", "Streaming platforms need strong access, resilience, monitoring, incident and change controls.", "Are privileged broker and schema-registry actions logged, reviewed and controlled?"],
                ["MAS Outsourcing Guidelines", "Managed streaming, cloud, support and regional operations may be outsourcing dependencies.", "What is the outsourcing register entry, materiality rating, exit plan and audit evidence?"],
                ["MAS FEAT principles for AI in finance", "Event-driven AI decisions in credit, fraud or customer treatment need fairness, ethics, accountability and transparency.", "Does the event trail support explainability and human accountability for automated decisions?"],
                ["FAST and PayNow", "Always-on payment rails need timely fraud, status and reconciliation events.", "Can delayed or duplicate payment-status events cause customer harm or wrong operational action?"],
                ["Regional treasury and wealth hubs", "Events may cross booking centres, branches and processing hubs.", "What data crosses borders, and is it raw event data, derived data, anonymised data or operational metadata?"],
            ]
        )
        + H3("6.7  Other markets to recognise — Brazil, UAE, Australia and Hong Kong")
        + table(
            ["Market", "Streaming relevance", "Design pressure"],
            [
                ["Brazil", "Pix instant payments, Open Finance and strong fraud controls create high-volume real-time event use cases.", "Fraud, consent, customer status and chargeback/dispute evidence need event-level lineage."],
                ["UAE", "Digital-banking growth, cross-border payments, Islamic finance, data-protection and central-bank supervision.", "Cloud region choice, outsourcing, payment screening and Sharia-product event semantics need care."],
                ["Australia", "New Payments Platform, Consumer Data Right, APRA CPS 230 operational risk management from July 2025.", "Important operations, service-provider dependencies and payment events need strong resilience evidence."],
                ["Hong Kong", "Faster Payment System, virtual banks, wealth and regional treasury activity.", "Cross-border access, cyber resilience and customer-data controls are central for regional platforms."],
            ]
        )
        + H3("6.8  Data classification matrix for event streams")
        + table(
            ["Event type", "Example fields", "Likely classification", "Control expectation"],
            [
                ["Payment status", "Payment ID, amount, currency, payer, payee, rail, reason code.", "Payment data plus personal data.", "Localisation where required, masking, strict topic access, reconciliation and retention."],
                ["Card authorisation", "Token, merchant category, amount, location, risk score.", "Payment and fraud-sensitive data.", "Low latency, fraud evidence, tokenisation, restricted replay."],
                ["Credit decision", "Income, bureau score, model features, reason codes.", "Personal, credit and model-risk data.", "Explainability, model version, consent and retention."],
                ["AML or sanctions alert", "Customer, counterparty, match score, list version.", "Highly sensitive financial-crime data.", "Need-to-know access, audit logs, case linkage and legal hold policy."],
                ["Market trade event", "Order ID, execution time, price, trader, venue.", "Market conduct and recordkeeping data.", "Timestamp accuracy, immutable evidence, surveillance integration."],
                ["Technology telemetry", "Service name, latency, pod, host, error code.", "Operational data, sometimes sensitive if payloads leak.", "No customer payloads in logs, incident linkage, retention by operational need."],
            ]
        )
        + H3("6.9  Reconciliation and evidence by region")
        + p("Regulators rarely accept ‘the stream said so’ as final truth. Evidence needs reconciliation. Payment "
            "events reconcile to ledger postings, scheme reports and customer notifications. Trading events "
            "reconcile to order management, execution venues and confirmations. Credit events reconcile to "
            "decision records, documents and loan booking.")
        + table(
            ["Flow", "Source of operational truth", "Event evidence should prove"],
            [
                ["UPI or IMPS payment", "Payment hub, ledger, NPCI or bank reports.", "Every status event corresponds to a real status transition and customer notification wording."],
                ["FedNow or RTP payment", "Payment rail response, bank ledger and fraud case system.", "Screening and fraud decisions happened before or after release according to policy."],
                ["Faster Payments APP fraud flow", "Payment hub, Confirmation of Payee, fraud engine, customer warning log.", "Warning, customer action, hold or release decision and reimbursement evidence."],
                ["SEPA Instant payment", "Payment engine, TIPS or clearing feedback, ledger.", "Customer-visible status and finality are not confused with internal processing state."],
                ["Credit decision", "LOS, decisioning engine, model registry and LMS booking.", "Decision inputs, model version, reason codes and booking terms align."],
                ["Trade surveillance", "Order management system, execution venue, market data and surveillance platform.", "Event sequence, timestamp and replay reproduce the monitored conduct scenario."],
            ]
        )
        + H3("6.10  Regulatory overlay takeaway")
        + callout("What regulation changes",
            ul([
                "A BFSI event stream is often a regulated evidence trail, not just a data pipe.",
                "Privacy, localisation, outsourcing, operational resilience, model governance and recordkeeping all affect topic design.",
                "Dead-letter topics, observability logs, backups and replay stores are part of the regulated data path.",
                "Each region has a different pressure point: India localisation, US sanctions and fair lending, UK outcomes and APP fraud, Eurozone DORA and GDPR, Singapore outsourcing and regional access.",
                "A leader should ask for event lineage, access evidence, retention policy, resilience tests and reconciliation proof before trusting real-time decisions.",
            ]),
            "info")
    )
    return TopicSection("6.  BFSI and regulatory overlay — what changes because events carry regulated facts", "advanced", body)


def _sec7() -> TopicSection:
    body = (
        primer(
            p("Section 7 is the leader's decision section. Engineers can explain how to create topics, consumers "
              "and processors. A techno-functional leader decides which business promises deserve real time, "
              "which events become contracts, which data may move, which platform is acceptable, what failure "
              "the bank can tolerate, and where accountability sits when an automated event-driven action harms "
              "a customer.")
        )
        + H3("7.1  Decision 1 — real time, near real time, micro-batch or batch")
        + p("Not every process deserves streaming. Real time is expensive because it requires 24×7 operations, "
            "observability, retries, replay, incident response and careful side-effect control. Batch remains "
            "good when the business value does not decay quickly.")
        + table(
            ["Use case", "Best timing pattern", "Why"],
            [
                ["Card authorisation fraud score", "Real time in the approval path.", "The decision must happen before approval or decline."],
                ["UPI customer status", "Real time or near real time.", "Stale status causes duplicate payments, complaints and support load."],
                ["IFRS 9 month-end provisioning", "Batch or controlled micro-batch.", "Correctness, audit and sign-off matter more than sub-second speed."],
                ["Market risk intraday limits", "Streaming with short windows.", "Positions and prices change during the trading day."],
                ["Monthly customer statement", "Batch.", "Customer value does not require event-by-event statement generation."],
                ["Operational incident detection", "Streaming telemetry and business events.", "Early detection can reduce customer impact."],
            ]
        )
        + example("The latency-cost decision",
            p("A bank wants every loan repayment event reflected in analytics. If the analytics dashboard is used "
              "for morning portfolio review, a 15-minute micro-batch may be enough. If the same event releases a "
              "blocked credit line for a corporate customer, 15 minutes may be unacceptable. The same data item can "
              "need different timing for different decisions. A leader should define the business decision first, "
              "then the latency target.")
        )
        + H3("7.2  Decision 2 — what should become an event contract")
        + p("An event contract is a promise to other teams. Once many consumers depend on it, changing the event "
            "becomes a governance act. Publish too few events and the bank remains tightly coupled. Publish too "
            "many weak events and the bank creates a noisy, expensive rumour network.")
        + table(
            ["Candidate event", "Should it be a shared contract?", "Reason"],
            [
                ["<code>payment_status_changed</code>", "Usually yes.", "Many teams need status, but it must carry clear lifecycle meaning."],
                ["<code>customer_clicked_button</code>", "Usually no for enterprise event backbone.", "Useful for product analytics, not usually a regulated domain event."],
                ["<code>ledger_posting_committed</code>", "Yes, with strong controls.", "Money-state fact used by reconciliation, finance and customer views."],
                ["<code>debug_validation_failed</code>", "No as a domain event.", "Belongs in observability unless it has business meaning."],
                ["<code>sanctions_case_opened</code>", "Yes, restricted.", "Sensitive financial-crime workflow fact with strict access."],
                ["<code>credit_offer_accepted</code>", "Yes for lending workflows.", "Triggers booking, documentation, disclosure and downstream servicing."],
            ]
        )
        + red_flag(
            p("Push back if every database table change is declared an enterprise event contract. Table changes "
              "can feed integration, but stable business events need names, owners, semantics, schema versioning "
              "and consumer commitments.")
        )
        + H3("7.3  Decision 3 — central platform, domain platforms or product-owned streams")
        + p("A tier-1 bank may have a central streaming platform team, domain platforms for payments or markets, "
            "and product teams that own their own event contracts. The decision is organisational as much as "
            "technical.")
        + table(
            ["Operating model", "When it works", "Watch-out"],
            [
                ["Central streaming platform team", "Bank wants common brokers, standards, security and operations.", "Can become a bottleneck if it owns business semantics it does not understand."],
                ["Domain-owned event platforms", "Payments, cards, markets or risk have specialised volume and rules.", "Can fragment tooling and governance if each domain invents its own standards."],
                ["Product-team-owned streams on shared platform", "Mature engineering teams own event contracts while using common guardrails.", "Needs strong schema registry, catalogue, access workflow and production support discipline."],
                ["Managed cloud streaming service", "Bank wants faster provisioning and less broker operations.", "Outsourcing, data residency, support access and exit plan become board-level questions."],
            ]
        )
        + H3("7.4  Decision 4 — build, buy, managed service or vendor event backbone")
        + table(
            ["Choice", "Best fit", "Leader questions"],
            [
                ["Self-managed Kafka or Pulsar", "Large banks with strong platform engineering, on-prem or private-cloud needs.", "Can we operate upgrades, certificates, quotas, disaster recovery and capacity 24×7?"],
                ["Confluent Cloud or managed Kafka", "Banks that want Kafka ecosystem with reduced broker operations.", "Which regions, keys, logs, subcontractors and support staff can access regulated data?"],
                ["Cloud-native stream services", "Cloud-aligned workloads on AWS, Azure or Google Cloud.", "Do ordering, replay, retention and portability match BFSI requirements?"],
                ["Vendor-domain event backbone", "Payment hub, core banking or trading platform includes its own event model.", "Are events open, documented and governable, or locked inside vendor tooling?"],
                ["Enterprise service bus plus messaging", "Legacy estates where assured delivery and transformation dominate.", "Are we solving work distribution and integration, or do we need replayable event logs?"],
            ]
        )
        + H3("7.5  Decision 5 — topic granularity and ownership")
        + p("Topic granularity decides whether events are understandable and controllable. One giant topic for "
            "all payments is easy to create but hard to govern. Hundreds of tiny topics may overwhelm consumers "
            "and operations. The leader should force each topic to have a business owner and an operational owner.")
        + table(
            ["Granularity choice", "Good when", "Bad when"],
            [
                ["One topic per broad domain", "Low volume, few consumers, early discovery.", "Different events have different schemas, access rules and retention needs."],
                ["One topic per event family", "Payment status, card authorisation, customer consent each need clear contracts.", "Teams create too many nearly identical topics with weak ownership."],
                ["One topic per product or rail", "UPI, Faster Payments, SEPA Instant or cards have distinct rules.", "Consumers need a unified business view and must subscribe to many topics."],
                ["Compacted current-state topic plus event-history topic", "Consumers need both latest view and full history.", "Teams confuse current-state snapshots with audit history."],
            ]
        )
        + H3("7.6  Decision 6 — event payload richness versus privacy and coupling")
        + table(
            ["Payload style", "Benefit", "Risk", "Use when"],
            [
                ["Thin event with identifiers", "Minimises data exposure and payload cost.", "Consumers call source systems and may create load or coupling.", "Details are sensitive or rarely needed."],
                ["Rich event-carried state", "Consumers can act independently and build views quickly.", "Spreads data widely and increases schema-change impact.", "Many authorised consumers need the same fields immediately."],
                ["Reference plus secure lookup", "Balances minimisation with access-controlled detail retrieval.", "Adds lookup latency and dependency.", "Sensitive details are needed by a subset of consumers."],
                ["Derived event", "Exposes decision result rather than raw inputs.", "Consumers may lose explainability if lineage is missing.", "Fraud score, credit decision or risk signal needs controlled sharing."],
            ]
        )
        + example("Payload decision for fraud",
            p("A fraud model may use 120 features, including device, location, behavioural history and beneficiary "
              "risk. Publishing all 120 fields to a broad event topic is rarely justified. A safer design may publish "
              "a fraud-decision event with score band, reason codes, model version and decision ID, while keeping raw "
              "features in a restricted feature store accessible only to authorised fraud and model-risk teams.")
        )
        + H3("7.7  Decision 7 — ordering, latency and throughput trade-off")
        + table(
            ["Priority", "Design implication", "Trade-off"],
            [
                ["Strict order per account", "Key by account or maintain per-account sequencing.", "Large accounts may become hot partitions."],
                ["Maximum throughput", "Increase partitions and distribute keys widely.", "Business ordering may be weaker or require downstream correction."],
                ["Lowest latency", "Reduce batching and synchronous dependencies.", "Cost rises and durability choices must be reviewed."],
                ["Strong durability", "Wait for more acknowledgements and replicas.", "Latency may rise, especially during degraded cluster health."],
                ["Easy replay", "Longer retention, idempotent consumers and replay tooling.", "Storage, privacy and side-effect complexity increase."],
            ]
        )
        + H3("7.8  Decision 8 — retention, replay and legal hold")
        + p("Replay is one of streaming's most valuable features, but a replayable log is also a retention and "
            "privacy responsibility. A leader should separate operational replay from audit retention. They are "
            "not always the same store.")
        + table(
            ["Retention decision", "Example", "Leader trade-off"],
            [
                ["Short operational retention", "Keep payment events 7 to 14 days for consumer recovery.", "Lower cost and privacy exposure, limited rebuild history."],
                ["Long analytical retention", "Copy selected events to lakehouse for 7 years where policy permits.", "Better analytics and audit, higher governance burden."],
                ["Immutable evidence store", "Trade or customer-warning evidence retained in controlled archive.", "Strong proof, stricter access and legal-hold process."],
                ["Compacted state topic", "Keep latest customer preference per key.", "Efficient current-state rebuild, not a full audit trail."],
                ["Deletion or tombstone support", "Remove preference projection after lawful deletion request.", "Must propagate to derived copies and prove completion."],
            ]
        )
        + H3("7.9  Decision 9 — who can replay and who approves it")
        + p("Replay is a production action. Replaying the wrong events can duplicate customer messages, reopen cases, "
            "retrigger payment holds or corrupt derived tables. The leader should insist on a replay control model.")
        + table(
            ["Replay control", "Weak version", "Strong version"],
            [
                ["Approval", "Developer decides during incident.", "Change or incident approval with business owner, risk and operations visibility."],
                ["Scope", "Replay from yesterday roughly.", "Exact topic, partition, offset, event-time window, consumer group and sink impact defined."],
                ["Dry run", "No pre-check.", "Replay into test or shadow sink to compare counts and side effects."],
                ["Idempotency", "Assumed.", "Evidence that each sink deduplicates by event ID or business key."],
                ["Communication", "Only engineering knows.", "Operations, customer support and affected business teams know expected impact."],
                ["Reconciliation", "Hope dashboard looks right.", "Post-replay counts, exceptions and ledger/source reconciliation signed off."],
            ]
        )
        + H3("7.10  Decision 10 — customer-facing status and wording")
        + p("Event-driven status is not just internal state. It becomes words customers read: pending, processing, "
            "failed, reversed, held, completed. A misleading status can create complaints and regulatory exposure. "
            "Leaders should own the boundary between internal lifecycle events and customer-visible language.")
        + table(
            ["Internal event", "Unsafe customer wording", "Safer wording"],
            [
                ["<code>debit_confirmed</code>", "Payment successful.", "Money debited, beneficiary confirmation pending."],
                ["<code>fraud_review_started</code>", "Payment failed.", "Payment is under review for your protection."],
                ["<code>rail_timeout</code>", "Beneficiary did not receive money.", "We are checking the payment status with the payment network."],
                ["<code>credit_decision_referred</code>", "Loan rejected.", "Application needs manual review."],
                ["<code>reversal_posted</code>", "Original payment never happened.", "Refund or reversal has been posted."],
            ]
        )
        + H3("7.11  Decision 11 — control metrics on the executive dashboard")
        + p("A streaming platform dashboard should not stop at broker health. Executives need business and control "
            "metrics that translate technology into customer, risk and regulatory impact.")
        + table(
            ["Metric", "Technical version", "Leader version"],
            [
                ["Consumer lag", "Offsets behind latest.", "Fraud decisions for card stream are 35 seconds late at peak."],
                ["End-to-end latency", "Broker ingest to sink write.", "UPI customer status delivered at p95 700 milliseconds, p99 2.8 seconds."],
                ["Dead-letter count", "Number of failed events.", "312 payment events unresolved beyond 15-minute SLA, 18 customer-impacting."],
                ["Replay count", "Number of replay jobs.", "Three production replays this month, all reconciled, no duplicate side effects."],
                ["Schema failure", "Compatibility rejection.", "One producer blocked from deploying incompatible card amount field."],
                ["Access exceptions", "Unauthorised read attempts.", "Two denied attempts to read sanctions-alert topic, investigated and closed."],
                ["Reconciliation break", "Count mismatch.", "Payment status stream is 27 events short versus payment hub for cycle."],
            ]
        )
        + H3("7.12  Decision 12 — funding and operating model")
        + p("Many streaming programmes fail because they are funded like a one-time middleware install. A real "
            "event backbone needs product ownership, platform operations, schema governance, data stewardship, "
            "security review, consumer onboarding, resilience testing and support. The leader owns this operating "
            "model.")
        + table(
            ["Capability", "Minimum operating commitment", "Failure symptom if unfunded"],
            [
                ["Platform operations", "24×7 monitoring, capacity, patching, certificates, disaster recovery.", "Broker incidents become business outages."],
                ["Event governance", "Schema review, catalogue, ownership, lifecycle, deprecation.", "Consumers depend on undocumented topics."],
                ["Security and privacy", "Access workflow, classification, masking, audit and review.", "Sensitive data spreads through uncontrolled consumers."],
                ["Consumer onboarding", "Templates, standards, testing, support and runbooks.", "Every consumer reinvents retries and idempotency."],
                ["Data quality and reconciliation", "Expected counts, source matching, exception workflow.", "Dashboards drift from ledger truth."],
                ["Training and BA enablement", "Business analysts can read events, lineage, schemas and controls.", "Requirements stay screen-based and miss event semantics."],
            ]
        )
        + H3("7.13  Decision matrix — leader choices in one view")
        + table(
            ["Decision", "Option A", "Option B", "When to choose A", "When to choose B"],
            [
                ["Timing", "Streaming", "Batch", "Decision value decays in seconds or minutes.", "Correctness and sign-off matter more than freshness."],
                ["Platform", "Self-managed", "Managed cloud", "Control, locality and custom operations dominate.", "Speed and reduced infrastructure operations dominate, with outsourcing controls accepted."],
                ["Payload", "Thin", "Rich", "Privacy and source ownership dominate.", "Many authorised consumers need immediate independent action."],
                ["Retention", "Short operational", "Long evidence", "Replay window is operational only.", "Audit, dispute, conduct or regulatory recordkeeping requires history."],
                ["Ownership", "Central platform", "Domain-owned events", "Common controls are weak or duplicated.", "Domain semantics and specialised volume dominate."],
                ["Processing", "Simple consumers", "Stateful processor", "Each event can be handled alone.", "Patterns, joins, windows or aggregations are required."],
                ["Replay", "Manual controlled", "Self-service guarded", "Low maturity or high side-effect risk.", "Strong tooling, dry runs, idempotency and approvals exist."],
            ]
        )
        + H3("7.14  Red-flag decisions to challenge")
        + red_flag(
            ul([
                "‘Make everything real time.’ Real time without business value creates cost, complexity and operational risk.",
                "‘Keep all events forever.’ Retention must balance replay, audit, privacy, legal hold and cost.",
                "‘Everyone can subscribe.’ Least privilege applies to event streams as much as databases.",
                "‘Kafka replay will fix it.’ Replay without idempotency and approval can create a second incident.",
                "‘The platform team owns event meaning.’ Business domains own semantics; platform owns shared machinery.",
                "‘Customer status is just a UI label.’ Status wording is a customer-outcome and complaint-risk control.",
                "‘Managed service means no operational responsibility.’ The bank still owns outsourcing, resilience and customer impact.",
            ])
        )
        + H3("7.15  Section 7 takeaway")
        + callout("Leader decision recap",
            ul([
                "A leader decides where real time is worth the control cost.",
                "Event contracts are business promises with owners, schemas, access rules, retention and deprecation paths.",
                "Platform choice is also an outsourcing, data-residency and operating-model decision.",
                "Replay, retention, customer status and dashboard metrics need explicit governance.",
                "The best executive dashboard translates offsets and lag into fraud, payment, customer, risk and regulatory impact.",
            ]),
            "info")
    )
    return TopicSection("7.  Trade-offs and decisions a leader owns — timing, contracts, platforms, replay and accountability", "intermediate", body)


def _sec8() -> TopicSection:
    body = (
        primer(
            p("Section 8 turns the previous sections into boardroom-grade examples. Each example starts "
              "with a business moment, gives numbers, shows the streaming design, then forces a leader "
              "decision. The aim is not to memorise Kafka commands. The aim is to hear a proposal in a "
              "design review and quickly ask: what is the event, who owns it, what is the value of speed, "
              "what can go wrong, and how will we prove control?")
        )
        + H3("8.1  How to read these examples")
        + p("Every worked example uses the same pattern. First identify the event that represents a "
            "meaningful business fact. Then estimate volume, latency, financial impact and control risk. "
            "Only after that choose whether you need a durable log, stateful processing, replay, long "
            "retention, customer messaging or a simpler batch approach.")
        + table(
            ["Question", "Plain-English meaning", "Why it matters"],
            [
                ["What fact happened?", "The business event, not the screen or database table.", "Prevents vague topics such as <code>digital_events</code> that nobody owns."],
                ["How fast does the decision lose value?", "Seconds, minutes, hours or next day.", "Separates true streaming use cases from expensive fashion."],
                ["What is the key?", "Account, card, customer, payment, trade or device identifier.", "Controls ordering, partitioning, state and reconciliation."],
                ["What is the evidence?", "Counts, event IDs, offsets, timestamps, rules and outcomes.", "Lets audit, operations and regulators reconstruct what happened."],
                ["What side effect happens?", "Hold a payment, send a notification, create a case, update a model.", "Determines idempotency, replay approvals and customer harm controls."],
            ]
        )
        + mermaid(
            "flowchart TB\n"
            "  A[Business moment] --> B[Named event]\n"
            "  B --> C[Volume and latency estimate]\n"
            "  C --> D[Control design]\n"
            "  D --> E[Streaming platform choice]\n"
            "  E --> F[Operational evidence]\n"
            "  F --> G[Leader decision]",
            "Figure 8.1 — A streaming worked example should move from business moment to evidence, not from product name to product name."
        )
        + H3("8.2  Worked example 1 — India UPI payment status repair")
        + example("UPI status stream with customer wording and reconciliation",
            p("A bank in India processes 12 million Unified Payments Interface (UPI) transactions per day. "
              "During evening peak it sees 2,000 payment attempts per second. Most complete quickly, but "
              "0.35% enter an uncertain state because the bank debited the customer, then did not receive "
              "a final network response before the timeout. That sounds small, but 0.35% of 12 million is "
              "42,000 uncertain payment journeys per day. If the mobile app simply says ‘failed’, many "
              "customers retry, contact support or complain.")
            + table(
                ["Input", "Number", "Meaning"],
                [
                    ["Daily UPI attempts", "12,000,000", "All customer payment attempts across the bank."],
                    ["Timeout or pending rate", "0.35%", "Transactions where status is not final at first response."],
                    ["Uncertain journeys", "42,000 per day", "12,000,000 × 0.0035."],
                    ["Average customer ticket", "₹1,850", "Low-ticket retail payments still create high complaint volume."],
                    ["Support contact rate if unclear", "8%", "Around 3,360 contacts per day if wording and status are weak."],
                ]
            )
            + p("The streaming design publishes <code>upi_payment_status_changed</code> events whenever the "
              "payment hub learns a new fact: initiated, debit posted, network pending, credit confirmed, "
              "reversal initiated, reversal posted. The customer app does not invent its own status. It "
              "consumes a controlled customer-status projection that maps internal events into approved "
              "wording such as ‘Payment is being confirmed with the receiving bank’ rather than ‘failed’.")
            + table(
                ["Design choice", "Recommended answer", "Reason"],
                [
                    ["Event key", "Payment reference plus customer account", "Keeps all lifecycle events for one payment ordered."],
                    ["Producer", "Payment orchestration hub", "The system closest to payment state owns the event."],
                    ["Consumers", "Customer status, operations dashboard, reconciliation, support view", "Each has a different reaction to the same fact."],
                    ["Latency target", "p95 under 1 second for status projection", "Customers need fast reassurance, but ledger correctness still wins."],
                    ["Retention", "Short operational stream plus formal evidence store", "Raw event replay is useful, but dispute evidence may need longer controlled retention."],
                    ["Replay control", "Approved replay by payment ID and time window", "Replaying customer notifications blindly can create confusion."],
                ]
            )
            + callout("Leader decision",
                p("Approve streaming for customer status and operations because the value of speed is high: "
                  "it reduces duplicate payments, support calls and complaint risk. Do not approve a design "
                  "where the mobile app reads raw internal events directly. The app should read a governed "
                  "customer-status projection with approved wording, evidence and reconciliation."),
                "info")
        )
        + H3("8.3  Worked example 2 — United States card fraud decision inside 150 milliseconds")
        + example("Card authorisation fraud stream",
            p("A United States issuer receives 180 million card authorisation requests per day, with a peak "
              "of 5,000 requests per second during shopping windows. The network decision budget is tight: "
              "the issuer must usually decide in a few hundred milliseconds. Suppose the bank allocates "
              "150 milliseconds to fraud scoring so the rest of the authorisation path can check funds, "
              "limits and response formatting.")
            + table(
                ["Item", "Number", "Implication"],
                [
                    ["Peak authorisations", "5,000 per second", "The stream must scale horizontally."],
                    ["Fraud scoring budget", "150 milliseconds", "Slow joins or remote database calls can break the customer experience."],
                    ["False-decline target", "Below 0.25%", "Overblocking legitimate customers damages trust and revenue."],
                    ["High-risk rule", "3 declined attempts plus new merchant country within 20 minutes", "Requires stateful memory, not just one-event checks."],
                    ["Average prevented fraud amount", "$210", "Small improvements can be financially material at large volume."],
                ]
            )
            + p("The bank uses a card-authorisation topic keyed by card token. A stream processor maintains "
              "short-lived state: recent declines, merchant countries, device confidence, velocity by card "
              "and customer, and merchant risk. For a suspicious pattern, it emits "
              "<code>card_authorisation_risk_scored</code> with score, reason codes and model version. "
              "The authorisation service still makes the final approve or decline decision.")
            + p("Now calculate the operational value. If improved streaming rules catch only 0.02% additional "
              "fraudulent authorisations at peak-day scale, that is 36,000 events across 180 million requests. "
              "At $210 average prevented loss, the theoretical gross value is $7.56 million. The real value "
              "will be lower after false positives, investigation cost and merchant disputes, but the example "
              "shows why milliseconds can matter.")
            + table(
                ["Risk", "Control"],
                [
                    ["Model or rule blocks good customers", "Champion/challenger monitoring, false-decline dashboards and reason-code analysis."],
                    ["Late features cause timeout", "Local state in the stream processor, not synchronous calls to ten systems."],
                    ["Duplicate event creates duplicate case", "Idempotency by authorisation ID and model version."],
                    ["Replay retriggers customer decline", "Replay into shadow sink for analytics unless explicitly approved for operational action."],
                    ["Sensitive card data spreads", "Tokenisation, masking, field-level access and audit on fraud topics."],
                ]
            )
            + callout("Leader decision",
                p("Approve streaming and stateful processing for fraud scoring because the decision value "
                  "decays in milliseconds. Insist that the design separates scoring from final authorisation, "
                  "records model version and reason codes, and proves that replay cannot silently decline "
                  "customers a second time."),
                "info")
        )
        + H3("8.4  Worked example 3 — United Kingdom APP fraud monitoring for Faster Payments")
        + example("Authorised Push Payment scam pattern",
            p("A United Kingdom retail bank sees a customer add a new payee, pass mobile authentication, "
              "and send £18,750 by Faster Payments within six minutes. The payment is technically authorised "
              "by the customer, but it may be an Authorised Push Payment (APP) scam. Since mandatory APP "
              "fraud reimbursement rules came into force in the United Kingdom in October 2024, the quality "
              "of scam detection, warnings, customer friction and evidence matters commercially and conduct-wise.")
            + table(
                ["Event stream", "Example event", "Why it matters"],
                [
                    ["Login stream", "<code>login_succeeded_new_device</code>", "A new device before a high-value payment increases risk."],
                    ["Payee stream", "<code>new_payee_created</code>", "Scam payments often involve new or changed beneficiary details."],
                    ["Confirmation stream", "<code>confirmation_of_payee_mismatch</code>", "Name mismatch is a direct risk signal."],
                    ["Payment stream", "<code>faster_payment_initiated</code>", "Amount, timing and payee history drive the decision."],
                    ["Customer interaction stream", "<code>warning_acknowledged</code>", "Evidence of the warning shown and customer response is important."],
                ]
            )
            + p("A stream processor joins these events by customer ID and payee ID over a 30-minute window. "
              "The rule does not say ‘block every new payee’. It scores a pattern: new device, new payee, "
              "Confirmation of Payee mismatch, high amount relative to customer history, and rapid progression "
              "through screens. If the score is high, the payment journey can add friction: stronger warning, "
              "cooling-off, call-back or manual review depending on policy.")
            + table(
                ["Decision", "Weak answer", "Strong answer"],
                [
                    ["Customer warning", "Generic scam warning on every payment.", "Event-driven warning explains the specific risk pattern in plain language."],
                    ["Evidence", "Screenshot may or may not exist.", "Event records warning text version, timestamp, channel and customer action."],
                    ["Customer fairness", "All large payments delayed.", "Risk-based friction with vulnerable-customer and accessibility considerations."],
                    ["Operations", "Manual queue floods.", "Thresholds sized against team capacity and customer harm appetite."],
                    ["Regulatory posture", "Fraud model is a black box.", "Reason codes and outcome monitoring support conduct review."],
                ]
            )
            + callout("Leader decision",
                p("Approve event correlation because no single event proves a scam. The value comes from "
                  "joining time-ordered signals. Challenge any design that cannot show the exact warning, "
                  "risk reason, decision timestamp and customer response for a disputed case."),
                "info")
        )
        + H3("8.5  Worked example 4 — Eurozone SEPA Instant operational resilience")
        + example("SEPA Instant backlog under incident conditions",
            p("A Eurozone bank joins SEPA Instant Credit Transfer processing. Customers expect near-real-time "
              "euro payments, and European operational-resilience expectations are stricter after the Digital "
              "Operational Resilience Act (DORA) became applicable on 17 January 2025. The bank processes "
              "900 instant payments per second at peak. During an incident, one downstream sanctions consumer "
              "slows from 900 events per second to 300 events per second for 12 minutes.")
            + table(
                ["Metric", "Number", "Calculation"],
                [
                    ["Incoming rate", "900 events per second", "Payment status events entering the topic."],
                    ["Consumer processing rate", "300 events per second", "Sanctions consumer under degraded dependency."],
                    ["Backlog growth", "600 events per second", "900 incoming minus 300 processed."],
                    ["Incident duration", "12 minutes", "720 seconds."],
                    ["Backlog created", "432,000 events", "600 × 720."],
                ]
            )
            + p("The streaming dashboard must translate this into business impact. ‘Consumer lag is 432,000’ "
              "is a technical statement. The leader version is: ‘432,000 payment-status events are waiting "
              "for sanctions processing, estimated catch-up time is 24 minutes at current recovery rate, "
              "and customer-visible pending status is increasing by 600 payments per second.’")
            + table(
                ["Control area", "Design answer"],
                [
                    ["Back-pressure", "Payment orchestration knows when downstream risk controls are degraded and can slow, hold or route according to policy."],
                    ["Priority", "High-risk and high-value payments may be prioritised differently from low-risk status enrichments."],
                    ["Customer wording", "Pending message explains that status confirmation is delayed, not that funds disappeared."],
                    ["DORA evidence", "Incident timeline preserves event rates, lag, decisions, customer impact and recovery proof."],
                    ["Recovery", "Catch-up plan estimates time to normal and validates no event loss or duplicate release."],
                ]
            )
            + callout("Leader decision",
                p("Approve a resilience design where streaming metrics are tied to payment impact, not only "
                  "server health. Require incident runbooks that state when to hold traffic, when to degrade "
                  "non-critical consumers, how to communicate customer status, and how to prove recovery."),
                "info")
        )
        + H3("8.6  Worked example 5 — Singapore real-time liquidity and treasury visibility")
        + example("Intraday liquidity stream for corporate and retail rails",
            p("A Singapore-based regional bank runs high-volume FAST and PayNow payments, card settlement, "
              "corporate collections and treasury movements. Treasury wants a near-real-time view of cash "
              "positions because a large corporate payout file, a market movement or a payment-rail incident "
              "can change funding needs during the day. The question is not ‘can we stream everything?’ "
              "The question is which events materially change the liquidity view.")
            + table(
                ["Source", "Event", "Example amount", "Liquidity impact"],
                [
                    ["Retail payments", "<code>paynow_credit_confirmed</code>", "S$42", "High volume, low individual value, useful for trend and exception detection."],
                    ["Corporate payouts", "<code>corporate_bulk_payment_released</code>", "S$18,000,000", "Immediate cash-position impact."],
                    ["Card settlement", "<code>scheme_settlement_file_received</code>", "S$64,000,000", "Forecast-to-actual movement."],
                    ["Treasury transfer", "<code>nostro_transfer_confirmed</code>", "S$120,000,000", "Large balance and funding impact."],
                    ["Rail incident", "<code>payment_rail_degraded</code>", "No amount", "Changes expected outflows and operational decisions."],
                ]
            )
            + p("The design uses a streaming layer for fresh operational facts and a governed treasury model "
              "for balances. A stream processor aggregates confirmed inflows and outflows by currency, legal "
              "entity, rail and time bucket. It does not replace the general ledger or treasury management "
              "system. It creates an intraday lens that can show, for example, that expected Singapore dollar "
              "outflows for the next hour increased from S$310 million to S$428 million after a corporate "
              "file was released.")
            + table(
                ["Leader challenge", "Good answer"],
                [
                    ["Is this accounting truth?", "No. It is an intraday operating view reconciled to treasury and ledger sources."],
                    ["What is the allowed error?", "Define tolerance by currency and use case, such as S$1 million for operational alerting."],
                    ["What happens if a late event arrives?", "Event-time windows update the relevant bucket and mark the view as revised."],
                    ["Who can see it?", "Treasury, operations and authorised risk users only, with role-based access and audit."],
                    ["What is the fallback?", "Treasury reverts to last reconciled snapshot plus manual rail updates during platform outage."],
                ]
            )
            + callout("Leader decision",
                p("Approve streaming for intraday liquidity visibility if it is labelled as an operational "
                  "view, reconciled regularly, access-controlled, and connected to funding decisions. Reject "
                  "claims that it replaces the official ledger or treasury book of record."),
                "info")
        )
        + H3("8.7  Summary matrix — what each example teaches")
        + table(
            ["Example", "Region", "Streaming value", "Main control"],
            [
                ["UPI status repair", "India", "Reduce unclear status, duplicate attempts and support load.", "Customer wording, lifecycle events and payment reconciliation."],
                ["Card fraud scoring", "United States", "Stop fraud while authorisation is still in flight.", "Latency budget, reason codes, false-decline monitoring and safe replay."],
                ["APP fraud monitoring", "United Kingdom", "Join weak signals before a scam payment leaves.", "Evidence of warning, customer response and fairness."],
                ["SEPA Instant resilience", "Eurozone", "Translate lag into payment impact during incidents.", "Back-pressure, recovery evidence and DORA-aligned incident timeline."],
                ["Intraday liquidity", "Singapore", "Give treasury a fresh operating view of cash movements.", "Label as operational view, reconcile and control access."],
            ]
        )
        + H3("8.8  Section 8 takeaway")
        + callout("Worked-example recap",
            ul([
                "Start with business value and timing, not with Kafka or Flink as nouns.",
                "Small percentages become large operational numbers at bank scale.",
                "Every streaming example needs a control story: ownership, evidence, replay, reconciliation, privacy and customer impact.",
                "The best leader explanation translates technical metrics into money movement, fraud loss, customer harm, support load, resilience and regulatory evidence.",
            ]),
            "info")
    )
    return TopicSection("8.  Worked examples — numbers and decisions across payments, fraud, resilience and liquidity", "intermediate", body)


def _sec9() -> TopicSection:
    body = (
        primer(
            p("Section 9 is the practical review checklist. Use it when a team proposes Kafka, Flink, "
              "Pulsar, Kinesis, a cloud event service, Change Data Capture or any event-driven design. "
              "The goal is not to sound technical. The goal is to protect business value, customer outcomes, "
              "auditability and operational resilience before the architecture becomes expensive to change.")
        )
        + H3("9.1  The review flow — five gates before approval")
        + mermaid(
            "flowchart LR\n"
            "  A[Business value] --> B[Event meaning]\n"
            "  B --> C[Control design]\n"
            "  C --> D[Operations and resilience]\n"
            "  D --> E[Evidence and accountability]\n"
            "  E --> F[Approve, revise or stop]",
            "Figure 9.1 — A leader reviews event-driven design through value, meaning, controls, operations and evidence."
        )
        + table(
            ["Gate", "Approval question", "If the answer is weak"],
            [
                ["Business value", "What decision becomes better because the event is available sooner?", "Use batch, scheduled API or simpler integration until the value is clear."],
                ["Event meaning", "What exact fact does the event represent, and who owns that meaning?", "The topic will become a dumping ground."],
                ["Control design", "How are privacy, access, schema, ordering, replay and reconciliation controlled?", "The platform spreads risk faster than the old system."],
                ["Operations", "Who monitors lag, failures, dead letters, capacity and customer impact 24×7?", "Incidents will be detected by customers first."],
                ["Evidence", "Can audit reconstruct event, decision, side effect and recovery?", "The design is not ready for regulated BFSI use."],
            ]
        )
        + H3("9.2  Questions about business value and timing")
        + p("These questions stop the team from using streaming as a fashion word. A valid real-time use "
            "case should state the business decision, the time window and the consequence of being late.")
        + ul([
            "What decision or customer promise improves if this event is available in seconds rather than tomorrow?",
            "What is the value decay curve: milliseconds, seconds, minutes, hours or next day?",
            "How many events happen per day and at peak per second?",
            "What percentage of events create customer, fraud, liquidity, conduct or regulatory impact?",
            "What is the financial or operational cost of a one-minute, one-hour and one-day delay?",
            "Which use cases truly need streaming, and which can stay batch or near-real-time?",
            "What is the minimum viable event set for the first release?",
            "What business metric will prove success after go-live: fraud prevented, calls reduced, pending statuses reduced, liquidity forecast improved or incident time reduced?",
        ])
        + H3("9.3  Questions about event meaning and ownership")
        + p("Most event-driven failures start with unclear language. If a team cannot explain what an event "
            "means in business terms, consumers will interpret it differently and controls will drift.")
        + table(
            ["Question", "Good answer sounds like", "Weak answer sounds like"],
            [
                ["What is the event?", "A payment changed from network pending to credit confirmed.", "It is a payment message."],
                ["Who owns the meaning?", "The payment orchestration domain owner and product operations.", "The platform team owns the topic."],
                ["What does it not mean?", "Debit confirmed does not mean beneficiary credit confirmed.", "Consumers will figure it out."],
                ["What is the business key?", "Payment reference plus rail-specific transaction ID.", "Whatever ID is in the payload."],
                ["What state transitions are legal?", "Initiated to pending to confirmed or reversal path.", "Any status string can arrive."],
                ["What customer wording maps to it?", "Approved wording by lifecycle state.", "The app can display the raw event."],
            ]
        )
        + H3("9.4  Questions about producers, consumers and coupling")
        + ul([
            "Which system is the authoritative producer, and why is it closest to the fact?",
            "Can more than one producer publish the same event type, and if yes how is conflict avoided?",
            "Which consumers are approved for release one, and what business action does each take?",
            "Can a consumer fail without slowing the producer or corrupting the source system?",
            "Are consumers using the event contract, or are they depending on hidden producer internals?",
            "How will a new consumer be onboarded: access request, schema review, testing, quotas and operational runbook?",
            "What happens if a consumer is offline for two hours?",
            "What is the deprecation path if the producer needs to change the event?",
        ])
        + H3("9.5  Questions about schemas, compatibility and data quality")
        + p("A schema is the contract that tells consumers what fields exist and what they mean. In a bank, "
            "schema drift can become customer harm or regulatory evidence failure, not just a developer issue.")
        + table(
            ["Area", "Question to ask", "Evidence to request"],
            [
                ["Schema ownership", "Who approves field additions, removals and meaning changes?", "Named data owner and schema review workflow."],
                ["Compatibility", "Can old consumers still read new events?", "Backward and forward compatibility rules with test results."],
                ["Mandatory fields", "Which fields must never be blank?", "Validation rules and rejection handling."],
                ["Reference data", "How are codes such as rail, currency, country and status governed?", "Code lists, versioning and mapping ownership."],
                ["Data quality", "What happens to malformed, duplicate or impossible events?", "Dead-letter queue policy, triage ownership and service-level agreement."],
                ["Lineage", "Can we trace an event back to source transaction and downstream decisions?", "Lineage IDs, correlation IDs and sample trace."],
            ]
        )
        + H3("9.6  Questions about ordering, partitions and keys")
        + p("Ordering is not a generic platform promise. It depends on how the event is keyed and partitioned. "
            "A leader does not need to tune partitions personally, but must know what business sequence must "
            "never be scrambled.")
        + ul([
            "Which events must be processed in order: payment lifecycle, account balance events, card authorisation attempts, trade state or case notes?",
            "What key preserves that order: account ID, payment ID, card token, customer ID, trade ID or merchant ID?",
            "What ordering is not required and can be parallelised for scale?",
            "Can two related events land on different partitions and be seen out of order?",
            "How are late events handled when the event time differs from the processing time?",
            "How will the team prove that ordering assumptions hold in load testing?",
        ])
        + H3("9.7  Questions about latency, throughput and capacity")
        + table(
            ["Question", "Why it matters"],
            [
                ["What is peak events per second, not just average per day?", "Average hides the festival, salary-day, market-open or incident peak."],
                ["What are p50, p95 and p99 latency targets?", "Averages can look healthy while many customers wait too long."],
                ["Where is the latency budget spent?", "Producer, broker, processor, sink and notification each consume time."],
                ["What happens when the downstream system is slower than the stream?", "Backlog grows unless throttling, buffering or degradation is planned."],
                ["What volume is used for testing?", "Production-like load should include bursts, bad messages and consumer failures."],
                ["What capacity margin is funded?", "A platform running at 80–90% continuously has little room for incidents or onboarding."],
            ]
        )
        + H3("9.8  Questions about stateful processing and Flink-style logic")
        + p("Whenever a rule says ‘within ten minutes’, ‘three times’, ‘join payment and login’, or ‘aggregate "
            "by customer’, the design is stateful. Stateful processing has memory, checkpoints and recovery "
            "concerns that simple message movement does not.")
        + ul([
            "What state is stored: counts, windows, balances, previous status, model features or joins?",
            "How long is the state retained, and what business rule sets that duration?",
            "How are checkpoints taken and restored after failure?",
            "If the processor restarts, can it continue without losing or duplicating decisions?",
            "How are late and out-of-order events handled in event-time windows?",
            "Are model version, rule version and reason codes written to the output event?",
            "Can the same logic run in shadow mode before it affects customers?",
        ])
        + H3("9.9  Questions about delivery semantics, idempotency and side effects")
        + p("Exactly-once language is often misunderstood. In real banking processes, the hardest part is not "
            "whether the streaming engine processed a record once internally. The hard part is whether an "
            "external side effect, such as a payment hold, notification, case creation or ledger write, happens "
            "safely if events are retried or replayed.")
        + table(
            ["Side effect", "Idempotency question"],
            [
                ["Customer notification", "If the same event is consumed twice, does the customer receive one message or two?"],
                ["Fraud case", "Is case creation deduplicated by event ID, authorisation ID and risk version?"],
                ["Payment hold", "Can retry create a second hold, or does the account service reject duplicate hold IDs?"],
                ["Ledger posting", "Is the ledger protected by its own transaction and unique business key?"],
                ["Data lake write", "Can duplicate event files be compacted or deduplicated downstream?"],
                ["Regulatory alert", "Can replay mark old evidence as new production activity?"],
            ]
        )
        + H3("9.10  Questions about security, privacy and cross-border data")
        + ul([
            "What data classification applies to each field: public, internal, confidential, personal data, payment data or highly restricted?",
            "Does the event contain personal data that could be replaced with a token, reference or masked value?",
            "Which regions will store, process or replicate the event?",
            "Do India payment-data storage expectations, United States sanctions access needs, United Kingdom conduct evidence, European Union General Data Protection Regulation duties or Singapore outsourcing controls affect this topic?",
            "Who can read the topic, who can produce to it, and who approves access?",
            "Is access logged in a way that audit can review by user, service account, topic and time?",
            "How are secrets, certificates and service identities rotated?",
            "How is right-to-erasure or retention minimisation handled when events are immutable for a period?",
        ])
        + H3("9.11  Questions about replay, retention and legal hold")
        + p("Replay is powerful because it lets a bank rebuild state. Replay is dangerous because it can repeat "
            "side effects. Retention is powerful because it preserves evidence. Retention is dangerous because "
            "it stores sensitive history. Treat both as controlled business decisions.")
        + table(
            ["Question", "Minimum acceptable answer"],
            [
                ["Why do we need replay?", "Named scenarios such as rebuilding fraud features, recovering a projection or reprocessing corrected schema."],
                ["What exactly will be replayed?", "Topic, partition, offset range, event-time window, consumer group and destination."],
                ["Who approves production replay?", "Business owner, technology owner, risk or operations depending on side effect."],
                ["How are side effects blocked?", "Shadow sink, dry run, idempotency keys or explicit operational approval."],
                ["How long are events retained?", "Policy-backed duration by topic class, not a blanket forever."],
                ["What if litigation or investigation starts?", "Legal hold process freezes relevant evidence without broad uncontrolled retention."],
            ]
        )
        + H3("9.12  Questions about reconciliation and evidence")
        + ul([
            "What source of truth will the event stream reconcile to: ledger, payment hub, card processor, trade store or case system?",
            "What count should match: produced events, consumed events, successful side effects, rejected events and unresolved exceptions?",
            "How often is reconciliation performed: real time, hourly, end of day or incident-triggered?",
            "What is the tolerance for mismatch, and who owns exception clearing?",
            "Can a sample transaction be traced from source event to stream offset to consumer decision to customer-visible outcome?",
            "Where is evidence stored for audit and dispute handling?",
            "Can operations explain yesterday's failed or pending events without asking engineering to inspect logs manually?",
        ])
        + H3("9.13  Questions about operations and incident response")
        + table(
            ["Operational area", "Question"],
            [
                ["Monitoring", "Which dashboards show business lag, not just broker CPU and memory?"],
                ["Alerting", "What alert threshold maps to customer or regulatory impact?"],
                ["Dead letters", "Who owns dead-letter triage and by when?"],
                ["Runbooks", "What does support do when lag crosses the danger threshold?"],
                ["Disaster recovery", "What is the Recovery Time Objective and Recovery Point Objective for each critical stream?"],
                ["Change management", "How are schema, topic, ACL and processor changes released safely?"],
                ["Capacity", "Who forecasts growth when a new product or geography onboards?"],
                ["Skills", "Can business analysts, support and operations read event names and lifecycle states?"],
            ]
        )
        + H3("9.14  Questions by role in the room")
        + table(
            ["Role", "Question they should be able to answer"],
            [
                ["Product owner", "Which customer or business outcome improves, and how will success be measured?"],
                ["Business analyst", "What are the event lifecycle states, legal transitions and customer wording?"],
                ["Architect", "Why streaming instead of API, file, database replica or batch?"],
                ["Data owner", "What fields are authoritative, classified, masked and retained?"],
                ["Security lead", "Who can produce, consume, administer and audit the stream?"],
                ["Operations lead", "What are the support model, service levels, dashboards and runbooks?"],
                ["Risk or compliance", "What evidence proves the control worked during normal and incident conditions?"],
                ["Vendor or platform team", "What parts are managed service responsibility, and what remains bank responsibility?"],
            ]
        )
        + H3("9.15  Minimum evidence pack before go-live")
        + p("For a regulated BFSI streaming use case, do not rely on slideware. Ask for a small evidence pack "
            "that a new reviewer can inspect without trusting verbal assurances.")
        + ul([
            "Event catalogue entry with owner, meaning, producer, consumers, classification and retention.",
            "Schema with sample valid event, sample invalid event and compatibility test results.",
            "Architecture diagram showing producer, broker, processor, consumers, sinks and trust boundaries.",
            "Latency and throughput test results with peak load, burst load and downstream slowdown.",
            "Reconciliation design with source of truth, counts, exception workflow and owner.",
            "Replay runbook with approval path, dry-run method, idempotency proof and communication plan.",
            "Security review showing access controls, encryption, masking, audit logs and service identities.",
            "Operational runbook showing dashboards, alerts, dead-letter triage and incident roles.",
            "Customer-impact assessment for status wording, notifications, delays, false positives and complaints.",
            "Regulatory mapping where relevant: RBI, NPCI, OFAC, FCA, PSR, DORA, GDPR, MAS or local outsourcing rules.",
        ])
        + H3("9.16  A simple scoring card for design reviews")
        + table(
            ["Dimension", "0 — not ready", "1 — partial", "2 — ready"],
            [
                ["Business value", "No clear decision improved.", "Value stated but not measured.", "Metric, baseline and target defined."],
                ["Event meaning", "Vague event names.", "Some definitions exist.", "Owned lifecycle and legal transitions documented."],
                ["Control design", "Privacy, replay and reconciliation unclear.", "Controls exist but are not tested.", "Controls tested with evidence."],
                ["Operations", "No runbook or support owner.", "Technical monitoring only.", "Business-impact monitoring and runbooks live."],
                ["Resilience", "No failure testing.", "Component failure tested.", "Backlog, replay, disaster recovery and customer impact tested."],
                ["Audit evidence", "Logs only.", "Some traceability.", "End-to-end trace from source to decision to outcome."],
            ]
        )
        + callout("How to use the score",
            p("A critical payment, fraud, sanctions or customer-status stream should not go live with any "
              "zero score. A low-risk analytics feed may go live with partial controls if the risk is accepted "
              "and no customer or regulatory side effect occurs. The point is not bureaucracy. The point is "
              "to match control depth to business harm."),
            "info")
        + H3("9.17  Section 9 takeaway")
        + callout("Design-review recap",
            ul([
                "Ask what business decision gets better because events arrive sooner.",
                "Force clear event meaning, ownership, keys, legal transitions and customer wording.",
                "Treat replay, retention, idempotency, privacy and reconciliation as first-class controls.",
                "Translate platform health into customer, fraud, liquidity, operations and regulatory impact.",
                "Require evidence before go-live: tests, runbooks, schemas, access controls and traceability.",
            ]),
            "info")
    )
    return TopicSection("9.  Questions a leader asks in any streaming design or business review", "basic", body)


def _sec10() -> TopicSection:
    body = (
        primer(
            p("This final section is the field checklist you use when a streaming proposal sounds impressive "
              "but may be unsafe. A red flag is not an automatic rejection. It is a sentence that should make "
              "you slow the meeting down, ask for evidence, and separate product fashion from business control. "
              "After the red flags, the glossary gives you the vocabulary of the whole topic in one place.")
        )
        + H3("10.1  Red flags about real-time value")
        + red_flag(
            ul([
                "<strong>‘Make everything real time.’</strong> Push back because real time is not free. It adds operational monitoring, replay risk, data duplication, privacy exposure and failure modes. Ask which decision loses value in seconds or minutes.",
                "<strong>‘Batch is old, so streaming is always better.’</strong> Push back because end-of-day accounting, regulatory reports, interest accrual, archive loads and some reconciliations may be safer in controlled batch windows.",
                "<strong>‘The dashboard is live, so the business is live.’</strong> Push back because a live chart may still be based on delayed, duplicated or unreconciled events. Ask for source-of-truth reconciliation.",
                "<strong>‘We need Kafka because every modern bank has Kafka.’</strong> Push back because the design should start with event meaning, volume, latency and controls. The product choice comes after the use case.",
                "<strong>‘The value is better customer experience.’</strong> Push back if no one can name the specific customer promise: payment status within one second, fraud challenge before release, fewer duplicate attempts or faster support answer.",
            ])
        )
        + example("Real-time value test",
            p("Suppose a payment-status use case affects 40,000 uncertain journeys per day and unclear wording "
              "creates 3,000 support calls. Streaming status repair has visible value. Suppose a monthly fee "
              "report is read by finance on the third working day. Streaming that report may be expensive theatre. "
              "The question is not whether the technology can stream. The question is whether earlier knowledge "
              "changes a decision, a customer outcome or a control.")
        )
        + H3("10.2  Red flags about event meaning")
        + red_flag(
            ul([
                "<strong>‘The event name is self-explanatory.’</strong> Push back because <code>payment_success</code> may mean request accepted, debit posted, network accepted, beneficiary credited or settlement complete. Each is different.",
                "<strong>‘Consumers can interpret the payload.’</strong> Push back because every consumer will create its own meaning. Event contracts need owner, definition, legal states and examples.",
                "<strong>‘The platform team owns the event.’</strong> Push back because the platform team owns brokers, permissions and shared standards. The business domain owns event meaning.",
                "<strong>‘Just publish the database row change.’</strong> Push back because a changed row is not always a business event. Consumers need a meaningful fact, not every internal implementation detail.",
                "<strong>‘Status is just a string.’</strong> Push back because status drives customer wording, support scripts, complaints, operations and reconciliation.",
            ])
        )
        + table(
            ["Bad event language", "Better event language", "Why it matters"],
            [
                ["<code>payment_success</code>", "<code>beneficiary_credit_confirmed</code>", "Separates accepted request from actual credit confirmation."],
                ["<code>customer_update</code>", "<code>customer_address_verified</code>", "Names the fact and avoids vague topic dumping."],
                ["<code>fraud_result</code>", "<code>card_authorisation_risk_scored</code>", "Makes clear it is a risk score, not necessarily final decline."],
                ["<code>loan_done</code>", "<code>loan_agreement_executed</code>", "Separates offer, acceptance, disbursement and servicing setup."],
                ["<code>trade_changed</code>", "<code>trade_allocation_confirmed</code>", "Names the capital-markets lifecycle moment."],
            ]
        )
        + H3("10.3  Red flags about Kafka, Flink and product claims")
        + red_flag(
            ul([
                "<strong>‘Kafka gives exactly-once, so duplicates cannot happen.’</strong> Push back because exactly-once claims usually apply inside a bounded processing path. External side effects such as notifications, cases, payment holds and ledger writes still need idempotency.",
                "<strong>‘Flink will remember everything.’</strong> Push back because state has size, retention, checkpoint, recovery and privacy implications. Ask what state is stored, for how long and under whose policy.",
                "<strong>‘Managed service means the bank has no operations.’</strong> Push back because cloud or vendor operations do not remove the bank's accountability for outsourcing, resilience, access, data and customer impact.",
                "<strong>‘We can replay whenever something goes wrong.’</strong> Push back because replay can repeat side effects. Ask for dry run, approval, scope, idempotency and post-replay reconciliation.",
                "<strong>‘The topic has retention forever, so audit is solved.’</strong> Push back because audit evidence needs governed records, context, access control, legal hold and privacy retention logic.",
            ])
        )
        + table(
            ["Claim", "Question that exposes the risk"],
            [
                ["Exactly-once", "Exactly once where: broker, processor, sink, customer notification, ledger or case system?"],
                ["Stateful processing", "What state is stored, what is the checkpoint, and what happens on restore?"],
                ["Managed streaming", "What remains the bank's responsibility under outsourcing and operational-resilience rules?"],
                ["Replay", "What side effects are blocked or deduplicated during replay?"],
                ["Long retention", "Which policy permits this data to be retained in this form for this duration?"],
            ]
        )
        + H3("10.4  Red flags about customer harm and conduct")
        + red_flag(
            ul([
                "<strong>‘Customer wording can be decided later by the app team.’</strong> Push back because internal event states and customer-facing statuses must be mapped before go-live.",
                "<strong>‘Pending means failed.’</strong> Push back because pending means unknown or in progress. Calling it failed can trigger duplicate payments, complaints and wrong support action.",
                "<strong>‘Fraud friction only hurts conversion.’</strong> Push back because fraud friction can also prevent scam loss and reimbursement exposure. The trade-off needs false-positive, false-negative and vulnerable-customer analysis.",
                "<strong>‘A notification is harmless.’</strong> Push back because duplicate, premature or wrong notifications can mislead customers about money movement.",
                "<strong>‘Operations can manually fix exceptions.’</strong> Push back unless the team has volumes, ageing, ownership and service-level agreements for exception queues.",
            ])
        )
        + example("Customer harm hidden inside small percentages",
            p("A mobile payment flow has 8 million attempts per day. If 0.2% have unclear streaming status, "
              "that is 16,000 customer journeys. If only 10% call support, the bank receives 1,600 calls. "
              "If 3% retry and create a duplicate attempt, that is 480 risky journeys. Small percentages "
              "become real harm at retail scale.")
        )
        + H3("10.5  Red flags about security, privacy and geography")
        + red_flag(
            ul([
                "<strong>‘It is only an event, not a database.’</strong> Push back because events can contain personal data, payment data, card data, device data, sanctions data and behavioural data.",
                "<strong>‘We encrypted the stream, so data residency is handled.’</strong> Push back because encrypted data may still be regulated by country, purpose, access, backup, support and replication rules.",
                "<strong>‘All consumers can subscribe by default.’</strong> Push back because least privilege applies to streams. A topic can leak sensitive data to dozens of systems if access is casual.",
                "<strong>‘Logs are not in scope.’</strong> Push back because streaming platforms often write payload samples, errors, dead letters and traces into logs and support tools.",
                "<strong>‘Masking can be added later.’</strong> Push back because payload richness, tokenisation and field-level access should be designed before consumers build dependencies.",
            ])
        )
        + table(
            ["Region", "Privacy or control question to ask"],
            [
                ["India", "Does payment data, event copy, log, backup or support access conflict with Reserve Bank of India or payment-data storage expectations?"],
                ["United States", "Can sanctions, fraud and card data access be limited and evidenced, especially for vendors and support teams?"],
                ["United Kingdom", "Does customer-status and fraud-warning evidence support conduct, complaint and APP fraud review?"],
                ["Eurozone", "Does General Data Protection Regulation minimisation, lawful basis, retention and DORA resilience evidence apply to the stream?"],
                ["Singapore", "Do Monetary Authority of Singapore technology-risk, outsourcing and access controls cover the managed service and regional support model?"],
            ]
        )
        + H3("10.6  Red flags about operations and resilience")
        + red_flag(
            ul([
                "<strong>‘The brokers are green, so the service is healthy.’</strong> Push back because broker health does not prove consumers are current, customer status is right or downstream controls are working.",
                "<strong>‘Consumer lag is only technical debt.’</strong> Push back because lag can mean fraud decisions are late, payments are stuck, treasury view is stale or customer messages are misleading.",
                "<strong>‘Dead letters can be reviewed later.’</strong> Push back because dead letters may contain real payment, fraud or sanctions events that need business triage.",
                "<strong>‘Disaster recovery is the platform team's problem.’</strong> Push back because recovery must prove event loss, duplicate side effects, ordering, state restore and reconciliation.",
                "<strong>‘We will monitor after go-live.’</strong> Push back because monitoring, alert thresholds and runbooks are part of go-live readiness, not post-go-live decoration.",
            ])
        )
        + table(
            ["Metric", "Weak interpretation", "Leader interpretation"],
            [
                ["Consumer lag", "The consumer is behind.", "Which customer, payment, fraud, sanctions or liquidity decision is now late?"],
                ["Dead-letter count", "Some messages failed.", "Which business events are unresolved, how old are they, and who owns them?"],
                ["Replay job", "Engineering reprocessed data.", "What scope was approved, what side effects were blocked, and what reconciliation proves success?"],
                ["p99 latency", "Some tail delay exists.", "Which customers or controls are affected by the slowest 1%?"],
                ["Schema rejection", "A producer deployment failed.", "Which incompatible change was prevented from reaching consumers?"],
            ]
        )
        + H3("10.7  Topic glossary — the words you should now own")
        + kv([
            ("Event", "A recorded fact that something meaningful happened at a particular time, such as payment initiated, card authorised, fraud score produced or status changed."),
            ("Stream", "A continuous sequence of events over time. A payment-status stream is many payment-status events arriving as payments move through their lifecycle."),
            ("Topic", "A named lane for related events, such as <code>cards.authorisations</code> or <code>payments.status</code>. Producers write to it and consumers read from it."),
            ("Producer", "A system that publishes events to a topic. The best producer is usually the system closest to the business fact."),
            ("Consumer", "A system that reads events and reacts, such as fraud scoring, customer notification, operations dashboard, data-lake ingestion or case creation."),
            ("Consumer group", "A logical consuming application that may have many workers sharing the work while behaving as one reader of the topic."),
            ("Partition", "A lane inside a topic that allows scale and preserves order for events with the same key within that partition."),
            ("Key", "The field used to route events to partitions, such as payment ID, account ID, card token, customer ID or trade ID."),
            ("Offset", "The position of an event in a partition. Consumers track offsets so they know what they have processed."),
            ("Broker", "A server in the streaming cluster that stores and serves event data."),
            ("Cluster", "A group of brokers working together to provide the streaming platform."),
            ("Apache Kafka", "An open-source distributed event-log platform widely used to store, publish, subscribe and replay event streams."),
            ("Apache Flink", "An open-source stream-processing engine used for stateful, continuous calculations over event streams, such as windows, joins and pattern detection."),
            ("Apache Pulsar", "An open-source messaging and streaming platform often discussed as an alternative to Kafka, with different storage and tenancy architecture."),
            ("Amazon Kinesis", "Amazon Web Services' managed streaming service for collecting and processing real-time data streams."),
            ("Azure Event Hubs", "Microsoft Azure's managed event-ingestion service commonly used for streaming telemetry and event data."),
            ("Google Pub/Sub", "Google Cloud's managed publish-subscribe messaging service used for event distribution and asynchronous integration."),
            ("Publish-subscribe", "A pattern where producers publish messages and multiple authorised consumers subscribe without direct point-to-point calls."),
            ("Queue", "A messaging pattern where work is usually distributed to one worker or worker group. It is useful for task processing but differs from a replayable event log."),
            ("Event log", "A durable ordered record of events that consumers can read and often replay for a retention period."),
            ("Retention", "How long events are kept in the log. Retention should balance replay, audit, privacy, legal hold and cost."),
            ("Replay", "Reading historical events again to rebuild state, recover a projection, backfill a consumer or reprocess corrected logic."),
            ("Idempotency", "The property that repeating the same event or request does not create duplicate side effects."),
            ("At-least-once delivery", "A delivery model where an event is not lost but may be delivered more than once. Consumers must handle duplicates."),
            ("At-most-once delivery", "A delivery model where duplicates are avoided but an event may be lost if failure occurs at the wrong moment."),
            ("Exactly-once processing", "A bounded processing guarantee where a platform prevents duplicate processing within a controlled path. External side effects still need careful design."),
            ("Side effect", "A real-world action caused by consuming an event, such as sending a notification, placing a hold, creating a case or writing to a ledger."),
            ("Dead-letter queue", "A place where failed or unprocessable events are parked for triage instead of being silently dropped."),
            ("Back-pressure", "A condition where downstream systems cannot keep up, requiring slowing, buffering, prioritising or degrading work safely."),
            ("Consumer lag", "How far a consumer is behind the latest events. In BFSI, lag should be translated into late fraud, payment, customer or risk decisions."),
            ("Schema", "The agreed structure of an event payload, including fields, types, required values and meaning."),
            ("Schema registry", "A governed catalogue that stores schemas and compatibility rules for event producers and consumers."),
            ("Schema evolution", "Changing event schemas over time while keeping existing consumers safe."),
            ("Backward compatibility", "A change where old consumers can still read new events."),
            ("Forward compatibility", "A change where new consumers can tolerate older events."),
            ("Event contract", "The full promise around an event: name, meaning, owner, fields, allowed states, access, retention, examples and change rules."),
            ("Event catalogue", "A searchable inventory of topics and event contracts so teams can discover and govern streams."),
            ("Domain event", "An event named around a business fact owned by a domain, such as payment credited or loan approved."),
            ("Change Data Capture", "CDC. A technique that detects database changes and publishes them for downstream systems. It is useful but not always the same as a clean business event."),
            ("Outbox pattern", "A design where a business transaction and an event-to-publish record are written together, then a relay publishes the event reliably."),
            ("Event sourcing", "A design where the event history is the source of truth for state, rather than only storing the latest state in tables."),
            ("Command", "A request to do something, such as initiate payment. It is different from an event, which says something happened."),
            ("Choreography", "An event-driven coordination style where services react to events without one central orchestrator telling every step what to do."),
            ("Orchestration", "A coordination style where a central process controls the steps and decisions across services."),
            ("Saga", "A sequence of local transactions coordinated through events or commands, with compensating actions when later steps fail."),
            ("Compensating action", "A controlled follow-up action that offsets a previous step, such as reversal after a later payment step fails."),
            ("Stateful processing", "Stream processing that remembers prior events, windows or aggregates, such as failed logins in the last ten minutes."),
            ("Stateless processing", "Processing where each event can be handled independently without remembering previous events."),
            ("Window", "A time-bounded grouping of events, such as all events for one customer in ten minutes."),
            ("Event time", "The time when the business event actually happened."),
            ("Processing time", "The time when the streaming system processed the event."),
            ("Late event", "An event that arrives after the time window or expected order in which it logically belongs."),
            ("Watermark", "A stream-processing marker used to estimate that events up to a certain event time have mostly arrived."),
            ("Checkpoint", "A saved processing state that lets a stream processor recover after failure."),
            ("Materialised view", "A derived view built from events, such as current payment status by payment ID."),
            ("Projection", "A read model derived from events for a specific purpose, such as customer-status screen, support view or operations dashboard."),
            ("Reconciliation", "The process of proving that event counts, ledgers, payment hubs, downstream actions and exception queues agree or have explained breaks."),
            ("Lineage", "The ability to trace an event from source through topics, processors, consumers and side effects."),
            ("Correlation ID", "An identifier used to link related events, requests, logs and decisions across systems."),
            ("Trace ID", "An identifier used to follow a transaction or request path across distributed systems and observability tools."),
            ("Customer-status projection", "A governed view that translates internal lifecycle events into customer-safe wording."),
            ("Operational dashboard", "A dashboard used by support, operations or technology teams to see business health, lag, exceptions and impact."),
            ("Data residency", "Where data is stored or processed, including events, logs, backups, dead letters, analytics copies and support tools."),
            ("Data localisation", "A legal or policy requirement that certain data stay within a particular country or region."),
            ("General Data Protection Regulation", "GDPR. European Union data-protection regulation governing personal data use, rights, minimisation, transfer and retention."),
            ("Digital Operational Resilience Act", "DORA. European Union regulation applicable from January 2025 covering information and communication technology risk in financial services."),
            ("Reserve Bank of India", "RBI. India's central bank and banking regulator, relevant for IT governance, outsourcing and payment-data controls."),
            ("National Payments Corporation of India", "NPCI. Operator of major Indian retail payment systems including UPI and RuPay arrangements."),
            ("Office of Foreign Assets Control", "OFAC. United States Treasury office administering major sanctions programmes."),
            ("Financial Conduct Authority", "FCA. United Kingdom conduct regulator for financial services."),
            ("Payment Systems Regulator", "PSR. United Kingdom regulator focused on payment systems, including APP fraud reimbursement policy context."),
            ("Monetary Authority of Singapore", "MAS. Singapore's central bank and financial regulator, including technology-risk and outsourcing expectations."),
            ("Unified Payments Interface", "UPI. India's instant account-to-account payment system operated through NPCI arrangements."),
            ("Faster Payments", "The United Kingdom's near-real-time domestic account-to-account payment rail."),
            ("Authorised Push Payment fraud", "APP fraud. A scam where the genuine customer is manipulated into authorising a payment to a fraudster."),
            ("Single Euro Payments Area", "SEPA. European framework for euro credit transfers and direct debits across participating countries."),
            ("SEPA Instant Credit Transfer", "A SEPA scheme for euro credit transfers designed to complete in seconds and operate continuously."),
            ("FAST", "Fast And Secure Transfers, Singapore's instant domestic electronic funds transfer service."),
            ("PayNow", "Singapore's proxy addressing service that lets users pay using mobile number, national identity number or entity identifier over FAST."),
            ("FedNow", "The United States Federal Reserve's instant payment service launched in July 2023."),
            ("Real-Time Payments", "RTP. The Clearing House's private-sector instant payment rail in the United States."),
            ("ISO 20022", "An international financial messaging standard with rich structured data, widely relevant to payment status, reconciliation and compliance."),
            ("Anti-Money Laundering", "AML. Controls to detect and prevent money laundering through monitoring, investigation and reporting."),
            ("Sanctions screening", "Checking parties, banks, countries, goods or text against legal restriction lists before or during processing."),
            ("False positive", "A legitimate activity incorrectly flagged as risky, such as a genuine payment challenged by fraud controls."),
            ("False negative", "A risky or fraudulent activity incorrectly allowed to pass as safe."),
            ("Model version", "The specific version of a model used to score or decide an event, important for audit and dispute review."),
            ("Reason code", "A structured explanation for a decision, such as why a fraud score was high or a payment was held."),
            ("Recovery Time Objective", "RTO. The target maximum time to restore a service after disruption."),
            ("Recovery Point Objective", "RPO. The target maximum acceptable data loss measured as time."),
            ("Impact tolerance", "The maximum tolerable disruption to an important business service, measured by time, volume, value, customers or harm."),
            ("Runbook", "Step-by-step operational instructions for routine support, failures, replay, escalation and incident handling."),
            ("Service-level agreement", "SLA. A promised service level such as response time, recovery time, processing window or exception-clearing time."),
            ("p95 latency", "The response time below which 95% of events complete. It is more useful than average for customer experience."),
            ("p99 latency", "The response time below which 99% of events complete, highlighting tail delays in high-volume systems."),
        ])
        + H3("10.8  Final recap — what you should be able to say now")
        + callout("If you can explain these, Topic III.2 has done its job",
            ul([
                "Streaming moves meaningful facts while they are still useful, but the ledger and controlled systems of record remain the truth for money.",
                "Kafka-style logs are valuable because they decouple producers and consumers, keep ordered event history for a retention period and support replay.",
                "Flink-style processing is valuable when the bank must remember patterns over time, join streams, calculate windows or maintain derived state.",
                "In BFSI, streaming is never just speed. It changes fraud, sanctions, customer wording, privacy, resilience, reconciliation, replay and audit evidence.",
                "A leader's job is to ask what fact happened, who owns it, how fast it matters, what side effect follows, and what evidence proves control.",
                "The safest design reviews translate offsets, lag, partitions and schemas into customer, payment, fraud, liquidity, regulatory and operational impact.",
            ]),
            "info")
    )
    return TopicSection("10. Red flags + topic glossary", "basic", body)
