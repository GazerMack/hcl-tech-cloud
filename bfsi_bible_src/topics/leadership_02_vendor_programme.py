"""Leadership Lenses · 02 — Vendor management and large-programme delivery."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="VII.2",
        slug="02-vendor-management-and-programme-delivery",
        title="Vendor management and large-programme delivery — RFP, MSA, SoW, governance, rituals",
        one_liner=(
            "Most BFSI technology spend goes through vendors — "
            "hyperscalers, software vendors, system integrators, "
            "advisory firms, niche specialists. Most large programmes "
            "are delivered by a mix of internal teams and external "
            "partners under multi-year contracts. The skill that "
            "separates senior techno-functional leaders is not "
            "writing code or even drafting architecture — it is "
            "running these vendor and programme relationships well. "
            "This topic gives you fluent vocabulary in the contract "
            "stack (MSA, SoW, DPA, BAA, SLA), the procurement "
            "rituals (RFI, RFP, RFQ, demo, PoC, SOW), the delivery "
            "rituals (steerco, working group, RAID, scrum-of-scrums), "
            "and the regulator overlays (DORA CTP, RBI Outsourcing "
            "of IT Services, PRA SS2/21, MAS Outsourcing, NYDFS) "
            "that shape every contract."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("A senior BFSI technology leader spends a quarter to "
              "half of their time on vendor relationships and "
              "programme delivery. The remaining time spent on "
              "engineering, architecture, hiring and strategy "
              "depends on these going well. Lose a programme to "
              "drift; let a vendor relationship sour; miss a "
              "regulator-mandated deadline — and the rest of the "
              "agenda stops mattering.")
        )
        + H3("0.1  IT-side anchor — building a house with a contractor")
        + it_anchor(
            p("If you’ve ever built or renovated a house, you have "
              "done vendor management. You wrote a brief (RFP), "
              "got quotes (RFP responses), picked a builder (vendor "
              "selection), signed a contract (MSA + Statement of "
              "Work), agreed milestones (delivery plan), held weekly "
              "site visits (steerco), kept a list of issues (RAID "
              "log), paid against milestones (invoicing), and "
              "argued about variations (change requests). A "
              "USD 100M IT programme is the same shape, with more "
              "lawyers and a regulator.")
        )
        + H3("0.2  BFSI-side anchor — what makes BFSI vendor management distinct")
        + bfsi_anchor(
            p("Compared with non-regulated industries, BFSI vendor "
              "management has four extra constraints. <strong>"
              "Outsourcing rules</strong> (RBI, PRA, MAS, EU EBA, "
              "DORA) require board-approved policies, due "
              "diligence, exit plans, audit rights. <strong>Data "
              "localisation</strong> (RBI, China PIPL, Russia, "
              "increasingly Indonesia, Vietnam, Saudi) constrains "
              "where the vendor can host. <strong>Concentration "
              "risk</strong> on a small number of cloud and "
              "software vendors is now an explicit regulator "
              "topic. <strong>Operational resilience</strong> "
              "expects you to test what happens if a vendor goes "
              "down. None of these are optional, and all of them "
              "shape the contract.")
        )
        + H3("0.3  The five vendor categories you must recognise")
        + ul([
            "<strong>Hyperscalers and infrastructure</strong> — "
            "AWS, Azure, GCP, OCI, IBM Cloud, Alibaba; sometimes "
            "Equinix, Digital Realty, NTT for colocation.",
            "<strong>Software product vendors</strong> — Temenos, "
            "Finacle, FIS, Fiserv, Murex, Calypso (Adenza), "
            "Guidewire, Duck Creek, Sapiens, ICE, Black Knight, "
            "Bloomberg, Aladdin, Snowflake, Databricks, Salesforce, "
            "Workday, ServiceNow.",
            "<strong>System integrators (SIs)</strong> — HCLTech, "
            "TCS, Infosys, Wipro, Tech Mahindra, LTIMindtree, "
            "Mphasis, Cognizant, Capgemini, Accenture, IBM "
            "Consulting, Atos / Eviden, Kyndryl, NTT DATA, "
            "Deloitte, EY, KPMG, PwC.",
            "<strong>Niche specialists</strong> — fintech "
            "platforms (Mambu, Thought Machine, Form3), security "
            "vendors (CrowdStrike, Wiz, Sigstore, Vault), data "
            "vendors (Bloomberg, LSEG, S&amp;P, Moody’s).",
            "<strong>Advisory firms</strong> — McKinsey, BCG, "
            "Bain, Oliver Wyman, Promontory; the strategic "
            "advisors who shape decisions before procurement "
            "starts.",
        ])
        + H3("0.4  The contract stack you will see on every deal")
        + ul([
            "<strong>MSA — Master Services Agreement</strong>. "
            "Umbrella terms: liabilities, IP, data, audit rights, "
            "termination, dispute resolution.",
            "<strong>SoW — Statement of Work</strong>. The "
            "specific scope, deliverables, milestones, "
            "acceptance criteria, fees per engagement.",
            "<strong>DPA — Data Processing Agreement</strong>. "
            "Required under GDPR / UK GDPR / DPDP Act / state "
            "privacy laws; defines processor / controller "
            "responsibilities.",
            "<strong>BAA — Business Associate Agreement</strong>. "
            "Healthcare-equivalent (US HIPAA); sometimes invoked "
            "for health-insurance lines.",
            "<strong>SLA / SLO schedule</strong>. Measurable "
            "service levels, credits and remedies.",
            "<strong>Security and resilience schedules</strong>. "
            "Vendor cyber controls, incident notification, "
            "TLPT cooperation; mandatory under DORA.",
            "<strong>Exit plan / termination assistance "
            "schedule</strong>. How you get out, what data is "
            "returned, in what format, over what period.",
            "<strong>Audit rights schedule</strong>. Who can "
            "audit, when, with what notice.",
        ])
    )
    return TopicSection(
        "0.  Primer — vendors, contracts and what makes BFSI different",
        "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Why is vendor management now a board-level technology topic?")
        + ol([
            "<strong>DORA designated CTPs.</strong> The EU "
            "Commission’s 2025 process formally designates Critical "
            "ICT Third Parties (hyperscalers and major vendors); "
            "they are subject to direct EU oversight; banks are "
            "required to hold tested exit plans.",
            "<strong>UK CTP regime live.</strong> Under FSMA 2023, "
            "HMT and the regulators jointly designate CTPs and "
            "set rules; first wave of designations expected during "
            "2025.",
            "<strong>RBI Outsourcing of IT Services MD (April "
            "2023).</strong> Comprehensive rule covering due "
            "diligence, board oversight, exit, and material "
            "outsourcing reporting.",
            "<strong>PRA SS2/21 + BoE / FCA / PRA OpRes</strong> "
            "— material outsourcing register, scenario testing, "
            "exit-plan reviews.",
            "<strong>MAS Outsourcing Guidelines + Cloud "
            "Annex</strong>; <strong>HKMA Supervisory Policy "
            "Manual SA-2</strong>; <strong>NYDFS Part 500.11</strong> "
            "third-party service-provider security; <strong>OCC "
            "Heightened Standards</strong> + <strong>Fed SR "
            "23-4</strong>.",
            "<strong>Talent + cost.</strong> Total cost of "
            "vendor relationships at tier-1 banks is regularly "
            "USD 5–15B a year; small efficiency gains are very "
            "large numbers.",
        ])
    )
    return TopicSection(
        "1.  Why vendor management is now board-level",
        "basic", body)


def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  subgraph "Procurement"\n'
            '    Need["Capability gap"]\n'
            '    Rfi["RFI<br/>shortlist the market"]\n'
            '    Rfp["RFP<br/>compare on scope and price"]\n'
            '    Demo["Demo + PoC"]\n'
            '    Sel["Selection + business case"]\n'
            '    Need --> Rfi --> Rfp --> Demo --> Sel\n'
            '  end\n'
            '  subgraph "Contracting"\n'
            '    MSA["MSA umbrella"]\n'
            '    Sow["SoW per engagement"]\n'
            '    DPA["DPA / data schedules"]\n'
            '    Sec["Security and resilience"]\n'
            '    Exit["Exit and termination"]\n'
            '    Sel --> MSA --> Sow\n'
            '    MSA --> DPA\n'
            '    MSA --> Sec\n'
            '    MSA --> Exit\n'
            '  end\n'
            '  subgraph "Delivery"\n'
            '    Plan["Plan and RAID"]\n'
            '    Steer["Steerco<br/>monthly"]\n'
            '    Wg["Working groups<br/>weekly"]\n'
            '    Run["Run, change and renew"]\n'
            '    Sow --> Plan --> Steer --> Wg --> Run\n'
            '  end\n'
            '  subgraph "Oversight"\n'
            '    Reg["Regulator: DORA / RBI / PRA / MAS / NYDFS"]\n'
            '    Aud["Internal audit"]\n'
            '    Risk["Operational risk"]\n'
            '    Sec --> Reg\n'
            '    Exit --> Reg\n'
            '    Run --> Aud --> Risk',
            "Procurement → contracting → delivery → oversight, with "
            "regulator and audit overlays at every stage.")
    )
    return TopicSection(
        "2.  The picture — procurement, contracting, delivery, oversight",
        "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  RFI / RFP / RFQ — the three procurement instruments")
        + ul([
            "<strong>RFI (Request for Information)</strong> — "
            "early-stage market scan; ‘who exists, what do you do, "
            "ballpark price?’ Used to shortlist 3–6 vendors.",
            "<strong>RFP (Request for Proposal)</strong> — formal "
            "scope, requirements, evaluation criteria; vendors "
            "respond with capability statements, references, "
            "demos, indicative pricing. The decision artefact.",
            "<strong>RFQ (Request for Quotation)</strong> — used "
            "when scope is settled and price is the variable; "
            "common for hardware and commodity services.",
            "<strong>PoC (Proof of Concept)</strong> — short, "
            "scoped, time-boxed test against your real data; "
            "typically 6–12 weeks; often paid; the most reliable "
            "input to a decision.",
        ])
        + H3("3.2  Vendor due diligence — what regulators expect to see")
        + ul([
            "<strong>Financial health</strong> — audited "
            "accounts, going-concern view, parent-company "
            "support letters where relevant.",
            "<strong>Cyber posture</strong> — SOC 2 Type II, "
            "ISO 27001, ISO 22301, PCI DSS attestations as "
            "applicable; penetration-test summaries; SBOM.",
            "<strong>Operational resilience</strong> — capacity "
            "and redundancy, continuity tests, incident history.",
            "<strong>Data and privacy</strong> — data-flow map, "
            "sub-processors, hosting locations, encryption-in-"
            "use approach, key custody.",
            "<strong>Concentration and sub-contracting</strong> — "
            "who else uses them, what % of their revenue you are, "
            "their own dependencies (often other hyperscalers).",
            "<strong>Conduct and integrity</strong> — sanctions "
            "and AML screening on the legal entity and beneficial "
            "owners; modern-slavery and ESG declarations.",
            "<strong>Reference checks</strong> — three "
            "regulator-relevant peers.",
        ])
        + H3("3.3  MSA, SoW, DPA — the named clauses to negotiate")
        + ul([
            "<strong>Liability cap</strong> — usually 1–3× annual "
            "fees; carve-outs for data breach, IP infringement, "
            "wilful misconduct, regulatory fines.",
            "<strong>Indemnities</strong> — IP, third-party data, "
            "regulator fines arising from vendor act/omission.",
            "<strong>Audit rights</strong> — bank, regulator and "
            "their appointees; reasonable notice; cost "
            "allocation.",
            "<strong>Sub-contracting and assignment</strong> — "
            "vendor cannot sub-contract material services or "
            "assign without consent.",
            "<strong>Change control</strong> — process, fee "
            "structure, dispute resolution.",
            "<strong>Step-in / termination assistance</strong> — "
            "regulator may require step-in rights; vendor "
            "supports orderly exit at agreed rate-card.",
            "<strong>Pricing</strong> — fixed, time-and-"
            "materials, capacity-based, outcome-based; "
            "indexation; benchmarking clauses.",
            "<strong>Service credits</strong> — meaningful "
            "(e.g. >5% of monthly fee for material breaches), "
            "but credits are not the regulator’s only "
            "remedy.",
            "<strong>Exit terms</strong> — notice, cost, data "
            "return format and timeline, parallel-running "
            "support.",
        ])
        + H3("3.4  Pricing models — pick by the work, not by habit")
        + ul([
            "<strong>Fixed price / fixed scope</strong> — best "
            "when scope is genuinely settled; vendor carries "
            "delivery risk.",
            "<strong>Time and materials (T&amp;M)</strong> — for "
            "discovery, advisory, exploratory work; "
            "rate cards.",
            "<strong>Managed services</strong> — agreed scope at "
            "agreed SLAs for monthly fee.",
            "<strong>Capacity-based / FTE pool</strong> — common "
            "for SI delivery teams; ‘pod’ pricing.",
            "<strong>Consumption / pay-as-you-go</strong> — "
            "hyperscalers; SaaS commitments and Reserved "
            "Instances; FinOps essential.",
            "<strong>Outcome-based</strong> — fees tied to "
            "agreed outcomes (savings, throughput, NPS); "
            "intellectually attractive, operationally hard.",
        ])
        + H3("3.5  Programme delivery — the named rituals")
        + ul([
            "<strong>Programme charter</strong> — purpose, "
            "scope, governance, sponsors, success criteria, "
            "constraints. Signed before money flows.",
            "<strong>RAID log</strong> — Risks, Assumptions, "
            "Issues, Dependencies. Living document.",
            "<strong>Steering committee (steerco)</strong> — "
            "monthly; SVP sponsor + business + risk + "
            "compliance + technology + vendor.",
            "<strong>Working groups</strong> — weekly per stream; "
            "the engine room.",
            "<strong>Scrum-of-scrums / Nexus / SAFe Release "
            "Train</strong> — operational coordination across "
            "teams.",
            "<strong>Programme MIS</strong> — burn-down, "
            "burn-up, milestone tracker, RAG status, run-cost "
            "tracker, regulator-deadline tracker.",
            "<strong>Quality gates</strong> — design, security, "
            "performance, regulator readiness; named owners.",
            "<strong>Cutover and hypercare</strong> — go-live "
            "checklist, war-room, hypercare period.",
            "<strong>Lessons learned</strong> — at the end of "
            "every release; a programme-level PIR.",
        ])
        + H3("3.6  RAG status — the most-abused report in BFSI")
        + p("Red, Amber, Green status is the standard programme "
            "summary. The discipline is to keep the definition "
            "consistent: <strong>Green</strong> = on plan, no "
            "intervention needed; <strong>Amber</strong> = "
            "intervention required, recovery plan exists; "
            "<strong>Red</strong> = material risk to objective, "
            "executive escalation needed. Programmes that go from "
            "‘green’ to ‘red’ in a single update without ‘amber’ "
            "in between have governance problems, not delivery "
            "problems.")
    )
    return TopicSection(
        "3.  How procurement, contracting and delivery actually work",
        "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  Outsourcing and resilience rules — region by region")
        + table(
            ["Regime", "What it requires", "Practical effect"],
            [
                ["<strong>EU DORA + EBA Outsourcing "
                 "Guidelines</strong>",
                 "ICT third-party register; designation of CTPs; "
                 "exit plans; threat-led testing of vendors; "
                 "concentration-risk monitoring.",
                 "Every material vendor in scope has a documented "
                 "exit plan and tested incident drill."],
                ["<strong>UK CTP regime (FSMA 2023) + PRA SS2/21 "
                 "+ FCA / PRA OpRes</strong>",
                 "Material-outsourcing register; CTP "
                 "designations; impact-tolerance mapping per "
                 "important business service.",
                 "Exit plans are tested; HMT-PRA-FCA can ask "
                 "for evidence directly."],
                ["<strong>RBI Outsourcing of IT Services MD "
                 "(April 2023)</strong>",
                 "Board-approved outsourcing policy; due "
                 "diligence; agreement clauses; material "
                 "outsourcing reporting; right of audit; exit "
                 "management.",
                 "Engagement letters and SoWs aligned to RBI "
                 "model clauses; regulator can step in."],
                ["<strong>MAS Outsourcing Guidelines + Cloud "
                 "Annex</strong>",
                 "Risk assessment; due diligence; contractual "
                 "clauses; on-site inspection; sub-contracting "
                 "consent.",
                 "Audit clauses are non-negotiable; regulator "
                 "can inspect cloud."],
                ["<strong>HKMA SA-2</strong>",
                 "Risk-based outsourcing oversight.",
                 "Material outsourcing requires HKMA "
                 "engagement."],
                ["<strong>NYDFS Part 500.11 + OCC + Fed SR "
                 "23-4</strong>",
                 "Third-party service provider security; "
                 "minimum cybersecurity controls; ongoing "
                 "monitoring.",
                 "Vendor cyber posture must be evidenced "
                 "annually."],
                ["<strong>Australia APRA CPS 230</strong> "
                 "(in force July 2025)",
                 "Operational risk management including service "
                 "providers; tolerances; testing.",
                 "Material service-provider register and "
                 "tolerances."],
            ]
        )
        + H3("4.2  Concentration risk — the conversation no one wants to have")
        + p("Tier-1 banks have legitimate, large concentrations on "
            "a small number of vendors: AWS or Azure; one of HCLTech "
            "/ TCS / Infosys / Accenture for application services; "
            "Murex or Aladdin for critical workflows; Bloomberg for "
            "data. Regulators are not against this, but they are "
            "against it being unacknowledged. The expected shape:")
        + ul([
            "Documented identification of concentrations (vendor, "
            "service, geography, sub-processor).",
            "Quantified impact tolerance per important business "
            "service.",
            "Multi-year roadmap for de-concentration where "
            "possible (e.g. multi-cloud strategic capabilities).",
            "Tested exit plan even where exit is "
            "implausible.",
        ])
        + H3("4.3  Multi-vendor and multi-cloud — when, and when not")
        + ul([
            "<strong>Multi-vendor for SI services</strong> — "
            "common; encourages competition and avoids "
            "single-supplier capture.",
            "<strong>Multi-cloud strategic</strong> — chosen "
            "deliberately for redundancy of business services, "
            "not for every workload; cost overhead is real.",
            "<strong>Multi-cloud incidental</strong> — most "
            "tier-1 banks have workloads on 2–3 hyperscalers "
            "without it being a strategic choice; manage as "
            "estate, not architecture.",
            "<strong>Single-vendor by design</strong> — "
            "acceptable when the workload is non-systemic and "
            "the exit plan is feasible.",
        ])
    )
    return TopicSection(
        "4.  Region by region — outsourcing, resilience, "
        "concentration",
        "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  Vendor segmentation — the four-quadrant view")
        + ul([
            "<strong>Strategic</strong> — high spend + high "
            "criticality. Joint roadmap, executive sponsors, "
            "quarterly business reviews.",
            "<strong>Operational</strong> — high spend + lower "
            "criticality. Disciplined commercial management, "
            "clear SLAs.",
            "<strong>Critical</strong> — lower spend + high "
            "criticality. Often niche specialists; risk-managed "
            "tightly; succession plans.",
            "<strong>Tactical</strong> — lower spend + lower "
            "criticality. Streamlined procurement; minimum "
            "compliance overhead.",
        ])
        + H3("5.2  Programme delivery — the eight failure modes")
        + ul([
            "<strong>Scope creep without re-baseline</strong> — "
            "scope grows, plan stays; collision delayed not "
            "averted.",
            "<strong>Vendor optimism in proposals</strong> — "
            "‘we’ve done this 50 times’; rarely with this stack, "
            "this regulator, this scale.",
            "<strong>Asymmetric incentives</strong> — vendor "
            "paid for activity, bank values outcomes; align "
            "before signing.",
            "<strong>Discovery treated as delivery</strong> — "
            "the first 90 days are not the next 9 months.",
            "<strong>Hero leadership</strong> — programme "
            "depends on one person; bus-factor 1.",
            "<strong>Underweight risk and compliance</strong> — "
            "find regulator gaps in UAT, not design.",
            "<strong>Steerco theatre</strong> — green RAG "
            "until the day before launch.",
            "<strong>Hypercare absent</strong> — go-live with "
            "no war-room and no rollback plan.",
        ])
        + H3("5.3  Patterns that consistently work")
        + ul([
            "<strong>Discovery sprint</strong> — 4–8 weeks "
            "before contract signature; co-funded if needed.",
            "<strong>Two-vendor PoC</strong> — pay both, "
            "evaluate seriously, cheaper than a wrong "
            "decision.",
            "<strong>Outcome-linked milestones</strong> — "
            "release fees against acceptance, not progress.",
            "<strong>Embedded risk and compliance</strong> in "
            "the squad, not at the gate.",
            "<strong>Independent assurance</strong> — small, "
            "named, standing review; not a dotted line on the "
            "org chart.",
            "<strong>Programme war-room for cutover</strong> "
            "with named on-call across vendor, bank and "
            "regulator-relevant teams.",
            "<strong>Lessons-learned culture</strong> — "
            "blameless write-ups; cross-programme libraries.",
        ])
        + H3("5.4  AI in vendor management and programme delivery")
        + ul([
            "<strong>Contract analysis</strong> — Generative AI "
            "extracts obligations from MSAs and SoWs; named "
            "vendors include Ironclad, LinkSquares, Robin AI.",
            "<strong>RAID and steerco summarisation</strong> — "
            "LLMs surface what changed since last steerco from "
            "Jira / ADO / spreadsheets.",
            "<strong>Vendor monitoring</strong> — automated "
            "evidence collection (SOC 2 reports, status "
            "dashboards, regulator filings) for continuous "
            "third-party risk.",
            "<strong>Demand forecasting</strong> — AI for "
            "capacity planning across vendor pools.",
            "<strong>Audit readiness</strong> — RAG over "
            "ADRs, SoWs, RAID and risk decisions for fast "
            "regulator responses.",
        ])
    )
    return TopicSection(
        "5.  Advanced — segmentation, failure modes, patterns, AI",
        "advanced", body)


def _sec6() -> TopicSection:
    body = (
        H3("6.1  Choosing an SI partner")
        + table(
            ["Need", "Best fit in 2025", "Why"],
            [
                ["Large core-banking / payments programme",
                 "Tier-1 SI (HCLTech, TCS, Infosys, Wipro, "
                 "Capgemini, Accenture, IBM Consulting, "
                 "Cognizant)",
                 "Scale, regulator-acceptable, deep platform "
                 "practices, India-anchored cost base."],
                ["Cloud-native modernisation",
                 "Hyperscaler partners + tier-1 SI",
                 "Need cloud-native engineering and BFSI "
                 "domain depth in equal parts."],
                ["Risk and regulatory transformation",
                 "Big 4 (Deloitte, EY, KPMG, PwC) + "
                 "specialist tier-2 SI",
                 "Regulator-fluent advisory + delivery "
                 "execution."],
                ["Niche product implementation (Murex, "
                 "Calypso, Guidewire)",
                 "Specialist boutiques + tier-1 SI’s vendor "
                 "practice",
                 "Vendor-certified expertise; reference "
                 "implementations matter."],
                ["Greenfield digital bank build",
                 "Cloud-native specialists + bank-side "
                 "platform team",
                 "Speed and engineering culture more "
                 "important than scale."],
            ]
        )
        + H3("6.2  Engagement model — pick by the work")
        + table(
            ["Model", "When it wins", "Watch-outs"],
            [
                ["<strong>Time and materials</strong>",
                 "Discovery, advisory, exploratory.",
                 "Open-ended cost; risk needs "
                 "active management."],
                ["<strong>Fixed price / fixed scope</strong>",
                 "Stable scope, well-understood domain.",
                 "Brittle to genuine change; vendor will "
                 "manage to scope, not to outcome."],
                ["<strong>Managed services</strong>",
                 "Run and steady-state; integration testing.",
                 "Innovation pace can drop without "
                 "deliberate counter-pressure."],
                ["<strong>Capacity-based / pod</strong>",
                 "Multi-year platform programmes.",
                 "Productivity erosion if bench is not "
                 "managed."],
                ["<strong>Outcome-based</strong>",
                 "Mature programmes with measurable "
                 "outcomes.",
                 "Designing the metric is the hardest part; "
                 "easy to game."],
            ]
        )
        + H3("6.3  Steerco design — small choices that matter")
        + ul([
            "Sponsor in the room, not delegated.",
            "Risk and compliance in the room, not informed.",
            "RAG is a leading indicator, not a status.",
            "Named decisions, owners, dates per item.",
            "Consent agenda for routine; debate the 2–3 "
            "decisions worth debating.",
            "Vendor partner sits at the table for material "
            "items; both sides own the outcome.",
        ])
    )
    return TopicSection(
        "6.  Decision matrices — partner choice, engagement model, "
        "steerco design",
        "intermediate", body)


def _sec7() -> TopicSection:
    body = (
        example(
            "TSB 2018 — what a bad cutover costs",
            ol([
                "TSB Bank in the UK migrated 5M customers from "
                "Lloyds infrastructure to a new Sabadell-built "
                "platform on a single weekend in April 2018.",
                "Defects, capacity gaps and incident-management "
                "failures left services degraded for weeks; FCA "
                "+ PRA fined TSB £48.7M in 2022.",
                "Lessons widely cited: insufficient end-to-end "
                "testing; over-confident cutover plan; vendor "
                "and bank governance not joined up; "
                "insufficient resilience capacity for first-day "
                "load; hypercare staffing miscalculated.",
            ])
        )
        + example(
            "Lloyds + Thought Machine — multi-year strangler-fig",
            ol([
                "Lloyds invested in Thought Machine and is "
                "progressively migrating products to Vault — "
                "savings first, lending later.",
                "Programme governance combines Lloyds product "
                "owners with Thought Machine engineering and "
                "tier-1 SI delivery teams.",
                "Lessons: multi-year migrations succeed by "
                "narrow scope per release, intense governance, "
                "explicit retreat options.",
            ])
        )
        + example(
            "Standard Chartered ‘aXess’ — multi-vendor platform "
            "engineering",
            ol([
                "SC built an internal developer platform on "
                "Azure (AKS) with Backstage, Argo CD, Datadog; "
                "delivery is multi-vendor with HCLTech among "
                "others.",
                "Steerco governance separates platform "
                "engineering from product delivery; "
                "consumption metrics drive funding.",
                "Lessons: the platform team is its own product "
                "team; vendors deliver against platform "
                "standards, not against parallel architectures.",
            ])
        )
        + example(
            "Indian PSU bank — RBI Outsourcing MD compliance",
            ol([
                "Tier-1 PSU bank reviewed its IT outsourcing "
                "estate against the April 2023 RBI MD; "
                "identified material vs non-material vendors, "
                "rewrote SoW templates, added board-approved "
                "outsourcing policy and exit plans.",
                "Lessons: regulatory updates of this size are "
                "an opportunity to consolidate, not just a "
                "compliance exercise.",
            ])
        )
        + example(
            "EU bank preparing for DORA — vendor-side workstream",
            ol([
                "EU bank classified all material ICT third "
                "parties; obtained DORA-aligned addenda from "
                "every one; re-tested exit plans for two "
                "tier-1 vendors; reported register to the "
                "national competent authority by deadline.",
                "Lessons: vendor cooperation on addenda is "
                "tractable when the deadline is real; the "
                "exit-plan tests are where most rework "
                "happens.",
            ])
        )
    )
    return TopicSection(
        "7.  Worked examples — five real BFSI vendor and programme "
        "stories",
        "intermediate", body)


def _sec8() -> TopicSection:
    return TopicSection(
        "8.  Questions a leader asks of any vendor or programme review",
        "basic",
        ol([
            "Is the vendor on our material outsourcing register, "
            "and is the rationale documented?",
            "What is the tested exit plan, and when did we last "
            "rehearse it?",
            "Where does this engagement sit in the four-quadrant "
            "(strategic / operational / critical / tactical) "
            "view?",
            "What is the named SMF / officer accountable for the "
            "vendor relationship?",
            "Is the SoW outcome-linked, time-and-materials, or "
            "fixed-price — and is that the right model for the "
            "work?",
            "What does the RAID log say is on fire this week, "
            "and who owns each item?",
            "Has the steerco moved from ‘green’ to ‘red’ "
            "without an ‘amber’ in between?",
            "What is the regulator-deadline tracker for this "
            "programme, and is there a credible margin to each "
            "deadline?",
            "What concentration are we creating with this "
            "engagement, and how is it acknowledged?",
            "Are security and resilience clauses (DORA-aligned) "
            "in the contract, with TLPT cooperation, incident "
            "notification and audit rights?",
            "What is the exit-cost projection, and have we "
            "modelled it?",
            "What are the 2–3 decisions we need to make at this "
            "steerco, and who is the decision-maker?",
        ]))


def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘The vendor will tell us if there is a problem.’ — "
            "They will, eventually. Independent assurance and "
            "your own delivery insight catch it earlier.",
            "‘Fixed price is safer.’ — Fixed price is safer for "
            "scope you understand; it is more dangerous for "
            "scope you don’t. Match the model to the work.",
            "‘Service credits are our protection.’ — They are a "
            "tiny fraction of the loss in a real incident. The "
            "controls that prevent the incident are the "
            "protection.",
            "‘RFP scoring solves vendor selection.’ — Scoring "
            "rationalises a decision that has often already been "
            "made. The PoC and the references settle it.",
            "‘Exit plans are paperwork.’ — DORA tests them; RBI "
            "tests them; PRA tests them. Untested exit plans are "
            "findings.",
            "‘Programme is green.’ — Green for what? On budget, "
            "on scope, on time, on outcome — usually one is "
            "true and one is hiding.",
            "‘Steerco doesn’t need risk and compliance.’ — Then "
            "it isn’t a BFSI steerco.",
            "‘Sub-contracting was a vendor decision.’ — In BFSI "
            "regulators expect explicit consent for material "
            "sub-contracting.",
            "‘We’ll outsource the operational risk to the "
            "vendor.’ — Operational risk cannot be outsourced; "
            "only the activity can.",
            "‘We don’t need a programme war-room; the vendor "
            "has one.’ — You both need one. Cutover incidents "
            "compound across boundaries.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("MSA / SoW / DPA / BAA", "Master Services Agreement "
                "/ Statement of Work / Data Processing Agreement "
                "/ Business Associate Agreement."),
            ("RFI / RFP / RFQ", "Request for Information / "
                "Proposal / Quotation."),
            ("PoC", "Proof of Concept — short, scoped vendor "
                "evaluation."),
            ("SLA / SLO", "Service-Level Agreement / Objective."),
            ("RAID", "Risks, Assumptions, Issues, Dependencies "
                "log."),
            ("RAG", "Red / Amber / Green programme status."),
            ("Steerco", "Steering committee — programme "
                "governance forum."),
            ("Hypercare", "Post-go-live elevated support "
                "period."),
            ("Outcome-based pricing", "Fees tied to measurable "
                "business outcomes."),
            ("Capacity / pod model", "FTE-pool engagement common "
                "with SI delivery."),
            ("CTP", "Critical Third Party — designated vendor "
                "under EU DORA / UK FSMA 2023."),
            ("Material outsourcing", "Classification under RBI / "
                "PRA / EBA / MAS rules."),
            ("Step-in / termination assistance", "Vendor "
                "obligations to support orderly exit or "
                "regulator step-in."),
            ("Sub-processor / sub-contractor", "Vendor’s "
                "vendors; subject to bank consent for material "
                "services."),
            ("Concentration risk", "Excessive reliance on a "
                "small number of vendors / clouds / regions."),
            ("Schrems II", "2020 CJEU ruling restricting "
                "personal-data flows from EU to non-adequate "
                "jurisdictions."),
            ("Right of audit", "Bank, regulator and appointee "
                "audit rights baked into the contract."),
            ("Indemnity / liability cap", "Risk-allocation "
                "clauses negotiated in MSAs."),
            ("Service credit", "Fee reduction for SLA "
                "breaches; not the only remedy."),
            ("Discovery sprint", "Pre-contract paid exploration "
                "to de-risk scope and design."),
            ("Strangler-fig migration", "Incremental "
                "replacement pattern; default for legacy "
                "modernisation."),
            ("Programme PIR", "Post-Implementation Review at "
                "the programme level."),
            ("DORA / RBI Outsourcing MD / PRA SS2/21 / MAS "
             "Outsourcing / NYDFS Part 500.11 / OCC Heightened "
             "Standards / Fed SR 23-4 / APRA CPS 230",
             "The major outsourcing-related regulator regimes."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
