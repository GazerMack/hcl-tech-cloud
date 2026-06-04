"""Foundations · I.1 v2 — deep rewrite, slow build-up, 12th-standard friendly.

This is the May 2026 deep rewrite of I.1. v1 (foundations_01_transactions.py)
remains on disk for archive/reference but is no longer imported by generate.py.

Sections shipped so far in this rewrite:
  0. Primer (dual-anchor + five questions + where-it-sits)
  1. Why a transaction system exists at all — first principles
  2. The core concept in one picture
  3. How it actually works — phase by phase
  4. Types & variations
  5. Advanced — the mechanisms underneath
  6. Domain overlay — what changes because BFSI is regulated
  7. Trade-offs and decisions a leader owns
  8. Worked examples — numbers and decisions
  9. Questions a leader asks in any review
 10. Red flags + topic glossary
"""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, term, TopicPage, TopicSection,
)


# =============================================================== build entry

def build() -> TopicPage:
    s: list[TopicSection] = [
        _sec0(),
        _sec1(),
        _sec2(),
        _sec3(),
        _sec4(),
        _sec5(),
        _sec6(),
        _sec7(),
        _sec8(),
        _sec9(),
        _sec10(),
    ]
    return TopicPage(
        code="I.1",
        slug="01-transactions",
        title="How a digital banking transaction actually flows",
        one_liner=(
            "Before we touch a single piece of jargon, we are going to do two ordinary things you "
            "have done a hundred times — press a key on a laptop, and tap UPI to pay a tea-seller "
            "— and watch each one in slow motion. By the end of Section 1 you should be able to "
            "stop a senior banker mid-sentence, ask 'which of the four promises of a ledger is at "
            "risk here?', and have them agree it was the right question. <em>This topic is being "
            "deep-rewritten two sections at a time; you are now looking at the full topic "
            "(Sections 0–10).</em>"
        ),
        sections=s,
    )


# =============================================================== Section 0

def _sec0() -> TopicSection:
    body = (
        _wip_banner()
        + p("Before any acronym, any diagram, any vendor name — we are going to anchor this entire "
            "topic in two things you already know in your bones. One from the gadget on your desk. "
            "One from the bank account on your phone. We will spend the next few pages doing "
            "nothing but watching these two ordinary actions in slow motion, because every "
            "concept we meet later in this bible — APIs, microservices, ledgers, ISO 20022, "
            "Kubernetes, encryption, regulators — is just a grown-up version of something you "
            "will see in this primer.")

        # ----------------------------------------------------- 0.1 IT anchor
        + H3("0.1  IT-side anchor — what happens when you press the letter ‘A’ on your laptop")
        + p("Pick up the laptop in front of you. Press the key marked <strong>A</strong>. The "
            "letter ‘A’ appears on screen, in your Word document, in maybe 50 milliseconds. Feels "
            "instant. It is not. Between your finger and that pixel turning white, an entire "
            "miniature factory ran. Let us walk it, in plain English, with no jargon for now.")
        + ol([
            "<strong>Your finger pushes the key down by about 2 millimetres.</strong> Underneath "
            "the key is a tiny rubber dome or a metal switch. It collapses and closes an "
            "electrical circuit — two metal plates touch.",
            "<strong>That closed circuit is one of 80-odd circuits</strong> the keyboard chip is "
            "scanning, hundreds of times a second. It notices ‘circuit number 30 is now closed’ "
            "and produces a number — let us call it <em>scancode 30</em>.",
            "<strong>That number travels down a thin ribbon cable</strong> into the main board of "
            "the laptop, into a small dedicated chip called the keyboard controller, which "
            "translates it again and hands it to the laptop’s main brain.",
            "<strong>The main brain (the CPU — Central Processing Unit)</strong> is busy doing a "
            "hundred other things — playing music, refreshing the clock, downloading email — but "
            "it agrees to be interrupted, briefly, to deal with this keystroke. This polite "
            "interruption has a name: an <em>interrupt</em>.",
            "<strong>The operating system (Windows, macOS or Linux) wakes up</strong>, looks at "
            "which window is currently in focus on your screen — Word, in this case — and hands "
            "the keystroke to that program.",
            "<strong>Word looks at the scancode</strong>, decides ‘the user wants the letter A in "
            "the document’, inserts it into the document’s memory, then asks the graphics card to "
            "redraw a small rectangle of the screen with the new letter visible.",
            "<strong>The graphics card paints that rectangle</strong> by changing the colour of a "
            "few thousand pixels, sixty times a second — so fast that to your eye, the ‘A’ just "
            "appears.",
        ])
        + it_anchor(
            p("Seven separate actors — your finger, the rubber dome, the keyboard chip, the "
              "ribbon cable, the CPU, the operating system, the graphics card — each did one tiny "
              "job and then handed the work to the next one. None of them did the whole thing. "
              "None of them knew the others personally. Each one trusted that the previous step "
              "had been done correctly. Each one was prepared, in principle, for the previous "
              "step to have failed and would either retry or show you an error.")
            + p("<strong>Hold on to this image.</strong> A bank transaction is exactly the same "
               "story, just with seven different actors — your phone, the merchant’s app, the "
               "payment network, two banks, a regulator, and a settlement system. Each does one "
               "tiny job. None of them does the whole thing. None of them fully trusts the "
               "others. Each one is prepared for the previous step to have failed.")
        )
        + mermaid(
            "flowchart LR\n"
            "  F[Your finger] -->|press| K[Rubber dome closes circuit]\n"
            "  K -->|scancode 30| KC[Keyboard chip]\n"
            "  KC -->|ribbon cable| CPU[CPU brain]\n"
            "  CPU -->|interrupt| OS[Operating system Windows]\n"
            "  OS -->|deliver keystroke| APP[Word document]\n"
            "  APP -->|insert letter A| MEM[Document in memory]\n"
            "  MEM -->|redraw rectangle| GPU[Graphics card]\n"
            "  GPU -->|paint pixels| SCR[Screen shows A]\n",
            "Figure 0.1 — Seven actors, one keystroke. Each step hands off to the next; none does the whole job."
        )
        + p("Now hold on to one more idea before we leave your laptop. The CPU brain was doing "
            "many things in parallel — music, email, clock — and politely paused to handle your "
            "key. That politeness is what makes the laptop feel responsive. If the CPU refused to "
            "be interrupted, your music would stutter or your typing would lag. The whole point "
            "of an operating system is to share the brain fairly between many jobs.")
        + analogy(
            p("A modern bank server is like that CPU brain, but with millions of customers all "
              "pressing keys at once. Some are tapping UPI. Some are logging into net banking. "
              "Some are buying mutual funds. Some are an automated job paying out salaries. The "
              "server has to be polite to every one of them, share itself fairly, and never lose "
              "anyone’s work — even when one of them yanks the cable out.")
        )

        # ----------------------------------------------------- 0.2 BFSI anchor
        + H3("0.2  BFSI-side anchor — you tap UPI to pay the chaiwala ₹100")
        + p("Now leave the laptop. You are at a tea stall outside the office. The chaiwala has a "
            "small printed paper QR (Quick Response) code stuck on the front of his cart. You "
            "open PhonePe / Google Pay / Paytm on your phone, scan the QR, the screen already "
            "shows ‘Ramesh Tea Stall’, you type <strong>100</strong>, press <em>Pay</em>, enter "
            "your 4-digit UPI PIN (Personal Identification Number), and within roughly two "
            "seconds your phone says <strong>Payment successful</strong> and the chaiwala’s "
            "phone makes a small beep that says ‘₹100 received from Priya Sharma’.")
        + p("Two seconds. One beep. From your point of view, nothing has happened — you have "
            "given the chaiwala nothing physical. From the chaiwala’s point of view, nothing has "
            "happened either — he has not seen any money. And yet both of you walk away happy. "
            "<strong>Why?</strong> Because somewhere in the country, a database row in your "
            "bank decreased by 100 and a database row in the chaiwala’s bank increased by 100, "
            "and both of you trust the system enough to treat those two number changes as if "
            "they were a hundred-rupee note physically passing between your hands.")
        + p("Let us walk what actually happened, again in plain English, no jargon yet.")
        + ol([
            "<strong>Your phone’s camera reads the QR code.</strong> The QR is not magic; it is "
            "just a black-and-white pattern that encodes a short piece of text. In this case the "
            "text is roughly: ‘pay-to-ID = ramesh@okhdfcbank, name = Ramesh Tea Stall’.",
            "<strong>The UPI app on your phone builds a small message.</strong> Something like: "
            "‘Priya (priya@oksbi) wants to send ₹100 to Ramesh (ramesh@okhdfcbank)’. The app "
            "asks you for your 4-digit UPI PIN to prove that the person holding the phone is "
            "really you and not someone who picked up your phone.",
            "<strong>That message is sent over the mobile internet</strong> to a national switch "
            "called NPCI (National Payments Corporation of India). Think of NPCI as a giant "
            "telephone exchange that knows every Indian bank.",
            "<strong>NPCI looks at the ‘to’ address</strong>, sees ‘okhdfcbank’, and calls HDFC "
            "Bank. It also calls your bank, SBI (State Bank of India), the ‘from’ address.",
            "<strong>SBI checks three things, very fast.</strong> Is this really Priya’s account? "
            "Is the PIN correct? Does she have at least ₹100 in her account? If yes to all three, "
            "SBI says ‘OK, I will reduce Priya’s balance by ₹100 and hold the money for HDFC’.",
            "<strong>NPCI tells HDFC Bank</strong> ‘there is ₹100 incoming for Ramesh from SBI; "
            "please credit his account’. HDFC adds ₹100 to Ramesh’s balance.",
            "<strong>NPCI tells both phones</strong> ‘done’. Your screen flips to ‘Payment "
            "successful’. The chaiwala’s phone beeps. You walk away with tea. He walks away with "
            "a row in a database that says he is ₹100 richer.",
            "<strong>Later that night, behind the scenes</strong>, NPCI tots up everything that "
            "moved between SBI and HDFC across the whole day — millions of small payments in "
            "both directions — and the two banks settle the net difference by moving real money "
            "in their accounts at the Reserve Bank of India (RBI). You and the chaiwala never "
            "see this step. It is called <em>settlement</em> and we will come back to it.",
        ])
        + bfsi_anchor(
            p("Seven separate actors again — your phone, your bank (SBI), NPCI, the chaiwala’s "
              "bank (HDFC), the chaiwala’s phone, the RBI, and the laws of India that say these "
              "rows in databases are legally binding. Each one did one tiny job. None of them did "
              "the whole thing. None of them trusts the others without proof. Each one is "
              "prepared for the previous step to have failed.")
            + p("If you go back and read the laptop story in section 0.1, you will see it is the "
               "<strong>same shape</strong>. That is not a coincidence. <em>Every</em> digital "
               "system that has to be reliable looks like this: many small actors, each doing "
               "one small job, each handing off carefully, each prepared for the others to "
               "misbehave. The art of BFSI tech is learning what those small jobs are and what "
               "can go wrong at each handoff.")
        )
        + mermaid(
            "sequenceDiagram\n"
            "  autonumber\n"
            "  participant U as Your phone\n"
            "  participant S as Your bank SBI\n"
            "  participant N as NPCI switch\n"
            "  participant H as Chaiwala bank HDFC\n"
            "  participant C as Chaiwala phone\n"
            "  U->>N: Pay 100 from priya@oksbi to ramesh@okhdfcbank, PIN attached\n"
            "  N->>S: Debit 100 from Priya, here is her PIN-proof\n"
            "  S-->>N: OK, debited and held\n"
            "  N->>H: Credit 100 to Ramesh\n"
            "  H-->>N: OK, credited\n"
            "  N-->>U: Payment successful\n"
            "  N-->>C: Received 100 from Priya Sharma\n"
            "  Note over S,H: Hours later, NPCI nets all SBI-HDFC flows and the two banks settle at RBI\n",
            "Figure 0.2 — A ₹100 UPI payment in slow motion. Seven actors, two seconds of clock time."
        )
        + p("Two things to notice before we move on. <strong>First</strong>, nobody in this story "
            "actually moved any money during those two seconds. SBI just wrote ‘Priya: -100’ in "
            "its own database and HDFC wrote ‘Ramesh: +100’ in its own database. The real money "
            "moved between SBI and HDFC much later, in bulk, at the central bank. <strong>"
            "Second</strong>, every single arrow in that diagram is a place where things can go "
            "wrong — the phone can lose signal, NPCI can be busy, SBI can crash, HDFC can be "
            "slow, the regulator can change a rule. The reason a senior BFSI architect earns "
            "what they earn is that they have learnt, arrow by arrow, what can go wrong and how "
            "to make sure nobody loses ₹100 when it does.")

        # ----------------------------------------------------- 0.3 five questions
        + H3("0.3  The five questions every banking transaction must answer")
        + p("Before we go any further, let us collect, in plain English, the five questions that "
            "every banking transaction — UPI in India, Faster Payments in the United Kingdom, "
            "FedNow in the United States, SEPA Instant in the Eurozone, FAST in Singapore — has "
            "to answer correctly, every single time, with no exceptions. Once you have these "
            "five in your head, the rest of this bible will keep coming back to them.")
        + table(
            ["#", "Question (plain English)", "What it means in one sentence", "The grown-up word for it"],
            [
                ["1", "Is this really you?",
                 "We have to be sure the person tapping pay is the person who owns the account, not someone who picked up the phone.",
                 "<strong>Authentication</strong>"],
                ["2", "Are you actually allowed to do this right now?",
                 "Even if it is you, are you within your daily limit, not blocked by fraud rules, not on a sanctions list, with enough balance, and is the receiver allowed to receive?",
                 "<strong>Authorisation</strong>"],
                ["3", "Did the whole thing happen, or none of it?",
                 "Either ₹100 leaves your account AND ₹100 lands in his account, or neither happens. There is no ‘half-paid’ in a working bank.",
                 "<strong>Atomicity</strong>"],
                ["4", "Once we say ‘done’, is it really done forever?",
                 "Neither bank can quietly reverse it later. The chaiwala can spend his ₹100 tomorrow without checking again.",
                 "<strong>Finality</strong>"],
                ["5", "Can we prove all of this five years from now?",
                 "If a regulator, an auditor, or a court asks, we can show exactly what happened, who approved it, when, from which phone, with which PIN.",
                 "<strong>Auditability</strong>"],
            ])
        + callout("Hold these five questions",
            p("Every protocol, every database, every encryption library, every regulator rule, "
              "every middleware product you will ever meet in BFSI was built to answer one or "
              "more of these five questions. When you read about Kubernetes (IV.2), it is mostly "
              "helping with question 3 (the whole thing, or none). When you read about TLS "
              "(V.1), it is mostly questions 1 and 2. ISO 20022 message formats (II.1) carry the "
              "evidence for question 5. Cloud regions and DORA (V.1) are about making sure 3 and "
              "4 still hold when a data centre catches fire. <strong>Memorise these five.</strong> "
              "They are the lens for the entire bible."), "info")

        # ----------------------------------------------------- 0.4 where it sits
        + H3("0.4  Where this topic sits in the rest of the bible")
        + p("This topic — I.1 — is the spine of everything that comes after. Once you understand "
            "what a transaction is and what guarantees it must keep, every other topic in the "
            "bible becomes ‘how this layer of the stack helps the transaction keep one of its "
            "five promises’. Here is the map.")
        + table(
            ["Part", "What it teaches", "Which of the five questions it mainly serves"],
            [
                ["I — Foundations",
                 "The mental model: transactions, the seven layers, cloud vs on-prem.",
                 "All five — this is the lens."],
                ["II — Application Stack",
                 "How banking software is actually built: APIs, microservices, message formats.",
                 "Mainly Q3 (atomicity) and Q5 (auditability)."],
                ["III — Data",
                 "Where the ledger physically lives: OLTP databases, data warehouses, streaming.",
                 "Q3 (atomicity), Q4 (finality), Q5 (auditability)."],
                ["IV — Infrastructure & Operations",
                 "Where the software runs: cloud, Kubernetes, observability, FinOps, SRE.",
                 "Q3 and Q4 — keeping the system alive while transactions are in flight."],
                ["V — Security, Risk & Compliance",
                 "Who is allowed to do what, how we prove it, how regulators check.",
                 "Q1 (authentication), Q2 (authorisation), Q5 (auditability)."],
                ["VI — BFSI Domain Platforms",
                 "The vendor estate that actually runs banks: Finacle, T24, Mambu, Volante, etc.",
                 "All five — these are the products that operationalise the model."],
                ["VII — Leadership Lenses",
                 "How a senior techno-functional leader decides, debates, and delivers all this.",
                 "Meta — how to choose the right answer to each of the five questions."],
            ])
        + p("If you ever feel lost later in the bible — and you will, the field is enormous — "
            "come back to this section, look at the five questions, and ask: <em>which of the "
            "five is this thing trying to protect?</em> That single question will give you 80% "
            "of the intuition a senior architect uses every day.")
    )
    return TopicSection(
        "0.  Primer — anchored to things you already know",
        "basic", body)


# =============================================================== Section 1

def _sec1() -> TopicSection:
    body = (
        primer(
            p("In Section 0 we watched a UPI payment in slow motion. In Section 1 we are going "
              "to ask a deeper question: <strong>why does the word ‘transaction’ even exist?</strong> "
              "Why did mathematicians, monks, merchants, central bankers, and finally computer "
              "scientists, all converge on this single word and build entire careers around it? "
              "We are going to start in 14th-century Florence with a leather-bound book and "
              "finish in 21st-century data centres with a global standard called ACID — and you "
              "will see that the modern standard is literally the same four promises the Florentine "
              "monks made, written in a new language.")
        )

        # ----------------------------------------------------- 1.1 history
        + H3("1.1  Before computers — the bank as a leather-bound book")
        + p("Forget servers, screens, internet. The year is 1340. You are a wool merchant in "
            "Florence. You have just sold 200 bolts of cloth in Bruges and you do not want to "
            "carry 5,000 gold florins back across the Alps where bandits are waiting. You walk "
            "into the Florence branch of the <strong>Medici</strong> bank. The clerk pulls out "
            "a heavy leather-bound book — the <em>libro mastro</em>, the master book — and "
            "writes two lines in it.")
        + table(
            ["Line in the Medici master book", "What it says"],
            [
                ["Line 1 — debit",
                 "‘Branch Bruges owes Florence 5,000 florins, received from Signore Datini, 14 March 1340.’"],
                ["Line 2 — credit",
                 "‘Signore Datini may withdraw 5,000 florins from Florence branch, anytime, 14 March 1340.’"],
            ])
        + p("That is it. Two lines in a book. No gold moved. The merchant walked out of Bruges, "
            "crossed the Alps with nothing but a slip of paper in his pocket — what we would now "
            "call a <em>cheque</em> — and walked into the Florence branch a month later, where "
            "they read their copy of the book, matched the slip, and handed him 5,000 florins. "
            "The Medici bank had just invented something we now take so completely for granted "
            "that we cannot see it: <strong>money as an entry in a ledger</strong> rather than "
            "money as a physical object.")
        + p("The Florentines (and a generation later, a Franciscan monk called Luca Pacioli, who "
            "wrote it all down in 1494) figured out four things that make this work. These four "
            "things are not historical curiosities; they are <strong>the same four things every "
            "modern bank still has to do</strong>, and every database engine your bank runs is "
            "an implementation of them.")

        # ----------------------------------------------------- 1.2 four promises
        + H3("1.2  The four promises any ledger — paper or digital — must keep")
        + p("Pacioli’s 1494 book was called <em>Summa de Arithmetica</em>. In one chapter, he "
            "wrote down the rules of <strong>double-entry bookkeeping</strong>: every "
            "transaction has two sides (a debit and a credit), they must balance, and the book "
            "must keep four promises. Translated into plain English:")
        + table(
            ["Promise", "What it says, in plain English", "What breaks if you don’t keep it"],
            [
                ["<strong>All or nothing</strong>",
                 "If I write the debit but not the credit (or vice versa), the books no longer "
                 "balance. So either both lines are in the book, or neither is. There is no "
                 "‘halfway’ ever.",
                 "Money would appear or vanish from thin air. The bank would go bust within a week."],
                ["<strong>The book always makes sense</strong>",
                 "The total of all debits must always equal the total of all credits, in every "
                 "branch, on every date. If they don’t, you stop and find the mistake before you "
                 "do anything else.",
                 "You would not be able to trust the numbers to make any decision (lend, pay tax, "
                 "calculate profit). The bank would not know if it was solvent."],
                ["<strong>Two clerks can’t step on each other</strong>",
                 "If two clerks are writing in the book at the same time, you cannot have one "
                 "clerk seeing the book half-updated by the other and acting on that half-truth.",
                 "Two clerks could each tell two different customers ‘you have ₹1,000 available’ "
                 "based on the same balance — and the customer who spends second would discover "
                 "the bank is short."],
                ["<strong>Ink does not fade</strong>",
                 "Once an entry is in the book, it stays there. Fire, flood, mouse, rebellion — "
                 "the book survives, or at least there is a copy in another branch.",
                 "A merchant could walk in with a cheque the bank no longer remembers issuing. "
                 "Trust collapses. Nobody banks with you."],
            ])
        + p("These four promises are so important that 500 years later, when computer scientists "
            "in the 1970s and 1980s built the first commercial databases, they gave each promise "
            "a one-word name, took the first letter of each, and called the set <strong>ACID</strong>: "
            "<em>Atomicity, Consistency, Isolation, Durability</em>. We will build up to ACID "
            "letter by letter at the end of this section. For now just notice that every word in "
            "ACID maps directly to one of Pacioli’s 500-year-old promises.")
        + analogy(
            p("The bank ledger is like the scoresheet in a cricket match. The score has to be "
              "‘all-or-nothing’ (you cannot record a four without recording it for the batter "
              "AND for the total). It has to ‘make sense’ (runs scored must equal runs conceded "
              "across the innings). Two scorers writing at once must not contradict each other. "
              "And the scoresheet must survive — if it is lost, the match is in dispute. The "
              "rules of cricket scoring and the rules of banking ledgers are not similar by "
              "accident. They are both attempts to keep a shared truth between many people who "
              "do not fully trust each other.")
        )

        # ----------------------------------------------------- 1.3 failure stories
        + H3("1.3  What happens when each promise breaks — three real-world disasters")
        + p("Theory is forgettable. Disasters are not. Here is one real story for each of the "
            "first three promises. (The fourth — durability — we will come back to under cloud "
            "outages in topic I.3.) These are public, well-documented events; we’ll cite the "
            "regulator filings or major-paper coverage where useful.")
        + example("All-or-nothing broken — Knight Capital, USA, 1 August 2012",
            p("Knight Capital was a large American stock-trading firm. On 1 August 2012, they "
              "deployed new software to their trading engine but accidentally left a piece of "
              "old test code running on one of the eight servers. The result: for 45 minutes, "
              "their system kept sending stock buy orders to the New York Stock Exchange "
              "<em>but never recorded that they had been sent</em>. The ‘send order’ side of "
              "the transaction happened; the ‘record the order’ side did not. So the system, "
              "thinking it had not yet bought, kept buying. Again. And again.")
            + p("In 45 minutes Knight Capital bought roughly <strong>US$7 billion of stock it "
               "did not want</strong>. By the end of the day they had lost <strong>$440 million</strong>. "
               "Within five days the firm was bankrupt and had to be acquired. This was a pure "
               "atomicity failure — one half of the transaction (the send) executed without the "
               "other half (the record).")
        )
        + example("The book stops making sense — TSB Bank, UK, April 2018",
            p("TSB is a UK retail bank. Over the weekend of 21–22 April 2018, they migrated "
              "their core banking system from the old Lloyds platform to a new system called "
              "<em>Proteo4UK</em>, built by their Spanish parent Sabadell. On Monday morning, "
              "1.9 million customers logged in. Some saw other people’s accounts. Some saw "
              "balances that did not match their statements. Some made payments that vanished "
              "and then reappeared. Some saw mortgages they did not have.")
            + p("This was a <em>consistency</em> failure — the book had stopped making sense. "
               "Different parts of the bank’s systems disagreed with each other on what the "
               "truth was. TSB took <strong>nine months</strong> to fully recover, was fined "
               "<strong>£48.65 million</strong> by the Financial Conduct Authority and "
               "Prudential Regulation Authority in 2022, and paid <strong>over £32 million</strong> "
               "in customer compensation. Many customers never trusted them again.")
        )
        + example("Two clerks step on each other — the classic ‘double-spend’",
            p("This one is less about a single famous disaster and more about a class of bug "
              "that has cost banks billions over the decades. Imagine you have exactly ₹1,000 "
              "in your account. At the exact same instant — say, 11:00:00.123 AM — you tap UPI "
              "to send ₹800 to a friend, and your standing instruction for the electricity bill "
              "tries to debit ₹700.")
            + p("If both processes read your balance at the same time, both see ₹1,000, both "
               "decide ‘yes, sufficient funds’, both proceed, and your balance ends up at "
               "<strong>minus ₹500</strong>. This is called a <em>race condition</em>. It is an "
               "isolation failure: two transactions stepped on each other because neither knew "
               "the other was happening. Real-world examples: in 2012 a major Indian bank had "
               "to manually reverse roughly 6,000 such overdrafts after a wallet integration "
               "bug. In 2021 a US neobank had a similar incident during a Black Friday surge.")
        )
        + red_flag(
            p("If a vendor tells you ‘we are going to skip transactions for performance’, you "
              "have just been told that one of these three disasters is in your future. The "
              "right answer is ‘show me, on a whiteboard, how you guarantee atomicity, "
              "consistency, isolation and durability without using the word transaction — and "
              "if you cannot, what is the maximum money I can lose per second when this fails?’")
        )

        # ----------------------------------------------------- 1.4 the word
        + H3("1.4  Why we needed the word ‘transaction’")
        + p("Up to now we have been using the word freely. Let us nail it down. A "
            "<strong>transaction</strong> is the smallest unit of work that the bank promises "
            "to either fully complete or fully undo. <em>Smallest unit</em> is the operative "
            "phrase. The bank does not promise that 100 small transfers will all succeed or all "
            "fail together; it promises that <em>each individual one</em> will be all-or-nothing.")
        + p("Why give it a special name? Because the moment you say ‘this is a transaction’, "
            "you have signed a contract — with the customer, the regulator, the auditor, the "
            "next engineer — that the four ACID promises apply to it. The word is shorthand "
            "for a guarantee. When a banking engineer says ‘wrap that in a transaction’, what "
            "they mean is ‘put the ACID promises around it’. When a regulator audits, the very "
            "first thing they ask is: ‘show me your transaction boundaries.’")
        + callout("Three sizes of ‘transaction’ in everyday banker speak",
            ul([
                "<strong>Business transaction</strong> — what the customer sees. ‘I paid the "
                "chaiwala ₹100.’ One event, in plain English, on the customer’s screen.",
                "<strong>System transaction</strong> — what the bank’s software sees. The same "
                "payment, internally, is often <em>several</em> system transactions: debit my "
                "account, write to the journal, send the message to NPCI, post the credit, "
                "update fraud counters, post the audit log. Each is wrapped in its own ACID box.",
                "<strong>Settlement transaction</strong> — what the central bank sees. Hours "
                "later, ‘SBI net owes HDFC ₹14.6 crore for today’s UPI flows; please move that "
                "between their RBI accounts.’ One big ACID box at the very end.",
            ]),
            "info")
        + p("When you read the rest of this bible, always ask: <em>which size of transaction "
            "is this paragraph talking about?</em> Most confusion in design reviews comes from "
            "two people using the same word at different sizes.")

        # ----------------------------------------------------- 1.5 geographic story
        + H3("1.5  The geographic story — how each major economy went from paper to electronic")
        + p("Every country that runs a modern banking system had to make the same journey: from "
            "Pacioli’s leather-bound book, through carbon-copy paper slips and telegraph wires, "
            "to today’s electronic real-time rails. Knowing this story in five economies gives "
            "you the vocabulary to talk to bankers from any of them. Each row below is one "
            "country’s ‘first electronic transaction system’.")
        + table(
            ["Country", "First electronic system", "Year it went live", "What it did",
             "What runs there today (real-time retail)"],
            [
                ["United States",
                 "<strong>Fedwire</strong> (Federal Reserve Wire Network)",
                 "1918 (telegraph), 1970 (computers)",
                 "Banks moved large amounts of central-bank money to each other electronically.",
                 "<strong>FedNow</strong> (live July 2023) and the private <strong>RTP</strong> rail."],
                ["United Kingdom",
                 "<strong>CHAPS</strong> (Clearing House Automated Payment System)",
                 "9 February 1984",
                 "Same-day high-value transfers between UK banks via the Bank of England.",
                 "<strong>Faster Payments Service (FPS)</strong> — live since 2008, 24×7."],
                ["Eurozone",
                 "<strong>TARGET</strong> (Trans-European Automated Real-time Gross settlement Express Transfer)",
                 "4 January 1999 (alongside euro launch)",
                 "Real-time gross settlement of euro payments between European central banks.",
                 "<strong>TARGET2</strong> (2007) → <strong>T2</strong> (2023), plus <strong>SEPA "
                 "Instant Credit Transfer (SCT Inst)</strong> for retail."],
                ["India",
                 "<strong>RTGS</strong> (Real-Time Gross Settlement)",
                 "26 March 2004",
                 "Real-time same-day high-value transfers between Indian banks via RBI.",
                 "<strong>UPI</strong> (Unified Payments Interface, live April 2016) — now ~14 "
                 "billion transactions/month."],
                ["Singapore",
                 "<strong>MEPS+</strong> (MAS Electronic Payment System)",
                 "20 December 2006 (replacing 1998 MEPS)",
                 "Real-time high-value transfers between Singapore banks via the Monetary "
                 "Authority of Singapore.",
                 "<strong>FAST</strong> (Fast And Secure Transfers, live March 2014) and "
                 "<strong>PayNow</strong> (2017)."],
            ])
        + p("Notice three patterns. <strong>First</strong>, every country started with a "
            "<em>wholesale</em> system (banks paying each other, large amounts, working hours) "
            "and only later added a <em>retail real-time</em> system for ordinary people. "
            "<strong>Second</strong>, the central bank always sits at the centre — Fed, Bank of "
            "England, ECB (European Central Bank), RBI, MAS. <strong>Third</strong>, the "
            "underlying promises (the four ACID ones) are <em>identical</em> across all five "
            "systems. What changes is the speed, the value limits, the operating hours, the "
            "message format, and the regulator. Everything else is the same problem.")
        + callout("Why this matters for an HCLTech BFSI consultant",
            p("A client engagement at Citi in New York, Standard Chartered in Singapore, "
              "Deutsche Bank in Frankfurt, Barclays in London or HDFC in Mumbai will use "
              "different rails, different regulators and different vendors — but the "
              "<em>questions</em> their architects are debating are the same five we listed in "
              "Section 0.3, and the <em>guarantees</em> they are protecting are the same four "
              "Florentine promises. If you have those in your head, you can walk into any of "
              "those rooms and immediately follow the conversation."), "info")

        # ----------------------------------------------------- 1.6 ACID
        + H3("1.6  ACID — Pacioli’s promises in 20th-century clothes")
        + p("Finally we are ready to meet ACID. The acronym was coined in 1983 by Andreas "
            "Reuter and Theo Härder, two German computer scientists. Each letter is one of the "
            "four promises we already know. We will build them up one at a time, with a worked "
            "example for each.")

        + H4("A — Atomicity (‘all or nothing’)")
        + p("A transaction is treated as a single indivisible unit. Either every step inside it "
            "happens, or none of them does. There is no halfway state that the outside world "
            "can ever observe. The word <em>atomic</em> comes from Greek <em>atomos</em>, "
            "meaning ‘cannot be split’.")
        + example("Atomicity in UPI",
            p("Your ₹100 UPI payment contains at least four steps inside SBI’s systems: (1) "
              "verify the PIN, (2) check the balance, (3) reduce your balance by ₹100, (4) "
              "write the row into the outgoing message journal that NPCI will read. Atomicity "
              "says: either all four happen, or none of them does. If the server crashes "
              "between step 3 and step 4 — your balance was reduced but NPCI never heard about "
              "the payment — then on recovery, step 3 must be undone. Otherwise you are ₹100 "
              "poorer and the chaiwala never got the money.")
        )

        + H4("C — Consistency (‘the book always makes sense’)")
        + p("After the transaction finishes, the database is still in a state that obeys all "
            "the bank’s rules. Total debits equal total credits. No account is negative unless "
            "it is allowed to be. No interest rate is above 100%. No customer is both alive and "
            "deceased. The transaction is a function that takes a valid state of the database "
            "and produces another valid state of the database — never an invalid one in between "
            "that anyone can see.")
        + example("Consistency in a cross-border wire",
            p("Citi New York wires US$1 million to Standard Chartered Singapore on behalf of "
              "Acme Corp. Internally there are eight ledger postings: Acme’s account, Citi’s "
              "nostro at JPMorgan, the FX leg if needed, the wire fee, the regulatory "
              "withholding, the GL (General Ledger) account, the suspense account, and the "
              "audit log. Consistency says: at the end of all eight, the sum of every "
              "ledger position must still balance to zero across the bank — debits exactly "
              "equal credits. If they don’t, the transaction is rolled back, even if all eight "
              "individual writes succeeded.")
        )

        + H4("I — Isolation (‘two clerks can’t step on each other’)")
        + p("If many transactions are running at the same time — and at a real bank, millions "
            "are — each one must look as if it is running alone. Transaction A must not be "
            "able to see transaction B half-done. The technical name for ‘as if running alone’ "
            "is <em>serialisable</em>: the final state must be one that could have been "
            "reached by running the transactions one after the other in some order. In "
            "practice, full serialisability is expensive, so databases offer weaker "
            "<em>isolation levels</em> (we will go deep into these in III.1).")
        + example("Isolation in a flash sale",
            p("On the morning a new IPO (Initial Public Offering) opens, 500,000 retail "
              "investors hit ‘buy’ on their broker app at 10:00:00 AM. Each one’s order "
              "reads ‘shares available in IPO pool: 1,000,000’, decides ‘yes, plenty’, and "
              "tries to reserve 50. Without isolation, all 500,000 would each see 1,000,000 "
              "shares available and all 500,000 would succeed — promising 25 million shares "
              "that don’t exist. With isolation, each transaction sees the pool only as it "
              "stood after the previous one finished, and the moment the pool hits zero, the "
              "remaining 499,999 orders are correctly rejected.")
        )

        + H4("D — Durability (‘ink does not fade’)")
        + p("Once the database says ‘the transaction is committed’, it survives anything that "
            "happens next — power cut, server crash, fire, flood. The change is on persistent "
            "storage (disk, or modern flash, or in multiple data centres) before the user "
            "is told ‘done’. This is why a real bank database fsync’s to disk (forces the "
            "write physically to the platter / flash, not just to memory) before "
            "acknowledging — and why databases that skip that step for speed are unsuitable "
            "for the ledger.")
        + example("Durability and the data centre fire",
            p("In March 2021, the OVH cloud provider’s SBG2 data centre in Strasbourg, France, "
              "burned down completely. Some customers had relied on a single region. Their "
              "data — including transactions they had been told were committed — was lost "
              "permanently because durability had been promised on one site only. Banks "
              "regulated under DORA (the EU Digital Operational Resilience Act, in force from "
              "17 January 2025) must now demonstrate that committed transactions survive the "
              "loss of an entire region, not just a single server.")
        )

        + callout("End-of-section recap — what you should now be able to say out loud",
            ul([
                "‘A transaction is the smallest unit of work the bank promises to either "
                "fully complete or fully undo.’",
                "‘Banks have made four promises for 500 years — all-or-nothing, the book "
                "makes sense, two clerks can’t step on each other, ink does not fade. The "
                "modern acronym is ACID.’",
                "‘If a system breaks any of those four, here is a real-world disaster that "
                "happened — Knight Capital (atomicity), TSB (consistency), classic race "
                "conditions (isolation), the OVH fire (durability).’",
                "‘The first electronic transaction system in the US was Fedwire (1918/1970), "
                "in the UK CHAPS (1984), in the Eurozone TARGET (1999), in India RTGS (2004), "
                "in Singapore MEPS+ (2006). Today the real-time retail rails on top are "
                "FedNow, FPS, SEPA Instant, UPI and FAST respectively.’",
            ]),
            "info")
        + p("If you can say those four bullets to a senior banker and not stumble, you have "
            "passed the bar for Sections 0 and 1. Sections 2 and 3 now put the transaction on "
            "a whiteboard and walk every phase of its life. The next batch will move into "
            "Section 4 (rail types and variations) and Section 5 (the deeper mechanisms under "
            "every rail).")
    )
    return TopicSection(
        "1.  Why a transaction system exists at all — first principles",
        "basic", body)


def _sec2() -> TopicSection:
    body = (
        primer(
            p("Sections 0 and 1 gave us the why. Now we need the picture you can keep on a "
              "whiteboard in any client meeting. Every digital payment looks messy because the "
              "names change by country — UPI, FPS, FedNow, SEPA Instant, FAST, SWIFT, cards — "
              "but underneath, the same eight boxes repeat. If you can draw these eight boxes "
              "from memory, you can place almost any BFSI payment conversation correctly.")
        )
        + H3("2.1  The one picture — from customer intent to settled money")
        + mermaid(
            "flowchart LR\n"
            "  A[\"1 Initiate<br/>customer expresses intent\"] --> B[\"2 Authenticate<br/>prove who is acting\"]\n"
            "  B --> C[\"3 Authorise<br/>check permission and risk\"]\n"
            "  C --> D[\"4 Validate<br/>check message and account facts\"]\n"
            "  D --> E[\"5 Route<br/>choose rail and next hop\"]\n"
            "  E --> F[\"6 Clear<br/>record obligation between banks\"]\n"
            "  F --> G[\"7 Settle<br/>move central-bank money\"]\n"
            "  G --> H[\"8 Notify and reconcile<br/>tell parties and match records\"]\n"
            "  C -. fraud, AML, limits .-> X[\"Risk controls\"]\n"
            "  D -. schema, balance, status .-> Y[\"Validation controls\"]\n"
            "  F -. netting, scheme rules .-> Z[\"Clearing house\"]\n"
            "  G -. RTGS or net settlement .-> R[\"Central bank accounts\"]\n",
            "Figure 2.1 — The universal eight-phase skeleton behind digital banking transactions."
        )
        + p("Read the picture slowly. It is not a technology architecture diagram yet. It is a "
            "business-trust diagram. Each box answers one question that must be true before the "
            "next box is safe. If the customer never intended the payment, everything after that "
            "is fraud. If the customer is not authenticated, the bank does not know who is acting. "
            "If authorisation fails, the customer may be real but not allowed to pay this amount "
            "to this person. If validation fails, the bank may be trying to send a message that "
            "the receiving rail cannot understand. If routing fails, the message goes to the "
            "wrong place. If clearing succeeds but settlement fails, the banks know who owes whom "
            "but the money has not actually moved. If notification works but reconciliation fails, "
            "customers may see success while the bank's back office has a break.")
        + analogy(
            p("Think of a restaurant bill. Initiate is you saying ‘I want to pay ₹1,200’. "
              "Authenticate is proving the card or UPI handle is yours. Authorise is the bank "
              "checking whether you have enough balance and no block. Validate is the waiter "
              "checking the bill number, merchant ID and amount are real. Route is choosing "
              "whether the payment goes by UPI, card, cash or wallet. Clear is the restaurant "
              "and your bank agreeing ‘this customer owes this merchant ₹1,200’. Settle is the "
              "actual money reaching the merchant's bank. Notify and reconcile is the receipt, "
              "the merchant statement and the bank ledger all matching later.")
        )
        + H3("2.2  The same picture across five geographies")
        + table(
            ["Phase", "India UPI", "United States FedNow / RTP", "United Kingdom FPS", "Eurozone SEPA Instant", "Singapore FAST / PayNow"],
            [
                ["1 Initiate",
                 "Customer scans VPA or QR and enters amount.",
                 "Customer or business initiates instant payment through bank channel.",
                 "Customer enters sort code, account and amount, often after Confirmation of Payee.",
                 "Customer initiates SCT Inst credit transfer through bank or fintech.",
                 "Customer pays by mobile number, NRIC, UEN or account via PayNow over FAST."],
                ["2 Authenticate",
                 "Device binding plus UPI PIN through NPCI common library.",
                 "Bank authentication, MFA for online banking, tokenised corporate flows.",
                 "Strong Customer Authentication for digital channels, risk-based step-up.",
                 "PSD2 Strong Customer Authentication with exemptions where allowed.",
                 "Bank MFA, device controls, MAS cyber hygiene expectations."],
                ["3 Authorise",
                 "Balance, UPI limit, MCC, fraud, cooling-off and bank risk rules.",
                 "Limits, OFAC screening, fraud rules, account status.",
                 "Limits, APP fraud controls, sanctions and fraud scoring.",
                 "Limits, sanctions, AML, fraud and PSD2 controls.",
                 "Limits, sanctions, scam controls and bank risk policy."],
                ["4 Validate",
                 "VPA mapping, account status, message schema and NPCI rules.",
                 "FedNow / RTP message format, account reachability and directory checks.",
                 "Sort code, account, CoP result, FPS message rules.",
                 "IBAN, BIC if needed, ISO 20022 pacs message and reachability.",
                 "Proxy mapping, account status and FAST message validation."],
                ["5 Route",
                 "Payer PSP to NPCI to payer and payee banks.",
                 "Bank to FedNow or RTP operator to receiving bank.",
                 "Sending bank to Pay.UK FPS central infrastructure.",
                 "Bank to TIPS, RT1 or national clearing and settlement mechanism.",
                 "Bank to FAST through Singapore clearing infrastructure."],
                ["6 Clear",
                 "NPCI records interbank obligation.",
                 "FedNow settles gross, RTP uses prefunded joint account model.",
                 "FPS central infrastructure records accepted payment obligations.",
                 "Instant clearing occurs through TIPS, RT1 or national CSM.",
                 "FAST records instant interbank transfer obligation."],
                ["7 Settle",
                 "Net settlement at RBI in cycles for many UPI flows.",
                 "FedNow settles in Federal Reserve accounts, RTP uses prefunded position.",
                 "Net positions settle at Bank of England in cycles.",
                 "Settlement in central-bank money through TARGET services.",
                 "Settlement through MAS-linked banking infrastructure."],
                ["8 Notify and reconcile",
                 "Both apps show success, SMS/push, NPCI and bank MIS files reconcile.",
                 "Status confirmation, customer alerts, Fed reports, bank reconciliation.",
                 "Customer notification, FPS reports, bank back-office reconciliation.",
                 "pacs.002 status, camt reports and ledger reconciliation.",
                 "Instant notification, bank statement and operations reconciliation."],
            ]
        )
        + p("The names are different, but the skeleton does not change. This is why you should "
            "not memorise payments as a list of rail names. Memorise the skeleton first. Then "
            "each rail becomes a particular implementation of the skeleton, with different speed, "
            "limit, settlement model, fraud rules and regulator.")
        + H3("2.3  Where the five promises sit inside the picture")
        + table(
            ["Promise from Section 0.3", "Main boxes that protect it", "Plain-English test"],
            [
                ["Authentication — is this really you?",
                 "2 Authenticate, plus device and channel controls before initiation.",
                 "Could someone who stole the phone, password or API key start this payment?"],
                ["Authorisation — are you allowed?",
                 "3 Authorise, with fraud, limit, sanctions, KYC and account rules.",
                 "Even if it is the real customer, should this exact payment be allowed now?"],
                ["Atomicity — whole thing or none?",
                 "4 Validate through 8 Reconcile, especially ledger posting and message journals.",
                 "Can money leave one place without the matching obligation or credit being recorded?"],
                ["Finality — once done, is it done?",
                 "6 Clear and 7 Settle, shaped heavily by rail rules.",
                 "After success, can either side rely on the result, or can it be unwound?"],
                ["Auditability — can we prove it?",
                 "Every box, but especially 8 Notify and reconcile plus immutable logs.",
                 "Can we reconstruct the payment years later from IDs, logs, messages and ledger entries?"],
            ]
        )
        + H3("2.4  One worked picture — ₹100 UPI at the chai stall")
        + example("Mapping the chaiwala payment to the eight boxes",
            table(
                ["Box", "What happens in the ₹100 UPI example", "Approximate clock time"],
                [
                    ["1 Initiate", "You scan the QR and press Pay for ₹100.", "0–3 seconds of human time"],
                    ["2 Authenticate", "You enter UPI PIN, device and app sign the request.", "300–800 milliseconds"],
                    ["3 Authorise", "Your bank checks balance, limits, fraud score, account status.", "50–300 milliseconds"],
                    ["4 Validate", "NPCI and banks check VPA, bank codes, message format and mandatory fields.", "20–150 milliseconds"],
                    ["5 Route", "NPCI routes to the right payer and payee banks.", "20–100 milliseconds"],
                    ["6 Clear", "NPCI records that payer bank owes payee bank for this successful payment.", "Part of the instant flow"],
                    ["7 Settle", "Later settlement windows move net money between banks at RBI.", "Minutes to hours later"],
                    ["8 Notify and reconcile", "Both apps show success now, banks reconcile MIS files later.", "Instant to end-of-day"],
                ]
            )
        )
        + callout("The non-obvious lesson",
            p("Customers experience all eight boxes as one green tick. Engineers and operations "
              "teams must treat them as eight different failure zones. A payment can fail before "
              "authentication, after debit but before credit, after clearing but before settlement, "
              "or after customer notification but before reconciliation. Each failure point has "
              "a different customer message, accounting treatment, regulatory risk and support "
              "runbook."),
            "info")
    )
    return TopicSection("2.  The core concept in one picture", "basic", body)


def _sec3() -> TopicSection:
    body = (
        primer(
            p("Now we walk the eight boxes slowly, as if we are following one payment through "
              "the building with a clipboard. At each phase, ask four things: what physically "
              "happens, what can go wrong, what control catches it, and what a leader should ask "
              "in a design review.")
        )
        + H3("3.1  Phase 1 — Initiate: turning human intent into a machine instruction")
        + p("A transaction begins as intent. A person or system says: move this amount, from "
            "this source, to this destination, for this reason, now. The important detail is that "
            "intent must be captured as a structured message. A human says ‘pay Ramesh ₹100’. "
            "The machine needs fields: payer identifier, payee identifier, amount, currency, "
            "timestamp, device ID, channel, purpose, merchant category, location, and a unique "
            "request ID.")
        + example("Why the request ID matters",
            p("Suppose your phone loses signal after sending a ₹100 payment. You press Pay again. "
              "Without a unique idempotency key, the bank may see two requests and debit ₹200. "
              "With an idempotency key such as <code>UPI-20260519-PRIYA-000123</code>, the bank "
              "can safely say: ‘I have already processed this exact intent, here is the previous "
              "success response.’ This is the difference between a retry and a duplicate debit."))
        + table(
            ["What can go wrong", "Control", "Leader question"],
            [
                ["Customer taps twice or network retries the request.", "Idempotency key and duplicate detection.", "What is the retry window and where is the idempotency key stored?"],
                ["Amount or beneficiary is changed by malware before submission.", "Transaction signing and clear customer confirmation screen.", "Does the signed payload include amount, payee and currency, or only login identity?"],
                ["Wrong rail chosen at source.", "Payment orchestration rules and beneficiary reachability checks.", "Who owns rail-selection logic and how is it tested at cut-off time?"],
            ]
        )
        + H3("3.2  Phase 2 — Authenticate: proving who or what is acting")
        + p("Authentication answers ‘is this really the actor?’ For a consumer, the actor may be "
            "a person holding a phone. For a corporate payment, it may be two authorised treasury "
            "staff approving a file. For a bank-to-bank API, it may be another system presenting "
            "a certificate. Do not confuse authentication with authorisation. Authentication says "
            "‘this is Priya’. Authorisation says ‘Priya may send ₹100 to Ramesh right now’.")
        + table(
            ["Channel", "Typical authentication", "Concrete example"],
            [
                ["Mobile retail payment", "Device binding, biometric unlock, PIN or passcode, risk step-up.", "UPI PIN for India, banking app MFA in UK / US / Singapore."],
                ["Corporate file upload", "User MFA, maker-checker workflow, digital file signature.", "Treasury uploads salary file, second approver signs before release."],
                ["Open banking API", "OAuth 2.0 token plus client certificate in many regions.", "UK Account Information Service Provider connecting to Barclays APIs."],
                ["Bank-to-bank system", "mTLS, signed messages, network allowlists, Hardware Security Module keys.", "FedLine Direct, SWIFT interfaces, payment-engine to core-banking calls."],
            ]
        )
        + analogy(
            p("Authentication is the bank asking for your passport at the airport entrance. It "
              "does not yet mean you may board any plane. It only proves who you are. Boarding "
              "a specific plane is authorisation, which comes next.")
        )
        + H3("3.3  Phase 3 — Authorise: deciding whether this actor may do this exact thing")
        + p("Authorisation combines business rules, customer limits, fraud signals, sanctions, "
            "account state and product rules. This is where BFSI becomes different from ordinary "
            "e-commerce. A shopping website may ask ‘is the card valid?’ A bank asks a denser "
            "question: is this customer allowed, under law and policy, to move this amount, to "
            "this beneficiary, at this time, from this account, through this channel, from this "
            "device, with this risk score?")
        + example("Authorisation math for a simple UPI payment",
            ol([
                "Priya has ₹10,000 available balance.",
                "Her per-transaction UPI limit is ₹1,00,000, but her bank has set a lower risk limit of ₹25,000 for new beneficiaries.",
                "Ramesh was added as a beneficiary five minutes ago. The bank applies a 24-hour cooling-off cap of ₹5,000.",
                "The payment amount is ₹8,000.",
                "Authentication succeeded, but authorisation fails because ₹8,000 exceeds the temporary ₹5,000 new-beneficiary cap.",
                "The correct customer message is not ‘wrong PIN’. It is ‘limit exceeded for new beneficiary’. The difference matters for support and fraud operations.",
            ])
        )
        + table(
            ["Authorisation check", "Why it exists", "Region-specific flavour"],
            [
                ["Balance and overdraft", "Prevents spending money the account cannot legally spend.", "Universal, with overdraft rules varying by product and country."],
                ["Customer limit", "Caps loss if account is compromised.", "UPI limits in India, FPS bank limits in UK, bank-set instant-payment limits elsewhere."],
                ["Sanctions", "Prevents prohibited persons or entities receiving funds.", "OFAC US, OFSI UK, EU consolidated list, UN lists, MAS targeted sanctions, India MHA lists."],
                ["Fraud score", "Detects scams, mule accounts, unusual device or location.", "UK APP fraud controls, India mule-account monitoring, Singapore anti-scam controls."],
                ["KYC and product status", "Prevents restricted accounts from transacting beyond allowed level.", "Minimum-KYC wallets, frozen accounts, dormant accounts, deceased customer markers."],
            ]
        )
        + H3("3.4  Phase 4 — Validate: checking the instruction is mechanically usable")
        + p("Validation is less glamorous than fraud but just as important. A perfectly genuine, "
            "authorised customer can still send an unusable instruction. The account number may "
            "be too short, the International Bank Account Number (IBAN) checksum may fail, a "
            "required ISO 20022 field may be missing, the beneficiary bank may not be reachable "
            "on that rail, the account may be closed, or the message may exceed the rail's value "
            "limit. Validation catches these before the instruction becomes a downstream break.")
        + example("IBAN checksum in plain English",
            p("An IBAN is not just a long account number. It contains a country code, check digits "
              "and bank/account identifiers. The check digits act like the last digit on a parcel "
              "tracking number: if one earlier digit was mistyped, the maths usually fails. If a "
              "German supplier gives <code>DE89 3704 0044 0532 0130 00</code>, the sending bank "
              "can run the checksum before sending money. A one-digit typo is often caught in "
              "milliseconds, before an expensive investigation begins."))
        + H3("3.5  Phase 5 — Route: choosing the rail and the next hop")
        + p("Routing decides where the payment message goes next. In a simple domestic instant "
            "payment, routing may be obvious. In a global bank, it is a decision engine. The same "
            "business intent — pay a supplier — may be routed through RTGS, ACH, instant payment, "
            "card push payment, SWIFT correspondent banking, an internal book transfer, or a "
            "fintech partner. Routing considers value, urgency, currency, country, cut-off time, "
            "cost, beneficiary reachability, sanctions exposure and customer promise.")
        + table(
            ["Scenario", "Likely route", "Why"],
            [
                ["₹250 merchant payment in India", "UPI", "Low value, instant, QR-native, 24×7."],
                ["USD 5 million same-day corporate payment in New York", "Fedwire or CHIPS", "High value, finality and wholesale settlement required."],
                ["£4,500 UK salary", "FPS or BACS depending timing and employer setup", "FPS for instant, BACS for bulk scheduled payroll economics."],
                ["€80,000 urgent supplier payment", "SEPA Instant if reachable, otherwise SEPA Credit Transfer or TARGET", "Instant if available, wholesale route if value and urgency demand."],
                ["SGD retail proxy payment", "PayNow over FAST", "Proxy addressing and instant domestic settlement."],
                ["USD to AED cross-border supplier payment", "SWIFT gpi correspondent route or multi-rail fintech", "Currency conversion, correspondent reach and compliance screening."],
            ]
        )
        + H3("3.6  Phase 6 — Clear: recording who owes whom")
        + p("Clearing is the most misunderstood phase. Clearing does not necessarily move money. "
            "It records obligations. If SBI sends 10 million UPI payments to HDFC customers and "
            "HDFC sends 9.8 million UPI payments to SBI customers, the clearing system does not "
            "need both banks to move the gross total of every payment one by one. It can calculate "
            "the net obligation. Perhaps SBI owes HDFC ₹42 crore after all inflows and outflows. "
            "That net obligation is what later settlement moves.")
        + analogy(
            p("Imagine five friends eating together all month. Instead of handing cash after every "
              "chai, lunch and cab ride, they record each item in Splitwise. Splitwise is clearing: "
              "it knows who owes whom. The bank transfer you make at month-end is settlement: "
              "actual money moves. Confusing the two is one of the quickest ways to sound junior "
              "in a payments meeting.")
        )
        + H3("3.7  Phase 7 — Settle: moving the real money")
        + p("Settlement is where the final money movement happens, usually in accounts held at "
            "the central bank or in a prefunded settlement account. Two models dominate. Real-Time "
            "Gross Settlement (RTGS) moves each transaction individually and finally. Deferred Net "
            "Settlement (DNS) groups many cleared obligations and moves only the net amounts later. "
            "RTGS reduces credit risk but uses more liquidity. DNS is liquidity-efficient but "
            "creates a time gap where obligations exist before final money movement.")
        + table(
            ["Settlement model", "Physical analogy", "Examples", "Leader trade-off"],
            [
                ["RTGS", "Every courier trip moves the full cash immediately.", "RBI RTGS, Fedwire, CHAPS, TARGET, FedNow in Fed accounts.", "High finality and low credit risk, but more liquidity needed."],
                ["Deferred net settlement", "Friends settle the net amount at the end of the day.", "UPI net cycles, ACH, BACS, many card scheme settlements.", "Efficient for high volume, but creates settlement and reconciliation risk."],
                ["Prefunded instant model", "Participants keep money in a shared safe before payments begin.", "RTP in the US, some instant-payment schemes.", "Fast and low credit risk, but liquidity must be locked in advance."],
            ]
        )
        + H3("3.8  Phase 8 — Notify and reconcile: making every book agree")
        + p("The customer cares about the notification. The bank cares about reconciliation. "
            "Notification is the green tick, SMS, email, merchant beep or API status. Reconciliation "
            "is the back-office proof that the customer channel, payment switch, core ledger, "
            "clearing house, settlement account and general ledger all show the same amount, count "
            "and status. A payment can look successful to a customer and still create a reconciliation "
            "break if one downstream file is missing or late.")
        + example("A reconciliation break with numbers",
            p("A bank's mobile channel records 1,000,000 successful UPI payments worth ₹82 crore "
              "on Monday. The core ledger records 999,998 payments worth ₹81.999 crore. NPCI's MIS "
              "file records 1,000,001 payments worth ₹82.0007 crore. The difference is tiny compared "
              "with total value, but it is not ignorable. Operations must identify the three breaks: "
              "which two channel successes did not post to core, which extra NPCI item appeared, "
              "whether customers were affected, and whether settlement was over- or under-funded. "
              "This is why auditability is a real engineering requirement, not a compliance slogan."))
        + H3("3.9  What failure looks like at each phase")
        + table(
            ["Phase", "Customer-visible symptom", "Operations interpretation", "Likely owner"],
            [
                ["Initiate", "Button spins, duplicate pending payments.", "Retry/idempotency or channel capture problem.", "Channel and API gateway teams."],
                ["Authenticate", "Wrong PIN, OTP failure, biometric retry.", "Identity, device binding or authentication service issue.", "Identity and channel security teams."],
                ["Authorise", "Limit exceeded, blocked beneficiary, suspicious transaction.", "Risk, fraud, sanctions or product-rule decision.", "Risk engine, compliance, product operations."],
                ["Validate", "Invalid account, beneficiary not reachable, malformed message.", "Schema, directory, account status or rail-validation failure.", "Payment engine and master-data teams."],
                ["Route", "Payment unavailable for this bank or rail.", "Reachability, cut-off, rail outage or routing-table issue.", "Payment orchestration and network operations."],
                ["Clear", "Payment accepted but interbank status uncertain.", "Scheme or clearing-house obligation mismatch.", "Scheme operations and settlement operations."],
                ["Settle", "Customer success but bank liquidity or position break.", "Central-bank settlement, prefunding or net-position issue.", "Treasury, settlement and finance operations."],
                ["Notify/reconcile", "Customer says paid, merchant says not received.", "Status propagation, MIS, ledger or reconciliation break.", "Customer ops, reconciliation and technology support."],
            ]
        )
        + callout("End-of-section recap",
            ul([
                "A payment is not one action. It is eight phases that customers experience as one green tick.",
                "Authentication proves the actor. Authorisation decides whether the proven actor may do this exact thing.",
                "Clearing records obligations. Settlement moves actual money. Never use those words as synonyms.",
                "Notification is not reconciliation. A customer green tick is not the same as every ledger, scheme and settlement file agreeing.",
                "Every phase needs its own controls, owner, monitoring and recovery runbook.",
            ]),
            "info")
    )
    return TopicSection("3.  How it actually works — phase by phase", "intermediate", body)


def _sec4() -> TopicSection:
    body = (
        primer(
            p("A payment rail is the combination of rulebook, network, message format, clearing "
              "arrangement, settlement model, operating hours, participant list and dispute process "
              "that lets money move. Do not memorise rails as brand names. First ask: is it instant "
              "or batch, push or pull, domestic or cross-border, gross or net, final or reversible, "
              "low-value or high-value? Once you answer those six questions, the rail name becomes "
              "much easier to remember.")
        )
        + H3("4.1  The six-way classification every leader should use")
        + table(
            ["Question", "Option A", "Option B", "Concrete examples", "Why a leader cares"],
            [
                ["Speed", "Instant or near-real-time", "Batch or deferred", "UPI, FedNow, FPS vs ACH, BACS, NACH", "Determines customer promise and operations staffing."],
                ["Direction", "Push credit transfer", "Pull debit / mandate / card", "UPI P2P, SEPA SCT vs cards, NACH debit, SEPA Direct Debit", "Determines consent, fraud and dispute model."],
                ["Settlement", "Real-time gross", "Deferred net or prefunded", "RTGS, Fedwire, CHAPS vs UPI net cycles, ACH, BACS, RTP prefunding", "Determines liquidity, credit risk and treasury impact."],
                ["Geography", "Domestic", "Cross-border", "FPS domestic vs SWIFT gpi, Visa Direct, Wise multi-rail", "Determines FX, sanctions, correspondent banks and data-transfer rules."],
                ["Value", "Retail low-value", "Wholesale high-value", "UPI merchant QR vs Fedwire treasury payment", "Determines controls, approval levels and failure tolerance."],
                ["Finality", "Hard final", "Reversible / disputable", "RTGS, UPI success vs card chargeback, direct debit indemnity", "Determines customer recourse, fraud losses and accounting treatment."],
            ]
        )
        + analogy(
            p("Think of transport. A bicycle courier, metro train, cargo ship, armoured van and "
              "international air freight all move things. You would never ask ‘which is best?’ "
              "without asking what is being moved, how urgent it is, how valuable it is, whether "
              "it can be returned, and which border it crosses. Payment rails are the same. UPI "
              "is a bicycle courier for small instant domestic value. RTGS is an armoured van. "
              "ACH and BACS are scheduled postal bags. SWIFT is international freight paperwork "
              "with several handlers.")
        )
        + H3("4.2  India — a dense rail ecosystem around NPCI and RBI")
        + p("India is the best place to learn modern retail payments because almost every rail "
            "type exists at national scale. The Reserve Bank of India (RBI) runs the high-value "
            "settlement backbone. National Payments Corporation of India (NPCI) runs many mass "
            "retail rails. Banks, Payment Service Providers (PSPs), merchants and fintechs sit "
            "around those shared utilities.")
        + table(
            ["Rail", "What it is in plain English", "Speed and value", "Settlement", "Where you see it"],
            [
                ["<strong>UPI</strong> (Unified Payments Interface)", "Instant account-to-account push payment using a Virtual Payment Address, QR or mobile number.", "Usually 2–5 seconds, 24×7; standard limit often ₹1 lakh, higher for some categories.", "Interbank obligations cleared by NPCI and settled in RBI cycles.", "QR at shops, P2P transfers, Autopay mandates, app-to-app checkout."],
                ["<strong>IMPS</strong> (Immediate Payment Service)", "Older instant account-to-account rail using account/IFSC, MMID or mobile.", "Seconds to under a minute, 24×7; generally up to ₹5 lakh.", "Net settlement through NPCI/RBI arrangements.", "Bank apps, fallbacks, account-number transfers."],
                ["<strong>NEFT</strong> (National Electronic Funds Transfer)", "Batch retail and business credit transfer.", "Half-hourly batches, 24×7 since December 2019; no floor or formal cap.", "Deferred net settlement at RBI.", "Salary, vendor payments, scheduled transfers."],
                ["<strong>RTGS</strong> (Real-Time Gross Settlement)", "High-value central-bank settlement rail.", "Real-time, 24×7 since December 2020; minimum ₹2 lakh, no upper cap.", "Real-time gross settlement in RBI money.", "Large corporate, treasury, interbank and high-value customer payments."],
                ["<strong>NACH</strong> (National Automated Clearing House)", "Mandate-based bulk debit and credit system.", "Mandate setup and debit cycles vary, often T+1 style operating rhythm.", "Net settlement.", "EMIs, insurance premiums, mutual fund SIPs, dividends, subsidies."],
                ["<strong>RuPay / Visa / Mastercard</strong>", "Card authorisation, clearing and settlement networks.", "Authorisation in seconds, clearing and settlement typically T+1/T+2.", "Scheme net settlement through settlement banks.", "POS, e-commerce, recurring cards, tokenised card-on-file."],
                ["<strong>CTS</strong> (Cheque Truncation System)", "Image-based cheque clearing, replacing physical cheque movement.", "Usually T+1; declining but still important in courts, government and some B2B flows.", "Net settlement.", "Legacy cheque-dependent processes."],
                ["<strong>e₹</strong> (Digital Rupee pilot)", "Central Bank Digital Currency where the claim is directly on RBI.", "Pilot flows are near-real-time and programmable.", "On the RBI CBDC ledger rather than normal commercial bank deposit rails.", "Retail and wholesale pilots, programmable money experiments."],
            ]
        )
        + example("India rail choice for three payments",
            ol([
                "A ₹180 coffee QR payment should use UPI because the customer expects instant confirmation and the value is tiny.",
                "A ₹4 crore supplier payment should use RTGS because finality and large-value settlement matter more than retail convenience.",
                "A ₹2,500 monthly loan EMI should use NACH or UPI Autopay because the pattern is recurring and mandate-driven, not manually initiated each month.",
            ])
        )
        + H3("4.3  United States — batch legacy plus two instant rails")
        + p("The United States has a large, layered payments estate because old rails remain "
            "economically useful even after new rails arrive. Automated Clearing House (ACH) is "
            "cheap and deeply embedded. Fedwire is the high-value Federal Reserve wire rail. CHIPS "
            "handles large-value private-sector USD clearing. Real-Time Payments (RTP) by The "
            "Clearing House and FedNow by the Federal Reserve are the newer instant rails.")
        + table(
            ["Rail", "Plain-English role", "Speed and value", "Settlement model", "Typical use"],
            [
                ["<strong>ACH</strong>", "The scheduled postal van of US payments.", "Same-day or next-day batches; per-rule limits rather than one universal statutory cap.", "Deferred net through FedACH or Electronic Payments Network.", "Payroll, bill pay, mortgage, subscriptions, corporate batches."],
                ["<strong>Fedwire</strong>", "The Federal Reserve's high-value wire rail.", "Seconds during operating hours; no practical retail-style cap.", "Real-time gross settlement at the Federal Reserve.", "Treasury, interbank, securities, large corporate payments."],
                ["<strong>CHIPS</strong>", "Private large-value USD clearing for major banks.", "Business-day large-value processing.", "Final net settlement with liquidity-saving algorithms.", "Correspondent banking, cross-border USD flows, FX legs."],
                ["<strong>RTP</strong>", "Private instant rail operated by The Clearing House.", "24×7 seconds; limit raised to USD 1 million in 2024.", "Prefunded joint account model at the Fed.", "Instant B2B, gig payouts, request-for-payment use cases."],
                ["<strong>FedNow</strong>", "Public instant rail operated by the Federal Reserve.", "24×7 seconds; default transfer limit up to USD 500,000, banks may set lower.", "Settlement in Federal Reserve master accounts.", "Instant consumer and business payments since July 2023."],
                ["<strong>Zelle</strong>", "Bank-consortium consumer P2P experience.", "Seconds to user, settlement can use underlying rails.", "Uses bank and network arrangements behind the scenes.", "Consumer domestic person-to-person transfers."],
                ["<strong>Cards</strong>", "Authorisation now, merchant settlement later.", "Authorisation in seconds, settlement often T+1/T+2.", "Scheme clearing and settlement.", "POS, e-commerce, subscriptions, chargeback-heavy commerce."],
            ]
        )
        + H3("4.4  United Kingdom — Pay.UK, Bank of England and fraud pressure")
        + p("The UK is useful because rail design is now inseparable from scam reimbursement and "
            "operational resilience. Faster Payments Service (FPS) gives near-instant domestic "
            "payments. BACS remains the bulk salary and direct-debit workhorse. CHAPS is the "
            "high-value Bank of England rail. Confirmation of Payee is not a money movement rail; "
            "it is a pre-payment name-check control that materially changes fraud risk.")
        + table(
            ["Rail / control", "Plain-English role", "Speed/value", "Settlement", "Why it matters"],
            [
                ["<strong>FPS</strong> (Faster Payments Service)", "Instant domestic credit transfer.", "Seconds, 24×7; scheme limit up to £1 million though banks often set lower.", "Net settlement at Bank of England cycles.", "Retail and business instant payments, open-banking payment initiation."],
                ["<strong>BACS</strong>", "Three-day batch rail.", "Three working day cycle.", "Net settlement at Bank of England.", "Payroll, Direct Debit, supplier payments with predictable timing."],
                ["<strong>CHAPS</strong>", "High-value same-day sterling rail.", "Same-day final payment, business hours.", "Real-time gross settlement at Bank of England.", "House purchases, large corporate and treasury transfers."],
                ["<strong>ICS</strong> (Image Clearing System)", "Cheque image clearing.", "Typically next weekday style clearing.", "Net settlement.", "Legacy cheque use."],
                ["<strong>Confirmation of Payee</strong>", "Name-check before account-to-account payment.", "Before payment initiation.", "Not applicable.", "Key control for Authorised Push Payment fraud, mandatory reimbursement context from October 2024."],
                ["<strong>Open Banking PISP</strong>", "Third-party payment initiation over bank APIs.", "Often uses FPS underneath.", "Rail-dependent.", "Account-to-account e-commerce and bill payments."],
            ]
        )
        + red_flag(
            p("If a UK design review treats Confirmation of Payee as optional ‘nice-to-have UX’, "
              "push back. In the UK, scam controls now connect directly to customer harm, Consumer "
              "Duty, APP fraud reimbursement and operational resilience. It is a control, not a "
              "screen decoration.")
        )
        + H3("4.5  Eurozone — SEPA, TARGET services and DORA-era resilience")
        + p("The Eurozone separates pan-European retail formats from central-bank settlement "
            "services. Single Euro Payments Area (SEPA) defines common euro credit transfer and "
            "direct debit schemes. TARGET services run by the Eurosystem provide settlement "
            "in central-bank money. The 2024 EU Instant Payments Regulation pushes instant euro "
            "payments from optional innovation toward baseline service.")
        + table(
            ["Rail", "Plain-English role", "Speed/value", "Settlement", "Design implication"],
            [
                ["<strong>SEPA Credit Transfer</strong>", "Standard euro push transfer.", "Usually next business day.", "Net through clearing and settlement mechanisms into TARGET services.", "Corporate and retail euro transfers across SEPA countries."],
                ["<strong>SEPA Instant Credit Transfer</strong>", "Instant euro push transfer.", "Ten-second target, 24×7; historically €100,000 scheme cap, evolving under regulation.", "TIPS, RT1 or national instant mechanisms.", "Banks must design always-on fraud, sanctions and liquidity controls."],
                ["<strong>SEPA Direct Debit</strong>", "Mandate-based euro pull payment.", "Pre-notified, scheme timelines.", "Net settlement.", "Utilities, subscriptions, B2B mandates."],
                ["<strong>T2</strong>", "Eurosystem high-value settlement platform replacing TARGET2 branding after consolidation.", "Real-time business-day settlement.", "Central-bank money.", "Wholesale euro payments and monetary-policy operations."],
                ["<strong>TIPS</strong>", "TARGET Instant Payment Settlement.", "24×7 instant settlement.", "Central-bank money.", "Pan-European instant settlement layer."],
                ["<strong>T2S</strong>", "TARGET2-Securities.", "Securities and cash settlement.", "Delivery versus Payment in central-bank money.", "Capital markets settlement, not normal retail payments."],
            ]
        )
        + H3("4.6  Singapore and major adjacent markets")
        + p("Singapore is cloud-positive and digitally advanced, but still control-heavy under "
            "Monetary Authority of Singapore (MAS) expectations. FAST is the instant domestic "
            "rail. PayNow is the proxy addressing layer over FAST. GIRO handles batch debit and "
            "credit. MEPS+ is the high-value real-time settlement system.")
        + table(
            ["Market", "Instant / retail rail", "Batch / mandate rail", "High-value rail", "Why consultants see it"],
            [
                ["Singapore", "FAST and PayNow", "GIRO", "MEPS+", "Regional treasury, digital banks, cross-border linkages with India and Thailand."],
                ["Hong Kong", "FPS", "Autopay / legacy clearing", "CHATS", "North Asia cash management and multi-currency settlement."],
                ["UAE", "Instant Payment Platform and Aani", "Direct debit systems", "UAEFTS", "Middle East transaction banking and remittance corridors."],
                ["Australia", "NPP with PayID", "BECS", "RITS", "Open banking, real-time data-rich payments and APRA operational resilience."],
                ["Brazil", "PIX", "Boleto and direct debit arrangements", "STR", "One of the world's most successful instant-payment adoption stories."],
            ]
        )
        + H3("4.7  Cross-border — SWIFT is messaging, not settlement")
        + p("Cross-border payments feel mysterious because there may be no direct account "
            "relationship between the payer's bank and the beneficiary's bank. Banks solve this "
            "through correspondent banking. A nostro account is ‘our money held at your bank’. "
            "A vostro account is ‘your money held at our bank’. SWIFT carries the instruction. "
            "The actual money moves by debiting and crediting correspondent accounts, sometimes "
            "through multiple banks.")
        + mermaid(
            "flowchart LR\n"
            "  C[\"Corporate customer<br/>India\"] --> B1[\"Sending bank<br/>Mumbai\"]\n"
            "  B1 --> S[\"SWIFT message<br/>pacs.008 or MT103\"]\n"
            "  S --> CB[\"Correspondent bank<br/>New York nostro\"]\n"
            "  CB --> B2[\"Beneficiary bank<br/>United States\"]\n"
            "  B2 --> V[\"Vendor account<br/>credited\"]\n"
            "  B1 -. funds .-> N[\"Nostro account<br/>USD balance\"]\n"
            "  N -. debit and credit .-> CB\n",
            "Figure 4.1 — SWIFT carries the instruction; correspondent accounts carry the value."
        )
        + table(
            ["Mechanism", "What it is", "What changed recently"],
            [
                ["<strong>SWIFT MT</strong>", "Legacy Message Type format such as MT103 and MT202.", "Cross-border CBPR+ migration to ISO 20022 has a November 2025 coexistence end-date."],
                ["<strong>SWIFT MX / ISO 20022</strong>", "Structured XML messages such as pacs.008, pacs.009 and pacs.002.", "Richer party, purpose, remittance and compliance data."],
                ["<strong>SWIFT gpi</strong>", "Global Payments Innovation tracker and service-level improvements.", "End-to-end traceability and fee transparency improved cross-border experience."],
                ["<strong>CLS</strong>", "Continuous Linked Settlement for foreign exchange.", "Payment-versus-payment reduces Herstatt risk across major currencies."],
                ["<strong>Wise / Revolut / Airwallex style networks</strong>", "Fintech multi-rail networks using local accounts in many countries.", "Often avoid long correspondent chains for retail and SME transfers."],
                ["<strong>Project Nexus / mBridge pilots</strong>", "Interlinking instant-payment systems or central-bank digital currency platforms.", "Important future direction, not yet replacement for mainstream correspondent banking."],
            ]
        )
        + callout("How to choose a rail in a review",
            ol([
                "Start with customer promise: instant, same-day, scheduled or low-cost batch?",
                "Check value and finality: low-value reversible flow or high-value final treasury flow?",
                "Check geography and currency: domestic, SEPA-wide, USD correspondent, FX leg?",
                "Check fraud and sanctions: is real-time screening mature enough for this rail?",
                "Check operations: can support, reconciliation, treasury and incident teams run it 24×7?",
            ]),
            "info")
    )
    return TopicSection("4.  Types & variations — the rails that move money worldwide", "intermediate", body)


def _sec5() -> TopicSection:
    body = (
        primer(
            p("Section 4 described rails from the outside. Section 5 opens the machine. Under "
              "every rail are mechanisms that make it safe: message formats, addressing, cryptography, "
              "clearing rules, settlement-risk controls, idempotency, sagas, outbox publishing and "
              "reconciliation. You do not need to code them to lead a BFSI programme, but you do "
              "need to know what they physically protect.")
        )
        + H3("5.1  Message formats — the grammar of money movement")
        + p("A payment message is not a sentence in English. It is a strict form with fields. "
            "If the field is missing, misspelled, too long, wrongly encoded or placed in the "
            "wrong part of the message, the receiving rail may reject it. That is why ISO 20022 "
            "migration is not a cosmetic format change. It changes what data can travel with the "
            "payment and how downstream sanctions, reconciliation and analytics systems work.")
        + table(
            ["Format", "Where it appears", "What it looks like conceptually", "Why it matters"],
            [
                ["<strong>ISO 20022</strong>", "SEPA, SWIFT MX / CBPR+, FedNow, many modern rails.", "Structured XML messages such as pacs.008 customer credit transfer, pacs.009 bank transfer, pacs.002 status, camt.053 statement.", "Carries rich party, remittance, purpose, Legal Entity Identifier and compliance data."],
                ["<strong>SWIFT MT</strong>", "Legacy cross-border messaging.", "Colon-delimited fields such as :50K: ordering customer and :71A: charges.", "Compact and familiar, but weak for structured compliance data. CBPR+ migration retires it for cross-border by November 2025."],
                ["<strong>ISO 8583</strong>", "Card authorisation networks.", "Bitmap-driven card message with fields for PAN/token, merchant, amount, response code.", "Explains why card auth feels instant while settlement and disputes happen later."],
                ["<strong>NACHA / BACS / NACH files</strong>", "Batch direct credit and debit rails.", "Fixed or scheme-defined file layouts with header, detail and control totals.", "Tiny formatting errors can reject an entire payroll or EMI batch."],
                ["<strong>API JSON payloads</strong>", "Open banking, fintech APIs, internal payment orchestration.", "JSON fields signed or transported over TLS/mTLS.", "Developer-friendly, but must be schema-validated, signed and versioned."],
            ]
        )
        + example("Why one missing field can block a payment",
            p("A German corporate sends €120,000 to a French supplier. Under ISO 20022, the bank "
              "expects a purpose code and structured creditor address for a compliance-sensitive "
              "payment. If the old system stuffs the address into one free-text line, the new "
              "screening engine may fail to parse it and hold the payment. The customer sees "
              "‘payment delayed’. The root cause is not liquidity or fraud. It is message-data "
              "quality.")
        )
        + H3("5.2  Addressing — how the system knows where money should land")
        + p("Addressing is the payment equivalent of postal addresses. Different rails identify "
            "the destination differently. A Virtual Payment Address is convenient for humans. "
            "An International Bank Account Number is precise across many countries. A card token "
            "hides the real card number. A SWIFT Business Identifier Code identifies a financial "
            "institution, not necessarily a customer's final account.")
        + table(
            ["Address type", "Expanded meaning", "Where used", "Plain-English example"],
            [
                ["<strong>VPA</strong>", "Virtual Payment Address", "India UPI", "<code>ramesh@okhdfcbank</code> maps behind the scenes to a bank account."],
                ["<strong>IFSC + account</strong>", "Indian Financial System Code plus account number", "NEFT, RTGS, IMPS", "IFSC identifies bank branch or service node, account identifies customer."],
                ["<strong>ABA routing number</strong>", "American Bankers Association routing number", "US ACH, wires", "Nine-digit bank identifier plus account number."],
                ["<strong>Sort code + account</strong>", "UK bank/branch code plus account number", "FPS, BACS, CHAPS", "Six-digit sort code and eight-digit account."],
                ["<strong>IBAN</strong>", "International Bank Account Number", "SEPA and many cross-border flows", "Country code, check digits, bank and account identifiers."],
                ["<strong>BIC</strong>", "Business Identifier Code", "SWIFT", "Identifies the bank or branch on SWIFT."],
                ["<strong>PAN / token</strong>", "Primary Account Number or network token", "Cards", "Real card number is increasingly replaced by a token for merchant storage."],
                ["<strong>Proxy ID</strong>", "Mobile number, email, tax ID, company ID", "PayNow, PIX, NPP PayID, UPI mobile mapping", "Human-friendly alias resolved to a bank account."],
            ]
        )
        + H3("5.3  Cryptography — proving and protecting the instruction")
        + p("Cryptography in payments has three jobs. First, confidentiality: outsiders cannot "
            "read sensitive data in transit. Second, integrity: nobody can alter the amount or "
            "beneficiary without detection. Third, non-repudiation: a party cannot later plausibly "
            "deny that it sent a signed instruction. The exact tools vary, but the shape is stable.")
        + table(
            ["Mechanism", "What it physically does", "BFSI example"],
            [
                ["<strong>TLS</strong> (Transport Layer Security)", "Encrypts the connection between two endpoints and authenticates the server.", "Mobile app to API gateway, bank portal to backend."],
                ["<strong>mTLS</strong> (mutual TLS)", "Both sides present certificates, proving client and server identity.", "Bank payment engine to NPCI / SWIFT gateway / internal service."],
                ["<strong>Digital signature</strong>", "Signs message content so tampering is detectable.", "Corporate payment file signed by treasury, ISO 20022 payload signature."],
                ["<strong>HSM</strong> (Hardware Security Module)", "Tamper-resistant device that stores keys and performs cryptographic operations.", "PIN verification, card network keys, SWIFT signing keys."],
                ["<strong>DUKPT</strong> (Derived Unique Key Per Transaction)", "Derives a different key per transaction so one key compromise has limited blast radius.", "Point-of-sale PIN block encryption."],
                ["<strong>Tokenisation</strong>", "Replaces sensitive value with a safer substitute.", "Card-on-file token under RBI CoFT and global network tokenisation."],
            ]
        )
        + example("What mTLS adds beyond normal TLS",
            p("Normal TLS is like you checking the bank branch signboard before entering. mTLS "
              "is the branch also checking your employee badge before letting you behind the "
              "counter. For an internal payment API, this matters because the server should not "
              "accept money-movement instructions from any machine on the network. It should "
              "accept only a workload with a valid client certificate issued by the bank's Public "
              "Key Infrastructure.")
        )
        + H3("5.4  Clearing houses — the shared referee")
        + p("A clearing house is the referee and scorekeeper between many banks. It defines the "
            "rulebook, validates participant messages, records obligations, calculates positions, "
            "manages returns or disputes and sends settlement instructions. Without a shared "
            "referee, every bank would need a separate bilateral agreement and technical link "
            "with every other bank.")
        + table(
            ["Region / domain", "Shared referee", "What it clears or coordinates"],
            [
                ["India", "NPCI and RBI", "UPI, IMPS, NACH, RuPay, CTS, NEFT and RTGS arrangements."],
                ["United States", "FedACH, EPN, The Clearing House, Federal Reserve", "ACH, RTP, CHIPS, Fedwire, FedNow."],
                ["United Kingdom", "Pay.UK and Bank of England", "FPS, BACS, Image Clearing System and CHAPS settlement."],
                ["Eurozone", "EBA Clearing, Eurosystem, national CSMs", "SEPA SCT, SEPA Instant, SEPA Direct Debit, T2 and TIPS."],
                ["Singapore", "BCS and MAS", "FAST, GIRO and MEPS+."],
                ["Cards", "Visa, Mastercard, Amex, RuPay, UnionPay", "Authorisation, clearing, disputes, scheme settlement."],
                ["FX", "CLS", "Payment-versus-payment settlement for major currencies."],
            ]
        )
        + H3("5.5  Settlement risk — the Herstatt lesson")
        + p("Settlement risk is the danger that one side of a deal pays but the other side fails "
            "before paying back. The classic case is Bankhaus Herstatt in Germany in 1974. It "
            "received Deutsche Marks during the European day but was closed before it paid US "
            "Dollars later in the New York day. Counterparties lost the dollar leg. That incident "
            "is why foreign-exchange settlement conversations still use the phrase Herstatt risk.")
        + table(
            ["Control", "How it reduces settlement risk", "Example"],
            [
                ["RTGS", "Moves each payment finally in central-bank money.", "Fedwire, CHAPS, RBI RTGS, T2."],
                ["Payment versus Payment", "Both currency legs settle together or neither settles.", "CLS for FX."],
                ["Delivery versus Payment", "Securities and cash settle together.", "T2S and many securities depositories."],
                ["Prefunding", "Participants put money in before they send instant payments.", "RTP-style prefunded positions."],
                ["Default funds and loss sharing", "Members contribute resources to absorb a participant failure.", "Clearing house rulebooks for schemes and central counterparties."],
                ["Net debit caps", "Limits how much one participant can owe before settlement.", "ACH and scheme risk controls."],
            ]
        )
        + H3("5.6  Idempotency — making retries safe")
        + p("Distributed systems fail in boring ways: the phone loses signal, a gateway times out, "
            "a response is delayed, a service restarts after writing to the database but before "
            "replying. The user presses again. The app retries. The gateway retries. If every retry "
            "can create a new debit, the bank will duplicate money movement. Idempotency is the "
            "pattern that makes repeated requests with the same key produce the same result.")
        + mermaid(
            "sequenceDiagram\n"
            "  autonumber\n"
            "  participant C as Customer app\n"
            "  participant G as API gateway\n"
            "  participant P as Payment service\n"
            "  participant D as Idempotency store\n"
            "  participant L as Ledger\n"
            "  C->>G: Pay 100 with key ABC123\n"
            "  G->>P: Forward key ABC123\n"
            "  P->>D: Have we seen ABC123\n"
            "  D-->>P: No\n"
            "  P->>L: Debit and record payment\n"
            "  L-->>P: Committed\n"
            "  P->>D: Store ABC123 as success\n"
            "  P-->>G: Success\n"
            "  Note over C,G: Response is lost on the network\n"
            "  C->>G: Retry pay 100 with key ABC123\n"
            "  G->>P: Forward key ABC123\n"
            "  P->>D: Have we seen ABC123\n"
            "  D-->>P: Yes, success already stored\n"
            "  P-->>G: Return previous success, no new debit\n",
            "Figure 5.1 — Idempotency turns a dangerous duplicate request into a safe repeat."
        )
        + H3("5.7  Sagas — when one business transaction spans many systems")
        + p("A single customer-visible transaction often crosses several systems that cannot "
            "share one database transaction. A loan disbursal might update the Loan Origination "
            "System, Loan Management System, core banking ledger, notification service, general "
            "ledger and document store. A two-phase commit across all of them would be slow and "
            "fragile. A saga breaks the journey into local transactions plus compensating actions.")
        + table(
            ["Saga step", "Local transaction", "Compensating action if later step fails"],
            [
                ["Reserve funds", "Mark ₹5 lakh approved loan funds as reserved.", "Release reservation."],
                ["Create loan account", "Open account in Loan Management System.", "Close or mark account as cancelled."],
                ["Credit customer account", "Post credit to core banking ledger.", "Post reversing debit with audit reason."],
                ["Generate documents", "Create sanction and disbursal documents.", "Void document versions."],
                ["Notify customer", "Send SMS/email/app confirmation.", "Send correction notice if reversal is required."],
            ]
        )
        + red_flag(
            p("If a team says ‘we guarantee atomicity across ten microservices’ and cannot show "
              "the saga, outbox, idempotency and compensation design, push back. They may be "
              "using the word transaction as a hope, not an engineering guarantee.")
        )
        + H3("5.8  The outbox pattern — preventing lost events")
        + p("A common failure is this: the service debits the ledger, then tries to publish an "
            "event to Kafka or another message bus saying ‘payment debited’. The service crashes "
            "after the debit but before the event publish. Downstream systems never hear about "
            "the debit. The outbox pattern solves this by writing the business change and an "
            "outbox row in the same database transaction. A separate relay later publishes the "
            "outbox row. If the relay crashes, it retries from the outbox table.")
        + mermaid(
            "sequenceDiagram\n"
            "  autonumber\n"
            "  participant P as Payment service\n"
            "  participant DB as Payment database\n"
            "  participant R as Outbox relay\n"
            "  participant K as Kafka event bus\n"
            "  P->>DB: Begin transaction\n"
            "  P->>DB: Insert ledger posting\n"
            "  P->>DB: Insert outbox event PaymentDebited\n"
            "  P->>DB: Commit\n"
            "  R->>DB: Poll unsent outbox events\n"
            "  DB-->>R: PaymentDebited\n"
            "  R->>K: Publish PaymentDebited\n"
            "  K-->>R: Ack\n"
            "  R->>DB: Mark outbox event sent\n",
            "Figure 5.2 — Outbox makes the database commit and event publication recoverable."
        )
        + H3("5.9  Reconciliation — proving all books agree")
        + p("Reconciliation is the discipline of comparing records across systems and counterparties. "
            "The bank compares its channel records, core ledger, payment engine, clearing-house "
            "files, settlement account, general ledger and customer notifications. Items are "
            "classified as matched, missing internally, missing externally, amount mismatch, status "
            "mismatch or timing difference. Each break gets an owner and Service Level Agreement.")
        + example("A practical reconciliation drill",
            ol([
                "Mobile channel says 2,000,000 UPI payments succeeded on Tuesday worth ₹164 crore.",
                "Core ledger says 1,999,996 succeeded worth ₹163.9992 crore.",
                "NPCI file says 2,000,001 accepted worth ₹164.0003 crore.",
                "Settlement file says the bank's net payable is ₹23.4 crore.",
                "Operations identifies four channel items missing in core, one NPCI item not in channel, and an ₹11,000 value mismatch.",
                "Until the breaks are resolved, finance cannot blindly certify the day's position and customer support cannot answer affected complaints confidently.",
            ])
        )
        + table(
            ["Break type", "What it means", "Typical action"],
            [
                ["Missing in core", "Channel or switch says success but core ledger lacks posting.", "Post, reverse or investigate before customer harm grows."],
                ["Missing externally", "Bank posted but clearing house has no matching record.", "Hold customer-visible finality, investigate switch transmission."],
                ["Amount mismatch", "Same transaction ID but different amount.", "Escalate immediately, potential corruption or mapping defect."],
                ["Status mismatch", "One side says success, another says failed or pending.", "Use scheme status enquiry and customer communication runbook."],
                ["Timing difference", "Both sides agree, but in different windows or files.", "Monitor until expected settlement/reporting window closes."],
            ]
        )
        + callout("End-of-section recap",
            ul([
                "Message format is the grammar of money movement; ISO 20022 changes downstream controls, not just field names.",
                "Addressing determines where money lands and how mistakes are caught before movement.",
                "Cryptography protects confidentiality, integrity and non-repudiation.",
                "Clearing houses are shared referees; settlement risk is why central-bank money, prefunding, PvP and DvP matter.",
                "Idempotency, sagas and outbox are the core software patterns that stop retries, partial failure and lost events from duplicating or losing money.",
                "Reconciliation is the proof that every book agrees after the customer sees the green tick.",
            ]),
            "info")
    )
    return TopicSection("5.  Advanced — the mechanisms underneath every rail", "advanced", body)


def _sec6() -> TopicSection:
    body = (
        primer(
            p("A banking transaction is not just a technical event. It is a regulated promise. "
              "The same ₹500, £50, USD 100 or €200 transfer has to satisfy customer-protection "
              "law, privacy law, anti-money-laundering law, sanctions law, scheme rules, operational "
              "resilience expectations, outsourcing rules, record-retention rules and sometimes "
              "central-bank settlement rules. The important leadership move is to stop seeing "
              "regulation as a PDF that compliance reads after technology is done. Regulation "
              "changes the shape of the system itself: what data is collected, where it is stored, "
              "which checks run before posting, how fast incidents are reported, whether a customer "
              "can reverse a payment, and who signs off a cloud or vendor design.")
        )
        + H3("6.1  Start with the physical picture — a regulator changes the factory floor")
        + p("Imagine a bakery that sells bread. If a city rule says the bakery must label allergens, "
            "keep refrigeration logs, record supplier batches and allow health inspectors to audit "
            "the kitchen, the rule is not merely paperwork. The bakery needs thermometers, logbooks, "
            "supplier records, staff training and a recall process. A bank is the same. If a rule "
            "says ‘screen sanctions before payment’, the system needs a sanctions-list feed, fuzzy "
            "matching engine, hold queue, maker-checker review, audit trail and customer-status "
            "message. Regulation becomes software, data, people and operating rhythm.")
        + mermaid(
            "flowchart TB\n"
            "  R[\"Regulatory obligation\"] --> P[\"Policy interpretation\"]\n"
            "  P --> C[\"Control design\"]\n"
            "  C --> S[\"System capability\"]\n"
            "  S --> O[\"Operations runbook\"]\n"
            "  O --> E[\"Evidence for audit and regulator\"]\n"
            "  E --> R\n"
            "  C --> D[\"Data fields and retention\"]\n"
            "  C --> A[\"Approval and accountability\"]\n"
            "  C --> M[\"Monitoring and incident reporting\"]\n",
            "Figure 6.1 — In BFSI, a rule becomes controls, systems, operations and evidence."
        )
        + example("How one rule changes a simple payment",
            p("Suppose a customer in London sends £4,000 to a new payee. Without regulation, a "
              "naive system might only check password, balance and sort code. In the real UK flow, "
              "the bank also considers Strong Customer Authentication, Confirmation of Payee, "
              "Authorised Push Payment scam risk, sanctions screening, transaction monitoring, "
              "consumer-duty treatment, fraud warnings, audit logging and potential reimbursement "
              "liability. The button still says ‘Pay’. Behind the button, the factory floor is far "
              "larger because the regulated promise is larger."))
        + H3("6.2  The eight regulatory questions to map onto any transaction")
        + table(
            ["Question", "Plain-English meaning", "System design consequence", "Example"],
            [
                ["Who is the customer?", "Know Your Customer and identity obligations.", "Onboarding data, document verification, risk rating, periodic refresh.", "A bank cannot let an anonymous shell company send high-value international wires."],
                ["May this customer do this transaction?", "Product, limit, mandate, fraud, sanctions and suitability checks.", "Authorisation engine, limits, holds, exception queues.", "A minor, dormant account or blocked customer may fail authorisation."],
                ["Where is the data allowed to live?", "Localisation, privacy, transfer and retention rules.", "Regional storage, encryption, masking, deletion and legal-hold design.", "Indian payment data may need India storage under RBI payment-data localisation expectations."],
                ["Who else touches the flow?", "Outsourcing, cloud, vendor and third-party-risk rules.", "Due diligence, audit rights, exit plans, concentration-risk monitoring.", "A payment processor or cloud provider becomes part of the regulated supply chain."],
                ["How fast must the bank detect and report trouble?", "Cyber, fraud and operational-incident reporting clocks.", "Monitoring, severity taxonomy, regulator notification workflow.", "A material ICT incident may have to be escalated under region-specific rules."],
                ["Can the customer get money back?", "Consumer-protection and scheme-dispute rights.", "Dispute case management, evidence capture, provisional credit, reimbursement rules.", "Card chargebacks, UK APP scam reimbursement and electronic-funds-transfer liability differ."],
                ["How is financial crime prevented?", "Anti-Money Laundering, Countering Financing of Terrorism and sanctions controls.", "Screening, transaction monitoring, suspicious-activity reporting, case management.", "A fuzzy OFAC or EU sanctions match may pause an otherwise valid payment."],
                ["What proof survives later?", "Audit, record retention, ledger evidence and explainability.", "Immutable logs, reconciliation records, model decisions, retention schedules.", "A regulator asks six months later why a transaction was allowed or blocked."],
            ]
        )
        + H3("6.3  Regional overlay matrix — same transaction, different rule pressure")
        + p("The names differ by geography, but the pattern is stable: protect customers, keep "
            "criminal money out, keep critical services resilient, control outsourcing, protect "
            "data and preserve evidence. A global bank such as Citi, Standard Chartered, HSBC, "
            "JPMorgan or Deutsche Bank usually has to satisfy several columns at once because "
            "the customer, booking entity, currency, data centre, correspondent bank and vendor "
            "may sit in different jurisdictions.")
        + table(
            ["Concern", "India", "United States", "United Kingdom", "Eurozone", "Singapore"],
            [
                ["Payment data and privacy", "Reserve Bank of India payment-data localisation expectations plus Digital Personal Data Protection Act 2023 obligations.", "Gramm-Leach-Bliley Act for financial privacy, state privacy laws such as California Consumer Privacy Act / California Privacy Rights Act, and sectoral record rules.", "United Kingdom General Data Protection Regulation and Data Protection Act 2018 with international-transfer controls.", "European Union General Data Protection Regulation plus cross-border transfer scrutiny after Schrems II.", "Personal Data Protection Act and Monetary Authority of Singapore technology-risk expectations."],
                ["Customer authentication and consent", "RBI digital-payment security controls, two-factor authentication norms, UPI PIN and device binding under scheme rules.", "Electronic Fund Transfer Act and Regulation E for many consumer electronic transfers, card network rules and bank authentication policies.", "Payment Services Regulations, Strong Customer Authentication expectations, Confirmation of Payee and Consumer Duty context.", "Revised Payment Services Directive, Strong Customer Authentication, SEPA scheme rules and Instant Payments Regulation requirements.", "Payment Services Act, MAS e-payments user-protection expectations and Shared Responsibility Framework direction."],
                ["Financial crime controls", "Prevention of Money Laundering Act, RBI Know Your Customer Master Direction and Financial Intelligence Unit India reporting.", "Bank Secrecy Act, USA PATRIOT Act, Financial Crimes Enforcement Network reporting and Office of Foreign Assets Control sanctions.", "Money Laundering Regulations 2017, Joint Money Laundering Steering Group guidance and Office of Financial Sanctions Implementation lists.", "European Union Anti-Money Laundering directives, AML package and EU consolidated sanctions.", "MAS Notice 626, Corruption Drug Trafficking and Other Serious Crimes Act and targeted financial sanctions."],
                ["Operational resilience", "RBI business-continuity and disaster-recovery expectations, IT governance Master Direction and sectoral cyber frameworks.", "Federal Financial Institutions Examination Council guidance, Office of the Comptroller of the Currency standards, Federal Reserve and New York Department of Financial Services cyber rules.", "Prudential Regulation Authority / Financial Conduct Authority / Bank of England operational resilience regime with important business services and impact tolerances.", "Digital Operational Resilience Act effective from January 2025, Network and Information Security Directive 2 and European Banking Authority guidance.", "MAS Technology Risk Management Guidelines and business-continuity requirements."],
                ["Outsourcing and cloud", "RBI Master Direction on Outsourcing of IT Services 2023 and data-localisation constraints for payment data.", "Interagency third-party-risk guidance, OCC Bulletins and bank-specific supervisory expectations.", "PRA Supervisory Statement 2/21 and FCA outsourcing / third-party expectations.", "European Banking Authority outsourcing guidelines and DORA third-party ICT risk regime.", "MAS Outsourcing Guidelines and TRM expectations, with clear exit and audit provisions."],
                ["Cards and stored credentials", "RBI card-on-file tokenisation rules and restrictions on merchant storage of Primary Account Number.", "Payment Card Industry Data Security Standard 4.0, Regulation E / Z and card-network operating rules.", "PCI DSS 4.0, card-scheme rules and consumer-credit protections.", "PCI DSS 4.0, PSD2 Strong Customer Authentication and card-scheme rules.", "PCI DSS, MAS notices and merchant-acquirer controls."],
                ["Customer liability and disputes", "RBI limited-liability framework for unauthorised electronic banking transactions and scheme chargeback rules.", "Regulation E for debit / electronic transfers, Regulation Z for credit cards and network chargebacks.", "Mandatory Authorised Push Payment fraud reimbursement rules from October 2024, plus Financial Ombudsman Service pathways.", "PSD2 refund and liability provisions, SEPA return rules and evolving instant-payment verification requirements.", "MAS e-payment user-protection guidelines and Shared Responsibility Framework direction."],
                ["Reporting and evidence", "RBI, FIU-IND, CERT-In and scheme reporting depending on incident type.", "FinCEN suspicious activity reports, cyber incident notification expectations and supervisory examination evidence.", "FCA / PRA notifications, suspicious activity reporting and operational-resilience self-assessments.", "DORA incident reporting, suspicious-transaction reporting and GDPR breach notification.", "MAS incident reporting, suspicious transaction reports and audit evidence expectations."],
            ]
        )
        + H3("6.4  Data localisation and privacy — why architecture diagrams need geography")
        + p("A payment is data before it is money. It contains names, account identifiers, device "
            "identifiers, merchant details, location hints, purpose codes, fraud scores, sanctions "
            "screening results and ledger references. Privacy and localisation rules decide where "
            "that data may be stored, who may see it, how long it survives and whether it can be "
            "copied to another country for analytics or support. That means a transaction architecture "
            "diagram without geography is incomplete.")
        + example("The India payment-data localisation design choice",
            p("A global bank runs a card-tokenisation support platform. Indian card-on-file payment "
              "data cannot be casually replicated into a United States analytics lake just because "
              "the fraud team prefers one global dashboard. A compliant design may keep full payment "
              "data and sensitive identifiers in India, export only permitted masked or aggregated "
              "signals, and require India-based operational access for certain support actions. The "
              "trade-off is real: global analytics becomes harder, but regulatory breach risk falls."))
        + table(
            ["Design artefact", "Regulatory question to ask", "Bad answer", "Stronger answer"],
            [
                ["Logical data model", "Which fields are personal data, payment data, card data, bank secrecy data or sanctions evidence?", "All transaction data is treated as one generic table.", "Fields are classified and mapped to retention, masking and residency rules."],
                ["Deployment diagram", "Which country stores primary, replica, backup, log and analytics copies?", "Only production database region is shown.", "Primary, replica, disaster recovery, logs, support exports and data lake are all geographically labelled."],
                ["Access model", "Who can view raw account, card, beneficiary and fraud data?", "Developers can query production during incidents.", "Break-glass access, masking, approval workflow and immutable audit logs are enforced."],
                ["Vendor integration", "Does the vendor receive regulated data or only a token / decision response?", "Full payload is sent because it is technically convenient.", "Data minimisation, contractual controls, audit rights and deletion paths are documented."],
            ]
        )
        + H3("6.5  Financial crime — AML, CFT and sanctions are not one checkbox")
        + p("Financial-crime controls exist because banks can be misused to hide criminal proceeds, "
            "fund terrorism, evade sanctions, bribe officials, move stolen money or disguise tax "
            "evasion. Anti-Money Laundering means detecting and preventing disguised criminal money. "
            "Countering Financing of Terrorism means detecting funding connected to terrorism even "
            "when the amount is small. Sanctions screening means not dealing with prohibited people, "
            "entities, vessels, geographies or sectors. These controls operate before, during and "
            "after a transaction.")
        + mermaid(
            "flowchart LR\n"
            "  K[\"KYC profile<br/>customer risk\"] --> T[\"Transaction request\"]\n"
            "  S[\"Sanctions lists<br/>names and entities\"] --> SC[\"Screening\"]\n"
            "  T --> SC\n"
            "  T --> TM[\"Transaction monitoring<br/>patterns over time\"]\n"
            "  K --> TM\n"
            "  SC --> H[\"Hold or release decision\"]\n"
            "  TM --> C[\"Case management\"]\n"
            "  C --> R[\"Suspicious activity report<br/>where required\"]\n",
            "Figure 6.2 — Financial-crime controls use customer profile, list screening and behavioural monitoring."
        )
        + example("Why a USD 900 transfer may be riskier than a USD 90,000 transfer",
            p("A known corporate sends USD 90,000 to a long-standing supplier with a matching invoice, "
              "expected country, normal frequency and clean sanctions screening. A newly opened "
              "personal account sends USD 900 to ten unrelated beneficiaries in a high-risk corridor "
              "within two hours, just below internal review thresholds. The second flow may deserve "
              "more attention. Financial crime is not only about amount. It is about pattern, customer "
              "profile, geography, purpose, beneficiary and timing."))
        + table(
            ["Control", "Where it sits in the transaction journey", "Common false comfort", "Leader's better question"],
            [
                ["KYC risk rating", "Before the customer transacts and during periodic refresh.", "The customer passed onboarding once.", "Has the customer's behaviour drifted away from the risk profile we approved?"],
                ["Sanctions screening", "At beneficiary setup, payment initiation, repair and sometimes post-event rescreening.", "We screen only exact names.", "How do we tune fuzzy matching, aliases, transliteration and false positives without missing true hits?"],
                ["Transaction monitoring", "After or near-real-time, depending on rail and risk.", "Rules exist in the engine.", "Which typologies do the rules cover, and what is the alert-to-case-to-report conversion quality?"],
                ["Case management", "When a payment or pattern needs human decision.", "Analysts can decide manually.", "Is the evidence complete enough for audit, regulator and law-enforcement review?"],
                ["Model governance", "For machine-learning risk scores and fraud models.", "The model has high accuracy.", "Can we explain adverse action, bias, drift and override decisions?"],
            ]
        )
        + H3("6.6  Operational resilience — regulators care whether the promise survives stress")
        + p("Operational resilience asks a simple question: when technology, people, vendors or "
            "facilities fail, can the bank still keep important business services within tolerable "
            "harm limits? This is stronger than classic disaster recovery. Disaster recovery asks "
            "whether systems can be restored. Operational resilience asks whether customers, markets "
            "and the wider financial system are protected while stress is happening.")
        + table(
            ["Concept", "Plain-English meaning", "Transaction example"],
            [
                ["Important business service", "A customer or market-facing service whose failure could cause intolerable harm.", "Retail payments, card authorisation, ATM cash withdrawal, corporate payroll, high-value settlement."],
                ["Impact tolerance", "Maximum tolerable disruption, expressed in time, volume, value or harm.", "No more than two hours outage for retail payments, or no missed high-value settlement cut-off."],
                ["Scenario testing", "Deliberately testing severe but plausible failures.", "Payment switch unavailable, cloud region outage, sanctions vendor unavailable, database corruption, cyber attack."],
                ["Substitutability", "Whether another channel, rail, site or process can take over.", "If UPI is degraded, can customers use IMPS or cards? If FPS is down, can CHAPS or BACS cover priority flows?"],
                ["Board evidence", "Proof senior management understands and accepts residual risk.", "Self-assessment, test results, remediation plan, customer-harm analysis."],
            ]
        )
        + example("Impact tolerance with numbers",
            p("A bank processes 20 million instant payments per day, with a peak of 1,200 payments "
              "per second. If the board sets an impact tolerance of 30 minutes for the instant-payment "
              "service, the design must survive roughly 2.16 million peak-window attempts without "
              "uncontrolled customer harm. That number shapes queue depth, retry strategy, customer "
              "messaging, liquidity monitoring, fallback rail design and call-centre staffing. A "
              "tolerance is not a slogan; it becomes capacity and runbook design."))
        + H3("6.7  Outsourcing and cloud — the bank can outsource work, not accountability")
        + p("BFSI outsourcing rules exist because a bank remains accountable even when a cloud "
            "provider, software-as-a-service vendor, payment processor, card bureau, contact centre "
            "or analytics provider performs part of the work. If the vendor fails, leaks data or "
            "prevents exit, customers and regulators still look to the bank. That is why contracts, "
            "audit rights, concentration-risk monitoring, exit plans, business-continuity tests and "
            "data-return clauses are architecture concerns, not legal afterthoughts.")
        + table(
            ["Vendor design question", "Why it matters in transactions", "Evidence a leader should ask for"],
            [
                ["Is the service material or critical?", "A card authorisation processor outage blocks customer spending, unlike a low-risk newsletter tool.", "Materiality assessment tied to business service and customer harm."],
                ["Where does data go?", "Payment, card, fraud and identity data may trigger privacy, localisation or bank-secrecy rules.", "Data-flow map, subprocessor list, encryption and residency evidence."],
                ["Can the bank audit or obtain assurance?", "Regulators expect oversight, not blind trust.", "SOC reports, penetration tests, right-to-audit clauses and remediation tracking."],
                ["How does the bank exit?", "A locked-in payment engine can become systemic operational risk.", "Exit plan, data export format, transition runbook, tested recovery approach."],
                ["What concentration risk exists?", "Many banks using the same provider can create system-wide fragility.", "Provider dependency map and scenario test for provider or region outage."],
            ]
        )
        + H3("6.8  Customer protection — reversibility is a policy choice, not a bug")
        + p("Customers experience payments morally: ‘I was tricked’, ‘I typed the wrong account’, "
            "‘the merchant did not deliver’, ‘my card was stolen’. Payment systems experience "
            "payments mechanically: authenticated, authorised, cleared, settled, final. Consumer "
            "protection rules bridge that gap. Some rails are hard-final but have scam reimbursement "
            "or recall processes. Some rails are naturally disputable, such as cards. Some direct "
            "debits have indemnity or refund rights. Leaders must design the customer journey around "
            "the legal reality of the rail, not around what the database status says.")
        + table(
            ["Rail / flow", "Technical finality", "Customer-protection overlay", "Design implication"],
            [
                ["Card purchase", "Authorisation is immediate, settlement later.", "Chargebacks, fraud liability rules, scheme evidence cycles.", "Capture merchant evidence, device data, fulfilment proof and dispute timelines."],
                ["UK instant push payment", "FPS can move money in seconds.", "APP fraud reimbursement rules and Confirmation of Payee pressure.", "Invest in scam warnings, name-checks, mule detection and reimbursement operations."],
                ["India UPI payment", "Customer sees success quickly, interbank settlement follows cycles.", "RBI limited-liability framework, NPCI rules and bank complaint handling.", "Preserve authentication, device, PSP and switch evidence for disputes."],
                ["SEPA Direct Debit", "Debit follows mandate and scheme timelines.", "Refund rights and mandate-dispute process.", "Store mandate evidence and handle returns cleanly."],
                ["High-value RTGS / wire", "Hard final settlement.", "Limited recourse, strong pre-payment controls.", "Use maker-checker, beneficiary validation, sanctions and call-back for risky flows."],
            ]
        )
        + H3("6.9  Translating regulation into backlog items")
        + p("The most useful techno-functional leader does not stop at ‘regulation says we must’. "
            "They translate the rule into precise backlog work. Each obligation should become a "
            "control, each control should become system behaviour, and each system behaviour should "
            "produce evidence. If a team cannot point to the screen, API, data field, policy rule, "
            "alert, log, report or runbook that satisfies the obligation, the obligation is not yet "
            "implemented.")
        + table(
            ["Regulatory sentence", "Control interpretation", "Engineering backlog item", "Evidence produced"],
            [
                ["Report material ICT incidents quickly.", "Classify incidents and start notification workflow.", "Add severity taxonomy, incident timer, regulator-notification checklist and approval workflow.", "Timestamped incident record, approvals, submitted notification."],
                ["Do not store card PAN at merchants.", "Replace sensitive card number with token.", "Implement token vault / network token integration and purge stored PAN fields.", "Tokenisation logs, data-discovery scans, merchant attestation."],
                ["Screen sanctioned parties.", "Check originator, beneficiary and intermediaries against lists.", "Integrate sanctions engine, list update job, fuzzy matching and case queue.", "Screening result, match score, analyst decision and audit trail."],
                ["Maintain exit plan for critical outsourcing.", "Prove bank can transition or terminate service.", "Create data export, migration runbook, fallback process and annual exit test.", "Exit-test report, recovery time, issues and remediation."],
                ["Protect personal data.", "Limit collection, access, retention and transfer.", "Classify fields, mask screens, enforce retention jobs and track access.", "Data inventory, access logs, deletion evidence and privacy impact assessment."],
            ]
        )
        + red_flag(
            p("If a programme says ‘compliance will sign off at the end’, push back. In transaction "
              "systems, late compliance review usually discovers missing data fields, missing audit "
              "evidence, impossible reporting clocks, unapproved vendors or customer-dispute gaps. "
              "Those are architecture defects found too late, not paperwork defects."))
        + callout("End-of-section recap",
            ul([
                "Regulation changes transaction architecture: data, controls, vendors, operations, evidence and accountability.",
                "Map every transaction through eight regulatory questions: customer, permission, data location, third parties, incident clocks, reversibility, financial crime and proof.",
                "Global banks must satisfy overlapping India, US, UK, Eurozone and Singapore obligations, not a single-country checklist.",
                "AML, CFT and sanctions controls are separate but connected layers: profile, screen, monitor, case and report.",
                "Operational resilience turns customer harm limits into capacity, fallback, runbook and board-evidence requirements.",
            ]),
            "info")
    )
    return TopicSection("6.  Domain overlay — what changes because BFSI is regulated", "advanced", body)


def _sec7() -> TopicSection:
    body = (
        primer(
            p("A leader is rarely paid to choose the perfect answer in a vacuum. They are paid to "
              "make visible trade-offs: speed versus certainty, convenience versus fraud control, "
              "centralisation versus local regulation, cloud elasticity versus exit risk, hard "
              "finality versus customer recourse, low cost versus rich data, automation versus "
              "human judgement. Section 7 gives you the decision muscles. In a design review, do "
              "not ask ‘is this modern?’ Ask ‘what promise are we making, what risk are we accepting, "
              "what evidence will prove we are still inside tolerance, and who owns the failure?’")
        )
        + H3("7.1  The leader's decision equation")
        + p("Every transaction decision has five variables. The first is customer promise: what "
            "does the user believe will happen, and by when? The second is money risk: how much "
            "value can be lost, duplicated, delayed or stolen? The third is regulatory risk: what "
            "law, scheme rule or supervisory expectation is touched? The fourth is operational "
            "risk: can the bank run, reconcile and recover it every day? The fifth is economics: "
            "fees, liquidity, vendor cost, engineering cost and opportunity cost.")
        + mermaid(
            "flowchart LR\n"
            "  P[\"Customer promise\"] --> D[\"Decision\"]\n"
            "  M[\"Money risk\"] --> D\n"
            "  R[\"Regulatory risk\"] --> D\n"
            "  O[\"Operational risk\"] --> D\n"
            "  E[\"Economics\"] --> D\n"
            "  D --> C[\"Chosen design<br/>with explicit owner\"]\n"
            "  C --> EV[\"Evidence and monitoring\"]\n",
            "Figure 7.1 — A payment decision is a balance of promise, risk, operations and economics."
        )
        + example("Why ‘instant’ is not automatically better",
            p("A bank considers moving USD payroll for 80,000 employees from next-day Automated "
              "Clearing House to an instant rail. The customer promise improves: workers get money "
              "immediately. But the bank now needs 24×7 liquidity monitoring, stronger fraud controls, "
              "real-time exception handling, customer support outside business hours and a fallback "
              "if the instant rail or receiving bank is unavailable. Instant is better only if the "
              "operating model grows with the promise."))
        + H3("7.2  Decision matrix — the core trade-offs in transaction design")
        + table(
            ["Decision", "Option A", "Option B", "When A wins", "When B wins", "Questions a leader should ask"],
            [
                ["Synchronous vs asynchronous", "Synchronous request / response where the customer waits for final or near-final status.", "Asynchronous processing where the customer receives accepted / pending and final status later.", "Low-value instant payments, card authorisation, real-time balance checks.", "Bulk payroll, file-based corporate payments, long sanctions repair, cross-border chains.", "What exact status are we promising in the user interface: accepted, authorised, cleared, settled or credited?"],
                ["Real-time gross vs deferred net settlement", "Each payment settles individually in central-bank or prefunded money.", "Many payments are netted and settled in cycles.", "High-value systemic payments, treasury, urgent corporate flows.", "High-volume low-value retail and bulk flows where liquidity efficiency matters.", "What is the maximum daylight exposure, and who funds it if a participant fails?"],
                ["Push vs pull", "Payer initiates a credit transfer.", "Payee or merchant initiates debit under mandate or card credentials.", "One-off transfers, salary, supplier payment, account-to-account checkout.", "Subscriptions, EMIs, utilities, cards, direct debits.", "Where is consent captured, where is mandate evidence stored, and what dispute right exists?"],
                ["Hard finality vs reversible experience", "Once success is returned, reversal is exceptional and manual.", "Dispute, chargeback, refund or recall is part of the normal lifecycle.", "RTGS, high-value wires, some instant-payment flows where certainty matters.", "Cards, direct debits, consumer commerce and high-scam environments.", "Does the customer understand finality before pressing Pay, and what support path exists after harm?"],
                ["Centralised global platform vs local rails", "One global payment orchestration and control platform.", "Region-specific platforms or adapters optimised for local schemes.", "Common controls, analytics, reuse, global clients, consistent operations.", "Data localisation, local scheme complexity, latency, regulatory independence.", "Which parts can be global without violating local data, resilience or scheme expectations?"],
                ["Build vs buy vs scheme utility", "Build proprietary capability.", "Buy vendor platform or rely on scheme / market utility.", "Strategic differentiation, unique controls, large scale, integration ownership.", "Commodity capability, regulatory time pressure, proven scheme connectivity.", "Are we buying speed only, or also vendor concentration, exit and roadmap dependency?"],
                ["Cloud vs on-prem / private infrastructure", "Public cloud or cloud-native managed services.", "Bank data centre, private cloud or dedicated regulated hosting.", "Elastic peaks, faster provisioning, modern resilience tooling, analytics.", "Strict data residency, ultra-low latency to legacy rails, regulator or risk appetite constraints.", "Can we prove resilience, encryption, access control, exit and data residency for every copy of data?"],
                ["Automated decision vs human review", "System decides based on rules or model.", "Human analyst approves, repairs or escalates.", "High-volume low-risk decisions with measurable false-positive / false-negative rates.", "Sanctions hits, high-value exceptions, vulnerable-customer cases, ambiguous fraud.", "What is the cost of a false allow versus false block, and how do we evidence overrides?"],
                ["Fail open vs fail closed", "Continue processing when a control is unavailable.", "Stop or hold transactions when a control is unavailable.", "Low-risk non-money movement, degraded read-only services, pre-agreed fallback controls.", "Sanctions screening, ledger posting, high-value payments, authentication.", "Which customers are harmed by stopping, and which laws are breached by continuing?"],
                ["Rich data vs minimum data", "Collect and pass structured purpose, party, invoice and risk data.", "Collect only fields required to move money.", "ISO 20022, reconciliation, compliance analytics, corporate treasury.", "Privacy minimisation, low-friction retail UX, legacy constraints.", "Which downstream control breaks if we do not collect the field, and is the field lawful to collect?"],
            ]
        )
        + H3("7.3  Speed versus certainty — what does the green tick really mean?")
        + p("Customers read a green tick emotionally: the money is gone, the merchant is paid, the "
            "problem is solved. Systems use more precise states. Accepted means the request entered "
            "the system. Authorised means checks passed. Debited means the payer ledger posted. "
            "Cleared means interbank obligations were calculated. Settled means final money moved "
            "between banks. Credited means the beneficiary ledger posted. A good design labels the "
            "green tick according to the state actually reached.")
        + table(
            ["User wording", "Possible system state", "Risk if wording is careless", "Better design"],
            [
                ["Payment received", "Only request accepted by channel.", "Customer believes beneficiary has money when bank has not even authorised.", "Use ‘Payment request received’ until authorisation / posting completes."],
                ["Payment successful", "Payer debited but beneficiary confirmation pending.", "Merchant may release goods while credit can still fail.", "Show ‘Paid by you, awaiting receiver confirmation’ for uncertain rails."],
                ["Transfer complete", "Cleared but not settled.", "Treasury and reconciliation teams face breaks while customers assume finality.", "Reserve ‘complete’ for rail-defined final or credited state."],
                ["Refund issued", "Merchant initiated refund but acquirer / issuer settlement pending.", "Customer expects immediate balance restoration.", "Show expected timeline and status tracking."],
            ]
        )
        + example("A 5-second checkout with a 2-day dispute tail",
            p("A cardholder buys shoes for USD 120. Authorisation returns in two seconds, so the "
              "merchant ships. Clearing and settlement happen later, and the cardholder can still "
              "raise a dispute if the shoes never arrive. The customer experience is instant, but "
              "the risk lifecycle lasts weeks. That is why card platforms need evidence capture, "
              "merchant-risk monitoring and chargeback operations even though the checkout screen "
              "looks simple."))
        + H3("7.4  Liquidity versus customer experience")
        + p("Liquidity is the cash or central-bank balance the bank must have available to settle "
            "payments. Faster rails often move liquidity pressure from end-of-day treasury teams to "
            "always-on monitoring. Deferred net settlement is liquidity-efficient because many "
            "payments offset each other. Real-time gross settlement gives stronger finality but "
            "requires money to be available payment by payment. Prefunded instant rails require "
            "participants to park funds before customers spend them.")
        + table(
            ["Settlement model", "Customer experience", "Liquidity implication", "Leadership trade-off"],
            [
                ["Deferred net", "May feel instant or same-day depending on rail.", "Bank settles net position later, reducing gross funding need.", "Efficient but creates exposure until settlement and requires strong reconciliation."],
                ["Real-time gross", "Final high-value payment during operating window.", "Each payment needs available central-bank money immediately.", "Certainty and systemic safety at higher liquidity cost."],
                ["Prefunded instant", "24×7 instant customer experience.", "Funds sit in prefunded account or arrangement before use.", "Always-on experience but idle liquidity and weekend / holiday forecasting matter."],
                ["Correspondent chain", "Cross-border status may improve through tracking but value can move through multiple accounts.", "Nostro balances and FX timing create treasury cost.", "Global reach with settlement, sanctions and fee opacity trade-offs."],
            ]
        )
        + example("Prefunding with simple numbers",
            p("A bank's instant rail sees normal Sunday volume of USD 40 million but festival-season "
              "Sunday volume can hit USD 95 million. If the bank prefunds only USD 50 million, "
              "customers may see declines even though the bank is solvent. If it prefunds USD 120 "
              "million every weekend, unused liquidity has opportunity cost. The right answer needs "
              "forecasting, intraday top-up rules, alerts, treasury ownership and fallback messaging."))
        + H3("7.5  Fraud friction versus conversion")
        + p("Every extra fraud control has two effects. It catches some bad transactions and blocks "
            "or annoys some good customers. Removing friction improves conversion but can increase "
            "scams and reimbursement losses. Adding friction reduces fraud but can lose customers, "
            "break accessibility and push users to competitors. Mature banks do not argue ‘more "
            "friction’ or ‘less friction’ abstractly. They segment by risk.")
        + table(
            ["Transaction context", "Low-friction choice", "High-control choice", "Balanced leader decision"],
            [
                ["Known device, known payee, ₹500 grocery UPI", "Fast biometric or PIN flow.", "Manual review would be absurd.", "Keep friction low, monitor anomaly signals in background."],
                ["New payee, £9,500 first-time transfer", "One-click payment improves speed.", "Confirmation of Payee, scam warning, cooling-off or step-up check.", "Use targeted friction because scam harm and reimbursement exposure are high."],
                ["Corporate payroll file to 5,000 employees", "Upload and release immediately.", "Maker-checker, file totals, beneficiary-change checks, cut-off controls.", "Automate validation but require dual approval and exception reporting."],
                ["Recurring streaming subscription", "Stored credential with low-friction renewal.", "Repeated Strong Customer Authentication every month.", "Use mandate / credential-on-file rules and risk-based step-up on anomalies."],
            ]
        )
        + red_flag(
            p("If a product team says ‘fraud checks are killing conversion’ but cannot quantify "
              "fraud loss, false positives, abandonment, reimbursement cost and vulnerable-customer "
              "harm separately, push back. Averages hide the decision. Segment by customer, device, "
              "beneficiary, amount, geography and behaviour."))
        + H3("7.6  Central platform versus local regulation")
        + p("Global banks want central platforms because reuse is powerful. One payment hub, one "
            "fraud platform, one sanctions engine and one data lake sound efficient. Regulators and "
            "schemes often pull in the other direction: local data residency, local incident reporting, "
            "domestic rail certification, local language complaints, domestic outsourcing approval "
            "and country-specific customer-protection rules. The leadership job is to separate what "
            "can be global from what must remain local.")
        + table(
            ["Capability", "Good candidate for global reuse", "Often needs local variation", "Reason"],
            [
                ["Payment orchestration core", "Common workflow engine, idempotency, status model, audit pattern.", "Rail adapters, cut-offs, limits, scheme status codes.", "Rail rules differ even when the business concepts repeat."],
                ["Sanctions screening", "Common engine, list management, case workflow.", "Local list sources, thresholds, language handling, reporting.", "OFAC, UK OFSI, EU, UN, MAS and domestic lists overlap but are not identical."],
                ["Fraud models", "Feature platform, model governance, monitoring.", "Local typologies, reimbursement rules, data availability.", "PIX scam patterns, UK APP fraud and card-not-present fraud need different signals."],
                ["Data platform", "Common metadata, lineage, analytics tooling.", "Residency, masking, retention and access rules.", "Data copies trigger privacy and localisation obligations."],
                ["Operations", "Common playbooks and severity taxonomy.", "Regulator contacts, reporting clocks, language and market hours.", "Incident response is global in coordination but local in obligation."],
            ]
        )
        + H3("7.7  Build, buy or use the rail utility")
        + p("Build means the bank writes and owns the capability. Buy means a vendor provides "
            "software or service. Use-the-utility means the bank relies on scheme, clearing-house "
            "or market infrastructure where the shared network already exists. The wrong way to "
            "choose is by fashion. The right way is by strategic differentiation, regulatory urgency, "
            "scale, integration complexity, exit risk, data control and run cost.")
        + table(
            ["Question", "Build points", "Buy points", "Use utility points"],
            [
                ["Is this differentiating?", "Unique corporate treasury experience, proprietary risk engine.", "Standard case management or payment operations tooling.", "Domestic clearing, settlement and proxy directory where network effect matters."],
                ["How fast is the deadline?", "Slow if building from scratch unless capability already exists.", "Faster if vendor is certified and integration is manageable.", "Fast for network reach if bank can meet scheme onboarding requirements."],
                ["Who owns regulatory change?", "Bank owns full interpretation and implementation.", "Vendor may deliver updates but bank remains accountable.", "Scheme utility updates rulebook, bank adapts participant systems."],
                ["What is exit risk?", "Lower vendor dependency but higher internal key-person risk.", "Contract, data export and roadmap dependency.", "Cannot exit core market rail without exiting the market use case."],
                ["What does scale cost?", "Engineering and operations scale directly with bank choices.", "Licence, transaction and professional-service cost.", "Scheme fees, settlement funding and participant obligations."],
            ]
        )
        + example("Vendor choice for ISO 20022 migration",
            p("A mid-sized bank has 18 months to migrate cross-border messaging to ISO 20022. Building "
              "a full translator, validation engine, repair queue, testing harness and SWIFT gateway "
              "integration may give control but risks missing deadline. Buying a proven payment hub "
              "or message transformation layer may reduce delivery risk but creates vendor dependency "
              "and mapping constraints. The leader should ask: which payment flows are genuinely "
              "differentiating, which are compliance deadlines, and how will we exit or replace the "
              "vendor if pricing or roadmap becomes unacceptable?"))
        + H3("7.8  Cloud decision — elasticity is not the whole answer")
        + p("Cloud can be excellent for transaction systems: elastic capacity, automated deployment, "
            "managed resilience, observability, security tooling and faster environment creation. "
            "But BFSI cloud decisions must also answer data residency, encryption-key control, "
            "privileged access, concentration risk, service outage, regulator access, exit plan, "
            "latency to rails and compatibility with legacy host systems. The decision is not "
            "‘cloud good’ or ‘cloud bad’. It is which workload, which data, which region, which "
            "controls and which fallback.")
        + table(
            ["Workload", "Cloud-friendly factors", "Caution factors", "Typical decision shape"],
            [
                ["Customer mobile channel", "Elastic peaks, content delivery, security telemetry.", "Authentication dependency, data exposure, incident reporting.", "Cloud front end with strong identity, rate limiting, observability and regional failover."],
                ["Payment orchestration", "Horizontal scaling, event processing, DevSecOps speed.", "Exactly-once semantics illusion, rail connectivity, idempotency and resilience.", "Cloud-native if ledger safety, connectivity and failover are proven."],
                ["Core ledger posting", "Modern cores may run cloud-native.", "Latency, regulator comfort, data residency, migration blast radius.", "Careful phased migration, often product by product or ledger segment by segment."],
                ["Analytics and fraud modelling", "Large-scale compute and machine learning tooling.", "Sensitive data copies, model governance, privacy.", "Masked / tokenised data lake with strict access and residency controls."],
                ["HSM and key management", "Managed key services can reduce operational burden.", "Key custody, certification, payment-network rules.", "Hybrid model with Hardware Security Module requirements reviewed by security and schemes."],
            ]
        )
        + H3("7.9  Automation versus human judgement")
        + p("Automation is essential because payment volume is too large for manual review. Human "
            "judgement is essential because some decisions carry legal, ethical, vulnerable-customer "
            "or sanctions consequences that require context. The bad pattern is pretending one can "
            "replace the other entirely. The good pattern is tiering: automate routine clean flows, "
            "route ambiguous cases to skilled review, and continuously learn from outcomes.")
        + table(
            ["Decision type", "Automate when", "Use human review when", "Evidence to preserve"],
            [
                ["Low-risk payment approval", "Known customer, known beneficiary, normal amount and device.", "Signals conflict or customer appears vulnerable.", "Rule result, risk score, input features and final status."],
                ["Sanctions alert", "Clear false positive with strong deterministic evidence.", "Close name match, high-risk geography, vessel / company ownership complexity.", "List version, match logic, analyst rationale and approval."],
                ["Fraud reimbursement", "Simple policy case with complete evidence.", "Scam, coercion, vulnerable customer or disputed warning effectiveness.", "Customer communications, warnings shown, device data and decision rationale."],
                ["Payment repair", "Formatting correction is mechanical and low-risk.", "Beneficiary identity, purpose or amount ambiguity.", "Original message, repair change, approver and customer instruction."],
            ]
        )
        + H3("7.10  A practical review checklist for any transaction decision")
        + ol([
            "<strong>Name the promise.</strong> What exactly does the customer, merchant, corporate treasurer or regulator believe will happen?",
            "<strong>Name the state.</strong> Is the system saying accepted, authenticated, authorised, debited, cleared, settled, credited, failed, reversed or disputed?",
            "<strong>Name the rail rule.</strong> Which scheme, central bank, payment-system or card-network rule defines the lifecycle?",
            "<strong>Name the money at risk.</strong> What is the maximum single-transaction, daily, participant and outage exposure?",
            "<strong>Name the data boundary.</strong> Which fields cross country, vendor, environment and analytics boundaries?",
            "<strong>Name the control owner.</strong> Who owns authentication, fraud, sanctions, limits, reconciliation, liquidity and customer complaints?",
            "<strong>Name the failure mode.</strong> What happens if the rail, vendor, cloud region, sanctions engine, ledger, notification service or reconciliation file fails?",
            "<strong>Name the evidence.</strong> Six months later, what log, report, case note or ledger record proves the bank behaved correctly?",
            "<strong>Name the exit.</strong> If the vendor, rail adapter or cloud region becomes unacceptable, how does the bank move without customer harm?",
            "<strong>Name the decision owner.</strong> Which executive accepts the residual risk after controls and trade-offs are visible?",
        ])
        + callout("End-of-section recap",
            ul([
                "Leadership decisions in transaction systems are trade-offs, not technology beauty contests.",
                "Speed, finality, liquidity, fraud friction, customer protection, data residency and vendor dependency pull against one another.",
                "The user-interface status must match the actual payment lifecycle state.",
                "Cloud, vendor and automation choices are valid only when accountability, evidence, resilience and exit are designed.",
                "A strong review names the promise, state, rule, money risk, data boundary, control owner, failure mode, evidence, exit and accountable executive.",
            ]),
            "info")
    )
    return TopicSection("7.  Trade-offs and decisions a leader owns", "intermediate", body)


def _sec8() -> TopicSection:
    body = (
        primer(
            p("Sections 0 through 7 gave you the map. Section 8 now makes you use it. Each worked "
              "example follows one real transaction from customer intent to ledger posting, clearing, "
              "settlement, reconciliation and leadership decision. Do not read these as scripts to "
              "memorise. Read them as drills. In every drill, pause and ask: what state is the "
              "transaction in, what money is at risk, what evidence exists, and what decision would "
              "a senior leader have to own if the happy path breaks?")
        )
        + H3("8.1  The common frame for every worked example")
        + p("A worked transaction example is useful only if it separates the customer story from "
            "the bank story. The customer sees one sentence: ‘paid’, ‘salary received’, ‘wire sent’, "
            "‘refund pending’. The bank sees many states, many ledgers and many controls. The "
            "discipline is to keep both views visible at the same time.")
        + table(
            ["Lens", "Plain-English question", "What to calculate", "Evidence you should expect"],
            [
                ["Customer promise", "What does the user believe has happened?", "Elapsed time, wording shown, reversal rights and support path.", "Screen copy, notification, terms, complaint script."],
                ["Ledger state", "Which book has actually changed?", "Debit amount, credit amount, fees, tax, FX, suspense and general ledger entries.", "Journal IDs, posting timestamp, balance-before and balance-after."],
                ["Rail state", "Where is the payment in the scheme lifecycle?", "Accepted, authorised, cleared, settled, rejected, returned, recalled or disputed.", "Scheme message, status code, settlement file, return reason."],
                ["Risk state", "What can still go wrong?", "Fraud loss, liquidity gap, sanctions hold, customer harm, reconciliation break.", "Risk score, screening result, liquidity dashboard, exception queue."],
                ["Owner decision", "Who accepts the residual risk?", "Limit, fallback, manual review, customer communication and compensation threshold.", "Decision record, runbook, approval, audit trail."],
            ]
        )
        + mermaid(
            "flowchart LR\n"
            "  A[\"Customer action\"] --> B[\"Bank promise\"]\n"
            "  B --> C[\"Ledger impact\"]\n"
            "  C --> D[\"Rail lifecycle\"]\n"
            "  D --> E[\"Risk and controls\"]\n"
            "  E --> F[\"Evidence and owner\"]\n"
            "  F --> G[\"Customer support story\"]\n",
            "Figure 8.1 — Every worked example is read through promise, ledger, rail, risk, evidence and support."
        )
        + H3("8.2  India — ₹750 UPI QR payment at a kirana store")
        + p("Start with the most familiar payment: a customer buys groceries worth ₹750 at a local "
            "kirana store. The merchant has an account with Bank B. The customer has an account with "
            "Bank A and uses a third-party app. Everyone in the shop wants the whole thing to feel "
            "like cash: scan, PIN, beep, leave. But because there is no physical cash, the system must "
            "create equivalent confidence through messages, controls and ledger entries.")
        + example("Happy path with balances and ledger entries",
            ol([
                "<strong>Before payment.</strong> Priya's Bank A savings account available balance is ₹18,250. Ramesh Stores' Bank B current account available balance is ₹42,300.",
                "<strong>Initiation.</strong> Priya scans the static QR. The app reads a payee handle such as <code>rameshstores@bankb</code>, merchant name, merchant category and currency INR. Priya enters ₹750.",
                "<strong>Authentication.</strong> Priya enters her UPI Personal Identification Number. The app does not send the plain PIN to the bank. It sends a protected proof through the approved UPI library and secure channel.",
                "<strong>Authorisation.</strong> Bank A checks four simple facts: Priya is active, the PIN proof is valid, ₹750 is within her per-transaction and daily limit, and ₹18,250 is enough balance.",
                "<strong>Debit posting.</strong> Bank A posts a debit of ₹750. Priya's available balance becomes ₹17,500. The debit journal references the UPI transaction identifier so a retry cannot create a second debit for the same instruction.",
                "<strong>Credit posting.</strong> Bank B receives the credit instruction and posts ₹750 to Ramesh Stores. The merchant available balance becomes ₹43,050.",
                "<strong>Customer notification.</strong> Priya sees ‘Payment successful ₹750’. Ramesh hears the merchant app beep. That message should mean both customer-facing ledger postings have completed, not merely that the request was accepted.",
                "<strong>Settlement later.</strong> Across the day, National Payments Corporation of India calculates Bank A's and Bank B's net UPI obligations. Actual interbank settlement happens through Reserve Bank of India accounts in settlement cycles.",
            ]))
        + table(
            ["Entry", "Priya Bank A ledger", "Ramesh Bank B ledger", "Interbank position"],
            [
                ["Before", "Priya available ₹18,250", "Ramesh available ₹42,300", "No new obligation."],
                ["After customer success", "Priya available ₹17,500, debit journal ₹750", "Ramesh available ₹43,050, credit journal ₹750", "Bank A owes Bank B ₹750 until net settlement."],
                ["After settlement cycle", "No change to Priya", "No change to Ramesh", "Bank A and Bank B net obligations settled at RBI after offsetting all bilateral / multilateral flows."],
            ]
        )
        + H3("8.3  India failure branch — customer debited, merchant says not received")
        + p("The most important teaching case is not the happy path. It is the uncomfortable sentence "
            "every payments operations team hears: ‘money left my account but the merchant says it "
            "did not arrive’. This can happen because a notification is delayed, the credit posting "
            "failed, a timeout hid the final status, or reconciliation files disagree. A leader must "
            "not guess. They must ask where the transaction stopped.")
        + example("A disputed ₹750 UPI transaction",
            ol([
                "<strong>10:00:00.</strong> Priya presses Pay. Bank A debits ₹750 and returns success to the switch.",
                "<strong>10:00:02.</strong> The message to Bank B times out. Priya's app receives an ambiguous response and shows ‘processing’ for 30 seconds.",
                "<strong>10:00:35.</strong> Priya receives a debit SMS. Ramesh's app has no beep. The store asks Priya to pay again in cash.",
                "<strong>Operations check.</strong> The bank must compare four records: Bank A debit journal, switch transaction status, Bank B credit journal and settlement / dispute file.",
                "<strong>If Bank B later credited.</strong> The customer communication is ‘merchant was credited at 10:01, here is reference ID’. No refund is due, but the notification failure still needs defect tracking.",
                "<strong>If Bank B never credited.</strong> Bank A must reverse Priya or trigger the scheme dispute process within the required timeline. The reversal journal must link to the original transaction ID, not look like a fresh credit.",
                "<strong>If both debit and credit exist but settlement disagrees.</strong> This is a reconciliation break. Customer support should not invent an answer until settlement operations identify the break.",
            ]))
        + red_flag(
            p("If the team says ‘the customer can just retry’, push back. Retrying is safe only when "
              "the original transaction has a stable idempotency key and a reliable final-status "
              "lookup. Without that, the second attempt may duplicate the payment and move the "
              "problem from customer support to financial loss."))
        + H3("8.4  United States — USD 850,000 corporate Fedwire supplier payment")
        + p("Now move from a ₹750 retail payment to a high-value US dollar corporate payment. A "
            "treasury team at a global bank client needs to pay a technology vendor USD 850,000 by "
            "same-day final wire. The customer promise is not ‘cheap and convenient’. The promise is "
            "finality: once the wire is released and settled, the beneficiary bank can rely on it.")
        + example("Fedwire-style high-value payment with controls",
            ol([
                "<strong>Customer instruction.</strong> A corporate treasurer enters USD 850,000 to Vendor LLC, routing number 021000021, account number ending 4472, purpose ‘software licence renewal’.",
                "<strong>Maker-checker approval.</strong> The company's policy requires one maker and two approvers above USD 500,000. The bank portal records who entered, who approved and from which device / network.",
                "<strong>Limit check.</strong> The corporate has a daily wire limit of USD 2 million. Earlier wires today total USD 600,000, so after this wire the used limit would be USD 1.45 million. The payment is within limit.",
                "<strong>Sanctions and fraud check.</strong> The originator, beneficiary, beneficiary bank and free-text fields are screened. A close name match produces a case only if the score crosses the bank threshold. Clear false positives must still preserve list version and match rationale.",
                "<strong>Liquidity check.</strong> The bank confirms it has enough Federal Reserve master-account balance or intraday credit capacity. This is not a customer-balance question only. It is a bank-treasury question.",
                "<strong>Settlement.</strong> Fedwire is real-time gross settlement. The sending bank's Federal Reserve balance is debited and the receiving bank's Federal Reserve balance is credited payment by payment.",
                "<strong>Finality.</strong> Once settled, the wire is final under the rail rules. A recall request is possible operationally, but the receiving bank and beneficiary are not in the same position as a card chargeback.",
            ]))
        + table(
            ["Decision", "Wrong junior answer", "Leader answer"],
            [
                ["Can we send it over a cheaper batch rail?", "Yes, ACH is cheaper.", "Maybe, but only if same-day finality is not required and return risk is acceptable."],
                ["Can support reverse it if the account number is wrong?", "Raise a ticket and reverse.", "A wire recall depends on receiving-bank cooperation. Prevention and verification matter more than after-the-fact reversal."],
                ["Is customer balance enough?", "Yes, the corporate has funds.", "Also check bank settlement liquidity, intraday credit, cut-off, sanctions status and approval evidence."],
                ["What does success mean?", "The portal says sent.", "Success should identify whether the wire is accepted, released, settled by Fedwire, or credited by the beneficiary bank."],
            ]
        )
        + H3("8.5  United Kingdom — £9,500 Faster Payments transfer with scam risk")
        + p("The United Kingdom is a good lesson because payment speed, name-checking and scam "
            "reimbursement now sit in the same leadership decision. Imagine Asha wants to transfer "
            "£9,500 as a deposit for a second-hand car. The beneficiary is new. The payment is "
            "domestic, fast and customer-initiated. The obvious product instinct is to make it "
            "instant. The risk instinct is to ask whether Asha is being manipulated.")
        + example("APP fraud-sensitive Faster Payments journey",
            ol([
                "<strong>Beneficiary setup.</strong> Asha enters sort code, account number and name ‘Green Motors Ltd’. Confirmation of Payee returns ‘close match’ because the receiving account is actually ‘G Motors Trading’.",
                "<strong>Customer warning.</strong> The bank shows a specific warning: the name does not fully match, the payee is new, the amount is high relative to Asha's normal behaviour, and car-purchase scams are common.",
                "<strong>Risk score.</strong> Asha normally sends under £300. She is on a new device, at 22:40, to a new payee, for £9,500. The model routes the payment to step-up confirmation or temporary hold depending on policy.",
                "<strong>Customer decision.</strong> If Asha ignores warnings and proceeds, the bank still needs evidence of what warning was shown, in what wording, and whether accessibility needs were considered.",
                "<strong>Rail movement.</strong> Faster Payments can credit the receiving bank in seconds, with settlement through Bank of England arrangements. Speed increases the need to stop harm before release.",
                "<strong>Post-event handling.</strong> If Asha reports a scam, the bank must investigate under the UK reimbursement framework, checking customer vulnerability, effective warning, gross negligence standard where applicable and receiving-bank responsibilities.",
            ]))
        + callout("Leadership decision in this example",
            p("The decision is not ‘block all risky payments’ or ‘let customers do what they want’. "
              "The decision is targeted friction. For a £9,500 new-payee transfer with a name "
              "mismatch, friction is not bad user experience. It is part of the product promise: "
              "fast payments without abandoning customers to authorised push payment fraud."),
            "info")
        + H3("8.6  Eurozone — €120,000 SEPA Instant supplier payment and liquidity")
        + p("A Eurozone corporate wants to pay a supplier €120,000 urgently. The corporate expects "
            "near-real-time confirmation. The bank wants to use SEPA Instant Credit Transfer and a "
            "settlement path such as TARGET Instant Payment Settlement or another instant clearing "
            "and settlement mechanism. The invisible constraint is liquidity: instant rails need "
            "money ready when customers act, including nights, weekends and public holidays.")
        + example("Instant euro payment with prefunding and sanctions timing",
            ol([
                "<strong>Customer file.</strong> The corporate submits an ISO 20022 <code>pain.001</code> instruction at 23:15 on a Friday for €120,000.",
                "<strong>Translation.</strong> The bank converts customer initiation into interbank credit-transfer messaging such as <code>pacs.008</code>, preserving structured remittance data and legal-entity details.",
                "<strong>Sanctions screening.</strong> Screening must complete fast enough for the instant promise, but not so loosely that EU, national or United Nations restrictions are missed. A real hit must stop the payment even if the customer expected ten seconds.",
                "<strong>Liquidity position.</strong> The bank has €8 million in its instant settlement account. Forecast weekend outgoing volume is €6.5 million, incoming volume is €4.2 million, and a large corporate batch may add €3 million. The €120,000 payment is individually small for treasury but meaningful in aggregate.",
                "<strong>Settlement.</strong> If the rail uses central-bank money, the sending participant's instant settlement balance decreases and the receiving participant's balance increases immediately.",
                "<strong>Reconciliation.</strong> On Monday, the bank must prove customer ledger, instant-settlement account, scheme reports and general ledger all agree. A ten-second payment still needs a multi-day evidence trail.",
            ]))
        + table(
            ["Number", "Calculation", "Why it matters"],
            [
                ["Weekend opening balance", "€8.0 million available for instant settlement.", "Treasury starts with a finite pot, not an abstract promise."],
                ["Expected net outflow", "€6.5 million outgoing minus €4.2 million incoming equals €2.3 million net outflow.", "Normal forecast leaves €5.7 million after weekend netting if no surprises occur."],
                ["Stress batch", "Extra €3.0 million corporate batch reduces projected balance to €2.7 million.", "The bank remains funded, but alert thresholds may trigger before hard failure."],
                ["Single payment", "€120,000 consumes 1.5% of opening balance and 4.4% of stressed remaining balance.", "One payment is manageable, but many urgent corporates can create liquidity bunching."],
            ]
        )
        + H3("8.7  Singapore — SGD 2.4 million payroll via FAST / PayNow proxies")
        + p("Singapore is useful because it combines modern real-time rails with strong technology "
            "risk expectations. Imagine a fintech payroll provider sends salary payouts for 1,200 "
            "workers. Total value is SGD 2.4 million. The average salary is SGD 2,000, but the file "
            "contains varied amounts and proxy identifiers such as mobile numbers or Unique Entity "
            "Numbers routed through PayNow over FAST.")
        + example("Bulk payroll that customers experience as many small instant credits",
            ol([
                "<strong>File control.</strong> The payroll provider uploads 1,200 records with a declared control total of SGD 2,400,000. The bank independently recalculates count and amount before release.",
                "<strong>Proxy resolution.</strong> PayNow-style proxy lookup maps each mobile number or entity number to a receiving bank account. Failed proxy matches go to exception handling before money moves.",
                "<strong>Sanctions and mule checks.</strong> Even domestic salary payments need screening and mule-account controls. A payment to a newly opened account with unusual inbound pattern may be held for review.",
                "<strong>Rail release.</strong> Clean items are sent over the instant rail. Employees see credits quickly, but the corporate file is still managed as one business obligation with many child transactions.",
                "<strong>Partial failure.</strong> Suppose 1,196 records succeed, 3 fail proxy validation and 1 is held for fraud review. The customer dashboard must not simply say ‘payroll failed’. It should show SGD 2,392,000 paid, SGD 6,000 invalid proxy, SGD 2,000 under review.",
                "<strong>Audit evidence.</strong> The bank preserves original file hash, approval record, item-level statuses, exception reasons, release times and final reconciliation. This matters under Monetary Authority of Singapore technology-risk and operational-resilience expectations.",
            ]))
        + table(
            ["Status bucket", "Count", "Amount", "Customer communication", "Operations owner"],
            [
                ["Successful credits", "1,196", "SGD 2,392,000", "Employees credited, item references available.", "Payments operations and reconciliation."],
                ["Invalid proxy", "3", "SGD 6,000", "Employer must correct mobile / Unique Entity Number mapping.", "Corporate support and master-data team."],
                ["Fraud review hold", "1", "SGD 2,000", "Payment under review, do not re-submit until final status.", "Fraud operations with service-level timer."],
                ["File total", "1,200", "SGD 2,400,000", "Dashboard reconciles count and amount across all states.", "Corporate channel owner."],
            ]
        )
        + H3("8.8  Cross-border — USD 50,000 India to Hong Kong supplier payment")
        + p("Cross-border payments teach the difference between instruction, FX conversion, "
            "correspondent accounts and final beneficiary credit. A Mumbai importer pays a Hong Kong "
            "supplier USD 50,000. The Indian customer thinks ‘I sent dollars’. The bank thinks "
            "through rupee debit, foreign-exchange rate, nostro funding, sanctions screening, SWIFT "
            "message, correspondent fees, time zones and beneficiary-bank credit.")
        + example("Cross-border decision with FX, fees and settlement uncertainty",
            ol([
                "<strong>Customer quote.</strong> The importer requests USD 50,000. The bank quotes ₹83.40 per USD plus ₹2,000 fee and applicable tax / charges. Customer rupee debit before tax is ₹41,72,000: ₹41,70,000 for FX plus ₹2,000 fee.",
                "<strong>Compliance checks.</strong> The bank checks purpose code, invoice, importer documentation, sanctions lists, anti-money-laundering profile and any country / goods restrictions.",
                "<strong>Message construction.</strong> The payment instruction carries ordering customer, beneficiary, beneficiary bank, charges option, remittance details and regulatory reporting fields. Under ISO 20022 migration, preserving structured party data improves screening and repair.",
                "<strong>Nostro impact.</strong> The sending bank's USD nostro account is debited by USD 50,000 plus any correspondent charge depending on fee arrangement. If the bank's nostro was underfunded, the customer promise could fail despite rupee debit being successful.",
                "<strong>Beneficiary credit.</strong> The Hong Kong supplier may receive USD 50,000, or a lower amount if charges are deducted en route under shared / beneficiary charge rules. If the supplier expected full value, the wrong charge option becomes a business dispute.",
                "<strong>Status tracking.</strong> SWIFT gpi-style tracking can show timestamps, but tracking is not the same as settlement finality in every account. The leader must know what the status actually proves.",
            ]))
        + table(
            ["Item", "Amount", "Who cares", "Decision question"],
            [
                ["Customer FX debit", "USD 50,000 × ₹83.40 = ₹41,70,000", "Importer treasury.", "Was the FX rate locked, indicative or refreshed at release?"],
                ["Bank fee", "₹2,000 plus taxes / charges if applicable.", "Importer and bank revenue.", "Was the fee disclosed before authorisation?"],
                ["Correspondent charge", "Could be zero to customer, shared, or deducted en route.", "Supplier and relationship manager.", "Is the charges code OUR, SHA or BEN, and does it match contract expectation?"],
                ["Nostro usage", "USD 50,000 principal plus charge handling.", "Bank treasury.", "Is the nostro funded for time-zone and cut-off constraints?"],
            ]
        )
        + H3("8.9  What these examples should train you to notice")
        + callout("Pattern recap",
            ul([
                "Small retail and large wholesale payments use the same skeleton: authenticate, authorise, validate, route, clear, settle, notify and reconcile.",
                "The phrase ‘successful’ is dangerous until you know whether it refers to request acceptance, ledger debit, beneficiary credit, clearing, settlement or dispute closure.",
                "Liquidity is invisible to customers but decisive for real-time gross, prefunded and cross-border payments.",
                "Fraud friction is not always bad design. In scam-sensitive journeys, the absence of friction can be the defect.",
                "Bulk files need item-level truth. A payroll file can be partly successful, partly invalid and partly under review at the same time.",
                "Cross-border payments are not just messages. They are instructions plus FX, correspondent balances, fees, time zones, sanctions and regulatory reporting.",
            ]),
            "info")
    )
    return TopicSection("8.  Worked examples — numbers and decisions", "intermediate", body)


def _sec9() -> TopicSection:
    body = (
        primer(
            p("Section 9 is your meeting-room tool. When you sit in a design review, programme "
              "steering committee, vendor demo, migration checkpoint or incident review, you do "
              "not need to sound technical by naming every product. You need to ask questions that "
              "force the real design into the open. A strong question does three things: it names "
              "the customer promise, it names the state of money, and it asks what evidence will "
              "prove the promise was kept.")
        )
        + H3("9.1  How to use this question bank")
        + p("Do not ask all questions in every meeting. Choose the relevant block. For a new mobile "
            "payment journey, start with customer promise, authentication, fraud and status wording. "
            "For a payment-hub migration, start with ledger state, idempotency, reconciliation, "
            "cut-over and rollback. For a regulator-facing review, start with data, outsourcing, "
            "incident clocks, evidence and accountability.")
        + table(
            ["Meeting type", "Start with these questions", "Proof you should ask to see"],
            [
                ["New payment product", "Promise, rail, limits, customer status, fraud friction, dispute path.", "Journey screenshots, rulebook extract, control matrix, test cases."],
                ["Payment-engine migration", "State model, idempotency, ledger parity, reconciliation, cut-over, rollback.", "Parallel-run report, data-mapping evidence, exception ageing, rollback rehearsal."],
                ["Cloud / vendor review", "Data location, resilience, privileged access, exit, concentration risk.", "Architecture diagram, outsourcing assessment, recovery test, exit plan."],
                ["Incident review", "Customer harm, stuck states, duplicate risk, settlement impact, regulator clock.", "Timeline, affected transaction list, root-cause analysis, customer remediation file."],
                ["Executive steering", "Residual risk, money at risk, timeline realism, owner, decision needed.", "Decision log, risk acceptance, dependency map, burn-down of open controls."],
            ]
        )
        + H3("9.2  Customer promise and user-interface status")
        + ol([
            "<strong>What exactly are we promising on screen?</strong> Are we saying request received, payment processing, authorised, debited, credited, settled, refunded or disputed?",
            "<strong>Does the wording match the rail state?</strong> If the rail only confirms acceptance, why does the screen say complete?",
            "<strong>What does the customer do when the state is ambiguous?</strong> Do we tell them not to retry, show a reference ID and provide a final-status lookup?",
            "<strong>What is the worst customer harm if the message is wrong?</strong> Could a merchant release goods, a salary earner miss rent, or a vulnerable customer be scammed?",
            "<strong>Are limits visible before failure?</strong> Does the user learn about per-transaction, daily, beneficiary or rail limits before entering all details?",
            "<strong>Is the support script consistent with the system state model?</strong> Customer support should not call a payment settled when operations sees only accepted.",
            "<strong>What notifications are mandatory?</strong> SMS, email, push notification, merchant beep and corporate file reports may have different clocks and legal value.",
            "<strong>How do refunds, reversals, recalls and disputes differ in the customer journey?</strong> These are not synonyms and should not share one generic ‘reverse payment’ label.",
            "<strong>What evidence is shown to the customer?</strong> Reference number, beneficiary name, amount, timestamp, fee, FX rate and expected completion time should be clear.",
            "<strong>Have accessibility and language needs been tested?</strong> A fraud warning that a vulnerable or screen-reader user cannot understand is not a real control.",
        ])
        + H3("9.3  Money movement, ledgers and settlement")
        + ol([
            "<strong>Which ledger is the system of record for this transaction?</strong> Channel database, payment hub, core ledger, card ledger, wallet ledger and general ledger cannot all be treated as truth.",
            "<strong>What are the exact debit and credit entries?</strong> Show balance before, balance after, fee, tax, FX, suspense and settlement-account postings.",
            "<strong>When does available balance change versus booked balance?</strong> Card authorisation holds, pending credits and settlement postings may affect these differently.",
            "<strong>Where is the transaction identifier generated?</strong> The identifier must survive channel retry, payment-hub processing, ledger posting, scheme messages and reconciliation.",
            "<strong>What prevents duplicate money movement on retry?</strong> Where is the idempotency key stored, for how long, and what response is returned for a duplicate request?",
            "<strong>What happens if debit succeeds and credit fails?</strong> Is there reversal, suspense, repair, scheme dispute or manual queue, and who owns ageing?",
            "<strong>What happens if the rail succeeds and our internal posting fails?</strong> A scheme-success / ledger-failure mismatch is a serious operational break.",
            "<strong>Is settlement gross, net, prefunded or correspondent-based?</strong> The liquidity, finality and failure model changes completely.",
            "<strong>What is the maximum exposure before settlement?</strong> Calculate single transaction, customer, participant, bilateral, net-cycle and outage exposure.",
            "<strong>How are fees and FX handled?</strong> Is the rate locked, refreshed, marked up, disclosed and reconciled to treasury and revenue systems?",
            "<strong>How does the general ledger receive truth?</strong> Is finance relying on batch files, event streams, manual journals or reconciled settlement reports?",
            "<strong>How long can an item sit in suspense?</strong> Ageing thresholds, escalation owners and write-off approvals should be defined before go-live.",
        ])
        + H3("9.4  Rail, scheme and message design")
        + ol([
            "<strong>Which exact rail is used?</strong> UPI, IMPS, NEFT, RTGS, ACH, Fedwire, RTP, FedNow, Faster Payments, BACS, CHAPS, SEPA Credit Transfer, SEPA Instant, FAST, PayNow, card or SWIFT are different promises.",
            "<strong>What rulebook defines finality?</strong> Do not rely on vendor wording. Find the scheme or central-bank rule that defines when obligations become final.",
            "<strong>What are the cut-offs, operating hours and holiday rules?</strong> A 24×7 channel over a business-hours rail creates pending states that must be explained.",
            "<strong>What message format is native?</strong> Are we using ISO 20022, legacy SWIFT MT, card ISO 8583, domestic scheme XML / JSON, or a proprietary vendor format?",
            "<strong>What data is lost in translation?</strong> Mapping rich ISO 20022 fields into legacy fields can lose purpose, party, address and remittance detail needed for compliance and reconciliation.",
            "<strong>What status codes can come back?</strong> List success, reject, pending, timeout, duplicate, returned, recalled, repair and investigation statuses, then map each to customer and operations action.",
            "<strong>What rail limits apply?</strong> Per-transaction, daily, monthly, merchant-category, new-beneficiary, account-type and scheme-participant limits should be explicit.",
            "<strong>What certification or scheme testing is required?</strong> Domestic rail changes often need scheme test packs, production proving and operational sign-off.",
            "<strong>What fallback rail exists?</strong> If instant payment fails, can the bank use batch, wire, card, manual repair or no fallback? Who chooses and who informs the customer?",
            "<strong>Are scheme changes monitored?</strong> Rulebook updates, ISO migration dates, reimbursement rules and operating-hour changes need owners, not ad hoc emails.",
        ])
        + H3("9.5  Authentication, fraud, sanctions and customer protection")
        + ol([
            "<strong>How do we know it is really the customer?</strong> Name the authentication factor: password, PIN, biometric, device binding, one-time password, certificate, hardware token or corporate approval.",
            "<strong>How do we know the customer is allowed to do this transaction?</strong> Authentication proves identity. Authorisation checks balance, limit, product rule, mandate, entitlement and risk.",
            "<strong>Where is consent captured?</strong> For pull payments, mandates, cards and recurring payments, consent evidence is as important as the debit itself.",
            "<strong>What is the fraud segmentation?</strong> Known payee, new payee, high amount, unusual device, unusual time, vulnerable customer and high-risk merchant should not receive identical friction.",
            "<strong>What is the false-positive cost?</strong> Blocking a legitimate salary, rent, medical or supplier payment creates customer harm, not just an inconvenience metric.",
            "<strong>What is the false-negative cost?</strong> Letting a scam or mule payment through may trigger reimbursement, regulatory scrutiny and customer trauma.",
            "<strong>Which sanctions lists are screened?</strong> OFAC, UK OFSI, EU, United Nations, MAS and domestic lists may all matter depending on customer, currency and geography.",
            "<strong>What happens on a possible sanctions hit?</strong> Is the payment blocked, held, queued for analyst review, reported, or released after documented false-positive decision?",
            "<strong>Are warnings measurable?</strong> The bank should know which warning was shown, whether the customer saw it, and whether it reduced scam loss without unacceptable abandonment.",
            "<strong>How are vulnerable customers protected?</strong> Scam controls, cooling-off, call-back and specialist support should not assume every customer can self-protect in real time.",
        ])
        + H3("9.6  Data, privacy, outsourcing and geography")
        + ol([
            "<strong>Which personal data fields move through the transaction?</strong> Name, account number, card number, address, phone, device ID, IP address, geolocation and remittance text may all be sensitive.",
            "<strong>Which fields are payment data, card data or bank secrecy data?</strong> Different labels trigger different localisation, masking, retention and access obligations.",
            "<strong>Where is the data stored at rest?</strong> Country, cloud region, database, log store, analytics platform, backup and archive all count.",
            "<strong>Where does data travel in processing?</strong> API gateway, fraud vendor, sanctions vendor, cloud support, observability tool and offshore operations can all create transfer questions.",
            "<strong>Who can see plaintext?</strong> Encryption is not enough if administrators, support teams, vendors or analysts can view sensitive data without controlled process.",
            "<strong>What is tokenised, masked or encrypted?</strong> Card primary account numbers, account numbers, national IDs and device identifiers need different controls.",
            "<strong>What is the retention rule?</strong> Regulators may require evidence retention, while privacy law may require minimisation and deletion. The design must reconcile both.",
            "<strong>Is the vendor material or critical?</strong> Payment processing, cloud hosting, fraud scoring, sanctions screening and reconciliation can trigger outsourcing governance.",
            "<strong>What is the exit plan?</strong> If a vendor fails or contract ends, can the bank export data, rebuild service, reroute traffic and continue reconciliation?",
            "<strong>Does the same design work in India, US, UK, Eurozone and Singapore?</strong> A global platform may need local data boundaries, rule packs, reporting clocks and operational owners.",
        ])
        + H3("9.7  Resilience, operations and incident response")
        + ol([
            "<strong>What are the important business services?</strong> Name the customer-visible services that regulators and executives care about, not just servers and applications.",
            "<strong>What is the impact tolerance?</strong> How much outage, delay, duplicate risk, stuck payment volume or customer harm is tolerable before the service is outside appetite?",
            "<strong>What is the p95 and p99 latency by phase?</strong> Break down channel, authentication, fraud, ledger, rail, notification and reconciliation rather than quoting one average.",
            "<strong>What happens when the rail is down?</strong> Queue, fail fast, reroute, degrade, manual process or stop? Each choice has customer and regulatory consequences.",
            "<strong>What happens when our ledger is down?</strong> Continuing to accept payments without ledger posting may create unacceptable financial and customer harm.",
            "<strong>What happens when fraud or sanctions screening is down?</strong> Fail-open may breach law. Fail-closed may harm customers. The policy must be pre-approved.",
            "<strong>How are in-flight transactions recovered after restart?</strong> The system needs durable state, replay rules, duplicate protection and exception queues.",
            "<strong>How often is reconciliation run?</strong> Intraday, end-of-day, settlement-cycle and month-end reconciliation catch different breaks.",
            "<strong>Who owns exceptions at 2 a.m.?</strong> Always-on rails need always-on operations, escalation, treasury and customer communication.",
            "<strong>What is the regulator notification clock?</strong> UK, EU, India, US and Singapore incident clocks differ. The incident runbook must know which clock starts when.",
            "<strong>Has the failover been tested with real transaction states?</strong> A clean infrastructure failover is not enough if pending, debited, credited and disputed items cannot recover.",
            "<strong>What is the customer remediation process?</strong> Refunds, fee waivers, interest compensation, complaint handling and vulnerable-customer outreach should be rehearsed.",
        ])
        + H3("9.8  Migration, cut-over and programme governance")
        + ol([
            "<strong>What is the migration unit?</strong> Customer, account, product, rail, country, ledger segment, merchant portfolio or message type?",
            "<strong>Can old and new systems run in parallel?</strong> If yes, which system is authoritative for balance, status, dispute and reconciliation during parallel run?",
            "<strong>What data is migrated and what remains historical?</strong> Open disputes, mandates, saved payees, audit logs, limits and fraud profiles are often harder than account balances.",
            "<strong>What is the cut-over freeze?</strong> Payment systems need clear rules for in-flight transactions, pending files, scheme windows and settlement cycles.",
            "<strong>What is the rollback trigger?</strong> Define measurable thresholds: error rate, reconciliation break, latency, fraud-control failure, customer complaints or settlement issue.",
            "<strong>Can rollback restore money truth?</strong> Rolling back code is easy compared with rolling back ledger entries and rail messages that already left the bank.",
            "<strong>What has been tested with production-like volume?</strong> Peak salary day, festival sale, tax deadline, market volatility and outage replay are better tests than average-day synthetic load.",
            "<strong>What defects are acceptable at go-live?</strong> Cosmetic defects differ from defects in posting, screening, settlement, reconciliation, customer notification and audit.",
            "<strong>Who signs residual risk?</strong> Technology, operations, product, compliance, treasury and business executives may each own a different piece.",
            "<strong>What is the hypercare model?</strong> Name the war room, dashboards, decision rights, customer-support scripts, vendor contacts and daily reconciliation sign-off.",
        ])
        + H3("9.9  Evidence and accountability")
        + p("The final question in every review is not technical. It is evidential: six months from "
            "now, if a regulator, auditor, customer, court or executive asks what happened, can the "
            "bank prove it? Transaction systems are memory machines. If the memory is incomplete, "
            "the bank may have behaved correctly and still be unable to defend itself.")
        + table(
            ["Claim the team makes", "Evidence to ask for", "If evidence is missing"],
            [
                ["Customers cannot be double-debited.", "Idempotency design, duplicate test results, ledger replay test, exception report.", "Treat as a go-live blocker for money movement."],
                ["Sanctions screening is complete.", "List sources, update timestamp, match rules, case workflow, sample alert decisions.", "Do not accept a diagram alone. Ask for operational proof."],
                ["The system is resilient.", "Failover test with in-flight transactions, recovery time, data-loss result, reconciliation after failover.", "Infrastructure uptime claim is not transaction resilience proof."],
                ["The vendor can be exited.", "Data export test, replacement process, contract rights, migration runbook, retained bank capability.", "Exit plan is theoretical and may fail regulatory scrutiny."],
                ["Customers understand the risk.", "Screenshots, wording tests, accessibility review, warning-effectiveness metrics, complaint analysis.", "Disclosure may be legally present but practically ineffective."],
                ["Finance can reconcile.", "Scheme file, ledger report, settlement account, general-ledger mapping, break-ageing dashboard.", "Operations will discover defects after customers are already affected."],
            ]
        )
        + red_flag(
            p("If a meeting ends with ‘we will document that later’, push back. In BFSI transaction "
              "systems, evidence is not decoration after delivery. Evidence is part of the control. "
              "If the system cannot produce proof automatically or through a reliable operational "
              "process, the design is unfinished."))
        + callout("Section 9 takeaway",
            ul([
                "Good transaction-review questions are simple but sharp: promise, state, owner, evidence.",
                "Never let a team hide behind generic words like success, complete, real time, resilient, secure or compliant.",
                "Ask for numbers: value, count, limit, latency, exposure, ageing, recovery time and error rate.",
                "Ask for geography: the same global design may need different data, fraud, incident and reimbursement handling by region.",
                "Ask for proof: logs, journals, scheme messages, settlement files, tests, dashboards, approvals and customer communications.",
            ]),
            "info")
    )
    return TopicSection("9.  Questions to ask the team in any design review", "basic", body)


def _sec10() -> TopicSection:
    body = (
        primer(
            p("This final section is the part you use when someone says something that sounds "
              "reasonable but hides a dangerous misunderstanding. A red flag is not a personal "
              "attack. It is an early-warning signal that the team may be about to lose money, "
              "mislead a customer, breach a rule, or build something operations cannot safely run. "
              "After the red flags, the glossary gives you the vocabulary of the whole topic in "
              "one place, written in plain English so you can revise it before a client meeting.")
        )
        + H3("10.1  Red flags about customer promise and payment status")
        + red_flag(
            ul([
                "<strong>‘Payment successful’ means the request reached our server.</strong> Push back because customers read success as money moved. If only the request was accepted, the screen must say request received or processing, not successful.",
                "<strong>‘The customer can just try again if it times out.’</strong> Push back unless the original request has an idempotency key, final-status lookup and duplicate-protection evidence. Retrying money movement without those controls can double-debit or double-credit.",
                "<strong>‘Pending is enough detail for the customer.’</strong> Push back because pending can mean many different states: authentication done, debit posted, rail response missing, beneficiary credit pending, settlement pending or manual review. Support cannot help if the word hides the state.",
                "<strong>‘Refund, reversal, recall and dispute are basically the same.’</strong> Push back because each has a different legal, accounting and rail meaning. A card chargeback, UPI reversal, wire recall and merchant refund follow different rulebooks.",
                "<strong>‘Notifications are just user experience.’</strong> Push back because notifications are often evidence. SMS, push, email, merchant beep and corporate file response may become proof in a complaint, fraud case, audit or court dispute.",
                "<strong>‘Customers do not need to see limits until the transaction fails.’</strong> Push back because hidden limits create avoidable failure, repeated attempts and support load. For high-value or urgent payments, pre-disclosure is part of responsible design.",
            ])
        )
        + table(
            ["If you hear", "Ask this immediately", "Good answer looks like"],
            [
                ["The payment is done.", "Done at which state: accepted, debited, credited, cleared, settled or dispute-closed?", "The team names the exact lifecycle state and customer wording."],
                ["Retry will fix it.", "What prevents duplicate money movement?", "Stable idempotency key, duplicate lookup, replay test and final-status API."],
                ["Support will handle confusion.", "What status and evidence does support see?", "Support screen shows rail state, ledger state, reference IDs and next action."],
                ["Refund it.", "Is this a refund, reversal, recall, chargeback or goodwill credit?", "The team chooses the correct mechanism and accounting treatment."],
            ]
        )
        + H3("10.2  Red flags about ledgers, settlement and reconciliation")
        + red_flag(
            ul([
                "<strong>‘The channel database is good enough as transaction truth.’</strong> Push back because the channel records what the user attempted. The ledger records money. The payment switch records rail status. Reconciliation proves whether those views agree.",
                "<strong>‘Reconciliation is a back-office problem.’</strong> Push back because engineering choices create or prevent reconciliation breaks. Missing identifiers, inconsistent timestamps, lossy message mapping and weak status models become operations pain.",
                "<strong>‘Clearing and settlement are the same thing.’</strong> Push back because clearing records obligations and settlement moves final money. Confusing them leads to wrong liquidity, risk and customer-finality decisions.",
                "<strong>‘The amount is small, so breaks do not matter.’</strong> Push back because small breaks at scale become large financial, regulatory and reputational problems. A ₹10 break across one million payments is ₹1 crore.",
                "<strong>‘We can manually fix suspense later.’</strong> Push back unless suspense ageing, approval, evidence and customer-impact rules are defined. Suspense is a control tool, not a dumping ground.",
                "<strong>‘Settlement files arrive tomorrow, so today’s status can be approximate.’</strong> Push back because customer status, intraday risk and treasury exposure still need a controlled state today.",
            ])
        )
        + example("Why one tiny reconciliation percentage is still serious",
            p("A retail payment platform processes 4 million transactions a day worth ₹320 crore. "
              "A team says the mismatch rate is only 0.02%. That sounds tiny. But 0.02% of 4 million "
              "is 800 transactions every day. If the average break is ₹600, that is ₹4,80,000 of "
              "daily value needing investigation. Over 30 days, the operations team has 24,000 "
              "items and ₹1.44 crore of broken value to explain. Percentages hide workload and "
              "customer harm; counts, value and ageing reveal it."))
        + H3("10.3  Red flags about fraud, sanctions and customer protection")
        + red_flag(
            ul([
                "<strong>‘Fraud checks are killing conversion, remove them.’</strong> Push back unless the team separates fraud loss, false positives, abandonment, vulnerable-customer harm and reimbursement cost. Averages hide the trade-off.",
                "<strong>‘Known customer means low risk.’</strong> Push back because scams often use genuine authenticated customers. Authentication proves the actor; it does not prove the actor is not being manipulated.",
                "<strong>‘Sanctions screening can run after the payment.’</strong> Push back for money movement where law or policy requires screening before release. After-the-fact detection may be too late.",
                "<strong>‘A false-positive sanctions alert is just an inconvenience.’</strong> Push back because blocked salary, medical, rent or supplier payments can create real harm. The control needs skilled review and service-level clocks.",
                "<strong>‘The warning was shown, so liability is solved.’</strong> Push back because a warning must be understandable, specific, accessible and evidenced. Generic warnings that users blindly click through may not protect customers or the bank.",
                "<strong>‘The model score is enough evidence.’</strong> Push back because fraud and sanctions decisions need inputs, thresholds, list versions, analyst rationale where relevant, override evidence and model-governance controls.",
            ])
        )
        + table(
            ["Control area", "Weak sign", "Stronger design"],
            [
                ["Authentication", "Only checks password or device, then assumes all payments are safe.", "Separates identity proof from transaction authorisation and behavioural risk."],
                ["Fraud", "One generic rule for all customers and amounts.", "Segments by amount, payee, device, history, geography, vulnerability and scam typology."],
                ["Sanctions", "Screens only names with no list-version evidence.", "Preserves list source, version, match score, rationale and release / block decision."],
                ["Warnings", "Generic ‘be careful’ banner.", "Context-specific warning with measurable user action and accessible wording."],
                ["Reimbursement", "Handled case by case with no evidence pack.", "Links warning, device, customer communication, payment state and policy decision."],
            ]
        )
        + H3("10.4  Red flags about data, cloud, vendors and geography")
        + red_flag(
            ul([
                "<strong>‘The data is encrypted, so location does not matter.’</strong> Push back because encrypted data can still be regulated data. Payment data, personal data, card data, logs and backups may trigger localisation, transfer and access obligations.",
                "<strong>‘It is only logs.’</strong> Push back because logs often contain account numbers, names, device identifiers, Internet Protocol addresses, error payloads and sometimes full payment messages.",
                "<strong>‘The vendor is certified, so the bank is covered.’</strong> Push back because certifications help but do not transfer accountability. The bank still owns outsourcing risk, data use, resilience, exit and customer harm.",
                "<strong>‘We can exit the vendor if needed.’</strong> Push back until someone proves data export, replacement process, contract rights, parallel run, reconciliation continuity and operational capacity.",
                "<strong>‘One global design will satisfy every region.’</strong> Push back because India payment-data storage, United Kingdom scam reimbursement, Eurozone operational resilience, United States consumer and sanctions rules, and Singapore technology-risk expectations differ.",
                "<strong>‘Cloud failover solves resilience.’</strong> Push back because transaction resilience is about in-flight states, ledger consistency, duplicate prevention, rail connectivity, reconciliation and customer communication, not just servers restarting elsewhere.",
            ])
        )
        + example("The hidden data-copy problem",
            p("A payment hub stores the official payment message in India. The team says payment data "
              "does not leave India. But error logs are shipped to a global observability platform, "
              "support tickets copy message snippets to an offshore queue, a fraud vendor receives "
              "device and beneficiary data, and backups are replicated to another region. The design "
              "may still be useful, but the original statement was false. Data architecture must map "
              "official databases, logs, tickets, analytics, backups, vendor feeds and support access."))
        + H3("10.5  Red flags about resilience, migration and programme governance")
        + red_flag(
            ul([
                "<strong>‘The system is active-active, so resilience is solved.’</strong> Push back until the team proves transaction-state recovery, idempotent replay, ledger consistency and reconciliation after failover.",
                "<strong>‘We tested failover with synthetic traffic.’</strong> Push back unless tests include real transaction states: pending, debited, credited, timed out, reversed, disputed and in manual review.",
                "<strong>‘Rollback is just redeploying the old version.’</strong> Push back because payment messages may already have left the bank and ledger entries may already be posted. Code rollback is not money rollback.",
                "<strong>‘We will clean migration data after go-live.’</strong> Push back if the dirty data affects balances, mandates, saved payees, limits, disputes, sanctions evidence or reconciliation keys.",
                "<strong>‘Operations can scale manually during hypercare.’</strong> Push back with numbers. How many exceptions per hour, how many trained analysts, what ageing threshold, what weekend coverage?",
                "<strong>‘Compliance will sign off at the end.’</strong> Push back because late compliance review finds architecture defects: missing data, missing evidence, unapproved outsourcing, impossible reporting clocks and weak customer-dispute handling.",
            ])
        )
        + table(
            ["Programme claim", "Reality check", "Evidence before go-live"],
            [
                ["We can migrate safely.", "Migration is safe only if old and new systems agree on money truth.", "Parallel-run reconciliation, open-item report, migrated-data control totals."],
                ["We can roll back.", "Rollback must handle messages already sent and ledgers already posted.", "Rollback rehearsal with in-flight transactions and finance sign-off."],
                ["Operations can handle exceptions.", "Exception volume can overwhelm teams faster than transaction volume.", "Staffing model, ageing dashboard, runbook and escalation test."],
                ["Resilience tested green.", "Infrastructure green does not mean transaction states recovered.", "Failover report showing no duplicate, lost or stuck payments."],
                ["Regulatory risk accepted.", "Risk acceptance needs named owner and evidence, not meeting optimism.", "Decision log, control gaps, expiry date and accountable executive."],
            ]
        )
        + H3("10.6  The 20-second mental model to carry into any meeting")
        + p("When you feel lost in a transaction discussion, come back to one sentence: a banking "
            "transaction is a legally meaningful change of money state that customers, banks, schemes "
            "and regulators must all be able to trust later. That sentence gives you five questions.")
        + callout("Five questions that never fail",
            ol([
                "<strong>What promise did we make?</strong> The screen, contract, rail rule or operations process promised something to someone.",
                "<strong>What state is the money in?</strong> Accepted, debited, credited, cleared, settled, reversed, disputed or stuck are different states.",
                "<strong>What can still go wrong?</strong> Fraud, sanctions, duplicate, liquidity, timeout, reconciliation, vendor, data and customer-harm risks may remain.",
                "<strong>Who owns the next action?</strong> Product, technology, operations, fraud, compliance, treasury, vendor, scheme desk or customer support must be named.",
                "<strong>What evidence proves it?</strong> Ledger journal, scheme message, settlement file, log, case note, customer communication and approval record must survive.",
            ]),
            "info")
        + H3("10.7  Topic glossary — the words you should now own")
        + kv([
            ("Transaction", "A controlled change from one valid state to another. In banking, it usually means money, obligation or account status changes in a way the bank can prove later."),
            ("Payment", "A transaction whose purpose is to move value from a payer to a payee. It may involve customer ledgers, payment rails, clearing, settlement, fees, FX and notifications."),
            ("Payer", "The person or organisation whose money is being sent or whose account is being debited."),
            ("Payee", "The person, merchant or organisation expected to receive value."),
            ("Ledger", "The bank's book of monetary truth. It records debits, credits, balances and journals in a controlled way."),
            ("Journal", "A recorded ledger entry or group of entries showing a financial movement, such as debit customer ₹750 and credit merchant ₹750."),
            ("Debit", "A decrease to an account or ledger position. In a payment, the payer account is usually debited."),
            ("Credit", "An increase to an account or ledger position. In a payment, the payee account is usually credited."),
            ("Available balance", "The amount the customer can use now after holds, pending debits, limits and other restrictions."),
            ("Booked balance", "The formal ledger balance after posted entries. Available and booked balances can differ, especially with card holds and pending items."),
            ("Authentication", "The process of proving the actor is who they claim to be, such as through PIN, biometric, password, token, certificate or device binding."),
            ("Authorisation", "The decision that an authenticated actor is allowed to do this exact transaction now, considering balance, limits, mandates, fraud, sanctions and product rules."),
            ("Atomicity", "The all-or-nothing property: either all required changes happen or none do. No half-paid state should be left as final truth."),
            ("Consistency", "The property that every completed transaction leaves the system in a valid business state, such as total debits equalling total credits."),
            ("Isolation", "The property that simultaneous transactions do not corrupt one another, such as two withdrawals both spending the same ₹1,000."),
            ("Durability", "The property that once a system confirms a committed transaction, it survives crash, restart or power loss."),
            ("Finality", "The point at which a payment or settlement is legally and operationally irreversible except through a new permitted process."),
            ("Auditability", "The ability to prove who did what, when, through which channel, under which rule, with which result and evidence."),
            ("Payment rail", "The rulebook, network, message format, participants, clearing method, settlement method and dispute process that allow payments to move."),
            ("Scheme", "The organisation and rulebook that governs a payment rail, such as a card scheme, domestic payment scheme or account-to-account payment system."),
            ("Switch", "A central routing system that receives payment messages from participants and sends them to the right destination, often applying scheme rules."),
            ("Clearing", "The process of calculating and recording obligations between participants. Clearing may happen before actual money settlement."),
            ("Settlement", "The actual movement of final value between banks or participants, often in central-bank money or prefunded accounts."),
            ("Real-Time Gross Settlement", "RTGS. A settlement model where each payment settles individually and finally in real time, common for high-value payments."),
            ("Deferred Net Settlement", "DNS. A settlement model where many obligations are netted and settled later, reducing liquidity needs but creating exposure before settlement."),
            ("Prefunding", "Putting money into a settlement account before transactions occur so instant payments can settle without waiting for later funding."),
            ("Liquidity", "Immediately usable money or central-bank balance needed to meet payment and settlement obligations."),
            ("Nostro account", "Our money held at another bank, usually in another currency or country. Used heavily in correspondent banking."),
            ("Vostro account", "Another bank's money held with us. Nostro and vostro are two views of the same correspondent relationship."),
            ("Correspondent banking", "A network where banks use accounts with other banks to make payments in countries or currencies where they do not directly participate."),
            ("Foreign exchange", "FX. Conversion from one currency to another, such as INR to USD, with a rate, spread, fee and settlement implication."),
            ("Float", "Value held or economically available during the gap between customer posting, clearing and settlement."),
            ("Payment versus Payment", "PvP. A foreign-exchange settlement method where both currency legs settle together or neither settles, reducing settlement risk."),
            ("Herstatt risk", "The risk one party pays its currency leg in a foreign-exchange trade but the counterparty fails before paying the other leg."),
            ("Idempotency key", "A unique identifier that lets a system safely recognise a retried request as the same instruction rather than a new payment."),
            ("Retry", "Trying a request again after failure or timeout. Safe retry needs idempotency, state lookup and duplicate protection."),
            ("Timeout", "A situation where one system does not receive a response within expected time. Timeout means unknown state, not automatic failure."),
            ("Reversal", "A linked correcting entry that undoes or offsets an earlier transaction under defined rules."),
            ("Refund", "A merchant or service provider returning money to a customer, usually as a new transaction linked to the original purchase."),
            ("Recall", "A request to retrieve or cancel a payment after release, often dependent on receiving-bank cooperation and rail rules."),
            ("Chargeback", "A card dispute process where a cardholder challenges a transaction and the scheme rulebook determines liability and evidence."),
            ("Dispute", "A formal disagreement about a transaction, such as unauthorised payment, non-receipt of goods, wrong amount or scam."),
            ("Reconciliation", "The process of proving that channel records, ledgers, scheme messages, settlement files and general ledger all agree or explaining breaks."),
            ("Reconciliation break", "A mismatch between expected and actual records, such as customer debited but scheme file missing, or settlement amount not matching ledger totals."),
            ("Suspense account", "A temporary ledger location for uncertain or unmatched money while investigation completes. It needs strict ageing and ownership."),
            ("General ledger", "GL. The finance book used for statutory and management accounting, fed by product ledgers, settlement accounts, fees and adjustments."),
            ("Payment Service Provider", "PSP. An entity that provides payment initiation, acceptance or processing services to customers or merchants."),
            ("Virtual Payment Address", "VPA. A UPI handle such as <code>priya@oksbi</code> that points to an underlying bank account without exposing account number."),
            ("Unified Payments Interface", "UPI. India's instant account-to-account payment system run by National Payments Corporation of India."),
            ("Immediate Payment Service", "IMPS. India's older instant account-to-account payment rail operated through NPCI arrangements."),
            ("National Electronic Funds Transfer", "NEFT. India's batch-style electronic funds transfer system with half-hourly settlement cycles and 24×7 availability."),
            ("Real-Time Gross Settlement in India", "RTGS in India is RBI's high-value real-time gross settlement system, generally used for payments of ₹2 lakh and above."),
            ("Automated Clearing House", "ACH. A United States batch payment network commonly used for payroll, bill payments and recurring transfers."),
            ("Fedwire", "The Federal Reserve's high-value real-time gross settlement wire service in the United States."),
            ("FedNow", "The Federal Reserve's instant payment service launched in July 2023 for 24×7 account-to-account payments."),
            ("Real-Time Payments", "RTP. The Clearing House's private-sector instant payment rail in the United States."),
            ("CHIPS", "Clearing House Interbank Payments System, a private large-value US dollar clearing and settlement system."),
            ("Faster Payments Service", "FPS. The United Kingdom's near-real-time domestic account-to-account payment rail."),
            ("BACS", "The United Kingdom's batch system widely used for payroll and Direct Debit."),
            ("CHAPS", "Clearing House Automated Payment System, the United Kingdom's high-value sterling real-time gross settlement rail."),
            ("Confirmation of Payee", "A United Kingdom name-checking control that compares entered beneficiary details with the receiving account name to reduce misdirected payments and scams."),
            ("Authorised Push Payment fraud", "APP fraud. A scam where the genuine customer is manipulated into authorising a payment to a fraudster."),
            ("Single Euro Payments Area", "SEPA. A European framework for euro credit transfers and direct debits across participating countries."),
            ("SEPA Instant Credit Transfer", "A SEPA scheme for euro credit transfers targeted to complete in seconds, operating 24×7."),
            ("TARGET Instant Payment Settlement", "TIPS. Eurosystem infrastructure for instant settlement of euro payments in central-bank money."),
            ("T2", "Eurosystem real-time gross settlement service for high-value euro payments after TARGET2 consolidation."),
            ("FAST", "Fast And Secure Transfers, Singapore's instant domestic electronic funds transfer service."),
            ("PayNow", "Singapore's proxy addressing service that lets users pay using mobile number, national identity number or entity identifier over FAST."),
            ("SWIFT", "Society for Worldwide Interbank Financial Telecommunication, a global financial messaging network. SWIFT carries instructions, not money itself."),
            ("SWIFT gpi", "Global Payments Innovation, SWIFT's service for improved tracking, transparency and service levels in cross-border payments."),
            ("ISO 20022", "An international financial messaging standard with richer structured data than many legacy formats."),
            ("pacs.008", "An ISO 20022 customer credit transfer message used in interbank payment flows."),
            ("pacs.009", "An ISO 20022 financial institution credit transfer message, often used for bank-to-bank movement."),
            ("pacs.002", "An ISO 20022 payment status report message that communicates acceptance, rejection or other status."),
            ("pain.001", "An ISO 20022 customer credit transfer initiation message, often sent by corporates to banks."),
            ("MT103", "A legacy SWIFT Message Type used for single customer credit transfers, being replaced or supplemented by ISO 20022 in many cross-border contexts."),
            ("Message mapping", "Converting data from one message format to another. Poor mapping can lose compliance, remittance or reconciliation data."),
            ("Merchant Category Code", "MCC. A four-digit code describing merchant type, used for limits, fraud rules, rewards, reporting and interchange."),
            ("Legal Entity Identifier", "LEI. A 20-character identifier for legal entities, used in financial reporting, risk and some payment contexts."),
            ("Hardware Security Module", "HSM. A tamper-resistant device or service used to protect cryptographic keys and perform sensitive cryptographic operations."),
            ("Derived Unique Key Per Transaction", "DUKPT. A key-management method where each transaction uses a derived unique key, common in payment PIN encryption contexts."),
            ("Transport Layer Security", "TLS. A protocol that encrypts data in transit between systems, such as a payment app and bank server."),
            ("Mutual Transport Layer Security", "mTLS. TLS where both sides prove identity with certificates, common between banks, gateways and payment processors."),
            ("Personal Account Number", "PAN. The number on a payment card. It is highly sensitive and subject to payment-card security rules."),
            ("Card-on-File Tokenisation", "CoFT. Replacing stored card numbers with tokens so merchants and apps do not keep the actual card number."),
            ("Know Your Customer", "KYC. Processes to identify and verify customers and understand their risk profile."),
            ("Anti-Money Laundering", "AML. Controls to detect and prevent money laundering through customer due diligence, monitoring, investigation and reporting."),
            ("Countering Financing of Terrorism", "CFT. Controls to prevent financial systems being used to fund terrorism."),
            ("Sanctions screening", "Checking parties, banks, vessels, countries, goods and sometimes text against legal restriction lists before or during processing."),
            ("Office of Foreign Assets Control", "OFAC. The US Treasury office administering major US sanctions programmes."),
            ("Office of Financial Sanctions Implementation", "OFSI. The United Kingdom body responsible for financial sanctions implementation."),
            ("Digital Operational Resilience Act", "DORA. European Union regulation, applicable from January 2025, covering information and communication technology risk in financial services."),
            ("Operational resilience", "The ability to continue delivering important business services within impact tolerance through failures, disruptions and recovery."),
            ("Impact tolerance", "The maximum tolerable disruption to an important business service, measured by time, volume, value, customers or harm."),
            ("Business continuity planning", "BCP. Preparing people, process, technology and premises so critical services can continue or recover during disruption."),
            ("Disaster recovery", "DR. Restoring technology services after major failure, often measured by recovery time and data-loss targets."),
            ("Recovery Time Objective", "RTO. The target maximum time to restore a service after disruption."),
            ("Recovery Point Objective", "RPO. The target maximum data loss measured as time, such as losing no more than five minutes of data."),
            ("Outbox pattern", "A design where a business database write and an event-to-publish record are committed together, then a relay publishes the event safely."),
            ("Saga", "A sequence of local transactions coordinated through events or commands, with compensating actions when later steps fail."),
            ("Two-phase commit", "A distributed transaction protocol where participants prepare and then commit together. Powerful but often impractical across independent payment systems."),
            ("Eventual consistency", "A state where systems may temporarily disagree but are designed to converge to correct truth after processing and reconciliation."),
            ("Maker-checker", "A control where one person creates an instruction and another approves it, common in corporate and high-value payments."),
            ("Four-eyes control", "A control requiring at least two people to approve or verify a sensitive action."),
            ("Privileged access", "Powerful system access that can view, change or administer sensitive systems and therefore requires strong controls and evidence."),
            ("Data localisation", "A requirement or design choice to store or process certain data within a specific country or region."),
            ("Data residency", "Where data physically or legally resides, including databases, backups, logs, analytics copies and support tooling."),
            ("Outsourcing", "Using a third party to provide a service or capability. In BFSI, material outsourcing often triggers governance, resilience and exit obligations."),
            ("Exit plan", "A tested plan to leave a vendor, cloud region or platform without unacceptable customer harm, data loss or regulatory breach."),
            ("Hypercare", "The intensified support period after go-live, with war rooms, dashboards, rapid defect triage and daily operational review."),
            ("Parallel run", "Running old and new systems together for a period to compare outputs, find breaks and prove readiness."),
            ("Cut-over", "The controlled moment or window when processing moves from old system to new system."),
            ("Rollback", "Returning to a previous system or version. In payments, rollback must consider money and messages already moved, not just software."),
            ("Runbook", "Step-by-step operational instructions for handling routine processes, failures and escalations."),
            ("Service-level agreement", "SLA. A promised level of service such as response time, resolution time, uptime or processing window."),
            ("p95 latency", "The response time below which 95% of requests complete. More useful than average for user experience."),
            ("p99 latency", "The response time below which 99% of requests complete. Important for tail delays in high-volume systems."),
            ("Blast radius", "The maximum scope of impact if something fails, such as one product, one country, one rail, one bank or all payments."),
        ])
        + H3("10.8  Final recap — what you should be able to say now")
        + callout("If you can explain these, Topic I.1 has done its job",
            ul([
                "A banking transaction is not a button click. It is a controlled, evidenced state change with customer, ledger, rail, settlement, risk and regulatory meaning.",
                "The five promises are authentication, authorisation, atomicity, finality and auditability. Most architecture choices exist to protect one or more of them.",
                "Clearing records obligations. Settlement moves final value. Reconciliation proves the bank's many books agree.",
                "Instant does not mean simple. Fast rails increase the need for real-time fraud, liquidity, resilience, operations and customer-communication discipline.",
                "A leader's job is to make trade-offs visible: speed versus certainty, friction versus fraud, global reuse versus local regulation, automation versus judgement, cloud elasticity versus exit risk.",
                "The safest question in any meeting is: what exactly did we promise, what state is the money in, who owns the next action, and what evidence proves it?",
            ]),
            "info")
    )
    return TopicSection("10. Red flags + topic glossary", "basic", body)


# =============================================================== helpers

def _wip_banner() -> str:
    return callout(
        "Deep-rewrite complete",
        p("You are reading the May 2026 deep rewrite of Topic I.1. Sections 0 through 10 are "
          "complete at the new depth bar. The previous (v1) version of this topic was 62 KB "
          "across 11 sections; this rewrite is intentionally much deeper, with every "
          "concept built up slowly from zero rather than name-dropped. If you need the v1 "
          "content for comparison, it remains on disk at "
          "<code>bfsi_bible_src/topics/foundations_01_transactions.py</code> but is no longer "
          "linked from the sidebar."),
        "info")
