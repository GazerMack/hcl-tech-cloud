"""Leadership Lenses · 03 — Communicating with regulators and boards."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="VII.3",
        slug="03-regulator-and-board-communication",
        title="Communicating with regulators and boards — the skill that unlocks everything else",
        one_liner=(
            "You can build the finest architecture and run the sharpest programme, but if you "
            "cannot explain it to a board that thinks in risk appetite and a regulator that "
            "thinks in supervisory expectations, you will be overruled, delayed, or fined. "
            "This topic teaches the language, the formats, the rituals, and the traps of "
            "upward and outward communication in regulated financial services."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


# ------------------------------------------------------------------ 0
def _sec0() -> TopicSection:
    body = (
        primer(
            p("A techno-functional leader in BFSI does not just build technology. They translate "
              "technology into the language that boards and regulators use: risk, resilience, "
              "capital, consumer outcomes, and systemic stability. If you cannot do this "
              "translation, someone else will — and they will get it wrong.")
        )
        + H3("0.1  IT-side anchor — the investor pitch")
        + it_anchor(
            p("If you have ever seen a startup pitch to a VC, you know the shape: problem, "
              "solution, traction, team, ask. A board paper works the same way, but the audience "
              "is a fiduciary, not a speculator. They do not want to hear how clever the "
              "technology is. They want to know: what risk does this create or retire, what "
              "does it cost, what happens if it fails, and who is accountable. Every sentence "
              "must answer one of those questions or it does not belong in the paper.")
        )
        + H3("0.2  BFSI-side anchor — the RBI inspection visit")
        + bfsi_anchor(
            p("Imagine an RBI inspection team arriving at your bank's IT office. They ask: "
              "'Show us the board-approved IT strategy. Show us the risk appetite statement "
              "for technology. Show us how you test operational resilience. Show us the exit "
              "plan for your largest cloud provider.' If the CISO, CTO, or Head of IT cannot "
              "answer fluently — in the regulator's own language — the inspection becomes an "
              "adverse finding. Every major regulator (RBI, PRA, MAS, ECB/SSM, OCC, NYDFS, "
              "APRA) conducts these reviews, and the technology leader is expected to present "
              "directly.")
        )
        + H3("0.3  The two audiences you must serve — and how they differ")
        + table(
            ["Dimension", "Board / Board Risk Committee", "Regulator (supervisory team)"],
            [
                ["Primary concern", "Shareholder value, risk appetite, reputation, fiduciary duty",
                 "Financial stability, consumer protection, market integrity"],
                ["Time horizon", "Quarterly earnings to 3-year strategy",
                 "Supervisory cycle (12–18 months) to systemic horizon (5+ years)"],
                ["Language", "Risk appetite, capital impact, customer outcomes, competitive position",
                 "Supervisory expectations, prudential standards, remediation plans, attestations"],
                ["Decision power", "Approve strategy, set risk appetite, hold management accountable",
                 "Set rules, conduct inspections, impose restrictions, levy fines"],
                ["What they hate", "Surprises, jargon, unclear accountability, missing options",
                 "Gaps between policy and evidence, unacknowledged risks, late notification"],
            ]
        )
    )
    return TopicSection("0.  Primer — anchored to things you already know", "basic", body)


# ------------------------------------------------------------------ 1
def _sec1() -> TopicSection:
    body = (
        p("Technology leaders in BFSI must communicate upward and outward because:")
        + ol([
            "<strong>Accountability regimes demand it.</strong> The UK Senior Managers and "
            "Certification Regime (SM&CR) makes named individuals personally liable for "
            "technology failures. India's RBI Master Direction on IT Governance (Nov 2023) "
            "requires board-level oversight of IT strategy. The EU's DORA assigns ICT risk "
            "management to the management body. In the US, OCC Heightened Standards require "
            "a board-approved technology risk appetite.",

            "<strong>Boards cannot govern what they do not understand.</strong> If the only "
            "technology briefing a board receives is a vendor slide deck, governance is "
            "performative. The techno-functional leader's job is to make the board genuinely "
            "capable of challenging management on technology decisions.",

            "<strong>Regulators set the rules of the game.</strong> Early, transparent "
            "engagement with your supervisor avoids nasty surprises. A regulator who learns "
            "about a major migration from a newspaper article will respond very differently "
            "from one who was briefed six months in advance.",

            "<strong>The cost of getting it wrong is existential.</strong> TSB's botched 2018 "
            "migration led to £48.7M in FCA/PRA fines, £366M in total costs, and a CEO "
            "departure. Much of the root cause was governance and communication failure, "
            "not just technical failure.",
        ])
    )
    return TopicSection("1.  Why communication is a first-class leadership skill", "basic", body)


# ------------------------------------------------------------------ 2
def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart TB\n'
            '  subgraph "Board Governance"\n'
            '    BA["Board / Board Risk Committee"]\n'
            '    EA["Executive Committee / ExCo"]\n'
            '    CRO["CRO / Chief Risk Officer"]\n'
            '    CTO["CTO / CIO"]\n'
            '  end\n'
            '  subgraph "Management Layer"\n'
            '    TF["Techno-functional Leader"]\n'
            '    CISO["CISO"]\n'
            '    COO["COO / Head of Ops"]\n'
            '  end\n'
            '  subgraph "Regulator Engagement"\n'
            '    SUP["Supervisory Team"]\n'
            '    INS["Inspection / On-site"]\n'
            '    ENF["Enforcement"]\n'
            '  end\n'
            '  TF -->|"Board papers<br/>risk reports"| CTO\n'
            '  CTO -->|"ExCo papers"| EA\n'
            '  EA -->|"Board pack"| BA\n'
            '  TF -->|"Incident reports<br/>remediation plans"| CRO\n'
            '  CRO --> BA\n'
            '  TF -->|"Direct presentation<br/>during inspections"| INS\n'
            '  CTO -->|"Periodic meetings<br/>thematic reviews"| SUP\n'
            '  SUP -->|"Findings<br/>s166 / MRA"| EA\n'
            '  INS -->|"Adverse findings"| ENF',
            "How a techno-functional leader's communication flows upward to the board and outward to the regulator.")
    )
    return TopicSection("2.  The communication map in one picture", "basic", body)


# ------------------------------------------------------------------ 3
def _sec3() -> TopicSection:
    body = (
        H3("3.1  Board papers — the most important document you will write")
        + p("A board paper is not a PowerPoint. It is a structured decision document. "
            "The standard shape across UK, EU, Singapore, and increasingly Indian banks is:")
        + ol([
            "<strong>Purpose.</strong> One sentence: 'This paper seeks board approval for X' "
            "or 'This paper is for information on Y.'",
            "<strong>Executive summary.</strong> Half a page. The busy NED reads only this.",
            "<strong>Background and context.</strong> What the board needs to know to decide.",
            "<strong>Options and recommendation.</strong> At least two options with pros, cons, "
            "cost, risk, and timeline. Never present a single option.",
            "<strong>Risk assessment.</strong> What new risks does this create? How do they map "
            "to the board's stated risk appetite?",
            "<strong>Financial impact.</strong> CapEx, OpEx, run-rate change, payback period.",
            "<strong>Regulatory implications.</strong> Which regulators care? Have they been "
            "engaged? Any conditions?",
            "<strong>Recommendation.</strong> Clear, one sentence.",
            "<strong>Appendices.</strong> Technical detail for those who want it. Never in the "
            "main body.",
        ])
        + callout("Golden rule", p("If a board member has to ask 'so what do you want me to "
            "decide?', the paper has failed. Lead with the decision."), "info")

        + H3("3.2  Regulator engagement — proactive vs reactive")
        + p("The two modes of regulator communication are fundamentally different:")
        + table(
            ["Mode", "When", "Format", "Tone"],
            [
                ["<strong>Proactive / BAU</strong>",
                 "Periodic supervisory meetings, thematic reviews, pre-notification of major changes",
                 "Structured presentations, written submissions, data returns",
                 "Transparent, factual, forward-looking. 'We are doing X because of Y. Here is our timeline.'"],
                ["<strong>Reactive / incident</strong>",
                 "After a major incident, during an inspection finding, in response to an enforcement action",
                 "Incident reports, remediation plans, attestations, s166 skilled-person reviews (UK)",
                 "Contrite where warranted, precise, committed to deadlines. Never defensive."],
            ]
        )

        + H3("3.3  The named regulatory instruments you will encounter")
        + table(
            ["Instrument", "Jurisdiction", "What it means for you"],
            [
                ["<strong>MRA (Matter Requiring Attention)</strong>", "US (OCC, Fed)",
                 "A formal finding that requires a documented remediation plan with deadlines. "
                 "Failure to remediate can escalate to a MRIA (Matter Requiring Immediate Attention) "
                 "or Consent Order."],
                ["<strong>s166 Skilled Person Review</strong>", "UK (FCA/PRA)",
                 "The regulator appoints an independent reviewer (Big 4, boutique) at the bank's cost "
                 "to investigate a specific area. You will present to them."],
                ["<strong>Dear CEO / Dear CRO letter</strong>", "UK, EU, India",
                 "A thematic letter setting supervisory expectations. Not optional. Requires a "
                 "board-acknowledged response."],
                ["<strong>RBI Inspection Report</strong>", "India",
                 "After an on-site inspection, RBI issues findings. The bank responds with a "
                 "compliance report. Unresolved findings escalate."],
                ["<strong>ECB/SSM SREP</strong>", "Eurozone",
                 "Supervisory Review and Evaluation Process. Annual assessment that can result in "
                 "additional capital requirements or operational restrictions."],
                ["<strong>MAS Notice / Circular</strong>", "Singapore",
                 "Legally binding directions (Notices) or guidance (Circulars). Non-compliance "
                 "is an offence."],
            ]
        )

        + H3("3.4  Incident communication — the golden hour")
        + p("When a major technology incident hits (system outage, data breach, cyber attack), "
            "the communication clock starts immediately:")
        + ol([
            "<strong>Internal escalation (0–30 minutes).</strong> War room activated, CTO/CISO "
            "informed, initial impact assessment.",
            "<strong>Board notification (1–4 hours).</strong> Chair of Board Risk Committee "
            "informed if the incident is material. Brief facts only — do not speculate.",
            "<strong>Regulator notification (per regime).</strong> "
            "RBI: report material cyber incidents within 6 hours. "
            "ECB/DORA: major ICT incident notification within 4 hours (initial), 72 hours (intermediate), "
            "1 month (final). "
            "PRA: as soon as reasonably practicable. "
            "MAS: within 1 hour for critical system failures. "
            "NYDFS Part 500: 72 hours for cybersecurity events.",
            "<strong>Customer communication (as needed).</strong> If customers are affected, "
            "communicate proactively. Silence breeds complaint escalation and media attention.",
            "<strong>Post-incident review (within 2 weeks).</strong> Root-cause analysis, "
            "remediation plan, lessons learned. Share with the board and regulator.",
        ])
    )
    return TopicSection("3.  How it actually works — board papers, regulator engagement, incidents",
                        "intermediate", body)


# ------------------------------------------------------------------ 4
def _sec4() -> TopicSection:
    body = (
        H3("4.1  Board committees that a technology leader presents to")
        + table(
            ["Committee", "Focus", "What they want from technology"],
            [
                ["<strong>Board Risk Committee (BRC)</strong>",
                 "All material risks, including technology and cyber",
                 "Risk appetite metrics, incident trends, top-5 technology risks, remediation status"],
                ["<strong>Board Audit Committee</strong>",
                 "Internal audit findings, external audit, controls",
                 "Audit finding closure rates, control effectiveness, SOX/SOC attestation status"],
                ["<strong>Board Technology Committee</strong> (where it exists)",
                 "Technology strategy, investment, talent",
                 "Strategy execution, investment portfolio health, talent pipeline, innovation pipeline"],
                ["<strong>Full Board</strong>",
                 "Strategic decisions, risk appetite, major investments",
                 "Major programme approvals (core migration, cloud strategy), annual IT strategy refresh"],
            ]
        )

        + H3("4.2  Regulatory engagement models by jurisdiction")
        + table(
            ["Jurisdiction", "Primary supervisor for tech risk", "Engagement cadence"],
            [
                ["<strong>India</strong>", "RBI Department of Supervision / IT Examination",
                 "Annual IT examination (on-site), periodic off-site returns, thematic reviews. "
                 "RBI can issue directions under Banking Regulation Act."],
                ["<strong>United Kingdom</strong>", "PRA (prudential) + FCA (conduct)",
                 "Continuous supervision for Category 1 firms. Named supervisor. Periodic reviews, "
                 "thematic deep-dives, s166 when needed."],
                ["<strong>Eurozone</strong>", "ECB/SSM (significant banks) + NCA (less significant)",
                 "Annual SREP, on-site inspections, thematic reviews (e.g., IT and cyber risk). "
                 "DORA adds ICT risk-specific oversight from January 2025."],
                ["<strong>United States</strong>", "OCC (national banks), Fed (BHCs), FDIC, NYDFS (state)",
                 "Annual exam cycle, quarterly meetings for large banks, targeted exams. "
                 "Interagency guidance (FFIEC IT Handbook)."],
                ["<strong>Singapore</strong>", "MAS Technology Risk Supervision",
                 "Periodic inspections, thematic assessments, FEAT principles for AI. "
                 "MAS is known for being technically sophisticated."],
            ]
        )
    )
    return TopicSection("4.  Types and variations — committees, jurisdictions, formats",
                        "intermediate", body)


# ------------------------------------------------------------------ 5
def _sec5() -> TopicSection:
    body = (
        H3("5.1  The language gap — and how to bridge it")
        + p("The deepest failure mode in board and regulator communication is the language gap. "
            "Technology leaders speak in systems, architectures, and SLAs. Board members speak "
            "in risk appetite, capital, and strategic objectives. Regulators speak in prudential "
            "standards, supervisory expectations, and systemic stability.")
        + table(
            ["You say (technology)", "Board hears", "Say this instead"],
            [
                ["'We need to migrate to Kubernetes'",
                 "'Another expensive IT project'",
                 "'Our current infrastructure cannot scale to meet the 30% transaction growth we "
                 "forecast. Migration to container orchestration reduces unplanned downtime risk "
                 "by 60% and cuts infrastructure cost by 25% over 3 years.'"],
                ["'Our SLA is 99.95%'",
                 "'Numbers I cannot evaluate'",
                 "'We are available 99.95% of the time, which means up to 4.4 hours of downtime "
                 "per year. Our risk appetite target is 99.99% (52 minutes). We have a plan to "
                 "close this gap by Q3.'"],
                ["'We need a WAF and SIEM upgrade'",
                 "'More security spending'",
                 "'Two of our top-5 technology risks — web application attacks and delayed "
                 "incident detection — are mitigated by this investment. Without it, we remain "
                 "outside our stated risk appetite for cyber.'"],
            ]
        )

        + H3("5.2  Risk appetite statements for technology — how to write them")
        + p("A risk appetite statement converts abstract tolerance into measurable thresholds. "
            "The board approves these, and the technology leader reports against them.")
        + table(
            ["Risk category", "Example appetite statement", "Metric"],
            [
                ["Availability", "'We will not tolerate more than 2 hours of unplanned downtime "
                 "per quarter for Tier-1 business services.'",
                 "Unplanned downtime hours per quarter"],
                ["Cyber", "'We will maintain a residual cyber risk rating of Medium or below "
                 "as assessed by our internal framework, aligned to NIST CSF 2.0.'",
                 "Residual risk rating per domain"],
                ["Change failure", "'No more than 5% of production changes will cause incidents.'",
                 "Change failure rate (DORA metric)"],
                ["Third-party concentration", "'No single ICT third party will support more than "
                 "40% of our Tier-1 business services without a tested exit plan.'",
                 "Concentration percentage per vendor"],
                ["Data", "'Zero material data breaches involving customer PII per year.'",
                 "Reportable data breaches"],
            ]
        )

        + H3("5.3  The art of the regulator relationship")
        + p("Experienced BFSI leaders treat the regulator relationship like a client relationship:")
        + ul([
            "<strong>No surprises.</strong> If you are planning a major migration, tell your "
            "supervisor before you tell the vendor. They would rather hear your plan than read "
            "about your outage.",
            "<strong>Be the credible voice.</strong> When the regulator asks a technical question, "
            "the CTO or Head of Technology should answer directly, not defer to a consultant.",
            "<strong>Respond to findings promptly and completely.</strong> A finding that lingers "
            "for two supervisory cycles becomes an escalation. Close it or explain credibly why "
            "the timeline has moved.",
            "<strong>Anticipate thematic priorities.</strong> If the regulator publishes a "
            "thematic review on operational resilience, assume an inspection is coming. "
            "Prepare before they ask.",
            "<strong>Understand your supervisor's KPIs.</strong> Supervisors are measured on "
            "whether they identified risks early. Help them succeed and they become allies.",
        ])
    )
    return TopicSection("5.  Advanced — the language gap, risk appetite, and the art of the relationship",
                        "advanced", body)


# ------------------------------------------------------------------ 6
def _sec6() -> TopicSection:
    body = (
        p("Board and regulator communication requirements vary significantly by jurisdiction.")
        + table(
            ["Region", "Board governance requirements", "Regulator reporting obligations"],
            [
                ["<strong>India</strong>",
                 "RBI MD on IT Governance (Nov 2023): board-approved IT strategy, IT Steering "
                 "Committee, annual review of IT risk. Board must approve outsourcing policy and "
                 "cloud adoption. CISO reports to MD/CEO, with dotted line to board.",
                 "Annual IT examination responses. Cyber incident reports within 6 hours. "
                 "Material outsourcing register. Digital Lending compliance attestation."],
                ["<strong>United Kingdom</strong>",
                 "SM&CR: named Senior Manager for technology (SMF24). Board must set impact "
                 "tolerances for important business services (OpRes). Annual attestation on "
                 "operational resilience readiness (fully embedded from March 2025).",
                 "PRA regulatory returns. Incident notification 'as soon as practicable'. "
                 "s166 responses. CTP regime reporting."],
                ["<strong>Eurozone</strong>",
                 "DORA: management body approves ICT risk management framework, sets digital "
                 "operational resilience strategy. Must have 'sufficient knowledge and skills' "
                 "in ICT risk (training requirement).",
                 "Major ICT incident reports (4h/72h/1mo). ICT third-party register to NCA. "
                 "TLPT/TIBER-EU test results."],
                ["<strong>United States</strong>",
                 "OCC Heightened Standards: board-approved risk appetite for technology. "
                 "FFIEC IT Handbook: board oversight of IT audit, information security programme. "
                 "SOX Section 302/404 CEO/CFO attestation of IT controls.",
                 "SAR filing for cyber incidents. OCC/Fed examination responses. "
                 "NYDFS Part 500 CISO annual report to the board and to NYDFS."],
                ["<strong>Singapore</strong>",
                 "MAS Technology Risk Management Guidelines: board approves technology risk "
                 "management framework. Board must be briefed on material technology incidents "
                 "and technology risk posture.",
                 "MAS incident notification within 1 hour for critical systems. "
                 "Annual technology risk self-assessment."],
            ]
        )
    )
    return TopicSection("6.  Region-by-region governance and reporting overlay", "advanced", body)


# ------------------------------------------------------------------ 7
def _sec7() -> TopicSection:
    return TopicSection(
        "7.  Decision matrix — when and how to communicate", "intermediate",
        table(
            ["Situation", "Who to tell", "When", "Format"],
            [
                ["Major technology investment (>$10M)",
                 "Board or Board Technology Committee",
                 "Before commitment",
                 "Full board paper with options, risk assessment, financial impact"],
                ["Core system migration",
                 "Board + Regulator (proactive engagement)",
                 "6–12 months before go-live",
                 "Board paper for approval. Regulator briefing (presentation + written submission)"],
                ["Material cyber incident",
                 "Board Risk Committee Chair + Regulator + Customers (if affected)",
                 "Board: 1–4 hours. Regulator: per regime timelines",
                 "Factual incident notification. No speculation. Follow-up PIR within 2 weeks"],
                ["Adverse audit finding on technology",
                 "Board Audit Committee + Regulator (if material)",
                 "Next committee cycle",
                 "Finding summary, root cause, remediation plan with dates and owners"],
                ["Cloud strategy adoption",
                 "Board + Regulator",
                 "Before major workload migration",
                 "Strategy paper showing risk assessment, exit plan, data residency compliance"],
                ["Annual technology risk report",
                 "Board Risk Committee",
                 "Annually, aligned to risk appetite review",
                 "Dashboard showing risk appetite metrics, trend, top-5 risks, remediation pipeline"],
                ["Regulator thematic review response",
                 "Regulator supervisory team",
                 "Within stated deadline",
                 "Self-assessment against thematic expectations, gap analysis, remediation timeline"],
            ]
        )
    )


# ------------------------------------------------------------------ 8
def _sec8() -> TopicSection:
    body = (
        example("HDFC Bank — RBI technology upgrade directive",
            p("After a series of outages in 2020–2021 affecting internet banking, mobile banking, "
              "and payment systems, RBI imposed restrictions on HDFC Bank's digital launches and "
              "new credit card issuance in December 2020. The bank was required to submit a "
              "board-approved IT remediation plan. Restrictions were lifted in March 2022 after "
              "the bank demonstrated progress. Lesson: when the regulator loses confidence in "
              "your technology governance, the business impact is immediate and public. The "
              "bank's response — a board-level technology transformation committee, third-party "
              "audit, and structured reporting to RBI — is the template for regulator remediation.")
        )
        + example("Equifax 2017 — Congressional testimony after a breach",
            p("The Equifax data breach (143 million records) led to the CEO testifying before "
              "the US Congress. The testimony revealed that the board had limited visibility into "
              "the security programme's actual posture. The CISO reported three levels below the "
              "CEO. Lesson: board-level reporting lines for security are not bureaucratic overhead; "
              "they are the mechanism by which the board fulfils its fiduciary duty. Post-Equifax, "
              "NYDFS Part 500 was strengthened to require an annual CISO report to the board.")
        )
        + example("Standard Chartered — proactive MAS engagement for digital bank launch",
            p("When Standard Chartered launched Trust (its digital bank in Singapore on the Mambu "
              "platform), the bank engaged MAS early — presenting the technology architecture, "
              "cloud deployment model, operational resilience plan, and exit strategy months before "
              "launch. MAS's Technology Risk Supervision team reviewed the submission in detail. "
              "Lesson: proactive regulator engagement de-risks the launch timeline. MAS did not "
              "impose last-minute conditions because the bank had answered questions before they "
              "were asked.")
        )
        + example("UK bank — s166 review of operational resilience",
            p("A UK bank received a PRA direction to commission a s166 skilled-person review of "
              "its operational resilience framework. The review found that while the bank had "
              "documented impact tolerances, it had not actually tested them against realistic "
              "scenarios. The technology leader had to present remediation to the Board Risk "
              "Committee and PRA within 90 days. Lesson: documentation without evidence of testing "
              "is a finding, not a control.")
        )
        + example("EU bank — DORA ICT incident reporting dry run",
            p("A Eurozone bank conducted a dry run of DORA's new ICT incident reporting "
              "requirements (in force January 2025) six months before the deadline. They "
              "simulated a major ICT incident and tested the 4-hour initial notification, "
              "72-hour intermediate report, and 1-month final report. The exercise revealed "
              "that their internal escalation process added 2 hours of delay, making the "
              "4-hour window impossible. They re-engineered the process. Lesson: test your "
              "communication processes with the same rigour you test your technology.")
        )
    )
    return TopicSection("8.  Worked examples — five real governance and communication stories",
                        "intermediate", body)


# ------------------------------------------------------------------ 9
def _sec9() -> TopicSection:
    body = (
        H3("Questions a leader asks before any board or regulator interaction")
        + ol([
            "What is the decision I am asking the board to make, and is it stated in the "
            "first paragraph?",
            "Have I presented at least two options with honest trade-offs?",
            "Does my risk assessment map to the board's stated risk appetite?",
            "Have I quantified the financial impact (CapEx, OpEx, run-rate) and the cost of "
            "inaction?",
            "Have I anticipated the regulator's likely questions and pre-answered them?",
            "Is there a clear owner and timeline for every action item?",
            "If this is an incident, have I met the notification timeline for every relevant "
            "regulator?",
            "Am I presenting facts I can defend, or opinions I will have to retract?",
            "Does the board member who reads only the executive summary get the right message?",
            "Have I removed all jargon, or at minimum expanded every abbreviation on first use?",
        ])
        + red_flag(ul([
            "'The board doesn't need to understand the technology.' — Under SM&CR, DORA, "
            "RBI IT Governance MD, and OCC Heightened Standards, the board IS required to "
            "understand the technology risk. If they cannot challenge management, you have "
            "a governance failure.",
            "'We'll tell the regulator after go-live.' — For material changes (core migration, "
            "cloud adoption, new product launch), pre-notification is expected in every major "
            "jurisdiction. Surprising your supervisor is the fastest path to a formal review.",
            "'Our incident notification process is email.' — Regulatory notification timelines "
            "(1 hour MAS, 4 hours DORA, 6 hours RBI) require automated escalation, not email "
            "chains. If your process depends on someone checking their inbox at 3 AM, it will fail.",
            "'The CISO reports to the CTO, that's fine.' — Post-Equifax, regulators globally "
            "expect the CISO to have independent reporting access to the board. Burying security "
            "under technology creates a conflict of interest.",
            "'We passed the audit, so we're compliant.' — An audit is a point-in-time sample. "
            "Regulators increasingly expect continuous evidence of control effectiveness, not "
            "annual attestations.",
            "'Board papers should be short.' — Board papers should be as short as possible and "
            "no shorter. A two-page paper on a $200M core migration is not concise; it is "
            "incomplete.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("SM&CR", "Senior Managers and Certification Regime — UK accountability framework "
             "making named individuals personally liable for their areas."),
            ("SMF24", "Senior Management Function 24 — the PRA-designated role for the Chief "
             "Operations function, often covering technology."),
            ("SREP", "Supervisory Review and Evaluation Process — the ECB/SSM's annual "
             "assessment of a bank's risk profile and governance."),
            ("MRA / MRIA", "Matter Requiring Attention / Matter Requiring Immediate Attention — "
             "US regulatory findings with escalating severity."),
            ("s166", "Section 166 of FSMA 2000 — PRA/FCA power to appoint a skilled person to "
             "review a specific area at the firm's cost."),
            ("Dear CEO letter", "Thematic letter from a regulator setting expectations. "
             "Requires a board-acknowledged response."),
            ("Risk appetite statement", "Board-approved quantitative and qualitative expression "
             "of how much risk the institution is willing to take."),
            ("Impact tolerance", "The maximum tolerable disruption to an important business "
             "service, measured in time, data loss, or customer impact."),
            ("Board pack", "The bundle of papers distributed to board members ahead of a "
             "board meeting."),
            ("NED", "Non-Executive Director — board member who does not hold an executive "
             "position. Provides independent oversight and challenge."),
            ("DORA", "Digital Operational Resilience Act — EU regulation (in force January 2025) "
             "governing ICT risk management, incident reporting, and third-party oversight."),
            ("Attestation", "Formal declaration (often by CEO, CFO, or CISO) that a control "
             "or process meets a stated standard."),
            ("Remediation plan", "Structured plan to close a regulatory finding, with actions, "
             "owners, and deadlines."),
            ("CISO annual report", "Required under NYDFS Part 500: the CISO must report annually "
             "to the board on the cybersecurity programme."),
            ("Thematic review", "Regulator-led cross-industry examination of a specific topic "
             "(e.g., operational resilience, cloud, AI)."),
        ])
    )
    return TopicSection("9.  Questions, red flags, and glossary", "basic", body)
