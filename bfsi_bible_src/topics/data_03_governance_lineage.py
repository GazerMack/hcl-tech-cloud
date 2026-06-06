"""Data · 03 — Data governance, lineage, and the CDO function."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="III.3",
        slug="03-data-governance-lineage-cdo",
        title="Data governance, lineage, and the CDO function — owning the bank's most valuable asset",
        one_liner=(
            "A bank's data is worth more than its buildings. Regulatory reports, credit "
            "decisions, risk models, customer analytics, and AI all depend on data that is "
            "accurate, traceable, and governed. Yet most banks struggle with data quality, "
            "lineage gaps, and unclear ownership. This topic teaches you the frameworks, "
            "the roles, the tooling, and the regulator expectations that make data governance "
            "work in practice."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


# ------------------------------------------------------------------ 0
def _sec0() -> TopicSection:
    body = (
        primer(
            p("Data governance is the unsexy discipline that makes everything else possible. "
              "Without it, your AI models train on garbage, your regulatory reports are wrong, "
              "your customer analytics mislead, and your board makes decisions on fiction. "
              "A techno-functional leader who cannot explain data lineage, data quality "
              "dimensions, or the CDO's mandate will struggle in any BFSI design review.")
        )
        + H3("0.1  IT-side anchor — the file manager on your laptop")
        + it_anchor(
            p("Your laptop has thousands of files. Some are duplicates. Some are outdated. "
              "Some have names like 'final_v3_REAL_final.docx'. You cannot find the one you "
              "need. Now imagine this at a bank with 10,000 applications, 50,000 database "
              "tables, and 500 reports submitted to regulators quarterly. Data governance is "
              "the discipline that names things consistently, tracks where data comes from "
              "(lineage), ensures it is accurate (quality), defines who is responsible "
              "(ownership), and controls who can access it (access control).")
        )
        + H3("0.2  BFSI-side anchor — why your bank balance might be wrong")
        + bfsi_anchor(
            p("When a regulator asks a bank 'What is your total exposure to commercial real "
              "estate in Germany?', the answer should be a number. But in practice, it requires "
              "pulling data from the core banking system, the loan origination system, the "
              "collateral management system, and the general ledger — each of which may define "
              "'commercial real estate' differently, use different currency conversion rates, "
              "and update at different times. Data governance exists to make the answer "
              "consistent, auditable, and correct.")
        )
        + H3("0.3  The three pillars of data governance")
        + ol([
            "<strong>Data quality.</strong> Is the data accurate, complete, timely, and "
            "consistent? Measured by defined dimensions (accuracy, completeness, timeliness, "
            "validity, uniqueness, consistency).",
            "<strong>Data lineage.</strong> Where did this data come from, what transformations "
            "were applied, and where does it go? Critical for regulatory reporting, model "
            "validation, and incident investigation.",
            "<strong>Data ownership and stewardship.</strong> Who is accountable for this data "
            "domain? Who resolves quality issues? The CDO sets the framework; data stewards "
            "in business lines execute it.",
        ])
    )
    return TopicSection("0.  Primer — anchored to things you already know", "basic", body)


# ------------------------------------------------------------------ 1
def _sec1() -> TopicSection:
    body = (
        p("Data governance exists in BFSI because regulators, risk managers, and customers "
          "all demand it:")
        + ol([
            "<strong>Regulatory reporting accuracy.</strong> BCBS 239 (Principles for effective "
            "risk data aggregation and risk reporting) was issued after the 2008 crisis "
            "specifically because banks could not aggregate their exposures fast enough. "
            "Every G-SIB must comply. Accuracy requires governance.",
            "<strong>Model risk management.</strong> Every AI/ML model depends on input data. "
            "Fed SR 11-7 explicitly requires data quality assessment as part of model "
            "validation. Garbage in, garbage out is not a metaphor — it is an audit finding.",
            "<strong>Privacy and data protection.</strong> GDPR, UK GDPR, India's DPDP Act, "
            "Singapore's PDPA, and US state privacy laws all require that banks know what "
            "personal data they hold, where it is, and who has access. You cannot comply with "
            "privacy laws without a data inventory.",
            "<strong>Operational resilience.</strong> When a system fails, you need to know "
            "which downstream reports and processes are affected. Lineage tells you the blast "
            "radius.",
            "<strong>Cost and efficiency.</strong> Tier-1 banks spend hundreds of millions "
            "annually on data infrastructure. Without governance, teams duplicate data, build "
            "conflicting reports, and waste engineering effort reconciling numbers that should "
            "have been consistent from the start.",
        ])
    )
    return TopicSection("1.  Why data governance exists — first principles", "basic", body)


# ------------------------------------------------------------------ 2
def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart TB\n'
            '  subgraph "Governance Layer"\n'
            '    CDO["CDO / Chief Data Officer"]\n'
            '    DC["Data Council"]\n'
            '    DS["Data Stewards<br/>per domain"]\n'
            '    POL["Policies and standards"]\n'
            '  end\n'
            '  subgraph "Data Management"\n'
            '    CAT["Data catalogue<br/>Business glossary"]\n'
            '    LIN["Data lineage<br/>Impact analysis"]\n'
            '    DQ["Data quality<br/>Rules and monitoring"]\n'
            '    MDM["Master Data<br/>Management"]\n'
            '    ACC["Access control<br/>Classification"]\n'
            '  end\n'
            '  subgraph "Data Infrastructure"\n'
            '    SRC["Source systems<br/>Core, LOS, TMS"]\n'
            '    ETL["ETL / ELT<br/>Pipelines"]\n'
            '    DW["Data warehouse<br/>Data lake"]\n'
            '    RPT["Regulatory reports<br/>Analytics, AI"]\n'
            '  end\n'
            '  CDO --> DC --> DS\n'
            '  CDO --> POL\n'
            '  POL --> CAT\n'
            '  POL --> DQ\n'
            '  DS --> DQ\n'
            '  DS --> CAT\n'
            '  SRC --> ETL --> DW --> RPT\n'
            '  CAT --> LIN\n'
            '  LIN --> DW\n'
            '  DQ --> DW\n'
            '  MDM --> SRC\n'
            '  ACC --> DW',
            "Data governance sits above data management and data infrastructure.")
    )
    return TopicSection("2.  The data governance stack in one picture", "basic", body)


# ------------------------------------------------------------------ 3
def _sec3() -> TopicSection:
    body = (
        H3("3.1  Phase 1: Establish the CDO function and operating model")
        + p("The Chief Data Officer (CDO) is the senior executive accountable for data as a "
            "strategic asset. The CDO typically reports to the CEO, COO, or CRO (reporting "
            "line varies; best practice is CEO or COO to ensure independence from technology). "
            "The CDO's mandate includes:")
        + ul([
            "Setting and enforcing data governance policies and standards.",
            "Establishing the data quality framework and monitoring programme.",
            "Building and maintaining the enterprise data catalogue and lineage.",
            "Chairing the Data Council (cross-functional governance body).",
            "Owning the data strategy and aligning it to business and regulatory priorities.",
            "Ensuring compliance with data-related regulations (BCBS 239, GDPR, DPDP, etc.).",
        ])

        + H3("3.2  Phase 2: Build the data catalogue and business glossary")
        + p("A data catalogue is a searchable inventory of every data asset in the bank: "
            "tables, columns, reports, dashboards, APIs. A business glossary defines "
            "business terms ('What exactly is a Non-Performing Asset?') so that everyone "
            "uses the same definition. Without a glossary, the risk team's 'NPA' and the "
            "finance team's 'NPA' may differ by billions.")
        + p("Major data catalogue vendors in BFSI:")
        + ul([
            "<strong>Collibra</strong> — market leader for enterprise data governance; strong "
            "in lineage, glossary, stewardship workflows.",
            "<strong>Alation</strong> — strong data catalogue with AI-driven discovery and "
            "collaboration features.",
            "<strong>Informatica Data Governance (CDGC)</strong> — integrated with Informatica's "
            "data integration and quality tools; large BFSI install base.",
            "<strong>Atlan</strong> — modern, developer-friendly; growing in data-forward banks.",
            "<strong>Microsoft Purview</strong> — integrated with Azure ecosystem; suitable for "
            "Azure-first banks.",
            "<strong>AWS Glue Data Catalog</strong> — lightweight, integrated with AWS analytics.",
            "<strong>Google Dataplex</strong> — data fabric approach for GCP-centric banks.",
        ])

        + H3("3.3  Phase 3: Implement data lineage")
        + p("Data lineage traces the journey of a data element from source to consumption. "
            "There are three types:")
        + ul([
            "<strong>Technical lineage</strong> — column-level tracking through ETL jobs, "
            "SQL transformations, and pipelines. Automated by tools like Informatica, "
            "Collibra Lineage, MANTA, Ataccama, or dbt (for SQL-based transformations).",
            "<strong>Business lineage</strong> — higher-level view showing how business "
            "concepts flow across systems. Often manually maintained or derived from "
            "technical lineage with mapping.",
            "<strong>Regulatory lineage</strong> — specifically tracing how each field in a "
            "regulatory report (e.g., a CCAR submission to the Fed, an XBRL filing to RBI, "
            "a COREP return to ECB) maps back to source systems. This is what auditors and "
            "regulators inspect.",
        ])

        + H3("3.4  Phase 4: Establish data quality management")
        + p("Data quality is measured across six standard dimensions:")
        + table(
            ["Dimension", "Definition", "BFSI example"],
            [
                ["<strong>Accuracy</strong>", "Does the data reflect reality?",
                 "Is the customer's address current?"],
                ["<strong>Completeness</strong>", "Are all required fields populated?",
                 "Is the collateral valuation date present for every secured loan?"],
                ["<strong>Timeliness</strong>", "Is the data available when needed?",
                 "Is the position data refreshed before the risk report runs?"],
                ["<strong>Validity</strong>", "Does the data conform to defined formats and ranges?",
                 "Is the country code a valid ISO 3166 code?"],
                ["<strong>Uniqueness</strong>", "Is there exactly one record per entity?",
                 "Does the customer master have duplicate records?"],
                ["<strong>Consistency</strong>", "Do related data elements agree across systems?",
                 "Does the loan balance in the LOS match the balance in the GL?"],
            ]
        )
        + p("Data quality rules are defined, automated, and monitored. Failures generate "
            "alerts, and stewards investigate and remediate. Major DQ tools: Informatica "
            "Data Quality, Ataccama ONE, Great Expectations (open source), Talend, "
            "Monte Carlo (data observability), Soda.")

        + H3("3.5  Phase 5: Master Data Management (MDM)")
        + p("MDM ensures a single, authoritative version of critical entities: customer, "
            "product, counterparty, instrument, legal entity. Without MDM, the same customer "
            "appears differently in the core, the CRM, the AML system, and the data warehouse "
            "— making a single customer view impossible.")
        + p("MDM vendors in BFSI: Informatica MDM, Reltio, Stibo Systems, SAP MDG, "
            "Tamr, Semarchy.")
    )
    return TopicSection("3.  How it actually works — building data governance phase by phase",
                        "intermediate", body)


# ------------------------------------------------------------------ 4
def _sec4() -> TopicSection:
    body = (
        H3("4.1  Data governance operating models")
        + table(
            ["Model", "How it works", "Best for"],
            [
                ["<strong>Centralised</strong>",
                 "CDO team owns all governance activities — catalogue, quality, lineage, "
                 "stewardship. Business lines consume but do not govern.",
                 "Smaller banks, early-stage governance programmes. Ensures consistency but "
                 "can become a bottleneck."],
                ["<strong>Federated</strong>",
                 "CDO sets policies and standards. Data stewards in each business line execute "
                 "governance for their domain. CDO provides tooling, training, and oversight.",
                 "Tier-1 banks with complex, multi-geography estates. Scales well but requires "
                 "strong steward accountability."],
                ["<strong>Data mesh</strong>",
                 "Each domain (e.g., lending, payments, risk) owns its data as a product. "
                 "A central platform team provides self-serve infrastructure. Governance is "
                 "embedded in the domain, not layered on top.",
                 "Digitally mature banks with strong engineering culture. Emerging pattern; "
                 "few banks have fully implemented it."],
            ]
        )

        + H3("4.2  Data classification and access control")
        + p("Banks classify data by sensitivity (Public, Internal, Confidential, Restricted / "
            "Highly Restricted) and by regulatory category (PII, SPI, Payment Data, Material "
            "Non-Public Information). Classification drives access controls, encryption "
            "requirements, retention policies, and cross-border transfer restrictions.")
        + table(
            ["Classification", "Examples", "Controls"],
            [
                ["<strong>Restricted</strong>",
                 "Cryptographic keys, authentication secrets, PINs",
                 "HSM storage, no human access, audited access logs"],
                ["<strong>Confidential</strong>",
                 "Customer PII, account balances, credit bureau data, trade data",
                 "Encryption at rest and in transit, role-based access, DLP monitoring, "
                 "cross-border transfer controls"],
                ["<strong>Internal</strong>",
                 "Internal reports, architecture documents, org charts",
                 "Authentication required, no public sharing"],
                ["<strong>Public</strong>",
                 "Published annual reports, marketing materials, public APIs",
                 "No special controls"],
            ]
        )

        + H3("4.3  Data domains in a typical bank")
        + ul([
            "<strong>Customer / Party</strong> — customer master, KYC data, beneficial "
            "ownership, contact information.",
            "<strong>Account / Product</strong> — account master, product catalogue, terms "
            "and conditions, pricing.",
            "<strong>Transaction</strong> — payment transactions, trade executions, "
            "fee postings, interest accruals.",
            "<strong>Risk</strong> — credit ratings, market risk sensitivities, operational "
            "risk events, collateral valuations.",
            "<strong>Finance / GL</strong> — general ledger entries, cost centres, P&L "
            "allocations, regulatory capital.",
            "<strong>Reference data</strong> — currency codes, country codes, exchange rates, "
            "interest rate curves, instrument identifiers (ISIN, CUSIP, SEDOL).",
        ])
    )
    return TopicSection("4.  Types and variations — operating models, classification, domains",
                        "intermediate", body)


# ------------------------------------------------------------------ 5
def _sec5() -> TopicSection:
    body = (
        H3("5.1  BCBS 239 — the regulation that created the CDO function")
        + p("BCBS 239 (Principles for effective risk data aggregation and risk reporting, "
            "January 2013) was the Basel Committee's response to the 2008 crisis, when banks "
            "could not aggregate their exposures across business lines and geographies fast "
            "enough to manage the crisis. It established 14 principles across four themes:")
        + ul([
            "<strong>Governance and infrastructure</strong> — board and senior management "
            "must be involved; data architecture must support aggregation.",
            "<strong>Risk data aggregation capabilities</strong> — accuracy, completeness, "
            "timeliness, adaptability.",
            "<strong>Risk reporting practices</strong> — accuracy, comprehensiveness, clarity, "
            "frequency, distribution.",
            "<strong>Supervisory review</strong> — regulators assess compliance.",
        ])
        + p("Compliance with BCBS 239 remains uneven. The Basel Committee's 2024 progress "
            "report noted that many G-SIBs still have gaps in data lineage, automated "
            "aggregation, and ad-hoc reporting capabilities.")

        + H3("5.2  Data lineage at depth — why it is so hard")
        + p("In theory, lineage is simple: trace the data from source to report. In practice, "
            "it is one of the hardest problems in enterprise IT because:")
        + ul([
            "<strong>Heterogeneous technology.</strong> Data flows through mainframe COBOL "
            "programs, ETL tools (Informatica, Talend, SSIS), Python scripts, Spark jobs, "
            "stored procedures, and Excel macros. No single tool traces all of them.",
            "<strong>Undocumented transformations.</strong> A 15-year-old stored procedure "
            "applies a business rule that nobody remembers writing. It transforms a field "
            "that feeds a regulatory report.",
            "<strong>Shadow IT.</strong> Business analysts extract data into spreadsheets, "
            "apply manual adjustments, and feed the result into a submission. The lineage "
            "breaks at the spreadsheet boundary.",
            "<strong>Change velocity.</strong> Lineage metadata goes stale as pipelines change. "
            "Automated lineage (parsing ETL code, SQL, and pipeline DAGs) is essential; "
            "manual lineage is always out of date.",
        ])

        + H3("5.3  The data mesh debate")
        + p("Data mesh (coined by Zhamak Dehghani, 2019) proposes that each business domain "
            "owns and publishes its data as a product, with self-serve infrastructure and "
            "federated governance. In BFSI, the appeal is clear: it aligns data ownership with "
            "business accountability. But the challenges are significant:")
        + ul([
            "Regulatory reports cut across domains — who owns the aggregated view?",
            "Data quality standards must be consistent across domains; federated governance "
            "requires strong coordination.",
            "Few banks have the engineering maturity to operate self-serve data platforms.",
            "The 'data as a product' mindset requires cultural change in traditional institutions.",
        ])
        + p("In practice, most BFSI organisations adopt elements of data mesh (domain "
            "ownership, data products) within a federated governance model, rather than a "
            "pure implementation.")

        + H3("5.4  Data observability — monitoring data like infrastructure")
        + p("Data observability applies the principles of infrastructure monitoring (uptime, "
            "latency, error rates) to data pipelines. Tools like Monte Carlo, Bigeye, Soda, "
            "and Great Expectations monitor data freshness, volume, schema changes, and "
            "distribution anomalies. When a pipeline delivers 30% fewer records than usual, "
            "or a column's distribution shifts dramatically, data observability catches it "
            "before it corrupts a downstream report.")
    )
    return TopicSection("5.  Advanced — BCBS 239, lineage at depth, data mesh, observability",
                        "advanced", body)


# ------------------------------------------------------------------ 6
def _sec6() -> TopicSection:
    body = (
        p("Data governance is shaped by a dense web of regulations that vary by jurisdiction.")
        + table(
            ["Region", "Key data governance regulations", "Practical impact"],
            [
                ["<strong>Global (Basel)</strong>",
                 "BCBS 239 (risk data aggregation). BCBS 530 (climate risk data). "
                 "Basel III/IV capital calculations require accurate, traceable data.",
                 "G-SIBs must demonstrate automated risk data aggregation, lineage to source, "
                 "and ad-hoc reporting capability."],
                ["<strong>India</strong>",
                 "RBI Master Direction on IT Governance (Nov 2023): data governance is a "
                 "board-level topic. RBI Storage of Payment Data (Apr 2018): payment data "
                 "must be stored in India. DPDP Act 2023: personal data protection with "
                 "consent and purpose limitation. SEBI data localisation for market data.",
                 "Data residency is non-negotiable for payment data. DPDP requires data "
                 "inventory and consent management. RBI expects data quality frameworks."],
                ["<strong>United States</strong>",
                 "OCC Heightened Standards: data governance as part of risk management. "
                 "CCAR/DFAST: stress testing requires traceable risk data. CCPA/state privacy "
                 "laws: data inventory and consumer rights. SOX: financial data controls.",
                 "Fed/OCC examiners inspect data lineage for CCAR submissions. Data quality "
                 "deficiencies are MRA/MRIA material."],
                ["<strong>United Kingdom</strong>",
                 "PRA expectations aligned to BCBS 239. FCA data strategy (published 2022). "
                 "UK GDPR: data protection with accountability principle. SM&CR: named "
                 "accountability for data.",
                 "PRA inspects risk data aggregation. FCA increasingly focused on data ethics "
                 "and algorithmic fairness."],
                ["<strong>Eurozone</strong>",
                 "ECB/SSM BCBS 239 assessments (annual). GDPR: comprehensive data protection. "
                 "DORA: ICT data integrity. EBA ITS on supervisory reporting.",
                 "ECB conducts targeted BCBS 239 inspections. GDPR fines for data governance "
                 "failures are large and public."],
                ["<strong>Singapore</strong>",
                 "MAS Technology Risk Management Guidelines: data integrity requirements. "
                 "PDPA: personal data protection. MAS Notice 610: risk data reporting.",
                 "MAS expects banks to demonstrate data lineage for regulatory submissions."],
            ]
        )
    )
    return TopicSection("6.  BFSI / domain regulatory overlay", "advanced", body)


# ------------------------------------------------------------------ 7
def _sec7() -> TopicSection:
    return TopicSection(
        "7.  Trade-offs and decisions a leader owns", "intermediate",
        table(
            ["Decision", "Trade-offs and considerations"],
            [
                ["<strong>CDO reporting line</strong>",
                 "CDO under CTO: closer to data infrastructure but risks being seen as 'just IT'. "
                 "CDO under COO or CEO: stronger business mandate but may lack technical depth. "
                 "CDO under CRO: strong regulatory focus but may neglect commercial data value. "
                 "Best practice: CDO as a peer to CTO and CRO with direct board access."],
                ["<strong>Buy vs build data catalogue</strong>",
                 "Enterprise tools (Collibra, Alation) are mature but expensive ($1–5M/year). "
                 "Open-source (OpenMetadata, DataHub, Amundsen) are capable but require "
                 "engineering investment. Most tier-1 banks buy; data-forward fintechs build."],
                ["<strong>Automated vs manual lineage</strong>",
                 "Automated lineage (parsing ETL/SQL) covers 60–80% of flows. The remaining "
                 "20–40% (spreadsheets, manual processes, undocumented logic) requires manual "
                 "documentation. Plan for both."],
                ["<strong>Centralised vs federated data quality</strong>",
                 "Central DQ team ensures consistency but becomes a bottleneck. Federated DQ "
                 "(stewards run rules in their domain) scales but requires strong standards and "
                 "tooling. Hub-and-spoke is the pragmatic answer."],
                ["<strong>Data mesh adoption</strong>",
                 "Full data mesh requires engineering maturity most banks lack. Adopt the "
                 "principles (domain ownership, data as product) within a federated governance "
                 "model. Do not reorganise around a buzzword."],
            ]
        )
    )


# ------------------------------------------------------------------ 8
def _sec8() -> TopicSection:
    body = (
        example("A G-SIB fails the BCBS 239 assessment",
            p("A European G-SIB received an adverse ECB/SSM finding on BCBS 239 compliance. "
              "The bank could not demonstrate automated lineage from risk report fields to "
              "source systems. Manual reconciliation of a single COREP return took 3 weeks. "
              "The ECB required a remediation plan within 90 days. The bank invested in "
              "Collibra for catalogue and lineage, automated 70% of lineage within 18 months, "
              "and reduced reconciliation time to 2 days. Lesson: BCBS 239 compliance is not "
              "optional for G-SIBs, and manual lineage does not scale.")
        )
        + example("Indian bank — RBI inspection on data localisation",
            p("An Indian private-sector bank stored payment transaction analytics on a US-based "
              "cloud provider's servers. During an RBI IT examination, the bank was asked to "
              "demonstrate that raw payment data (as defined under the April 2018 circular) "
              "remained in India. The bank could show that processing occurred offshore but "
              "raw data was replicated back within 24 hours. RBI found this non-compliant — "
              "the circular requires storage 'only in India', not eventual consistency. The "
              "bank re-architected to process and store in the Mumbai region. Lesson: data "
              "residency rules in India are strict and literal.")
        )
        + example("UK bank — GDPR data subject access request reveals data chaos",
            p("A UK bank received a GDPR Subject Access Request (SAR) from a customer. The "
              "legal team needed to find all personal data held about this customer across "
              "all systems. Without a data catalogue, this required manual trawling of 47 "
              "systems over 28 days (the legal deadline is 30 days). The bank invested in "
              "an automated data discovery tool (BigID) and a data catalogue (Alation) to "
              "make future SARs tractable. Lesson: privacy compliance requires data governance "
              "infrastructure, not just policy.")
        )
        + example("Data quality failure corrupts a regulatory submission",
            p("A US bank submitted its quarterly call report to the FDIC. A data quality "
              "issue in the ETL pipeline double-counted certain intercompany loans, overstating "
              "total assets by $1.2 billion. The error was caught by the bank's second-line "
              "review after submission, requiring an amended filing and an OCC MRA. Root cause: "
              "no automated DQ rules on the intercompany elimination step. Lesson: data quality "
              "rules must cover not just source data but every transformation in the pipeline.")
        )
    )
    return TopicSection("8.  Worked examples — four real data governance stories",
                        "intermediate", body)


# ------------------------------------------------------------------ 9
def _sec9() -> TopicSection:
    body = (
        H3("Questions a leader asks in any data governance review")
        + ol([
            "Do we have an enterprise data catalogue, and what percentage of critical data "
            "assets are catalogued?",
            "Can we trace the lineage of every field in our top-10 regulatory reports back to "
            "source systems?",
            "What is our data quality score for each critical data domain, and what is the "
            "trend?",
            "Who is the named data steward for each domain, and do they have time and authority "
            "to resolve issues?",
            "How long does it take to respond to a data subject access request (GDPR/DPDP)?",
            "Are our MDM golden records actually consumed by downstream systems, or are they "
            "bypassed?",
            "What percentage of our data lineage is automated vs manually maintained?",
            "How does our data governance framework address AI/ML training data quality?",
        ])
        + red_flag(ul([
            "'We have a data catalogue — it is in a SharePoint.' — A SharePoint with data "
            "definitions is not a data catalogue. It is not searchable, not linked to lineage, "
            "not integrated with access controls, and goes stale on day one.",
            "'Data governance is an IT project.' — Data governance is a business discipline. "
            "The CDO sets policy, business stewards execute, and technology provides tooling. "
            "If it lives entirely in IT, business ownership never materialises.",
            "'We'll do lineage later.' — Lineage is the foundation for impact analysis, "
            "regulatory traceability, and incident investigation. Building reports without "
            "lineage means you cannot explain your numbers to the regulator.",
            "'Our data quality is fine — nobody has complained.' — Absence of complaints is "
            "not evidence of quality. Measure the six dimensions (accuracy, completeness, "
            "timeliness, validity, uniqueness, consistency) against defined thresholds. "
            "What you do not measure, you do not govern.",
            "'BCBS 239 only applies to G-SIBs.' — The principles apply to all banks. "
            "Regulators in India (RBI), UK (PRA), and elsewhere increasingly hold non-G-SIBs "
            "to the same expectations.",
            "'We cannot afford a data catalogue tool.' — You cannot afford not to have one. "
            "Open-source options (OpenMetadata, DataHub) are capable and free. The cost of a "
            "regulatory finding for untraceable data far exceeds the tool investment.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("CDO", "Chief Data Officer — senior executive accountable for data governance, "
             "quality, and strategy."),
            ("BCBS 239", "Basel Committee principles for effective risk data aggregation and "
             "risk reporting (January 2013)."),
            ("Data lineage", "The traced path of a data element from source through "
             "transformations to consumption (reports, models, analytics)."),
            ("Data catalogue", "A searchable inventory of data assets with metadata, "
             "descriptions, ownership, and lineage."),
            ("Business glossary", "An authoritative dictionary of business terms and their "
             "definitions, ensuring consistent use across the organisation."),
            ("Data quality dimensions", "The six standard measures: accuracy, completeness, "
             "timeliness, validity, uniqueness, consistency."),
            ("MDM", "Master Data Management — maintaining a single, authoritative version of "
             "critical entities (customer, product, counterparty)."),
            ("Data steward", "A business-line representative accountable for data quality and "
             "governance within their domain."),
            ("Data mesh", "An architectural paradigm where each domain owns and publishes its "
             "data as a product, with federated governance."),
            ("Data observability", "Monitoring data pipelines for freshness, volume, schema, "
             "and distribution anomalies — like infrastructure monitoring for data."),
            ("Feature store", "A centralised repository of pre-computed ML features, ensuring "
             "consistency between training and serving."),
            ("DLP", "Data Loss Prevention — tools that detect and prevent unauthorised data "
             "exfiltration."),
            ("SAR (GDPR)", "Subject Access Request — a GDPR right allowing individuals to "
             "request all personal data held about them."),
            ("COREP / FINREP", "EU regulatory reporting frameworks for capital (COREP) and "
             "financial (FINREP) data."),
        ])
    )
    return TopicSection("9.  Questions, red flags, and glossary", "basic", body)
