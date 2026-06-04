"""Infrastructure & Operations · 02 — DevOps and SRE in depth:
CI/CD pipelines, Infrastructure as Code, platform engineering,
incident management, DORA metrics, and reliability at scale."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="IV.2",
        slug="02-devops-sre-deep",
        title="DevOps and Site Reliability Engineering in depth",
        one_liner=(
            "IV.1 showed you what cloud-native operations looks like; this topic "
            "takes you inside the engine room. We cover CI/CD pipelines at "
            "banking scale, Infrastructure as Code, platform engineering, "
            "incident command systems, the four DORA metrics in practice, and "
            "the human side of reliability. By the end you can lead a DevOps "
            "transformation or an SRE function in any tier-1 bank."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9(), _sec10()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("DevOps is a cultural and technical movement (born 2009) that "
              "breaks down the wall between Development and Operations. "
              "SRE (Site Reliability Engineering, born at Google in 2003) "
              "is a specific implementation of DevOps: treat operations as "
              "software engineering, measure reliability with SLOs, and use "
              "error budgets to balance speed against stability. "
              "<strong>Platform engineering</strong> (the 2020s evolution) "
              "productises the internal platform so application teams can "
              "self-serve infrastructure without becoming infrastructure "
              "experts. In BFSI, all three are now mandatory for "
              "regulatory compliance, not optional optimisations.")
        )
        + H3("0.1  IT-side anchor — your smartphone app updates")
        + it_anchor(
            p("Your smartphone updates apps automatically while you sleep. "
              "You do not call Apple or Samsung to ask when the next "
              "WhatsApp version will arrive; it just appears. Behind that "
              "is a pipeline: code commit → build → test → sign → deploy. "
              "That pipeline is CI/CD (Continuous Integration / Continuous "
              "Delivery). Now imagine the same thing for a bank’s loan "
              "origination system: a developer commits a fix for an interest-"
              "calculation bug, and within hours (not weeks) it is in "
              "production, tested, compliant, and observable. That requires "
              "the same discipline as your smartphone, but with far more "
              "safety checks because money is involved.")
        )
        + H3("0.2  BFSI-side anchor — the monthly regulatory report")
        + bfsi_anchor(
            p("Every month, your bank submits a regulatory report (Liquidity "
              "Coverage Ratio, NPA classification, FX exposure). The data "
              "comes from a dozen systems, stitched together by hand in "
              "spreadsheets, reviewed by three people, then uploaded to a "
              "portal. It takes four days and nobody trusts the numbers. "
              "DevOps thinking says: automate the extraction, automate the "
              "validation, automate the submission, and monitor the pipeline "
              "like a production service. SRE thinking adds: define an SLO "
              "(the report must be submitted by T-2 with 99.9% accuracy), "
              "measure error budget (how many rows were wrong last month), "
              "and hold someone accountable for reliability. Both mindsets "
              "turn a manual ordeal into a reliable system.")
        )
        + H3("0.3  The five deep topics we will cover")
        + ul([
            "<strong>CI/CD pipelines at scale</strong> — multi-environment, "
            "multi-region, with compliance gates and rollback strategies.",
            "<strong>Infrastructure as Code (IaC)</strong> — Terraform, "
            "Pulumi, CDK, and the testing / security / drift-detection "
            "ecosystem around it.",
            "<strong>Platform engineering</strong> — Internal Developer "
            "Platforms (IDP), golden paths, developer experience (DX), "
            "and the team topology that makes it work.",
            "<strong>Incident management and reliability culture</strong> "
            "— incident command, blameless postmortems, toil budgets, "
            "chaos engineering at banking scale.",
            "<strong>DORA metrics and continuous improvement</strong> — "
            "deploy frequency, lead time, MTTR, change failure rate; "
            "how to measure them honestly and improve them without gaming.",
        ])
    )
    return TopicSection(
        "0.  Primer — DevOps, SRE, and platform engineering",
        "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Why does DevOps matter enough to have its own regulatory "
          "expectations in BFSI?")
        + ol([
            "<strong>Speed without safety is now a compliance risk.</strong> "
            "EU DORA Article 8 (ICT risk management) and UK PRA SS2/13 "
            "both expect ‘rapid and reliable software updates’ as part of "
            "operational resilience. Slow patching is a reportable incident.",
            "<strong>Manual change is a concentration risk.</strong> "
            "Regulators now ask: ‘How many people know how to deploy the "
            "core ledger?’ If the answer is ‘two, and they are both on holiday,’ "
            "that is a risk. IaC and automated pipelines capture knowledge "
            "in code, not in heads.",
            "<strong>Auditability requires immutable history.</strong> "
            "GitOps (state declared in Git, reconciled automatically) gives "
            "regulators an auditable trail: who changed what, when, and "
            "what tests ran. Manual deployments leave no trail.",
            "<strong>Cloud spend optimisation depends on automation.</strong> "
            "FinOps (IV.1) requires tagging, rightsizing, and scheduling. "
            "All of those are implemented in CI/CD and IaC pipelines; without "
            "them, waste is guaranteed.",
            "<strong>Talent retention.</strong> "
            "Engineers leave banks that make them fight manual tickets to "
            "provision a VM. A modern IDP is a recruiting tool; its absence "
            "is a retention risk.",
        ])
    )
    return TopicSection(
        "1.  Why DevOps and SRE are now regulatory topics",
        "basic", body)


def _sec2() -> TopicSection:
    diagram = (
        "flowchart TB\n"
        '  subgraph "Developer"\n'
        '    IDE["IDE / Editor"]\n'
        '    PR["Pull Request"]\n'
        "  end\n"
        '  subgraph "CI Pipeline"\n'
        '    BUILD["Build / Compile"]\n'
        '    UNIT["Unit Tests"]\n'
        '    SAST["SAST / SCA<br/>SonarQube, Snyk, Checkmarx"]\n'
        "    BUILD --> UNIT --> SAST\n"
        "  end\n"
        '  subgraph "Artifact Store"\n'
        '    REG["Container Registry<br/>Signed image, SBOM"]\n'
        "  end\n"
        '  subgraph "CD Pipeline"\n'
        '    DAST["DAST / Pen-test"]\n'
        '    STAGE["Deploy to Staging"]\n'
        '    INTEG["Integration Tests<br/>Contract Tests"]\n'
        '    POLICY["Policy Gate<br/>OPA / Kyverno"]\n'
        '    PROD["Deploy to Production<br/>Canary / Blue-green"]\n'
        "    DAST --> STAGE --> INTEG --> POLICY --> PROD\n"
        "  end\n"
        '  subgraph "Runtime"\n'
        '    K8S["Kubernetes Cluster"]\n'
        '    OBS["Observability<br/>OTel → Backend"]\n'
        "  end\n"
        "  IDE --> PR --> BUILD\n"
        "  SAST --> REG\n"
        "  REG --> DAST\n"
        "  PROD --> K8S --> OBS"
    )
    body = mermaid(
        diagram,
        "A BFSI-grade CI/CD pipeline: build → security scan → artifact → "
        "deploy → policy gate → production with observability.")
    return TopicSection(
        "2.  The picture — a BFSI-grade CI/CD pipeline",
        "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  CI/CD phases and gates")
        + ul([
            "<strong>Source</strong> — commit to trunk or merge request; "
            "trigger webhook to CI server.",
            "<strong>Build</strong> — compile, package, create container "
            "image. Deterministic: same source → same binary.",
            "<strong>Unit test</strong> — fast, in-memory tests; fail the "
            "pipeline if coverage drops below threshold.",
            "<strong>SAST (Static Application Security Testing)</strong> — "
            "SonarQube, Checkmarx, Semgrep, CodeQL; find SQL injection, "
            "hardcoded secrets, vulnerable dependencies.",
            "<strong>SCA (Software Composition Analysis)</strong> — Snyk, "
            "JFrog Xray, Mend; check for CVEs in open-source libraries.",
            "<strong>Artifact storage</strong> — signed container image, "
            "SBOM generated, provenance attestation (Sigstore/cosign).",
            "<strong>DAST (Dynamic Application Security Testing)</strong> — "
            "OWASP ZAP, Burp Suite; test running application for runtime "
            "vulnerabilities.",
            "<strong>Integration / contract tests</strong> — Pact, Spring "
            "Cloud Contract; verify API contracts with downstream systems.",
            "<strong>Policy gate</strong> — OPA, Kyverno, Open Policy Agent; "
            "enforce ‘no critical CVEs,’ ‘resource limits declared,’ ‘no root "
            "user.’",
            "<strong>Deploy strategy</strong> — canary (5% traffic), blue-green "
            "(instant switch), rolling (gradual replacement).",
            "<strong>Smoke tests / synthetic monitoring</strong> — verify "
            "critical paths immediately after deploy.",
        ])
        + H3("3.2  Pipeline tools by category")
        + table(
            ["Category", "Open source", "Cloud-native", "Enterprise"],
            [
                ["CI server", "Jenkins, GitLab CE, Drone, Concourse",
                 "GitHub Actions, AWS CodeBuild, Azure DevOps",
                 "CloudBees, GitLab EE, GitHub Enterprise"],
                ["GitOps", "Argo CD, Flux, Tekton",
                 "AWS CodeDeploy, Azure Arc",
                 "Weave GitOps Enterprise"],
                ["Security scanning", "Trivy, Grype, Semgrep, ZAP",
                 "AWS Inspector, Azure Defender",
                 "Snyk, Checkmarx, SonarQube Enterprise"],
                ["Artifact registry", "Harbor, Nexus, JFrog OSS",
                 "ECR, ACR, GCR, Artifact Registry",
                 "JFrog Artifactory, Sonatype Nexus Pro"],
                ["Secrets", "External Secrets Operator, Sealed Secrets",
                 "AWS Secrets Manager, Azure Key Vault",
                 "HashiCorp Vault Enterprise, CyberArk"],
            ]
        )
        + H3("3.3  Multi-environment promotion")
        + p("BFSI requires at least four environments before production:")
        + ul([
            "<strong>Dev</strong> — developer sandbox; unstable by design.",
            "<strong>CI / Integration</strong> — shared testing of pull requests; "
            "ephemeral, spun up per branch.",
            "<strong>Staging / Pre-prod</strong> — production-like, shared, "
            "sized for full integration tests; sometimes called ‘QA’ or ‘UAT’.",
            "<strong>Production</strong> — live customer traffic; changes only "
            "via pipeline, never manual.",
        ])
        + p("Promotion rules: artifact built once, promoted unchanged; "
            "configuration per environment via ConfigMap / external secrets; "
            "no ‘it works on my machine’ because containers are identical.")
        + H3("3.4  Rollback strategies")
        + ul([
            "<strong>Blue-green</strong> — maintain two identical environments; "
            "switch traffic instantly; keep old version warm for instant "
            "rollback. Cost: 2× infrastructure.",
            "<strong>Canary</strong> — route small percentage (5%, 10%, 25%) to "
            "new version; monitor error rate and latency; abort if SLOs breached; "
            "ramp to 100% over hours. Cost: minimal overhead.",
            "<strong>Feature flags</strong> — code is deployed dark; flag enables "
            "feature per user cohort. Rollback is a flag flip, not a deploy. "
            "Tools: LaunchDarkly, Split, Unleash, OpenFeature (CNCF).",
            "<strong>Database migrations</strong> — hardest part. Backward-"
            "compatible schema changes (expand-contract pattern); data "
            "migration as separate job; never drop column in same release "
            "that stops writing to it.",
        ])
    )
    return TopicSection(
        "3.  How CI/CD works at banking scale — phases, tools, "
        "environments, rollbacks",
        "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  Infrastructure as Code — the basics")
        + p("IaC means defining infrastructure (networks, VMs, databases, "
            "Kubernetes clusters, IAM policies) in declarative files, "
            "versioned in Git, applied automatically. Benefits: repeatability, "
            "auditability, drift detection, disaster recovery.")
        + ul([
            "<strong>Terraform</strong> (HashiCorp, 2014) — de facto standard; "
            "HCL language; state file in S3 / Terraform Cloud; modules for "
            "reuse; providers for AWS, Azure, GCP, Kubernetes, and 2000+ others.",
            "<strong>Pulumi</strong> (2018) — TypeScript, Python, Go, C# instead "
            "of HCL; imperative style; good for complex logic.",
            "<strong>AWS CDK / CDKTF</strong> — define infrastructure in "
            "TypeScript/Python; synthesises to CloudFormation or Terraform.",
            "<strong>CloudFormation / ARM / Deployment Manager</strong> — "
            "cloud-native IaC; vendor lock-in but tight integration.",
            "<strong>Ansible / Chef / Puppet</strong> — configuration management "
            "(not strictly IaC); still used for VM bootstrapping.",
        ])
        + H3("4.2  Terraform at scale — patterns and pitfalls")
        + ul([
            "<strong>Module registry</strong> — internal modules for ‘approved "
            "EKS cluster,’ ‘compliant S3 bucket with logging’; semantic "
            "versioning; enforced via CI.",
            "<strong>Workspace per environment</strong> — dev, staging, prod "
            "Terraform workspaces; separate state files; separate IAM roles.",
            "<strong>State file protection</strong> — state contains secrets; "
            "store in S3 with SSE-KMS, versioning, locking via DynamoDB.",
            "<strong>Drift detection</strong> — nightly Terraform plan in CI; "
            "alert if reality differs from code (someone made a console change).",
            "<strong>Policy as Code for IaC</strong> — Checkov, tfsec, "
            "Terrascan; enforce ‘no open security groups,’ ‘S3 must have "
            "versioning,’ ‘EKS must have private endpoints.’",
        ])
        + H3("4.3  GitOps — the next level of IaC")
        + p("GitOps (coined by Weaveworks, 2017) applies the same Git-centric "
            "workflow to Kubernetes and infrastructure:")
        + ol([
            "Declarative: desired state in Git (YAML manifests, Helm charts, "
            "Terraform plans).",
            "Versioned and immutable: Git is the single source of truth.",
            "Pulled automatically: in-cluster controllers (Argo CD, Flux) "
            "continuously reconcile cluster to Git.",
            "Continuously reconciled: drift is auto-corrected; alerts fire if "
            "reconciliation fails.",
        ])
        + p("Benefits for BFSI: audit trail (who merged what when); rollback "
            "(revert a Git commit); separation of duties (developers propose, "
            "approvers merge, controllers apply).")
        + H3("4.4  Testing infrastructure code")
        + ul([
            "<strong>Static analysis</strong> — terraform validate, tflint, "
            "checkov.",
            "<strong>Unit tests</strong> — Terratest (Go), kitchen-terraform "
            "(Ruby); spin up infra in test account, verify outputs, destroy.",
            "<strong>Contract tests</strong> — validate that module outputs "
            "match what consuming services expect.",
            "<strong>Integration tests</strong> — ephemeral environment spun "
            "up by CI, full application deployed, smoke tests run, environment "
            "destroyed.",
        ])
    )
    return TopicSection(
        "4.  Infrastructure as Code — Terraform, GitOps, testing",
        "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  From DevOps to platform engineering")
        + p("DevOps said: ‘you build it, you run it.’ Platform engineering "
            "says: ‘here is a paved road so you can run it without becoming "
            "an infrastructure expert.’ The platform team treats internal "
            "services as a product: APIs, documentation, SLAs, and a "
            "backlog driven by user research with application teams.")
        + ul([
            "<strong>Internal Developer Platform (IDP)</strong> — a self-"
            "service layer hiding complexity: provision a cluster, deploy "
            "an app, rotate a secret, view logs, all via portal or API.",
            "<strong>Golden paths</strong> — opinionated, supported "
            "templates: ‘Spring Boot on EKS with OTel, Argo CD, and "
            "Datadog.’ Teams can go off-road, but they own the support "
            "burden.",
            "<strong>Developer Experience (DX)</strong> — measure: time from "
            "‘I want a database’ to ‘I have a connection string’; time to "
            "first deploy for a new service; Mean Time To Patch (MTTP).",
        ])
        + H3("5.2  Team topologies for platform engineering")
        + table(
            ["Team type", "Purpose", "Size rule"],
            [
                ["Stream-aligned", "Deliver customer value (retail banking, "
                 "lending, payments); own feature and operation",
                 "8–12 people; full stack"],
                ["Platform", "Enable streams by providing infrastructure, "
                 "IDP, security, SRE tooling; product mindset",
                 "1 platform team per 4–8 stream teams"],
                ["Complicated Subsystem", "Deep expertise (mainframe "
                 "connectivity, risk models, cryptography); support multiple "
                 "streams",
                 "Form when cost of expertise duplication > coordination cost"],
                ["Enabling", "Help streams adopt new tech; temporary; "
                 "mentoring focus",
                 "Temporary; 2–3 people"],
            ]
        )
        + p("Reference: Team Topologies (Matthew Skelton, Manuel Pais, 2019) — "
            "the standard framework for organising engineering teams at scale.")
        + H3("5.3  IDP tooling landscape")
        + ul([
            "<strong>Backstage</strong> (Spotify, CNCF Sandbox) — most "
            "adopted IDP framework; React frontend; plugin ecosystem; "
            "Software Catalog tracks ownership; Scaffolder creates services "
            "from templates; TechDocs renders docs. Users: JPMC, Standard "
            "Chartered, ING, Netflix.",
            "<strong>Port</strong> — SaaS IDP; no-ops setup; strong "
            "workflows and scorecards.",
            "<strong>Humanitec</strong> — Platform Orchestrator; drives "
            "Terraform/Helm/Argo; workflow-centric.",
            "<strong>Cortex / Compass</strong> — SaaS IDPs with service "
            "catalog focus; Atlassian Compass integrates Jira/Confluence.",
        ])
        + H3("5.4  Service catalog and ownership")
        + p("The IDP’s heart is a catalog: every service, who owns it, what "
            "it depends on, its SLOs, on-call rotation, documentation link, "
            "API specs. This is mandatory for regulatory reporting "
            "(DORA Article 8 requires mapping of critical dependencies).")
    )
    return TopicSection(
        "5.  Platform engineering — IDP, golden paths, team topologies",
        "advanced", body)


def _sec6() -> TopicSection:
    body = (
        H3("6.1  Incident management lifecycle")
        + ol([
            "<strong>Detection</strong> — alert from observability (SLO "
            "breach), customer report, or chaos test failure. Automated "
            "ticket creation; no ‘did you see my email?’",
            "<strong>Response</strong> — incident commander (IC) declared; "
            "communication channel created (Slack, Teams, PagerDuty); "
            "on-call engineers paged.",
            "<strong>Resolution</strong> — mitigate first (rollback, scale "
            "up, disable feature flag), then diagnose. MTTR measures "
            "mitigation time, not root-cause time.",
            "<strong>Recovery</strong> — confirm service restored; monitor "
            "for regression; close incident.",
            "<strong>Postmortem</strong> — within 24–48 hours; blameless; "
            "focus on system factors; action items tracked.",
        ])
        + H3("6.2  Incident Command System")
        + p("Borrowed from emergency services and adopted by Google, Netflix, "
            "and major banks:")
        + ul([
            "<strong>Incident Commander (IC)</strong> — coordinates, does "
            "not troubleshoot; frees engineers to fix.",
            "<strong>Scribe</strong> — real-time timeline; every command run, "
            "every decision, with timestamp.",
            "<strong>Communications Lead</strong> — internal updates to "
            "leadership, external to customers/regulators if needed.",
            "<strong>Subject Matter Experts</strong> — the engineers actually "
            "fixing things; rotate out when tired.",
        ])
        + H3("6.3  Blameless postmortems")
        + p("The gold standard: Google SRE book, Etsy, PagerDuty. Rules:")
        + ol([
            "Assume good faith; people did what made sense given the info.",
            "Focus on what made the system allow the mistake.",
            "Action items are system fixes, not training or ‘be more careful’.",
            "Share widely; psychological safety requires executive sponsorship.",
        ])
        + H3("6.4  Chaos engineering at banking scale")
        + p("Principles from Netflix (Chaos Monkey, 2010) and formalised "
            "by Gremlin and AWS/Azure chaos services:")
        + ul([
            "<strong>Start in dev/test</strong> — prove the tool, then "
            "graduate to staging, then controlled prod.",
            "<strong>Minimize blast radius</strong> — one pod, one AZ, one "
            "microservice; abort conditions defined upfront.",
            "<strong>Align to SLOs</strong> — the experiment validates "
            "that SLOs survive failure modes.",
            "<strong>Regulatory relevance</strong> — UK PRA, MAS TRM, "
            "RBI all expect ‘scenario testing’; chaos engineering is the "
            "technical implementation.",
        ])
        + table(
            ["Failure mode", "Tool example", "What it proves"],
            [
                ["Random pod kill", "Chaos Monkey, Litmus", "Resilience to "
                 "node failure; PDBs work"],
                ["Network latency/packet loss", "Chaos Mesh, Toxiproxy",
                 "Timeouts and retries configured correctly"],
                ["Database slowness", "Gremlin, AWS FIS", "Connection pooling "
                 "and circuit breakers"],
                ["AZ failure", "AWS FIS AZ blackout", "Multi-AZ failover "
                 "actually works"],
                ["Certificate expiry", "Custom job", "Monitoring and "
                 "rotation alerts fire"],
            ]
        )
        + H3("6.5  Regulatory overlay — incident reporting requirements")
        + table(
            ["Regime", "Reporting trigger", "Timeline"],
            [
                ["EU DORA", "Major ICT-related incident affecting payment "
                 "services, trading, ATM network", "Initial: 4 hours; "
                 "intermediate: 72 hours; final: 1 month"],
                ["UK PRA / FCA", "Operational disruption to important "
                 "business services exceeding impact tolerance", "As soon as "
                 "practicable; no hard deadline but expectation is prompt"],
                ["RBI Cyber Security MD", "Cybersecurity incident involving "
                 "unauthorized access, data breach, ransomware", "Within 2–6 "
                 "hours depending on category"],
                ["MAS TRM", "System outage affecting critical systems; "
                 "cyber incident", "1 hour for critical; 4 hours for others"],
                ["NYDFS Part 500", "Cybersecurity event with potential "
                 "material impact", "72 hours"],
            ]
        )
    )
    return TopicSection(
        "6.  Incident management, postmortems, chaos, and regulators",
        "advanced", body)


def _sec7() -> TopicSection:
    body = (
        H3("7.1  The four DORA metrics")
        + p("DORA (DevOps Research and Assessment, founded by Nicole "
            "Forsgren, Jez Humble, Gene Kim) publishes annual benchmarks "
            "based on 30,000+ professionals. The four key metrics:")
        + table(
            ["Metric", "Elite performer", "What it measures"],
            [
                ["Deployment Frequency", "On demand (multiple per day)",
                 "How often we deliver value to production"],
                ["Lead Time for Changes", "< 1 hour (commit to production)",
                 "Velocity of the pipeline"],
                ["Time to Restore Service (MTTR)", "< 1 hour",
                 "Resilience and recovery capability"],
                ["Change Failure Rate", "< 5%",
                 "Quality of the release process"],
            ]
        )
        + p("These are outcome metrics, not vanity metrics like ‘lines of "
            "code.’ They correlate with organizational performance and, in "
            "BFSI, with operational resilience compliance.")
        + H3("7.2  Measuring honestly — avoiding gaming")
        + ul([
            "<strong>Deployment frequency</strong> — count any change to "
            "production code or config; hotfixes count; rollbacks count.",
            "<strong>Lead time</strong> — measure from commit (not story "
            "start) to production (not ‘ready for QA’).",
            "<strong>MTTR</strong> — time from detection to mitigation (not "
            "root cause).",
            "<strong>Change failure</strong> — any deployment causing "
            "incident, rollback, or hotfix; be honest, not political.",
        ])
        + H3("7.3  SLOs and error budgets in depth")
        + p("SLI (Service Level Indicator) — quantitative measure: "
            "‘latency of p99 request’ or ‘error rate.’")
        + p("SLO (Service Level Objective) — target for the SLI: ‘p99 "
            "latency < 200ms over 28-day window.’")
        + p("Error budget — (1 − SLO); how much ‘unreliability’ is allowed. "
            "If SLO is 99.9%, error budget is 0.1% = ~43 minutes/month.")
        + p("Policy: when error budget is exhausted, freeze feature "
            "releases and invest in reliability. SRE team has veto power "
            "over launches if budget is spent.")
        + H3("7.4  Toil budget")
        + p("Toil — repetitive, manual, automatable operational work. "
            "Google SRE rule: each SRE spends ≤ 50% of time on toil; ≥ 50% "
            "on engineering (automation, improving the platform). Measured "
            "quarterly; toil percentage is a team health metric.")
        + H3("7.5  Decision matrix — when to automate")
        + table(
            ["Task", "Automate if...", "Keep manual if..."],
            [
                ["Deploy to production", "Always; this is the definition of "
                 "CI/CD maturity",
                 "Emergency break-glass only; audited and rare"],
                ["Rotate TLS certificates", "Always; cert-manager, Vault",
                 "Legacy mainframe with no API"],
                ["Scale pods manually", "Never; use HPA/VPA",
                 "Emergency override during incident"],
                ["Database query tuning", "Analyse and suggest; human "
                 "approves execution",
                 "Unique one-off query; safety requires human judgment"],
                ["Alert response (page)", "Automated runbooks for known "
                 "issues; auto-remediation",
                 "Novel incident requiring investigation"],
            ]
        )
    )
    return TopicSection(
        "7.  DORA metrics, SLOs, error budgets, and toil",
        "intermediate", body)


def _sec8() -> TopicSection:
    body = (
        example(
            "Goldman Sachs — platform engineering for Marquee",
            ol([
                "Marquee (Goldman’s digital platform for institutional "
                "clients) runs on an internal platform with strict golden "
                "paths; all services instrumented with proprietary "
                "observability stack.",
                "SRE function embedded in product teams; error budgets "
                "enforced by leadership.",
                "CI/CD deploys multiple times daily; DORA metrics tracked "
                "and published internally.",
            ])
        )
        + example(
            "JPMorgan Chase — SLOs and the Resilient Architecture Council",
            ol([
                "JPMC’s Resilient Architecture Council defines SLOs for "
                "all Tier-1 services; services must meet SLOs to launch.",
                "Backstage-based IDP (internal) for service catalog and "
                "golden paths; GitOps via internal tools.",
                "Chaos testing program with AZ-level failure injection; "
                "results reviewed by risk committee.",
            ])
        )
        + example(
            "Standard Chartered — aXess platform DevOps transformation",
            ol([
                "Platform engineering team created IDP on Azure with "
                "Backstage, Argo CD, and Datadog.",
                "Golden path: ‘Java/Node service on AKS with built-in SLO "
                "dashboards, canary deploys, and policy gates.’",
                "DORA metrics tracked: from quarterly deployments to "
                "multiple daily across critical services.",
            ])
        )
        + example(
            "Santander UK — retail bank CI/CD compliance pipeline",
            ol([
                "Built mandatory compliance gates into CI/CD: every deploy "
                "must pass SAST, DAST, SCA, and policy checks.",
                "GitOps with Flux for Kubernetes workloads; Terraform for "
                "Azure infrastructure.",
                "Incident management integrated with FCA operational "
                "resilience reporting; automated timeline for postmortems.",
            ])
        )
        + example(
            "Hypothetical: 18-month DevOps transformation at a regional bank",
            ol([
                "Month 1–2: Assessment — DORA baseline, toil survey, IDP "
                "prototype with Backstage.",
                "Month 3–6: Platform foundation — CI/CD on GitHub Actions, "
                "EKS clusters, Terraform modules, golden path templates.",
                "Month 7–12: Migration — pilot with 5 services; SLOs "
                "defined; SRE rotation established; error budget policy.",
                "Month 13–18: Scale — 50 services on platform; chaos "
                "testing program; FinOps integration; first regulator "
                "demonstration of automated recovery.",
            ])
        )
    )
    return TopicSection(
        "8.  Worked examples — five real-world DevOps/SRE journeys",
        "intermediate", body)


def _sec9() -> TopicSection:
    body = (
        ol([
            "What are our four DORA metrics, and are we elite, high, medium, "
            "or low performers? What is the trend over the last 6 months?",
            "Which tier-1 services have defined SLOs and error budgets? "
            "How many error budgets were exhausted last quarter?",
            "What percentage of operational work is toil? What is the "
            "plan to reduce the highest-toil services?",
            "How long from ‘git commit’ to ‘production deploy’ for the "
            "median service? What is the bottleneck?",
            "What is our change failure rate? For failed changes, what is "
            "the MTTR? Do we prioritize speed or recovery?",
            "Is our IDP adoption voluntary or mandatory? What percentage "
            "of services use the golden path?",
            "How many manual steps remain in our production deployment "
            "process? Can any be automated?",
            "What is our incident MTTR trend? Are postmortems completed "
            "within 24 hours? Are action items resolved?",
            "Do we run chaos experiments in production? What was the "
            "last unexpected finding?",
            "What is our mean time to patch a critical CVE end-to-end? "
            "How does that compare to regulator expectations?",
            "Are SAST, DAST, and SCA gates mandatory in CI/CD? What "
            "exceptions exist, and who approved them?",
            "Do we have drift detection for IaC? When did we last find "
            "untracked manual changes in production?",
        ])
    )
    return TopicSection(
        "9.  Questions a leader asks in any DevOps/SRE review",
        "basic", body)


def _sec10() -> TopicSection:
    body = (
        red_flag(ul([
            "‘We deploy 50 times a day, so we are elite.’ — Counting "
            "deploys without measuring change failure rate or MTTR is "
            "vanity. Elite means all four DORA metrics, not one.",
            "‘Our SLO is 99.99%’ — Without defining the SLI, the window, "
            "and the error budget policy, this is a slogan not an SLO.",
            "‘Toil is just part of the job.’ — No; toil >50% means the "
            "platform is failing and people will burn out.",
            "‘We don’t need an IDP; engineers can learn K8s.’ — They can, "
            "but they should focus on business logic. Platform teams exist "
            "to abstract complexity.",
            "‘GitOps is just CI/CD with Git.’ — No; GitOps is pull-based, "
            "continuously reconciled, and declarative. CI/CD alone lacks "
            "drift correction.",
            "‘We’ll automate later; speed first.’ — Manual process accretes "
            "and calcifies. Automate from day one; speed comes from "
            "automation.",
            "‘Terraform is too risky; console is safer.’ — Console changes "
            "are untracked, unaudited, and drift from code. IaC is safer "
            "with proper review and testing.",
            "‘Chaos engineering is just breaking things randomly.’ — "
            "Professional chaos is hypothesis-driven, blast-radius-limited, "
            "and aligned to SLOs.",
            "‘Postmortems should identify who made the mistake.’ — Blameful "
            "postmortems drive incidents underground. Blameless culture is "
            "safety-critical.",
            "‘Our MTTR is 2 hours because that is our SLA.’ — MTTR is "
            "measured from reality, not set by contract. If actual MTTR is "
            "longer, fix it; don’t redefine it.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("CI/CD", "Continuous Integration / Continuous Delivery — "
                "automated build, test, and deploy pipeline."),
            ("SAST", "Static Application Security Testing — analyse source "
                "code for vulnerabilities without executing it."),
            ("DAST", "Dynamic Application Security Testing — test running "
                "application for vulnerabilities."),
            ("SCA", "Software Composition Analysis — scan open-source "
                "dependencies for known CVEs."),
            ("IaC", "Infrastructure as Code — define infrastructure in "
                "declarative files (Terraform, CloudFormation)."),
            ("GitOps", "Git-centric operations: desired state in Git, "
                "reconciled automatically by cluster controllers."),
            ("IDP", "Internal Developer Platform — self-service layer "
                "abstracting infrastructure for application teams."),
            ("Golden path", "Opinionated, supported template for common "
                "service types; teams can deviate but own the burden."),
            ("Platform engineering", "Discipline of building internal "
                "platforms as products with UX and SLAs."),
            ("DORA metrics", "Four metrics from DevOps Research and "
                "Assessment: deployment frequency, lead time, MTTR, change "
                "failure rate."),
            ("SLO", "Service Level Objective — target reliability for a "
                "service over a time window (e.g., 99.9% availability)."),
            ("SLI", "Service Level Indicator — quantitative measure "
                "underlying an SLO (e.g., error rate, latency)."),
            ("Error budget", "(1 − SLO); allowed unreliability before "
                "feature releases pause."),
            ("Toil", "Repetitive, manual, automatable operational work; "
                "SRE target is <50% of time."),
            ("MTTR", "Mean Time To Restore — time from incident detection "
                "to mitigation."),
            ("MTTD", "Mean Time To Detect — time from incident start to "
                "alert firing."),
            ("Chaos engineering", "Discipline of injecting controlled "
                "failures to validate resilience."),
            ("Postmortem", "Structured review of incident, blameless, "
                "action-item oriented."),
            ("Incident Commander", "Role coordinating incident response, "
            "separate from technical fixers."),
            ("Drift detection", "Automated comparison of deployed "
                "infrastructure against IaC definitions."),
            ("Canary deploy", "Release to small percentage of traffic, "
                "monitor, then ramp up."),
            ("Blue-green", "Two identical environments; instant traffic "
                "switch; instant rollback."),
            ("Feature flag", "Toggle enabling code paths per user "
                "cohort; decouples deploy from release."),
            ("SBOM", "Software Bill of Materials — inventory of "
                "components in an artifact; required by regulators."),
            ("Sigstore/cosign", "Open-source tooling for signing and "
                "verifying container images."),
        ])
    )
    return TopicSection("10.  Red flags + topic glossary", "basic", body)
