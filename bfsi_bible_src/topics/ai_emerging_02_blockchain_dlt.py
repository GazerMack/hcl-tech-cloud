"""AI & Emerging Technology · 02 — Blockchain, DLT, and tokenised assets in BFSI.

Covers permissioned and permissionless DLT, smart contracts, tokenisation of
real-world assets, CBDCs, stablecoins, and the regulatory landscape across
India, US, UK, EU, Singapore, UAE, Hong Kong.
"""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="VIII.2",
        slug="02-blockchain-dlt-tokenised-assets",
        title="Blockchain, DLT, and tokenised assets — from Bitcoin to institutional rails",
        one_liner=(
            "Distributed Ledger Technology (DLT) promised to disrupt banking. A decade "
            "later the disruption is real but looks nothing like the early hype: major "
            "banks are not replacing their core systems with public blockchains, but they "
            "are tokenising money-market funds, settling repo on-chain, issuing digital "
            "bonds, piloting Central Bank Digital Currencies (CBDCs), and building "
            "institutional custody for digital assets. This topic separates the signal "
            "from the noise, maps the technology vendor by vendor, and explains the "
            "regulatory regime region by region."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(),
                  _sec5(), _sec6(), _sec7(), _sec8(), _sec9()],
    )


# ------------------------------------------------------------------ sec 0

def _sec0() -> TopicSection:
    body = (
        primer(
            p("Blockchain and DLT are not the same thing, but the terms are often "
              "used interchangeably. A blockchain is a specific type of Distributed "
              "Ledger that uses cryptographic hashing and a chain of blocks. A "
              "Distributed Ledger is the broader concept: a database shared and "
              "synchronised across multiple nodes without a single central "
              "administrator. In BFSI, the distinction matters because most "
              "institutional implementations use permissioned DLT (not the "
              "permissionless blockchains like Bitcoin or public Ethereum) — and "
              "increasingly, even the permissionless chains are being used via "
              "institutional-grade wrappers.")
        )
        + H3("0.1  IT-side anchor — a shared Google Sheet with an audit trail")
        + it_anchor(
            p("Imagine a Google Sheet shared between ten departments. Everyone can "
              "see every row. Every edit is timestamped and attributed to a user. "
              "Nobody can delete or silently modify a past entry — the version "
              "history is immutable. If Google (the central administrator) disappears, "
              "the sheet is gone. Now imagine the same sheet, but instead of Google "
              "hosting it, every department has a full copy, and a consensus protocol "
              "ensures all copies stay identical. If one department's server goes "
              "down, the other nine still have the data. That is a Distributed Ledger. "
              "A blockchain adds one more feature: every batch of edits (a 'block') "
              "includes a cryptographic fingerprint (hash) of the previous batch, "
              "creating a tamper-evident chain.")
        )
        + H3("0.2  BFSI-side anchor — your bank's reconciliation nightmare")
        + bfsi_anchor(
            p("When Bank A sends ₹10 lakh to Bank B via NEFT, both banks record "
              "the transaction in their own separate ledgers. At the end of the day, "
              "they reconcile: Bank A's outgoing entry must match Bank B's incoming "
              "entry. Multiply this by millions of transactions across hundreds of "
              "counterparties, across payments, securities, derivatives, and trade "
              "finance — and you have the banking industry's single largest "
              "operational cost centre: reconciliation. The fundamental promise of "
              "DLT is that if both banks write to the same shared ledger, there is "
              "nothing to reconcile. The 'golden copy' is the ledger itself. That "
              "promise is why every major bank has a DLT programme.")
        )
        + H3("0.3  The three layers of confusion to clear up immediately")
        + ol([
            "<strong>Cryptocurrency ≠ blockchain technology.</strong> Bitcoin is one "
            "application of blockchain. When a bank says 'we are using blockchain', "
            "they almost never mean Bitcoin. They mean a permissioned DLT for a "
            "specific use case (repo settlement, trade finance, digital bonds).",
            "<strong>Permissioned ≠ permissionless.</strong> Public blockchains "
            "(Bitcoin, Ethereum) let anyone participate. Permissioned DLTs "
            "(R3 Corda, Hyperledger Fabric, Canton, Quorum) restrict participation "
            "to known, vetted entities. Banks almost exclusively use permissioned "
            "DLTs — until recently.",
            "<strong>Tokenisation ≠ cryptocurrency.</strong> Tokenisation means "
            "representing a real-world asset (a bond, a share, a money-market "
            "fund unit, a piece of real estate) as a digital token on a ledger. "
            "The asset is real; the token is just a new way to record ownership "
            "and transfer it. This is the area with the most institutional "
            "traction in 2024–25.",
        ])
    )
    return TopicSection(
        "0.  Primer — anchored to things you already know", "basic", body)


# ------------------------------------------------------------------ sec 1

def _sec1() -> TopicSection:
    body = (
        p("DLT exists in BFSI because the current financial infrastructure has "
          "fundamental limitations that DLT can address — not everywhere, but "
          "in specific high-value use cases:")
        + ol([
            "<strong>Reconciliation cost.</strong> Banks spend an estimated "
            "USD 10–15 billion per year globally on reconciliation. A shared "
            "ledger between counterparties eliminates the need for bilateral "
            "reconciliation.",
            "<strong>Settlement speed.</strong> Securities settlement in most "
            "markets is T+1 (the US moved to T+1 in May 2024). DLT enables "
            "atomic settlement — delivery versus payment (DvP) in the same "
            "transaction, in seconds, not days.",
            "<strong>Fractional ownership.</strong> A traditional bond has a "
            "minimum denomination (e.g., USD 100,000). Tokenisation allows "
            "fractional units (e.g., USD 100), opening bond markets to "
            "retail investors.",
            "<strong>Programmable money and assets.</strong> Smart contracts "
            "can automate coupon payments, dividend distributions, compliance "
            "checks, and corporate actions — removing manual processing.",
            "<strong>Transparency and auditability.</strong> Every transaction "
            "on a DLT is timestamped, attributed, and immutable. This is "
            "valuable for regulatory reporting, trade finance, and "
            "supply-chain financing.",
            "<strong>24/7 markets.</strong> Traditional securities markets "
            "operate during business hours. Tokenised assets on DLT can "
            "trade and settle 24/7, which is already happening with "
            "tokenised money-market funds.",
        ])
        + callout("Why hasn't DLT replaced everything already?", p(
            "Because the existing infrastructure (SWIFT, DTCC, Euroclear, "
            "central banks) works. It is slow, expensive, and reconciliation-"
            "heavy, but it is battle-tested, deeply integrated, and regulated. "
            "DLT adoption in BFSI is incremental — replacing specific "
            "workflows where the cost-benefit is clear, not wholesale "
            "infrastructure replacement."
        ), "info")
    )
    return TopicSection(
        "1.  Why DLT exists in BFSI — first principles", "basic", body)


# ------------------------------------------------------------------ sec 2

def _sec2() -> TopicSection:
    body = (
        mermaid(
            'flowchart TB\n'
            '  subgraph "Layer 1: Base DLT protocol"\n'
            '    PUB["Public chains\u003cbr/\u003eEthereum, Solana, Polygon"]\n'
            '    PERM["Permissioned DLT\u003cbr/\u003eCorda, Fabric, Canton, Besu"]\n'
            '  end\n'
            '  subgraph "Layer 2: Institutional wrappers"\n'
            '    CUST["Institutional custody\u003cbr/\u003eFireblocks, Copper, Anchorage, BitGo"]\n'
            '    COMP["Compliance layer\u003cbr/\u003eChainanalysis, Elliptic, TRM Labs"]\n'
            '    ORCH["Tokenisation platform\u003cbr/\u003eSecuritize, Tokeny, Paxos, Fireblocks"]\n'
            '  end\n'
            '  subgraph "Layer 3: Applications"\n'
            '    TOK["Tokenised RWA\u003cbr/\u003ebonds, funds, repo, real estate"]\n'
            '    CBDC["CBDCs\u003cbr/\u003ee-rupee, mBridge, digital euro"]\n'
            '    STBL["Stablecoins\u003cbr/\u003eUSDC, USDT, PayPal USD, bank coins"]\n'
            '    DEFI["Institutional DeFi\u003cbr/\u003eAave Arc, Compound Treasury"]\n'
            '  end\n'
            '  PUB --> CUST\n'
            '  PERM --> ORCH\n'
            '  CUST --> COMP\n'
            '  COMP --> TOK\n'
            '  ORCH --> TOK\n'
            '  ORCH --> CBDC\n'
            '  CUST --> STBL\n'
            '  COMP --> DEFI',
            "The three-layer architecture of institutional DLT in BFSI: protocol, "
            "wrappers, and applications."
        )
        + p("The key insight: institutional adoption happens at Layer 2 and Layer 3. "
            "Banks rarely interact with raw blockchain protocols. They use "
            "institutional-grade custody, compliance, and tokenisation platforms "
            "that abstract away the underlying DLT complexity — just as you use a "
            "banking app rather than raw TCP/IP.")
    )
    return TopicSection(
        "2.  The core concept in one picture", "basic", body)


# ------------------------------------------------------------------ sec 3

def _sec3() -> TopicSection:
    body = (
        H3("3.1  Phase 1: Choose the ledger — permissioned vs. permissionless")
        + table(
            ["Attribute", "Permissioned DLT", "Public blockchain"],
            [
                ["<strong>Who can participate</strong>",
                 "Only approved, KYC'd institutions",
                 "Anyone with an internet connection"],
                ["<strong>Consensus</strong>",
                 "PBFT, Raft, notary-based (faster, deterministic)",
                 "Proof of Stake, Proof of Work (slower, probabilistic)"],
                ["<strong>Throughput</strong>",
                 "1,000–10,000 TPS (sufficient for most BFSI use cases)",
                 "15–65 TPS (Ethereum L1) to 2,000+ TPS (Solana, L2 rollups)"],
                ["<strong>Privacy</strong>",
                 "Transaction-level privacy between counterparties",
                 "Transparent by default; privacy via ZK-proofs or private layers"],
                ["<strong>Finality</strong>",
                 "Immediate or near-immediate (seconds)",
                 "Probabilistic (minutes for Ethereum; faster on Solana)"],
                ["<strong>Key platforms</strong>",
                 "R3 Corda, Hyperledger Fabric, Canton (Digital Asset), "
                 "Hyperledger Besu (private mode), Quorum (ConsenSys)",
                 "Ethereum (L1 + L2 rollups: Arbitrum, Optimism, Base, zkSync), "
                 "Solana, Polygon PoS/zkEVM, Avalanche"],
                ["<strong>BFSI use</strong>",
                 "Trade finance, repo, interbank settlement, CBDC wholesale",
                 "Tokenised funds (BUIDL), stablecoins, DeFi, retail CBDC"],
            ]
        )
        + p("The trend in 2024–25: the boundary is blurring. BlackRock launched "
            "BUIDL on public Ethereum. JPMorgan's Onyx (previously Quorum) is "
            "exploring public chain interoperability. Singapore MAS Project "
            "Guardian uses public DeFi protocols with institutional wrappers. "
            "The institutional world is moving from 'only permissioned' to "
            "'public chains with institutional controls'.")

        + H3("3.2  Phase 2: Tokenise the asset")
        + p("Tokenisation is the process of creating a digital representation "
            "of a real-world asset on a DLT. The token is not the asset — it is "
            "a record of ownership, rights, and obligations associated with the "
            "asset. The process:")
        + ol([
            "<strong>Legal structuring.</strong> Determine the legal wrapper: "
            "does the token represent direct ownership, a beneficial interest, "
            "or a claim? Depends on jurisdiction.",
            "<strong>Smart contract deployment.</strong> Write and audit the "
            "smart contract that defines the token's rules — transfer "
            "restrictions, compliance checks, dividend/coupon logic, "
            "whitelisting.",
            "<strong>Issuance.</strong> Mint tokens and distribute to investors "
            "via a tokenisation platform (Securitize, Tokeny, Paxos, Broadridge "
            "DLR, HSBC Orion).",
            "<strong>Primary distribution.</strong> Investors subscribe; the "
            "platform performs KYC/AML, suitability checks, and records "
            "ownership on-chain.",
            "<strong>Secondary trading.</strong> Tokens trade on regulated "
            "venues (tZERO, Archax, SIX Digital Exchange, ADDX Singapore) "
            "or bilaterally.",
            "<strong>Lifecycle events.</strong> Coupon payments, dividends, "
            "maturities, corporate actions — executed automatically via smart "
            "contracts or triggered by an oracle.",
        ])

        + H3("3.3  Phase 3: Settlement — atomic DvP")
        + p("The transformative capability of DLT for capital markets is "
            "atomic Delivery versus Payment (DvP): the transfer of the "
            "tokenised security and the transfer of the cash (or stablecoin "
            "or CBDC) happen in a single, indivisible transaction. Either both "
            "legs succeed or neither does. This eliminates settlement risk — "
            "the risk that one party delivers the asset but the other fails "
            "to pay. In today's T+1 world, settlement risk is managed by "
            "CCPs (Central Counterparties) and margin. Atomic DvP could "
            "reduce or eliminate the need for CCPs in some use cases.")

        + H3("3.4  Phase 4: Custody and safekeeping")
        + p("Holding digital assets requires specialised custody — managing "
            "cryptographic private keys that control the assets. This is "
            "fundamentally different from traditional custody (holding "
            "securities at a CSD). The institutional custody landscape:")
        + table(
            ["Custodian / Platform", "Type", "Notable clients and features"],
            [
                ["<strong>Fireblocks</strong>",
                 "Infrastructure-as-a-service (MPC-based key management)",
                 "BNY Mellon, BNP Paribas, ANZ, Standard Chartered, "
                 "Revolut. Multi-party computation (MPC) eliminates "
                 "single-point-of-failure for private keys."],
                ["<strong>Anchorage Digital</strong>",
                 "Federally chartered digital-asset bank (US OCC)",
                 "First federally chartered crypto bank in the US. "
                 "Institutional custody, staking, and governance."],
                ["<strong>Copper.co</strong>",
                 "Institutional custody and prime brokerage",
                 "Barclays, Nomura (via Laser Digital), Standard Chartered "
                 "(via Zodia Custody, a JV with SBI)."],
                ["<strong>BitGo</strong>",
                 "Multi-sig custody and institutional trading",
                 "Acquired by Galaxy Digital 2023 (later terminated). "
                 "Widely used by exchanges and institutions."],
                ["<strong>Zodia Custody</strong>",
                 "Standard Chartered and SBI Digital Asset Holdings JV",
                 "Regulated institutional custody in UK, EU, Singapore, "
                 "Hong Kong, Japan, Australia."],
                ["<strong>Traditional custodians entering</strong>",
                 "BNY Mellon, State Street, Citi, HSBC, "
                 "Deutsche Boerse / Clearstream",
                 "BNY Mellon launched digital-asset custody 2022. "
                 "Citi Token Services live. HSBC Orion for tokenised "
                 "assets. Clearstream D7 digital post-trade."],
            ]
        )
    )
    return TopicSection(
        "3.  How it actually works — ledger, tokenise, settle, custody",
        "intermediate", body)


# ------------------------------------------------------------------ sec 4

def _sec4() -> TopicSection:
    body = (
        H3("4.1  Tokenised Real-World Assets (RWA) — the institutional use case")
        + table(
            ["Asset class", "Status in 2024–25", "Key examples"],
            [
                ["<strong>Money-market funds</strong>",
                 "Live and growing rapidly; USD 2B+ tokenised by mid-2025",
                 "BlackRock BUIDL (Ethereum, USD 500M+ in 9 months), "
                 "Franklin Templeton OnChain US Govt Money Fund (Stellar "
                 "and Polygon), Ondo USDY, Superstate."],
                ["<strong>Repo and securities financing</strong>",
                 "Production at scale; trillions in notional settled",
                 "Broadridge DLR (Distributed Ledger Repo) — settled "
                 "USD 1T+ monthly by 2024. JPMorgan Onyx — intraday repo. "
                 "Goldman Sachs GS DAP."],
                ["<strong>Bonds (digital/tokenised)</strong>",
                 "Growing; sovereign and corporate issuances",
                 "EIB digital bond on Ethereum (EUR 100M, 2021 — first ever). "
                 "Hong Kong HKMA tokenised green bond (HKD 800M, 2023). "
                 "HSBC Orion digital bond (GBP, 2023). SIX Digital Exchange "
                 "bond issuances."],
                ["<strong>Structured products / funds</strong>",
                 "Pilot to early production",
                 "JPMorgan Tokenised Collateral Network. UBS tokenised "
                 "money-market fund on Ethereum (2024). Citi Token Services."],
                ["<strong>Private equity and real estate</strong>",
                 "Early stage; regulatory friction",
                 "Securitize for KKR Health Care Strategic Growth Fund "
                 "(tokenised on Avalanche). RealT (tokenised US real estate). "
                 "ADDX Singapore (private market access)."],
                ["<strong>Trade finance</strong>",
                 "Selective production; after Contour failure",
                 "Contour (trade finance DLT backed by major banks) shut down "
                 "Oct 2023. Marco Polo restructured. we.trade wound down. "
                 "Survivors: Komgo (commodity trade finance on Ethereum/Quorum), "
                 "MonetaGo (fraud prevention), TradeGo."],
            ]
        )

        + H3("4.2  Central Bank Digital Currencies (CBDCs)")
        + table(
            ["CBDC", "Type", "Status (2024–25)"],
            [
                ["<strong>India e₹ (Digital Rupee)</strong>",
                 "Retail (e₹-R) and wholesale (e₹-W)",
                 "Retail pilot live since Dec 2022 via 8 banks (SBI, ICICI, "
                 "HDFC, Yes, IDFC First, Kotak, BoB, Union). 5M+ users by "
                 "2024. Wholesale pilot for G-Sec settlement with 15 banks."],
                ["<strong>Digital euro</strong>",
                 "Retail",
                 "ECB preparation phase from Nov 2023. Design phase complete. "
                 "Legislation pending. Earliest launch 2027–28."],
                ["<strong>Digital pound ('Britcoin')</strong>",
                 "Retail",
                 "Bank of England design phase since Feb 2023. Technology "
                 "partner selection ongoing. Earliest launch 2028+."],
                ["<strong>China e-CNY</strong>",
                 "Retail",
                 "Most advanced globally. Integrated into WeChat Pay, "
                 "Alipay. 180B+ yuan in cumulative transactions by 2024."],
                ["<strong>mBridge</strong>",
                 "Wholesale cross-border (BIS, HKMA, BoT, PBOC, CBUAE, "
                 "SAR Bank)",
                 "Minimum Viable Product reached June 2024. Real-value "
                 "cross-border settlements between central banks. "
                 "Potential SWIFT alternative for participating countries."],
                ["<strong>Project Agorá</strong>",
                 "Wholesale (BIS + 7 central banks)",
                 "Launched 2024 — exploring tokenised wholesale CBDC for "
                 "cross-border payments. Fed, BoE, BoJ, ECB, SNB, "
                 "BoK, Banxico."],
                ["<strong>US — no CBDC plan</strong>",
                 "Neither retail nor wholesale",
                 "Executive Order (Jan 2025) explicitly bars Fed CBDC "
                 "issuance. FedNow (instant payments) is the US answer. "
                 "Political opposition to 'surveillance coin'."],
            ]
        )

        + H3("4.3  Stablecoins — the bridge between crypto and TradFi")
        + table(
            ["Stablecoin", "Issuer", "Backing", "AUM / circulation"],
            [
                ["<strong>USDT (Tether)</strong>", "Tether Limited",
                 "US Treasuries, cash, commercial paper (controversial "
                 "reserve composition)",
                 "USD 115B+ (largest by market cap, dominant in Asia/emerging "
                 "markets)"],
                ["<strong>USDC</strong>", "Circle",
                 "US Treasuries and cash at regulated banks",
                 "USD 35B+ (preferred by institutions for transparency; "
                 "Circle has full reserve attestation by Deloitte)"],
                ["<strong>PayPal USD (PYUSD)</strong>", "PayPal (Paxos-issued)",
                 "US Treasuries and cash",
                 "USD 500M+ (growing; PayPal's 430M user base gives "
                 "distribution advantage)"],
                ["<strong>JPM Coin (now JPM CRN — Coin Routing Network)</strong>",
                 "JPMorgan",
                 "JPM deposit-backed",
                 "Used for intraday repo and cross-border corporate payments "
                 "on Onyx. Not publicly traded."],
                ["<strong>HSBC, DBS, Citi, SocGen stablecoins/tokens</strong>",
                 "Various banks",
                 "Bank deposit-backed",
                 "Pilot/production for institutional use cases (intraday "
                 "liquidity, tokenised DvP cash leg)."],
            ]
        )
        + p("Stablecoins matter for BFSI because they solve the 'cash leg' "
            "problem: you cannot do atomic DvP with a tokenised bond if the "
            "cash side is still on a traditional bank payment rail. A stablecoin "
            "(or CBDC) on the same ledger enables true same-ledger settlement.")

        + H3("4.4  The DLT platform landscape for BFSI")
        + table(
            ["Platform", "Type", "BFSI positioning"],
            [
                ["<strong>R3 Corda</strong>",
                 "Permissioned",
                 "Designed for financial services. Point-to-point privacy "
                 "(only counterparties see their transactions). Used by "
                 "SWIFT, DTCC, SBI, HSBC, Bank of Thailand. Corda 5 "
                 "release 2023."],
                ["<strong>Canton (Digital Asset / DAML)</strong>",
                 "Permissioned (with interoperability)",
                 "DAML smart contract language is ledger-agnostic. Canton "
                 "Network (2023) connects multiple DAML-based ledgers. "
                 "Used by Goldman Sachs GS DAP, Deutsche Boerse D7, ASX "
                 "(replaced CHESS replacement — project cancelled 2022 "
                 "but DAML continues elsewhere)."],
                ["<strong>Hyperledger Fabric</strong>",
                 "Permissioned",
                 "Linux Foundation. Channel-based privacy. Used by "
                 "Walmart (supply chain), Trade Finance (Komgo, Marco "
                 "Polo heritage), several central banks for CBDC "
                 "experiments."],
                ["<strong>Hyperledger Besu</strong>",
                 "Permissioned or public (Ethereum-compatible)",
                 "Enterprise Ethereum client. Used by ConsenSys, "
                 "Palmera, some CBDC pilots. EVM-compatible — can "
                 "bridge to public Ethereum."],
                ["<strong>Quorum (ConsenSys)</strong>",
                 "Permissioned (Ethereum fork)",
                 "Originally built by JPMorgan. Now maintained by "
                 "ConsenSys. JPM Onyx runs on Quorum heritage. "
                 "Privacy via private transactions."],
                ["<strong>Public Ethereum (L1 + L2)</strong>",
                 "Permissionless",
                 "BlackRock BUIDL, UBS tokenised fund, EIB bonds, "
                 "Securitize, Tokeny. L2 rollups (Base, Arbitrum, "
                 "Optimism, zkSync) for lower gas costs."],
                ["<strong>Solana</strong>",
                 "Permissionless",
                 "High throughput (2,000+ TPS). Visa settled USDC on "
                 "Solana (2023 pilot). Growing institutional interest."],
            ]
        )
    )
    return TopicSection(
        "4.  Types and variations — RWA, CBDCs, stablecoins, platforms",
        "intermediate", body)


# ------------------------------------------------------------------ sec 5

def _sec5() -> TopicSection:
    body = (
        H3("5.1  Smart contracts — programmable finance")
        + p("A smart contract is code deployed on a DLT that executes "
            "automatically when predefined conditions are met. In BFSI, "
            "smart contracts automate:")
        + ul([
            "<strong>Coupon payments.</strong> A tokenised bond's smart "
            "contract automatically calculates and distributes coupon payments "
            "to token holders on the scheduled date — no paying agent needed.",
            "<strong>Transfer restrictions.</strong> The smart contract "
            "enforces that tokens can only be transferred to whitelisted "
            "addresses (KYC'd investors), preventing transfer to non-"
            "compliant parties.",
            "<strong>Collateral management.</strong> JPMorgan's Tokenised "
            "Collateral Network moves collateral between counterparties "
            "intraday, triggered by margin calls — settlement in minutes "
            "instead of hours.",
            "<strong>Dividend distribution.</strong> Proportional distribution "
            "to all token holders based on a snapshot of the on-chain "
            "cap table.",
            "<strong>Compliance checks.</strong> Pre-trade checks embedded "
            "in the token contract — investor accreditation status, "
            "jurisdictional restrictions, holding-period locks.",
        ])
        + p("The primary risk of smart contracts: they are immutable once "
            "deployed (or upgradeable only via specific proxy patterns). A "
            "bug in a smart contract can result in loss of funds with no "
            "recourse. This is why smart contract auditing (by firms like "
            "Trail of Bits, OpenZeppelin, Consensys Diligence, CertiK) is "
            "critical for institutional deployments.")

        + H3("5.2  Interoperability — the multi-chain problem")
        + p("The biggest technical challenge in institutional DLT is "
            "interoperability: assets tokenised on one chain need to be "
            "transferable, tradeable, or settled against assets on another "
            "chain. Solutions:")
        + ul([
            "<strong>Bridge protocols</strong> — transfer assets between "
            "chains (e.g., Wormhole, LayerZero, Axelar). High risk — "
            "bridge hacks have been the largest DeFi losses "
            "(Ronin: USD 625M, Wormhole: USD 320M).",
            "<strong>CCIP (Chainlink Cross-Chain Interoperability "
            "Protocol)</strong> — institutional-grade cross-chain messaging "
            "with rate limiting and risk management. Adopted by SWIFT "
            "for its blockchain experiments.",
            "<strong>Canton Network</strong> — DAML-based interoperability "
            "layer connecting permissioned ledgers. Goldman, Deutsche "
            "Boerse, others participating.",
            "<strong>IBC (Inter-Blockchain Communication)</strong> — "
            "Cosmos ecosystem standard. Used by some DeFi protocols.",
            "<strong>SWIFT experiments</strong> — SWIFT is testing "
            "blockchain interoperability using CCIP, Corda, and Solana "
            "in partnership with Chainlink and multiple banks.",
        ])

        + H3("5.3  Privacy on public chains — zero-knowledge proofs")
        + p("Public blockchains are transparent — everyone can see every "
            "transaction. This is unacceptable for institutional finance "
            "(counterparty exposure, trading strategy, client data). "
            "Zero-Knowledge Proofs (ZKPs) solve this: they allow one party "
            "to prove a statement is true without revealing the underlying "
            "data. Types used in BFSI:")
        + ul([
            "<strong>zk-SNARKs / zk-STARKs</strong> — used in zkRollups "
            "(zkSync, Polygon zkEVM, Starknet) for scaling and in privacy "
            "protocols (Aztec, Railgun).",
            "<strong>Institutional privacy layers</strong> — Nightfall "
            "(EY/Ernst & Young, open-sourced) for private transactions on "
            "Ethereum. EY uses it for enterprise supply chain.",
            "<strong>Confidential tokens</strong> — R3 Corda and Canton "
            "provide transaction-level privacy natively; public chains "
            "need ZKPs to achieve equivalent privacy.",
        ])

        + H3("5.4  Oracles — connecting blockchains to the real world")
        + p("Smart contracts cannot natively access external data (market "
            "prices, interest rates, weather events for parametric insurance). "
            "Oracles are services that feed real-world data into smart "
            "contracts. Chainlink is the dominant oracle network, providing "
            "price feeds, proof of reserves, and CCIP. For BFSI, oracle "
            "reliability is critical: a faulty price feed can trigger "
            "incorrect margin calls or liquidations.")

        + H3("5.5  Decentralised Finance (DeFi) — the institutional version")
        + p("DeFi is finance built on smart contracts — lending, borrowing, "
            "trading, derivatives — without traditional intermediaries. "
            "Institutional DeFi adds KYC/AML, compliance, and regulated "
            "wrappers:")
        + table(
            ["Protocol", "Use case", "Institutional adoption"],
            [
                ["<strong>Aave Arc</strong>",
                 "Permissioned lending pool (KYC'd participants only)",
                 "Fireblocks integration. Limited adoption so far — "
                 "regulatory clarity still evolving."],
                ["<strong>MakerDAO / Sky</strong>",
                 "Decentralised stablecoin (DAI) and RWA vaults",
                 "USD 2B+ in tokenised US Treasuries as collateral "
                 "backing DAI. Significant institutional RWA exposure."],
                ["<strong>Centrifuge</strong>",
                 "Real-world asset financing on-chain",
                 "Tokenised trade receivables, real estate, structured "
                 "credit. Integrated with MakerDAO."],
                ["<strong>Ondo Finance</strong>",
                 "Tokenised US Treasuries and structured products",
                 "USDY (yield-bearing stablecoin), OUSG (tokenised "
                 "short-term US Treasuries). Growing institutional use."],
            ]
        )
    )
    return TopicSection(
        "5.  Advanced — smart contracts, interoperability, ZKPs, oracles, DeFi",
        "advanced", body)


# ------------------------------------------------------------------ sec 6

def _sec6() -> TopicSection:
    body = (
        p("DLT and digital-asset regulation is evolving rapidly. No two "
          "jurisdictions have the same framework, but convergence is "
          "emerging around consumer protection, AML, and market integrity.")
        + table(
            ["Region", "Key regulations and frameworks"],
            [
                ["<strong>European Union</strong>",
                 "<strong>MiCA (Markets in Crypto-Assets Regulation)</strong> — "
                 "in force 30 Dec 2024. Comprehensive framework covering: "
                 "stablecoin issuance (reserve requirements, EUR/USD thresholds), "
                 "crypto-asset service provider (CASP) licensing, market abuse "
                 "rules, consumer protection. ARTs (Asset-Referenced Tokens) and "
                 "EMTs (E-Money Tokens) have specific capital and reserve "
                 "requirements. First comprehensive crypto regulation globally. "
                 "<strong>DLT Pilot Regime</strong> — EU sandbox for trading and "
                 "settlement of tokenised securities on DLT (live since Mar 2023). "
                 "<strong>DORA</strong> — applies to CASPs from Jan 2025. "
                 "Transfer of Funds Regulation (TFR) — 'travel rule' for crypto "
                 "transfers."],
                ["<strong>United Kingdom</strong>",
                 "<strong>FCA</strong> regulates crypto-asset promotions (from Oct "
                 "2023) and AML registration for crypto firms. <strong>UK Digital "
                 "Securities Sandbox (DSS)</strong> — operational from 2024; "
                 "allows testing of tokenised securities issuance and settlement. "
                 "Stablecoin regulation under the Financial Services and Markets "
                 "Act 2023 (FSMA 2023). Property (Digital Assets etc.) Bill "
                 "recognises digital assets as personal property (2024). "
                 "Full UK regulatory framework for crypto expected 2025–26."],
                ["<strong>United States</strong>",
                 "Fragmented. <strong>SEC</strong> treats most crypto tokens as "
                 "securities (Howey Test). <strong>CFTC</strong> regulates crypto "
                 "commodities (Bitcoin, Ethereum). <strong>Executive Order (Jan "
                 "2025)</strong> supports responsible digital-asset development "
                 "but bans Fed CBDC. FIT21 (Financial Innovation and Technology "
                 "for the 21st Century Act) — passed House 2024, creates a "
                 "framework for crypto commodity vs. security classification. "
                 "State-level: New York BitLicense, Wyoming SPDI (Special "
                 "Purpose Depository Institution). OCC allows national banks "
                 "to custody crypto (2020 interpretive letters)."],
                ["<strong>Singapore</strong>",
                 "<strong>MAS Payment Services Act (PSA) 2019, amended 2023</strong> "
                 "— licensing for Digital Payment Token (DPT) service providers. "
                 "Stablecoin framework (Aug 2023) — SG-dollar-denominated "
                 "stablecoins regulated by MAS. <strong>Project Guardian</strong> "
                 "— MAS-led industry pilot for institutional tokenisation and "
                 "DeFi (with DBS, JPMorgan, SBI, Standard Chartered). "
                 "<strong>Project Ubin+</strong> — wholesale CBDC for cross-"
                 "border settlement."],
                ["<strong>India</strong>",
                 "<strong>No comprehensive crypto law</strong> as of 2025. "
                 "Crypto gains taxed at 30% flat + 1% TDS (Tax Deducted at "
                 "Source) on transfers (Finance Act 2022). RBI has been "
                 "consistently sceptical of private crypto. <strong>e₹ "
                 "(Digital Rupee)</strong> pilot ongoing. SEBI proposed "
                 "multi-regulator framework for crypto in 2024 (RBI for "
                 "stablecoins, SEBI for crypto securities, IRDAI for "
                 "crypto insurance). India's G20 presidency pushed for "
                 "global crypto regulatory coordination via FSB/IMF "
                 "Synthesis Paper (Sep 2023)."],
                ["<strong>UAE</strong>",
                 "<strong>VARA (Virtual Assets Regulatory Authority)</strong> — "
                 "Dubai's comprehensive crypto regulator since 2023. "
                 "<strong>ADGM FSRA</strong> — Abu Dhabi's framework for "
                 "digital assets. UAE is positioning as a crypto-friendly "
                 "hub; Binance, OKX, Bybit, Crypto.com licensed in Dubai. "
                 "Central Bank of UAE exploring wholesale CBDC (Project "
                 "mBridge participant)."],
                ["<strong>Hong Kong</strong>",
                 "<strong>SFC</strong> licensing regime for Virtual Asset "
                 "Trading Platforms (VATPs) since Jun 2023. Spot Bitcoin "
                 "and Ethereum ETFs approved Apr 2024. HKMA exploring "
                 "tokenised deposits (Project Ensemble). Hong Kong "
                 "positioning as a regulated crypto hub for Asia."],
            ]
        )
        + H3("6.1  AML and the travel rule for crypto")
        + p("FATF's 'travel rule' (Recommendation 16) requires Virtual Asset "
            "Service Providers (VASPs) to share originator and beneficiary "
            "information for crypto transfers, just like banks do for wire "
            "transfers. Compliance tools: Notabene, Chainalysis, TRM Labs, "
            "Elliptic, Sygna Bridge. EU TFR makes this mandatory from "
            "Dec 2024. MiCA CASPs must comply. This is a significant "
            "operational burden for crypto firms and an opportunity for "
            "RegTech vendors.")
    )
    return TopicSection(
        "6.  BFSI / domain regulatory overlay", "advanced", body)


# ------------------------------------------------------------------ sec 7

def _sec7() -> TopicSection:
    body = (
        table(
            ["Decision", "Option A", "Option B", "Key trade-off"],
            [
                ["<strong>Permissioned vs. public chain</strong>",
                 "R3 Corda or Canton for bilateral/consortium use cases",
                 "Public Ethereum (L2) with institutional wrappers (Fireblocks, "
                 "Securitize)",
                 "Permissioned gives privacy and control but limits network effects. "
                 "Public gives liquidity and composability but requires privacy "
                 "solutions and regulatory comfort."],
                ["<strong>Build vs. buy tokenisation platform</strong>",
                 "Build in-house on Corda/Fabric/Ethereum (JPMorgan Onyx model)",
                 "Buy from Securitize, Tokeny, Paxos, or use Broadridge DLR",
                 "Build gives IP control and customisation but requires 50+ "
                 "engineers with DLT expertise. Buy is faster but creates "
                 "platform dependency."],
                ["<strong>Custody: in-house vs. third-party vs. sub-custody</strong>",
                 "Build in-house key management (requires HSMs, MPC, "
                 "operational rigour)",
                 "Use Fireblocks, Copper, or Zodia as third-party custodian",
                 "In-house preserves control but key management errors are "
                 "catastrophic and irreversible (lost keys = lost assets). "
                 "Third-party adds counterparty risk but provides insurance "
                 "and operational maturity."],
                ["<strong>Stablecoin strategy: use existing vs. issue own</strong>",
                 "Use USDC, PYUSD, or partner bank's stablecoin for DvP",
                 "Issue own bank-deposit-backed token (JPM Coin model)",
                 "Using existing stablecoins is faster but introduces dependency "
                 "on Circle/Paxos. Own token is controlled but requires "
                 "e-money or banking license and reserve management."],
                ["<strong>CBDC participation: early mover vs. wait</strong>",
                 "Join CBDC pilot programmes (e₹, digital euro, mBridge)",
                 "Wait for production launch and learn from others",
                 "Early movers shape the design and earn regulator goodwill. "
                 "Late movers avoid pilot costs and learn from failures. "
                 "Most tier-1 banks are choosing early participation."],
                ["<strong>DeFi engagement: ignore vs. institutional DeFi</strong>",
                 "Avoid DeFi entirely (regulatory uncertainty)",
                 "Participate via permissioned pools (Aave Arc, Compound "
                 "Treasury, MAS Project Guardian)",
                 "Ignoring DeFi risks missing yield and innovation. Participating "
                 "risks regulatory backlash if frameworks tighten. Permissioned "
                 "DeFi is the emerging middle ground."],
            ]
        )
    )
    return TopicSection(
        "7.  Trade-offs and decisions a leader owns", "intermediate", body)


# ------------------------------------------------------------------ sec 8

def _sec8() -> TopicSection:
    body = (
        example(
            "BlackRock BUIDL — tokenised money-market fund on Ethereum",
            p("In March 2024, BlackRock launched BUIDL (BlackRock USD "
              "Institutional Digital Liquidity Fund) on public Ethereum via "
              "Securitize as the tokenisation and transfer agent. BUIDL invests "
              "in US Treasuries and repo, paying daily accrued yield directly "
              "to token holders' wallets. Within 9 months, BUIDL crossed "
              "USD 500M in AUM. Key architectural decisions: (1) Ethereum "
              "mainnet for maximum composability and transparency, (2) "
              "Securitize handles KYC/AML and whitelisting — only approved "
              "investors can hold BUIDL tokens, (3) USDC redemption pathway "
              "via Circle for 24/7 instant liquidity, (4) tokens are ERC-20 "
              "with transfer restrictions enforced at the smart contract "
              "level. Significance: the world's largest asset manager chose "
              "a public permissionless chain, validating the 'public chain "
              "with institutional wrappers' thesis.")
        )
        + example(
            "Broadridge DLR — repo settlement at trillions in notional",
            p("Broadridge's Distributed Ledger Repo (DLR) platform settles "
              "US Treasury repo transactions on a permissioned DLT (based on "
              "Canton/DAML). By 2024, DLR was settling over USD 1 trillion "
              "per month in notional. Participants include JPMorgan, Goldman "
              "Sachs, Societe Generale, and others. The platform enables "
              "intraday repo (borrow in the morning, return by evening) with "
              "atomic DvP, reducing settlement risk and capital charges. "
              "The key innovation: tokenised US Treasuries and tokenised "
              "cash on the same ledger, eliminating the need for a separate "
              "cash settlement system.")
        )
        + example(
            "HSBC Orion — tokenised bonds and gold",
            p("HSBC launched Orion, its in-house tokenisation platform, in "
              "2022. By 2024, HSBC had issued tokenised gold (representing "
              "physical gold held in HSBC's London vault) and facilitated "
              "digital bond issuances. HSBC also used Orion for a GBP-"
              "denominated digital bond — the first tokenised sterling bond "
              "by a global bank. Orion runs on permissioned infrastructure "
              "and integrates with HSBC's existing custody and settlement "
              "systems. Significance: a Tier-1 global bank building "
              "tokenisation into its core infrastructure, not as a separate "
              "fintech experiment.")
        )
        + example(
            "RBI e₹ wholesale pilot — G-Sec settlement",
            p("The Reserve Bank of India's wholesale CBDC pilot (e₹-W) "
              "enables settlement of government securities (G-Sec) "
              "transactions using tokenised central bank money. Fifteen "
              "banks participate, including SBI, HDFC Bank, ICICI Bank, "
              "and Kotak Mahindra Bank. The pilot demonstrated same-day "
              "settlement of G-Sec trades using e₹-W for the cash leg — "
              "effectively T+0 settlement for government bonds. Key "
              "learning: the technology works, but liquidity management "
              "is complex — banks must hold e₹-W reserves separately from "
              "their regular RBI balances, creating an additional "
              "liquidity-management challenge.")
        )
        + example(
            "ASX CHESS replacement failure — the cautionary tale",
            p("The Australian Securities Exchange (ASX) embarked on the "
              "most ambitious DLT project in capital markets: replacing "
              "its CHESS clearing and settlement system with a DAML-based "
              "(Digital Asset) platform. The project started in 2017 and "
              "was abandoned in November 2022 after a write-off of "
              "AUD 250M+. Root causes: (1) scope creep — the project tried "
              "to replace a working system entirely rather than augmenting "
              "it, (2) technology immaturity at the time, (3) insufficient "
              "industry testing, (4) governance failures. Lesson: DLT "
              "succeeds when it targets specific, high-value use cases "
              "(repo, tokenised funds). It fails when positioned as a "
              "wholesale replacement for battle-tested infrastructure.")
        )
    )
    return TopicSection(
        "8.  Worked examples — numbers and decisions", "intermediate", body)


# ------------------------------------------------------------------ sec 9

def _sec9() -> TopicSection:
    body = (
        H3("9.1  Questions a leader asks in any review")
        + ol([
            "What specific use case are we targeting with DLT, and what is the "
            "cost-benefit vs. the current process?",
            "Are we using a permissioned or public chain, and what is the "
            "regulatory posture of our jurisdiction for each?",
            "Who is our custody provider for digital assets, and what is our "
            "key-management architecture (MPC, multi-sig, HSM)?",
            "How does the tokenised asset interact with our existing post-trade "
            "infrastructure (CSD, SWIFT, reconciliation)?",
            "What is our stablecoin / CBDC strategy for the cash leg of "
            "tokenised settlements?",
            "Have we completed smart contract audits, and what is our "
            "upgrade/patch process for deployed contracts?",
            "How are we complying with MiCA (EU), FCA crypto rules (UK), "
            "SEC/CFTC guidance (US), MAS PSA (Singapore), or RBI norms (India)?",
            "What is our AML/travel-rule compliance solution for crypto "
            "transfers?",
            "How are we managing interoperability risk — are we locked into "
            "one chain, or do we have a multi-chain strategy?",
            "What is our CBDC participation roadmap — are we in any pilot "
            "programmes, and what have we learned?",
            "How does our DLT strategy connect to our broader capital-markets "
            "and payments modernisation roadmap?",
            "What is the talent plan — do we have smart-contract developers, "
            "DLT architects, and crypto-compliance specialists?",
        ])
        + H3("9.2  Red flags")
        + red_flag(ul([
            "'We need a blockchain strategy.' — You need a business problem "
            "that DLT solves better than existing technology. Blockchain is "
            "a solution, not a strategy. Start with the use case.",
            "'We'll build on a private blockchain so we don't need to worry "
            "about regulation.' — Permissioned DLT is still regulated. "
            "Tokenised securities are securities regardless of the ledger. "
            "MiFID II, SEC rules, and MAS SFA apply.",
            "'Smart contracts are self-executing so we don't need legal "
            "agreements.' — Smart contracts execute code. Legal enforceability "
            "requires legal documentation. The smart contract implements "
            "the legal agreement, it does not replace it.",
            "'DLT will replace SWIFT and DTCC.' — Not in this decade. SWIFT "
            "processes 45M+ messages daily across 11,000+ institutions. "
            "DTCC settles USD 2.4 quadrillion/year. DLT will complement and "
            "gradually modernise parts of this infrastructure, not replace it.",
            "'We can custody our own crypto — just store the keys.' — "
            "Institutional key management is a specialised discipline. Lost "
            "keys mean lost assets with no recourse. QuadrigaCX (CAD 190M "
            "lost when founder died with sole key access) is the cautionary "
            "tale. Use institutional-grade MPC custody.",
            "'Stablecoins are all the same.' — USDT's reserve transparency "
            "is fundamentally different from USDC's regulated reserves. "
            "Algorithmic stablecoins (TerraUSD/LUNA, collapsed May 2022, "
            "USD 40B wiped out) are a different category entirely. Due "
            "diligence on reserves is non-negotiable.",
            "'The ASX tried DLT and failed, so DLT doesn't work.' — ASX "
            "tried to replace an entire national settlement system with "
            "immature technology. BlackRock BUIDL and Broadridge DLR "
            "succeeded by targeting specific, high-value use cases. "
            "The lesson is about scope, not technology.",
            "'Our compliance team can handle crypto.' — Crypto compliance "
            "requires specialised skills: blockchain analytics (Chainalysis, "
            "Elliptic), travel-rule implementation, token classification "
            "(security vs. utility vs. e-money), and cross-border "
            "regulatory mapping. General AML/KYC teams are not equipped.",
            "'DeFi is too risky for banks.' — Unregulated DeFi is. "
            "Institutional DeFi with KYC'd pools (Aave Arc, MAS Project "
            "Guardian) is a regulated experiment backed by central banks "
            "and tier-1 institutions. Blanket dismissal is outdated.",
            "'CBDCs are surveillance coins.' — This is a political argument, "
            "not a technical one. Wholesale CBDCs (mBridge, Project Agorá) "
            "are interbank instruments with no consumer surveillance "
            "dimension. Retail CBDCs vary — design choices (privacy "
            "features, transaction limits) determine the answer.",
        ]))
        + H3("Glossary for this topic")
        + kv([
            ("DLT", "Distributed Ledger Technology — a database shared and "
             "synchronised across multiple nodes without a central administrator."),
            ("Blockchain", "A specific type of DLT where transactions are grouped "
             "into blocks, each cryptographically linked to the previous one."),
            ("Smart contract", "Self-executing code deployed on a DLT that "
             "runs automatically when predefined conditions are met."),
            ("Tokenisation", "Creating a digital representation of a real-world "
             "asset (bond, fund unit, real estate) as a token on a DLT."),
            ("RWA", "Real-World Assets — the umbrella term for tokenised "
             "traditional financial assets (bonds, equities, funds, real estate)."),
            ("CBDC", "Central Bank Digital Currency — digital money issued "
             "directly by a central bank."),
            ("Stablecoin", "A crypto token pegged to a fiat currency (usually "
             "USD), backed by reserves of fiat, Treasuries, or other assets."),
            ("DvP", "Delivery versus Payment — simultaneous exchange of "
             "securities and cash, eliminating settlement risk."),
            ("Atomic settlement", "Settlement where both legs (asset and cash) "
             "succeed or fail together in a single indivisible transaction."),
            ("MPC", "Multi-Party Computation — a cryptographic technique where "
             "multiple parties jointly compute a function (e.g., sign a "
             "transaction) without any party knowing the full private key."),
            ("ZKP", "Zero-Knowledge Proof — a cryptographic method allowing "
             "one party to prove a statement is true without revealing the "
             "underlying data."),
            ("MiCA", "Markets in Crypto-Assets Regulation — the EU's "
             "comprehensive regulatory framework for crypto assets (in force "
             "Dec 2024)."),
            ("CASP", "Crypto-Asset Service Provider — the MiCA term for "
             "regulated crypto firms (exchanges, custodians, brokers)."),
            ("Travel rule", "FATF Recommendation 16 requiring VASPs to share "
             "originator/beneficiary information for crypto transfers."),
            ("VASP", "Virtual Asset Service Provider — FATF's term for any "
             "entity providing crypto exchange, transfer, custody, or "
             "advisory services."),
            ("Oracle", "A service that feeds external real-world data (prices, "
             "events) into smart contracts on a DLT."),
            ("L1 / L2", "Layer 1 (base blockchain protocol, e.g., Ethereum "
             "mainnet) / Layer 2 (scaling solution built on top, e.g., "
             "Arbitrum, Optimism, zkSync)."),
            ("ERC-20", "The Ethereum token standard for fungible tokens. "
             "Most tokenised assets and stablecoins use ERC-20."),
            ("DeFi", "Decentralised Finance — financial services (lending, "
             "trading, derivatives) built on smart contracts without "
             "traditional intermediaries."),
            ("BUIDL", "BlackRock USD Institutional Digital Liquidity Fund — "
             "the first tokenised money-market fund by the world's largest "
             "asset manager, launched on Ethereum in March 2024."),
        ])
    )
    return TopicSection(
        "9.  Questions, red flags, and glossary", "basic", body)
