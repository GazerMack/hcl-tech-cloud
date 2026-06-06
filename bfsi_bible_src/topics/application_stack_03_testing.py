"""Application Stack · 03 — Testing strategies in BFSI (performance, regression, regulatory UAT).

Covers functional testing, performance/load testing, regression, security testing,
regulatory UAT, test data management, shift-left, and test automation across
banking, payments, capital markets, and insurance.
"""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="II.3",
        slug="03-testing-strategies-bfsi",
        title="Testing strategies in BFSI — performance, regression, regulatory UAT",
        one_liner=(
            "A failed payment, a wrong interest calculation, a regulatory report "
            "with incorrect figures, a mobile-banking app that crashes on payday — "
            "every one of these is a testing failure. In BFSI, testing is not a "
            "quality-assurance afterthought; it is a regulatory obligation, a "
            "reputational shield, and one of the largest cost centres in any "
            "technology programme. This topic teaches the full testing landscape "
            "from unit tests to regulatory UAT, with the tools, metrics, and "
            "trade-offs a techno-functional leader must own."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


# ------------------------------------------------------------------ sec 0

def _sec0() -> TopicSection:
    body = (
        primer(
            p("Testing in BFSI is different from testing in a consumer tech "
              "company. When Spotify pushes a buggy release, a song might not "
              "play for a few minutes. When a bank pushes a buggy release, a "
              "customer's salary might not credit, a margin call might be "
              "miscalculated, a regulatory report might be filed with wrong "
              "figures, or a payment might go to the wrong account. The "
              "consequences are financial loss, regulatory fines, and "
              "reputational damage that takes years to recover from. This is "
              "why testing in BFSI is deeper, more structured, and more "
              "expensive than in most other industries.")
        )
        + H3("0.1  IT-side anchor — testing a car before it leaves the factory")
        + it_anchor(
            p("A car manufacturer tests every component individually (unit test "
              "each part), tests components together (integration test the engine "
              "with the transmission), tests the whole car on a track (system "
              "test), has test drivers simulate real roads (UAT — User Acceptance "
              "Testing), crash-tests with dummies (performance/stress test), and "
              "verifies it meets emission standards (regulatory compliance "
              "testing). Only then does the car ship. A banking application goes "
              "through exactly the same progression — but with one extra "
              "dimension: every release must also be tested against regulatory "
              "rules that change multiple times a year.")
        )
        + H3("0.2  BFSI-side anchor — why your bank's app goes down for "
              "'scheduled maintenance'")
        + bfsi_anchor(
            p("When your banking app shows 'scheduled maintenance — services "
              "will be unavailable from 2 AM to 5 AM', the bank is deploying a "
              "new release. Before that release reached production, it went "
              "through dozens of testing stages: did the interest calculation "
              "change correctly? Does the new feature work with all 47 account "
              "types? Can the system handle 10 million logins on salary day? "
              "Does the regulatory report still produce the right numbers? Did "
              "the API change break the mobile app? If any of these tests fail, "
              "the release is rolled back — and you see 'maintenance extended'. "
              "The difference between a bank that deploys weekly and one that "
              "deploys quarterly is almost entirely about testing maturity.")
        )
        + H3("0.3  The testing pyramid in BFSI")
        + p("The testing pyramid is a universal concept, but in BFSI each layer "
            "has regulatory and domain-specific implications:")
        + table(
            ["Layer", "What it tests", "BFSI-specific concern", "Typical ratio"],
            [
                ["<strong>Unit tests</strong>",
                 "Individual functions/methods in isolation",
                 "Interest calculations, fee logic, currency rounding, "
                 "date conventions (ACT/360 vs 30/360)",
                 "60–70% of all tests"],
                ["<strong>Integration tests</strong>",
                 "Interactions between components/services",
                 "Core banking ↔ payments gateway, OMS ↔ exchange, "
                 "policy admin ↔ claims",
                 "15–20%"],
                ["<strong>API / contract tests</strong>",
                 "API request/response schemas and contracts",
                 "ISO 20022 message validation, SWIFT MT format, "
                 "Open Banking API compliance",
                 "5–10%"],
                ["<strong>End-to-end (E2E) tests</strong>",
                 "Full business flows through all layers",
                 "Loan origination end-to-end, payment from initiation "
                 "to settlement, claim from FNOL to payout",
                 "5–10%"],
                ["<strong>UAT (User Acceptance Testing)</strong>",
                 "Business users validate real scenarios",
                 "Regulatory UAT is mandatory for many changes — "
                 "auditors and regulators may review UAT evidence",
                 "Varies — can be weeks"],
            ]
        )
    )
    return TopicSection(
        "0.  Primer — anchored to things you already know", "basic", body)


# ------------------------------------------------------------------ sec 1

def _sec1() -> TopicSection:
    body = (
        p("Testing exists in every software project. In BFSI it is elevated "
          "to a first-class discipline because of five forces:")
        + ol([
            "<strong>Regulatory mandate.</strong> Regulators explicitly require "
            "testing evidence. The PRA (UK) expects banks to demonstrate that "
            "changes to models, systems, and processes are tested before "
            "deployment. The Fed's SR 11-7 requires model validation testing. "
            "EU DORA (in force Jan 2025) mandates Threat-Led Penetration "
            "Testing (TLPT) for critical financial entities. RBI's IT "
            "Governance Master Direction (Nov 2023) requires banks to have "
            "documented testing frameworks.",
            "<strong>Financial accuracy.</strong> A rounding error in interest "
            "calculation, compounded across millions of accounts, can cost "
            "millions. A fee calculation bug on a card product with 10 million "
            "customers is a potential class-action lawsuit. Testing must verify "
            "financial precision to the penny/paisa.",
            "<strong>Systemic risk.</strong> A failed payment system does not "
            "just affect one bank — it can cascade. The UK's TSB migration "
            "disaster (April 2018) left 1.9 million customers locked out for "
            "weeks, triggered FCA enforcement, and cost GBP 330M+ in remediation.",
            "<strong>Data sensitivity.</strong> Test environments must handle "
            "test data that is realistic enough to be useful but must not "
            "expose real customer data (PII). GDPR, DPDP Act (India), PDPA "
            "(Singapore) all constrain how production data can be used in testing.",
            "<strong>Change velocity vs. stability.</strong> Banks now deploy "
            "hundreds of changes per month. Each change must be tested without "
            "slowing delivery. The tension between speed and safety defines "
            "the testing strategy.",
        ])
    )
    return TopicSection(
        "1.  Why testing is a first-class discipline in BFSI — first principles",
        "basic", body)


# ------------------------------------------------------------------ sec 2

def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  subgraph "Development"\n'
            '    UT["Unit tests\u003cbr/\u003eDeveloper machine"]\n'
            '    SAST["Static analysis\u003cbr/\u003eSAST / linters"]\n'
            '  end\n'
            '  subgraph "CI Pipeline"\n'
            '    IT["Integration tests"]\n'
            '    CT["Contract / API tests"]\n'
            '    SEC["Security scans\u003cbr/\u003eDAST and SCA"]\n'
            '  end\n'
            '  subgraph "Pre-Production"\n'
            '    E2E["End-to-end tests"]\n'
            '    PERF["Performance tests\u003cbr/\u003eload and stress"]\n'
            '    REG["Regression suite"]\n'
            '    UAT["UAT\u003cbr/\u003eBusiness and regulatory"]\n'
            '  end\n'
            '  subgraph "Production"\n'
            '    SMK["Smoke tests"]\n'
            '    MON["Monitoring and\u003cbr/\u003eobservability"]\n'
            '  end\n'
            '  UT --> SAST --> IT --> CT --> SEC --> E2E --> PERF --> REG --> UAT --> SMK --> MON',
            "The BFSI testing pipeline — from developer machine to production "
            "monitoring. Every stage is a quality gate."
        )
        + p("The pipeline is not strictly sequential in modern CI/CD — many "
            "stages run in parallel. But every stage must pass before the "
            "next gate opens. In BFSI, the UAT gate often requires sign-off "
            "from business owners, compliance, and sometimes external auditors.")
    )
    return TopicSection(
        "2.  The core concept in one picture", "basic", body)


# ------------------------------------------------------------------ sec 3

def _sec3() -> TopicSection:
    body = (
        H3("3.1  Functional testing — does the logic work correctly?")
        + p("Functional testing verifies that the system behaves as specified. "
            "In BFSI, this means testing business rules that are often "
            "extraordinarily complex:")
        + ul([
            "<strong>Interest calculation.</strong> A savings account might "
            "use daily balance, monthly compounding, ACT/365 day count. A "
            "corporate loan might use ACT/360. A bond might use 30/360. "
            "Each must be tested with edge cases: leap years, month-end, "
            "partial periods, negative interest rates (yes, in Europe).",
            "<strong>Fee schedules.</strong> A single bank may have 200+ fee "
            "types across products. Testing must verify each fee triggers "
            "correctly, applies the right amount, respects waivers and "
            "caps, and posts to the correct GL (General Ledger) account.",
            "<strong>Regulatory calculations.</strong> Basel capital ratios, "
            "LCR (Liquidity Coverage Ratio), NSFR (Net Stable Funding Ratio), "
            "Solvency II SCR (Solvency Capital Requirement) — each involves "
            "hundreds of data points and complex formulas. A single error "
            "in a regulatory return can trigger supervisory scrutiny.",
            "<strong>Multi-currency.</strong> A cross-border payment involves "
            "currency conversion, FX margin, rounding rules (which differ by "
            "currency — JPY has no decimal places, BHD has three), nostro/"
            "vostro reconciliation, and SWIFT message formatting.",
        ])

        + H3("3.2  Regression testing — did we break anything?")
        + p("Regression testing is the largest and most expensive testing "
            "activity in most banks. Every change must be validated against "
            "existing functionality to ensure nothing is broken. At a tier-1 "
            "bank, the regression suite can contain 50,000–200,000 test cases "
            "across core banking, payments, lending, cards, and channels.")
        + p("The challenge: running the full regression suite takes days or "
            "weeks. Solutions:")
        + ul([
            "<strong>Risk-based regression.</strong> Analyse which test cases "
            "are affected by the change (impact analysis) and run only those. "
            "Tools: Tricentis qTest, Micro Focus ALM, in-house dependency maps.",
            "<strong>Test prioritisation.</strong> Run the most critical tests "
            "first (payments, account opening, regulatory) and lower-priority "
            "tests in parallel.",
            "<strong>AI-assisted test selection.</strong> Use ML to predict "
            "which tests are most likely to fail based on the code changes. "
            "Tools: Launchable, Buildkite Test Analytics, Tricentis Vision AI.",
            "<strong>Continuous regression.</strong> Run the full suite nightly "
            "and a subset on every commit.",
        ])

        + H3("3.3  Performance and load testing — can it handle payday?")
        + p("BFSI systems experience extreme demand peaks: salary day (every "
            "month-end), IPO application days (India ASBA), Black Friday "
            "(card transactions), year-end closing (GL and regulatory). "
            "Performance testing validates that the system meets its SLAs "
            "under these conditions.")
        + table(
            ["Test type", "What it measures", "BFSI example"],
            [
                ["<strong>Load test</strong>",
                 "Response time and throughput under expected peak load",
                 "10,000 concurrent UPI transactions per second on salary day"],
                ["<strong>Stress test</strong>",
                 "System behaviour beyond peak — when does it degrade?",
                 "What happens at 2x normal NEFT volume? Does the queue "
                 "overflow or gracefully degrade?"],
                ["<strong>Soak / endurance test</strong>",
                 "Memory leaks and degradation over extended periods",
                 "Run the core banking batch for 72 hours straight — "
                 "does memory grow unbounded?"],
                ["<strong>Spike test</strong>",
                 "Sudden burst of traffic",
                 "IPO application window opens — 5 million ASBA "
                 "applications in 30 minutes"],
                ["<strong>Capacity test</strong>",
                 "Maximum throughput before SLA breach",
                 "How many cards can the switch authorise per second "
                 "before latency exceeds 500ms?"],
            ]
        )
        + p("Tools: Gatling (open-source, Scala-based, excellent for API "
            "load testing), JMeter (Apache, widely used but aging), k6 "
            "(Grafana, developer-friendly), LoadRunner (Micro Focus, "
            "enterprise standard in BFSI), NeoLoad (Tricentis), Locust "
            "(Python-based, scriptable).")

        + H3("3.4  Security testing — DAST, SAST, IAST, penetration testing")
        + p("Security testing in BFSI is not optional — it is regulated:")
        + ul([
            "<strong>SAST (Static Application Security Testing)</strong> — "
            "scans source code for vulnerabilities. Run in CI pipeline. "
            "Tools: Checkmarx, Fortify (OpenText), SonarQube, Veracode, "
            "Snyk Code.",
            "<strong>DAST (Dynamic Application Security Testing)</strong> — "
            "tests running applications for vulnerabilities (XSS, SQLi, "
            "CSRF). Tools: OWASP ZAP, Burp Suite (PortSwigger), "
            "Invicti (Netsparker), Qualys WAS.",
            "<strong>SCA (Software Composition Analysis)</strong> — "
            "identifies vulnerabilities in open-source dependencies. "
            "Critical in BFSI where a Log4j-style vulnerability can "
            "affect hundreds of applications. Tools: Snyk, Black Duck "
            "(Synopsys), Dependabot, Mend (WhiteSource).",
            "<strong>IAST (Interactive Application Security Testing)</strong> "
            "— instruments the running application to detect vulnerabilities "
            "during functional testing. Tools: Contrast Security, Seeker "
            "(Synopsys).",
            "<strong>Penetration testing</strong> — ethical hackers attempt to "
            "breach the system. EU DORA mandates TLPT (Threat-Led "
            "Penetration Testing) based on the TIBER-EU framework for "
            "critical financial entities. PCI DSS requires annual "
            "penetration testing for any system handling card data.",
        ])

        + H3("3.5  Regulatory and compliance testing")
        + p("Regulatory testing verifies that the system complies with "
            "specific regulatory requirements:")
        + ul([
            "<strong>Regulatory UAT.</strong> When a bank implements a "
            "regulatory change (e.g., new Basel III.1 capital rules, IFRS 17 "
            "accounting, MiFID II cost disclosure), the business and "
            "compliance teams must sign off that the implementation matches "
            "the regulation. This is not optional — auditors will ask for "
            "UAT evidence.",
            "<strong>Regulatory reporting validation.</strong> Automated "
            "validation of regulatory returns (CCAR, COREP, FINREP, RBI "
            "returns) against known-good expected outputs. Often involves "
            "parallel runs: the old and new systems produce the same report, "
            "and the outputs are compared cell by cell.",
            "<strong>PCI DSS testing.</strong> Quarterly ASV (Approved "
            "Scanning Vendor) scans, annual penetration testing, and "
            "ongoing compliance validation for any system touching "
            "card data.",
            "<strong>Accessibility testing.</strong> FCA Consumer Duty (UK) "
            "and ADA (US) require digital banking services to be accessible. "
            "Tools: axe (Deque), WAVE, Pa11y.",
        ])

        + H3("3.6  Test data management (TDM) — the hardest problem")
        + p("Tests need realistic data. But using production data in test "
            "environments violates data protection laws (GDPR, DPDP Act, "
            "PDPA). Solutions:")
        + ul([
            "<strong>Data masking / anonymisation.</strong> Replace PII "
            "(names, account numbers, Aadhaar, SSN) with realistic but "
            "fake values while preserving referential integrity. Tools: "
            "Delphix, Informatica TDM, IBM InfoSphere Optim, Broadcom "
            "Test Data Manager.",
            "<strong>Synthetic data generation.</strong> Generate entirely "
            "artificial test data that has the same statistical properties "
            "as production data. Tools: Tonic.ai, Mostly AI, Gretel, "
            "Hazy (now Synthetic Data Vault).",
            "<strong>Test data subsetting.</strong> Extract a representative "
            "subset of production data (e.g., 5% of accounts across all "
            "product types) and mask it.",
            "<strong>Data virtualisation.</strong> Create virtual copies of "
            "production datasets that can be refreshed in minutes without "
            "copying terabytes. Tools: Delphix, Actifio (Google Cloud).",
        ])
    )
    return TopicSection(
        "3.  How it actually works — the testing types, phase by phase",
        "intermediate", body)


# ------------------------------------------------------------------ sec 4

def _sec4() -> TopicSection:
    body = (
        H3("4.1  Testing across BFSI domains")
        + table(
            ["Domain", "Critical test scenarios", "Unique challenges"],
            [
                ["<strong>Retail banking</strong>",
                 "Account opening, balance enquiry, fund transfer (NEFT/IMPS/"
                 "UPI/SWIFT), standing instructions, interest accrual, "
                 "statement generation, multi-currency",
                 "Massive account variety (savings, current, NRE, NRO, FCNR). "
                 "Each product has different rules. Salary-day load spikes."],
                ["<strong>Payments</strong>",
                 "Payment initiation, routing, clearing, settlement, "
                 "reconciliation, exception handling, timeout/retry, "
                 "ISO 20022 message validation",
                 "Real-time systems (UPI, FedNow, SEPA Inst) have sub-second "
                 "SLAs. Failure means customer-visible outage. Must test "
                 "against scheme-specific test harnesses (NPCI, EBA, TCH)."],
                ["<strong>Lending</strong>",
                 "Loan origination, credit scoring, disbursement, EMI "
                 "calculation, prepayment, foreclosure, NPA classification, "
                 "provisioning, collections",
                 "Interest calculation variations (flat, reducing, daily "
                 "reducing). Regulatory classification (90-day NPA rule in "
                 "India). Provisioning logic changes with every RBI circular."],
                ["<strong>Cards and switches</strong>",
                 "Authorization, clearing, settlement, chargeback, "
                 "tokenization, EMV cryptogram validation, stand-in "
                 "processing",
                 "ISO 8583 message testing requires specialised simulators. "
                 "Must test against Visa/Mastercard certification suites. "
                 "HSM integration testing."],
                ["<strong>Capital markets</strong>",
                 "Order entry, execution, allocation, position management, "
                 "P&L calculation, risk (VaR, ES), regulatory reporting "
                 "(EMIR, MiFID II), T+1 settlement",
                 "Multi-asset testing (equities, FI, FX, derivatives). "
                 "Complex pricing models. Market-data dependency. "
                 "FIX protocol testing."],
                ["<strong>Insurance</strong>",
                 "Quote, underwrite, bind, policy issue, endorsement, "
                 "renewal, claim FNOL, claim assessment, claim payment, "
                 "actuarial valuation, IFRS 17 reporting",
                 "Long policy lifecycles (25-year term life). Actuarial "
                 "model validation is its own testing discipline. "
                 "Guidewire/Duck Creek configuration testing."],
            ]
        )

        + H3("4.2  Test automation frameworks in BFSI")
        + table(
            ["Layer", "Recommended tools (2024–25)", "Notes"],
            [
                ["<strong>Unit testing</strong>",
                 "JUnit 5 / TestNG (Java), pytest (Python), NUnit (.NET), "
                 "Jest (JavaScript/TypeScript)",
                 "Standard across industries. In BFSI, ensure financial "
                 "calculation tests use decimal/BigDecimal, never floats."],
                ["<strong>API testing</strong>",
                 "Postman/Newman, REST Assured (Java), Karate DSL, "
                 "Pact (contract testing), WireMock (service virtualisation)",
                 "Pact is increasingly used for microservices contract "
                 "testing in BFSI. WireMock mocks external services "
                 "(payment gateways, credit bureaus)."],
                ["<strong>UI / E2E testing</strong>",
                 "Playwright (Microsoft — fastest growing), Cypress, "
                 "Selenium (legacy but dominant), Appium (mobile)",
                 "Playwright recommended for new projects. Selenium "
                 "still dominant in BFSI due to legacy investment."],
                ["<strong>Performance testing</strong>",
                 "Gatling, k6 (Grafana), JMeter, LoadRunner (Micro Focus), "
                 "NeoLoad (Tricentis)",
                 "Gatling and k6 for developer-owned perf tests. "
                 "LoadRunner for enterprise-wide capacity testing."],
                ["<strong>Security testing</strong>",
                 "Checkmarx (SAST), Snyk (SCA+SAST), OWASP ZAP (DAST), "
                 "Burp Suite (pentest)",
                 "Integrated into CI/CD pipeline. SAST and SCA run on "
                 "every pull request."],
                ["<strong>BDD / specification by example</strong>",
                 "Cucumber (Gherkin syntax), SpecFlow (.NET), "
                 "Behave (Python)",
                 "Popular in BFSI for bridging business and tech. "
                 "Business analysts write Gherkin; automation engineers "
                 "implement step definitions."],
                ["<strong>Test management</strong>",
                 "Jira + Zephyr/Xray, TestRail, qTest (Tricentis), "
                 "Azure DevOps Test Plans",
                 "Regulatory audit trails require linking test cases to "
                 "requirements and defects."],
                ["<strong>Test data</strong>",
                 "Delphix, Tonic.ai, Mostly AI, Broadcom TDM",
                 "Data masking and synthetic generation are mandatory "
                 "for GDPR/DPDP compliance."],
            ]
        )

        + H3("4.3  Shift-left testing and DevOps integration")
        + p("Shift-left means moving testing earlier in the development "
            "lifecycle. In BFSI, this is critical because late-stage defects "
            "are 10–100x more expensive to fix than early-stage ones. A "
            "defect caught in UAT costs days; a defect in production costs "
            "millions (remediation, regulatory reporting, customer "
            "compensation). Shift-left practices:")
        + ul([
            "<strong>TDD (Test-Driven Development)</strong> — write the "
            "test before the code. Particularly valuable for financial "
            "calculations where the expected output is defined by the "
            "business specification.",
            "<strong>CI-integrated testing</strong> — unit tests, SAST, "
            "and SCA run on every pull request. No merge without green "
            "tests.",
            "<strong>Contract testing in CI</strong> — Pact tests verify "
            "API contracts between microservices on every commit, catching "
            "integration breaks before deployment.",
            "<strong>Chaos engineering</strong> — inject failures "
            "(network partition, database timeout, dependency down) in "
            "pre-production to validate resilience. Tools: Gremlin, "
            "Chaos Monkey (Netflix), LitmusChaos. EU DORA's TLPT "
            "requirement is pushing banks to adopt this.",
        ])
    )
    return TopicSection(
        "4.  Types and variations — domains, tools, and shift-left",
        "intermediate", body)


# ------------------------------------------------------------------ sec 5

def _sec5() -> TopicSection:
    body = (
        H3("5.1  Testing in a microservices architecture")
        + p("When a bank moves from a monolith to microservices (see II.2), "
            "the testing challenge explodes combinatorially. A monolith has "
            "one deployment; 50 microservices have 50 independent deployment "
            "pipelines, each potentially breaking the others.")
        + ul([
            "<strong>Service virtualisation.</strong> Mock external services "
            "so each microservice can be tested independently. Tools: "
            "WireMock, Hoverfly, Mountebank, Broadcom Service Virtualisation.",
            "<strong>Consumer-Driven Contract Testing (CDCT).</strong> "
            "Each consumer service defines the API contract it expects "
            "from the provider. Pact tests verify both sides independently. "
            "This catches integration breaks without needing a full "
            "integrated environment.",
            "<strong>Canary deployments and feature flags.</strong> Deploy "
            "to a small percentage of traffic (canary) and validate "
            "production behaviour before full rollout. Feature flags "
            "(LaunchDarkly, Unleash, Flagsmith) decouple deployment from "
            "release.",
            "<strong>Observability-driven testing.</strong> In production, "
            "monitor golden signals (latency, error rate, throughput, "
            "saturation) and alert on anomalies — this is 'testing in "
            "production' with SRE practices.",
        ])

        + H3("5.2  Testing mainframe and legacy systems")
        + p("Many tier-1 banks still run core processing on IBM Z mainframes "
            "(see I.5). Testing mainframe systems has unique challenges:")
        + ul([
            "<strong>COBOL unit testing.</strong> Compuware Topaz for Total "
            "Test (now BMC), IBM Developer for z/OS, COBOL-Check "
            "(open-source). Running tests on the mainframe is expensive "
            "(MIPS-based pricing), so banks optimise by running tests "
            "on emulators where possible.",
            "<strong>Batch testing.</strong> Mainframe batch jobs (end-of-day, "
            "month-end, year-end) must be tested end-to-end. A failed "
            "batch can delay an entire bank's processing. Tools: CA "
            "Batch Scheduler testing, BMC Control-M testing.",
            "<strong>Screen-scraping vs. API.</strong> Legacy mainframe "
            "systems expose 3270 terminal screens. Testing these via "
            "screen-scraping tools (Micro Focus Rumba, BlueZone) is "
            "brittle. Modern approaches wrap mainframe functions in APIs "
            "(IBM z/OS Connect, HCLTech's mainframe modernisation services) "
            "and test via standard API tools.",
            "<strong>Parallel runs.</strong> When migrating from mainframe "
            "to a new platform, both systems run in parallel for months. "
            "Outputs (GL postings, customer statements, regulatory reports) "
            "are compared automatically to ensure the new system produces "
            "identical results.",
        ])

        + H3("5.3  Model validation testing")
        + p("Credit risk models, fraud models, and pricing models require "
            "specialised testing beyond functional testing:")
        + ul([
            "<strong>Back-testing.</strong> Run the model on historical data "
            "and compare predictions to actual outcomes. A credit scoring "
            "model that predicted a 2% default rate but the actual rate was "
            "5% has failed back-testing.",
            "<strong>Sensitivity analysis.</strong> Vary inputs systematically "
            "to understand how the model responds. A pricing model that "
            "produces wildly different results for small input changes is "
            "unstable.",
            "<strong>Benchmark testing.</strong> Compare the model's output "
            "against a simpler benchmark model (logistic regression) or "
            "an industry benchmark. If the complex model doesn't "
            "outperform the benchmark, the added complexity isn't justified.",
            "<strong>Champion-challenger testing.</strong> Run the new model "
            "(challenger) alongside the current model (champion) in shadow "
            "mode and compare results before switching.",
        ])

        + H3("5.4  Testing AI/ML systems in BFSI")
        + p("AI/ML testing extends beyond traditional testing because "
            "ML models are non-deterministic and data-dependent:")
        + ul([
            "<strong>Data validation.</strong> Test that training data is "
            "representative, unbiased, and complete. Great Expectations "
            "(open-source) validates data pipelines.",
            "<strong>Fairness testing.</strong> Test for disparate impact "
            "across protected classes (gender, race, age). Tools: IBM "
            "AI Fairness 360, Google What-If Tool, Fiddler AI.",
            "<strong>Adversarial testing.</strong> Test the model against "
            "adversarial inputs designed to fool it (e.g., slightly "
            "modified images for facial recognition, crafted transactions "
            "for fraud models).",
            "<strong>Drift testing.</strong> Monitor model performance "
            "over time and alert when accuracy degrades. Tools: Evidently "
            "AI, WhyLabs, Arize, Fiddler.",
        ])
    )
    return TopicSection(
        "5.  Advanced — microservices testing, mainframe, model validation, AI",
        "advanced", body)


# ------------------------------------------------------------------ sec 6

def _sec6() -> TopicSection:
    body = (
        p("Testing requirements are explicitly or implicitly mandated by "
          "regulators across all major jurisdictions:")
        + table(
            ["Region", "Key testing-related regulations"],
            [
                ["<strong>European Union</strong>",
                 "<strong>EU DORA (Jan 2025)</strong> — mandates ICT testing "
                 "frameworks including TLPT (Threat-Led Penetration Testing) "
                 "for significant financial entities, based on TIBER-EU. "
                 "Requires regular testing of ICT systems and tools. "
                 "<strong>ECB SSM</strong> — expects model validation and "
                 "testing for IRB approaches. <strong>EBA Guidelines on ICT "
                 "and Security Risk Management</strong> — require testing of "
                 "changes before deployment. <strong>PCI DSS 4.0</strong> — "
                 "updated testing requirements for cardholder data environments."],
                ["<strong>United Kingdom</strong>",
                 "<strong>PRA SS2/21</strong> (Outsourcing and Third Party Risk) "
                 "— requires testing of outsourced services. <strong>FCA "
                 "Operational Resilience (PS21/3)</strong> — banks must test "
                 "Important Business Services against impact tolerances "
                 "(fully embedded Mar 2025). <strong>CBEST</strong> — UK's "
                 "threat-led penetration testing framework for systemically "
                 "important firms. <strong>PRA SS1/23</strong> — model risk "
                 "management requires validation testing."],
                ["<strong>United States</strong>",
                 "<strong>OCC Heightened Standards (12 CFR 30 Appendix D)</strong> "
                 "— require testing and validation of risk management processes. "
                 "<strong>Fed SR 11-7</strong> — model validation including "
                 "testing. <strong>FFIEC IT Examination Handbook</strong> — "
                 "comprehensive IT testing expectations. <strong>CCAR/DFAST "
                 "stress testing</strong> — models and processes tested annually. "
                 "<strong>PCI DSS</strong> — quarterly ASV scans, annual pen tests."],
                ["<strong>Singapore</strong>",
                 "<strong>MAS Technology Risk Management (TRM) Guidelines</strong> "
                 "— require system and integration testing, security testing, "
                 "UAT, performance testing, and regression testing before "
                 "deployment. Explicitly state that test environments must not "
                 "use production data without masking. <strong>MAS Cyber "
                 "Hygiene Notice</strong> — penetration testing requirements."],
                ["<strong>India</strong>",
                 "<strong>RBI IT Governance Master Direction (Nov 2023)</strong> "
                 "— banks must have documented testing frameworks, change "
                 "management procedures, and test environments. <strong>RBI "
                 "Cyber Security Framework</strong> — mandates vulnerability "
                 "assessment and penetration testing (VAPT). <strong>SEBI "
                 "Technical Standards for Stock Exchanges</strong> — capacity "
                 "testing requirements. <strong>IRDAI IT Guidelines</strong> — "
                 "testing requirements for insurance systems."],
            ]
        )
    )
    return TopicSection(
        "6.  BFSI / domain regulatory overlay", "advanced", body)


# ------------------------------------------------------------------ sec 7

def _sec7() -> TopicSection:
    body = (
        table(
            ["Decision", "Option A", "Option B", "Key trade-off"],
            [
                ["<strong>Full regression vs. risk-based regression</strong>",
                 "Run the full 100,000-test regression suite for every release",
                 "Use impact analysis to run only affected tests (10–30%)",
                 "Full regression catches more but takes days. Risk-based is "
                 "faster but requires accurate dependency mapping. Most mature "
                 "banks use risk-based for minor releases, full for major."],
                ["<strong>Test automation ratio</strong>",
                 "Target 80–90% automation (industry best practice)",
                 "Accept 40–50% automation (current reality at most banks)",
                 "Higher automation enables faster releases but requires "
                 "significant upfront investment and maintenance. Legacy "
                 "mainframe and packaged applications are hardest to automate."],
                ["<strong>Production data vs. synthetic data for testing</strong>",
                 "Use masked production data (realistic but privacy-controlled)",
                 "Use synthetic data (fully artificial, no privacy risk)",
                 "Masked production data is more realistic but has residual "
                 "privacy risk and requires ongoing masking pipelines. "
                 "Synthetic data is privacy-safe but may miss edge cases."],
                ["<strong>In-house testing team vs. managed testing services</strong>",
                 "Build in-house QA team with domain expertise",
                 "Outsource to managed testing providers (HCLTech, Wipro, "
                 "Cognizant, Capgemini, Accenture)",
                 "In-house has deeper domain knowledge. Outsourced scales "
                 "faster and has broader tool expertise. Most banks use a "
                 "hybrid: in-house for critical/regulatory, outsourced for "
                 "volume regression and automation."],
                ["<strong>Shift-left vs. traditional testing gates</strong>",
                 "Developers own testing; quality gates in CI pipeline",
                 "Separate QA team with formal test phases (SIT, UAT, PT)",
                 "Shift-left is faster but requires developer testing "
                 "discipline. Traditional gates provide more formal evidence "
                 "for regulators. Best practice: shift-left with formal "
                 "UAT/regulatory gates retained."],
                ["<strong>Selenium vs. Playwright for UI automation</strong>",
                 "Continue with Selenium (existing investment, broad ecosystem)",
                 "Migrate to Playwright (faster, more reliable, modern)",
                 "Selenium has the largest BFSI installed base but is aging. "
                 "Playwright is technically superior but requires rewriting "
                 "existing suites. Recommend Playwright for new projects, "
                 "Selenium maintenance for legacy."],
            ]
        )
    )
    return TopicSection(
        "7.  Trade-offs and decisions a leader owns", "intermediate", body)


# ------------------------------------------------------------------ sec 8

def _sec8() -> TopicSection:
    body = (
        example(
            "TSB UK migration disaster (April 2018) — the ultimate testing failure",
            p("TSB migrated 1.3 billion customer records from Lloyds' legacy "
              "platform to Sabadell's Proteo4UK core banking system over a "
              "weekend. The migration was insufficiently tested: (1) performance "
              "testing did not simulate real customer behaviour patterns, "
              "(2) batch processing in the new system had untested edge cases, "
              "(3) the mobile/internet banking platform was not tested against "
              "the full range of customer scenarios. Result: 1.9 million "
              "customers locked out, some customers saw other people's "
              "accounts, the CEO resigned, and the total cost exceeded "
              "GBP 330M. The FCA enforcement report explicitly cited "
              "inadequate testing as a root cause. The PRA fined TSB GBP "
              "48.65M. Lesson: a multi-billion-record migration requires "
              "months of parallel running, not a weekend cutover.")
        )
        + example(
            "UPI's journey to 14 billion transactions/month — performance "
            "testing at national scale",
            p("India's UPI (Unified Payments Interface) processed 14.04 "
              "billion transactions in December 2024 (₹23.25 lakh crore). "
              "NPCI (National Payments Corporation of India) and the "
              "participating banks conduct rigorous performance testing: "
              "(1) annual capacity planning exercises simulate 3x current "
              "peak volume, (2) banks must certify their UPI switches can "
              "handle allocated TPS (transactions per second) before going "
              "live, (3) NPCI runs 'war rooms' on predicted spike days "
              "(salary day, festive days, IPL match days). The testing "
              "infrastructure includes dedicated performance-testing "
              "environments that mirror production topology. When a bank "
              "fails performance certification, NPCI can throttle their "
              "UPI volume until remediation.")
        )
        + example(
            "A European bank's Basel III.1 regulatory UAT",
            p("A Tier-1 European bank implemented Basel III.1 capital "
              "requirements (EU CRR3, in force 1 Jan 2025). The regulatory "
              "UAT process: (1) the Risk team defined 850 test scenarios "
              "covering FRTB SA (Standardised Approach), output floors, "
              "credit risk SA revisions, and CVA risk, (2) each scenario "
              "had a manually calculated expected result from the Risk "
              "methodology team, (3) the system was run with test data "
              "and outputs compared to expected results — 17 scenarios "
              "failed on first pass due to rounding differences in the "
              "output floor calculation, (4) after defect fixes and re-test, "
              "all 850 scenarios passed, (5) the CRO signed off the UAT "
              "pack, which was submitted to the ECB as evidence of "
              "readiness. Total UAT duration: 14 weeks. Total UAT cost: "
              "EUR 2.8M (including business and vendor resources).")
        )
        + example(
            "An Indian bank's test data masking programme",
            p("A large Indian private-sector bank had 3,200 test environments "
              "using copies of production data — containing Aadhaar numbers, "
              "PAN details, mobile numbers, and account balances for 80 "
              "million customers. After the DPDP Act 2023 and RBI's "
              "emphasis on data protection, the bank implemented a test "
              "data masking programme: (1) deployed Delphix for dynamic "
              "data masking across all non-production environments, "
              "(2) defined masking rules: Aadhaar replaced with synthetic "
              "12-digit numbers, PAN replaced with format-preserving "
              "synthetic values, names replaced with realistic Indian "
              "names, balances randomised within ±20% of original, "
              "(3) referential integrity preserved — the same customer "
              "appears consistently across all tables, (4) masking runs "
              "nightly as part of the environment refresh pipeline. "
              "Result: full DPDP compliance in test environments, with "
              "no degradation in test quality. Annual cost: ₹3.5 crore "
              "for the platform plus ₹1.5 crore for the masking team.")
        )
        + example(
            "A global insurer's Guidewire testing factory",
            p("A global P&C insurer rolling out Guidewire InsuranceSuite "
              "across 12 European markets established a centralised testing "
              "factory. The factory: (1) maintains a shared Selenium-based "
              "regression suite of 15,000 test cases covering PolicyCenter, "
              "ClaimCenter, and BillingCenter, (2) uses Cucumber/Gherkin "
              "for BDD — business analysts in each market write scenarios "
              "in English; automation engineers implement step definitions, "
              "(3) runs the full regression nightly across all markets in "
              "parallel using a Selenium Grid on AWS, (4) uses Tricentis "
              "qTest for test management with full traceability from "
              "requirements to test cases to defects. The testing factory "
              "employs 120 people (mix of in-house and HCLTech managed "
              "testing). Annual cost: EUR 8M. The factory reduced "
              "production defects by 60% and release cycle time from "
              "8 weeks to 3 weeks.")
        )
    )
    return TopicSection(
        "8.  Worked examples — numbers and decisions", "intermediate", body)


# ------------------------------------------------------------------ sec 9

def _sec9() -> TopicSection:
    body = (
        H3("9.1  Questions a leader asks in any review")
        + ol([
            "What is our test automation ratio, and what is our target by "
            "segment (unit, integration, E2E, regression)?",
            "How long does a full regression run take, and is it on the "
            "critical path for every release?",
            "Do we have risk-based regression — can we intelligently select "
            "which tests to run based on the change?",
            "What is our performance testing strategy for peak days "
            "(salary day, year-end, IPO), and when was the last capacity test?",
            "How are we managing test data — are we using production data "
            "in non-production environments, and is it masked?",
            "What security testing is integrated into our CI/CD pipeline "
            "(SAST, SCA, DAST)?",
            "When was our last penetration test, and have all critical "
            "findings been remediated?",
            "How do we test regulatory changes — is there a formal "
            "regulatory UAT process with sign-off?",
            "Are our test environments representative of production "
            "(topology, data volume, integrations)?",
            "What is our DORA TLPT readiness, and have we conducted a "
            "threat-led penetration test?",
            "How are we testing AI/ML models — do we have fairness "
            "testing, back-testing, and drift monitoring?",
            "What is our defect leakage rate to production, and what is "
            "the trend?",
        ])
        + H3("9.2  Red flags")
        + red_flag(ul([
            "'We test manually because our systems are too complex to "
            "automate.' — This means releases will be slow, expensive, and "
            "error-prone. Complexity is the reason to automate, not the "
            "reason not to.",
            "'We use production data for testing — it's the most realistic.' "
            "— This likely violates GDPR, DPDP Act, and PDPA. If real "
            "customer PII is in test environments, it is a compliance "
            "breach waiting to be discovered by an auditor.",
            "'Our developers don't write tests — that's QA's job.' — This "
            "is a cultural failure. Developers who don't write unit tests "
            "produce code with 3–5x more defects. Shift-left requires "
            "developer-owned testing.",
            "'We skip performance testing because our cloud infrastructure "
            "auto-scales.' — Auto-scaling has limits, costs, and lag time. "
            "A UPI switch that can't handle salary-day volume will not be "
            "saved by auto-scaling that takes 3 minutes to provision new "
            "pods when transactions arrive in milliseconds.",
            "'Regulatory UAT is just a sign-off — we don't need test cases.' "
            "— Auditors will ask for UAT evidence: test cases, expected "
            "results, actual results, defect logs, sign-off records. "
            "'Just a sign-off' is an audit finding.",
            "'We'll test in production — that's the DevOps way.' — "
            "Observability-driven production validation is part of a "
            "mature testing strategy, not a replacement for pre-production "
            "testing. 'Testing in production' for financial calculations "
            "means customers are the testers.",
            "'Our testing is outsourced, so we don't need to manage it.' — "
            "Testing accountability cannot be outsourced. The bank is "
            "responsible for quality. Outsourced testing requires strong "
            "governance, defined SLAs, and in-house quality leadership.",
            "'We have 100% code coverage so we have no bugs.' — Code "
            "coverage measures lines executed, not logic validated. 100% "
            "coverage with poor assertions catches nothing. Focus on "
            "mutation testing and meaningful assertions.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("Regression testing", "Re-running existing tests after a change "
             "to verify that previously working functionality still works."),
            ("UAT", "User Acceptance Testing — business users validate that "
             "the system meets their requirements before go-live."),
            ("SAST", "Static Application Security Testing — scanning source "
             "code for security vulnerabilities without executing it."),
            ("DAST", "Dynamic Application Security Testing — testing a running "
             "application for security vulnerabilities."),
            ("SCA", "Software Composition Analysis — identifying known "
             "vulnerabilities in open-source dependencies."),
            ("TLPT", "Threat-Led Penetration Testing — simulated cyber-attack "
             "using real threat intelligence, mandated by EU DORA."),
            ("TIBER-EU", "Threat Intelligence-Based Ethical Red Teaming — the "
             "European framework for TLPT."),
            ("TDM", "Test Data Management — the discipline of providing "
             "realistic, compliant test data to test environments."),
            ("Service virtualisation", "Simulating external services and "
             "dependencies so systems can be tested in isolation."),
            ("Contract testing", "Verifying that API producers and consumers "
             "agree on the API contract (request/response format)."),
            ("Shift-left", "Moving testing activities earlier in the "
             "development lifecycle to catch defects sooner and cheaper."),
            ("BDD", "Behaviour-Driven Development — writing tests in natural "
             "language (Given/When/Then) to bridge business and technology."),
            ("Canary deployment", "Releasing a change to a small subset of "
             "users/traffic first, validating, then expanding."),
            ("Feature flag", "A toggle that enables or disables a feature "
             "without deploying new code, decoupling deployment from release."),
            ("Mutation testing", "Automatically introducing small code changes "
             "(mutations) and checking if tests detect them — measures test "
             "quality, not just coverage."),
            ("Defect leakage", "The percentage of defects that escape "
             "pre-production testing and are found in production."),
            ("Parallel run", "Running old and new systems simultaneously and "
             "comparing outputs to validate migration correctness."),
        ])
    )
    return TopicSection(
        "9.  Questions, red flags, and glossary", "basic", body)
