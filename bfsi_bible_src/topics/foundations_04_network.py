"""Foundations · 04 — Network fundamentals for BFSI."""
from __future__ import annotations

from ..site import (
    H3, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="I.4",
        slug="04-network-fundamentals",
        title="Network fundamentals for BFSI — TLS, mTLS, zero trust, latency and resilience",
        one_liner=(
            "Every digital bank is a networked bank. A customer tap, a card swipe, a SWIFT "
            "message, a market-data feed, a fraud score and an administrator login all travel "
            "through cables, routers, certificates, gateways and trust decisions. This topic "
            "builds networking from zero: what packets physically do, why latency matters, how "
            "Transport Layer Security (TLS) and mutual Transport Layer Security (mTLS) prove "
            "trust, and how zero trust changes the old perimeter model for regulated BFSI."
        ),
        sections=[
            _sec0(), _sec1(), _sec2(), _sec3(), _sec4(), _sec5(),
            _sec6(), _sec7(), _sec8(), _sec9(), _sec10(),
        ],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("A network is not magic air around software. It is a chain of physical and "
              "logical hand-offs. Your phone turns a message into tiny chunks called packets. "
              "Those packets move over Wi-Fi, fibre, mobile towers, routers, firewalls, load "
              "balancers and application gateways. At each hop, a device asks a small question: "
              "where should this packet go next, is it allowed, and should I record it?")
        )
        + H3("0.1  IT-side anchor — sending a parcel from your home")
        + it_anchor(
            p("Imagine sending a parcel from Mumbai to London. You write a destination address, "
              "the courier breaks the journey into legs, each sorting centre scans the parcel, "
              "and the final delivery agent needs proof before handing it over. Networking is "
              "the same. The <strong>Internet Protocol address</strong> is the destination "
              "address, the <strong>router</strong> is the sorting centre, the <strong>firewall" 
              "</strong> is the security guard, and <strong>Transport Layer Security (TLS)</strong> "
              "is the tamper-evident sealed bag that proves nobody read or changed the contents "
              "in transit.")
        )
        + H3("0.2  BFSI-side anchor — what happens when you tap Pay")
        + bfsi_anchor(
            p("When you tap Pay in a banking app, you see one spinner for maybe two seconds. "
              "Under that spinner, the phone resolves the bank domain name, opens a secure TLS "
              "connection, sends a payment request to an edge gateway, crosses one or more "
              "private bank networks, reaches fraud scoring, posts to a ledger, gets a response, "
              "and returns the result. If each network leg adds only 40 milliseconds and there "
              "are 12 legs, the network alone consumes 480 milliseconds before application logic "
              "does any useful work. That is why senior BFSI reviews discuss latency budgets, "
              "not just server capacity.")
        )
        + H3("0.3  Four nouns you must separate")
        + table(
            ["Noun", "Physical picture", "BFSI example"],
            [
                ["<strong>Network</strong>",
                 "The roads and junctions packets travel through.",
                 "Bank branch wide-area network, cloud virtual private cloud, SWIFT connectivity."],
                ["<strong>Protocol</strong>",
                 "The agreed language used on the road.",
                 "Transmission Control Protocol (TCP), Hypertext Transfer Protocol (HTTP), ISO 20022 over MQ."],
                ["<strong>Encryption</strong>",
                 "A sealed envelope whose contents cannot be read by couriers.",
                 "TLS 1.3 on mobile APIs, database encryption in transit, SWIFT secure channel."],
                ["<strong>Identity</strong>",
                 "Proof that the sender and receiver are who they claim to be.",
                 "Server certificate for mobile banking, client certificate for partner APIs, SPIFFE identity for workloads."],
            ]
        )
        + H3("0.4  The practical mental model")
        + analogy(
            p("Think of a bank network as a secure airport. Customers enter through public "
              "doors, staff enter through badges, planes move through controlled taxiways, and "
              "high-value cargo moves through special screening lanes. The old model trusted "
              "anyone once they were inside the airport. The zero-trust model checks the ticket, "
              "passport, gate, device, route and cargo at every meaningful step.")
        )
    )
    return TopicSection("0.  Primer — packets are parcels, networks are roads", "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Networking exists because one computer rarely owns the whole banking job. A mobile "
          "app, a customer identity service, a fraud model, a ledger, a notification service and "
          "a regulator reporting store all need to coordinate while sitting in different places. "
          "The network is the nervous system that lets those organs behave as one bank.")
        + ol([
            "<strong>Distance must be hidden.</strong> A customer in Pune may hit a Mumbai cloud "
            "region, a fraud service in Singapore and a core in an on-prem data centre. The user "
            "still expects a single two-second experience.",
            "<strong>Trust must be proven.</strong> The bank cannot assume a request is safe "
            "because it came from a known subnet. Malware, insider risk, compromised vendors and "
            "cloud misconfiguration all make location-based trust weak.",
            "<strong>Failures must be contained.</strong> If a router, certificate authority, "
            "Domain Name System (DNS) provider, cloud region or firewall rule fails, the bank "
            "needs graceful degradation rather than a national outage.",
            "<strong>Performance must be budgeted.</strong> A payment path with 20 network calls "
            "can fail a service-level objective even when each individual service is healthy.",
            "<strong>Evidence must be retained.</strong> Regulators and auditors ask who connected, "
            "from where, using which certificate, through which control, and with what failure "
            "mode. Network logs become legal evidence after incidents.",
        ])
        + callout("The leader's translation",
            p("When engineers say, ‘the network is fine’, ask which of the five dimensions they "
              "mean: reachability, latency, throughput, loss, or trust. A green ping only proves "
              "reachability. It does not prove the TLS handshake is valid, the firewall allows "
              "the right ports, the application gateway can route traffic, or the path meets a "
              "200 millisecond payment budget."),
            "info")
    )
    return TopicSection("1.  Why networking exists at all — first principles", "basic", body)


def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  C["Customer phone<br/>bank app"] --> I["ISP or mobile network<br/>4G, 5G, fibre"]\n'
            '  I --> D["DNS resolver<br/>name to IP"]\n'
            '  D --> E["Edge layer<br/>CDN, DDoS, WAF"]\n'
            '  E --> G["API gateway<br/>rate limit and auth"]\n'
            '  G --> T["TLS termination<br/>server certificate"]\n'
            '  T --> M["Private bank network<br/>VPN, Direct Connect"]\n'
            '  M --> S["Service mesh<br/>mTLS between services"]\n'
            '  S --> F["Fraud and risk<br/>scoring service"]\n'
            '  S --> L["Ledger or payment engine<br/>core system"]\n'
            '  L --> R["Response path<br/>status and receipt"]\n'
            '  R --> C\n'
            '  S -. logs .-> O["Observability and audit<br/>SIEM, regulator evidence"]\n'
            '  G -. policy .-> Z["Zero trust engine<br/>identity, device, context"]',
            "A simplified path for one digital banking request."
        )
        + p("The diagram is deliberately not drawn as one clean arrow from phone to core. Real "
          "banking traffic crosses multiple control points. Some points improve speed, such as a "
          "Content Delivery Network (CDN). Some improve safety, such as a Web Application Firewall "
          "(WAF). Some prove identity, such as TLS certificates and mTLS workload certificates. "
          "Some create evidence, such as Security Information and Event Management (SIEM) logs.")
        + callout("Read the picture like a senior reviewer",
            ul([
                "If the issue is <strong>customer-visible slowness</strong>, inspect the phone to edge path, DNS, TLS handshake time and gateway queueing.",
                "If the issue is <strong>partner trust</strong>, inspect client certificates, API keys, OAuth scopes and rate limits.",
                "If the issue is <strong>east-west risk</strong> inside the bank, inspect service mesh mTLS, network segmentation and workload identity.",
                "If the issue is <strong>regulatory evidence</strong>, inspect immutable logs, time synchronisation and incident replay capability.",
            ]),
            "info")
    )
    return TopicSection("2.  The core concept in one picture", "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  Phase 1 — the customer finds the bank")
        + p("The customer types or taps a domain such as <code>api.bank.com</code>. The phone "
            "does not understand names; it needs an Internet Protocol (IP) address. DNS is the "
            "phone book. A resolver returns one or more IP addresses, often pointing to the "
            "nearest edge location. If DNS lookup takes 80 milliseconds in normal conditions and "
            "250 milliseconds during a resolver problem, every login inherits that delay before "
            "the bank's application code even starts.")
        + H3("3.2  Phase 2 — the device opens a transport connection")
        + p("Most banking APIs still use Transmission Control Protocol (TCP). TCP first performs "
            "a three-step handshake: client says synchronize, server says synchronize plus "
            "acknowledge, client acknowledges. On a 40 millisecond round-trip network, this costs "
            "about 40 milliseconds. Newer paths may use QUIC over User Datagram Protocol (UDP), "
            "which can reduce handshake overhead, but banks adopt it carefully because security "
            "inspection and operational tooling are less mature in some estates.")
        + H3("3.3  Phase 3 — TLS proves the server and creates session keys")
        + p("Transport Layer Security (TLS) is the padlock in the browser and the default secure "
            "channel for mobile apps. In TLS 1.3, the client and server negotiate cryptographic "
            "algorithms, the server presents a certificate, the client validates that certificate "
            "against trusted certificate authorities, and both sides derive temporary session "
            "keys. The bank does not encrypt every message with the long-term certificate key; it "
            "uses short-lived symmetric keys because they are faster and safer.")
        + example("Latency math for TLS",
            p("Assume a customer in Bengaluru reaches a Mumbai edge with a 35 millisecond round "
              "trip. DNS takes 25 milliseconds, TCP handshake takes 35 milliseconds, TLS 1.3 "
              "takes roughly one additional round trip of 35 milliseconds, and the API gateway "
              "adds 20 milliseconds. Before business logic, the request has already spent about "
              "115 milliseconds. If a misconfiguration forces TLS renegotiation or routes traffic "
              "via Singapore at 95 milliseconds round trip, the same path can jump above 250 "
              "milliseconds.")
        )
        + H3("3.4  Phase 4 — gateways enforce policy")
        + p("At the edge, a CDN may cache static content, a Distributed Denial-of-Service (DDoS) "
            "service absorbs floods, a WAF blocks obvious attacks, and an API gateway validates "
            "tokens, rate limits and routes the call. For an open-banking API, the gateway may "
            "also validate a partner's client certificate and OAuth 2.0 token before allowing the "
            "request near the bank's internal services.")
        + H3("3.5  Phase 5 — inside the bank, mTLS proves service-to-service identity")
        + p("Mutual Transport Layer Security (mTLS) means both sides present certificates. The "
            "client proves itself to the server and the server proves itself to the client. In a "
            "service mesh such as Istio, Linkerd or Consul, sidecar proxies or ambient agents can "
            "create mTLS between workloads automatically. The business value is simple: a fraud "
            "service should accept requests from the payment orchestration service, not from any "
            "random server that happens to sit inside the same subnet.")
        + H3("3.6  Phase 6 — response, logging and replayability")
        + p("The response travels back through similar controls. Meanwhile, logs are emitted: DNS "
            "query, gateway request ID, TLS certificate fingerprint, service mesh trace ID, "
            "firewall decision, application result and database transaction ID. In a good estate, "
            "these IDs stitch into one trace. After a regulator asks what happened during a 43 "
            "minute outage, the bank should be able to replay the chain without guessing.")
    )
    return TopicSection("3.  How it actually works — phase by phase", "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  Network types a BFSI leader will hear")
        + table(
            ["Type", "What it means physically", "Where it appears in banks"],
            [
                ["<strong>Local Area Network (LAN)</strong>",
                 "A network inside one building or campus.",
                 "Branch network, trading floor, data-centre rack network."],
                ["<strong>Wide Area Network (WAN)</strong>",
                 "Private or carrier-managed links across cities and countries.",
                 "Branch to data centre, India operations centre to UK bank environment."],
                ["<strong>Virtual Private Network (VPN)</strong>",
                 "Encrypted tunnel over an untrusted network.",
                 "Remote employee access, third-party support, site-to-site connectivity."],
                ["<strong>Virtual Private Cloud (VPC) / Virtual Network (VNet)</strong>",
                 "Software-defined network inside a cloud provider.",
                 "AWS VPC, Azure VNet, Google Cloud VPC hosting banking workloads."],
                ["<strong>Direct private connectivity</strong>",
                 "Dedicated or partner-provided private circuits into cloud.",
                 "AWS Direct Connect, Azure ExpressRoute, Google Cloud Interconnect, OCI FastConnect."],
                ["<strong>Service mesh</strong>",
                 "Application-layer network fabric between microservices.",
                 "mTLS, retries, traffic shaping and policy inside Kubernetes."],
            ]
        )
        + H3("4.2  Protocols and controls")
        + table(
            ["Layer", "Common choices", "BFSI decision point"],
            [
                ["Addressing", "IPv4, IPv6", "IPv4 overlap is common after mergers; IPv6 is cleaner but operationally slower to adopt."],
                ["Routing", "Border Gateway Protocol (BGP), Open Shortest Path First (OSPF)", "BGP mistakes can route traffic to the wrong internet path; change control matters."],
                ["Transport", "TCP, UDP, QUIC", "TCP is predictable and inspectable; QUIC may improve customer latency but changes monitoring."],
                ["Security", "TLS 1.2, TLS 1.3, mTLS, Internet Protocol Security (IPsec)", "TLS 1.3 is preferred for modern channels; legacy partners may still force TLS 1.2."],
                ["Application", "HTTP/1.1, HTTP/2, gRPC, MQ, SWIFT protocols", "API channels need different controls from batch and messaging channels."],
                ["Policy", "WAF, API gateway, ZTNA, SASE", "Policy should follow identity and context, not only static IP ranges."],
            ]
        )
        + H3("4.3  Regional variations")
        + table(
            ["Region", "Common network pattern", "Why it differs"],
            [
                ["India", "In-country cloud regions plus private links to bank data centres and payment rails.", "RBI payment data localisation and high UPI volume make domestic routing and resilience critical."],
                ["United States", "Large multi-region public cloud plus carrier diversity and legacy mainframe links.", "No broad data localisation, but high third-party and cyber scrutiny from OCC, Federal Reserve, FDIC and NYDFS."],
                ["United Kingdom", "Hybrid cloud, strong operational-resilience mapping to important business services.", "FCA, PRA and Bank of England require impact tolerances and March 2025 resilience embedding."],
                ["Eurozone", "Country-aware routing, DORA-ready evidence and concentration-risk controls.", "Digital Operational Resilience Act (DORA) and NIS2 make ICT third-party oversight explicit."],
                ["Singapore", "Cloud-positive, regionally connected, strong MAS Technology Risk Management controls.", "MAS allows cloud adoption but expects robust outsourcing, cyber and recovery controls."],
                ["Brazil, UAE, Hong Kong, Australia", "Mixture of local cloud, regional hubs and strict outsourcing reviews.", "PIX, UAE data rules, HKMA cyber expectations and APRA CPS 230 shape connectivity and vendor controls."],
            ]
        )
    )
    return TopicSection("4.  Types & variations — networks, protocols and regional patterns", "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  DNS — the small dependency that can take down a bank")
        + p("Domain Name System (DNS) turns names into IP addresses. Banks usually use multiple "
            "authoritative DNS providers, short but not reckless time-to-live values, DNS Security "
            "Extensions (DNSSEC) for integrity where feasible, and emergency runbooks for provider "
            "outages. A five-minute DNS time-to-live means clients may keep using a bad endpoint "
            "for five minutes after failover; a five-second value creates more query load and can "
            "stress resolvers. There is no free answer, only a risk trade-off.")
        + H3("5.2  BGP — how the internet chooses roads")
        + p("Border Gateway Protocol (BGP) is how networks announce reachable address ranges to "
            "each other. It is powerful and blunt. If a provider accidentally announces a more "
            "specific route, traffic can be misdirected. Banks reduce risk through route filtering, "
            "Resource Public Key Infrastructure (RPKI), carrier diversity and monitored failover. "
            "A BGP incident may appear to the business as ‘the app is down in one city only’, "
            "because only some internet paths are affected.")
        + H3("5.3  NAT, proxies and why IP allowlists become brittle")
        + p("Network Address Translation (NAT) lets many private systems share fewer public IP "
            "addresses. It is useful but hides identity. If a partner API trusts only source IP, "
            "then every workload behind that NAT may look the same. Modern BFSI designs combine "
            "IP allowlists with stronger identity: mTLS client certificates, signed tokens, device "
            "posture and transaction-level controls.")
        + H3("5.4  Certificates and Public Key Infrastructure")
        + p("A certificate binds a public key to a name, such as <code>api.bank.com</code> or "
            "<code>payments-service.prod.bank</code>. Public Key Infrastructure (PKI) is the "
            "factory and governance model that issues, rotates, revokes and audits certificates. "
            "The operational lesson is brutal: a single expired certificate can break mobile "
            "login, partner payments or an internal batch chain. Mature banks use automated "
            "certificate lifecycle management, not spreadsheet reminders.")
        + H3("5.5  TLS 1.2, TLS 1.3 and post-quantum planning")
        + p("TLS 1.3 removes older weak options, reduces handshake round trips and improves "
            "forward secrecy. TLS 1.2 remains common for legacy partners, hardware security "
            "appliances and older clients. From 2024 onward, banks also need crypto-agility "
            "because the United States National Institute of Standards and Technology (NIST) "
            "published final post-quantum standards: ML-KEM, ML-DSA and SLH-DSA. This does not "
            "mean switching every TLS endpoint overnight. It means inventorying where cryptography "
            "is used, how certificates are issued, and whether systems can adopt hybrid key "
            "exchange when ecosystem support matures.")
        + H3("5.6  Zero trust, ZTNA and SASE")
        + p("Zero trust is not one product. It is an operating principle: never trust solely "
            "because of network location, always verify identity, device health, context and "
            "least privilege. Zero Trust Network Access (ZTNA) replaces broad VPN access with "
            "per-application access. Secure Access Service Edge (SASE) combines network security "
            "and wide-area networking from cloud-delivered points of presence. In a bank, zero "
            "trust usually begins with workforce and third-party access, then moves to service-to-"
            "service mTLS and data-aware controls.")
        + H3("5.7  Segmentation and blast-radius control")
        + p("Segmentation divides the estate so a compromise in one zone does not reach crown "
            "jewel systems. Old segmentation used static network zones: internet, demilitarized "
            "zone, application zone, database zone. Modern segmentation adds identity-aware "
            "microsegmentation: workload A can call workload B on one port for one purpose, but "
            "cannot scan or call everything else. This is how a ransomware incident in a call-centre "
            "desktop estate is prevented from becoming a core-banking outage.")
        + H3("5.8  Observability — seeing the packet without drowning in logs")
        + p("Network observability combines metrics, logs and traces. Metrics answer ‘how much "
            "latency, loss and throughput’. Logs answer ‘which decision did the firewall or gateway "
            "make’. Traces answer ‘which service call consumed the time’. A leader should expect "
            "one customer complaint to be traceable from device to edge to gateway to service mesh "
            "to database, with timestamps synchronised by Network Time Protocol (NTP) or Precision "
            "Time Protocol (PTP) in latency-sensitive trading environments.")
    )
    return TopicSection("5.  Advanced — the mechanisms underneath", "advanced", body)


def _sec6() -> TopicSection:
    body = (
        p("Networking decisions become regulatory decisions when they affect customer access, "
          "payment integrity, outsourcing, cyber evidence or data location. The exact laws differ, "
          "but the pattern is global: know your critical services, protect them, test recovery, "
          "manage third parties, retain evidence and avoid hidden concentration risk.")
        + table(
            ["Region", "Regulatory overlay", "Network design implication"],
            [
                ["India",
                 "Reserve Bank of India (RBI) IT Governance Master Direction 2023, Outsourcing of IT Services Master Direction 2023, Cyber Security Framework, payment data localisation circular 2018, Digital Personal Data Protection Act 2023.",
                 "Keep payment data lifecycle in India where required, document cloud and network outsourcing, test disaster recovery, monitor third-party links and maintain board-level cyber governance."],
                ["United States",
                 "Federal Financial Institutions Examination Council (FFIEC) Cybersecurity guidance, OCC Bulletin 2023-17 and Federal Reserve SR 23-4 on third-party risk, NYDFS Part 500 amendments, PCI DSS 4.0 for cardholder data.",
                 "Evidence third-party connectivity risk, segment cardholder environments, enforce multifactor and privileged access controls, and retain logs for incident investigation."],
                ["United Kingdom",
                 "Prudential Regulation Authority SS2/21, FCA and PRA Operational Resilience fully embedded March 2025, Critical Third Parties regime under FSMA 2023, FCA Consumer Duty.",
                 "Map networks to important business services, set impact tolerances, test loss of provider or link, and avoid customer harm from preventable access outages."],
                ["Eurozone",
                 "Digital Operational Resilience Act in force 17 January 2025, NIS2, European Banking Authority outsourcing guidelines, PSD2 and strong customer authentication, eIDAS trust services.",
                 "Treat network, cloud and security providers as ICT third parties, maintain incident reporting, threat-led penetration testing and exit strategies for critical paths."],
                ["Singapore",
                 "Monetary Authority of Singapore Technology Risk Management Guidelines, Outsourcing Guidelines, Notice 658 on business continuity management, Cyber Hygiene Notice.",
                 "Design resilient connectivity, secure administrative access, monitor outsourcing dependencies and prove recovery for digital banking services."],
                ["Cross-border",
                 "SWIFT Customer Security Controls Framework, ISO 27001, NIST Cybersecurity Framework 2.0, Basel operational resilience expectations, sanctions and data-transfer rules.",
                 "Separate payment networks from general corporate traffic, monitor SWIFT interfaces tightly, and align network evidence to global audit and regulator expectations."],
            ]
        )
        + red_flag(
            p("If a network design review does not mention which customer-facing business service "
              "is protected, which regulator can ask for evidence, and how recovery was tested, "
              "it is still a technical diagram, not a BFSI control design.")
        )
    )
    return TopicSection("6.  Domain overlay — regulation changes the network", "advanced", body)


def _sec7() -> TopicSection:
    body = table(
        ["Decision", "Option A", "Option B", "Leader's test"],
        [
            ["Internet exposure", "Public endpoint behind CDN, DDoS and WAF", "Private endpoint reachable only through VPN or private link", "Is this truly customer or partner facing, and what fraud or DDoS volume can it absorb?"],
            ["Partner trust", "IP allowlist plus API key", "mTLS plus OAuth scopes plus rate limits", "Could a compromised partner subnet or leaked key move money without stronger proof?"],
            ["Employee access", "Broad VPN into the network", "ZTNA per application with device posture", "Can a support engineer reach only the one tool needed for the ticket?"],
            ["Cloud connectivity", "Internet VPN", "Dedicated private circuits across two carriers", "What Recovery Time Objective and throughput does the service need during month-end or market stress?"],
            ["TLS termination", "Terminate at edge gateway", "End-to-end TLS or re-encrypt to service", "Where can plaintext exist, who can inspect it, and is that acceptable for this data class?"],
            ["Service-to-service trust", "Flat subnet trust", "Service mesh mTLS with workload identity", "If one pod or virtual machine is compromised, how far can it move laterally?"],
            ["DDoS defence", "Provider default only", "Layered DDoS provider, runbooks and traffic scrubbing", "What size attack can we survive before customer login or payments degrade?"],
            ["Vendor support", "Shared admin VPN account", "Privileged access broker with recording and just-in-time approval", "Can audit prove exactly who did what during a production change?"],
            ["Multi-region", "Active-warm failover", "Active-active cell architecture", "Does the business need minutes of recovery or near-zero interruption, and can data consistency support it?"],
        ]
    )
    return TopicSection("7.  Trade-offs and decisions a leader owns", "intermediate", body)


def _sec8() -> TopicSection:
    body = (
        example("India — UPI payment latency budget",
            ol([
                "Customer in Pune opens the bank app and pays ₹2,000 to a merchant.",
                "DNS and TLS to Mumbai edge consume 90 milliseconds on a good mobile path.",
                "API gateway and authentication consume 60 milliseconds.",
                "Fraud risk call consumes 120 milliseconds because it fetches device and behavioural features.",
                "Bank payment switch to NPCI path consumes 250 milliseconds round trip during peak time.",
                "Ledger posting and notification consume 180 milliseconds.",
                "Total technical path is roughly 700 milliseconds before mobile UI rendering. If the bank promises a two-second payment experience, it has about 1.3 seconds left for retries, queueing and variance. A single extra cross-region hop can consume the safety margin.",
            ])
        )
        + example("United Kingdom — certificate expiry on open banking APIs",
            p("A UK bank exposes account information APIs to regulated Third Party Providers "
              "under open banking. A client-certificate chain expires at 02:00. Only 8% of traffic "
              "uses the affected certificate authority, but that includes two large personal "
              "finance apps. If the bank serves 4 million API calls per day, 320,000 calls can fail "
              "in 24 hours. Under Consumer Duty and operational resilience expectations, this is "
              "not a minor technical issue; it is customer harm and an important-business-service "
              "incident. The control is automated certificate inventory, 30-day renewal alerts, "
              "pre-production chain validation and emergency trust-store rollback.")
        )
        + example("Eurozone — DORA-ready third-party network exit",
            p("A eurozone bank uses one cloud provider's private connectivity for a critical "
              "payments analytics platform. DORA requires exit strategy and concentration-risk "
              "management for critical ICT services. The bank models a provider-region loss: "
              "primary link 10 gigabits per second, normal peak 4 gigabits per second, disaster "
              "replay requires 7 gigabits per second for six hours. A backup 1 gigabit per second "
              "VPN is not an exit plan. The leader should require either a second private circuit, "
              "reduced replay objectives, workload degradation tiers, or a documented business "
              "acceptance signed by accountable executives.")
        )
        + example("Singapore — zero trust for vendor operations",
            p("A Singapore digital bank lets a core-platform vendor support production incidents. "
              "The old model gives the vendor a VPN profile reaching a whole subnet. The zero-trust "
              "model gives named engineers just-in-time access for two hours to one bastion or one "
              "support tool, validates device posture, records the session, blocks clipboard and "
              "file transfer unless approved, and writes logs to the bank's SIEM. If an engineer "
              "needs database access, a separate approval and masked view are required. MAS-style "
              "outsourcing evidence becomes a by-product of the workflow.")
        )
        + example("United States — DDoS on salary-day mobile login",
            p("A US regional bank normally sees 8,000 login requests per minute on payday morning. "
              "A botnet sends 400,000 requests per minute for 30 minutes. Without edge DDoS and "
              "bot controls, backend authentication melts and real customers cannot access wages. "
              "With layered controls, the edge provider absorbs volumetric traffic, bot scoring "
              "drops suspicious requests, the API gateway rate-limits per device and account, and "
              "the identity service remains under its 12,000 requests per minute safe capacity. "
              "The business outcome is not ‘we blocked an attack’; it is ‘salary access stayed "
              "within impact tolerance’." )
        )
    )
    return TopicSection("8.  Worked examples — numbers and decisions", "intermediate", body)


def _sec9() -> TopicSection:
    body = ol([
        "For this customer journey, what is the end-to-end latency budget and how much is consumed by DNS, TCP, TLS, gateway, service mesh and downstream systems?",
        "Where does TLS terminate, where is traffic re-encrypted, and where can plaintext exist?",
        "Which certificates are involved, who issues them, how are they rotated, and what breaks if one expires tonight?",
        "Is partner access protected by mTLS and scoped tokens, or are we still trusting IP allowlists and shared secrets?",
        "If a user, device or workload is inside the network, what additional proof is required before it reaches a crown-jewel system?",
        "What are the top five network dependencies for each important business service, and are they mapped in the resilience register?",
        "Can we survive loss of one carrier, one DNS provider, one cloud region, one firewall cluster and one certificate authority path?",
        "Are network logs, gateway logs and application traces correlated by request ID and synchronised time?",
        "Do third-party vendors get just-in-time, recorded, least-privilege access, or broad VPN access?",
        "What is the tested rollback plan for firewall, routing, DNS and certificate changes?",
        "How do we know data stays in the required geography during failover and support access?",
        "Which controls are preventive, which are detective, and which are only written in a policy document?",
    ])
    return TopicSection("9.  Questions to ask the team in any design review", "basic", body)


def _sec10() -> TopicSection:
    body = (
        red_flag(ul([
            "‘The network is green, so the application is fine.’ — Green reachability says nothing about TLS validation, gateway policy, packet loss, service mesh retries or downstream latency.",
            "‘It is safe because it is internal.’ — Internal networks are routinely reached through compromised laptops, vendors, service accounts and misconfigured cloud paths.",
            "‘IP allowlisting is enough for partner APIs.’ — IP helps, but mTLS, scoped tokens, transaction controls and monitoring are the stronger trust model.",
            "‘Zero trust means buying a SASE tool.’ — Tools help, but zero trust is an architecture and operating model: identity, device, least privilege, segmentation, monitoring and governance.",
            "‘Certificate renewal is an infrastructure detail.’ — Certificate expiry has caused major global outages. Treat certificate lifecycle as a production control with owners and testing.",
            "‘Active-active networking doubles resilience automatically.’ — It can double blast radius if routing, data consistency, failover and operations are not mature.",
            "‘DDoS is only a security problem.’ — In BFSI it is an operational-resilience and customer-harm problem because customers may be blocked from money access.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("Packet", "A small unit of data sent across a network, like one labelled parcel in a larger shipment."),
            ("IP address", "Internet Protocol address; the numeric destination used to route packets."),
            ("DNS", "Domain Name System; the phone book that maps names such as api.bank.com to IP addresses."),
            ("TCP", "Transmission Control Protocol; reliable transport that sets up a connection and retransmits lost data."),
            ("UDP / QUIC", "User Datagram Protocol and Quick UDP Internet Connections; lighter transport used where lower handshake cost or streaming behaviour matters."),
            ("TLS", "Transport Layer Security; cryptographic protocol that authenticates servers and encrypts data in transit."),
            ("mTLS", "Mutual Transport Layer Security; both client and server authenticate with certificates."),
            ("PKI", "Public Key Infrastructure; the governance and tooling for issuing, rotating and revoking certificates."),
            ("Certificate Authority", "Trusted issuer that signs certificates so clients can validate identities."),
            ("BGP", "Border Gateway Protocol; the internet routing protocol that tells networks which address ranges are reachable through which paths."),
            ("NAT", "Network Address Translation; maps private internal addresses to shared public addresses."),
            ("CDN", "Content Delivery Network; distributed edge network that serves content near users and absorbs traffic spikes."),
            ("WAF", "Web Application Firewall; edge control that blocks common web attacks before they reach applications."),
            ("DDoS", "Distributed Denial-of-Service; attack that floods a service with traffic to make it unavailable."),
            ("API gateway", "Policy enforcement and routing layer for application programming interfaces."),
            ("Service mesh", "Infrastructure layer for service-to-service traffic, often providing mTLS, retries, telemetry and traffic policy."),
            ("ZTNA", "Zero Trust Network Access; per-application access based on identity and context rather than broad network access."),
            ("SASE", "Secure Access Service Edge; cloud-delivered networking and security model combining wide-area networking, secure web gateway, cloud access security broker and zero-trust access."),
            ("RPKI", "Resource Public Key Infrastructure; cryptographic validation that helps prevent incorrect internet route announcements."),
            ("NTP / PTP", "Network Time Protocol and Precision Time Protocol; time synchronisation mechanisms used for logs, audit and low-latency environments."),
        ])
    )
    return TopicSection("10. Red flags + topic glossary", "basic", body)
