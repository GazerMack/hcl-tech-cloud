"""Leadership Lenses · 01 — Architecture decision frameworks for techno-
functional leaders."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="VII.1",
        slug="01-architecture-decision-frameworks",
        title="Architecture decision frameworks for techno-functional leaders",
        one_liner=(
            "Senior leaders in BFSI technology are not paid to write code; "
            "they are paid to make a small number of consequential decisions "
            "well, and then to defend them under audit, regulator scrutiny "
            "and market change. This topic gives you the named frameworks "
            "leaders use to make those decisions: ADRs and the lightweight "
            "documentation discipline; fitness functions for evolutionary "
            "architecture; Wardley mapping for strategic positioning; build-"
            "vs-buy-vs-partner; the TOGAF and BIAN reference models; the "
            "‘capability map’ way of looking at a bank; and the rituals — "
            "ARBs, design authorities, principal-engineer reviews — that "
            "turn decisions into outcomes."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("Most architecture decisions a BFSI leader regrets in "
              "year three were made in a hurry in year one with no "
              "written rationale. The discipline is not bigger "
              "models; it is making the consequential decisions "
              "<em>visible</em>, <em>reversible-where-possible</em>, "
              "and <em>tested in production-like conditions</em> "
              "before they become irreversible.")
        )
        + H3("0.1  IT-side anchor — the architect as a town planner")
        + it_anchor(
            p("Architects often imagine themselves as building "
              "designers. A more honest analogy is the <strong>town "
              "planner</strong>: deciding where roads, water, "
              "schools and zoning go, not what the houses look "
              "like. You don’t design every house; you decide the "
              "rules under which thousands of houses can be built "
              "without grinding traffic to a halt or flooding the "
              "drains. Capability maps are zoning. ADRs are "
              "planning permissions. Fitness functions are the "
              "noise and traffic limits.")
        )
        + H3("0.2  BFSI-side anchor — the credit committee for technology")
        + bfsi_anchor(
            p("Banks already know how to make consequential "
              "decisions: the credit committee. A loan is "
              "presented with a clear summary, an explicit risk "
              "rating, comparable cases, dissenting views, and a "
              "post-decision review schedule. Architecture "
              "decisions deserve exactly the same discipline. An "
              "ADR (Architecture Decision Record) is the credit "
              "memo for a technical decision. An ARB "
              "(Architecture Review Board) is the credit "
              "committee. The post-decision review is the same.")
        )
        + H3("0.3  Five frameworks worth memorising")
        + ul([
            "<strong>ADR — Architecture Decision Record.</strong> "
            "Lightweight markdown, version-controlled, one decision "
            "per file. Michael Nygard 2011.",
            "<strong>Fitness functions.</strong> Automated, "
            "continuous tests of architectural properties. "
            "Neal Ford / Rebecca Parsons / Patrick Kua, "
            "<em>Building Evolutionary Architectures</em>.",
            "<strong>Wardley mapping.</strong> Strategic "
            "positioning of components on a value-chain × "
            "evolution map. Simon Wardley.",
            "<strong>TOGAF and BIAN.</strong> The Open Group "
            "Architecture Framework + Banking Industry "
            "Architecture Network — the BFSI reference models "
            "regulators and partners speak.",
            "<strong>Capability mapping.</strong> A flat, "
            "verb-free map of <em>what</em> the bank does. "
            "Used to locate every technology investment "
            "against a stable business shape.",
        ])
    )
    return TopicSection(
        "0.  Primer — leaders make decisions, not designs",
        "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Why does this topic deserve its own chapter rather than a "
            "footnote in IV.1?")
        + ol([
            "<strong>The cost of bad architecture decisions in "
            "BFSI is asymmetric.</strong> A poor microservice "
            "boundary at a fintech is annoying; at a tier-1 bank "
            "it is a 200-FTE programme. Small numbers of "
            "decisions drive most outcomes.",
            "<strong>Regulators now expect documented "
            "rationale.</strong> DORA, RBI IT Governance MD, MAS "
            "TRM, NYDFS Part 500 expect to see <em>why</em> a "
            "bank chose its critical-third-party vendor, not just "
            "<em>that</em> it did.",
            "<strong>AI is amplifying the consequences.</strong> "
            "An ML model embedded in credit, fraud or pricing is "
            "an architecture decision; the EU AI Act asks for the "
            "lifecycle paper trail.",
            "<strong>Talent attrition is real.</strong> Without "
            "ADRs the institution forgets why; the next leader "
            "rebuilds the same room.",
            "<strong>Cost discipline.</strong> Build-vs-buy and "
            "build-vs-partner choices made well save 9-figure "
            "sums over a decade.",
        ])
    )
    return TopicSection(
        "1.  Why frameworks are the leadership job, not the engineering job",
        "basic", body)


def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  subgraph "Strategic"\n'
            '    Cm["Capability map<br/>what the bank does"]\n'
            '    Wm["Wardley map<br/>where each component is on its lifecycle"]\n'
            '    BvB["Build / buy / partner<br/>decision frame"]\n'
            '  end\n'
            '  subgraph "Tactical"\n'
            '    A["ADRs<br/>one decision per file"]\n'
            '    Ff["Fitness functions<br/>continuous architecture tests"]\n'
            '    Sd["Sequence diagrams<br/>C4 model context, container, component"]\n'
            '  end\n'
            '  subgraph "Governance"\n'
            '    AR["ARB / design authority"]\n'
            '    PR["Principal-engineer / staff-plus reviews"]\n'
            '    PM["Post-implementation reviews"]\n'
            '  end\n'
            '  Cm --> Wm --> BvB\n'
            '  BvB --> A\n'
            '  A --> Ff\n'
            '  A --> Sd\n'
            '  A --> AR\n'
            '  AR --> PR\n'
            '  PR --> PM',
            "Three layers of architecture work: strategic framing, "
            "tactical decisions, and governance rituals.")
    )
    return TopicSection(
        "2.  The picture — strategic, tactical, governance",
        "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  ADRs — Architecture Decision Records")
        + p("An ADR is a short markdown file with a fixed shape:")
        + ul([
            "<strong>Title</strong> and number (ADR-0042).",
            "<strong>Status</strong> — proposed, accepted, "
            "deprecated, superseded by ADR-0083.",
            "<strong>Context</strong> — what forces are at play; "
            "what we know; what we don’t.",
            "<strong>Decision</strong> — what we will do, in one or "
            "two sentences.",
            "<strong>Consequences</strong> — what becomes easier; "
            "what becomes harder; what is no longer true.",
        ])
        + p("ADRs live in the source repository, beside the code; "
            "review happens in pull requests; status is owned by "
            "principal engineers. Tools: <strong>adr-tools</strong> "
            "(Nat Pryce), <strong>adr-manager</strong>, <strong>"
            "Backstage TechDocs</strong>, <strong>Structurizr</strong> "
            "(Simon Brown).")
        + H3("3.2  C4 model — communicate at four zoom levels")
        + ul([
            "<strong>Level 1 — System Context</strong>: the system "
            "and the people / systems it interacts with.",
            "<strong>Level 2 — Container</strong>: applications and "
            "data stores inside the system boundary.",
            "<strong>Level 3 — Component</strong>: significant "
            "components inside a container.",
            "<strong>Level 4 — Code</strong>: optional; class or "
            "module-level diagrams.",
        ])
        + p("The C4 model (Simon Brown, 2018+) replaced UML in most "
            "BFSI shops because it has only four diagram types and "
            "is easy to keep up to date.")
        + H3("3.3  Fitness functions — architecture as code")
        + p("A fitness function is an automated test of an "
            "architectural property. Examples used in practice in "
            "BFSI:")
        + ul([
            "Every public API has an OpenAPI spec; CI fails if "
            "missing.",
            "No service depends on more than 3 downstream "
            "services synchronously (limit fan-out).",
            "P99 latency on the payments hub stays under "
            "500 ms in production-like load.",
            "Every container image carries an SBOM and a "
            "Sigstore signature.",
            "No PII column in the data lake without a tag and a "
            "tokenisation status.",
            "Cost per transaction trends downward week-on-week "
            "(FinOps fitness function).",
        ])
        + p("Fitness functions live in CI / observability; failures "
            "are tickets, not opinions. Reference: Neal Ford et al., "
            "<em>Building Evolutionary Architectures</em> (2017, 2nd "
            "ed. 2023).")
        + H3("3.4  Wardley mapping — where on the lifecycle is each component?")
        + p("A Wardley map plots components of a value chain on two "
            "axes: <strong>visibility to the user</strong> (vertical) "
            "and <strong>evolution stage</strong> (horizontal: "
            "Genesis → Custom-built → Product/Rental → Commodity / "
            "Utility). The discipline forces you to ask: ‘should "
            "this still be custom-built or is it now a utility?’ — "
            "the question that decides whether you build, buy or "
            "consume Postgres / K8s / observability.")
        + H3("3.5  Build vs buy vs partner — the named lenses")
        + table(
            ["Question", "Build", "Buy", "Partner / SaaS"],
            [
                ["Differentiator?",
                 "Yes — it is the moat",
                 "No — it is table stakes",
                 "No — but it is mission-critical"],
                ["Skills available?",
                 "Yes, sustained",
                 "No, or transient",
                 "Variable; partner provides"],
                ["Pace of change?",
                 "Fast and ours to set",
                 "Slow; vendor cadence is fine",
                 "Fast but driven by vendor"],
                ["Regulator stance?",
                 "Documented build-quality controls",
                 "Vendor due diligence",
                 "DORA / CTP exit-plan needed"],
                ["Total cost over 10 years?",
                 "High up-front, lower run-rate at scale",
                 "Predictable licence",
                 "Variable; consumption-based"],
            ]
        )
        + H3("3.6  Capability mapping — the bank as a flat list")
        + p("A capability map says <em>what</em> the bank does in "
            "verb-free language: ‘Customer Onboarding’, "
            "‘Counterparty Credit Assessment’, ‘Cash Management’, "
            "‘Claims Adjudication’. Capabilities are stable for "
            "decades; processes, products and systems shift "
            "constantly. The map is the canvas onto which every "
            "investment, every regulator finding and every vendor "
            "is plotted. <strong>BIAN</strong> (Banking Industry "
            "Architecture Network) publishes a reference "
            "capability and service-domain map for banking; "
            "<strong>ACORD</strong> publishes the equivalent for "
            "insurance.")
        + H3("3.7  TOGAF, BIAN, ACORD — when the words matter")
        + ul([
            "<strong>TOGAF</strong> (Open Group, currently TOGAF 10 "
            "/ 2022) — generic enterprise architecture method "
            "(ADM); known as much for its certification as for "
            "its content; useful as a shared vocabulary.",
            "<strong>BIAN</strong> — banking-specific service "
            "domains; the bank already speaks this when "
            "discussing vendors and APIs.",
            "<strong>ACORD</strong> — insurance-specific "
            "vocabulary, message standards and capability maps.",
            "<strong>IFW (IBM)</strong>, <strong>Oracle Reference "
            "Models</strong>, <strong>Capgemini Sefas</strong> — "
            "vendor-specific reference architectures often used "
            "alongside.",
        ])
        + H3("3.8  ARB, design authority and principal-engineer reviews")
        + ul([
            "<strong>Architecture Review Board (ARB)</strong> — "
            "monthly or fortnightly forum; decisions above a "
            "threshold (cost, regulator impact, cross-domain "
            "scope) need ARB approval; minutes are an audit "
            "artifact.",
            "<strong>Design Authority</strong> — programme-level "
            "version of the ARB for a single change programme.",
            "<strong>Principal-engineer / staff-plus reviews</strong> "
            "— peer review for technical depth; often the more "
            "useful of the two.",
            "<strong>Pre-mortem</strong> — before commitment, ask "
            "‘imagine this has failed in 18 months — what "
            "happened?’. Cheap, surprisingly effective.",
            "<strong>Post-implementation review (PIR)</strong> — "
            "did the decision deliver the consequences we "
            "predicted? Feeds the ADR status.",
        ])
    )
    return TopicSection(
        "3.  How leaders use these frameworks day to day",
        "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  How banks worldwide actually run this")
        + ul([
            "<strong>JPMorgan Chase</strong> — published <em>"
            "Engineering Standards</em>, golden paths, internal "
            "developer platform; ‘paved roads’ for cloud, "
            "Kubernetes, data; principal-engineer ladder is "
            "highly visible.",
            "<strong>Goldman Sachs</strong> — Marquee + "
            "developer-platform discipline; SecDB heritage of "
            "‘one platform for everything’ with explicit "
            "trade-offs.",
            "<strong>Capital One</strong> — Cloud Custodian, "
            "Hygieia, public ADR-style engineering blog; "
            "early adopter of fitness-function thinking.",
            "<strong>ING</strong> — squads / tribes / chapters "
            "model; design authorities at programme level.",
            "<strong>Standard Chartered</strong> — ‘aXess’ "
            "developer platform, internal architecture council; "
            "HCLTech is one of several partners contributing "
            "components.",
            "<strong>HDFC Bank, ICICI Bank, Axis Bank</strong> — "
            "internal architecture committees; recent build-out "
            "of ADR practice and capability maps; "
            "modernisation-board governance.",
        ])
        + H3("4.2  Regulator expectations on architecture governance")
        + ul([
            "<strong>RBI IT Governance MD (Nov 2023)</strong> — "
            "expects ‘board-approved IT strategy and architecture’; "
            "ARBs and capability maps are a clean way to evidence "
            "this.",
            "<strong>EU DORA Article 6</strong> — ‘ICT risk "
            "management framework’ shall include the ‘ICT "
            "architecture’ and a clear assignment of "
            "responsibilities.",
            "<strong>FCA / PRA</strong> — Senior Managers and "
            "Certification Regime (SMCR) means an SMF24 has "
            "personal accountability for ‘systems and controls’; "
            "documented architecture decisions help.",
            "<strong>NYDFS Part 500.4</strong> — CISO "
            "certification implies an ability to describe the "
            "architecture under oath.",
            "<strong>MAS TRM Section 4.1</strong> — board and "
            "senior management to approve a technology risk "
            "framework that includes architecture.",
        ])
    )
    return TopicSection(
        "4.  Region by region — how banks run this and what "
        "regulators expect",
        "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  Anti-patterns to name and refuse")
        + ul([
            "<strong>Architecture astronaut</strong> — diagrams "
            "without rationale; ADR-less decisions; ‘we’re going "
            "to standardise on a service mesh’ without a problem "
            "statement.",
            "<strong>Resume-driven development</strong> — picking "
            "technology because it looks good on a CV. Common "
            "with shiny ML, blockchain, mesh tools.",
            "<strong>Big-bang re-platform</strong> — ‘we’ll "
            "rewrite the core in three years’. Almost always "
            "extends to seven; strangler-fig is the default.",
            "<strong>Vendor capture</strong> — sole-source "
            "decisions made informally; no ADR; no exit clause.",
            "<strong>Decision by committee with no owner</strong> "
            "— ‘the ARB decided’ becomes ‘nobody decided’.",
            "<strong>Premature standardisation</strong> — "
            "freezing a stack before the first three "
            "implementations have shaken out.",
            "<strong>Architecture without operations</strong> — "
            "diagrams that ignore SRE, FinOps, identity, "
            "observability.",
        ])
        + H3("5.2  Patterns to embed and defend")
        + ul([
            "<strong>Strangler-fig migrations</strong> — wrap, "
            "redirect, retire; never big-bang.",
            "<strong>Two-pizza teams + bounded contexts</strong> "
            "— Conway’s Law respected on purpose.",
            "<strong>Outcome-based SLOs</strong> — measure "
            "important business services, not "
            "‘server availability’.",
            "<strong>Crypto-agility</strong> — pluggable "
            "primitives; PQC migration becomes a configuration.",
            "<strong>Data products with owners</strong> — data "
            "mesh discipline; SLAs on data quality and "
            "freshness.",
            "<strong>Paved roads</strong> — golden paths in the "
            "Internal Developer Platform; teams can deviate but "
            "they own the cost.",
            "<strong>Reversibility-first decisions</strong> — "
            "Bezos ‘two-way doors’; treat reversible decisions "
            "lightly, irreversible ones rigorously.",
        ])
        + H3("5.3  Cost-discipline patterns")
        + ul([
            "<strong>Unit economics</strong> — cost per "
            "transaction, per customer, per API call. The "
            "FinOps fitness function.",
            "<strong>Run-cost in design</strong> — budget for "
            "5-year run cost when approving a build; show the "
            "envelope at the ARB.",
            "<strong>Sunset budgets</strong> — every project "
            "must propose what it retires.",
            "<strong>Vendor portfolio review</strong> — annual "
            "review of redundant or sub-scale vendors; "
            "conscious consolidation.",
        ])
        + H3("5.4  AI-era additions to the toolkit")
        + ul([
            "<strong>Model registry as architecture asset</strong> "
            "— every model is a component of the architecture, "
            "not a side project.",
            "<strong>Data lineage as a non-negotiable</strong> — "
            "OpenLineage, Unity Catalog, Marquez; auditors and "
            "AI agents both want it.",
            "<strong>Prompt and evaluation governance</strong> — "
            "treat prompts and eval suites like code; ADRs "
            "for major prompt-strategy changes.",
            "<strong>Human-in-the-loop is a requirement, not a "
            "nicety</strong> — under EU AI Act, FCA Consumer "
            "Duty, MAS FEAT, RBI guidance.",
        ])
    )
    return TopicSection(
        "5.  Advanced — patterns, anti-patterns, cost discipline, "
        "AI era",
        "advanced", body)


def _sec6() -> TopicSection:
    body = (
        H3("6.1  When to use which framework")
        + table(
            ["Question on the table", "Use this", "Why"],
            [
                ["Should we build, buy or partner?",
                 "Wardley map + build/buy lenses + ADR",
                 "Forces the lifecycle question and writes the "
                 "rationale down."],
                ["Where should this new capability sit?",
                 "Capability map + BIAN / ACORD reference",
                 "Locates the investment against a stable "
                 "business shape."],
                ["Is the architecture deviating from intent?",
                 "Fitness functions in CI",
                 "Continuous, automated, blame-free."],
                ["How do we explain the system to the board?",
                 "C4 Level 1 + 2",
                 "Two diagrams everyone can read."],
                ["How do we evidence governance to a regulator?",
                 "ADRs + ARB minutes + PIR + capability map",
                 "Documented, traceable, defensible."],
                ["Why did we pick this vendor over the others?",
                 "ADR + decision matrix + exit plan",
                 "Required by DORA / RBI / PRA / MAS / NYDFS."],
                ["Is this a reversible decision?",
                 "Two-way / one-way door framing",
                 "Save oxygen for the irreversible ones."],
            ]
        )
        + H3("6.2  Decision matrix — picking your governance cadence")
        + table(
            ["Programme size", "Cadence", "Forum"],
            [
                ["Single squad / change",
                 "Per pull request",
                 "Principal-engineer review."],
                ["Bounded context / domain",
                 "Weekly",
                 "Domain architecture forum."],
                ["Cross-domain / programme",
                 "Fortnightly",
                 "Programme design authority."],
                ["Bank-wide / regulator-visible",
                 "Monthly",
                 "ARB; minutes filed; PIR scheduled."],
            ]
        )
    )
    return TopicSection(
        "6.  Decision matrices — when to use which framework",
        "intermediate", body)


def _sec7() -> TopicSection:
    body = (
        example(
            "Capital One — public-facing engineering practices",
            ol([
                "Capital One open-sourced Cloud Custodian and "
                "Hygieia and published its engineering principles; "
                "its post-2019 breach reviews fed visible changes "
                "(IMDSv2, least-privilege IAM by default).",
                "Public lessons: visible principles + open tooling "
                "+ explicit post-incident learnings make a culture "
                "you can hire into.",
            ])
        )
        + example(
            "JPM ‘paved road’ for cloud and data",
            ol([
                "JPM publishes internal Engineering Standards; "
                "developer platform with ‘paved roads’ for AWS, "
                "Kubernetes, OpenSearch, Snowflake; deviations "
                "require an explicit ADR and exit plan.",
                "Lessons: paved roads + opt-out discipline scales "
                "150,000 engineers; total platform standardisation "
                "is impossible at that size; explicit deviation "
                "is the answer.",
            ])
        )
        + example(
            "ING Tribes / Squads / Chapters",
            ol([
                "ING reorganised IT around the Spotify-derived "
                "tribes / squads / chapters model from 2015 with "
                "design authorities at the programme level "
                "rather than centralised.",
                "Public lessons: distribute decisions to the "
                "domain; keep cross-cutting concerns in chapters "
                "(security, data, SRE).",
            ])
        )
        + example(
            "Indian incumbent — modernisation-board governance",
            ol([
                "A tier-1 Indian private bank stood up a "
                "modernisation board with CTO + Chief Risk + "
                "Chief Compliance + business heads; reviewed all "
                "investments above ₹50 Cr.",
                "Adopted lightweight ADRs (markdown in GitHub "
                "Enterprise); ARB cadence monthly; PIR three "
                "months post-go-live.",
                "Lessons: senior cross-functional governance is "
                "the lever; tooling follows.",
            ])
        )
        + example(
            "EU bank for DORA — written architecture story",
            ol([
                "EU bank prepared for DORA by writing a single "
                "‘architecture story’: capability map, level-1 "
                "C4 of every important business service, ADR "
                "register, fitness-function dashboard, exit "
                "plan per critical ICT third party.",
                "Result: regulator review reduced from a 6-month "
                "discovery to a 6-week confirmation.",
            ])
        )
    )
    return TopicSection(
        "7.  Worked examples — five real architecture-governance "
        "stories",
        "intermediate", body)


def _sec8() -> TopicSection:
    return TopicSection(
        "8.  Questions a leader asks of any architecture review",
        "basic",
        ol([
            "Is the decision in writing as an ADR with status, "
            "context, decision, consequences?",
            "Have we plotted the relevant capabilities on the "
            "BIAN / ACORD / capability map and located the "
            "investment correctly?",
            "Where on the Wardley evolution axis is each "
            "component, and is build / buy / partner aligned?",
            "What fitness functions express the architectural "
            "properties we care about, and are they running in "
            "CI / observability?",
            "Is this a reversible (two-way door) or irreversible "
            "decision, and have we calibrated rigour "
            "accordingly?",
            "What is the exit plan from each critical vendor / "
            "cloud / SaaS in this scope?",
            "Who is the SMF / responsible officer, and is their "
            "name on the decision?",
            "How does the design respect Conway’s Law — does it "
            "match the team topology we have or the one we are "
            "willing to build?",
            "What is the run-cost projection over five years, "
            "and is FinOps embedded?",
            "What is the post-implementation review schedule, "
            "and what would change our minds?",
            "How does the design handle PQC migration, AI "
            "Act / FEAT obligations, and operational resilience "
            "scenarios?",
            "If a regulator walks in tomorrow and asks for the "
            "architecture, can we hand them one document?",
        ]))


def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘We don’t need ADRs, the team knows the rationale.’ "
            "— The team will turn over by year three. Future "
            "leaders will inherit decisions they cannot defend.",
            "‘Our ARB approves everything.’ — A 100% approval "
            "rate is a signal the ARB is theatre.",
            "‘Fitness functions are nice-to-have.’ — Without "
            "them, architectural intent decays silently and is "
            "discovered in audits.",
            "‘Wardley maps are too abstract.’ — They take 90 "
            "minutes to learn and routinely change build/buy "
            "decisions worth millions.",
            "‘TOGAF / BIAN / ACORD are paperwork.’ — They are "
            "shared vocabulary with regulators and partners; "
            "use them lightly, but use them.",
            "‘We picked the vendor because they were the "
            "incumbent.’ — Without an ADR documenting the "
            "alternatives, this is failed governance under "
            "DORA / RBI / PRA.",
            "‘The ARB owns the decision.’ — A committee cannot "
            "be held to account. An individual SMF / officer "
            "must own each consequential decision.",
            "‘Diagrams are outdated, ignore them.’ — Then "
            "remove them. Stale diagrams are worse than no "
            "diagrams.",
            "‘AI doesn’t need architectural review.’ — Models "
            "are components; data flows are integrations; "
            "regulators are watching.",
            "‘Architecture is what the architect does.’ — "
            "Architecture is what the system <em>is</em>. The "
            "architect documents and shapes it.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("ADR", "Architecture Decision Record — markdown "
                "file with status, context, decision, "
                "consequences."),
            ("C4 model", "Context / Container / Component / Code "
                "diagrams (Simon Brown)."),
            ("Fitness function", "Automated test of an "
                "architectural property (Ford / Parsons / Kua)."),
            ("Wardley map", "Strategic positioning of "
                "components on value-chain × evolution axes."),
            ("Build / buy / partner", "The named option set "
                "for major capability decisions."),
            ("Capability map", "Verb-free, stable list of what "
                "the bank does."),
            ("BIAN", "Banking Industry Architecture Network — "
                "service-domain reference for banks."),
            ("ACORD", "Association for Cooperative Operations "
                "Research and Development — insurance reference "
                "and message standards."),
            ("TOGAF", "The Open Group Architecture Framework — "
                "EA method (currently TOGAF 10)."),
            ("ARB", "Architecture Review Board — governance "
                "forum for consequential decisions."),
            ("Design Authority", "Programme-level architecture "
                "governance forum."),
            ("Principal-engineer / staff-plus review", "Peer "
                "review for technical depth."),
            ("PIR", "Post-Implementation Review — did the "
                "decision deliver?"),
            ("Pre-mortem", "‘Imagine this has failed in 18 "
                "months — why?’ exercise."),
            ("Strangler-fig", "Incremental migration pattern "
                "(Martin Fowler)."),
            ("Two-way door / one-way door", "Reversible vs "
                "irreversible decision framing (Bezos)."),
            ("Paved road / golden path", "Recommended platform "
                "configuration in an Internal Developer "
                "Platform."),
            ("Conway’s Law", "‘System designs mirror "
                "communication structures.’ Plan team topology "
                "deliberately."),
            ("Team Topologies", "Stream-aligned / platform / "
                "enabling / complicated-subsystem teams "
                "(Skelton & Pais)."),
            ("Reference architecture", "Vendor or standards-body "
                "blueprint (BIAN, ACORD, IBM IFW, AWS Well-"
                "Architected, Azure Well-Architected, Google "
                "Cloud Architecture Framework, OCI Well-"
                "Architected)."),
            ("SMF / SMCR", "Senior Manager Function under UK "
                "Senior Managers and Certification Regime."),
            ("DORA Article 6", "Requires an ICT risk management "
                "framework with explicit architecture and "
                "responsibilities."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
