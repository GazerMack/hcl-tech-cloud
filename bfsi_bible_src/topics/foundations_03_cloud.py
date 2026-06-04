"""Foundations · 03 — Cloud, on-prem, and hybrid for a regulated bank."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="I.3",
        slug="03-cloud-and-infra",
        title="Cloud, on-prem, and hybrid — where bank software actually runs",
        one_liner=("Every BFSI conversation today is shadowed by 'the cloud'. The reality is "
                   "that no large bank is fully on cloud and none is fully on-prem. Each runs a "
                   "specific hybrid that is shaped less by technology fashion and more by "
                   "regulators, latency budgets, vendor contracts and 30 years of legacy. This "
                   "topic gives you the language and the math to follow — and influence — those "
                   "decisions."),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("‘Cloud’ has come to mean too many things at once. Before we discuss strategies "
              "we need a precise vocabulary. The word covers four delivery models, three "
              "service models, and three deployment models. They combine to make most of the "
              "confusion in this space.")
        )
        + H3("0.1  IT-side anchor — Netflix vs your DVD shelf")
        + it_anchor(
            p("Imagine watching a film. <strong>Owning the DVD</strong> is on-prem: you bought "
              "the disc, you bought the player, you paid up front, the disc sits on your shelf "
              "even when you’re not watching, and if it scratches you replace it yourself. "
              "<strong>Renting from the video store</strong> is colocation: the disc is yours, "
              "but the shelf belongs to someone else. <strong>Netflix</strong> is the public "
              "cloud: you don’t own the disc, you don’t own the player, you pay only for what "
              "you watch, and the service silently scales up when more people want it. Most "
              "homes today have a hybrid: some DVDs on the shelf, plus a Netflix subscription. "
              "Banks are exactly the same.")
        )
        + H3("0.2  BFSI-side anchor — what cloud already does for you as a customer")
        + bfsi_anchor(
            p("When you tap to pay on UPI at 9 pm on Diwali night, the volume on NPCI is "
              "<em>15× the morning average</em>. There is no way NPCI keeps that much idle "
              "hardware year-round; they elastically scale on cloud (and on-prem capacity at "
              "their own data centre) for those peaks. When SBI YONO went down on a salary day "
              "in 2022, the public commentary was about ‘cloud capacity’; the reality was a "
              "specific application bottleneck. Every time you experience an instant cross-"
              "border transfer via Wise, you are using a fully cloud-native bank licence in "
              "the UK and Singapore.")
        )
        + H3("0.3  The three service models in 30 seconds")
        + ul([
            "<strong>IaaS (Infrastructure as a Service)</strong> — you rent virtual machines, "
            "disks and networks; you install the OS, runtime and app. Examples: AWS EC2, Azure "
            "VMs, GCP Compute Engine.",
            "<strong>PaaS (Platform as a Service)</strong> — you rent a runtime; you bring code. "
            "Examples: AWS Elastic Beanstalk, Azure App Service, Google App Engine, Heroku.",
            "<strong>SaaS (Software as a Service)</strong> — you rent finished software. "
            "Examples: Salesforce, Microsoft 365, Workday, Mambu, Thought Machine, Snowflake.",
        ])
        + H3("0.4  The three deployment models")
        + ul([
            "<strong>Public cloud</strong> — multi-tenant infrastructure run by a hyperscaler "
            "(AWS, Azure, GCP, OCI, IBM Cloud, Alibaba).",
            "<strong>Private cloud</strong> — single-tenant cloud on hardware you own or "
            "lease. VMware (Broadcom) Cloud Foundation, Red Hat OpenShift, Nutanix.",
            "<strong>Hybrid cloud</strong> — combination of the two with consistent management.",
        ])
        + H3("0.5  And four delivery flavours regulators care about")
        + ul([
            "<strong>Sovereign cloud</strong> — operated and audited within a single country, "
            "often with citizen-only operators. AWS European Sovereign Cloud (Brandenburg, "
            "online 2025), Microsoft Cloud for Sovereignty, Google Sovereign Cloud, OCI "
            "Sovereign Cloud, Bharat Cloud (proposed) for India.",
            "<strong>Government / dedicated regions</strong> — AWS GovCloud, Azure Government, "
            "Google Assured Workloads.",
            "<strong>Industry cloud</strong> — vertical-specific clouds with bank-friendly "
            "controls; e.g. Microsoft Cloud for Financial Services, AWS for Financial Services.",
            "<strong>Local zones / outposts / Anthos / Azure Stack</strong> — hyperscaler "
            "hardware running inside the bank’s own data centre with cloud APIs.",
        ])
    )
    return TopicSection("0.  Primer — vocabulary you must have before any cloud meeting",
                        "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Reframe ‘cloud vs on-prem’ as four real questions that are debated in every BFSI "
          "design review:")
        + ol([
            "<strong>Time-to-market</strong> — how quickly can a new product reach customers? "
            "Cloud usually wins by 6–18 months because procurement and capacity-planning "
            "disappear.",
            "<strong>Total Cost of Ownership (TCO)</strong> — over five years, which model is "
            "cheaper at <em>your</em> utilisation pattern? Cloud wins for spiky workloads and "
            "for greenfield; on-prem can still win for steady-state, predictable, very large "
            "workloads (especially mainframe-bound ones at JPM, Wells, Citi).",
            "<strong>Resilience</strong> — under what failure modes do we keep customers "
            "served? Multi-region cloud is now well ahead of most single-data-centre on-prem "
            "designs but introduces concentration risk that DORA and RBI watch closely.",
            "<strong>Regulatory comfort</strong> — can the regulator audit and contain risk? "
            "This is the question that has shaped the entire BFSI cloud journey since 2018.",
        ])
    )
    return TopicSection("1.  Why this is not a fashion debate — first principles",
                        "basic", body)


def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  subgraph "On-prem and private cloud"\n'
            '    A["Mainframe core<br/>IBM Z, DB2, COBOL"]\n'
            '    B["Tier-1 cores<br/>Finacle, Flexcube, T24"]\n'
            '    C["VMware / OpenShift<br/>internal apps"]\n'
            '  end\n'
            '  subgraph "Hybrid bridge"\n'
            '    D["Direct Connect / ExpressRoute<br/>private 10-100 Gbps"]\n'
            '    E["Identity bridge<br/>Entra ID / Okta"]\n'
            '  end\n'
            '  subgraph "Public cloud"\n'
            '    F["Channel apps<br/>mobile, web, partner APIs"]\n'
            '    G["Data lakehouse<br/>Snowflake, Databricks"]\n'
            '    H["AI / ML platform<br/>Bedrock, Vertex, Azure OpenAI"]\n'
            '    I["New product platforms<br/>Mambu, Thought Machine"]\n'
            '  end\n'
            '  A --> D\n'
            '  B --> D\n'
            '  C --> D\n'
            '  D --> F\n'
            '  D --> G\n'
            '  D --> H\n'
            '  D --> I\n'
            '  E -. SSO .-> F\n'
            '  E -. SSO .-> G',
            "Typical hybrid posture at a global tier-1 bank in 2025.")
    )
    return TopicSection("2.  The picture every CIO has on a wall", "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  Public cloud — the four-and-a-half hyperscalers")
        + table(
            ["Cloud", "Strengths in BFSI", "Where you’ll see it"],
            [
                ["<strong>AWS</strong>",
                 "Largest market share, broadest service breadth, mature financial-services "
                 "controls (FSI competency, AWS for FSI), strong India regions (Mumbai, "
                 "Hyderabad), upcoming European Sovereign Cloud.",
                 "Capital One (all-in on AWS since 2020), Goldman Marquee, NAB, Nubank, ICICI "
                 "Lombard, parts of HDFC, Bajaj Finserv."],
                ["<strong>Microsoft Azure</strong>",
                 "Enterprise-friendly licensing, deep ties with Microsoft 365 / Entra ID, "
                 "strong sovereign offerings, leading position with regulators in Europe.",
                 "Standard Chartered ‘cloud-first’ programme uses Azure heavily, UBS, Westpac, "
                 "Australia’s CBA, HCLTech engagements at Lloyds and NatWest."],
                ["<strong>Google Cloud (GCP)</strong>",
                 "Data and AI strengths (BigQuery, Vertex), rising fast among capital-markets "
                 "and analytics workloads.",
                 "Deutsche Bank ten-year partnership announced 2020, HSBC analytics, PayPal, "
                 "Wise."],
                ["<strong>Oracle Cloud (OCI)</strong>",
                 "Best place to run Oracle Database (which most banks have lots of), strong "
                 "in India (Mumbai + Hyderabad regions, sovereign cloud).",
                 "TCS BaNCS-on-OCI offerings, parts of HDFC, Citi runs significant Oracle "
                 "Exadata workloads on OCI."],
                ["<strong>IBM Cloud (½)</strong>",
                 "Mainframe affinity, IBM Cloud for Financial Services with built-in "
                 "regulatory controls, niche but credible.",
                 "BNP Paribas, MUFG, parts of Wells Fargo."],
            ]
        )
        + H3("3.2  Private cloud and on-prem in 2025")
        + p("Despite a decade of ‘cloud first’, most large banks still run 40–70% of their "
            "workloads on-prem or in private cloud. Why?")
        + ul([
            "<strong>Mainframe</strong>. JPM, BoA, Wells, Citi, BNY Mellon, Lloyds, BoB, "
            "SBI all still have IBM Z mainframes running tens of thousands of transactions per "
            "second on COBOL applications written between 1985 and 2005. Re-platforming a "
            "core takes 5–10 years and costs hundreds of millions of dollars; risk-adjusted "
            "return is often unattractive, so banks modernise <em>around</em> the mainframe.",
            "<strong>VMware / OpenShift estates</strong>. Decades of internal apps that work, "
            "are amortised, and don’t justify a re-platform. Broadcom’s 2024 changes to VMware "
            "licensing have, ironically, pushed many of these onto OpenShift or to cloud "
            "faster than the original plan.",
            "<strong>Latency-bound workloads</strong>. Cards switches at major banks need "
            "single-digit milliseconds end-to-end and run close to the rail switch.",
            "<strong>Sovereignty</strong>. RBI Storage of Payment Data (April 2018) requires "
            "the entire payment-data lifecycle to be stored in India; some banks meet this "
            "with cloud regions in India, others with on-prem.",
        ])
    )
    return TopicSection("3.  Where bank workloads actually run today",
                        "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  India")
        + p("RBI Storage of Payment System Data (April 2018) requires the entire payment data "
            "lifecycle to be stored in India. Both AWS (Mumbai, Hyderabad) and Azure (Pune, "
            "Mumbai, Chennai), GCP (Mumbai, Delhi), OCI (Mumbai, Hyderabad) operate in-country "
            "regions, but the bank remains accountable for data localisation. RBI Outsourcing "
            "of IT Services Master Direction (April 2023) sets explicit rules for cloud: board "
            "approval, exit strategy, concentration risk, right to audit.")
        + H3("4.2  United States")
        + p("No general data localisation. OCC Bulletin 2023-17 and Fed SR 23-4 set third-"
            "party risk management expectations. NYDFS Part 500 sets cybersecurity baselines "
            "for state-licensed financials. Capital One has been on AWS since 2020 — the most-"
            "cited reference architecture; JPM Athena and Onyx are major cloud programmes.")
        + H3("4.3  United Kingdom")
        + p("PRA SS2/21 (outsourcing and third-party risk) and BoE-FCA-PRA Operational "
            "Resilience policy (in effect Mar 2022, fully embedded Mar 2025) require named "
            "‘important business services’ with quantified impact tolerances. The Critical "
            "Third Parties (CTP) regime under FSMA 2023 brings the largest hyperscalers under "
            "direct UK regulator oversight from 2024.")
        + H3("4.4  Eurozone — DORA is now law")
        + p("<strong>EU DORA (Digital Operational Resilience Act)</strong> applies from "
            "<strong>17 January 2025</strong>. It sets ICT risk, incident reporting, threat-led "
            "penetration testing (TLPT, similar to TIBER-EU), and oversight of ‘critical ICT "
            "third-party providers’. The European Supervisory Authorities (EBA, ESMA, EIOPA) "
            "designate hyperscalers as critical third parties. EU AI Act in force from Aug "
            "2024 with banking-relevant clauses applying through Aug 2026; EU Cyber Resilience "
            "Act (2024) adds product-side rules including SBOM.")
        + H3("4.5  Singapore")
        + p("MAS Outsourcing Guidelines, MAS Notice 658 (BCM), and MAS TRM Guidelines. The MAS "
            "‘TRM Annex on Cloud’ requires a robust risk assessment, exit plan, and recovery "
            "objectives. Singapore is one of the most cloud-positive regulators globally — "
            "Wise, Revolut, GXS Bank, Trust Bank all run cloud-first.")
        + H3("4.6  Cross-cutting — sanctions and US export controls")
        + p("US export-control rules constrain which cloud regions can be used for some "
            "workloads. Russian sanctions since 2022 forced many banks to re-architect EU "
            "workloads to avoid US-controlled regions. China’s Cybersecurity Law and Personal "
            "Information Protection Law (PIPL) require local clouds (Alibaba, Tencent, AWS / "
            "Azure China through local partners).")
    )
    return TopicSection("4.  Region-by-region regulatory state — current as of 2025",
                        "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  Landing zone — the foundation you cannot skip")
        + p("Before any workload lands, a bank builds a <em>landing zone</em>: a hardened, "
            "regulator-aligned baseline of accounts (AWS), subscriptions (Azure), or projects "
            "(GCP), with networking, IAM, logging, encryption, guardrails, and break-glass "
            "access codified as Infrastructure-as-Code (IaC). Reference frameworks: AWS "
            "Control Tower / FSI Reference Architecture, Azure Cloud Adoption Framework + "
            "Sovereignty Policy Initiatives, GCP Cloud Foundation Toolkit, OCI Landing Zone.")
        + H3("5.2  Networking patterns")
        + ul([
            "<strong>Hub-and-spoke</strong> with a transit gateway (AWS Transit Gateway, Azure "
            "Virtual WAN, GCP Network Connectivity Center). The default for tier-1 banks.",
            "<strong>Private connectivity</strong> back to the data centre via AWS Direct "
            "Connect, Azure ExpressRoute, GCP Interconnect, OCI FastConnect — typically dual "
            "10–100 Gbps circuits across two providers for resilience.",
            "<strong>Egress controls</strong> — every flow out of a VPC / VNet is policy-"
            "controlled, logged, and DLP-scanned; PrivateLink / Private Endpoints for SaaS "
            "access.",
        ])
        + H3("5.3  Identity and access")
        + p("Every cloud account uses single sign-on against the corporate IdP (Microsoft Entra "
            "ID being the most common in BFSI, with Okta and Ping in second tier). Workforce "
            "identity goes through the IdP; workload identity uses cloud-native (AWS IAM Roles "
            "Anywhere, Azure Managed Identity, GCP Workload Identity Federation, SPIFFE/SPIRE "
            "in vendor-neutral environments). PAM (Privileged Access Management) via CyberArk "
            "or BeyondTrust; just-in-time elevation is the modern norm.")
        + H3("5.4  Encryption keys — who holds them")
        + ul([
            "<strong>BYOK (Bring Your Own Key)</strong> — bank generates the master key in "
            "its own HSM and imports the key material to the cloud KMS.",
            "<strong>HYOK (Hold Your Own Key) / EKM (External Key Manager)</strong> — keys "
            "never leave the bank’s HSM; cloud calls back for every encrypt / decrypt. Azure "
            "Key Vault Managed HSM, AWS KMS XKS (External Key Store), Google Cloud EKM.",
            "<strong>Confidential computing</strong> — data is encrypted even while in CPU "
            "memory. AWS Nitro Enclaves, Azure Confidential VMs, GCP Confidential VMs (AMD "
            "SEV-SNP, Intel TDX). Increasingly used for tokenisation, key custody, and AI "
            "inference on sensitive data.",
        ])
        + H3("5.5  Resilience patterns and the multi-region question")
        + p("DORA, RBI, MAS, FCA all converge on the same expectation: a tier-1 critical "
            "service must survive the loss of a region. Practical patterns:")
        + ul([
            "<strong>Active-active across two regions</strong> with eventual consistency "
            "between cells. Used by Capital One, Wise, Revolut.",
            "<strong>Active-warm</strong> — primary region serves traffic; secondary region is "
            "kept warm with continuous replication, fail-over in minutes. Most large incumbents.",
            "<strong>Pilot light</strong> — minimal footprint in secondary; spin up on disaster. "
            "Cheaper but RTO is in hours; only acceptable for non-critical workloads.",
            "<strong>Multi-cloud DR</strong> — primary on cloud A, DR on cloud B. Increasingly "
            "demanded by EU regulators to address concentration risk.",
        ])
        + H3("5.6  FinOps — controlling the bill")
        + p("Cloud spend at a tier-1 bank is now USD 200M–1.5B per year. FinOps (the "
            "discipline of cloud financial management; FinOps Foundation framework) is now a "
            "standing function: tag every resource by cost centre, allocate, forecast, "
            "automate rightsizing, and use savings plans / reservations. Major banks claim "
            "20–35% savings within the first 18 months of mature FinOps.")
    )
    return TopicSection("5.  Advanced — the patterns every cloud-mature bank uses",
                        "advanced", body)


def _sec6() -> TopicSection:
    return TopicSection(
        "6.  Decision matrix — when does each posture win?", "intermediate",
        table(
            ["Workload", "Best home in 2025", "Why"],
            [
                ["Mobile / web channel apps", "Public cloud",
                 "Spiky traffic, fast iteration, mature managed services."],
                ["Data lakehouse, BI, regulatory reporting", "Public cloud",
                 "Snowflake / Databricks / BigQuery economics dominate; Iceberg / Delta keep "
                 "you portable."],
                ["AI / ML platform, especially LLMs", "Public cloud",
                 "GPUs are scarce; only hyperscalers and a few specialists have them at scale."],
                ["Tier-1 core banking ledger (settled bank, large)",
                 "On-prem or private cloud, evolving",
                 "Mainframes still cheaper per transaction at very high TPS; modernise around "
                 "rather than replace, unless launching greenfield."],
                ["Tier-1 core (digital greenfield)", "Public cloud",
                 "Mambu, Thought Machine, 10x, FIS Modern Banking Platform are cloud-native; "
                 "no legacy to drag along."],
                ["Cards switch", "On-prem or co-located",
                 "Latency-bound; rail co-location wins."],
                ["Sanctions / AML screening", "Either",
                 "Vendor choice drives this more than infra; many SaaS options now."],
                ["High-frequency trading", "On-prem, exchange-co-located",
                 "Microseconds matter; cloud round-trip is too high."],
                ["Capital-markets risk batch (overnight)", "Public cloud",
                 "Massive elastic scale for 4–6 hours per day; idle the rest."],
                ["Confidential workloads (key custody, tokenisation)", "Confidential computing",
                 "On-prem HSM + cloud Nitro Enclaves / Confidential VMs / Azure Confidential."],
            ]
        )
    )


def _sec7() -> TopicSection:
    body = (
        example("Standard Chartered’s cloud-first programme",
            p("Public commitments: aim to run more than two-thirds of applications on cloud by "
              "2025, primarily Azure with strategic AWS use. Touched every layer: landing zone "
              "and FinOps on day one, IAM unified through Entra ID, ‘aXess’ developer platform "
              "for self-service, identity-aware perimeter replacing parts of the legacy network. "
              "HCLTech is among the partners delivering parts of the migration.")
        )
        + example("Capital One — the AWS reference",
            p("First major US bank to declare itself all-in on public cloud (AWS) and to close "
              "its last data centres (2020). Built much of its own tooling (Cardinal, Cloud "
              "Custodian — open-sourced, CMDB) and contributes back. Still cited as the most "
              "ambitious BFSI cloud migration; also cited (the 2019 data breach) as a "
              "cautionary tale about misconfiguration. The breach was an SSRF "
              "(Server-Side Request Forgery) bug + over-permissioned IAM role — both fixable "
              "L5/L6 issues, not an indictment of cloud per se.")
        )
        + example("DBS, GXS, and Trust — Singapore’s cloud-native ladder",
            p("DBS migrated 99% of compute to private cloud running on hardware they operate "
              "with public-cloud-style APIs; new digital banks GXS (DBS / Singtel) and Trust "
              "(Standard Chartered / NTUC) launched fully on AWS / GCP cloud cores (Mambu, "
              "Thought Machine) under MAS digital-bank licences. Useful contrast: DBS shows "
              "the incumbent path; GXS / Trust show the greenfield path.")
        )
        + example("Why a global bank cannot just ‘lift and shift’ a core banking system to cloud",
            ol([
                "Latency from cloud to existing on-prem cards switches and SWIFT gateways "
                "breaks SLAs.",
                "Mainframe-resident ledgers don’t run on x86; emulation adds risk and cost.",
                "Regulator-by-regulator approvals must be sequenced (RBI, MAS, FCA, OCC, ECB).",
                "Data localisation rules force per-country regions, multiplying complexity.",
                "Reconciliation and recovery procedures, decades-tuned, must be re-validated.",
                "The cost of <em>not</em> changing is rarely high enough to justify a 7-figure "
                "five-year migration; the practical answer is ‘strangler fig’ around the core.",
            ])
        )
    )
    return TopicSection("7.  Worked examples — three real BFSI cloud journeys",
                        "intermediate", body)


def _sec8() -> TopicSection:
    return TopicSection("8.  Questions a leader asks in any cloud design review", "basic",
        ol([
            "What is the landing zone, who owns it, and is every guardrail codified as IaC?",
            "Where do encryption keys live and who can get to plaintext under what process?",
            "What is the Recovery Time Objective (RTO) and Recovery Point Objective (RPO) of "
            "this service, and have we tested them with a real region failure in the last 12 "
            "months?",
            "Are we using managed services that lock us in, and is that acceptable per our "
            "DORA / RBI / MAS exit plan?",
            "What does our concentration risk look like across providers, and what is the "
            "credible plan if we needed to exit our largest cloud?",
            "Do we have a per-application FinOps owner, and what is the unit cost (per "
            "transaction, per customer) trend over the last six months?",
            "Is identity unified between cloud, SaaS, and on-prem, and is privileged access "
            "ephemeral and session-recorded?",
            "Have we run a Threat-Led Penetration Test (TLPT / TIBER-EU) on this service in "
            "the last two years?",
            "If a third-party SaaS vendor terminated tomorrow, how many days to recover with "
            "what data loss?",
        ]))


def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘Cloud is automatically more secure than on-prem.’ — It can be, with discipline. "
            "Capital One 2019 was a cloud breach; Equifax 2017 was on-prem. Architecture and "
            "operations decide outcomes, not delivery model.",
            "‘We don’t need an exit plan, the regulator never asks.’ — RBI, DORA, MAS, FCA all "
            "now ask. Have one written and tested.",
            "‘We’re cloud-native because we run on Kubernetes.’ — As noted in I.2: K8s is L5 "
            "only. Cloud-native means rethinking data and apps too.",
            "‘Multi-cloud means twice the resilience.’ — Almost the opposite if you don’t have "
            "twice the operational maturity. Many multi-cloud postures are the worst of both.",
            "‘Lift-and-shift will save us 30%.’ — Lift-and-shift typically saves 0–10% before "
            "FinOps and is sometimes <em>more</em> expensive than on-prem. Real savings come "
            "from re-architecting; if the business case rests on lift-and-shift alone, push "
            "back.",
            "‘Sovereign cloud means data never leaves the country.’ — Not always; the control "
            "plane and the support engineers may still be elsewhere. Read the contract.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("IaaS / PaaS / SaaS", "Infrastructure-as-a-Service / Platform-as-a-Service / "
             "Software-as-a-Service — the three classic service models."),
            ("Hyperscaler", "Cloud provider operating tens of thousands of servers per region; "
             "AWS, Azure, GCP, OCI, Alibaba, IBM."),
            ("Sovereign cloud", "Cloud operated within a single country with citizen-only "
             "access; growing in EU, India, France, Germany."),
            ("Landing zone", "The codified baseline of accounts, networking, IAM, logging, "
             "encryption and guardrails into which workloads land."),
            ("BYOK / HYOK / EKM", "Bring Your Own Key / Hold Your Own Key / External Key "
             "Manager — increasing levels of customer control over encryption keys."),
            ("Confidential computing", "Hardware-enforced data protection while in use "
             "(AMD SEV-SNP, Intel TDX, AWS Nitro Enclaves)."),
            ("DORA", "Digital Operational Resilience Act — EU regulation in force 17 Jan 2025; "
             "the most consequential cloud-relevant law of the decade."),
            ("TLPT / TIBER-EU", "Threat-Led Penetration Test / European framework for it; "
             "DORA mandates this for the most critical services."),
            ("CTP", "Critical Third Parties regime — UK FSMA 2023; brings hyperscalers under "
             "direct UK regulator oversight."),
            ("FinOps", "Discipline of managing cloud financial operations; FinOps Foundation "
             "publishes the framework."),
            ("RTO / RPO", "Recovery Time / Recovery Point Objective — how fast you must be "
             "back up and how much data loss is tolerable."),
            ("Concentration risk", "Risk arising from too much exposure to a single provider; "
             "DORA, RBI Outsourcing MD and PRA all monitor this."),
            ("Strangler fig", "Migration pattern where new services gradually replace pieces "
             "of a legacy monolith; named after the strangler fig tree, popularised by Martin "
             "Fowler."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
