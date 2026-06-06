"""Cloud FinOps & Cost Governance · 01 — Cloud FinOps and cost governance at scale.

Covers FinOps framework, cloud cost optimisation, showback/chargeback,
reserved instances, savings plans, spot/preemptible, unit economics,
and the regulatory dimension of cloud spend in BFSI.
"""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="IX.1",
        slug="01-cloud-finops-cost-governance",
        title="Cloud FinOps and cost governance at scale — the CFO meets the CTO",
        one_liner=(
            "A tier-1 bank can spend USD 500M–2B per year on cloud. Without "
            "FinOps discipline, 30–40% of that is waste — idle resources, "
            "over-provisioned instances, orphaned storage, un-negotiated "
            "on-demand pricing. FinOps (Financial Operations for cloud) is the "
            "practice that gives engineering, finance, and business a shared "
            "language for cloud cost, a shared accountability model, and the "
            "tools to optimise spend without sacrificing performance or "
            "compliance. This topic maps the full FinOps landscape for BFSI."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


# ------------------------------------------------------------------ sec 0

def _sec0() -> TopicSection:
    body = (
        primer(
            p("Cloud changed the economics of IT from CapEx (Capital Expenditure "
              "— buy servers, depreciate over 5 years) to OpEx (Operational "
              "Expenditure — pay monthly for what you use). This sounds like a "
              "good thing, and it is — but it also means costs are variable, "
              "unpredictable, and owned by every engineer who provisions a "
              "resource. Without governance, cloud costs grow 20–30% year-on-year "
              "with no corresponding improvement in business outcomes. FinOps is "
              "the discipline that fixes this.")
        )
        + H3("0.1  IT-side anchor — your electricity bill")
        + it_anchor(
            p("Before smart meters, you paid a flat electricity bill estimated "
              "by the utility. You had no idea which appliance consumed how much. "
              "Smart meters changed that — you can now see real-time consumption, "
              "identify the tumble dryer as the biggest cost, set a budget alert "
              "when you exceed your target, and shift heavy usage to off-peak "
              "tariffs. Cloud without FinOps is like electricity without a smart "
              "meter: every team provisions resources ('turns on appliances'), "
              "finance receives a huge monthly bill, and nobody knows which team "
              "or application is responsible for the spike. FinOps is the "
              "'smart meter' for cloud.")
        )
        + H3("0.2  BFSI-side anchor — why your bank's cloud bill matters to you")
        + bfsi_anchor(
            p("When a bank spends USD 100M more than necessary on cloud, that "
              "money comes from somewhere: higher fees for customers, lower "
              "returns for shareholders, less investment in new products, or "
              "lower bonuses for staff. In BFSI, where Cost-to-Income Ratio "
              "(CIR) is a key performance metric watched by analysts and "
              "regulators (the RBI tracks CIR for Indian banks, the ECB "
              "uses efficiency ratios in its SREP assessment), cloud waste "
              "directly worsens the ratio. A bank with a 60% CIR that lets "
              "cloud costs grow uncontrolled will see its CIR deteriorate — "
              "triggering analyst downgrades and regulatory questions.")
        )
        + H3("0.3  What FinOps is and is not")
        + ul([
            "<strong>FinOps IS:</strong> A cultural practice and set of "
            "processes that bring financial accountability to cloud spending. "
            "It is a cross-functional discipline — engineering, finance, and "
            "business jointly own cloud cost.",
            "<strong>FinOps IS NOT:</strong> A cost-cutting exercise. The goal "
            "is not to spend less — it is to spend efficiently. A bank might "
            "spend more on cloud after FinOps maturity if the incremental "
            "spend delivers proportional business value. FinOps is about "
            "maximising the value of every dollar spent on cloud.",
            "<strong>FinOps IS NOT:</strong> Just a tool. Tools (CloudHealth, "
            "Apptio Cloudability, FOCUS) are enablers, but FinOps is "
            "fundamentally a people-and-process discipline.",
        ])
    )
    return TopicSection(
        "0.  Primer — anchored to things you already know", "basic", body)


# ------------------------------------------------------------------ sec 1

def _sec1() -> TopicSection:
    body = (
        p("FinOps exists in BFSI because cloud adoption has reached a scale "
          "where costs are material to the P&L:")
        + ol([
            "<strong>Cloud spend is now a top-5 cost line.</strong> At "
            "tier-1 banks, cloud and infrastructure costs are USD 500M–2B "
            "annually. This is comparable to staff costs in some business "
            "units. It demands the same financial rigour applied to any "
            "major cost centre.",
            "<strong>Variable cost is harder to govern.</strong> In the "
            "on-prem world, capacity was fixed (you bought servers for 5 "
            "years). In the cloud world, any developer can spin up a "
            "USD 50,000/month GPU cluster with a single API call. "
            "Without controls, costs are unbounded.",
            "<strong>Multi-cloud complexity.</strong> Most banks use 2–3 "
            "clouds (AWS, Azure, GCP) plus private cloud. Each has "
            "different pricing models, discount mechanisms, and billing "
            "granularity. Comparing costs across clouds is non-trivial.",
            "<strong>Regulatory scrutiny of outsourcing costs.</strong> "
            "Regulators (PRA, ECB, RBI, MAS) increasingly scrutinise "
            "concentration risk and cost dependency on cloud providers. "
            "A bank must demonstrate that cloud spend is governed and "
            "that it has exit optionality.",
            "<strong>Business case pressure.</strong> Many cloud migration "
            "business cases promised 20–30% TCO savings vs. on-prem. "
            "Without FinOps, those savings rarely materialise — leading "
            "to board-level questions and potential cloud-repatriation "
            "conversations.",
            "<strong>Sustainability and ESG.</strong> Cloud compute has a "
            "carbon footprint. Waste compute is waste energy. FinOps "
            "aligns with ESG (Environmental, Social, Governance) goals — "
            "optimising cloud reduces both cost and carbon.",
        ])
    )
    return TopicSection(
        "1.  Why FinOps exists — first principles", "basic", body)


# ------------------------------------------------------------------ sec 2

def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart TB\n'
            '  subgraph "INFORM"\n'
            '    VIS["Visibility\u003cbr/\u003eWho is spending what?"]\n'
            '    ALL["Allocation\u003cbr/\u003eTag and attribute costs to teams"]\n'
            '    BEN["Benchmarking\u003cbr/\u003eCompare unit costs internally and externally"]\n'
            '  end\n'
            '  subgraph "OPTIMISE"\n'
            '    RS["Right-sizing\u003cbr/\u003eMatch resources to actual usage"]\n'
            '    RC["Rate optimisation\u003cbr/\u003eRIs, Savings Plans, EDPs"]\n'
            '    AR["Architecture optimisation\u003cbr/\u003eServerless, spot, storage tiering"]\n'
            '  end\n'
            '  subgraph "OPERATE"\n'
            '    BUD["Budgets and forecasts"]\n'
            '    GOV["Governance\u003cbr/\u003ePolicies, guardrails, approval workflows"]\n'
            '    CHG["Showback / chargeback\u003cbr/\u003eCosts flow to P and L owners"]\n'
            '  end\n'
            '  VIS --> ALL --> BEN --> RS --> RC --> AR --> BUD --> GOV --> CHG\n'
            '  CHG -->|"Feedback loop"| VIS',
            "The FinOps lifecycle — Inform, Optimise, Operate — is a "
            "continuous cycle, not a one-time project."
        )
        + p("The FinOps Foundation (part of the Linux Foundation) defines "
            "this as the three phases of the FinOps lifecycle. Most banks "
            "are still in the 'Inform' phase — they can see the bill but "
            "cannot attribute costs to teams or business outcomes.")
    )
    return TopicSection(
        "2.  The core concept in one picture", "basic", body)


# ------------------------------------------------------------------ sec 3

def _sec3() -> TopicSection:
    body = (
        H3("3.1  Phase 1: INFORM — visibility and allocation")
        + p("The first step is knowing who spends what on which cloud "
            "resources, for which application, serving which business "
            "function.")
        + ul([
            "<strong>Tagging strategy.</strong> Every cloud resource must "
            "be tagged with metadata: application name, business unit, "
            "cost centre, environment (dev/test/staging/prod), owner. "
            "Without tags, cost allocation is impossible. Best practice: "
            "enforce mandatory tags via infrastructure-as-code policies "
            "(OPA/Rego, AWS Service Control Policies, Azure Policy). "
            "Tag compliance below 90% makes FinOps unreliable.",
            "<strong>Cost allocation.</strong> Shared services (networking, "
            "security tooling, Kubernetes clusters) must be allocated to "
            "consuming teams — pro rata by usage, by headcount, or by "
            "fixed share. This is the most contentious part of FinOps.",
            "<strong>Showback vs. chargeback.</strong> Showback shows teams "
            "their costs (informational). Chargeback debits costs to the "
            "team's P&L (financial accountability). Most banks start with "
            "showback; mature organisations move to full chargeback.",
            "<strong>Unit economics.</strong> The critical metric: cost per "
            "business unit — cost per transaction, cost per customer, cost "
            "per trade, cost per policy. This links cloud spend to business "
            "value. If cost-per-transaction is declining while transaction "
            "volume is growing, cloud efficiency is improving.",
        ])

        + H3("3.2  Phase 2: OPTIMISE — spend less for the same outcomes")
        + p("Cloud optimisation levers, in order of impact:")
        + table(
            ["Optimisation lever", "Typical savings", "How it works"],
            [
                ["<strong>Right-sizing</strong>",
                 "20–40% of compute costs",
                 "Analyse CPU/memory utilisation over 14–30 days. If a VM "
                 "averages 10% CPU, downsize it. Tools: AWS Compute "
                 "Optimizer, Azure Advisor, GCP Recommender, Spot.io "
                 "(now Spot by NetApp), CloudHealth, Densify."],
                ["<strong>Reserved Instances (RIs) / Savings Plans</strong>",
                 "30–72% vs. on-demand for committed workloads",
                 "Commit to 1-year or 3-year usage in exchange for "
                 "discounted rates. AWS offers Compute Savings Plans "
                 "(flexible across instance families), EC2 RIs (locked to "
                 "instance type), and Azure Reservations. 3-year all-upfront "
                 "gives the deepest discount."],
                ["<strong>Enterprise Discount Programs (EDPs)</strong>",
                 "5–15% additional discount",
                 "A bank commits to a minimum annual cloud spend (e.g., "
                 "USD 100M/year) and receives a blanket discount on all "
                 "services. Requires CFO-level negotiation with cloud "
                 "provider."],
                ["<strong>Spot / preemptible instances</strong>",
                 "60–90% vs. on-demand",
                 "Use spare cloud capacity at a deep discount but the "
                 "instance can be terminated with 2-minute notice. "
                 "Suitable for batch processing, testing, CI/CD, ML "
                 "training — not for production banking transactions."],
                ["<strong>Storage tiering</strong>",
                 "50–80% for cold/archive data",
                 "Move infrequently accessed data from S3 Standard to "
                 "S3 Glacier Instant Retrieval or Azure Cool/Archive. "
                 "Regulatory retention data (7–10 year retention) should "
                 "be in the cheapest archive tier."],
                ["<strong>Idle resource cleanup</strong>",
                 "5–15% of total spend",
                 "Terminate unused resources: stopped VMs still incur "
                 "storage and IP costs, unattached EBS volumes, orphaned "
                 "snapshots, idle load balancers, unused Elastic IPs. "
                 "Automate cleanup with scheduled Lambda/Azure Functions."],
                ["<strong>Architecture optimisation</strong>",
                 "Variable — potentially 50%+",
                 "Move event-driven workloads to serverless (Lambda, "
                 "Cloud Functions), use managed services instead of "
                 "self-managed (RDS vs. self-hosted PostgreSQL), adopt "
                 "containers for better bin-packing on Kubernetes."],
            ]
        )

        + H3("3.3  Phase 3: OPERATE — governance and accountability")
        + ul([
            "<strong>Budgets and alerts.</strong> Every team has a monthly "
            "cloud budget. Alerts fire at 75%, 90%, and 100% of budget. "
            "AWS Budgets, Azure Cost Management, GCP Budgets provide "
            "native alerting.",
            "<strong>Anomaly detection.</strong> Automated detection of "
            "unexpected cost spikes — a misconfigured auto-scaling "
            "policy, a forgotten GPU instance, or a data-transfer spike. "
            "Tools: AWS Cost Anomaly Detection, Anodot, CloudHealth, "
            "Apptio Cloudability.",
            "<strong>Policy enforcement.</strong> Prevent waste before it "
            "happens: block provisioning of instance types larger than "
            "needed, require tagging before resource creation, auto-stop "
            "dev/test environments outside business hours, restrict "
            "expensive GPU instances to approved ML workloads.",
            "<strong>FinOps operating model.</strong> A central FinOps "
            "team (3–10 people at a mid-size bank, 15–30 at a tier-1) "
            "works with engineering leads and finance. The team produces "
            "weekly cost reports, monthly variance analysis, and "
            "quarterly optimisation recommendations.",
        ])
    )
    return TopicSection(
        "3.  How it actually works — Inform, Optimise, Operate",
        "intermediate", body)


# ------------------------------------------------------------------ sec 4

def _sec4() -> TopicSection:
    body = (
        H3("4.1  FinOps tools and platforms")
        + table(
            ["Tool / Platform", "Type", "Strengths"],
            [
                ["<strong>AWS Cost Explorer + AWS Budgets + "
                 "AWS Compute Optimizer</strong>",
                 "Native (AWS)",
                 "Free, deeply integrated. Cost Explorer for analysis, "
                 "Budgets for alerts, Compute Optimizer for right-sizing. "
                 "Limited for multi-cloud."],
                ["<strong>Azure Cost Management + Advisor</strong>",
                 "Native (Azure)",
                 "Free, integrated with EA (Enterprise Agreement) billing. "
                 "Good for Azure-centric estates."],
                ["<strong>GCP Billing + Recommender</strong>",
                 "Native (GCP)",
                 "BigQuery export for custom analytics. Active Assist "
                 "recommender for right-sizing and idle cleanup."],
                ["<strong>Apptio Cloudability (IBM)</strong>",
                 "Multi-cloud FinOps platform",
                 "Strong multi-cloud, mature allocation engine, FOCUS "
                 "format support. IBM acquired Apptio 2023."],
                ["<strong>CloudHealth (VMware / Broadcom)</strong>",
                 "Multi-cloud FinOps platform",
                 "Large BFSI installed base. Multi-cloud cost and "
                 "governance. Broadcom acquired VMware 2023."],
                ["<strong>Spot by NetApp</strong>",
                 "Optimisation-focused (spot automation + right-sizing)",
                 "Elastigroup for spot instance management, Ocean for "
                 "Kubernetes cost optimisation. Strong automation."],
                ["<strong>Kubecost / OpenCost</strong>",
                 "Kubernetes cost allocation (open-source)",
                 "Kubernetes-native cost allocation to namespaces, "
                 "labels, and pods. OpenCost is the CNCF project. "
                 "Essential for banks running Kubernetes."],
                ["<strong>Infracost</strong>",
                 "Shift-left cost estimation (open-source)",
                 "Shows cloud cost impact in Terraform pull requests "
                 "before deployment. Engineers see cost before provisioning."],
                ["<strong>Vantage</strong>",
                 "Multi-cloud cost platform",
                 "Modern UI, Kubernetes cost reporting, unit cost metrics. "
                 "Growing in mid-market."],
                ["<strong>FOCUS (FinOps Cost and Usage Specification)</strong>",
                 "Open standard",
                 "FinOps Foundation standard for normalising cost and "
                 "usage data across clouds. AWS, Azure, GCP support FOCUS "
                 "export. Enables true multi-cloud cost comparison."],
            ]
        )

        + H3("4.2  Cloud pricing models — the complexity map")
        + table(
            ["Pricing model", "AWS term", "Azure term", "When to use"],
            [
                ["<strong>On-demand</strong>",
                 "On-Demand Instances",
                 "Pay-As-You-Go",
                 "Short-lived workloads, dev/test, unpredictable demand. "
                 "Most expensive."],
                ["<strong>Commitment-based</strong>",
                 "Savings Plans (Compute / EC2) and Reserved Instances",
                 "Reserved VM Instances / Azure Savings Plans",
                 "Stable production workloads. 1-year or 3-year commitment. "
                 "30–72% savings vs. on-demand."],
                ["<strong>Spot / preemptible</strong>",
                 "Spot Instances",
                 "Spot VMs",
                 "Fault-tolerant batch, CI/CD, ML training. 60–90% savings "
                 "but can be terminated at any time."],
                ["<strong>Enterprise agreement</strong>",
                 "Enterprise Discount Program (EDP)",
                 "Enterprise Agreement (EA) / MACC",
                 "Bank-level commitment (USD 50M–500M+/year) for blanket "
                 "discount across all services."],
                ["<strong>Private pricing</strong>",
                 "Private Pricing (per-service negotiation)",
                 "Custom Agreements",
                 "Large customers negotiate per-service rates for their "
                 "highest-spend services (e.g., S3, RDS, EKS)."],
            ]
        )

        + H3("4.3  The FOCUS standard — multi-cloud cost normalisation")
        + p("The FOCUS (FinOps Open Cost and Usage Specification) is an "
            "open standard from the FinOps Foundation that normalises cost "
            "and usage data across all cloud providers into a common "
            "schema. Before FOCUS, comparing AWS and Azure costs was like "
            "comparing electricity bills in different currencies and units. "
            "FOCUS defines standard columns: BilledCost, EffectiveCost, "
            "ListUnitPrice, PricingQuantity, ServiceCategory, "
            "ResourceId, etc. AWS, Azure, and GCP all support FOCUS "
            "export as of 2024. For a multi-cloud bank, FOCUS is the "
            "foundation for accurate cross-cloud cost comparison.")

        + H3("4.4  Kubernetes cost allocation — the K8s-specific challenge")
        + p("Most banks run workloads on Kubernetes (EKS, AKS, GKE, "
            "on-prem OpenShift). Kubernetes shares compute resources "
            "across namespaces and pods, making cost allocation difficult. "
            "Solutions:")
        + ul([
            "<strong>Kubecost / OpenCost</strong> — monitor per-pod "
            "resource consumption and allocate node costs to namespaces, "
            "labels, and deployments. OpenCost is the CNCF open-source "
            "project; Kubecost is the commercial version with enterprise "
            "features.",
            "<strong>Resource requests and limits</strong> — Kubernetes "
            "allows pods to declare CPU/memory requests (guaranteed) and "
            "limits (maximum). Setting these correctly is the foundation "
            "of K8s cost management. Over-requesting wastes resources; "
            "under-requesting causes instability.",
            "<strong>Cluster right-sizing</strong> — Use Karpenter (AWS) "
            "or Cluster Autoscaler to automatically adjust node sizes "
            "and counts based on workload demand.",
        ])
    )
    return TopicSection(
        "4.  Types and variations — tools, pricing models, K8s costs",
        "intermediate", body)


# ------------------------------------------------------------------ sec 5

def _sec5() -> TopicSection:
    body = (
        H3("5.1  Unit economics — the metric that matters")
        + p("FinOps maturity is measured not by total spend but by unit "
            "cost efficiency. Examples of unit cost metrics in BFSI:")
        + table(
            ["Metric", "What it measures", "Benchmark range"],
            [
                ["<strong>Cost per transaction</strong>",
                 "Cloud cost / number of banking transactions",
                 "USD 0.001–0.01 per retail transaction; "
                 "USD 0.05–0.50 per wholesale/cross-border payment"],
                ["<strong>Cost per customer</strong>",
                 "Total cloud cost / number of active customers",
                 "USD 2–10/month per digital banking customer at scale"],
                ["<strong>Cost per trade</strong>",
                 "Cloud cost / number of executed trades",
                 "USD 0.01–0.10 for equities; USD 1–10 for complex "
                 "derivatives"],
                ["<strong>Cost per policy</strong>",
                 "Cloud cost / number of active insurance policies",
                 "USD 0.50–3.00/month per policy"],
                ["<strong>Cloud cost as % of revenue</strong>",
                 "Total cloud spend / total revenue",
                 "1–3% for digital-native fintechs; 3–8% for "
                 "traditional banks in migration"],
                ["<strong>Cloud cost / headcount</strong>",
                 "Total cloud spend / engineering headcount",
                 "USD 20,000–50,000/year per engineer"],
            ]
        )
        + p("The key: unit costs should decline over time even as total spend "
            "grows. If a bank's total cloud spend grows 30% but transaction "
            "volume grows 50%, the cost-per-transaction has improved. This "
            "is the story the CFO and the board want to hear.")

        + H3("5.2  Reserved Instance and Savings Plan portfolio management")
        + p("Managing a portfolio of RIs and Savings Plans is analogous to "
            "managing a bond portfolio: you have commitments at different "
            "tenors (1-year, 3-year), different coverage levels, different "
            "utilisation rates, and expiry dates. The FinOps team must:")
        + ul([
            "<strong>Track RI/SP utilisation.</strong> An RI that is only "
            "50% utilised is wasting 50% of its committed spend. Target: "
            ">95% utilisation.",
            "<strong>Plan for renewals.</strong> A 3-year RI expires — do "
            "we renew at the same size, right-size first, or convert to "
            "Savings Plans?",
            "<strong>Sell unused RIs.</strong> AWS allows selling unused "
            "RIs on the Reserved Instance Marketplace. Azure does not "
            "have a direct equivalent.",
            "<strong>Balance commitment vs. flexibility.</strong> Higher "
            "commitment = deeper discount but less flexibility. Banks "
            "migrating workloads frequently should lean toward Savings "
            "Plans (which are flexible across instance families) rather "
            "than RIs (locked to a specific type).",
            "<strong>Coverage target.</strong> Aim for 70–80% of stable "
            "production workloads covered by RIs/SPs. The remaining "
            "20–30% stays on-demand for flexibility.",
        ])

        + H3("5.3  Data transfer costs — the hidden monster")
        + p("Cloud providers charge for data egress (data leaving the cloud) "
            "and cross-region/cross-AZ data transfer. For BFSI, this is "
            "significant because:")
        + ul([
            "Multi-region architectures (active-active DR across "
            "Mumbai and Singapore, or US-East and US-West) generate "
            "continuous cross-region replication traffic.",
            "Data lakehouse architectures move large volumes of data "
            "between services (S3 → Redshift → SageMaker → S3 → "
            "downstream consumers).",
            "API-heavy architectures (microservices calling each other) "
            "generate cross-AZ traffic if services are spread across "
            "availability zones.",
            "Regulatory data exports — banks exporting data to "
            "regulators, auditors, or on-prem systems pay egress charges.",
        ])
        + p("Mitigation: use VPC endpoints (avoid NAT Gateway charges), "
            "compress data before transfer, co-locate services in the "
            "same AZ where possible (trading off availability), negotiate "
            "data-transfer discounts in the EDP, and use CloudFront or "
            "equivalent CDNs for customer-facing traffic.")

        + H3("5.4  FinOps and cloud exit — the regulatory dimension")
        + p("EU DORA, PRA SS2/21, and MAS outsourcing guidelines all "
            "require banks to have credible cloud exit strategies. FinOps "
            "intersects with this because:")
        + ul([
            "The bank must know the true cost of running on each cloud — "
            "including data egress costs for exit.",
            "Vendor lock-in (proprietary services like DynamoDB, Cosmos "
            "DB, BigQuery) increases exit costs. FinOps should track the "
            "percentage of spend on portable vs. proprietary services.",
            "Multi-cloud FinOps enables the bank to compare unit costs "
            "across providers and make informed placement decisions.",
        ])
    )
    return TopicSection(
        "5.  Advanced — unit economics, RI portfolio, data transfer, exit costs",
        "advanced", body)


# ------------------------------------------------------------------ sec 6

def _sec6() -> TopicSection:
    body = (
        p("Cloud cost governance is not just a CFO concern — it is "
          "increasingly a regulatory concern:")
        + table(
            ["Region", "Cloud cost and outsourcing governance requirements"],
            [
                ["<strong>European Union</strong>",
                 "<strong>EU DORA (Jan 2025)</strong> — requires financial "
                 "entities to manage concentration risk from ICT third-party "
                 "providers (cloud). Must have exit strategies and demonstrate "
                 "cost governance. <strong>ECB SSM</strong> scrutinises cloud "
                 "outsourcing arrangements including cost escalation clauses "
                 "and exit planning. <strong>EBA Outsourcing Guidelines</strong> "
                 "— require assessment of total cost of outsourcing including "
                 "transition-in, run, and exit costs."],
                ["<strong>United Kingdom</strong>",
                 "<strong>PRA SS2/21</strong> — outsourcing and third-party "
                 "risk management. Banks must assess concentration risk and "
                 "demonstrate cost-effective cloud usage. <strong>FCA PS21/3 "
                 "(Operational Resilience)</strong> — cost of resilience "
                 "(multi-region, DR) must be justified. <strong>UK CTP "
                 "(Critical Third Parties) regime</strong> under FSMA 2023 — "
                 "cloud providers may be designated CTPs; cost transparency "
                 "becomes a regulatory topic."],
                ["<strong>United States</strong>",
                 "<strong>OCC, Fed, FDIC Interagency Guidance on Third-Party "
                 "Risk Management (2023)</strong> — banks must have effective "
                 "contract management including cost monitoring. <strong>FFIEC "
                 "Cloud Computing (2023)</strong> — guidance on governance of "
                 "cloud services including cost. No specific FinOps mandate "
                 "but supervisory expectation of financial governance."],
                ["<strong>Singapore</strong>",
                 "<strong>MAS Outsourcing Guidelines</strong> — require banks "
                 "to manage outsourcing arrangements including cost "
                 "escalation, service-level management, and exit planning. "
                 "<strong>MAS TRM Guidelines</strong> — expect financial "
                 "controls over technology spend."],
                ["<strong>India</strong>",
                 "<strong>RBI Outsourcing of IT Services Master Direction "
                 "(Apr 2023)</strong> — banks must assess cost implications "
                 "of outsourcing, including cloud. <strong>RBI IT Governance "
                 "MD (Nov 2023)</strong> — requires governance over IT "
                 "spending. <strong>SEBI Cloud Framework (2023)</strong> — "
                 "regulated entities using cloud must demonstrate cost "
                 "governance and exit planning."],
            ]
        )
        + H3("6.1  The sustainability connection")
        + p("Cloud providers publish carbon-footprint data per customer: "
            "AWS (Customer Carbon Footprint Tool), Azure (Emissions Impact "
            "Dashboard), GCP (Carbon Footprint). FinOps and sustainability "
            "are converging: right-sizing reduces both cost and carbon; "
            "choosing a region with cleaner energy reduces carbon but may "
            "increase latency or conflict with data-residency rules. BFSI "
            "firms reporting under TCFD, EU CSRD, or UK SDR can use cloud "
            "carbon data in their Scope 3 emissions reporting.")
    )
    return TopicSection(
        "6.  BFSI / domain regulatory overlay", "advanced", body)


# ------------------------------------------------------------------ sec 7

def _sec7() -> TopicSection:
    body = (
        table(
            ["Decision", "Option A", "Option B", "Key trade-off"],
            [
                ["<strong>Showback vs. full chargeback</strong>",
                 "Show teams their costs (informational only)",
                 "Debit costs to team P&L (financial accountability)",
                 "Showback is easier to implement but does not drive "
                 "behavioural change. Chargeback drives accountability but "
                 "requires accurate cost allocation and can create friction. "
                 "Start with showback; move to chargeback within 12–18 months."],
                ["<strong>1-year vs. 3-year commitments</strong>",
                 "1-year RIs/Savings Plans (lower discount, more flexibility)",
                 "3-year RIs/Savings Plans (deeper discount, less flexibility)",
                 "3-year saves more but locks the bank in. If workloads are "
                 "migrating between clouds or being re-architected, 1-year "
                 "is safer. Blend: 60% 3-year for stable, 40% 1-year for "
                 "in-flux workloads."],
                ["<strong>Central FinOps team vs. embedded model</strong>",
                 "Central team owns all FinOps activities",
                 "Embedded FinOps engineers in each business unit",
                 "Central provides consistency and negotiating leverage. "
                 "Embedded provides domain context. Best practice: central "
                 "team for strategy, tools, and EDP negotiation; embedded "
                 "practitioners for daily optimisation."],
                ["<strong>Multi-cloud native tools vs. third-party platform</strong>",
                 "Use AWS Cost Explorer, Azure Cost Mgmt, GCP Billing "
                 "separately",
                 "Use Apptio Cloudability, CloudHealth, or Vantage for "
                 "unified view",
                 "Native tools are free and deeply integrated but siloed. "
                 "Third-party platforms provide multi-cloud normalisation "
                 "(FOCUS), unified dashboards, and cross-cloud optimisation — "
                 "essential for banks on 2+ clouds."],
                ["<strong>Spot instances for BFSI workloads</strong>",
                 "Use spot aggressively (batch, CI/CD, ML training, testing)",
                 "Avoid spot entirely (perceived risk in regulated industry)",
                 "Spot is safe and massively cost-effective for non-production "
                 "and fault-tolerant workloads. It is not suitable for "
                 "real-time banking transactions. The risk is interruption, "
                 "not data loss."],
                ["<strong>On-prem vs. cloud for cost-sensitive workloads</strong>",
                 "Repatriate stable, predictable workloads to on-prem/colo",
                 "Stay on cloud for all workloads",
                 "At very large scale (10,000+ cores of stable compute), "
                 "on-prem can be 30–40% cheaper than cloud on-demand. But "
                 "on-prem loses elasticity, managed services, and speed. "
                 "Hybrid approach: run stable workloads on reserved/spot "
                 "cloud or private cloud; keep burst capacity on public cloud."],
            ]
        )
    )
    return TopicSection(
        "7.  Trade-offs and decisions a leader owns", "intermediate", body)


# ------------------------------------------------------------------ sec 8

def _sec8() -> TopicSection:
    body = (
        example(
            "A tier-1 global bank saves USD 85M/year with FinOps",
            p("A global bank with USD 600M annual cloud spend across AWS "
              "and Azure established a FinOps Centre of Excellence (CoE) "
              "with 20 staff (10 engineers, 5 analysts, 3 cloud architects, "
              "2 managers). Year-1 results: (1) implemented mandatory "
              "tagging — tag compliance went from 35% to 94%, (2) "
              "right-sized 12,000 VMs — average utilisation went from "
              "15% to 45%, saving USD 35M/year, (3) purchased Savings "
              "Plans covering 75% of stable compute — saving USD 30M/year "
              "vs. on-demand, (4) implemented auto-stop for dev/test "
              "environments (running only during business hours) — saving "
              "USD 12M/year, (5) cleaned up 40TB of orphaned EBS snapshots "
              "and 8,000 unattached volumes — saving USD 8M/year. Total "
              "Year-1 savings: USD 85M (14% of total spend). The FinOps "
              "CoE cost USD 4M/year — a 21x ROI.")
        )
        + example(
            "An Indian bank's cloud chargeback transformation",
            p("A large Indian private-sector bank with ₹400 crore annual "
              "AWS spend (approximately USD 48M) had no cost accountability — "
              "the CTO's budget absorbed all cloud costs. The bank "
              "implemented chargeback in three phases: (1) Phase 1 (3 months): "
              "implemented AWS tagging via Terraform modules — every resource "
              "tagged with application, business-unit, and cost-centre. "
              "Used Apptio Cloudability for multi-account cost aggregation. "
              "(2) Phase 2 (3 months): showback — weekly cost reports to "
              "each business-unit head showing their cloud consumption. "
              "Immediate reaction: 'Why is my team spending ₹15 lakh/month "
              "on dev environments running 24/7?' Dev/test auto-stop "
              "implemented. (3) Phase 3 (6 months): full chargeback — "
              "cloud costs debited to each business unit's P&L monthly. "
              "Result: within one year, total cloud spend grew only 8% "
              "while transaction volume grew 35% — a 20% improvement in "
              "cost-per-transaction. The CTO's team now presents unit "
              "economics to the board quarterly.")
        )
        + example(
            "A European insurer's Kubernetes cost optimisation",
            p("A European P&C insurer running Guidewire Cloud on AWS EKS "
              "had Kubernetes costs growing 40% year-on-year despite stable "
              "policy volume. Investigation revealed: (1) pod resource "
              "requests were set at 2x actual usage (developers set high "
              "requests 'just in case'), wasting 50% of cluster capacity, "
              "(2) cluster auto-scaler was configured to add nodes but "
              "never remove them, (3) non-production clusters (4 environments "
              "× 3 squads) were running 24/7. Solutions: (1) deployed "
              "Kubecost to show per-namespace costs to each squad, "
              "(2) implemented Karpenter for intelligent node provisioning "
              "and removal, (3) right-sized pod requests based on 14-day "
              "P95 utilisation data, (4) implemented cluster schedules — "
              "non-prod clusters run 10 hours/day on weekdays. Result: "
              "Kubernetes costs reduced by 45% (EUR 1.8M/year saved) "
              "with zero performance impact.")
        )
        + example(
            "Multi-cloud EDP negotiation at a US bank",
            p("A US regional bank spending USD 80M on AWS and USD 40M on "
              "Azure renegotiated its Enterprise Discount Programs. Key "
              "negotiation levers: (1) combined the AWS EDP commitment "
              "with a 3-year term and achieved a 12% blanket discount "
              "(vs. 8% on the previous 1-year EDP), (2) negotiated custom "
              "pricing for top-5 services by spend (EC2, RDS, S3, EKS, "
              "Lambda) — additional 5–8% off list price, (3) on Azure, "
              "negotiated MACC (Microsoft Azure Consumption Commitment) "
              "with a 10% discount and credits for Azure OpenAI usage, "
              "(4) included data-egress caps in both EDPs — a critical "
              "win for exit-cost management. Total negotiated savings: "
              "USD 14M/year. The CFO co-signed both EDPs — FinOps "
              "bridged the CTO-CFO gap.")
        )
        + example(
            "Sustainability-linked FinOps at a Nordic bank",
            p("A Nordic bank integrated FinOps with its sustainability "
              "programme. Actions: (1) used AWS Customer Carbon Footprint "
              "Tool and Azure Emissions Impact Dashboard to measure cloud "
              "carbon, (2) right-sizing and idle cleanup (FinOps baseline) "
              "reduced compute hours by 30%, directly reducing Scope 3 "
              "carbon by an estimated 25%, (3) migrated batch workloads "
              "from eu-west-1 (Ireland, predominantly renewable) to "
              "eu-north-1 (Stockholm, 100% renewable) — a latency "
              "trade-off accepted for non-real-time batch, (4) reported "
              "cloud carbon reduction in the bank's CSRD sustainability "
              "report. The bank set a target: cloud cost per transaction "
              "and cloud carbon per transaction must both decline "
              "year-on-year.")
        )
    )
    return TopicSection(
        "8.  Worked examples — numbers and decisions", "intermediate", body)


# ------------------------------------------------------------------ sec 9

def _sec9() -> TopicSection:
    body = (
        H3("9.1  Questions a leader asks in any review")
        + ol([
            "What is our total cloud spend by provider, by business unit, "
            "and by application — and what percentage is tagged?",
            "What are our unit cost metrics (cost per transaction, cost per "
            "customer, cost per trade) — and are they improving?",
            "What percentage of compute is covered by RIs/Savings Plans, "
            "and what is the utilisation rate of those commitments?",
            "What is our right-sizing opportunity — how many VMs/containers "
            "are running below 20% CPU utilisation?",
            "Are dev/test environments running 24/7 or only during "
            "business hours?",
            "What is our data-transfer cost, and are we aware of the egress "
            "cost if we need to exit the cloud provider?",
            "Do we have a FinOps team, and do they report to CTO, CFO, "
            "or both?",
            "Are we on showback or chargeback — and do business-unit heads "
            "see their cloud costs on their P&L?",
            "What is our EDP discount level, and when does the current "
            "agreement expire?",
            "How does our cloud cost-to-revenue ratio compare to peers?",
            "What is our cloud carbon footprint, and is it tracked in "
            "our sustainability reporting?",
            "Are we using FOCUS to normalise costs across clouds, or are "
            "we comparing costs in provider-specific formats?",
        ])
        + H3("9.2  Red flags")
        + red_flag(ul([
            "'We don't know our cloud spend by application.' — This is "
            "the most basic FinOps capability. Without cost allocation, "
            "there is no accountability, no optimisation, and no unit "
            "economics.",
            "'Our tag compliance is below 50%.' — Tagging is the "
            "foundation of FinOps. Below 80%, cost allocation is "
            "unreliable. Below 50%, FinOps is not functional.",
            "'We're 100% on-demand.' — For stable production workloads, "
            "on-demand pricing is 30–72% more expensive than committed "
            "pricing. A bank running 100% on-demand is literally burning "
            "money.",
            "'Our dev/test environments run 24/7.' — If developers work "
            "10 hours/day on weekdays, that is 50 hours out of 168 — "
            "meaning 70% of dev/test compute is idle. Auto-stop "
            "policies are table stakes.",
            "'We negotiated our EDP two years ago and haven't renegotiated.' "
            "— Cloud pricing drops 5–10% annually. A stale EDP means "
            "the bank is paying above-market rates. Renegotiate annually "
            "or at least at each renewal.",
            "'FinOps reports to the CTO only.' — FinOps must bridge "
            "engineering and finance. If the CFO has no visibility into "
            "cloud costs and unit economics, the organisation is not "
            "doing FinOps — it is doing cost monitoring.",
            "'We'll optimise later once we've migrated.' — Cloud waste "
            "compounds monthly. A bank that migrates first and optimises "
            "later will waste 30–40% of its cloud spend during migration "
            "(typically 2–4 years). Optimise as you migrate.",
            "'Spot instances are too risky for a bank.' — Spot is risky "
            "for real-time transaction processing. It is perfectly safe "
            "and massively cost-effective for batch processing, CI/CD, "
            "load testing, ML training, and data analytics — which can "
            "constitute 30–50% of a bank's compute.",
            "'Our cloud provider manages our costs for us.' — Cloud "
            "providers' incentive is to increase your spend. They offer "
            "excellent tools (Compute Optimizer, Advisor, Recommender) "
            "but the bank must own the strategy, targets, and "
            "accountability. No vendor manages your costs for you.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("FinOps", "Financial Operations for cloud — the practice of "
             "bringing financial accountability to cloud spending through "
             "collaboration between engineering, finance, and business."),
            ("CIR", "Cost-to-Income Ratio — a key banking efficiency metric: "
             "operating costs divided by operating income. Lower is better."),
            ("RI", "Reserved Instance — a cloud commitment to use a specific "
             "instance type for 1 or 3 years in exchange for a discounted rate."),
            ("Savings Plan", "AWS pricing model offering discounted rates in "
             "exchange for a commitment to a consistent amount of usage "
             "(measured in USD/hour), flexible across instance families."),
            ("EDP", "Enterprise Discount Program — a bank-level commitment "
             "to minimum annual cloud spend in exchange for a blanket "
             "discount across all services."),
            ("MACC", "Microsoft Azure Consumption Commitment — Azure's "
             "equivalent of EDP."),
            ("Showback", "Showing teams their cloud costs without financially "
             "debiting their budget — informational accountability."),
            ("Chargeback", "Debiting cloud costs to the consuming team's P&L — "
             "financial accountability."),
            ("Right-sizing", "Adjusting cloud resource sizes (CPU, memory, "
             "storage) to match actual utilisation, reducing waste."),
            ("Spot instance", "Cloud compute using spare capacity at 60–90% "
             "discount, with the risk of interruption."),
            ("FOCUS", "FinOps Open Cost and Usage Specification — an open "
             "standard for normalising cost and usage data across cloud "
             "providers."),
            ("Unit economics", "Cost per unit of business value — cost per "
             "transaction, cost per customer, cost per trade."),
            ("Tag", "A key-value metadata label applied to cloud resources "
             "to enable cost allocation and governance."),
            ("Data egress", "Data leaving a cloud provider or region — "
             "typically charged per GB."),
            ("Kubecost / OpenCost", "Kubernetes-native cost allocation tools "
             "that attribute cluster costs to namespaces and pods."),
            ("TCO", "Total Cost of Ownership — the full cost of operating "
             "a system including compute, storage, licensing, staffing, "
             "and exit costs."),
        ])
    )
    return TopicSection(
        "9.  Questions, red flags, and glossary", "basic", body)
