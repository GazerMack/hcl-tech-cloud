"""Security, Risk & Compliance · 01 — Security, identity, and the global
regulator landscape."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="V.1",
        slug="01-security-identity-regulators",
        title="Security, identity, and the global regulator landscape",
        one_liner=(
            "A bank is, in the end, a trust machine. Strip away the products and "
            "the channels and what remains is a promise that money in is money "
            "safe. Security and identity are how that promise is engineered; the "
            "regulator landscape is how it is enforced. This topic gives you a "
            "fluent vocabulary in IAM, cryptography and Hardware Security "
            "Modules (HSMs), zero trust, post-quantum cryptography (PQC), "
            "DevSecOps, and the regulator regimes that now dominate BFSI design "
            "reviews — DORA, NIS2, the EU AI Act, UK FCA Operational Resilience "
            "and the Critical Third Parties (CTP) regime, RBI Cyber Security "
            "Master Directions, NYDFS Part 500, MAS TRM, and HKMA C-RAF."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("Security in BFSI is not one discipline; it is six, working "
              "in concert. Identity decides who is acting; cryptography "
              "decides what they can read and trust; network and "
              "endpoint controls decide where they can act; application "
              "security decides whether the code they touch is "
              "trustworthy; security operations watches them; and the "
              "regulator decides what evidence you must produce to "
              "prove it. Get any of the six wrong and you have an "
              "incident.")
        )
        + H3("0.1  IT-side anchor — the keys, the lock, and the doorbell")
        + it_anchor(
            p("Think of your front door. The <em>key</em> is "
              "<strong>authentication</strong> — proof you are you. The "
              "<em>lock</em> is <strong>authorisation</strong> — what "
              "the key opens (the front door, not the safe). The <em>"
              "doorbell camera</em> is <strong>logging and "
              "monitoring</strong> — a record of who came when. If you "
              "have a smart lock, the <em>app on your phone</em> is the "
              "<strong>identity provider</strong> that lets the lock "
              "and the camera and the alarm all agree about who you "
              "are. Banks have the same parts, on a vastly larger "
              "scale.")
        )
        + H3("0.2  BFSI-side anchor — what you already do every login")
        + bfsi_anchor(
            p("When you log in to your bank app, three things happen in "
              "under a second. Your fingerprint or face unlocks a key "
              "stored in the secure element of your phone. The phone "
              "presents that key to the bank as part of an <strong>"
              "OAuth 2.0 / OpenID Connect</strong> flow. The bank "
              "decides what you can do (view balance, transfer up to "
              "₹1,00,000 without a second factor) using "
              "<strong>authorisation</strong> rules that take in your "
              "device, your location, the time of day and the amount. "
              "If anything looks unusual, a <strong>step-up "
              "authentication</strong> challenge is fired. That is "
              "<strong>Strong Customer Authentication (SCA)</strong> "
              "in the EU, <strong>Risk-Based Authentication</strong> "
              "in the United States, and <strong>two-factor</strong> "
              "everywhere else. You experience it as ‘the bank app "
              "asked me for my PIN again’; the engineer experiences it "
              "as a six-discipline decision under 200 milliseconds.")
        )
        + H3("0.3  The six layers of a BFSI security stack")
        + ul([
            "<strong>Identity and Access Management (IAM)</strong> — "
            "who is acting and what are they allowed to do? Workforce, "
            "customer, machine.",
            "<strong>Cryptography and key management</strong> — what "
            "can be read, signed, decrypted; HSMs, KMS, certificates.",
            "<strong>Network and endpoint security</strong> — where "
            "they can act from; segmentation, zero trust, EDR / XDR.",
            "<strong>Application security and DevSecOps</strong> — is "
            "the code itself trustworthy; SAST, DAST, SCA, SBOM.",
            "<strong>Security operations (SecOps)</strong> — watching "
            "and responding; SOC, SIEM, SOAR, threat intelligence, "
            "incident response.",
            "<strong>Governance, Risk and Compliance (GRC)</strong> — "
            "the policies, the regulators, the auditors; the evidence "
            "machine.",
        ])
        + callout("Related topics in this bible",
            ul([
                "<a href='02-fraud-aml-sanctions.html'><strong>V.2 — Fraud, AML &amp; sanctions</strong></a> "
                "— the operational front line that Security underpins.",
                "<a href='../bfsi-platforms/02-payments-engines.html'><strong>VI.2 — Payments engines</strong></a> "
                "— every payment crosses the seven control points described here.",
                "<a href='../bfsi-platforms/05-cards-and-switches.html'><strong>VI.5 — Cards &amp; switches</strong></a> "
                "— PCI DSS, HSMs, and EMV/3DS2 are security-first card topics.",
                "<a href='../infra-ops/01-cloud-native-operations.html'><strong>IV.1 — Cloud-native operations</strong></a> "
                "— CSPM, CNAPP, and workload identity apply when the bank runs on cloud.",
            ]),
            "info")
    )
    return TopicSection(
        "0.  Primer — six disciplines, one trust promise",
        "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Why is this topic now more board-level than it has ever been?")
        + ol([
            "<strong>Operational resilience is now law.</strong> EU "
            "DORA in force 17 January 2025; UK Operational Resilience "
            "fully embedded March 2025; UK Critical Third Parties "
            "regime active under FSMA 2023; RBI Cyber Security and "
            "IT Governance Master Directions (2023). Boards are now "
            "personally accountable for cyber posture.",
            "<strong>Ransomware and APP fraud at industrial scale.</strong> "
            "Authorised Push Payment fraud crossed £459M in the UK in "
            "2023; mandatory reimbursement from October 2024 changes "
            "incentives sharply. Ransomware against banks and their "
            "third parties (ION 2023, MOVEit 2023, ICBC 2023) is now "
            "annual.",
            "<strong>The cryptographic horizon.</strong> NIST published "
            "the final Post-Quantum Cryptography (PQC) standards "
            "ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205) "
            "in August 2024. Banks must inventory cryptography now to "
            "be migrated by the early-2030s deadline regulators are "
            "signalling.",
            "<strong>AI risk.</strong> EU AI Act in force August 2024; "
            "MAS FEAT principles; Singapore Model AI Governance "
            "Framework; NIST AI RMF; UK AISI; India DPDP + RBI "
            "supervisory expectations.",
            "<strong>Identity is the new perimeter.</strong> The "
            "network perimeter has dissolved; SaaS and mobile mean "
            "identity is the only consistent control point.",
            "<strong>Concentration risk.</strong> Hyperscalers, key "
            "vendors, payment rails — when one fails, many fail "
            "together. Regulators now treat this as a systemic-risk "
            "topic.",
        ])
    )
    return TopicSection(
        "1.  Why security is now the headline BFSI conversation",
        "basic", body)


def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart LR\n'
            '  subgraph "Identity"\n'
            '    W["Workforce IdP<br/>Entra ID / Okta / Ping"]\n'
            '    C["Customer IdP<br/>ForgeRock / Auth0 / in-house"]\n'
            '    M["Machine identity<br/>SPIFFE / SPIRE"]\n'
            '  end\n'
            '  subgraph "Cryptography"\n'
            '    H["HSMs<br/>Thales / Entrust / cloud HSM"]\n'
            '    K["KMS / EKM<br/>AWS / Azure / GCP / OCI"]\n'
            '    P["PKI<br/>internal + eIDAS / DigiCert"]\n'
            '  end\n'
            '  subgraph "Network and endpoint"\n'
            '    Z["Zero Trust<br/>ZTNA / SASE"]\n'
            '    E["EDR / XDR<br/>CrowdStrike / SentinelOne / Defender"]\n'
            '  end\n'
            '  subgraph "AppSec / DevSecOps"\n'
            '    S["SAST / DAST / SCA"]\n'
            '    Sb["SBOM + signing<br/>Sigstore / SLSA"]\n'
            '  end\n'
            '  subgraph "SecOps"\n'
            '    Si["SIEM<br/>Splunk / Sentinel / Chronicle"]\n'
            '    So["SOAR<br/>Cortex XSOAR / Tines"]\n'
            '    Tt["Threat intel + DFIR"]\n'
            '  end\n'
            '  subgraph "GRC"\n'
            '    R["Regulators + auditors<br/>DORA, FCA, RBI, MAS, NYDFS, HKMA"]\n'
            '  end\n'
            '  W --> Z\n'
            '  C --> Z\n'
            '  M --> Z\n'
            '  H --> K --> Z\n'
            '  Z --> S --> Sb --> Si\n'
            '  E --> Si --> So --> Tt\n'
            '  Si --> R',
            "How the six disciplines fit together: identity and "
            "cryptography feed access; AppSec and SecOps watch and "
            "respond; GRC turns it all into regulator-acceptable "
            "evidence.")
    )
    return TopicSection(
        "2.  The picture — six disciplines, one diagram",
        "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  Identity — workforce, customer, machine")
        + ul([
            "<strong>Workforce identity</strong> — the bank’s "
            "employees, contractors and partners. Single Sign-On "
            "(SSO) via OIDC / SAML 2.0 against the corporate IdP "
            "(<strong>Microsoft Entra ID</strong>, <strong>Okta</strong>, "
            "<strong>Ping</strong>, <strong>ForgeRock</strong>). "
            "Multi-Factor Authentication (MFA) is mandatory; "
            "phishing-resistant MFA — FIDO2 security keys, Windows "
            "Hello, passkeys — is the modern target. Privileged "
            "Access Management (PAM) via <strong>CyberArk</strong>, "
            "<strong>BeyondTrust</strong>, <strong>Delinea</strong>, "
            "<strong>HashiCorp Boundary</strong>; just-in-time "
            "elevation is now the norm.",
            "<strong>Customer identity (CIAM)</strong> — the bank’s "
            "retail and corporate customers. Custom in-house at most "
            "tier-1 banks; <strong>ForgeRock</strong> (Ping), "
            "<strong>Auth0</strong> (Okta), <strong>Transmit "
            "Security</strong>, <strong>Akamai Identity Cloud</strong> "
            "are major commercial platforms. Federated to national "
            "identity in some markets — <strong>Aadhaar / e-KYC</strong> "
            "in India, <strong>SingPass</strong> in Singapore, "
            "<strong>BankID</strong> in the Nordics, <strong>itsme</strong> "
            "in Belgium, <strong>SPID</strong> in Italy, <strong>"
            "GOV.UK One Login</strong> in the UK.",
            "<strong>Machine / workload identity</strong> — services, "
            "scripts, and pipelines. <strong>SPIFFE / SPIRE</strong> "
            "(CNCF) for cloud-neutral workload identity; <strong>AWS "
            "IAM Roles Anywhere</strong>, <strong>Azure Managed "
            "Identity</strong>, <strong>GCP Workload Identity "
            "Federation</strong> for cloud-native; <strong>HashiCorp "
            "Vault</strong> for short-lived credentials.",
        ])
        + H3("3.2  Authentication and the slow death of passwords")
        + ul([
            "<strong>FIDO2 / WebAuthn / passkeys</strong> — public-key "
            "based, phishing-resistant. Apple, Google, Microsoft "
            "passkeys converging on a common UX. Banks rolling out "
            "to customers in 2024–2025.",
            "<strong>Strong Customer Authentication (SCA)</strong> — "
            "PSD2 RTS requirement: two of three factors (knowledge, "
            "possession, inherence). Mandatory for online card "
            "payments and Open Banking transactions.",
            "<strong>Risk-Based Authentication (RBA)</strong> — "
            "evaluate device, network, behaviour; step up only when "
            "risk crosses a threshold. <strong>BioCatch</strong>, "
            "<strong>Feedzai</strong>, <strong>BehavioSec</strong>, "
            "<strong>Transmit Security</strong> are common.",
            "<strong>Step-up authentication</strong> — escalate to a "
            "stronger factor for higher-risk actions.",
            "<strong>Confirmation of Payee (CoP)</strong> — UK "
            "innovation now spreading; verify the beneficiary name "
            "before payment to reduce APP fraud.",
        ])
        + H3("3.3  Authorisation — RBAC, ABAC, ReBAC, policy as code")
        + ul([
            "<strong>Role-Based Access Control (RBAC)</strong> — the "
            "old default; users get roles, roles get permissions. "
            "Suffers role explosion at scale.",
            "<strong>Attribute-Based Access Control (ABAC)</strong> — "
            "decisions based on attributes (department, location, "
            "data classification, time, risk score). NIST SP 800-162. "
            "More expressive, harder to debug.",
            "<strong>Relationship-Based Access Control (ReBAC)</strong> "
            "— Google Zanzibar paper (2019), now productised as "
            "<strong>SpiceDB</strong>, <strong>OpenFGA</strong>, "
            "<strong>Permify</strong>; powers fine-grained "
            "permissions in modern fintech.",
            "<strong>Policy as code</strong> — Open Policy Agent "
            "(OPA) / Rego, Cedar (AWS), Kyverno; policies "
            "expressed in code, version-controlled, tested.",
            "<strong>Just-in-time / break-glass</strong> — production "
            "access is granted on request, time-bound, recorded, "
            "and reviewed.",
        ])
        + H3("3.4  Cryptography — the moving floor")
        + ul([
            "<strong>Symmetric</strong> — AES-256-GCM is the default "
            "for data encryption; ChaCha20-Poly1305 where AES-NI is "
            "absent.",
            "<strong>Asymmetric (classical)</strong> — RSA-2048 and "
            "RSA-3072 still ubiquitous; Elliptic-Curve Cryptography "
            "(ECC) preferred for new systems (NIST P-256 / P-384, "
            "Curve25519).",
            "<strong>Hashing</strong> — SHA-256, SHA-3-256; password "
            "hashing with Argon2id, scrypt, or bcrypt; never SHA-1 "
            "or MD5 for new work; HMAC-SHA-256 for message "
            "authentication.",
            "<strong>Transport</strong> — TLS 1.3 is the modern "
            "baseline; TLS 1.2 acceptable; everything below "
            "deprecated. mTLS where both ends present "
            "certificates.",
            "<strong>Post-Quantum Cryptography (PQC)</strong> — NIST "
            "FIPS 203 ML-KEM (key encapsulation, ex-Kyber), FIPS "
            "204 ML-DSA (signatures, ex-Dilithium), FIPS 205 "
            "SLH-DSA (hash-based signatures, ex-SPHINCS+) finalised "
            "August 2024. Banks are starting <em>cryptographic "
            "inventories</em> and <em>hybrid TLS</em> deployments "
            "now to be ready by the early-to-mid 2030s.",
        ])
        + H3("3.5  Key management and HSMs")
        + ul([
            "<strong>Hardware Security Module (HSM)</strong> — "
            "tamper-resistant device that performs cryptographic "
            "operations and never releases the private key. "
            "<strong>Thales Luna</strong>, <strong>Entrust nShield</strong>, "
            "<strong>Utimaco</strong>, <strong>IBM Crypto Express "
            "(z/OS)</strong>, <strong>AWS CloudHSM</strong>, "
            "<strong>Azure Key Vault Managed HSM</strong>, "
            "<strong>GCP Cloud HSM</strong>, <strong>OCI Vault "
            "HSM</strong>.",
            "<strong>FIPS 140-3 Level 3</strong> — the certification "
            "BFSI HSMs target; mandatory for many regulator "
            "controls.",
            "<strong>Cloud KMS</strong> — fronts the HSM with a "
            "managed API; typical pattern is BYOK (Bring Your Own "
            "Key) or HYOK / EKM (Hold Your Own Key / External Key "
            "Manager) for sensitive workloads.",
            "<strong>Key lifecycle</strong> — generation, rotation, "
            "revocation, archival, destruction; rotation cadence "
            "tied to the data classification.",
            "<strong>Tokenisation and Format-Preserving Encryption "
            "(FPE)</strong> — replace card PANs and similar with "
            "tokens; <strong>Voltage SecureData</strong>, <strong>"
            "Protegrity</strong>, <strong>Thales CipherTrust</strong>, "
            "<strong>Comforte</strong>.",
            "<strong>Confidential computing</strong> — AMD SEV-SNP, "
            "Intel TDX, AWS Nitro Enclaves, Azure Confidential VMs, "
            "GCP Confidential VMs; data encrypted while in use.",
        ])
        + H3("3.6  Public Key Infrastructure (PKI)")
        + ul([
            "<strong>Internal PKI</strong> — Microsoft AD CS, "
            "HashiCorp Vault PKI, AWS Private CA, GCP CAS; signs "
            "internal mTLS certs, code-signing certs.",
            "<strong>External PKI</strong> — DigiCert, Sectigo, "
            "GlobalSign, Entrust; commercial TLS certs.",
            "<strong>eIDAS qualified PKI</strong> — Qualified "
            "Trust Service Providers (QTSPs) issue QWAC and QSealC "
            "certificates required by PSD2.",
            "<strong>Certificate Lifecycle Management</strong> — "
            "Venafi, Keyfactor, AppViewX; automation to prevent "
            "expiry incidents (the recurring root cause of bank "
            "outages).",
        ])
        + H3("3.7  Network — zero trust, segmentation, SASE")
        + p("The 2010 Forrester paper popularised <strong>Zero Trust "
            "(ZT)</strong>: never trust, always verify. NIST SP "
            "800-207 (2020) is the canonical reference. Operational "
            "shapes:")
        + ul([
            "<strong>Zero Trust Network Access (ZTNA)</strong> — "
            "replace VPN with identity-aware proxies. Cloudflare "
            "Access, Zscaler Private Access, Palo Alto Prisma, "
            "Netskope, Cisco Duo.",
            "<strong>Secure Access Service Edge (SASE)</strong> — "
            "ZTNA + SD-WAN + Cloud Access Security Broker (CASB) + "
            "Secure Web Gateway (SWG) + Firewall-as-a-Service "
            "(FWaaS). The ‘network is a service’ model.",
            "<strong>Microsegmentation</strong> — Illumio, "
            "Guardicore (Akamai), VMware NSX; identity-aware "
            "east-west firewalling.",
            "<strong>DDoS protection</strong> — Cloudflare, Akamai, "
            "AWS Shield Advanced, Azure DDoS Protection, Imperva.",
        ])
        + H3("3.8  Endpoint, EDR / XDR, and the rise of SaaS security")
        + ul([
            "<strong>EDR / XDR</strong> — CrowdStrike Falcon, "
            "SentinelOne, Microsoft Defender for Endpoint, Palo "
            "Alto Cortex XDR, Trend Micro.",
            "<strong>Mobile Threat Defence (MTD)</strong> — Lookout, "
            "Zimperium; relevant for mobile-banking apps.",
            "<strong>Browser security</strong> — Island, Talon "
            "(Palo Alto), Menlo; isolating SaaS access.",
            "<strong>SaaS Security Posture Management (SSPM)</strong> "
            "— Adaptive Shield, AppOmni, Obsidian; auditing SaaS "
            "config (Salesforce, Microsoft 365, Workday).",
        ])
        + H3("3.9  Application security and DevSecOps")
        + ul([
            "<strong>SAST (Static)</strong> — Checkmarx, Veracode, "
            "Sonatype, Snyk Code, GitHub Advanced Security, Semgrep.",
            "<strong>DAST (Dynamic)</strong> — OWASP ZAP, Burp "
            "Suite Enterprise, Invicti, Veracode DAST.",
            "<strong>SCA (Software Composition Analysis)</strong> — "
            "Snyk, Black Duck, Sonatype Nexus IQ, GitHub "
            "Dependabot.",
            "<strong>API security</strong> — Salt Security, Noname, "
            "Traceable, Akamai API Security; OWASP API Top 10 "
            "(2023).",
            "<strong>SBOM and supply-chain</strong> — CycloneDX / "
            "SPDX SBOMs, SLSA provenance, Sigstore (cosign) "
            "signing; required by EU Cyber Resilience Act (CRA) "
            "and US Executive Order 14028.",
            "<strong>Secrets scanning</strong> — GitGuardian, "
            "TruffleHog, GitHub Push Protection.",
            "<strong>Cloud Security Posture Management "
            "(CSPM)</strong>, <strong>Cloud-Native Application "
            "Protection Platform (CNAPP)</strong> — Wiz, Prisma "
            "Cloud, Orca, Lacework, Microsoft Defender for Cloud.",
        ])
        + H3("3.10  Security operations — SOC, SIEM, SOAR, threat intel")
        + ul([
            "<strong>SIEM</strong> — Splunk, Microsoft Sentinel, "
            "Google Chronicle / SecOps, Elastic Security, IBM "
            "QRadar, Sumo Logic.",
            "<strong>SOAR</strong> — Cortex XSOAR (Palo Alto), "
            "Splunk SOAR, Tines, Torq, Swimlane; automating "
            "response runbooks.",
            "<strong>Threat intelligence</strong> — Recorded Future, "
            "Mandiant (Google), Flashpoint, FS-ISAC for BFSI "
            "sector intel; STIX / TAXII as the exchange format.",
            "<strong>Incident response</strong> — Mandiant, CrowdStrike "
            "Services, Kroll, Palo Alto Unit 42; retainers are "
            "standard for tier-1 banks.",
            "<strong>Threat-Led Penetration Testing (TLPT)</strong> "
            "— TIBER-EU framework (ECB), CBEST (UK), iCAST (HKMA), "
            "AASE (MAS), GBEST (Saudi); now mandated by DORA for "
            "the most critical services.",
            "<strong>Purple teaming</strong> — red and blue teams "
            "working together; MITRE ATT&CK as the lingua franca "
            "of adversary behaviour.",
        ])
    )
    return TopicSection(
        "3.  How the security stack actually works — six disciplines "
        "in detail",
        "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  Eurozone — DORA, NIS2, AI Act, GDPR")
        + ul([
            "<strong>DORA (Digital Operational Resilience "
            "Act)</strong> — in force <strong>17 January 2025</strong>. "
            "ICT risk management, incident reporting, threat-led "
            "penetration testing, and oversight of critical ICT "
            "third parties (hyperscalers and major vendors).",
            "<strong>NIS2 Directive</strong> — applies from October "
            "2024; widens the cybersecurity baseline across "
            "‘essential’ and ‘important’ entities; banks already "
            "covered, but vendors many banks rely on are now in "
            "scope.",
            "<strong>EU AI Act</strong> — in force August 2024; "
            "phased applicability through August 2026. Risk-based "
            "classification; high-risk use cases include credit "
            "scoring and biometric verification.",
            "<strong>EU Cyber Resilience Act (CRA)</strong> — adopted "
            "2024; product-side cyber rules including SBOM and "
            "vulnerability disclosure for ‘products with digital "
            "elements’.",
            "<strong>GDPR</strong> — still the foundation; UK GDPR "
            "and Data Protection Act 2018 in the UK.",
            "<strong>eIDAS 2.0</strong> — adopted 2024; introduces "
            "the European Digital Identity Wallet from 2026.",
        ])
        + H3("4.2  United Kingdom — FCA, PRA, BoE, ICO")
        + ul([
            "<strong>FCA / PRA / BoE Operational Resilience</strong> "
            "policy — fully embedded March 2025; identify "
            "important business services, set impact tolerances, "
            "test through severe-but-plausible scenarios.",
            "<strong>UK Critical Third Parties (CTP) regime</strong> "
            "under FSMA 2023 — brings hyperscalers and other "
            "critical vendors under direct UK regulator oversight "
            "from 2024.",
            "<strong>FCA Consumer Duty</strong> — July 2023; raises "
            "the bar on consumer outcomes, including fraud and "
            "scam prevention.",
            "<strong>FCA APP fraud reimbursement</strong> — "
            "mandatory from October 2024; sender and receiver "
            "PSPs split the cost 50/50.",
            "<strong>UK GDPR + ICO</strong>, NCSC <strong>Cyber "
            "Assessment Framework (CAF)</strong>, NCSC <strong>"
            "Cyber Essentials</strong>.",
        ])
        + H3("4.3  India — RBI, SEBI, IRDAI, MeitY, DPDP")
        + ul([
            "<strong>RBI Cyber Security Framework for "
            "Banks</strong> (2016, regularly updated) and the "
            "<strong>RBI Master Direction on IT Governance, Risk, "
            "Controls and Assurance Practices</strong> (Nov 2023).",
            "<strong>RBI Master Direction on Outsourcing of IT "
            "Services</strong> (April 2023).",
            "<strong>RBI Storage of Payment System Data</strong> "
            "(April 2018) — payments data localised in India.",
            "<strong>RBI Digital Lending Guidelines</strong> (Sep "
            "2022, amended 2024).",
            "<strong>SEBI Cybersecurity and Cyber Resilience "
            "Framework</strong> for Market Infrastructure "
            "Institutions, 2024 update.",
            "<strong>IRDAI Information and Cyber Security "
            "Guidelines</strong> for insurers.",
            "<strong>DPDP Act 2023</strong> — Digital Personal "
            "Data Protection Act; rules notified 2024–2025.",
            "<strong>CERT-In Directions (April 2022)</strong> — "
            "incident reporting within 6 hours; log retention 180 "
            "days in India.",
        ])
        + H3("4.4  United States — federal and state")
        + ul([
            "<strong>NIST Cybersecurity Framework (CSF) 2.0</strong> "
            "— Feb 2024; the de-facto industry baseline; six "
            "functions: Govern, Identify, Protect, Detect, "
            "Respond, Recover.",
            "<strong>NYDFS Part 500</strong> — New York DFS "
            "Cybersecurity Regulation; 2023 amendment adds CISO "
            "certification and 72-hour incident reporting.",
            "<strong>OCC Heightened Standards</strong>, "
            "<strong>Fed SR 23-4</strong> third-party risk "
            "management, <strong>FDIC FFIEC IT Examination "
            "Handbook</strong>.",
            "<strong>SEC Cybersecurity Disclosure Rule</strong> "
            "(July 2023) — 4-business-day disclosure of material "
            "incidents on Form 8-K.",
            "<strong>GLBA Safeguards Rule</strong> (2003, 2021 "
            "update), <strong>Sarbanes-Oxley (SOX)</strong> for "
            "ICFR.",
            "<strong>Executive Order 14028</strong> (2021) — federal "
            "supply-chain rules; mandates SBOM for "
            "federal-vendor software; influences private sector.",
            "<strong>NIST SP 800-53 / 800-171 / 800-207 (Zero "
            "Trust)</strong>.",
        ])
        + H3("4.5  Singapore, Hong Kong, Australia, Brazil")
        + ul([
            "<strong>MAS TRM Guidelines</strong> (Singapore, "
            "updated 2021); <strong>MAS Notice 644 / 658</strong> "
            "on outsourcing and BCM; <strong>MAS Cyber Hygiene "
            "Notice</strong>; <strong>MAS FEAT principles</strong> "
            "for AI; <strong>Veritas</strong> consortium for "
            "AI governance.",
            "<strong>HKMA C-RAF (Cyber Resilience Assessment "
            "Framework)</strong> + <strong>iCAST</strong> "
            "intelligence-led testing.",
            "<strong>Australia APRA CPS 234 (2019)</strong> "
            "Information Security Prudential Standard; <strong>"
            "CPS 230 Operational Risk Management</strong> in force "
            "July 2025; <strong>Privacy Act</strong> reforms 2024.",
            "<strong>Brazil LGPD</strong> + <strong>Banco Central "
            "Cyber Resilience Resolution 4893/2021</strong>.",
            "<strong>UAE CBUAE Information and Cyber Security "
            "Standards</strong>; <strong>SAMA Cybersecurity "
            "Framework</strong> (Saudi Arabia); <strong>Israel "
            "Cyber Defense Methodology for Financial "
            "Institutions</strong>.",
        ])
        + H3("4.6  Cross-cutting — sanctions, AML, fraud")
        + ul([
            "<strong>OFAC, EU sanctions, UK OFSI, India MEA</strong> "
            "— sanctions screening across SWIFT messages, card "
            "transactions, customer onboarding.",
            "<strong>FATF Recommendations</strong> — global AML / "
            "CFT baseline; transposed into local law (PMLA in "
            "India, BSA in US, MLR in UK, AMLD6 in EU).",
            "<strong>PCI DSS 4.0</strong> — March 2025 fully in "
            "force; payment-card data security baseline.",
            "<strong>SWIFT CSCF</strong> — Customer Security Controls "
            "Framework, annual attestation by every SWIFT user.",
        ])
    )
    return TopicSection(
        "4.  Region by region — the regulator landscape, current as "
        "of 2025",
        "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  Zero trust — beyond the slogan")
        + p("Zero trust is not a product; it is an architectural "
            "stance with five practical components, derived from "
            "NIST SP 800-207:")
        + ul([
            "<strong>Identity-centric access</strong> — every "
            "request authenticated against an IdP, every action "
            "authorised against policy.",
            "<strong>Device posture</strong> — only known, healthy "
            "devices reach sensitive resources; integrated with "
            "MDM and EDR signals.",
            "<strong>Microsegmentation</strong> — east-west traffic "
            "is policy-controlled, not flat.",
            "<strong>Continuous evaluation</strong> — risk signals "
            "(geo, behaviour, time) re-evaluated mid-session; "
            "tokens short-lived.",
            "<strong>Encrypted everywhere</strong> — TLS 1.3 / mTLS "
            "between every hop.",
        ])
        + H3("5.2  Cryptographic agility and PQC migration")
        + p("Post-quantum migration is a 5–10 year programme. The "
            "playbook regulators are signalling:")
        + ol([
            "<strong>Cryptographic inventory</strong> — every place "
            "the bank uses public-key crypto: TLS, code signing, "
            "JWT, payments, document signing, archival storage.",
            "<strong>Crypto-agility</strong> — code that lets you "
            "swap algorithms without rewriting; abstract the "
            "primitives, version everything.",
            "<strong>Hybrid TLS</strong> — combine a classical and "
            "a PQC algorithm in TLS; if either is broken, traffic "
            "is still safe. Drafts implemented by AWS, Cloudflare, "
            "Google.",
            "<strong>Long-lived data</strong> — anything that must "
            "be confidential for >10 years (mortgages, insurance, "
            "trade tickets, archives) is at risk from ‘harvest "
            "now, decrypt later’ — migrate first.",
            "<strong>Vendor pressure</strong> — every HSM, KMS, PKI "
            "and SSL-termination vendor needs a PQC roadmap; the "
            "BFSI bar is ‘FIPS 203 / 204 / 205 by 2026’.",
        ])
        + H3("5.3  AI security and AI risk")
        + ul([
            "<strong>OWASP LLM Top 10</strong> (2023, updated "
            "2024) — Prompt Injection, Insecure Output Handling, "
            "Training Data Poisoning, Model Denial of Service, "
            "Supply Chain Vulnerabilities, Sensitive Information "
            "Disclosure, Insecure Plugin Design, Excessive Agency, "
            "Overreliance, Model Theft.",
            "<strong>NIST AI Risk Management Framework</strong> "
            "(AI RMF, 2023) and Generative AI Profile (2024).",
            "<strong>EU AI Act</strong> high-risk categorisation "
            "for credit scoring and biometric ID; conformity "
            "assessment, post-market monitoring.",
            "<strong>MAS FEAT principles</strong> — Fairness, "
            "Ethics, Accountability, Transparency for AI in "
            "finance.",
            "<strong>Singapore Model AI Governance Framework "
            "v2</strong> (2024) for generative AI.",
            "<strong>Model registries and AI BoMs</strong> — "
            "track every model, dataset, prompt, and dependency; "
            "MLflow, AWS SageMaker Model Registry, Vertex AI.",
        ])
        + H3("5.4  Fraud and AML — the operational front line")
        + ul([
            "<strong>Real-time transaction monitoring</strong> — "
            "<strong>Feedzai</strong>, <strong>NICE Actimize</strong>, "
            "<strong>SAS</strong>, <strong>Fiserv (Verafin)</strong>, "
            "<strong>FICO Falcon</strong>, <strong>Featurespace "
            "(Visa)</strong>, <strong>ThetaRay</strong>.",
            "<strong>AML case management</strong> — <strong>NICE "
            "Actimize</strong>, <strong>Oracle FCCM</strong>, "
            "<strong>SAS AML</strong>, <strong>SymphonyAI "
            "Sensa-NetReveal</strong>, <strong>ComplyAdvantage</strong>.",
            "<strong>Sanctions screening</strong> — <strong>"
            "Accuity</strong> (LSEG World-Check), <strong>Dow "
            "Jones Risk &amp; Compliance</strong>, <strong>Refinitiv "
            "World-Check</strong>.",
            "<strong>Authorised Push Payment fraud</strong> — UK "
            "PSR mandatory reimbursement Oct 2024; Confirmation "
            "of Payee, behavioural analytics, friction at the "
            "right moments.",
            "<strong>Card fraud</strong> — 3-D Secure 2.x with "
            "EMV 3DS; risk-based authentication; tokenisation of "
            "card data.",
        ])
        + H3("5.5  Resilience patterns regulators expect to see")
        + ul([
            "<strong>Important business services</strong> — named, "
            "with mapped dependencies and impact tolerances.",
            "<strong>Severe-but-plausible scenarios</strong> — "
            "tested at least annually; documented; reviewed at "
            "board level.",
            "<strong>Threat-led penetration testing (TLPT)</strong> "
            "— TIBER-EU under DORA; CBEST under UK; iCAST under "
            "HKMA. The bank does not know in advance which "
            "service the red team will hit.",
            "<strong>Cyber recovery vault / immutable backups</strong> "
            "— isolated, immutable copy of critical data; tested "
            "restoration.",
            "<strong>Exit plan from cloud / critical vendor</strong> "
            "— DORA, RBI, PRA all expect a documented, tested "
            "exit. Not a paper plan.",
        ])
    )
    return TopicSection(
        "5.  Advanced — zero trust, PQC, AI risk, fraud, resilience",
        "advanced", body)


def _sec6() -> TopicSection:
    body = (
        H3("6.1  Identity stack — choosing the IdP")
        + table(
            ["Vendor", "Strengths in BFSI", "Watch-outs"],
            [
                ["<strong>Microsoft Entra ID</strong>",
                 "Default at Microsoft 365 banks (Standard "
                 "Chartered, NatWest, Lloyds, Citi); deep PAM via "
                 "Privileged Identity Management; Conditional "
                 "Access policies.",
                 "Lock-in to Microsoft estate; CIAM is weaker than "
                 "specialists."],
                ["<strong>Okta + Auth0</strong>",
                 "Strong CIAM (Auth0); workforce SSO at many "
                 "challengers and US banks; deep app catalogue.",
                 "Cost growth; 2023 breach prompted security "
                 "review at many regulated tenants."],
                ["<strong>Ping + ForgeRock</strong>",
                 "Strong CIAM at large banks; on-prem-friendly; "
                 "FAPI / Open Banking expertise.",
                 "Migration complexity post Ping-ForgeRock merger "
                 "(2023)."],
                ["<strong>IBM Verify, Oracle IDCS, SAP IAS</strong>",
                 "Native fit inside large incumbent estates.",
                 "Less momentum in greenfield."],
                ["<strong>In-house CIAM</strong>",
                 "Common at the very largest banks (Citi, JPM, "
                 "HSBC) for full control over fraud signals and "
                 "consent.",
                 "Engineering and security responsibility you must "
                 "actually staff."],
            ]
        )
        + H3("6.2  HSM / KMS — choosing the key custody model")
        + table(
            ["Model", "When it wins", "Watch-outs"],
            [
                ["<strong>Cloud-managed KMS only</strong>",
                 "Greenfield, lower-sensitivity workloads; "
                 "fastest to operate.",
                 "Cloud provider has the master key; some "
                 "regulators (RBI, MAS) raise eyebrows for "
                 "tier-1 data."],
                ["<strong>BYOK</strong>",
                 "Bank owns the master, imports key material; "
                 "operationally simpler than HYOK; satisfies "
                 "many regulators.",
                 "Cloud KMS still does the operations; if the "
                 "cloud is compromised, plaintext is at risk."],
                ["<strong>HYOK / EKM (External Key Manager)</strong>",
                 "Highest assurance: keys never leave the bank "
                 "HSM; cloud calls back per encrypt/decrypt. "
                 "Required by some EU and Indian regulators for "
                 "the most sensitive data.",
                 "Latency, availability and operational "
                 "complexity; the bank’s HSM is the new single "
                 "point of failure."],
                ["<strong>Confidential computing + cloud KMS</strong>",
                 "Workloads where data must remain private even "
                 "from the cloud admin; tokenisation, AI on "
                 "sensitive data.",
                 "Newer technology; verify FIPS, attestation, "
                 "and supply chain."],
            ]
        )
        + H3("6.3  SOC and tooling — buy, build, or hybrid")
        + table(
            ["Choice", "When it wins", "Watch-outs"],
            [
                ["<strong>Build your own SOC + SIEM</strong>",
                 "Largest banks with global footprint and 24×7 "
                 "talent; deep customisation needed for tier-1 "
                 "fraud and AML integration.",
                 "Talent retention is the silent killer."],
                ["<strong>Hybrid SOC with MSSP</strong>",
                 "Most common: keep tier-1 in-house, outsource "
                 "tier-2 / tier-3 monitoring to a Managed "
                 "Security Services Provider (HCLTech, IBM, "
                 "Accenture, Atos, NTT, Wipro, Tata, Kyndryl).",
                 "Run-book ownership, escalation paths must be "
                 "tested and rehearsed."],
                ["<strong>Pure outsourced</strong>",
                 "Smaller banks, fintechs without 24×7 ops.",
                 "Regulator expects you to own the outcomes; "
                 "demonstrate governance."],
            ]
        )
    )
    return TopicSection(
        "6.  Decision matrices — IdP, key custody, SOC model",
        "intermediate", body)


def _sec7() -> TopicSection:
    body = (
        example(
            "ICBC London — the November 2023 ransomware lessons",
            ol([
                "ICBC Financial Services in New York was hit by "
                "Lockbit ransomware in November 2023, disrupting US "
                "Treasury settlements; trades had to be settled "
                "manually with USB drives carried between offices.",
                "Lessons drawn industry-wide: critical-third-party "
                "concentration risk is real; manual fallback "
                "procedures must be tested; backups alone do not "
                "give recovery if identity is also compromised.",
                "Regulator response: faster pace of TLPT under "
                "DORA, OCC and Fed letters on ransomware "
                "preparedness, FS-ISAC playbooks updated.",
            ])
        )
        + example(
            "Capital One 2019 — what really happened, and why it "
            "is still cited",
            ol([
                "A former AWS engineer exploited a Server-Side "
                "Request Forgery (SSRF) vulnerability in a "
                "misconfigured ModSecurity WAF rule to obtain "
                "temporary AWS credentials.",
                "Those credentials were attached to an "
                "over-permissioned IAM role that could read S3 "
                "buckets containing 100M+ customer records.",
                "Detection was delayed because the data egress "
                "looked like normal application behaviour and "
                "GuardDuty was not yet tuned to flag it.",
                "Resolution drove industry-wide adoption of: IMDSv2 "
                "(blocks SSRF-fetch of credentials), least-"
                "privilege IAM by default, automated config "
                "review, anomaly detection on egress.",
                "Why it still matters: the failure was at L5–L6 "
                "(application + identity), not in the cloud "
                "primitives; cloud is as secure as your "
                "configuration discipline.",
            ])
        )
        + example(
            "Standard Chartered passwordless workforce login",
            ol([
                "Standard Chartered moved 90,000+ employees to "
                "FIDO2 passkeys / Windows Hello on Entra ID by "
                "2024.",
                "Phishing-resistant MFA mandatory for all "
                "production access; CyberArk for privileged "
                "session recording.",
                "Reported >50% reduction in password-related "
                "helpdesk tickets and meaningful drop in "
                "credential-phishing incidents.",
            ])
        )
        + example(
            "Indian Account Aggregator — security in a consent-led "
            "ecosystem",
            ol([
                "AAs and FIPs and FIUs all use mTLS with eKYC + "
                "ReBIT-defined consent artefacts.",
                "Consent artefacts are cryptographically signed "
                "by the customer; AAs never see plaintext "
                "financial data — the FIP encrypts to the FIU’s "
                "public key.",
                "RBI reviews AAs as Non-Banking Financial "
                "Companies (NBFC-AA); CERT-In incident reporting "
                "applies.",
            ])
        )
        + example(
            "EU bank preparing for DORA — first 12 months",
            ol([
                "Month 1–3: regulatory gap analysis vs DORA RTS "
                "and ITS; ICT risk framework mapped to "
                "ISO 27001 / NIST CSF 2.0.",
                "Month 4–6: third-party register populated; "
                "‘critical ICT third party’ designation reviewed "
                "with ECB; concentration risk quantified.",
                "Month 7–9: incident classification engine "
                "deployed in SIEM; major-incident notification "
                "playbooks rehearsed under EBA timelines.",
                "Month 10–12: TIBER-EU TLPT scoping with national "
                "competent authority; cyber recovery vault "
                "tested; board attestation prepared.",
            ])
        )
    )
    return TopicSection(
        "7.  Worked examples — five real BFSI security stories",
        "intermediate", body)


def _sec8() -> TopicSection:
    return TopicSection(
        "8.  Questions a leader asks in any security review",
        "basic",
        ol([
            "Who are our identity providers — workforce, customer, "
            "machine — and is MFA phishing-resistant for all "
            "privileged access?",
            "What is our cryptographic inventory, and what is the "
            "PQC migration plan?",
            "Where are our HSMs, who can access them, and which "
            "data is HYOK / EKM vs cloud-managed?",
            "What is our zero-trust state — by service, not just "
            "as a slogan? Which services still rely on "
            "network-perimeter trust?",
            "How quickly can we rotate certificates and secrets "
            "estate-wide? When did we last test a mass rotation?",
            "What is our SBOM and supply-chain coverage; can we "
            "answer ‘are we exposed to library X?’ in under 24 "
            "hours?",
            "What did our last red-team / TLPT exercise find, "
            "and have those findings been closed?",
            "What is our incident-reporting clock under DORA / "
            "NYDFS / SEC / RBI / MAS, and have we rehearsed "
            "hitting them?",
            "How are AI / ML models inventoried; do high-risk "
            "models have documented evaluation and post-market "
            "monitoring?",
            "What is our APP fraud reimbursement exposure and "
            "control posture?",
            "Where is our cyber recovery vault; when did we last "
            "fully restore from it?",
            "What is the credible exit plan from each critical "
            "vendor / cloud, and when did we test it?",
        ]))


def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘We have ISO 27001, we’re secure.’ — ISO 27001 is a "
            "management-system standard; it tells you the bank "
            "has processes, not that they work. Test outcomes, "
            "not certificates.",
            "‘Zero trust means we replaced the VPN.’ — Zero trust "
            "is identity, device, segmentation, continuous "
            "evaluation and encryption. ZTNA is one corner.",
            "‘MFA is on, we’re fine.’ — SMS and TOTP MFA are "
            "phishable; modern attackers run real-time relay "
            "phishing kits. Phishing-resistant FIDO2 / passkeys "
            "are the bar.",
            "‘PQC is years away.’ — Long-lived data is "
            "‘harvest-now, decrypt-later’. Inventory and "
            "migration must start now.",
            "‘The cloud is secure by default.’ — The shared-"
            "responsibility model says <em>you</em> own "
            "configuration. Capital One, Pegasus Airlines, "
            "Toyota, MOVEit — all configuration failures.",
            "‘We outsource the SOC, so we’re covered.’ — "
            "Regulators hold you accountable; outsourcing is a "
            "delivery choice, not a transfer of liability.",
            "‘DORA only matters if we’re EU-based.’ — Any bank "
            "operating in the EU is in scope; many UK and Asian "
            "groups are aligning globally to avoid running two "
            "regimes.",
            "‘Backups are immutable, ransomware can’t hurt us.’ — "
            "Only if your <em>identity</em> domain is also "
            "isolated from the backup domain; otherwise the "
            "attacker who took your AD can take your backups.",
            "‘Our AI is behind the firewall, no governance "
            "needed.’ — Not under EU AI Act, MAS FEAT, or NIST "
            "AI RMF. Risk-classify and document.",
            "‘We rotate keys yearly, we’re compliant.’ — "
            "Rotation cadence depends on classification and on "
            "exposure events; fixed annual rotation is "
            "yesterday’s baseline.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("IAM / CIAM", "Identity and Access Management / "
                "Customer IAM — workforce / customer identity "
                "stacks."),
            ("OIDC / SAML / OAuth 2.0", "Identity and authorisation "
                "protocols — OpenID Connect / SAML 2.0 / OAuth "
                "2.0."),
            ("FIDO2 / WebAuthn / passkey", "Public-key, "
                "phishing-resistant authentication standards."),
            ("MFA / SCA / RBA", "Multi-Factor / Strong Customer / "
                "Risk-Based Authentication."),
            ("PAM", "Privileged Access Management — CyberArk, "
                "BeyondTrust, Delinea, HashiCorp Boundary."),
            ("RBAC / ABAC / ReBAC", "Authorisation models — "
                "role / attribute / relationship based."),
            ("OPA / Cedar / Kyverno", "Policy-as-code engines."),
            ("HSM", "Hardware Security Module — tamper-resistant "
                "key custody (Thales, Entrust, Utimaco, IBM, "
                "AWS / Azure / GCP / OCI Cloud HSMs)."),
            ("FIPS 140-3", "US/Canadian standard for cryptographic "
                "modules; Level 3 typical for BFSI HSMs."),
            ("KMS / BYOK / HYOK / EKM", "Key Management Service / "
                "Bring-Your-Own-Key / Hold-Your-Own-Key / "
                "External Key Manager."),
            ("PKI", "Public Key Infrastructure — internal CAs, "
                "external CAs, eIDAS QTSPs."),
            ("PQC", "Post-Quantum Cryptography — NIST FIPS "
                "203 / 204 / 205, finalised Aug 2024."),
            ("Crypto-agility", "Code that can swap cryptographic "
                "primitives without rewriting; precondition for "
                "PQC migration."),
            ("Zero Trust / ZTNA / SASE", "‘Never trust, always "
                "verify’ architecture; ZTNA replaces VPN; SASE "
                "fuses ZTNA + SD-WAN + CASB + SWG + FWaaS."),
            ("EDR / XDR / SSPM / CNAPP / CSPM", "Endpoint / "
                "extended detection-response; SaaS Security "
                "Posture; Cloud-Native Application Protection; "
                "Cloud Security Posture Management."),
            ("SAST / DAST / SCA / SBOM", "Static / Dynamic "
                "application security testing; Software "
                "Composition Analysis; Software Bill of "
                "Materials."),
            ("SIEM / SOAR", "Security Information & Event "
                "Management / Security Orchestration, Automation "
                "and Response."),
            ("MITRE ATT&CK", "Knowledge base of adversary "
                "tactics, techniques, and procedures."),
            ("TLPT / TIBER-EU / CBEST / iCAST", "Threat-Led "
                "Penetration Testing frameworks (EU, UK, HK)."),
            ("DORA", "EU Digital Operational Resilience Act — in "
                "force 17 January 2025."),
            ("NIS2", "EU Network and Information Security "
                "Directive 2 — applies from October 2024."),
            ("EU AI Act", "EU regulation on AI — in force August "
                "2024, phased through August 2026."),
            ("EU CRA", "Cyber Resilience Act — adopted 2024; "
                "product-side cyber rules including SBOM."),
            ("UK CTP regime", "UK Critical Third Parties under "
                "FSMA 2023."),
            ("FCA Consumer Duty / Operational Resilience", "UK "
                "consumer-outcome and resilience policy regimes."),
            ("RBI IT Governance MD / Cyber Security Framework", "India "
                "central-bank IT and cyber rules; 2023 update."),
            ("DPDP Act 2023", "India Digital Personal Data "
                "Protection Act."),
            ("NYDFS Part 500", "New York DFS Cybersecurity "
                "Regulation; 2023 amendments."),
            ("NIST CSF 2.0", "Cybersecurity Framework 2.0 — Feb "
                "2024; six functions Govern/Identify/Protect/"
                "Detect/Respond/Recover."),
            ("MAS TRM / FEAT", "Singapore Technology Risk "
                "Management Guidelines / Fairness, Ethics, "
                "Accountability, Transparency principles for AI."),
            ("HKMA C-RAF", "Cyber Resilience Assessment Framework, "
                "Hong Kong."),
            ("APRA CPS 234 / CPS 230", "Australian prudential "
                "information-security and operational-risk "
                "standards."),
            ("FATF / AML / CFT", "Financial Action Task Force; "
                "Anti-Money Laundering / Counter-Financing of "
                "Terrorism."),
            ("PCI DSS 4.0", "Payment Card Industry Data Security "
                "Standard; March 2025 fully in force."),
            ("SWIFT CSCF", "Customer Security Controls Framework "
                "— annual attestation by every SWIFT user."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
