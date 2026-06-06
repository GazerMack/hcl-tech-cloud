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
        one_liner=("When you tap your card at a coffee shop in London and money leaves your "
                   "account in Mumbai milliseconds later, a complex choreography of acquirers, "
                   "switches, networks, and issuers has occurred. Here is how card payments "
                   "actually work under the hood."),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


def _sec0() -> TopicSection:
    body = (
        primer(
            p("Card payments are the most universally accepted, complex, and profitable payment "
              "mechanisms in BFSI. While 'instant payments' like UPI or FedNow are replacing "
              "some card volume, the four-party card model remains the backbone of global "
              "consumer commerce.")
        )
        + H3("0.1  IT-side anchor — a global DNS resolution")
        + it_anchor(
            p("When you type a URL, your browser asks a local resolver, which asks a root server, "
              "which asks a TLD server, which asks the domain's name server to find the exact IP "
              "address. Card payments work similarly. The shop's terminal doesn't know your bank. "
              "It asks the shop's bank (the Acquirer), which asks the Network (Visa/Mastercard), "
              "which routes the message to your specific bank (the Issuer) to get an approval "
              "code.")
        )
        + H3("0.2  BFSI-side anchor — buying a coffee with a tap")
        + bfsi_anchor(
            p("You buy a £3 coffee and tap your Mastercard. The terminal says 'Approved' in "
              "one second. But no money actually moved yet. What happened was a cryptographic "
              "promise: your bank verified your balance, placed a £3 hold, and promised the "
              "shop's bank they will send the money tomorrow. That split between the instant "
              "'authorization' and the overnight 'clearing and settlement' is the fundamental "
              "secret of the card industry.")
        )
    )
    return TopicSection("0.  Primer — anchored to things you already know", "basic", body)


def _sec1() -> TopicSection:
    body = (
        p("Card payments exist to solve the fundamental problem of trust between strangers at "
          "scale. The 'Four-Party Model' (which actually has five or more entities) "
          "provides the rules, the routing, and the economic incentives.")
        + ol([
            "<strong>The Cardholder:</strong> You, the consumer.",
            "<strong>The Merchant:</strong> The coffee shop.",
            "<strong>The Issuer:</strong> Your bank (e.g., Citi, HDFC), who gave you the card and holds your money.",
            "<strong>The Acquirer:</strong> The merchant's bank (e.g., Chase Paymentech, Worldpay), who provides the POS terminal.",
            "<strong>The Network (Scheme):</strong> Visa, Mastercard, RuPay, Discover. They sit in the middle, setting rules and routing messages.",
        ])
        + p("The system exists to guarantee the merchant gets paid, protect the consumer from "
            "fraud, and earn fees for the banks (interchange) and the network (assessments) in "
            "exchange for this seamless global interoperability.")
    )
    return TopicSection("1.  Why card networks exist — the Four-Party Model", "basic", body)


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
            '  M->>A: Auth Request (ISO 8583)\n'
            '  A->>N: Route by BIN\n'
            '  N->>I: Auth Request to Issuer\n'
            '  I-->>I: Check balance, PIN, fraud risk\n'
            '  I->>N: Auth Response (Approved/Declined)\n'
            '  N->>A: Auth Response\n'
            '  A->>M: Terminal displays Approved\n'
            '  M->>C: Hand over coffee',
            "The instant authorization flow (Clearing and Settlement happen later).")
    )
    return TopicSection("2.  The core concept in one picture", "basic", body)


def _sec3() -> TopicSection:
    body = (
        H3("3.1  Phase 1: Authorization (Real-time)")
        + p("This is the sequence diagram above. When you tap, the POS generates an ISO 8583 "
            "0100 message containing your card number (PAN), amount, merchant category code (MCC), "
            "and cryptographic tokens (EMV cryptogram). It flows through the Acquirer and Network "
            "to the Issuer. The Issuer verifies the cryptogram, checks your balance, places a hold "
            "on the funds, and returns an approval code.")
        + H3("3.2  Phase 2: Clearing (Batch, End of Day)")
        + p("At the end of the day, the merchant 'batches out' their terminal. The Acquirer "
            "collects all the approved authorizations and sends a bulk clearing file to the Network. "
            "The Network sorts these by Issuer. This is when the exact fees (Interchange) are "
            "calculated based on the transaction type. No money moves yet; they are just trading "
            "the final receipts.")
        + H3("3.3  Phase 3: Settlement (T+1 or T+2)")
        + p("The Network calculates the net position for every bank. If Bank A owes Bank B $10M, "
            "and Bank B owes Bank A $8M, the Network tells the Central Bank (e.g., the Fed or RBI) "
            "to move a net $2M from Bank A's settlement account to Bank B's settlement account. "
            "Finally, the Acquirer deposits the funds (minus fees) into the merchant's bank account.")
    )
    return TopicSection("3.  How it actually works — auth, clear, settle", "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        H3("4.1  The Networks")
        + table(
            ["Network type", "Examples", "How it works"],
            [
                ["<strong>Four-party (Open Loop)</strong>", "Visa, Mastercard, RuPay (India), Cartes Bancaires (France)",
                 "The network connects independent issuing banks and acquiring banks. They do not issue cards directly."],
                ["<strong>Three-party (Closed Loop)</strong>", "American Express, Discover (mostly)",
                 "The network is ALSO the issuer and the acquirer. Amex issues the card to you and signs up the merchant directly."],
            ]
        )
        + H3("4.2  The Switches")
        + p("A 'Switch' is the software engine that speaks the complex ISO 8583 protocol, routes "
            "messages in milliseconds, and handles cryptography (HSM integration).")
        + table(
            ["Vendor / Product", "Origin", "Use Case"],
            [
                ["<strong>ACI Worldwide (BASE24 / UP)</strong>", "United States", "The legacy king of switching. Runs massive ATM and POS networks globally."],
                ["<strong>FIS (IST/Switch / Connex)</strong>", "United States", "Huge footprint in North America and Europe, powering many tier-1 acquirers."],
                ["<strong>Euronet / RS2 / BPC (SmartVista)</strong>", "Various", "Strong global challengers offering modern, often cloud-capable issuing and acquiring platforms."],
                ["<strong>FSS / In-house</strong>", "India", "Many Indian banks use FSS or build custom UPI/RuPay switches to handle massive volumes."],
            ]
        )
    )
    return TopicSection("4.  Types & variations", "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        H3("5.1  The Economics: Interchange, Assessments, and Discount Rates")
        + ul([
            "<strong>Merchant Discount Rate (MDR):</strong> The total fee the merchant pays (e.g., 2%).",
            "<strong>Interchange:</strong> The largest chunk (e.g., 1.5%), paid <em>by</em> the Acquirer <em>to</em> the Issuer. It funds your credit card rewards.",
            "<strong>Assessments/Scheme Fees:</strong> The small slice (e.g., 0.1%) Visa/Mastercard keep.",
            "<strong>Acquirer Margin:</strong> What the merchant's bank keeps (e.g., 0.4%).",
        ])
        + p("When politicians cap Interchange fees (as in the EU or India for debit), credit card "
            "rewards disappear because the Issuer no longer has the margin to fund them.")
        + H3("5.2  EMV (Chip) and Contactless Cryptography")
        + p("Magnetic stripes were static and easily cloned. EMV (Europay, Mastercard, Visa) chips "
            "are tiny secure computers. When you dip or tap, the terminal gives the chip a random "
            "number. The chip uses a secret key (that never leaves the chip) to encrypt the number, "
            "creating a unique Application Cryptogram (ARQC). The Issuer's HSM verifies this "
            "cryptogram, proving the physical card is present and preventing replay attacks.")
        + H3("5.3  Tokenization (Apple Pay, Google Pay)")
        + p("When you add a card to Apple Pay, Apple requests a 'Token' from the Network (MDES for "
            "Mastercard, VTS for Visa). The Network issues a Device Account Number (DAN) that replaces "
            "your real PAN. The DAN only works on that specific iPhone. If the merchant gets hacked, "
            "the stolen DAN is useless without the iPhone's secure enclave.")
    )
    return TopicSection("5.  Advanced — economics, EMV, and tokenization", "advanced", body)


def _sec6() -> TopicSection:
    body = (
        p("Card payments are heavily regulated due to their systemic importance and consumer impact.")
        + table(
            ["Region", "Key Regulations and Dynamics"],
            [
                ["<strong>India</strong>", "RBI mandates domestic routing for domestic transactions. MDR on RuPay debit and UPI is zero (subsidized). RBI strictly enforces tokenization for saved cards (Card-on-File) and mandates 2FA (OTP) for all online transactions."],
                ["<strong>United States</strong>", "Durbin Amendment (Dodd-Frank) caps debit card interchange fees for large banks. Credit card interchange remains uncapped and high, driving a massive rewards ecosystem."],
                ["<strong>United Kingdom & EU</strong>", "Interchange Fee Regulation (IFR) heavily caps interchange (0.2% debit, 0.3% credit). PSD2 mandates Strong Customer Authentication (SCA) for online payments."],
                ["<strong>Singapore / APAC</strong>", "MAS regulates payment services closely. High penetration of domestic QR schemes (PayNow) competing with cards."],
            ]
        )
    )
    return TopicSection("6.  BFSI / domain regulatory overlay", "advanced", body)


def _sec7() -> TopicSection:
    return TopicSection(
        "7.  Trade-offs and decisions a leader owns", "intermediate",
        table(
            ["Decision", "Trade-offs and considerations"],
            [
                ["<strong>Build vs. Buy an Issuing Switch</strong>", "Buying (ACI, BPC) is faster and compliance-ready. Building in-house allows unique products and API-first architectures (e.g., what modern fintechs do), but requires massive HSM and ISO 8583 expertise."],
                ["<strong>On-Premise vs. Cloud HSMs</strong>", "Physical HSMs (Thales, Safenet) in your data center offer ultimate control but scale poorly. Cloud HSMs (AWS Payment Cryptography) are now PCI-PIN certified and offer auto-scaling, but regulators in some regions still mandate on-prem keys."],
                ["<strong>Active-Active Resiliency</strong>", "Switches must handle thousands of TPS. Doing true active-active across multiple data centers is incredibly hard due to database replication lag. A split-brain scenario can result in double authorizations."],
            ]
        )
    )


def _sec8() -> TopicSection:
    body = (
        example("A $100 Credit Card Purchase in the US",
            p("Merchant charges $100. They pay a 2.5% MDR, receiving $97.50. The Acquirer takes "
              "that $2.50. They pay $2.00 (Interchange) to the Issuer (e.g., Chase) and $0.15 "
              "to Visa (Network). The Acquirer keeps $0.35. Chase uses the $2.00 to pay for "
              "your 1.5% cash-back reward and cover fraud/credit risk.")
        )
        + example("Stand-in Processing (STIP) during an Outage",
            p("If HDFC's core banking system goes down for maintenance, their switch might go into "
              "STIP mode. It uses cached balances or hardcoded limits (e.g., 'approve up to ₹5,000 "
              "even if core is down') to ensure customers aren't stranded. When the core returns, "
              "the switch syncs the authorizations.")
        )
        + example("Cross-border fx markup",
            p("You use a UK Barclays card in Dubai. The merchant's Acquirer sends the transaction in "
              "AED. Visa converts it to GBP using their daily wholesale rate. Barclays receives the "
              "authorization in GBP, adds a 2.99% 'non-sterling transaction fee', and posts that "
              "to your account. The FX spread is highly profitable for the issuer.")
        )
    )
    return TopicSection("8.  Worked examples — numbers and decisions", "intermediate", body)


def _sec9() -> TopicSection:
    body = (
        red_flag(ul([
            "‘We don't need HSMs if we use strong TLS.’ — Completely false. PCI-PIN and network rules legally mandate hardware-level cryptography for PINs and EMV cryptograms.",
            "‘Let's process the auths in the core banking batch.’ — Authorization must happen in under a second. Cores are too slow; this is why standalone Switches exist.",
            "‘We'll just use a JSON REST API instead of ISO 8583.’ — You can use JSON internally, but the second you talk to Visa, Mastercard, or a legacy Acquirer, you must translate to ISO 8583 or ISO 20022.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("Acquirer", "The bank that provides the merchant with a terminal and processes their card payments."),
            ("Issuer", "The bank that issues the credit or debit card to the consumer."),
            ("ISO 8583", "The dominant legacy messaging standard for card authorizations."),
            ("Interchange", "The fee paid by the Acquirer to the Issuer, usually a percentage of the transaction."),
            ("MDR", "Merchant Discount Rate; the total fee the merchant pays to accept the card."),
            ("EMV", "Europay, Mastercard, Visa; the global standard for chip cards and contactless cryptography."),
            ("HSM", "Hardware Security Module; a tamper-resistant physical device used to manage cryptographic keys securely."),
            ("STIP", "Stand-In Processing; when the network or switch approves a transaction on behalf of a downed issuer."),
            ("Tokenization", "Replacing a real card number (PAN) with a surrogate value (token) for Apple Pay, Google Pay, or Card-on-File."),
        ])
    )
    return TopicSection("9.  Red flags + topic glossary", "basic", body)
