"""BFSI Domain Platforms · 05 — Cards & switches (Visa/Mastercard/RuPay flows in depth)."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="VI.5",
        slug="05-cards-and-switches",
        title="Cards & switches — Visa, Mastercard, RuPay flows in depth",
        one_liner=(
            "When you tap your card at a coffee shop in London and money leaves your "
            "account in Mumbai milliseconds later, a complex choreography of acquirers, "
            "switches, networks, and issuers has occurred. This topic takes you from "
            "the physics of a contactless tap through ISO 8583 message anatomy, "
            "interchange economics with real numbers, EMV and 3-D Secure cryptography, "
            "network tokenisation (Apple Pay, Google Pay), the chargeback lifecycle, "
            "domestic scheme strategies (RuPay, UnionPay, Elo), Banking-as-a-Service "
            "card platforms (Marqeta, Lithic, M2P), and the regulatory landscape "
            "(PCI DSS 4.0, RBI tokenisation mandate, EU IFR and SCA, US Durbin "
            "Amendment). After this topic you can lead a card programme review, "
            "evaluate an issuer-processor RFP, or challenge a switch migration plan "
            "with confidence."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


# ------------------------------------------------------------------ 0
def _sec0() -> TopicSection:
    body = (
        primer(
            p("Card payments are the most universally accepted, complex, and profitable "
              "payment mechanism in BFSI. Global card transaction volume exceeded "
              "$40 trillion in 2024. While instant-payment rails (UPI, FedNow, PIX, "
              "FPS) are growing rapidly, the four-party card model remains the backbone "
              "of global consumer and corporate commerce — and the single largest revenue "
              "line for many retail banks.")
        )
        + H3("0.1  IT-side anchor — a global DNS resolution")
        + it_anchor(
            p("When you type a URL, your browser asks a local resolver, which asks a "
              "root server, which asks a TLD server, which asks the authoritative name "
              "server to return the exact IP address. Card payments work the same way. "
              "The shop's terminal does not know your bank. It asks the shop's bank "
              "(the Acquirer), which asks the Network (Visa or Mastercard), which reads "
              "the first 6–8 digits of your card number (the BIN — Bank Identification "
              "Number) to route the message to your specific bank (the Issuer), which "
              "returns an approval or decline. The entire round trip must complete in "
              "under 2 seconds, typically under 500 milliseconds.")
        )
        + H3("0.2  BFSI-side anchor — buying a coffee with a tap")
        + bfsi_anchor(
            p("You buy a £3 coffee and tap your Mastercard. The terminal says "
              "'Approved' in one second. But no money actually moved yet. What happened "
              "was a cryptographic promise: your bank verified your available balance, "
              "placed a £3 hold (an 'authorization hold'), and promised the shop's bank "
              "it will send the money during the next settlement cycle (typically T+1). "
              "That split between the instant 'authorization' and the overnight "
              "'clearing and settlement' is the fundamental architecture of the card "
              "industry — and it is radically different from UPI or FedNow where "
              "authorization and settlement are simultaneous.")
        )
        + H3("0.3  The card industry at a glance")
        + table(
            ["Metric", "Approximate 2024 figure"],
            [
                ["Global card transactions (value)", "$41 trillion (Nilson Report)"],
                ["Visa annual transaction volume", "~$15 trillion across 4.3 billion cards"],
                ["Mastercard annual transaction volume", "~$9 trillion across 3.1 billion cards"],
                ["RuPay cards issued (India)", "~900 million (NPCI)"],
                ["UnionPay cards issued (China)", "~9.4 billion (largest by card count)"],
                ["Global interchange revenue pool", "~$130 billion annually"],
                ["Average US credit card interchange", "~2.2% (uncapped)"],
                ["EU capped credit card interchange", "0.3% (IFR regulation)"],
            ]
        )
        + callout("Related topics in this bible",
            ul([
                "<a href='02-payments-engines.html'><strong>VI.2 — Payments engines</strong></a> "
                "— card settlement flows through the bank's payments hub alongside other rails.",
                "<a href='01-core-banking-platforms.html'><strong>VI.1 — Core banking</strong></a> "
                "— the core holds the cardholder's account, credit limit, and GL postings.",
                "<a href='03-lending-and-originations.html'><strong>VI.3 — Lending</strong></a> "
                "— credit-card lending, card-linked EMI, and BNPL connect cards to lending platforms.",
                "<a href='../security-risk/01-security-identity-regulators.html'><strong>V.1 — Security &amp; identity</strong></a> "
                "— HSMs, PCI DSS, and authentication underpin every card transaction.",
                "<a href='../security-risk/02-fraud-aml-sanctions.html'><strong>V.2 — Fraud &amp; AML</strong></a> "
                "— real-time fraud scoring runs on every card authorization.",
            ]),
            "info")
    )
    return TopicSection("0.  Primer — anchored to things you already know", "basic", body)


# ------------------------------------------------------------------ 1
def _sec1() -> TopicSection:
    body = (
        p("Card payments exist to solve the fundamental problem of trust between "
          "strangers at global scale. The four-party model provides the rules, the "
          "routing, and the economic incentives that make a card issued by a bank in "
          "Mumbai work at a shop in London without the two banks ever having a direct "
          "relationship.")
        + H3("1.1  The Five Actors")
        + ol([
            "<strong>The Cardholder:</strong> You, the consumer or corporate spender.",
            "<strong>The Merchant:</strong> The coffee shop, the airline, the e-commerce "
            "site.",
            "<strong>The Issuer:</strong> Your bank (HDFC, Citi, Chase, Barclays) — the "
            "bank that issued the card, holds your money or extends your credit line, "
            "bears the fraud risk, and earns interchange revenue.",
            "<strong>The Acquirer (Merchant's Bank):</strong> The bank or processor "
            "that provides the merchant with a terminal or payment gateway, collects "
            "transactions, and settles funds to the merchant's account. Examples: "
            "Worldpay (FIS), Chase Paymentech, Adyen, Fiserv.",
            "<strong>The Network (Scheme):</strong> Visa, Mastercard, RuPay, Discover, "
            "UnionPay, JCB, Cartes Bancaires, Elo. The network sits in the middle, "
            "setting rules, routing messages, managing settlement, and enforcing "
            "dispute resolution frameworks.",
        ])
        + H3("1.2  Why the model works")
        + ul([
            "<strong>Guaranteed payment:</strong> The merchant gets paid (minus fees) "
            "even if the cardholder later defaults — the Issuer bears the credit risk.",
            "<strong>Consumer protection:</strong> Chargebacks give consumers the right "
            "to dispute unauthorized or defective transactions — a right that does not "
            "exist in most instant-payment rails.",
            "<strong>Global interoperability:</strong> A Visa card issued in India works "
            "at any Visa-accepting merchant in 200+ countries without bilateral "
            "agreements between the banks.",
            "<strong>Revenue engine:</strong> Interchange (paid by the Acquirer to the "
            "Issuer) funds card rewards, loyalty programmes, and covers fraud losses. "
            "For many retail banks, card interchange is 15–25% of non-interest income.",
        ])
    )
    return TopicSection("1.  Why card networks exist — the Four-Party Model",
                        "basic", body)


# ------------------------------------------------------------------ 2
def _sec2() -> TopicSection:
    body = (
        mermaid(
            'sequenceDiagram\n'
            '  autonumber\n'
            '  participant C as Cardholder\n'
            '  participant M as Merchant POS\n'
            '  participant A as Acquirer\n'
            '  participant N as Network (Visa/MC)\n'
            '  participant I as Issuer (Your Bank)\n'
            '  C->>M: Tap or insert card\n'
            '  M->>A: Auth Request (ISO 8583 0100)\n'
            '  A->>N: Route by BIN\n'
            '  N->>I: Auth Request to Issuer\n'
            '  I-->>I: Check balance, PIN, fraud score, EMV cryptogram\n'
            '  I->>N: Auth Response (Approved/Declined + Auth Code)\n'
            '  N->>A: Auth Response\n'
            '  A->>M: Terminal displays Approved\n'
            '  M->>C: Hand over coffee\n'
            '  Note over M,A: End of day: Merchant batches out\n'
            '  A->>N: Clearing file (all transactions)\n'
            '  N->>I: Net settlement instruction\n'
            '  Note over N,I: T+1: Central bank moves net funds',
            "Authorization (real-time) followed by clearing and settlement (batch)."
        )
        + p("The diagram shows the two-phase nature of card payments. Phase 1 "
            "(authorization) is real-time and answers 'can this customer pay?'. "
            "Phase 2 (clearing and settlement) is batch and answers 'how much does "
            "each bank owe each other today?'. This separation is what enables the "
            "card industry's scale — authorizations are lightweight messages, while "
            "settlement moves actual money in bulk.")
    )
    return TopicSection("2.  The core concept in one picture", "basic", body)


# ------------------------------------------------------------------ 3
def _sec3() -> TopicSection:
    body = (
        H3("3.1  Phase 1: Authorization (real-time, under 2 seconds)")
        + p("When you tap, the POS terminal generates an ISO 8583 0100 authorization "
            "request message. This message contains approximately 40 data elements:")
        + ul([
            "<strong>Primary Account Number (PAN):</strong> Your 16-digit card number "
            "(or a network token replacing it).",
            "<strong>Amount and currency:</strong> £3.00 GBP.",
            "<strong>Merchant Category Code (MCC):</strong> 5812 (eating places, "
            "restaurants) — this code determines interchange tier and controls "
            "corporate card expense policies.",
            "<strong>Card acceptor terminal ID:</strong> Unique terminal identifier.",
            "<strong>EMV Application Cryptogram (ARQC):</strong> A one-time "
            "cryptographic proof that the physical chip is present and the transaction "
            "is not a replay.",
            "<strong>Processing code:</strong> 00 = purchase, 01 = cash advance, "
            "20 = refund.",
        ])
        + p("The message flows: POS → Acquirer processor → Network switch → Issuer "
            "processor. The Issuer's authorization system performs: EMV cryptogram "
            "validation (via HSM), balance or credit-limit check, velocity checks "
            "(how many transactions in the last hour?), real-time fraud scoring "
            "(see V.2), and PIN or CVM (Cardholder Verification Method) validation. "
            "If all checks pass, the Issuer places a hold on the funds and returns "
            "an ISO 8583 0110 response with an authorization code.")

        + H3("3.2  Phase 2: Clearing (batch, end of day)")
        + p("At the end of each business day, the merchant's terminal 'batches out' — "
            "sending all approved authorizations to the Acquirer. The Acquirer compiles "
            "a clearing file and transmits it to the Network. The Network sorts "
            "transactions by Issuer, calculates interchange fees for each transaction "
            "(based on card type, MCC, transaction type, and region), and produces "
            "net clearing reports.")
        + p("During clearing, the Network also applies scheme fees (assessments): "
            "a small per-transaction fee (typically 0.08–0.15%) that Visa or Mastercard "
            "charges for the routing, brand, and dispute infrastructure.")

        + H3("3.3  Phase 3: Settlement (T+1 or T+2)")
        + p("The Network calculates each bank's net position. If Bank A owes Bank B "
            "$10M and Bank B owes Bank A $8M, only a net $2M moves. Settlement happens "
            "through central bank settlement systems or designated settlement banks. "
            "Visa uses its own settlement bank (JPMorgan Chase in the US); Mastercard "
            "settles through commercial banks. RuPay settles through RBI's settlement "
            "infrastructure. After settlement, the Acquirer deposits the merchant's "
            "funds (minus the MDR) into the merchant's bank account.")

        + H3("3.4  ISO 8583 — the protocol that runs the world's cards")
        + p("ISO 8583 is the binary messaging standard used for card authorizations "
            "since 1987. It is not human-readable — each message is a packed bitmap of "
            "data elements. Every card network uses a variant (Visa's Base I, "
            "Mastercard's MDS, RuPay's proprietary format). The industry is slowly "
            "migrating to ISO 20022 (XML-based, richer data), but ISO 8583 will "
            "remain dominant for card auth through at least 2030.")
        + table(
            ["ISO 8583 field", "Data element", "Example"],
            [
                ["DE 2", "Primary Account Number", "4123 4567 8901 2345"],
                ["DE 3", "Processing Code", "00 (purchase)"],
                ["DE 4", "Transaction Amount", "000000000300 (£3.00)"],
                ["DE 18", "Merchant Category Code", "5812 (restaurants)"],
                ["DE 22", "POS Entry Mode", "071 (contactless chip)"],
                ["DE 38", "Authorization Code", "A1B2C3"],
                ["DE 39", "Response Code", "00 (approved)"],
                ["DE 55", "EMV Data (ARQC)", "Chip cryptogram + terminal data"],
            ]
        )
    )
    return TopicSection("3.  How it actually works — auth, clear, settle, and ISO 8583",
                        "intermediate", body)


# ------------------------------------------------------------------ 4
def _sec4() -> TopicSection:
    body = (
        H3("4.1  Card types")
        + table(
            ["Card type", "How it works", "Who bears credit risk"],
            [
                ["<strong>Debit card</strong>",
                 "Linked to a deposit account; authorization checks real-time balance.",
                 "Cardholder (funds must be available)"],
                ["<strong>Credit card</strong>",
                 "Linked to a credit line; cardholder pays later (interest if revolving).",
                 "Issuer (unsecured lending risk)"],
                ["<strong>Prepaid card</strong>",
                 "Pre-loaded with funds; not linked to a bank account. Used for gifting, "
                 "payroll, travel, government disbursements.",
                 "No credit risk (funds already received)"],
                ["<strong>Commercial / Corporate card</strong>",
                 "Issued to businesses for employee expenses. Often integrated with "
                 "expense management (SAP Concur, Navan). Higher interchange.",
                 "The company (corporate liability) or employee (individual liability)"],
                ["<strong>Virtual card</strong>",
                 "A card number generated for a single transaction or supplier. No "
                 "physical card. Used in B2B payments and travel.",
                 "Same as the underlying programme (credit, debit, or prepaid)"],
            ]
        )

        + H3("4.2  Network schemes — global and domestic")
        + table(
            ["Scheme", "Geography", "Key characteristics"],
            [
                ["<strong>Visa</strong>", "Global (200+ countries)",
                 "Largest by transaction value ($15T). VisaNet processes 65,000+ "
                 "TPS. Open-loop four-party model."],
                ["<strong>Mastercard</strong>", "Global (210+ countries)",
                 "Second-largest globally ($9T). Strong in Europe and emerging markets. "
                 "Banknet network."],
                ["<strong>RuPay</strong>", "India (expanding to SE Asia, Middle East)",
                 "NPCI's domestic scheme. ~900M cards. Zero MDR on debit (RBI subsidy). "
                 "Strategically important for India's payment sovereignty. Contactless "
                 "and credit variants growing fast."],
                ["<strong>UnionPay</strong>", "China (expanding globally)",
                 "Largest by card count (~9.4B). Dominates China's domestic market. "
                 "Growing international acceptance."],
                ["<strong>JCB</strong>", "Japan (niche global)",
                 "Japan's domestic scheme. Co-badged with Discover for international."],
                ["<strong>Cartes Bancaires</strong>", "France",
                 "France's dominant domestic scheme. All French debit cards carry CB "
                 "plus either Visa or Mastercard for international use."],
                ["<strong>Elo</strong>", "Brazil",
                 "Brazil's domestic scheme (Bradesco, Banco do Brasil, Caixa). Competes "
                 "with Visa/MC domestically."],
                ["<strong>American Express</strong>", "Global",
                 "Three-party model: Amex is both issuer and acquirer. Premium segment. "
                 "Higher interchange and MDR than Visa/MC."],
                ["<strong>Discover / Diners Club</strong>", "United States / Global",
                 "Three-party model. Smaller network; partners with JCB, UnionPay, "
                 "RuPay for international routing."],
            ]
        )

        + H3("4.3  Switch vendors — the engines behind the networks")
        + p("A 'switch' is the software engine that receives ISO 8583 messages, "
            "performs BIN-based routing, integrates with HSMs for cryptography, "
            "manages stand-in processing, and connects to card network gateways. "
            "The switch is the most performance-critical component in card "
            "processing — it must handle thousands of TPS with sub-second latency "
            "and 99.999% availability.")
        + table(
            ["Vendor / Product", "Origin", "Sweet spot"],
            [
                ["<strong>ACI Worldwide (BASE24-eps)</strong>", "United States",
                 "The legacy king. Runs ATM networks, POS acquiring, and issuing for "
                 "many tier-1 banks globally. Proven at massive scale."],
                ["<strong>FIS (NYCE, Connex)</strong>", "United States",
                 "Huge footprint in North America. Powers many tier-1 acquirers and "
                 "PIN debit networks."],
                ["<strong>Fiserv (Star, Accel)</strong>", "United States",
                 "US debit network and processing. Strong mid-tier footprint."],
                ["<strong>BPC (SmartVista)</strong>", "Switzerland / Global",
                 "Cloud-capable modern platform. Strong in emerging markets, digital "
                 "banks, and government payment programmes."],
                ["<strong>RS2 (BankWORKS)</strong>", "Malta / Global",
                 "Modern issuing and acquiring platform. Growing among European and "
                 "APAC processors."],
                ["<strong>Euronet (Ren)</strong>", "United States / Global",
                 "ATM management and EFT switching. Large footprint in Europe and "
                 "Asia."],
                ["<strong>FSS (Financial Software and Systems)</strong>", "India",
                 "Dominant in India for RuPay and UPI switching. Processes billions "
                 "of Indian transactions annually."],
                ["<strong>Marqeta (JIT funding)</strong>", "United States",
                 "Modern API-first card issuing platform. Just-In-Time (JIT) funding "
                 "model. Powers Square, DoorDash, Uber, Block, Klarna."],
                ["<strong>Lithic</strong>", "United States",
                 "Developer-first card issuing API. Virtual and physical cards. "
                 "Growing among fintechs and embedded-finance plays."],
                ["<strong>M2P Fintech</strong>", "India",
                 "API-first card issuance and banking infrastructure. Powers many "
                 "Indian fintechs and neobanks (Fi, Jupiter, slice)."],
            ]
        )
    )
    return TopicSection("4.  Types & variations — cards, schemes, switches",
                        "intermediate", body)


# ------------------------------------------------------------------ 5
def _sec5() -> TopicSection:
    body = (
        H3("5.1  Interchange economics — following the money")
        + p("Interchange is the fee paid by the Acquirer to the Issuer on every card "
            "transaction. It is the economic engine of the card industry — it funds "
            "rewards, absorbs fraud losses, and finances the credit risk of lending.")
        + table(
            ["Component", "Who pays", "Who receives", "Typical range"],
            [
                ["<strong>Interchange</strong>",
                 "Acquirer", "Issuer",
                 "US credit: 1.5–2.5%; EU credit: 0.3% (capped); India debit: 0% "
                 "(RuPay subsidy); US debit: 0.05% + $0.21 (Durbin cap for large banks)"],
                ["<strong>Scheme / Assessment fees</strong>",
                 "Both Acquirer and Issuer", "Network (Visa/MC)",
                 "0.08–0.15% per transaction + fixed per-transaction fees"],
                ["<strong>Acquirer margin</strong>",
                 "Merchant (via MDR)", "Acquirer",
                 "0.2–0.5% in competitive markets; higher for high-risk merchants"],
                ["<strong>MDR (total)</strong>",
                 "Merchant", "Split across above",
                 "US credit: 2.0–3.0%; EU credit: 0.7–1.2%; India UPI/RuPay debit: 0%; "
                 "India credit: 1.8–2.5%"],
            ]
        )
        + example("Where $100 goes in a US credit card purchase",
            p("Merchant charges $100. MDR is 2.5%, so merchant receives $97.50. "
              "Of the $2.50: $1.80 goes to the Issuer (Chase) as interchange — Chase "
              "uses this to fund 1.5% cash-back rewards ($1.50) and absorb fraud/credit "
              "losses ($0.30). $0.13 goes to Visa as scheme fees. $0.57 goes to the "
              "Acquirer (Worldpay) as margin. When politicians cap interchange (as the "
              "EU did at 0.3% for credit), the $1.80 drops to $0.30, and credit card "
              "rewards virtually disappear — which is exactly what happened in Europe.")
        )

        + H3("5.2  EMV chip and contactless cryptography")
        + p("Magnetic stripes stored static data that could be cloned with a $20 "
            "skimmer. EMV (Europay, Mastercard, Visa) chips are tiny secure "
            "microprocessors. When you dip or tap, the terminal sends a challenge "
            "(unpredictable number + transaction data) to the chip. The chip uses "
            "a secret key (that never leaves the chip, stored in tamper-resistant "
            "silicon) to compute an Application Request Cryptogram (ARQC). The "
            "Issuer's HSM (Hardware Security Module) independently computes the "
            "expected cryptogram and compares. If they match, the physical card "
            "is proven present and the transaction is not a replay.")
        + p("Contactless (NFC) adds a radio interface but the cryptographic flow "
            "is identical. The key difference: contactless transactions below a "
            "floor limit (£100 UK, €50 EU, ₹5,000 India, $200 Australia) may skip "
            "PIN entry for speed — this is a risk trade-off set by the Issuer.")

        + H3("5.3  3-D Secure 2 (3DS2) — online authentication")
        + p("For e-commerce (card-not-present) transactions, there is no physical "
            "chip to prove. 3-D Secure is the protocol that adds authentication:")
        + ol([
            "The merchant's payment page sends a 3DS2 authentication request to the "
            "card network's Access Control Server (ACS).",
            "The ACS evaluates risk factors: device fingerprint, IP geolocation, "
            "transaction history, behavioural biometrics.",
            "If low-risk, the ACS approves silently (frictionless flow — the customer "
            "sees nothing). If medium-risk, the ACS challenges: biometric (Face ID, "
            "fingerprint via the banking app), SMS OTP, or in-app push notification.",
            "If the cardholder authenticates, liability for fraud shifts from the "
            "merchant to the Issuer. This liability shift is the economic incentive "
            "for merchants to implement 3DS2.",
        ])
        + p("In the EU and India, 3DS2 is mandatory (PSD2 SCA in Europe, RBI 2FA "
            "mandate in India). In the US and many APAC markets, it is optional — "
            "merchants weigh the friction cost (cart abandonment) against the fraud "
            "liability benefit.")

        + H3("5.4  Tokenisation — Apple Pay, Google Pay, and Card-on-File")
        + p("Tokenisation replaces the real card number (PAN) with a surrogate "
            "value (token) that is useless if stolen. Three types exist:")
        + table(
            ["Token type", "How it works", "Example"],
            [
                ["<strong>Device token</strong>",
                 "When you add a card to Apple Pay, the Network (Visa VTS or "
                 "Mastercard MDES) issues a Device Account Number (DAN) that only "
                 "works on that specific device's secure enclave. Each transaction "
                 "also generates a one-time cryptogram.",
                 "Apple Pay, Google Pay, Samsung Pay"],
                ["<strong>Card-on-File (CoF) token</strong>",
                 "When you save a card on Amazon or Netflix, the merchant stores a "
                 "network token instead of the real PAN. If the real card is reissued "
                 "(new expiry, new number), the token automatically updates via the "
                 "network's Token Lifecycle Management — no customer action needed.",
                 "Amazon, Netflix, Uber stored cards"],
                ["<strong>Acquirer / PSP token</strong>",
                 "The payment gateway (Stripe, Adyen, Razorpay) creates its own token "
                 "to reduce PCI scope. The real PAN is vaulted in the PSP's secure "
                 "environment.",
                 "Stripe tok_xxx, Razorpay token"],
            ]
        )
        + callout("Why RBI mandated tokenisation",
            p("In September 2021, RBI prohibited merchants and payment aggregators "
              "from storing actual card numbers (Card-on-File). From October 2022, "
              "all stored cards must use network tokens. This was a direct response "
              "to multiple data breaches at Indian e-commerce platforms where millions "
              "of PANs were leaked. India is the only major market where CoF "
              "tokenisation is mandatory — elsewhere it is an industry best practice."),
            "info")

        + H3("5.5  The chargeback lifecycle")
        + p("Chargebacks are the consumer protection mechanism unique to cards. "
            "When a cardholder disputes a transaction, the following lifecycle "
            "unfolds:")
        + ol([
            "<strong>Cardholder dispute (Day 0):</strong> Customer contacts the "
            "Issuer — 'I did not make this purchase' or 'The goods never arrived'.",
            "<strong>Issuer review (Day 0–5):</strong> Issuer checks EMV cryptogram "
            "(was the chip present?), 3DS authentication (was the cardholder "
            "verified?), and transaction details.",
            "<strong>Chargeback filing (Day 5–30):</strong> If the dispute has merit, "
            "the Issuer files a chargeback through the Network to the Acquirer. The "
            "transaction amount is provisionally credited to the cardholder and debited "
            "from the merchant's settlement.",
            "<strong>Merchant representment (Day 30–45):</strong> The merchant can "
            "challenge the chargeback by providing evidence: signed delivery receipt, "
            "3DS proof, terms of service agreement.",
            "<strong>Arbitration (Day 45–120):</strong> If the dispute is not "
            "resolved, the Network arbitrates. Visa's chargeback window is 120 "
            "days from the transaction date; Mastercard's is 120 days. The losing "
            "party pays a Network arbitration fee ($500–$1,000 per case).",
        ])
        + p("At scale, chargebacks are expensive. A merchant with a chargeback rate "
            "above 1% of transactions risks entering a Network monitoring programme "
            "(Visa VDMP, Mastercard ECM), which imposes fines, operational "
            "requirements, and ultimately termination of card acceptance.")

        + H3("5.6  Banking-as-a-Service (BaaS) card platforms")
        + p("Modern fintechs do not build switches from scratch. They use API-first "
            "card issuance platforms that handle BIN sponsorship, network "
            "connectivity, compliance, and physical/virtual card production:")
        + table(
            ["Platform", "Origin", "Key differentiator"],
            [
                ["<strong>Marqeta</strong>", "United States",
                 "Just-In-Time (JIT) funding: the Issuer is called via webhook at "
                 "authorization time to approve/decline and fund from any source. "
                 "Powers Block (Square Card), DoorDash, Uber, Klarna, JP Morgan "
                 "commercial cards."],
                ["<strong>Lithic</strong>", "United States",
                 "Developer-first API for virtual and physical card issuance. Strong "
                 "in expense management, corporate cards, and embedded finance."],
                ["<strong>M2P Fintech</strong>", "India",
                 "India's leading BaaS card platform. Powers Fi, Jupiter, slice, and "
                 "50+ fintechs. RuPay and Visa issuance. API for prepaid, debit, "
                 "and credit programmes."],
                ["<strong>Galileo (SoFi)</strong>", "United States",
                 "Payment platform powering SoFi, Chime, Robinhood, MoneyLion. "
                 "Full processing stack."],
                ["<strong>GPS (Global Processing Services)</strong>", "United Kingdom",
                 "European BaaS leader. Powers Revolut, Starling, Curve. Visa and "
                 "Mastercard certified."],
            ]
        )
    )
    return TopicSection(
        "5.  Advanced — interchange math, EMV, 3DS2, tokenisation, "
        "chargebacks, BaaS",
        "advanced", body)


# ------------------------------------------------------------------ 6
def _sec6() -> TopicSection:
    body = (
        p("Card payments sit at the intersection of payment regulation, consumer "
          "protection, data security, and competition policy. The regulatory burden "
          "is among the heaviest in all of BFSI.")
        + table(
            ["Region", "Key regulations", "Impact on card architecture"],
            [
                ["<strong>Global</strong>",
                 "PCI DSS 4.0 (effective March 2025): 12 requirements for storing, "
                 "processing, and transmitting cardholder data. PCI PIN: HSM and PIN "
                 "handling requirements. PCI 3DS: certification for 3-D Secure. "
                 "PCI P2PE: point-to-point encryption of card data from terminal to "
                 "acquirer.",
                 "PCI DSS 4.0 adds continuous monitoring, risk-based approach, and "
                 "stricter authentication requirements. Network tokenisation reduces "
                 "PCI scope by eliminating PAN storage. Every entity that touches "
                 "card data must be PCI certified — this drives architecture (who "
                 "stores what where)."],
                ["<strong>India</strong>",
                 "RBI Card-on-File tokenisation mandate (Oct 2022): merchants cannot "
                 "store PANs. RBI zero-MDR on RuPay debit and UPI. RBI 2FA mandate: "
                 "all online transactions require Additional Factor Authentication "
                 "(AFA — typically OTP). RBI Master Direction on Payment Aggregators "
                 "(2020, amended 2024). RBI data localisation: card transaction data "
                 "must be stored in India.",
                 "Every Indian e-commerce platform must use network tokens. Online "
                 "checkout in India always requires OTP (higher security, higher "
                 "cart abandonment). Payment aggregators (Razorpay, PayU, Cashfree) "
                 "must obtain RBI licence."],
                ["<strong>United States</strong>",
                 "Durbin Amendment (Dodd-Frank 2010): caps debit interchange at "
                 "$0.21 + 0.05% for banks with assets above $10B. Credit interchange "
                 "remains uncapped. CFPB proposed late-fee cap ($8 vs. previous $30+). "
                 "No SCA mandate (3DS is optional). State privacy laws (CCPA) affect "
                 "card data handling.",
                 "Durbin created two-tier pricing: large bank debit interchange is "
                 "capped; small bank debit is exempt. This distorts competitive "
                 "dynamics. Uncapped credit interchange funds the massive US rewards "
                 "ecosystem — any cap would reshape consumer banking."],
                ["<strong>European Union</strong>",
                 "Interchange Fee Regulation (IFR 2015): caps consumer debit at 0.2%, "
                 "consumer credit at 0.3%. PSD2 Strong Customer Authentication (SCA): "
                 "3DS2 mandatory for most online payments. EMV liability shift for "
                 "non-chip transactions.",
                 "IFR eliminated high rewards but made card acceptance cheaper for "
                 "merchants. SCA added friction to online checkout. Exemptions exist "
                 "for low-value transactions (under €30, up to 5 consecutive "
                 "transactions), trusted beneficiaries, and merchant-initiated "
                 "transactions (subscriptions)."],
                ["<strong>United Kingdom</strong>",
                 "Post-Brexit, UK retained IFR caps. FCA Consumer Duty applies to "
                 "card products (fair value assessment of fees and charges). PSR "
                 "(Payment Systems Regulator) oversees Visa/MC fees. Strong Customer "
                 "Authentication via FCA rules.",
                 "PSR has scrutinised Visa and Mastercard scheme fee increases. "
                 "UK merchants pay higher cross-border interchange for EU-issued "
                 "cards post-Brexit."],
                ["<strong>Singapore</strong>",
                 "MAS Payment Services Act 2019: regulates card issuance, acquiring, "
                 "and processing. No interchange caps. MAS TRM guidelines apply to "
                 "card system resilience. PDPA for cardholder data.",
                 "Market-driven interchange. High card penetration competing with "
                 "PayNow (instant payments). MAS expects robust BCP for card "
                 "processing systems."],
            ]
        )
        + red_flag(
            p("PCI DSS 4.0 is not a checklist exercise. It requires <strong>continuous "
              "monitoring</strong> and a risk-based approach. Banks that treat PCI as an "
              "annual audit will fail the new standard. The transition deadline for all "
              "future-dated requirements is 31 March 2025.")
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
                ["<strong>Build vs buy an issuing/acquiring switch</strong>",
                 "Buying (ACI BASE24, BPC SmartVista, RS2) is faster and comes with "
                 "network certifications. Building in-house allows unique products "
                 "and API-first architectures but requires deep ISO 8583, HSM, and "
                 "network certification expertise. Modern fintechs increasingly use "
                 "BaaS platforms (Marqeta, Lithic, M2P) instead of building or buying "
                 "traditional switches."],
                ["<strong>Issuer processor: in-house vs outsourced</strong>",
                 "In-house processing (the bank runs its own auth, clearing, and "
                 "settlement systems) gives maximum control and data ownership. "
                 "Outsourced processing (FIS, Fiserv, i2c, FSS) reduces capex and "
                 "operational burden but creates vendor dependency. Tier-1 issuers "
                 "(Chase, HDFC, SBI) typically process in-house; tier-2 and neobanks "
                 "typically outsource."],
                ["<strong>Single-scheme vs multi-scheme strategy</strong>",
                 "Issuing on only Visa or only Mastercard simplifies operations but "
                 "creates concentration risk. Multi-scheme (Visa + Mastercard + RuPay) "
                 "provides negotiating leverage on scheme fees and satisfies regulatory "
                 "preferences (RBI actively encourages RuPay adoption). Indian banks "
                 "commonly issue both Visa/MC and RuPay."],
                ["<strong>On-premise HSMs vs cloud HSMs</strong>",
                 "Physical HSMs (Thales Luna, Utimaco) in the bank's data centre offer "
                 "maximum control and are required by some regulators. Cloud HSMs (AWS "
                 "Payment Cryptography, Azure Payment HSM) are now PCI-PIN certified "
                 "and offer auto-scaling, but exit strategy and key custody require "
                 "careful design. Hybrid is increasingly common."],
                ["<strong>Network tokenisation: full adoption vs partial</strong>",
                 "Full tokenisation (no PAN stored anywhere except issuer and network) "
                 "dramatically reduces PCI scope and breach impact. But it requires "
                 "end-to-end ecosystem readiness: acquirer, PSP, merchant, and issuer "
                 "must all support tokens. Mandated in India; voluntary elsewhere."],
                ["<strong>Contactless floor limit: high vs low</strong>",
                 "Higher floor limits (£100 UK, $200 Australia) improve speed and "
                 "customer experience but increase fraud exposure if a card is stolen. "
                 "Lower limits (€50 EU) reduce fraud but add PIN friction. This is a "
                 "risk appetite decision set by the Issuer within scheme limits."],
            ]
        )
    )


# ------------------------------------------------------------------ 8
def _sec8() -> TopicSection:
    body = (
        example("Anatomy of a cross-border card authorization (1.2 seconds)",
            ol([
                "A customer in Mumbai taps their HDFC Mastercard at a Zara store in London.",
                "The London POS terminal generates an ISO 8583 0100 auth request in GBP (£45).",
                "The terminal sends to the Acquirer (Worldpay UK). Worldpay adds acquiring "
                "data and forwards to Mastercard Banknet. Latency: 20ms.",
                "Banknet reads the BIN (5234xx — HDFC Bank), identifies the Issuer as HDFC "
                "India, converts £45 to ₹4,815 using Mastercard's daily wholesale FX rate, "
                "and routes to HDFC's issuer processor in Mumbai. Latency: 180ms "
                "(UK → Singapore → India network path).",
                "HDFC's authorization system validates the EMV cryptogram (HSM call: 15ms), "
                "checks the credit limit (balance check: 5ms), runs the real-time fraud "
                "model (SageMaker inference: 40ms), verifies the CVM (signature for "
                "contactless above ₹5,000 floor). Total issuer processing: 80ms.",
                "HDFC approves, places a ₹4,815 + 3.5% cross-currency markup = ₹4,983 hold "
                "on the credit line, returns ISO 8583 0110 response.",
                "Response flows back: HDFC → Banknet → Worldpay → POS terminal. Total "
                "round trip: ~1.2 seconds. Terminal displays 'Approved'.",
                "Next day: Mastercard clearing nets all HDFC↔Worldpay transactions and "
                "settles the GBP amount through settlement banks.",
            ])
        )
        + example("Stand-in processing during an issuer outage (India)",
            p("HDFC Bank's core banking system goes down for a scheduled maintenance "
              "window (2 AM–4 AM IST). During this period, their card switch enters "
              "Stand-In Processing (STIP) mode. The switch uses cached cardholder data "
              "and pre-defined rules: approve domestic transactions up to ₹5,000 if the "
              "last known available balance exceeds ₹25,000; decline international "
              "transactions entirely; decline cash advances. When the core returns, the "
              "switch replays all STIP authorizations for balance validation. Any that "
              "exceed the actual balance become the bank's liability. STIP is a "
              "calculated risk — stranding customers at ATMs at 2 AM is worse than "
              "absorbing a small loss on post-fact over-limit transactions.")
        )
        + example("The economics of RuPay vs Visa for an Indian issuer",
            p("An Indian bank issues 10 million debit cards: 6 million on RuPay and "
              "4 million on Visa. On a ₹1,000 POS purchase: RuPay MDR is zero (RBI "
              "subsidy) — the Issuer earns ₹0 interchange but receives RBI "
              "reimbursement of ₹0.15 per transaction (RuPay incentive scheme). Visa "
              "debit interchange is approximately 0.9%, earning the Issuer ₹9.00 per "
              "transaction. For the bank's P&L, Visa debit is 60× more profitable per "
              "transaction. But RBI strongly encourages RuPay adoption for financial "
              "inclusion (Jan Dhan accounts are mandated on RuPay). The bank must "
              "balance regulatory goodwill against interchange economics. Solution: "
              "issue RuPay for mass-market and Jan Dhan, Visa/MC for premium and "
              "credit segments.")
        )
        + example("Chargeback fraud and the EMV liability shift",
            p("A UK consumer reports that their card was used for a £2,000 online "
              "purchase at an electronics retailer. The retailer did not implement "
              "3DS2 (choosing to accept the fraud liability in exchange for lower "
              "checkout friction). The Issuer (Barclays) files a chargeback. Because "
              "the merchant chose not to use 3DS2, the liability shift means the "
              "merchant (not Barclays) bears the £2,000 loss plus a £15 chargeback "
              "processing fee. If the merchant had implemented 3DS2 and the "
              "cardholder had authenticated via biometric, the liability would have "
              "shifted to Barclays. This is the economic incentive that drives 3DS2 "
              "adoption — and why EU's SCA mandate eliminated the 'opt-out' choice.")
        )
        + example("Tokenisation migration at a large Indian e-commerce platform",
            p("An Indian e-commerce platform stored 45 million card-on-file PANs for "
              "repeat purchases. Under RBI's October 2022 tokenisation mandate, all "
              "PANs had to be replaced with network tokens. The migration involved: "
              "(1) integrating with Visa VTS and Mastercard MDES token requestor APIs, "
              "(2) batch-converting 45 million PANs to network tokens over 6 weeks, "
              "(3) implementing Token Lifecycle Management (when a card is reissued, "
              "the token auto-updates — reducing 'card expired' checkout failures by "
              "40%), (4) deleting all stored PANs from the platform's databases, "
              "reducing PCI DSS scope from 847 servers to 12. Net result: lower PCI "
              "compliance cost, lower breach risk, and paradoxically better checkout "
              "conversion (fewer expired-card failures).")
        )
    )
    return TopicSection("8.  Worked examples — numbers and decisions",
                        "intermediate", body)


# ------------------------------------------------------------------ 9
def _sec9() -> TopicSection:
    body = (
        H3("Questions a leader asks in any card programme review")
        + ol([
            "What is our interchange revenue per card type (credit, debit, prepaid, "
            "commercial), and how would a regulatory cap (Durbin-style) affect our P&L?",
            "What is our card fraud rate (basis points of loss per dollar processed), "
            "and how does it compare to network benchmarks?",
            "Are we PCI DSS 4.0 compliant, including the future-dated requirements "
            "(continuous monitoring, risk-based authentication)? What is our "
            "remediation timeline?",
            "What is our chargeback ratio, and are any merchant segments approaching "
            "Visa VDMP or Mastercard ECM monitoring thresholds?",
            "Have we implemented network tokenisation for all card-on-file use cases? "
            "If not, what is the timeline and what PCI scope reduction do we expect?",
            "What is our switch's maximum TPS capacity, and how does it compare to peak "
            "transaction volumes (Diwali, Black Friday, month-end salary day)?",
            "What is our STIP strategy? What floor limits do we use during issuer "
            "outages, and what is the historical loss from STIP approvals?",
            "Are we using 3DS2 for all e-commerce transactions, and what is the "
            "frictionless authentication rate vs challenge rate?",
            "What is our multi-scheme strategy — are we over-concentrated on one "
            "network? What are the scheme fee trends from Visa and Mastercard?",
            "What is our BaaS/embedded-card strategy — do we offer card issuance "
            "APIs to fintechs, or are we losing embedded-finance opportunities to "
            "Marqeta/M2P-powered competitors?",
        ])
        + red_flag(ul([
            "'We don't need HSMs if we use strong TLS.' — Completely false. PCI-PIN "
            "and network rules legally mandate hardware-level cryptography for PINs "
            "and EMV cryptograms. TLS protects data in transit; HSMs protect "
            "cryptographic keys at rest and during processing. They solve different "
            "problems.",
            "'Let's process card auths in the core banking batch.' — Authorization "
            "must happen in under 2 seconds. Core banking systems are designed for "
            "batch and are too slow for real-time card auth. This is why standalone "
            "switches exist as separate, latency-optimised systems.",
            "'We'll just use REST/JSON instead of ISO 8583.' — You can use JSON "
            "internally, but the second you connect to Visa, Mastercard, or any "
            "legacy acquirer, you must translate to ISO 8583 (or increasingly ISO "
            "20022). Ignoring ISO 8583 is not an option for any entity that touches "
            "card networks directly.",
            "'Chargebacks are just a cost of doing business.' — A chargeback ratio "
            "above 1% puts you in network monitoring programmes with escalating fines, "
            "operational requirements, and ultimately termination. Chargeback "
            "management is a strategic capability, not an accounting line item.",
            "'Zero MDR means cards are free for everyone.' — Zero MDR on RuPay debit "
            "is subsidised by the government. It benefits merchants and consumers but "
            "creates a revenue gap for issuers. If the subsidy is reduced, the "
            "economics shift dramatically. Build P&L models on both scenarios.",
            "'Apple Pay is just a wrapper — the card is the same.' — Apple Pay uses a "
            "Device Account Number (DAN) that is cryptographically different from the "
            "underlying PAN. A merchant breach that leaks DANs is useless to attackers "
            "because the DAN only works with the specific device's secure enclave. "
            "Tokenisation is a fundamental security upgrade, not a wrapper.",
            "'3DS adds too much friction — we should disable it.' — In the EU and "
            "India, 3DS/SCA is mandatory, not optional. In the US, disabling 3DS "
            "shifts fraud liability entirely to the merchant. The correct approach is "
            "to optimise frictionless authentication rates (risk-based analysis), not "
            "to disable authentication entirely.",
            "'We can build our own switch — it's just message routing.' — A production "
            "card switch requires: ISO 8583 message parsing across multiple network "
            "variants, HSM integration for PIN and cryptogram processing, BIN table "
            "management across 400,000+ BIN ranges, stand-in processing logic, "
            "network certification (6–12 months per scheme), and 99.999% uptime. "
            "Building is possible but requires a 50+ person team and 18+ months.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("Four-party model", "The card payment architecture with Cardholder, Merchant, "
             "Issuer, Acquirer, and Network as distinct roles."),
            ("Acquirer", "The bank or processor that provides the merchant with a terminal "
             "and processes their card payments."),
            ("Issuer", "The bank that issues the credit or debit card to the consumer and "
             "bears the credit or fraud risk."),
            ("Network / Scheme", "Visa, Mastercard, RuPay, UnionPay — the organisation that "
             "sets rules, routes messages, and manages settlement."),
            ("BIN", "Bank Identification Number — the first 6–8 digits of a card number "
             "that identify the Issuer and card programme."),
            ("ISO 8583", "The binary messaging standard for card authorization, clearing, "
             "and settlement — dominant since 1987."),
            ("ISO 20022", "The XML/JSON-based messaging standard gradually replacing ISO "
             "8583 for richer data and interoperability."),
            ("Interchange", "The fee paid by the Acquirer to the Issuer on every card "
             "transaction — the economic engine of the card industry."),
            ("MDR", "Merchant Discount Rate — the total fee the merchant pays to accept "
             "card payments (interchange + scheme fees + acquirer margin)."),
            ("EMV", "Europay, Mastercard, Visa — the global standard for chip-based card "
             "authentication using cryptographic Application Cryptograms."),
            ("ARQC", "Application Request Cryptogram — the one-time cryptographic proof "
             "generated by an EMV chip to prove physical card presence."),
            ("HSM", "Hardware Security Module — tamper-resistant hardware for managing "
             "cryptographic keys, PIN validation, and EMV cryptogram verification."),
            ("3DS2 / 3-D Secure 2", "The authentication protocol for online (card-not-"
             "present) transactions. Adds risk-based authentication with frictionless "
             "and challenge flows."),
            ("SCA", "Strong Customer Authentication — EU PSD2 requirement for two-factor "
             "authentication on electronic payments."),
            ("Tokenisation", "Replacing a real card number (PAN) with a surrogate value "
             "(token) for security. Types: device tokens (Apple Pay), Card-on-File tokens, "
             "acquirer tokens."),
            ("PAN", "Primary Account Number — the 16-digit (typically) card number."),
            ("DAN", "Device Account Number — a network token provisioned to a specific "
             "device (e.g., iPhone Secure Enclave) for mobile payments."),
            ("STIP", "Stand-In Processing — when the network or switch approves a "
             "transaction on behalf of a downed Issuer using cached data and rules."),
            ("Chargeback", "The dispute mechanism where a cardholder challenges a "
             "transaction and the Issuer reverses the funds from the merchant."),
            ("Liability shift", "The transfer of fraud liability from the merchant to the "
             "Issuer (or vice versa) based on whether EMV or 3DS authentication was used."),
            ("PCI DSS", "Payment Card Industry Data Security Standard — the 12-requirement "
             "security standard for all entities that store, process, or transmit "
             "cardholder data. Version 4.0 effective March 2025."),
            ("Durbin Amendment", "US regulation (Dodd-Frank 2010) capping debit card "
             "interchange fees for banks with assets above $10 billion."),
            ("IFR", "Interchange Fee Regulation — EU regulation capping consumer debit "
             "interchange at 0.2% and credit at 0.3%."),
            ("MCC", "Merchant Category Code — a 4-digit code classifying the merchant's "
             "business type, used for interchange tiering and expense categorisation."),
            ("Marqeta", "US-based modern card issuing platform with Just-In-Time (JIT) "
             "funding via API. Powers many fintechs."),
            ("M2P Fintech", "India's leading BaaS card issuance platform powering fintechs "
             "and neobanks."),
            ("RuPay", "India's domestic card scheme operated by NPCI. ~900 million cards. "
             "Zero MDR on debit."),
            ("CoF", "Card-on-File — storing card credentials at a merchant for repeat "
             "purchases. Must use network tokens in India."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
