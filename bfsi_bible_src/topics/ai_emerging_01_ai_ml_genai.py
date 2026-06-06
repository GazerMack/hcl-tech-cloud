"""AI & Emerging Technology · 01 — AI, ML, and GenAI in BFSI."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="VIII.1",
        slug="01-ai-ml-genai-in-bfsi",
        title="AI, ML, and GenAI in BFSI — model risk, LLMOps, and regulator guardrails",
        one_liner=(
            "Every bank on earth is deploying Artificial Intelligence (AI) and Machine Learning "
            "(ML) — from credit scoring to chatbots to anti-money-laundering. Generative AI "
            "(GenAI) has accelerated the pace and the stakes. But BFSI is a regulated industry: "
            "you cannot deploy a model that denies a loan without explaining why, or hallucinate "
            "an answer about a customer's balance. This topic teaches you how AI actually works "
            "in banks, what the regulators demand, and where the traps are."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


# ------------------------------------------------------------------ 0
def _sec0() -> TopicSection:
    body = (
        primer(
            p("AI in banking is not new — credit scoring models have existed since the 1950s. "
              "What is new is the scale, the ambition, and the risk. A techno-functional leader "
              "who cannot distinguish a gradient-boosted tree from a large language model, or "
              "explain model risk to a board, will be left behind in every strategic conversation "
              "from 2025 onward.")
        )
        + H3("0.1  IT-side anchor — the spam filter on your email")
        + it_anchor(
            p("Your email's spam filter is a machine learning model. It was trained on millions "
              "of emails labelled 'spam' or 'not spam'. It learned patterns (certain words, "
              "sender reputation, link density) and now classifies new emails automatically. "
              "It occasionally gets it wrong — a legitimate email in spam (false positive) or a "
              "spam email in your inbox (false negative). Every ML model in banking works the "
              "same way: trained on historical data, deployed to make predictions, and measured "
              "by how often it gets it right versus wrong.")
        )
        + H3("0.2  BFSI-side anchor — why your credit card application was declined")
        + bfsi_anchor(
            p("When you apply for a credit card online and get an instant decision, a machine "
              "learning model made that call. It looked at your credit bureau score (CIBIL in "
              "India, FICO in the US, Experian in the UK), your income, your existing debts, "
              "your repayment history, and dozens of other features. It outputted a probability "
              "of default. If that probability exceeded the bank's threshold, you were declined. "
              "The bank is legally required (in most jurisdictions) to tell you why — which means "
              "the model must be explainable. That single requirement — explainability — shapes "
              "every AI deployment in BFSI.")
        )
        + H3("0.3  The three waves of AI in banking")
        + ol([
            "<strong>Wave 1 — Statistical models (1960s–2010s).</strong> Logistic regression, "
            "decision trees, scorecards. Used for credit scoring, fraud rules, pricing. "
            "Well-understood, highly explainable, heavily regulated (Basel IRB, Fed SR 11-7).",
            "<strong>Wave 2 — Machine learning (2010s–2023).</strong> Gradient-boosted trees "
            "(XGBoost, LightGBM), random forests, neural networks. Used for fraud detection, "
            "AML transaction monitoring, customer churn, recommendation engines. More accurate "
            "but less explainable — creating tension with regulators.",
            "<strong>Wave 3 — Generative AI (2023–present).</strong> Large Language Models (LLMs) "
            "like GPT-4, Claude, Gemini, Llama. Used for document summarisation, code generation, "
            "customer service copilots, knowledge retrieval. Powerful but prone to hallucination, "
            "bias, and data leakage — the hardest AI to govern in a regulated environment.",
        ])
    )
    return TopicSection("0.  Primer — anchored to things you already know", "basic", body)


# ------------------------------------------------------------------ 1
def _sec1() -> TopicSection:
    body = (
        p("AI exists in BFSI because banks have three things in abundance: data, repetitive "
          "decisions, and regulatory pressure to be consistent.")
        + ol([
            "<strong>Scale of decisions.</strong> A tier-1 bank makes millions of credit "
            "decisions, fraud checks, and AML alerts per day. Humans cannot review them all. "
            "ML models act as the first line of triage.",
            "<strong>Pattern recognition.</strong> Fraud patterns are subtle, fast-evolving, "
            "and cross-channel. ML models detect anomalies that rule-based systems miss.",
            "<strong>Cost pressure.</strong> Automating document review, KYC checks, and "
            "customer queries with AI saves hundreds of millions annually at tier-1 scale.",
            "<strong>Competitive pressure.</strong> Neobanks and fintechs use AI-first "
            "architectures. Incumbents must match or lose share.",
            "<strong>Regulatory expectation.</strong> Regulators increasingly expect banks to "
            "use advanced analytics for AML (FATF guidance), fraud detection, and stress testing.",
        ])
    )
    return TopicSection("1.  Why AI exists in banking — first principles", "basic", body)


# ------------------------------------------------------------------ 2
def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  subgraph "Data Layer"\n'
            '    DW["Data warehouse<br/>Data lake"]\n'
            '    FE["Feature engineering<br/>Feature store"]\n'
            '  end\n'
            '  subgraph "Model Development"\n'
            '    TR["Training<br/>Experimentation"]\n'
            '    VAL["Validation<br/>Back-testing"]\n'
            '    REG["Model registry"]\n'
            '  end\n'
            '  subgraph "Model Deployment"\n'
            '    SRV["Serving<br/>Real-time or batch"]\n'
            '    MON["Monitoring<br/>Drift detection"]\n'
            '  end\n'
            '  subgraph "Governance"\n'
            '    MRM["Model Risk<br/>Management"]\n'
            '    AUD["Audit trail<br/>Explainability"]\n'
            '    REP["Regulator<br/>reporting"]\n'
            '  end\n'
            '  DW --> FE --> TR --> VAL --> REG --> SRV --> MON\n'
            '  MON -->|"Retrain trigger"| TR\n'
            '  VAL --> MRM\n'
            '  SRV --> AUD\n'
            '  MRM --> REP',
            "The ML lifecycle in a regulated bank: data, develop, deploy, govern.")
    )
    return TopicSection("2.  The AI lifecycle in one picture", "basic", body)


# ------------------------------------------------------------------ 3
def _sec3() -> TopicSection:
    body = (
        H3("3.1  Phase 1: Data preparation and feature engineering")
        + p("Every ML model starts with data. In banking, this means transaction history, "
            "customer demographics, bureau data, behavioural signals (app usage, login patterns), "
            "and external data (market prices, geolocation). A Feature Store (e.g., Feast, "
            "Tecton, Databricks Feature Store, SageMaker Feature Store) pre-computes and serves "
            "features consistently across training and inference, preventing 'training-serving "
            "skew' — one of the top causes of model failure in production.")

        + H3("3.2  Phase 2: Model training and experimentation")
        + p("Data scientists train candidate models, track experiments (MLflow, Weights & Biases, "
            "Neptune), and compare performance metrics. For credit risk, the standard metrics are "
            "Gini coefficient, KS statistic, and AUC-ROC. For fraud, precision, recall, and the "
            "false-positive rate matter most — because every false positive is a legitimate "
            "customer whose transaction was blocked.")

        + H3("3.3  Phase 3: Model validation (the second line of defence)")
        + p("In BFSI, the team that builds the model cannot approve it for production. An "
            "independent Model Validation team (second line of defence, often under the CRO) "
            "reviews the model's methodology, data quality, performance, assumptions, and "
            "limitations. This is mandated by Fed SR 11-7 (US), PRA SS1/23 (UK), ECB Guide on "
            "Internal Models, RBI guidelines on IRB approach, and MAS guidelines. Validation "
            "typically takes 4–12 weeks and is the single biggest bottleneck in the ML lifecycle "
            "at most banks.")

        + H3("3.4  Phase 4: Deployment and serving")
        + p("Models are deployed for real-time inference (fraud scoring at transaction time, "
            "sub-100ms latency) or batch inference (monthly credit-limit reviews, portfolio "
            "stress testing). MLOps platforms (SageMaker, Vertex AI, Azure ML, Databricks, "
            "Kubeflow) manage the deployment pipeline. In BFSI, every model deployment must "
            "include a rollback plan and a 'champion-challenger' setup where the new model "
            "runs in shadow mode before taking live traffic.")

        + H3("3.5  Phase 5: Monitoring and drift detection")
        + p("Models decay over time as the world changes — this is called 'model drift'. A "
            "fraud model trained before COVID performed poorly during lockdowns because spending "
            "patterns shifted. Monitoring systems track input drift (are the features changing?), "
            "output drift (are the predictions shifting?), and performance drift (is accuracy "
            "degrading?). When drift exceeds thresholds, the model is flagged for retraining or "
            "retirement.")
    )
    return TopicSection("3.  How it actually works — the ML lifecycle phase by phase",
                        "intermediate", body)


# ------------------------------------------------------------------ 4
def _sec4() -> TopicSection:
    body = (
        H3("4.1  AI use cases by banking function")
        + table(
            ["Function", "Traditional ML use cases", "GenAI use cases (emerging)"],
            [
                ["<strong>Credit risk</strong>",
                 "Application scoring, behavioural scoring, PD/LGD/EAD models, stress testing",
                 "Automated credit memo drafting, financial statement analysis from PDFs"],
                ["<strong>Fraud</strong>",
                 "Real-time transaction scoring, device fingerprinting, network analysis",
                 "Synthetic fraud pattern generation for training, alert summarisation"],
                ["<strong>AML/KYC</strong>",
                 "Transaction monitoring, name screening, risk scoring, SAR prioritisation",
                 "KYC document extraction, adverse media screening, investigation narrative generation"],
                ["<strong>Customer service</strong>",
                 "Chatbots (intent-based), next-best-action, churn prediction",
                 "Conversational AI agents, call summarisation, complaint root-cause analysis"],
                ["<strong>Operations</strong>",
                 "Document classification, OCR, straight-through processing optimisation",
                 "Email triage, contract clause extraction, reconciliation exception explanation"],
                ["<strong>Capital markets</strong>",
                 "Algo trading signals, portfolio optimisation, pricing models",
                 "Research summarisation, earnings-call analysis, regulatory filing parsing"],
                ["<strong>Internal productivity</strong>",
                 "Code review automation, test generation, log analysis",
                 "Developer copilots (GitHub Copilot, Amazon Q), internal knowledge search (RAG)"],
            ]
        )

        + H3("4.2  GenAI architecture patterns in BFSI")
        + table(
            ["Pattern", "How it works", "BFSI example"],
            [
                ["<strong>RAG (Retrieval-Augmented Generation)</strong>",
                 "Query a vector database of bank documents, feed retrieved context to the LLM, "
                 "generate a grounded answer",
                 "Internal policy Q&A for compliance officers, product knowledge base for call-centre agents"],
                ["<strong>Copilot / assistant</strong>",
                 "LLM embedded in an existing workflow tool (IDE, CRM, case management) to "
                 "suggest actions, draft content, or explain data",
                 "Developer copilot for COBOL-to-Java migration, relationship manager copilot for client briefings"],
                ["<strong>Agentic AI</strong>",
                 "LLM orchestrates multi-step tasks by calling tools (APIs, databases, calculators) "
                 "autonomously",
                 "Automated investigation of AML alerts (query TMS, pull customer profile, check "
                 "sanctions list, draft narrative). High risk — requires human-in-the-loop for BFSI"],
                ["<strong>Fine-tuned domain model</strong>",
                 "Base LLM fine-tuned on bank-specific data (internal docs, regulatory text, "
                 "domain jargon)",
                 "Bloomberg GPT (finance-specific LLM), internal models trained on bank's policy corpus"],
            ]
        )
    )
    return TopicSection("4.  Types & variations — use cases and GenAI patterns", "intermediate", body)


# ------------------------------------------------------------------ 5
def _sec5() -> TopicSection:
    body = (
        H3("5.1  Model Risk Management (MRM) — the governance backbone")
        + p("Model Risk Management is the discipline that prevents AI from causing harm in a "
            "regulated environment. The foundational framework is:")
        + ul([
            "<strong>Fed SR 11-7 / OCC 2011-12 (US)</strong> — the global gold standard. "
            "Defines model risk, requires model inventory, independent validation, ongoing "
            "monitoring, and board reporting. Every major jurisdiction references this.",
            "<strong>PRA SS1/23 (UK)</strong> — Model risk management principles for banks. "
            "Extends SR 11-7 with emphasis on model tiering, validation proportionality, and "
            "board accountability under SM&CR.",
            "<strong>ECB Guide on Internal Models (EU)</strong> — focused on IRB credit risk "
            "models but increasingly extended to all material models.",
            "<strong>RBI guidelines</strong> — less prescriptive than SR 11-7 but RBI's 2024 "
            "draft framework on AI/ML in financial services signals convergence.",
            "<strong>MAS FEAT principles</strong> — Fairness, Ethics, Accountability, "
            "Transparency. Singapore's principles-based approach to AI in finance.",
        ])
        + p("In practice, MRM means every model has a model card (documentation), a risk tier "
            "(Tier 1 = material, Tier 3 = low risk), an independent validation, an owner, and "
            "a scheduled review cycle (annually for Tier 1).")

        + H3("5.2  The EU AI Act — the world's first comprehensive AI law")
        + p("The EU AI Act (in force August 2024, phased applicability to August 2026) classifies "
            "AI systems by risk level:")
        + table(
            ["Risk level", "BFSI examples", "Requirements"],
            [
                ["<strong>Unacceptable (banned)</strong>",
                 "Social scoring, real-time biometric identification in public spaces (with narrow exceptions)",
                 "Prohibited outright"],
                ["<strong>High risk</strong>",
                 "Credit scoring, insurance pricing, AML/fraud detection, recruitment screening",
                 "Conformity assessment, risk management system, data governance, transparency, "
                 "human oversight, accuracy/robustness requirements, registration in EU database"],
                ["<strong>Limited risk</strong>",
                 "Customer-facing chatbots, AI-generated content",
                 "Transparency obligations (must disclose AI interaction)"],
                ["<strong>Minimal risk</strong>",
                 "Internal analytics, spam filters, process automation",
                 "No specific requirements (voluntary codes of conduct)"],
            ]
        )
        + p("For BFSI, most customer-facing and risk-related AI falls into the <strong>high-risk"
            "</strong> category. This means: documented risk management, data quality requirements, "
            "human oversight mechanisms, and conformity assessments before deployment. The "
            "compliance burden is significant and will require dedicated AI governance teams.")

        + H3("5.3  Explainability — the non-negotiable")
        + p("Regulators globally require that AI decisions affecting consumers be explainable. "
            "The US Equal Credit Opportunity Act (ECOA) requires adverse action notices with "
            "specific reasons for credit denial. The EU GDPR Article 22 gives individuals the "
            "right not to be subject to purely automated decisions. India's proposed DPDP rules "
            "are moving in the same direction.")
        + p("Explainability techniques used in BFSI:")
        + ul([
            "<strong>SHAP (SHapley Additive exPlanations)</strong> — assigns each feature a "
            "contribution to the prediction. The de facto standard for tabular ML in banking.",
            "<strong>LIME (Local Interpretable Model-agnostic Explanations)</strong> — creates "
            "a simple interpretable model around a specific prediction.",
            "<strong>Attention maps</strong> — for transformer-based models, show which input "
            "tokens influenced the output.",
            "<strong>Counterfactual explanations</strong> — 'Your loan was declined because your "
            "income is below X. If your income were Y, the decision would change.'",
        ])

        + H3("5.4  LLMOps — operationalising GenAI at scale")
        + p("LLMOps extends MLOps for the specific challenges of Large Language Models:")
        + ul([
            "<strong>Prompt management</strong> — versioning, testing, and A/B testing prompts "
            "as production artefacts.",
            "<strong>Guardrails</strong> — input/output filters to prevent prompt injection, "
            "toxic content, PII leakage, and hallucination. Tools: NeMo Guardrails (NVIDIA), "
            "Guardrails AI, custom regex/classifier layers.",
            "<strong>Evaluation</strong> — automated evaluation of LLM outputs against golden "
            "datasets (correctness, faithfulness, relevance). Human-in-the-loop review for "
            "high-stakes outputs.",
            "<strong>Cost management</strong> — LLM inference is expensive. Token budgets, "
            "model routing (use a smaller model for simple queries), and caching are essential.",
            "<strong>Data privacy</strong> — ensuring customer data does not leak to external "
            "LLM providers. Options: self-hosted models (Llama, Mistral on private infra), "
            "Azure OpenAI with data residency controls, or API-based with DLP filters.",
        ])
    )
    return TopicSection("5.  Advanced — MRM, EU AI Act, explainability, LLMOps", "advanced", body)


# ------------------------------------------------------------------ 6
def _sec6() -> TopicSection:
    body = (
        p("AI regulation in BFSI is evolving rapidly. Every jurisdiction is taking a different "
          "approach, but convergence is emerging around fairness, explainability, and human "
          "oversight.")
        + table(
            ["Region", "Key AI/ML regulations and guidance", "Practical impact"],
            [
                ["<strong>India</strong>",
                 "RBI 2024 draft framework on AI/ML in financial services. DPDP Act 2023 "
                 "(rules being notified). SEBI circular on AI/ML for market intermediaries. "
                 "RBI's focus on explainability for credit decisions. No comprehensive AI law yet.",
                 "Banks must document model governance. Credit scoring models need explainability. "
                 "Data localisation (RBI Storage of Payment Data) constrains where AI training "
                 "data can reside."],
                ["<strong>United States</strong>",
                 "Fed SR 11-7 / OCC 2011-12 (model risk). ECOA / Reg B (fair lending, adverse "
                 "action notices). CFPB guidance on AI in consumer lending. NIST AI RMF 1.0 "
                 "(voluntary framework). Executive Order on AI Safety (Oct 2023). No comprehensive "
                 "federal AI law.",
                 "Strongest MRM regime globally. Fair lending laws heavily constrain credit AI. "
                 "CFPB actively investigating AI-driven denials. Disparate impact liability "
                 "applies to ML models."],
                ["<strong>United Kingdom</strong>",
                 "PRA SS1/23 (model risk). FCA AI discussion papers. UK AI Safety Institute. "
                 "Pro-innovation approach — sector regulators (PRA, FCA) apply existing rules "
                 "to AI rather than creating a new AI-specific law.",
                 "PRA expects model tiering and proportionate validation. FCA focus on consumer "
                 "outcomes and fairness. SM&CR makes senior managers personally accountable for "
                 "AI failures in their area."],
                ["<strong>Eurozone</strong>",
                 "EU AI Act (in force Aug 2024). ECB SSM expectations on model risk. EBA "
                 "guidelines on IRB models (extending to ML). GDPR Article 22 (automated "
                 "decision-making).",
                 "Most prescriptive regime globally. High-risk AI in BFSI requires conformity "
                 "assessment, registration, and ongoing monitoring. Significant compliance "
                 "investment required."],
                ["<strong>Singapore</strong>",
                 "MAS FEAT principles (Fairness, Ethics, Accountability, Transparency). MAS "
                 "Veritas toolkit for FEAT assessment. AI Verify foundation (testing framework). "
                 "PDPA (data protection).",
                 "Principles-based but MAS is technically sophisticated and conducts deep "
                 "reviews. Veritas toolkit provides practical self-assessment methodology. "
                 "Singapore is a testbed for responsible AI in finance."],
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
                ["<strong>Build vs. buy AI/ML platform</strong>",
                 "Building on open-source (MLflow + Kubeflow + custom) gives control but requires "
                 "a 15–30 person ML platform team. Buying (SageMaker, Vertex AI, Databricks, "
                 "Azure ML) is faster but creates vendor lock-in and may conflict with data "
                 "residency requirements."],
                ["<strong>External LLM API vs. self-hosted model</strong>",
                 "External APIs (OpenAI, Anthropic, Google) are more capable but data leaves "
                 "your perimeter. Self-hosted (Llama, Mistral on private GPU) gives data control "
                 "but requires GPU infrastructure and is 6–18 months behind frontier models."],
                ["<strong>Accuracy vs. explainability</strong>",
                 "A deep neural network may be 2% more accurate than a gradient-boosted tree, "
                 "but if the regulator requires feature-level explanations for adverse actions, "
                 "the simpler model may be the only viable option."],
                ["<strong>Centralised vs. federated AI teams</strong>",
                 "A central AI/ML team ensures standards and governance. Embedded data scientists "
                 "in business lines move faster. Most tier-1 banks use a hub-and-spoke model: "
                 "central platform and governance, embedded execution."],
                ["<strong>GenAI for internal vs. customer-facing use</strong>",
                 "Internal copilots (developer tools, research summarisation) have lower risk — "
                 "a hallucination wastes an employee's time. Customer-facing GenAI (chatbots, "
                 "advisory) has much higher risk — a hallucination can cause financial harm or "
                 "regulatory violation."],
                ["<strong>Speed of deployment vs. validation rigour</strong>",
                 "Model validation takes 4–12 weeks. Business wants instant deployment. "
                 "The answer is not to skip validation but to tier models: Tier 3 (low-risk) "
                 "models get a lightweight review; Tier 1 (material) models get full validation."],
            ]
        )
    )


# ------------------------------------------------------------------ 8
def _sec8() -> TopicSection:
    body = (
        example("JPMorgan COIN — contract intelligence",
            p("JPMorgan's COiN (Contract Intelligence) platform uses NLP to review commercial "
              "loan agreements. It extracts key data points (covenants, terms, counterparties) "
              "from thousands of documents that previously required 360,000 hours of lawyer time "
              "annually. The model is not making decisions — it is extracting structured data from "
              "unstructured documents. This 'low-risk, high-volume' pattern is the safest entry "
              "point for AI in BFSI.")
        )
        + example("A credit scoring model fails the fairness test",
            p("A European bank built an ML credit scoring model that used postcode as a feature. "
              "The model performed well on accuracy metrics but showed significant disparate "
              "impact: applicants from certain postcodes (correlated with ethnicity) were declined "
              "at much higher rates. The model validation team flagged this. The bank had to "
              "retrain the model excluding postcode and using alternative features. Lesson: "
              "accuracy without fairness testing is a regulatory time bomb. Protected-class "
              "analysis (disparate impact, equal opportunity) must be part of every credit model "
              "validation.")
        )
        + example("A bank's GenAI chatbot hallucinates a rate",
            p("A bank deployed a GenAI-powered chatbot for customer queries. A customer asked "
              "about fixed deposit rates. The LLM, trained on general financial text, "
              "confidently stated a rate that was 50 basis points higher than the actual rate. "
              "The customer opened an FD based on this advice and later complained. Lesson: "
              "customer-facing GenAI must use RAG grounded in the bank's live product data, "
              "with output validation against source documents. A disclaimer alone is not "
              "sufficient — the FCA's Consumer Duty requires communications to be fair, clear, "
              "and not misleading.")
        )
        + example("HSBC — AI for AML alert triage",
            p("HSBC deployed ML models to prioritise AML transaction-monitoring alerts. The models "
              "reduced false positives by over 20%, allowing investigators to focus on genuinely "
              "suspicious activity. The model was approved by the bank's MRM function and "
              "reviewed by regulators in multiple jurisdictions. Key success factors: the model "
              "does not auto-close alerts (human-in-the-loop), it is explainable (feature "
              "importance for each alert), and it is monitored for drift monthly.")
        )
        + example("Indian bank — RBI scrutiny of AI-driven lending",
            p("An Indian bank used an AI model for instant personal loan approvals via its mobile "
              "app. RBI's inspection team asked three questions: (1) Can you explain why this "
              "applicant was declined? (2) Is the model auditable? (3) Does the model use any "
              "data prohibited under the Digital Lending Guidelines (Sep 2022)? The bank could "
              "answer questions 1 and 2 but discovered the model was using mobile phone contacts "
              "list data (prohibited under RBI's Digital Lending norms). The model was pulled "
              "from production. Lesson: data governance is the foundation of AI governance.")
        )
    )
    return TopicSection("8.  Worked examples — five real AI stories in BFSI", "intermediate", body)


# ------------------------------------------------------------------ 9
def _sec9() -> TopicSection:
    body = (
        H3("Questions a leader asks in any AI/ML review")
        + ol([
            "What tier is this model in our model risk framework, and has it been validated "
            "by the independent validation team?",
            "What is the explainability approach, and can we generate adverse action reasons "
            "for individual decisions?",
            "Has the model been tested for bias and disparate impact across protected classes?",
            "What is the monitoring plan for model drift, and what triggers retraining?",
            "If this is GenAI, what guardrails prevent hallucination, PII leakage, and "
            "prompt injection?",
            "Where does the training data reside, and does it comply with data localisation "
            "requirements (RBI, GDPR, PDPA)?",
            "Is there a human-in-the-loop for high-stakes decisions, and what is the override "
            "rate?",
            "What is the fallback if the model goes down — rule-based system, manual queue, "
            "or service degradation?",
            "Does this model fall under EU AI Act high-risk classification, and if so, have "
            "we completed the conformity assessment?",
            "What is the total cost of ownership — training compute, inference costs, "
            "platform fees, validation effort, ongoing monitoring?",
        ])
        + red_flag(ul([
            "'The model is a black box but it's accurate.' — In BFSI, accuracy without "
            "explainability is not deployable for customer-impacting decisions. Regulators "
            "will not accept 'trust the model'.",
            "'We'll use GPT-4 for credit decisions.' — LLMs are not suitable for credit "
            "scoring. They hallucinate, are not reproducible (same input can give different "
            "output), and cannot generate the structured adverse-action reasons required by "
            "law (ECOA, Consumer Duty).",
            "'Our AI team reports to the business line.' — Model risk management requires "
            "independence. The team that builds the model cannot validate it (three lines of "
            "defence). If AI governance reports to the P&L owner, there is a conflict.",
            "'We don't need to retrain — the model is stable.' — Every model drifts. A fraud "
            "model that is not retrained quarterly is missing new fraud patterns. A credit "
            "model that is not recalibrated annually is mispricing risk.",
            "'We'll deploy GenAI internally first and worry about governance later.' — Even "
            "internal GenAI creates risk: an LLM that summarises customer data internally can "
            "leak PII to logs, be cached by a cloud provider, or produce misleading analysis "
            "that drives a bad business decision.",
            "'AI will replace the compliance team.' — AI augments compliance. It triages "
            "alerts, extracts data, and drafts narratives. But regulatory accountability "
            "remains with named humans (SM&CR, SR 11-7). No regulator accepts 'the AI "
            "decided' as an answer.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("ML / AI", "Machine Learning / Artificial Intelligence — systems that learn "
             "patterns from data to make predictions or decisions."),
            ("GenAI / LLM", "Generative AI / Large Language Model — AI that generates text, "
             "code, or images. GPT-4, Claude, Gemini, Llama are examples."),
            ("MRM", "Model Risk Management — the governance framework for identifying, "
             "measuring, monitoring, and controlling model risk."),
            ("SR 11-7", "Fed Supervisory Letter 11-7 — the foundational US guidance on model "
             "risk management, referenced globally."),
            ("SHAP", "SHapley Additive exPlanations — a method for explaining individual "
             "model predictions by assigning feature contributions."),
            ("Feature store", "A centralised repository of pre-computed features used "
             "consistently across training and inference."),
            ("Model drift", "Degradation of model performance over time as real-world "
             "patterns change."),
            ("Champion-challenger", "Deployment pattern where the production model (champion) "
             "runs alongside a new model (challenger) to compare performance."),
            ("RAG", "Retrieval-Augmented Generation — grounding LLM responses in retrieved "
             "documents to reduce hallucination."),
            ("Guardrails", "Input/output filters on LLM interactions to prevent harmful, "
             "inaccurate, or policy-violating responses."),
            ("EU AI Act", "The European Union's comprehensive AI regulation, in force "
             "August 2024, classifying AI by risk level."),
            ("FEAT", "Fairness, Ethics, Accountability, Transparency — MAS's principles "
             "for AI in financial services."),
            ("Hallucination", "When an LLM generates plausible-sounding but factually "
             "incorrect output."),
            ("Adverse action notice", "Legally required explanation to a consumer when a "
             "credit application is denied (ECOA in US, similar requirements globally)."),
            ("Disparate impact", "When a neutral policy or model disproportionately affects "
             "a protected class, even without discriminatory intent."),
            ("MLOps / LLMOps", "Operational practices for deploying, monitoring, and "
             "governing ML models / LLMs in production."),
        ])
    )
    return TopicSection("9.  Questions, red flags, and glossary", "basic", body)
