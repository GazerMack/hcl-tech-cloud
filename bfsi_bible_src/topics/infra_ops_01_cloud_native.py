"""Infrastructure & Operations · 01 — Cloud-native ops: K8s, observability,
SRE, FinOps."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="IV.1",
        slug="01-cloud-native-operations",
        title="Cloud-native operations — Kubernetes, observability, SRE, FinOps",
        one_liner=(
            "Building a cloud-native bank is one problem; <em>operating</em> one "
            "is another, and it is the harder of the two. This topic gives you "
            "fluent vocabulary in the four operational disciplines that decide "
            "whether your cloud-native estate stays healthy: containers and "
            "Kubernetes (where things run), observability (how you know what they "
            "are doing), Site Reliability Engineering (how you decide what to fix "
            "first), and FinOps (how you decide what it should cost). Each is "
            "now a board-level conversation in BFSI."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("‘Cloud-native’ is the Cloud Native Computing Foundation’s "
              "(CNCF) shorthand for: containerised, dynamically orchestrated, "
              "microservice-shaped, observable, automated. The technology "
              "centrepiece is <strong>Kubernetes (K8s)</strong>; the "
              "operational centrepieces are <strong>observability</strong>, "
              "<strong>Site Reliability Engineering (SRE)</strong>, and "
              "<strong>FinOps</strong>. None of them is optional once you "
              "have more than a handful of services in production.")
        )
        + H3("0.1  IT-side anchor — the apartment block versus your house")
        + it_anchor(
            p("Imagine running a single house. You buy the land, build "
              "rooms exactly the size you need, and the heating bill is "
              "yours alone. That is a <em>virtual machine (VM)</em>. Now "
              "imagine an apartment block: many flats sharing one "
              "building, each isolated by walls, plumbing and an "
              "electricity meter. Tenants come and go, the building "
              "manager moves them around when needed; the heating is "
              "shared but billed per flat. That is a <em>container</em> "
              "and the building manager is <em>Kubernetes</em>. Containers "
              "are lightweight and start in seconds; VMs are heavier and "
              "start in minutes; both are fine, just for different jobs.")
        )
        + H3("0.2  BFSI-side anchor — the trading floor at 9:15 a.m.")
        + bfsi_anchor(
            p("Every trading day, an Indian bank’s NSE-facing systems "
              "see a 50× spike at 9:15 a.m. UPI sees a 15× spike on "
              "Diwali night; UK card switches see a 4× spike on Black "
              "Friday afternoon. None of those spikes can be served by "
              "buying enough idle hardware year-round. Containers and "
              "Kubernetes let the bank scale up for the spike and "
              "scale down again. <strong>FinOps</strong> is the "
              "discipline of making sure that elasticity actually "
              "saves money rather than letting cloud bills drift "
              "upward forever.")
        )
        + H3("0.3  The four pillars of cloud-native operations")
        + ul([
            "<strong>Containers and Kubernetes</strong> — the runtime: "
            "how applications are packaged, scheduled and scaled.",
            "<strong>Observability</strong> — logs, metrics, traces, and "
            "Service-Level Objectives (SLOs); how you know whether the "
            "system is healthy.",
            "<strong>Site Reliability Engineering (SRE)</strong> — the "
            "operational discipline (Google, 2003 onward): treat "
            "operations as software, set error budgets, automate "
            "everything that hurts.",
            "<strong>FinOps</strong> — the financial discipline (FinOps "
            "Foundation, 2019 onward): align engineering, finance and "
            "business on a real-time view of cloud cost.",
        ])
    )
    return TopicSection(
        "0.  Primer — what cloud-native operations actually means",
        "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Why are these four disciplines specifically board-level in BFSI?")
        + ol([
            "<strong>Operational resilience is now a regulator topic.</strong> "
            "EU DORA (in force 17 January 2025), UK FCA / PRA / BoE "
            "Operational Resilience (fully embedded March 2025), MAS "
            "Notice 658, RBI BCM and IT Governance MD all require "
            "<em>quantified</em> impact tolerances and tested recovery; "
            "you cannot meet those without observability and SRE "
            "discipline.",
            "<strong>Cloud spend is now finance-committee territory.</strong> "
            "Tier-1 banks now spend USD 200M–1.5B per year on public "
            "cloud; without FinOps, 25–40% of that is wasted.",
            "<strong>Concentration risk on cloud providers.</strong> DORA "
            "designates hyperscalers as critical ICT third parties; UK "
            "CTP regime (FSMA 2023) mirrors this. The operating model "
            "must be ready for joint regulator review of the "
            "hyperscaler.",
            "<strong>Cyber and ransomware.</strong> Without observability, "
            "ransomware is detected by users; with it, by the SOC.",
            "<strong>Talent.</strong> The skills market for K8s, SRE, "
            "and FinOps is the tightest in BFSI tech. Programmes that "
            "ignore platform engineering end up with 50 teams "
            "reinventing the wheel and a permanent staffing problem.",
        ])
    )
    return TopicSection(
        "1.  Why cloud-native operations is a board-level topic",
        "basic", body)


def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  subgraph "Developer plane"\n'
            '    G["Git / GitHub / GitLab"]\n'
            '    C["CI / CD<br/>Argo CD, Flux, Jenkins, GitHub Actions"]\n'
            '  end\n'
            '  subgraph "Runtime plane — Kubernetes"\n'
            '    K["Cluster<br/>EKS / AKS / GKE / OpenShift"]\n'
            '    M["Service mesh<br/>Istio / Linkerd"]\n'
            '    P["Pods, deployments, jobs"]\n'
            '    K --> P\n'
            '    K --> M\n'
            '  end\n'
            '  subgraph "Observability plane"\n'
            '    O["OpenTelemetry SDK"]\n'
            '    L["Logs — ELK / Loki / Splunk"]\n'
            '    Me["Metrics — Prometheus / Mimir"]\n'
            '    T["Traces — Jaeger / Tempo / Honeycomb"]\n'
            '    A["Alerts — PagerDuty / Opsgenie"]\n'
            '    O --> L\n'
            '    O --> Me\n'
            '    O --> T\n'
            '    Me --> A\n'
            '  end\n'
            '  subgraph "FinOps plane"\n'
            '    Tg["Tagging, cost allocation"]\n'
            '    Cu["Cloudability / Apptio / Vantage / Kubecost"]\n'
            '    Tg --> Cu\n'
            '  end\n'
            '  G --> C --> K\n'
            '  P -- emit --> O\n'
            '  K -- billing data --> Tg',
            "Four operational planes around a Kubernetes cluster: "
            "developer, runtime, observability, FinOps.")
    )
    return TopicSection(
        "2.  The picture — four planes around the cluster",
        "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  Containers — what they actually are")
        + p("A container is a Linux process bundled with its own "
            "filesystem, network namespace, and resource limits. The "
            "two enabling kernel features: namespaces (isolation) and "
            "cgroups (limits). The packaging format is the OCI (Open "
            "Container Initiative) image, built with Docker, Buildah, "
            "Podman or Kaniko, stored in a registry (Docker Hub, AWS "
            "ECR, Azure Container Registry, GCP Artifact Registry, "
            "Harbor, JFrog Artifactory).")
        + H3("3.2  Kubernetes in 12 nouns")
        + ul([
            "<strong>Cluster</strong> — a group of machines (nodes) that "
            "run containers under one control plane.",
            "<strong>Node</strong> — a machine (VM or bare metal).",
            "<strong>Pod</strong> — the smallest deployable unit; one or "
            "more containers that share a network and storage.",
            "<strong>Deployment / StatefulSet / DaemonSet / Job / "
            "CronJob</strong> — controllers that manage pods.",
            "<strong>Service</strong> — a stable network endpoint in "
            "front of a set of pods.",
            "<strong>Ingress / Gateway</strong> — HTTP entry to the "
            "cluster from outside.",
            "<strong>ConfigMap / Secret</strong> — configuration and "
            "credentials, separated from the image.",
            "<strong>PersistentVolume / PersistentVolumeClaim</strong> — "
            "storage attached to pods.",
            "<strong>Namespace</strong> — virtual cluster within a "
            "cluster; the BFSI tenancy boundary.",
            "<strong>Custom Resource Definition (CRD) / Operator</strong> "
            "— extension mechanism; how vendors ship managed "
            "databases, caches, message brokers as Kubernetes-native "
            "resources.",
            "<strong>Helm chart / Kustomize / Carvel</strong> — packaging "
            "and templating for K8s manifests.",
            "<strong>Horizontal Pod Autoscaler (HPA) / Vertical Pod "
            "Autoscaler (VPA) / Cluster Autoscaler / Karpenter</strong> "
            "— how the cluster scales up and down.",
        ])
        + H3("3.3  Where Kubernetes runs in BFSI")
        + ul([
            "<strong>Cloud-managed</strong> — Amazon EKS, Azure AKS, "
            "Google GKE, Oracle OKE, IBM IKS. The control plane is "
            "managed; you supply nodes (or use Fargate / serverless "
            "nodes).",
            "<strong>Vendor distributions</strong> — Red Hat OpenShift "
            "(ubiquitous in EU and Indian banks; runs on cloud or on-"
            "prem), VMware Tanzu (legacy in many incumbents; "
            "Broadcom-era pricing under review), SUSE Rancher.",
            "<strong>Vanilla on-prem</strong> — kubeadm, kops, kOps, "
            "Cluster API. Rare at scale because of operational burden.",
        ])
        + H3("3.4  Service mesh — the connective tissue")
        + p("Once a cluster has more than ~30 services, mTLS, retries, "
            "circuit breakers, traffic shifting, and observability "
            "should not live in each service. A service mesh injects a "
            "sidecar (Envoy proxy) into every pod and provides those "
            "concerns uniformly. Major options: <strong>Istio</strong> "
            "(most features, steeper learning curve), <strong>"
            "Linkerd</strong> (CNCF graduated, simpler, Rust data "
            "plane), <strong>Consul Connect</strong> (HashiCorp), "
            "<strong>AWS App Mesh</strong>. Standard Chartered, ING, "
            "JPM, Capital One are public Istio references; Monzo "
            "ran Linkerd before moving to in-house.")
        + H3("3.5  GitOps and progressive delivery")
        + ul([
            "<strong>GitOps</strong> — declared cluster state lives in "
            "Git; an in-cluster controller (Argo CD, Flux) "
            "continuously reconciles the cluster to the Git "
            "repository. Auditable, easy to roll back, regulator-"
            "friendly.",
            "<strong>Progressive delivery</strong> — canary, blue-green, "
            "feature-flag rollouts. Argo Rollouts, Flagger, "
            "LaunchDarkly, Split.io, Unleash.",
            "<strong>Policy as code</strong> — Open Policy Agent (OPA) "
            "/ Gatekeeper / Kyverno enforce rules at admission "
            "(‘every pod must have resource limits and a non-root "
            "user’; ‘no public Load Balancers in this namespace’).",
        ])
        + H3("3.6  Observability — three pillars and one promise")
        + ul([
            "<strong>Logs</strong> — structured (JSON), centralised. "
            "Open: Elasticsearch / Logstash / Kibana (ELK), Grafana "
            "Loki, Fluent Bit. Commercial: Splunk, Datadog Logs, "
            "Sumo Logic, New Relic, Dynatrace.",
            "<strong>Metrics</strong> — Prometheus (CNCF) is the de-"
            "facto standard; long-term storage via Mimir, Thanos, "
            "Cortex; dashboards in Grafana. Commercial alternatives: "
            "Datadog, Dynatrace, New Relic, AppDynamics.",
            "<strong>Traces</strong> — distributed traces across "
            "services. <strong>OpenTelemetry (OTel)</strong> is now "
            "the vendor-neutral instrumentation standard (CNCF "
            "incubating; adopted by AWS, Azure, GCP, Datadog, "
            "Dynatrace, Splunk, Honeycomb, Lightstep, Elastic). The "
            "back end can be Jaeger, Tempo, Honeycomb, Datadog APM, "
            "Dynatrace.",
            "<strong>SLO / SLI / Error budget</strong> — defined "
            "in Google’s SRE book (2016): a Service-Level Indicator "
            "(SLI) measures behaviour; an SLO is a target on the "
            "SLI; the error budget is <em>1 − SLO</em>. When you "
            "burn the budget, you stop shipping features and fix "
            "reliability instead. Tools: Nobl9, Prometheus + "
            "sloth, Datadog SLO, Honeycomb.",
        ])
        + H3("3.7  Site Reliability Engineering — what it really means")
        + ul([
            "<strong>Treat operations as software.</strong> Toil is "
            "tracked; engineers spend ≤ 50% of time on toil and ≥ 50% "
            "on engineering improvements.",
            "<strong>Error budgets drive prioritisation.</strong> If "
            "you’re inside the budget, ship. If you’re burning it, "
            "stop and fix.",
            "<strong>Blameless postmortems.</strong> The PagerDuty / "
            "Etsy / Google approach: incidents end with a written "
            "review naming systems, not people.",
            "<strong>Chaos engineering.</strong> Inject failures in "
            "production-like environments to learn before customers "
            "do. Netflix Chaos Monkey, Gremlin, AWS Fault Injection "
            "Service, Azure Chaos Studio. UK PRA, MAS, RBI all now "
            "expect ‘scenario testing’ which in practice means "
            "chaos.",
        ])
        + H3("3.8  FinOps — the third great operational discipline")
        + p("FinOps was formalised by the FinOps Foundation in 2019. "
            "Its principles: collaboration between engineering and "
            "finance; everyone takes ownership of cloud spend; cost "
            "data is real-time and accessible; decisions driven by "
            "business value; central FinOps team; take advantage of "
            "the variable cost model.")
        + ul([
            "<strong>Tag every resource</strong> by cost centre, "
            "environment, application, owner.",
            "<strong>Allocate by tag</strong> back to the business; "
            "showback first, chargeback when mature.",
            "<strong>Forecast and budget</strong> per service; alert "
            "on anomalies (Kubecost, Vantage, Apptio Cloudability, "
            "AWS / Azure / GCP native cost tools, Finout).",
            "<strong>Rightsize</strong> — match instance / pod size "
            "to actual demand. Karpenter and HPA / VPA are core.",
            "<strong>Commitments</strong> — Reserved Instances, "
            "Savings Plans, Committed Use Discounts; layered "
            "purchases against forecast.",
            "<strong>Architectural levers</strong> — Spot / "
            "preemptible nodes for stateless workloads; ARM / "
            "Graviton; intelligent tiering of storage; "
            "stop-non-prod-on-weekends.",
        ])
    )
    return TopicSection(
        "3.  How cloud-native ops actually work — runtime, "
        "observability, SRE, FinOps",
        "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  Operational resilience — what each regulator now expects")
        + table(
            ["Regime", "What it requires from ops",
             "What it touches in your stack"],
            [
                ["<strong>EU DORA</strong> (in force 17 Jan 2025)",
                 "ICT risk framework, incident classification and "
                 "reporting, threat-led penetration tests (TLPT, "
                 "TIBER-EU style), oversight of critical ICT third "
                 "parties.",
                 "Observability (incident classification), SRE "
                 "(impact tolerances), FinOps (concentration / exit "
                 "scenarios)."],
                ["<strong>UK Operational Resilience</strong> "
                 "(fully embedded Mar 2025); CTP regime under FSMA "
                 "2023.",
                 "Identify ‘important business services’, set "
                 "impact tolerances, test through severe-but-"
                 "plausible scenarios, map dependencies.",
                 "Service catalogue, dependency map, SLOs aligned to "
                 "impact tolerances."],
                ["<strong>RBI Cyber Security &amp; IT Governance "
                 "MD</strong> (Nov 2023)",
                 "Defined recovery objectives, board-level cyber "
                 "reporting, rigorous outsourcing controls.",
                 "All four planes; observability is regulator-"
                 "facing."],
                ["<strong>MAS TRM</strong> (Singapore)",
                 "Recovery objectives, system availability, "
                 "incident reporting; cloud annex for cloud "
                 "specifics.",
                 "SLOs, runbooks, postmortems, evidence."],
                ["<strong>NYDFS Part 500</strong> (US, NY-licensed)",
                 "Cybersecurity programme, CISO certification, "
                 "incident reporting within 72 hours.",
                 "Logs and detection; observability for forensics."],
                ["<strong>OCC Heightened Standards / Fed SR 23-4</strong>",
                 "Third-party risk, model risk; expectations on "
                 "production incident management.",
                 "Postmortem rigour; vendor / cloud reviews."],
            ]
        )
        + H3("4.2  How banks worldwide are organised today")
        + ul([
            "<strong>Platform team</strong> owns the cluster, the "
            "service mesh, the CI/CD pipelines, the observability "
            "stack, the policy engine, the FinOps tooling. Built as "
            "an Internal Developer Platform (IDP) — Backstage "
            "(Spotify, JPMC, Standard Chartered, ING), Humanitec, "
            "Port, Cortex, Atlassian Compass.",
            "<strong>SRE function</strong> embedded with each tier-1 "
            "service team or pooled centrally.",
            "<strong>FinOps team</strong> increasingly reports into "
            "the CFO via the CIO; runs monthly business reviews per "
            "domain.",
            "<strong>Security operations centre (SOC)</strong> "
            "consumes the observability data; SIEM (Splunk, Sentinel, "
            "Chronicle, Elastic) sits next to the metrics platform.",
        ])
        + H3("4.3  Public references")
        + ul([
            "<strong>India</strong> — HDFC Bank invested heavily in "
            "OpenShift after multiple high-profile mobile-banking "
            "outages in 2020–22. ICICI, Bajaj Finserv on EKS / AKS. "
            "PhonePe operates one of the largest Kubernetes estates "
            "in India.",
            "<strong>United States</strong> — JPM Athena uses Kubernetes "
            "extensively; Capital One on EKS; Wells Fargo, BoA on "
            "OpenShift hybrid; Goldman Marquee on K8s.",
            "<strong>United Kingdom</strong> — Standard Chartered "
            "‘aXess’ on AKS; NatWest Group on Azure; Lloyds on AKS / "
            "OpenShift; Monzo on AWS.",
            "<strong>Eurozone</strong> — ING (Spain, Belgium, "
            "Netherlands) on a hybrid OpenShift + AKS estate; BBVA "
            "on AWS / GCP; Deutsche on GCP partnership.",
            "<strong>Singapore</strong> — DBS hybrid cloud with "
            "private K8s + AWS; GXS, Trust on AWS / GCP cloud-"
            "native.",
            "<strong>Brazil</strong> — Nubank on AWS, K8s, "
            "Datomic; Itaú on hybrid Red Hat + AWS.",
        ])
    )
    return TopicSection(
        "4.  Region by region — regulators, organisation, "
        "and references",
        "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  Hardening Kubernetes for BFSI")
        + ul([
            "<strong>Pod Security Standards (PSS)</strong> — restricted "
            "profile by default; no privileged pods, no host "
            "networking, no root users.",
            "<strong>Network policies</strong> — default-deny; "
            "explicit allowlists per namespace.",
            "<strong>Image signing and provenance</strong> — Sigstore "
            "(cosign), in-toto / SLSA attestations; bank registries "
            "enforce signed images only.",
            "<strong>Software Bill of Materials (SBOM)</strong> — "
            "CycloneDX or SPDX per image; required by EU Cyber "
            "Resilience Act (2024) and US Executive Order 14028.",
            "<strong>Runtime protection</strong> — Falco, Sysdig "
            "Secure, Aqua, Wiz, Prisma Cloud, Microsoft Defender "
            "for Containers.",
            "<strong>Secrets management</strong> — HashiCorp Vault, "
            "AWS Secrets Manager, Azure Key Vault, GCP Secret "
            "Manager; secrets injected via CSI driver, never baked "
            "into images.",
            "<strong>Service-to-service auth</strong> — mTLS via "
            "service mesh; SPIFFE / SPIRE for workload identity in "
            "vendor-neutral settings.",
            "<strong>Multi-tenancy</strong> — namespaces with quotas "
            "for soft tenancy; vCluster, virtual clusters, or "
            "separate clusters for hard tenancy.",
        ])
        + H3("5.2  Reliability patterns inside the cluster")
        + ul([
            "<strong>Pod Disruption Budgets (PDB)</strong> — protect "
            "service availability during voluntary disruptions "
            "(node drains, upgrades).",
            "<strong>Topology Spread Constraints</strong> — spread "
            "replicas across availability zones automatically.",
            "<strong>Readiness, liveness and startup probes</strong> "
            "— let the cluster make correct decisions about traffic "
            "and restarts.",
            "<strong>Graceful shutdown</strong> — handle SIGTERM, "
            "drain in-flight requests within terminationGracePeriod.",
            "<strong>Bulkheads and circuit breakers</strong> — at the "
            "service mesh and inside the application "
            "(Resilience4j, Polly, Hystrix-pattern).",
        ])
        + H3("5.3  OpenTelemetry — the only instrumentation worth doing")
        + p("OpenTelemetry merged OpenTracing and OpenCensus; it is now "
            "the only vendor-neutral instrumentation standard. SDKs in "
            "every major language; auto-instrumentation for many "
            "frameworks. The OpenTelemetry Collector receives, "
            "processes and exports to any compliant backend "
            "(Jaeger, Tempo, Honeycomb, Datadog, New Relic, "
            "Dynatrace, Splunk Observability, AWS X-Ray, Azure "
            "Monitor, GCP Cloud Trace). <em>Standardise on OTel "
            "first; pick a back end second.</em> That gives you "
            "vendor portability for the operationally most "
            "consequential piece of middleware in a bank.")
        + H3("5.4  Reliability metrics that survive contact with the board")
        + ul([
            "<strong>Availability</strong> — % of time the service "
            "meets its SLO. Reported per service and per important "
            "business service.",
            "<strong>Mean Time To Detect (MTTD)</strong> and <strong>"
            "Mean Time To Recover (MTTR)</strong>.",
            "<strong>Change failure rate</strong> — % of deploys that "
            "cause an incident.",
            "<strong>Deployment frequency and lead time</strong> — "
            "the four DORA (DevOps Research & Assessment) metrics; "
            "elite teams deploy on demand and recover in <1 hour.",
            "<strong>Toil percentage</strong> — measured per SRE per "
            "quarter; > 50% means the platform is failing the "
            "engineers.",
        ])
        + H3("5.5  FinOps maturity model")
        + ul([
            "<strong>Crawl</strong> — visibility: tagging, dashboards, "
            "monthly reviews. Most BFSI estates are here in 2025.",
            "<strong>Walk</strong> — allocation: showback per app and "
            "team; rightsizing programmes; commitments tied to "
            "forecasts.",
            "<strong>Run</strong> — optimisation: unit economics "
            "(cost per transaction, per customer, per API call); "
            "automated rightsizing; spot strategies; engineers see "
            "cost on every PR.",
        ])
        + H3("5.6  Sustainability (Green Software)")
        + p("EU Corporate Sustainability Reporting Directive (CSRD) "
            "and ISSB IFRS S2 require listed financials to disclose "
            "Scope 3 emissions; the IT estate is increasingly part of "
            "that. Green Software Foundation’s carbon-aware patterns "
            "(shift workloads to greener regions / hours), AWS "
            "Customer Carbon Footprint, Azure Emissions Impact "
            "Dashboard, GCP Carbon Footprint reports.")
    )
    return TopicSection(
        "5.  Advanced — hardening, reliability, OTel, metrics, "
        "FinOps maturity",
        "advanced", body)


def _sec6() -> TopicSection:
    body = (
        H3("6.1  Decision matrix — where to run a workload")
        + table(
            ["Workload", "Best home in 2025", "Why"],
            [
                ["Channel apps (mobile / web BFFs, partner APIs)",
                 "Cloud-managed K8s (EKS / AKS / GKE)",
                 "Spiky traffic, fast iteration, mature managed "
                 "service."],
                ["Long-running batch (overnight risk, regulatory "
                 "reporting)",
                 "K8s Jobs on Spot / preemptible, or Serverless "
                 "(Lambda / Functions / Cloud Run)",
                 "Idle 18h/day; FinOps savings dominate."],
                ["Tier-1 stateful — core ledger DB, ESB, MQ",
                 "Managed cloud DB or VMs, NOT raw K8s",
                 "Data plane is too sensitive; vendors’ K8s "
                 "operators are improving but BFSI tier-1 still "
                 "uses managed services."],
                ["Real-time fraud scoring",
                 "K8s with HPA + GPUs / Inferentia, "
                 "OpenTelemetry-instrumented",
                 "Latency budget under 100 ms; needs autoscale."],
                ["Capital-markets risk grids",
                 "On-prem HPC or large-instance cloud, "
                 "containerised with Slurm / Volcano",
                 "Embarrassingly parallel; cost / GPU dominates "
                 "K8s niceties."],
                ["Vendor SaaS (Salesforce, Workday, Mambu, Thought "
                 "Machine, Snowflake)",
                 "Vendor-operated; bank operates only the "
                 "integrations",
                 "FinOps still applies to the consumption."],
            ]
        )
        + H3("6.2  Decision matrix — observability tooling")
        + table(
            ["Choice", "When it wins", "Watch-outs"],
            [
                ["<strong>Open source</strong> (Prometheus + Grafana "
                 "+ Loki + Tempo + OTel)",
                 "When the platform team has scale and skill; "
                 "vendor-neutral; lowest run-rate cost.",
                 "Real operational burden; pager rotations, upgrades, "
                 "long-term storage all on you."],
                ["<strong>Commercial APM</strong> (Datadog, Dynatrace, "
                 "New Relic, Splunk Observability, AppDynamics)",
                 "When time-to-value matters and headcount is the "
                 "constraint; mature root-cause analysis.",
                 "Cost grows with cardinality; ‘ingest gravity’ "
                 "creates lock-in. Standardise on OTel to keep "
                 "options open."],
                ["<strong>Cloud-native</strong> (CloudWatch, Azure "
                 "Monitor, GCP Operations Suite)",
                 "When the estate is single-cloud; cheap; tight "
                 "integration.",
                 "Multi-cloud or hybrid is awkward; export to a "
                 "neutral back end may still be needed."],
            ]
        )
    )
    return TopicSection(
        "6.  Decision matrices — workload placement and observability",
        "intermediate", body)


def _sec7() -> TopicSection:
    body = (
        example(
            "Capital One — open-source-first cloud-native ops on AWS",
            ol([
                "All-in on AWS since 2020; standardised on EKS, "
                "Argo CD for GitOps, Open Policy Agent for "
                "guardrails, OpenTelemetry for tracing.",
                "Cloud Custodian (open-sourced internally) "
                "automates policy and FinOps controls.",
                "Public reference: 2019 breach was a misconfigured "
                "AWS WAF + over-permissioned IAM role; the response "
                "drove deeper investments in policy-as-code and SRE.",
            ])
        )
        + example(
            "Standard Chartered ‘aXess’ — Azure platform engineering",
            ol([
                "Self-service developer platform on Azure (AKS), "
                "Backstage portal, Argo CD GitOps, Datadog "
                "observability.",
                "Embedded SRE function; published SLO catalogue per "
                "tier-1 service.",
                "FinOps via Apptio Cloudability across Azure spend.",
                "HCLTech is one of the partners delivering platform "
                "components.",
            ])
        )
        + example(
            "ING — early SRE and BizDevOps adopter in EU banking",
            ol([
                "ING’s 2015–2018 transformation reorganised IT into "
                "‘squads’ and ‘tribes’ Spotify-style, embedded "
                "SREs, and built a cloud-native platform on "
                "OpenShift and AWS.",
                "Public references: the ‘bank of the future’ "
                "engineering blog series; case studies with Red "
                "Hat and AWS.",
                "Continued evolution: post-2020 doubled down on "
                "FinOps and observability under regulator pressure "
                "(DNB, ECB).",
            ])
        )
        + example(
            "PhonePe — Kubernetes at Indian-volume scale",
            ol([
                "Operates a multi-cluster K8s estate handling 10B+ "
                "transactions per month; runs in Indian cloud "
                "regions for RBI data localisation.",
                "Internal observability built on Prometheus + "
                "ClickHouse + Grafana; OTel adoption in 2023–24.",
                "FinOps maturity high — public talks at KubeCon and "
                "Indian cloud-native conferences.",
            ])
        )
        + example(
            "An incumbent bank’s SRE adoption — 18 months",
            ol([
                "Month 1: define ‘important business services’ "
                "(mobile banking, ATM, payments, internet banking, "
                "card auth) per FCA / DORA / RBI; set impact "
                "tolerances.",
                "Month 3: instrument top 10 services with OTel; "
                "publish SLO dashboards; SRE on-call rotation.",
                "Month 6: error-budget policy approved by CTO and "
                "regulator-facing risk function.",
                "Month 9: platform team forms; Backstage portal; "
                "GitOps for top 5 services.",
                "Month 12: FinOps team in place; tagging policy "
                "audited; first showback reports per LOB.",
                "Month 18: chaos drills run quarterly; first "
                "regulator-witnessed scenario test passes.",
            ])
        )
    )
    return TopicSection(
        "7.  Worked examples — five real BFSI cloud-native ops "
        "journeys",
        "intermediate", body)


def _sec8() -> TopicSection:
    return TopicSection(
        "8.  Questions a leader asks in any cloud-native ops review",
        "basic",
        ol([
            "What are our important business services per regulator "
            "(DORA / FCA / RBI / MAS), and what are their impact "
            "tolerances and current SLOs?",
            "Are all tier-1 services instrumented with OpenTelemetry "
            "(or do we have the migration plan)?",
            "What is our error-budget policy, and how often have we "
            "stopped a release because the budget was burned?",
            "Do we have a single Internal Developer Platform, and "
            "what is its adoption rate across teams?",
            "Is GitOps the standard for cluster state, and is the "
            "Git repository the audit record?",
            "What is the result of the last chaos / scenario test, "
            "and what did it surface that we have since fixed?",
            "How quickly do we patch a critical CVE end-to-end "
            "(image rebuild, registry, deploy)?",
            "What is the current cloud bill, the trend, and the "
            "unit cost per transaction / per customer?",
            "Are we using Spot / preemptible nodes for non-critical "
            "workloads, and are commitments aligned with our "
            "forecast?",
            "Where is concentration risk on our cloud provider, and "
            "what is the credible exit plan per DORA / RBI / PRA?",
            "Are images signed, SBOMs generated, and is the registry "
            "set to deny unsigned images?",
            "Have we tested cross-region failover for our K8s "
            "control plane and our managed databases in the last "
            "12 months?",
        ]))


def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘We don’t need K8s; serverless is enough.’ — Serverless is "
            "great for spiky and stateless work; K8s remains the "
            "default for stateful, long-running, complex workloads. "
            "Don’t pick a side religiously.",
            "‘We deploy 100× a day, so we are SRE-mature.’ — "
            "Deployment frequency without correlated MTTR and change "
            "failure rate is a vanity metric. Watch the four DORA "
            "metrics together.",
            "‘Observability equals logs.’ — Logs are one pillar. "
            "Without metrics and traces, root cause is guesswork.",
            "‘Our SLO is 99.99%.’ — 99.99% on what SLI, measured how, "
            "with which error-budget policy? An undefined SLO is just "
            "a slogan.",
            "‘FinOps is procurement.’ — FinOps is a cross-functional "
            "discipline involving engineering, finance, product. "
            "Procurement is one input.",
            "‘We trust our cloud bill — it’s automated.’ — Untagged "
            "and forgotten resources can be 10–30% of a tier-1 "
            "estate. Audit, don’t trust.",
            "‘Service mesh adds complexity, we don’t need it.’ — At "
            "<20 services, fine. At >50, you will reinvent it badly "
            "in each service.",
            "‘We’ll just use Datadog because it’s easy.’ — Datadog is "
            "excellent; it is also expensive and concentrates "
            "ingest. Standardise on OTel, then choose a back end "
            "you can swap out.",
            "‘Our chaos exercise is a pen test.’ — Pen tests probe "
            "for vulnerabilities; chaos exercises probe for "
            "operational resilience. Different teams, different "
            "outcomes.",
            "‘DORA is just an EU thing.’ — UK CTP regime, RBI IT "
            "Governance MD, MAS TRM, NYDFS Part 500 are all "
            "converging on the same operational expectations.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("Container", "A Linux process bundled with its own "
                "filesystem and resource limits."),
            ("OCI", "Open Container Initiative — the image format "
                "standard."),
            ("Kubernetes (K8s)", "Open-source container orchestrator "
                "from Google (Borg → Kubernetes, 2014); CNCF-"
                "graduated."),
            ("EKS / AKS / GKE / OKE / IKS", "Cloud-managed K8s on AWS "
                "/ Azure / GCP / Oracle / IBM."),
            ("OpenShift", "Red Hat’s opinionated Kubernetes "
                "distribution; ubiquitous in EU and Indian banks."),
            ("Helm / Kustomize", "Packaging and templating for K8s "
                "manifests."),
            ("Operator", "Custom controller that manages an "
                "application via CRDs (databases, brokers, etc.)."),
            ("HPA / VPA / Cluster Autoscaler / Karpenter", "Pod- and "
                "node-level autoscalers."),
            ("Service mesh", "Sidecar-based platform layer for mTLS, "
                "retries, traffic shifting (Istio, Linkerd, Consul "
                "Connect, AWS App Mesh)."),
            ("GitOps", "Cluster state declared in Git, reconciled by "
                "an in-cluster controller (Argo CD, Flux)."),
            ("Observability", "Logs, metrics, traces; the ability to "
                "infer system state from outside."),
            ("OpenTelemetry (OTel)", "CNCF vendor-neutral "
                "instrumentation standard; merged OpenTracing + "
                "OpenCensus."),
            ("SRE", "Site Reliability Engineering — Google’s "
                "discipline of operating software reliably and "
                "automatically."),
            ("SLI / SLO / Error budget", "Indicator / objective / "
                "(1 − SLO); the SRE prioritisation engine."),
            ("MTTD / MTTR", "Mean Time To Detect / Recover."),
            ("DORA metrics", "Four DevOps Research & Assessment "
                "metrics: deploy frequency, lead time, MTTR, "
                "change failure rate. Distinct from EU DORA."),
            ("Chaos engineering", "Inject failures to test "
                "resilience (Chaos Monkey, Gremlin, AWS FIS, Azure "
                "Chaos Studio)."),
            ("FinOps", "Discipline of managing cloud financial "
                "operations; FinOps Foundation framework."),
            ("Showback / chargeback", "Allocate cloud cost back to "
                "the consuming team, informationally / "
                "financially."),
            ("Spot / preemptible / Reserved / Savings Plan", "Cloud "
                "purchase options balancing flexibility and cost."),
            ("SBOM", "Software Bill of Materials — required by EU "
                "CRA and US EO 14028."),
            ("Sigstore / cosign / SLSA", "Image signing and supply-"
                "chain provenance standards."),
            ("Pod Security Standards", "Restricted / baseline / "
                "privileged profiles built into K8s."),
            ("OPA / Gatekeeper / Kyverno", "Policy-as-code engines "
                "for K8s admission."),
            ("Backstage / Humanitec / Port / Cortex", "Internal "
                "Developer Platform tooling."),
            ("DORA (EU)", "Digital Operational Resilience Act; in "
                "force 17 January 2025."),
            ("CTP regime", "UK Critical Third Parties regime under "
                "FSMA 2023."),
            ("CSRD / IFRS S2", "Sustainability disclosure regimes "
                "now touching IT carbon footprint."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
