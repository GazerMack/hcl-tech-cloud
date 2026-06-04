"""Orchestrator: builds the entire BFSI Bible site.

Run from `C:\\Users\\gazer\\Downloads\\hcl tech cloud`:
    python -m bfsi_bible_src.generate
"""
from __future__ import annotations

from .site import (
    Part, SiteIndex, TopicLink, page_shell, write_site,
    H1, H2, H3, p, ul, lead, callout,
)
from .topics import (
    foundations_01_transactions_v2 as foundations_01_transactions,
    foundations_02_seven_layers,
    foundations_03_cloud,
    foundations_04_network,
    application_stack_01_apis,
    application_stack_02_microservices,
    data_01_databases,
    data_02_streaming,
    infra_ops_01_cloud_native,
    infra_ops_02_devops_sre,
    security_risk_01_security_identity,
    security_risk_02_fraud_aml,
    bfsi_platforms_01_core_banking,
    bfsi_platforms_02_payments_engines,
    bfsi_platforms_03_lending,
    bfsi_platforms_04_capmkts_insurance,
    leadership_01_architecture_decisions,
    leadership_02_vendor_programme,
)


# --------------------------------------------------------------- index

def build_index() -> SiteIndex:
    parts = [
        Part(roman="I", folder="foundations", name="Foundations",
             subtitle="The banker’s IT map",
             blurb=("How BFSI tech actually behaves. Read these first — they are the spine of "
                    "everything that follows. Zero IT background assumed."),
             topics=[
                 TopicLink("01-transactions",      "Transaction flow",          "I.1"),
                 TopicLink("02-seven-layers",      "Seven-layer mental model",  "I.2"),
                 TopicLink("03-cloud-and-infra",   "Cloud, on-prem, hybrid",    "I.3"),
                 TopicLink("04-network-fundamentals", "Network fundamentals",   "I.4"),
             ]),
        Part(roman="II", folder="application-stack", name="Application Stack",
             subtitle="How banking software is built",
             blurb=("Frontend, backend languages and runtimes, microservices and Domain-Driven "
                    "Design, APIs and integration, middleware and messaging."),
             topics=[
                 TopicLink("01-apis-and-integration",
                           "APIs and integration", "II.1"),
                 TopicLink("02-microservices-monoliths-ddd",
                           "Microservices, monoliths, DDD", "II.2"),
             ]),
        Part(roman="III", folder="data", name="Data",
             subtitle="Where banks keep their truth",
             blurb=("Online Transaction Processing (OLTP), NoSQL, streaming data, event-driven "
                    "architecture, warehousing, analytics, AI and ML."),
             topics=[
                 TopicLink("01-databases-and-the-ledger",
                           "Databases & the ledger", "III.1"),
                 TopicLink("02-streaming-data-event-driven-architecture",
                           "Streaming data & event-driven architecture", "III.2"),
             ]),
        Part(roman="IV", folder="infra-ops", name="Infrastructure & Operations",
             subtitle="Where software runs",
             blurb=("Cloud, containers and Kubernetes, networking, DevOps, observability, FinOps."),
             topics=[
                 TopicLink("01-cloud-native-operations",
                           "Cloud-native operations", "IV.1"),
                 TopicLink("02-devops-sre-deep",
                           "DevOps & SRE in depth", "IV.2"),
             ]),
        Part(roman="V", folder="security-risk", name="Security, Risk & Compliance",
             subtitle="The trust stack",
             blurb=("Identity, cryptography, application security, the regulator landscape line "
                    "by line, BCP and disaster recovery."),
             topics=[
                 TopicLink("01-security-identity-regulators",
                           "Security, identity & regulators", "V.1"),
                 TopicLink("02-fraud-aml-sanctions",
                           "Fraud, AML & sanctions in depth", "V.2"),
             ]),
        Part(roman="VI", folder="bfsi-platforms", name="BFSI Domain Platforms",
             subtitle="The vendor estate",
             blurb=("Core banking, lending, payments rails, capital markets, insurance, "
                    "mainframe modernisation."),
             topics=[
                 TopicLink("01-core-banking-platforms",
                           "Core banking platforms", "VI.1"),
                 TopicLink("02-payments-engines",
                           "Payments engines", "VI.2"),
                 TopicLink("03-lending-and-originations",
                           "Lending & originations", "VI.3"),
                 TopicLink("04-capmkts-and-insurance",
                           "Capital markets & insurance", "VI.4"),
             ]),
        Part(roman="VII", folder="leadership", name="Leadership Lenses",
             subtitle="Deciding & architecting",
             blurb=("Enterprise architecture, build-vs-buy, vendor management, decision "
                    "frameworks for techno-functional leaders."),
             topics=[
                 TopicLink("01-architecture-decision-frameworks",
                           "Architecture decision frameworks", "VII.1"),
                 TopicLink("02-vendor-management-and-programme-delivery",
                           "Vendor management & programme delivery", "VII.2"),
             ]),
    ]
    return SiteIndex(parts=parts)


# --------------------------------------------------------------- pages

def home_html(idx: SiteIndex) -> str:
    parts_summary = ul([
        f"<strong>{p.roman} — {p.name}.</strong> <em>{p.subtitle}.</em> {p.blurb}"
        for p in idx.parts
    ])
    return (
        H1("BFSI Techno-Functional Leader Bible")
        + lead("A self-contained, zero-assumption reference that takes you from MBA-Finance to "
               "fluent senior techno-functional leader in BFSI. Every topic starts from things "
               "you already know — the laptop in front of you and the banking apps you use — and "
               "climbs all the way to what a senior architect at Citi, Standard Chartered, "
               "Deutsche Bank, Barclays, NatWest, JPM or Wells Fargo debates in design reviews.")
        + callout("How to use this bible",
            ul([
                "Read sequentially the first time — Parts I → VII build on each other.",
                "After that, jump in via the sidebar or use the search box at the top of the sidebar.",
                "Every term is hover-tipped on first use; the consolidated glossary lives in the sidebar.",
                "Each section is tagged <span class='pill pill-basic'>Basic</span>, "
                "<span class='pill pill-inter'>Intermediate</span>, or "
                "<span class='pill pill-advanced'>Advanced</span> so you can pace yourself.",
                "To make a PDF: open any page in Chrome / Edge → Print → Save as PDF "
                "(the print stylesheet is tuned).",
            ]),
            "info")
        + H2("What is in each Part")
        + parts_summary
        + H2("Status of this draft")
        + p("This is the v1.14 build. The original core curriculum is complete across "
            "Foundations, Application Stack, Data, Infrastructure & Operations, Security, "
            "BFSI Domain Platforms and Leadership Lenses. Stretch topics now include: "
            "<code>I.4 — Network fundamentals</code>, <code>III.2 — Streaming data "
            "and event-driven architecture</code>, <code>IV.2 — DevOps & SRE in depth</code>, "
            "and <code>V.2 — Fraud, AML & sanctions in depth</code>. "
            "The May 2026 deep rewrite of <code>I.1 — transaction flow</code> is complete. "
            "The finalised pedagogy remains: dual-anchor primer, geographic balance, worked "
            "examples with numbers and explicit abbreviation discipline.")
    )


def glossary_html() -> str:
    return (
        H1("Glossary")
        + lead("A consolidated index of every technical term introduced anywhere in the bible. "
               "Each topic carries its own local glossary at the end, with hover tooltips used "
               "throughout the pages for first-use explanations. Use this page as the shared "
               "entry point, then jump into the topic-level glossaries for deeper context.")
    )


def part_overview(part: Part) -> str:
    body = (
        H1(f"{part.roman} — {part.name}")
        + lead(f"<strong>{part.subtitle}.</strong> {part.blurb}")
    )
    if part.topics:
        body += H2("Topics in this Part")
        body += ul([
            f"<a href='{t.slug}.html'><strong>{t.code}</strong> — {t.title}</a>"
            for t in part.topics
        ])
    else:
        body += callout("Coming next",
            p(f"Topics for Part {part.roman} ({part.name}) will be generated in the next "
              "iteration once Topic I.1 has been validated."), "info")
    return body


# --------------------------------------------------------------- main

def main() -> None:
    idx = build_index()
    pages: list[tuple] = []

    for part in idx.parts:
        pages.append((
            f"{part.folder}/index.html",
            f"{part.roman} — {part.name}",
            part_overview(part),
            None, None,
        ))

    # Foundations (Part I)
    found_topics = [
        foundations_01_transactions.build(),
        foundations_02_seven_layers.build(),
        foundations_03_cloud.build(),
        foundations_04_network.build(),
    ]
    for i, t in enumerate(found_topics):
        prev_l = (("index.html", "Foundations overview")
                  if i == 0
                  else (f"{found_topics[i-1].slug}.html", found_topics[i-1].title))
        next_l = ((f"{found_topics[i+1].slug}.html", found_topics[i+1].title)
                  if i + 1 < len(found_topics) else None)
        pages.append((f"foundations/{t.slug}.html", t.title, t.to_html(), prev_l, next_l))

    # Application stack (Part II)
    app_topics = [
        application_stack_01_apis.build(),
        application_stack_02_microservices.build(),
    ]
    for i, t in enumerate(app_topics):
        prev_l = (("index.html", "Application stack overview")
                  if i == 0
                  else (f"{app_topics[i-1].slug}.html", app_topics[i-1].title))
        next_l = ((f"{app_topics[i+1].slug}.html", app_topics[i+1].title)
                  if i + 1 < len(app_topics) else None)
        pages.append((f"application-stack/{t.slug}.html", t.title, t.to_html(),
                      prev_l, next_l))

    # Data (Part III)
    data_topics = [
        data_01_databases.build(),
        data_02_streaming.build(),
    ]
    for i, t in enumerate(data_topics):
        prev_l = (("index.html", "Data overview")
                  if i == 0
                  else (f"{data_topics[i-1].slug}.html", data_topics[i-1].title))
        next_l = ((f"{data_topics[i+1].slug}.html", data_topics[i+1].title)
                  if i + 1 < len(data_topics) else None)
        pages.append((f"data/{t.slug}.html", t.title, t.to_html(),
                      prev_l, next_l))

    # Infrastructure & Operations (Part IV)
    infra_topics = [infra_ops_01_cloud_native.build(), infra_ops_02_devops_sre.build()]
    for i, t in enumerate(infra_topics):
        prev_l = (("index.html", "Infra & Ops overview")
                  if i == 0
                  else (f"{infra_topics[i-1].slug}.html", infra_topics[i-1].title))
        next_l = ((f"{infra_topics[i+1].slug}.html", infra_topics[i+1].title)
                  if i + 1 < len(infra_topics) else None)
        pages.append((f"infra-ops/{t.slug}.html", t.title, t.to_html(),
                      prev_l, next_l))

    # Security, Risk & Compliance (Part V)
    sec_topics = [security_risk_01_security_identity.build(), security_risk_02_fraud_aml.build()]
    for i, t in enumerate(sec_topics):
        prev_l = (("index.html", "Security & Risk overview")
                  if i == 0
                  else (f"{sec_topics[i-1].slug}.html", sec_topics[i-1].title))
        next_l = ((f"{sec_topics[i+1].slug}.html", sec_topics[i+1].title)
                  if i + 1 < len(sec_topics) else None)
        pages.append((f"security-risk/{t.slug}.html", t.title, t.to_html(),
                      prev_l, next_l))

    # BFSI domain platforms (Part VI)
    plat_topics = [
        bfsi_platforms_01_core_banking.build(),
        bfsi_platforms_02_payments_engines.build(),
        bfsi_platforms_03_lending.build(),
        bfsi_platforms_04_capmkts_insurance.build(),
    ]
    for i, t in enumerate(plat_topics):
        prev_l = (("index.html", "BFSI platforms overview")
                  if i == 0
                  else (f"{plat_topics[i-1].slug}.html", plat_topics[i-1].title))
        next_l = ((f"{plat_topics[i+1].slug}.html", plat_topics[i+1].title)
                  if i + 1 < len(plat_topics) else None)
        pages.append((f"bfsi-platforms/{t.slug}.html", t.title, t.to_html(),
                      prev_l, next_l))

    # Leadership Lenses (Part VII)
    lead_topics = [
        leadership_01_architecture_decisions.build(),
        leadership_02_vendor_programme.build(),
    ]
    for i, t in enumerate(lead_topics):
        prev_l = (("index.html", "Leadership overview")
                  if i == 0
                  else (f"{lead_topics[i-1].slug}.html", lead_topics[i-1].title))
        next_l = ((f"{lead_topics[i+1].slug}.html", lead_topics[i+1].title)
                  if i + 1 < len(lead_topics) else None)
        pages.append((f"leadership/{t.slug}.html", t.title, t.to_html(),
                      prev_l, next_l))

    write_site(idx=idx, pages=pages, home_html=home_html(idx),
               glossary_html=glossary_html())
    print("Site written to bfsi_bible/. Open bfsi_bible/index.html in any browser.")


if __name__ == "__main__":
    main()
