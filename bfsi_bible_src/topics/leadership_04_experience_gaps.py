"""Leadership Lenses · 04 — Closing the four experience gaps: a tactical
survival and acceleration guide from a veteran Programme Director."""
from __future__ import annotations

from ..site import (
    H2, H3, H4, p, ul, ol, kv, primer, callout, analogy, example, red_flag,
    it_anchor, bfsi_anchor, table, mermaid, TopicPage, TopicSection,
)


def build() -> TopicPage:
    return TopicPage(
        code="VII.4",
        slug="04-closing-experience-gaps",
        title="Closing the four experience gaps — a tactical survival guide",
        one_liner=(
            "The BFSI Bible gives you the mental model. Your integration projects give you "
            "the technical scar tissue. But four gaps remain between 'knowledgeable BA' and "
            "'senior leader that a bank trusts with a £200M programme': live programme "
            "experience, stakeholder networks, decision-making under pressure, and commercial "
            "acumen. This topic is not a textbook. It is a private briefing from a veteran "
            "Programme Director who has led core banking migrations, payments modernisations, "
            "and regulatory remediation programmes across three continents — written for "
            "someone who is smart, motivated, and willing to do the uncomfortable work."
        ),
        sections=[_sec0(), _sec1(), _sec2(), _sec3(), _sec4(), _sec5()],
    )


# ------------------------------------------------------------------ 0
def _sec0() -> TopicSection:
    body = (
        primer(
            p("Let me be direct. You can read every topic in this bible twice, pass every "
              "vendor certification, and still fail spectacularly in your first programme "
              "leadership role. Not because you lack knowledge, but because these four "
              "capabilities are muscles that only grow under load. Knowledge is the "
              "foundation — it stops you from being lost. But the gap between 'I understand "
              "how Loan IQ batch processing works' and 'I can keep a 14-bank syndicated "
              "lending migration on track when the vendor misses their third consecutive "
              "milestone' is not a knowledge gap. It is an experience gap, a judgement gap, "
              "and a nerve gap.")
        )
        + H3("0.1  Why this topic exists")
        + p("I have watched brilliant analysts stall at the mid-career plateau because they "
            "kept doing what made them successful as analysts: going deeper into domain "
            "knowledge, building better documents, mastering more tools. That is the wrong "
            "strategy for the next level. The next level rewards a completely different set "
            "of behaviours: navigating ambiguity, building alliances, making irreversible "
            "decisions with incomplete information, and owning outcomes measured in money.")
        + callout("The uncomfortable truth",
            p("Nobody will explicitly teach you these skills. Your manager will not "
              "schedule a 'How to Run a 2 AM Crisis Bridge' training session. Your "
              "organisation will not offer a 'How to Negotiate a Vendor Escalation' "
              "workshop. These capabilities are learned by doing, by watching, and by "
              "failing — and then reflecting with brutal honesty on what happened. This "
              "topic accelerates that cycle by telling you what to look for and what to "
              "do, so you extract ten years of lessons in three."),
            "info")
        + H3("0.2  The career progression this topic addresses")
        + table(
            ["Level", "What you are judged on", "What actually differentiates you"],
            [
                ["<strong>BA / Senior BA</strong>",
                 "Quality of analysis, requirements, test coverage, documentation.",
                 "How well you understand the domain and translate it into actionable "
                 "work for delivery teams."],
                ["<strong>Lead BA / Delivery Manager</strong>",
                 "Stream delivery, team coordination, stakeholder satisfaction, "
                 "risk escalation.",
                 "Whether your stream delivers on time without surprises. Your ability "
                 "to manage up — keeping senior stakeholders informed before they "
                 "have to ask."],
                ["<strong>Programme Manager / Engagement Manager</strong>",
                 "Cross-stream coordination, vendor management, budget tracking, "
                 "client relationship.",
                 "Whether the client trusts you enough to tell you the real problem. "
                 "Whether you can hold a vendor accountable without destroying the "
                 "relationship. Whether you can absorb scope changes without losing "
                 "the plan."],
                ["<strong>Senior Consultant / Practice Lead / VP</strong>",
                 "Revenue, strategic client relationships, practice growth, "
                 "thought leadership.",
                 "Whether CxOs call you directly when they have a problem. Whether "
                 "your judgement is trusted enough that people act on your "
                 "recommendations without requiring a 40-page deck."],
            ]
        )
        + H3("0.3  How to use this topic")
        + ul([
            "Read each gap section completely before acting. The subsections build on "
            "each other.",
            "Start with <strong>Gap 1 (Live Programme Experience)</strong> — it is "
            "the foundation. You cannot build networks, make crisis decisions, or own "
            "P&amp;L if you have not been inside a real programme.",
            "The 'Action' items are not suggestions. They are assignments. Do them "
            "within the next 30 days of reading this.",
            "The 'Seen the Movie' sections contain hard truths. Some will be "
            "uncomfortable. That is the point.",
        ])
    )
    return TopicSection(
        "0.  Primer — the private briefing nobody gives you",
        "basic", body)


# ------------------------------------------------------------------ 1
def _sec1() -> TopicSection:
    body = (
        H3("Gap 1: Live Programme Experience")
        + p("The ability to lead core migrations, payment modernisations, and large-scale "
            "integration programmes. Senior leaders have 'seen the movie before' and know "
            "what typically breaks — before, during, and after go-live.")

        # --- Mindset Shift ---
        + H3("1.1  The Mindset Shift")
        + p("As a BA, your job is to be right. Your requirements must be accurate. Your "
            "mapping documents must be correct. Your test scenarios must cover edge cases. "
            "You are rewarded for precision and completeness.")
        + p("As a programme leader, your job shifts from being right to <strong>keeping "
            "the programme moving in roughly the right direction</strong>. You will never "
            "have complete information. You will never have enough time. You will make "
            "decisions that turn out to be wrong, and your value is in recognising that "
            "quickly and adjusting — not in avoiding mistakes entirely.")
        + table(
            ["BA mindset", "Programme leader mindset"],
            [
                ["'I need to understand this fully before I sign off.'",
                 "'I need to understand this enough to make a call, and I need to know what "
                 "I will check first if the call is wrong.'"],
                ["'The requirement is ambiguous — I need to clarify it.'",
                 "'The requirement is ambiguous — I need to decide what we assume, document "
                 "the assumption, get one person to agree, and move. We will validate in "
                 "the next sprint.'"],
                ["'The vendor's documentation is incomplete.'",
                 "'I will send three specific questions to the vendor by email at 9 AM, "
                 "escalate to their delivery manager at 5 PM if unanswered, and to their "
                 "account director at 9 AM tomorrow. Meanwhile, we proceed with our best "
                 "assumption and flag the risk.'"],
                ["'I found a defect in the integration specification.'",
                 "'I found a defect. Is it a blocker for the next milestone? If yes, who "
                 "owns it, what is the fix timeline, and what is the workaround? If no, "
                 "it goes into the backlog and I keep moving.'"],
            ]
        )
        + callout("The single most important transition",
            p("<strong>Stop optimising for being right. Start optimising for velocity "
              "of learning.</strong> A programme that moves fast, makes small mistakes, "
              "and corrects quickly will beat a programme that moves slowly trying to "
              "avoid all mistakes. The enemy is not errors — it is stagnation."),
            "info")

        # --- Action ---
        + H3("1.2  Action — what to do in the next 30 days")
        + ol([
            "<strong>Volunteer for the ugliest workstream.</strong> Every programme has "
            "a workstream nobody wants — data migration, legacy interface inventory, "
            "reconciliation design, or the 'integration with the system nobody understands'. "
            "Volunteer for it. This is where you learn the most, because this is where the "
            "programme will actually break. The glamorous workstreams (new digital channels, "
            "API design) teach you less because they are greenfield and forgiving.",

            "<strong>Get yourself into three rooms you are not currently in.</strong> "
            "The programme SteerCo (even as a note-taker). The weekly vendor sync. The "
            "test-readiness review. If you cannot get a seat, ask to 'shadow' someone who "
            "attends. Your goal: learn the rhythm and language of programme governance. "
            "Who asks the hard questions? Who deflects? Who gets listened to?",

            "<strong>Build a personal 'Programme Anatomy' document.</strong> For the "
            "programme you are on, write one page covering: governance structure (who "
            "decides what), key milestones and dates, top 5 risks and who owns them, "
            "the three decisions that have already been deferred and why. Update it "
            "weekly. This forces you to see the programme as a leader sees it, not "
            "just your workstream.",

            "<strong>Find the person who has done this before and buy them coffee.</strong> "
            "Every programme has one or two veterans — usually a senior client PM, an "
            "experienced vendor architect, or a consulting partner. Ask them: 'What went "
            "wrong on the last programme like this that you worked on?' Then shut up and "
            "listen. Take notes. The stories they tell you are worth more than any training "
            "course.",

            "<strong>Start a 'Lessons Learned' journal.</strong> Every Friday, write three "
            "things: (1) one thing that surprised me this week, (2) one decision I saw "
            "someone make that I would not have made, and (3) one moment where the "
            "programme almost went off the rails and what saved it. Do this for six months. "
            "You will be astonished at how much pattern recognition you build.",
        ])

        # --- How-To Playbook ---
        + H3("1.3  The How-To Playbook — building programme sense")
        + H4("How to read a programme like a senior leader")
        + p("A senior leader walks into a programme SteerCo and within 15 minutes knows "
            "whether the programme is healthy or dying. They are not reading the slides. "
            "They are reading the signals:")
        + ul([
            "<strong>The RAG status.</strong> If everything is Green, the programme is "
            "either genuinely healthy (rare) or the PM is hiding problems (common). "
            "A healthy programme has Amber items. A programme with no Amber is a "
            "programme where nobody feels safe escalating.",
            "<strong>The milestone slip pattern.</strong> One milestone slipping is "
            "normal. The same milestone slipping three sprints in a row is a structural "
            "problem — usually a dependency, a skills gap, or a requirements gap that "
            "nobody wants to name.",
            "<strong>The vendor's body language.</strong> When the vendor stops sending "
            "their senior people to the sync calls and starts sending junior delivery "
            "managers, they have mentally moved their best people to a more profitable "
            "engagement. This is the single most reliable early warning of a vendor "
            "delivery failure.",
            "<strong>The testing narrative.</strong> 'We are on track for SIT' means "
            "nothing. Ask: 'How many test scenarios have been executed? How many passed? "
            "What is the defect density? What is the P1 defect ageing?' If no one can "
            "answer, testing has not really started.",
            "<strong>The data migration silence.</strong> If nobody is talking about "
            "data migration, it is because nobody wants to face it. Data migration is "
            "where 60% of programme failures actually originate. If it is not a "
            "standing agenda item from month 2, escalate.",
        ])
        + H4("How to run a programme checkpoint that surfaces truth")
        + p("Most programme checkpoints are theatre. People present slides designed to "
            "show progress. The leader's job is to create an environment where truth is "
            "safer than optimism.")
        + ol([
            "Open with: <em>'Tell me the one thing that keeps you up at night on this "
            "workstream.'</em> Not 'give me your status update'. This question bypasses "
            "the prepared slides and goes straight to the real problem.",
            "When someone says 'on track', ask: <em>'What would have to go wrong for "
            "this to slip by two weeks?'</em> This forces them to think about fragility "
            "rather than success.",
            "When someone presents a risk, ask: <em>'What have you already done about "
            "it?'</em> Not 'what is the mitigation plan'. If the answer is 'nothing yet', "
            "the risk is not being managed — it is being documented.",
            "When a dependency is flagged, ask: <em>'Have you spoken to the dependency "
            "owner this week? What did they say?'</em> Most dependencies are 'assumed' "
            "rather than agreed.",
            "Close with: <em>'What decision do you need from me or from the SteerCo "
            "this week?'</em> If there are no decisions needed, either the workstream "
            "is genuinely autonomous (good) or the lead is not escalating (bad). "
            "Distinguish by checking the decision log.",
        ])

        # --- Seen the Movie ---
        + H3("1.4  The 'Seen the Movie' Reality Check")
        + red_flag(
            ul([
                "<strong>'The vendor will handle the migration.'</strong> No, they will "
                "not. The vendor will handle <em>their</em> migration tooling. Your data "
                "quality, your business rules, your reconciliation, your fallback plan — "
                "those are yours. Every programme that outsourced migration accountability "
                "to the vendor has regretted it. Every single one.",

                "<strong>'We will do a big-bang cutover.'</strong> Big-bang cutovers work "
                "in PowerPoint. In reality, they create a single point of failure with no "
                "retreat path. Every experienced programme director pushes for a phased "
                "approach — by product, by region, by customer segment — even when the "
                "vendor says big-bang is 'simpler'. Simpler for them, catastrophic for you.",

                "<strong>'Go-live is the hard part.'</strong> Go-live is the <em>visible</em> "
                "part. The hard part is the 90 days after go-live — batch failures that "
                "surface at month-end, reconciliation breaks that appear in the first "
                "interest accrual cycle, performance degradation that only shows under "
                "real production load, and the 200 change requests that pour in from "
                "operations teams who were never properly consulted during design.",

                "<strong>'Parallel run passed, so we are ready.'</strong> Parallel run "
                "compares outputs between old and new systems. But it only tests the "
                "scenarios that existed during the parallel run period. It does not test "
                "month-end, quarter-end, year-end, leap year, rate reset, covenant breach, "
                "or the regulatory return that only runs annually. The most dangerous "
                "defects hide in calendar-dependent logic.",

                "<strong>'The business signed off the requirements.'</strong> They signed "
                "off a document. They did not read it line by line. They trusted you. "
                "When the system goes live and the process does not match what they "
                "expected, 'but you signed off' is a career-ending argument. You will "
                "lose. Always. The sign-off protects the project plan, not you.",
            ])
        )
        + H4("What actually kills programmes — the real list")
        + ol([
            "<strong>Data quality discovered too late.</strong> The source system has "
            "25 years of inconsistent data. Nobody cleaned it. Nobody mapped the edge "
            "cases. Nobody tested with real data until SIT. By then, the migration "
            "rules are wrong and the timeline is dead.",
            "<strong>Organisational change neglected.</strong> The new system works "
            "differently. Operations teams were not retrained. Process maps were not "
            "updated. Day-1 in production, staff revert to old workarounds and the new "
            "system's controls are bypassed.",
            "<strong>The 'frozen requirements' illusion.</strong> Someone declared a "
            "requirements freeze. The business continued to change. Regulations "
            "continued to change. By go-live, the frozen requirements are stale and "
            "a mountain of change requests has been deferred to 'Phase 2' — which "
            "never happens.",
            "<strong>Testing that tests the happy path.</strong> 95% of test scenarios "
            "cover normal flows. The system breaks on exception flows: partial payments, "
            "back-dated transactions, multi-currency rollovers, manually corrected "
            "positions, accounts with special regulatory flags. These are the scenarios "
            "that cause P1 incidents in production.",
            "<strong>No fallback plan.</strong> Or a fallback plan that was never tested. "
            "'We can fall back to the old system' means nothing if you have not tested "
            "the rollback, if you have not preserved the old system's state, and if you "
            "have not trained operations on the fallback process.",
        ])
    )
    return TopicSection(
        "1.  Gap 1 — Live programme experience: building the 'seen the movie' instinct",
        "intermediate", body)


# ------------------------------------------------------------------ 2
def _sec2() -> TopicSection:
    body = (
        H3("Gap 2: Stakeholder Network")
        + p("Deep relationships with vendors, regulators, executives, and business leaders. "
            "Senior leaders solve problems through networks and influence, not just expertise.")

        # --- Mindset Shift ---
        + H3("2.1  The Mindset Shift")
        + p("As a BA, your network is your immediate team, your business SME, and maybe "
            "the test lead. You build relationships by being competent and reliable.")
        + p("As a senior leader, your network <em>is</em> your capability. The problems "
            "you face cannot be solved alone. You need the vendor's CTO to take your "
            "escalation seriously. You need the regulator's relationship manager to give "
            "you a heads-up before a new circular lands. You need the client's CFO to "
            "defend your programme's budget when cost-cutting starts. You need the "
            "HCLTech practice lead to find you three Loan IQ specialists in two weeks. "
            "None of these things happen through formal channels alone. They happen "
            "because people know you, trust you, and want to help you.")
        + table(
            ["BA networking", "Senior leader networking"],
            [
                ["Reactive — you meet people because the project requires it.",
                 "Proactive — you build relationships <em>before</em> you need them."],
                ["Transactional — 'I need this requirement clarified.'",
                 "Relational — 'I want to understand how your world works.'"],
                ["Narrow — your project, your team, your deliverables.",
                 "Broad — across vendors, across clients, across the industry."],
                ["Informal — you know people by working with them.",
                 "Deliberate — you invest time in people who are not in your "
                 "immediate project because they will be valuable later."],
            ]
        )
        + callout("The networking truth nobody says aloud",
            p("In BFSI services, <strong>your next role, your next promotion, and your "
              "next client engagement are all decided by someone who knows you "
              "personally</strong> — not by your CV, not by your certifications, not "
              "by your performance rating. The person who recommends you for the £200M "
              "programme is someone who has worked with you, seen you handle a crisis, "
              "and trusts your judgement. Everything in this section is about becoming "
              "that person."),
            "info")

        # --- Action ---
        + H3("2.2  Action — what to do in the next 30 days")
        + ol([
            "<strong>Map your stakeholder universe.</strong> Draw a simple grid: "
            "rows are stakeholder types (client executives, client operations, "
            "vendor delivery, vendor product, HCLTech leadership, regulators/auditors). "
            "Columns are: name, role, what they care about, my current relationship "
            "strength (1–5), and one action I will take this month. Fill every row. "
            "If you have blanks, you have blind spots.",

            "<strong>Schedule three 'non-agenda' conversations this month.</strong> "
            "Reach out to three people outside your immediate workstream — a client "
            "operations manager, a vendor solution architect, a colleague from a "
            "different programme — and ask for 20 minutes of their time. Not to discuss "
            "a deliverable. To understand their world: <em>'I am trying to understand "
            "how [your area] works in practice. Could I learn from you for 20 minutes?'</em> "
            "Most people are flattered and will say yes. The relationship starts here.",

            "<strong>Start attending one industry event per quarter.</strong> Not to "
            "collect business cards. To listen, ask one good question in a panel Q&amp;A, "
            "and introduce yourself to one speaker afterwards. Industry events are "
            "where you build the 'weak ties' — the people you do not work with daily "
            "but who can open doors when you need them.",

            "<strong>Create a 'stakeholder CRM' habit.</strong> After every significant "
            "meeting or conversation, spend 2 minutes noting: who was there, what they "
            "cared about, what they were worried about, and any follow-up you promised. "
            "Review this weekly. The person who remembers what a stakeholder said three "
            "months ago and follows up is the person who gets trusted.",

            "<strong>Find your sponsor.</strong> A sponsor is not a mentor. A mentor "
            "gives you advice. A sponsor puts your name forward for opportunities when "
            "you are not in the room. Identify one senior person — client-side or "
            "HCLTech-side — who has seen your work, and invest in that relationship. "
            "Ask them: <em>'What should I be doing differently to get to the next level?'</em> "
            "Then do exactly what they say, and show them you did it.",
        ])

        # --- How-To Playbook ---
        + H3("2.3  The How-To Playbook — building a high-value network")
        + H4("How to build trust with client executives")
        + p("Client executives do not want more updates. They want fewer surprises. "
            "The currency of trust at the executive level is predictability — "
            "specifically, the confidence that you will tell them the truth before "
            "it becomes a crisis.")
        + ol([
            "<strong>The pre-brief.</strong> Before every SteerCo, send the executive "
            "sponsor a 3-line message: <em>'Tomorrow's SteerCo will cover X, Y, Z. "
            "The one thing I want you to be aware of beforehand is [the difficult "
            "item]. I am handling it by [action]. I may need your support on [specific "
            "thing].'</em> Executives hate surprises in meetings. The pre-brief is "
            "how you become the person they trust.",
            "<strong>The bad-news formula.</strong> When delivering bad news, use "
            "this exact structure: <em>'Here is what happened. Here is the impact. "
            "Here is what we are doing about it. Here is what I need from you.'</em> "
            "Never deliver bad news without a proposed action. Never try to minimise "
            "it. Executives can smell sugarcoating. They respect directness.",
            "<strong>The 'close the loop' discipline.</strong> If you said you would "
            "do something, confirm when it is done. A simple email: <em>'Following "
            "up on our conversation — [action] is now complete. Result: [outcome]. "
            "No further action needed from you.'</em> Ninety percent of people never "
            "close the loop. The ten percent who do get remembered.",
        ])
        + H4("How to build a relationship with vendors")
        + p("Your vendor (Finastra, Temenos, nCino, Oracle, FIS, Infosys, whoever) "
            "is not your friend and not your enemy. They are a business partner with "
            "different incentives. Understanding those incentives is the key to the "
            "relationship.")
        + ul([
            "<strong>Their account manager cares about revenue and renewal.</strong> "
            "Speak to commercial impact: <em>'If this issue is not resolved by Friday, "
            "we risk a go-live delay that will affect the next SOW discussion.'</em>",
            "<strong>Their delivery manager cares about utilisation and margin.</strong> "
            "They will resist adding senior resources unless forced. When you need "
            "expertise, escalate specifically: <em>'We need your Loan IQ product "
            "specialist, not a generalist, for the next three weeks to resolve the "
            "batch sequencing defect.'</em>",
            "<strong>Their product team cares about roadmap, not your timeline.</strong> "
            "If you need a product enhancement, you must speak roadmap language: "
            "<em>'We have three clients who will adopt this feature. Can we discuss "
            "including it in the Q3 release?'</em> One client's request is a feature "
            "request. Three clients' request is a market signal.",
            "<strong>Build a relationship with their senior technical person.</strong> "
            "Not the account manager, not the PM — the person who actually knows the "
            "product deeply. Buy them coffee. Ask them about the product's real "
            "limitations. They will tell you things the sales team never will. This "
            "relationship will save you during a crisis.",
        ])
        + H4("How to influence executives without formal authority")
        + p("This is the most important leadership skill in consulting. You are never "
            "the client's boss. You have no formal authority. Yet you must get "
            "executives to make difficult decisions — replatform, increase budget, "
            "delay go-live, change organisational structure. Here is how:")
        + ol([
            "<strong>Frame every recommendation as a choice, not an instruction.</strong> "
            "Never: <em>'We should delay go-live.'</em> Always: <em>'We have three options. "
            "Option A: proceed on the current date with these known risks and this "
            "fallback plan. Option B: delay by four weeks, which eliminates [specific "
            "risks] but costs [specific amount]. Option C: descope [specific features] "
            "and proceed. My recommendation is B because [one sentence]. What is your "
            "preference?'</em> This gives the executive ownership of the decision while "
            "channelling them toward your recommendation.",
            "<strong>Pre-wire the room.</strong> Before any major decision meeting, "
            "have 1:1 conversations with every key stakeholder. Understand their "
            "concerns. Address them individually. By the time the meeting happens, "
            "everyone has already heard the idea, had their objections addressed, and "
            "feels heard. The meeting becomes a ratification, not a debate. This is "
            "how every successful senior leader operates.",
            "<strong>Use the 'let me take an action' technique.</strong> When a "
            "discussion is going in circles, say: <em>'I think we need more data "
            "before we can decide. Let me come back by Thursday with [specific "
            "analysis].'</em> This gives you control of the narrative. You choose "
            "what data to present, how to frame it, and what recommendation to make.",
            "<strong>Build credibility through small predictions.</strong> When you "
            "predict something will happen and it does, your credibility compounds. "
            "Start small: <em>'Based on the current defect trend, I expect we will "
            "need an additional two-week testing cycle.'</em> When that prediction "
            "proves accurate, executives start asking for your opinion — which is "
            "influence.",
        ])

        # --- Seen the Movie ---
        + H3("2.4  The 'Seen the Movie' Reality Check")
        + red_flag(
            ul([
                "<strong>'I will build my network when I need it.'</strong> By then "
                "it is too late. Networks are built in peacetime. When a crisis hits, "
                "you use the network you already have. If you have not invested, you "
                "will be alone in the room. Start today.",

                "<strong>'I am too junior to reach out to senior people.'</strong> "
                "Senior people are surprisingly accessible if you approach them "
                "correctly. Do not ask for 'mentoring' — that feels like a commitment. "
                "Ask for '20 minutes of your perspective on [specific topic]'. Be "
                "prepared with two or three specific questions. Respect their time. "
                "Follow up with a thank-you note and one concrete thing you did "
                "based on their advice.",

                "<strong>'Networking feels fake and political.'</strong> If it feels "
                "fake, you are doing it wrong. Genuine networking is about curiosity "
                "and generosity: learning what matters to people and finding ways to "
                "help them. Forward them a relevant article. Introduce them to someone "
                "they should meet. Share a useful insight from your project. Give "
                "before you ask.",

                "<strong>'The client's architect does not like our approach — I need "
                "to convince them with a better deck.'</strong> No. You need to have "
                "a conversation. The objection is rarely about the technical approach. "
                "It is about fear (of failure, of loss of control, of being blamed), "
                "about organisational politics (they recommended a different vendor), "
                "or about unspoken constraints (budget, skills, legacy commitments). "
                "You will never discover the real objection in a meeting. You will "
                "discover it in a 1:1 over coffee.",

                "<strong>'The vendor promised they would deliver.'</strong> Vendor "
                "promises are aspirational. Check their actions, not their words. "
                "Are their senior people showing up? Are they resolving P1 defects "
                "within the agreed SLA? Are they sharing their internal test results? "
                "Actions reveal commitment. Words reveal intent. These are not the "
                "same thing.",
            ])
        )
    )
    return TopicSection(
        "2.  Gap 2 — Stakeholder network: becoming someone people call when it matters",
        "intermediate", body)


# ------------------------------------------------------------------ 3
def _sec3() -> TopicSection:
    body = (
        H3("Gap 3: Decision-Making Under Pressure")
        + p("Handling major incidents, regulatory deadlines, and crisis situations. "
            "Theory does not teach you how to choose between two bad options at 2 AM "
            "when millions of pounds and reputations are at stake.")

        # --- Mindset Shift ---
        + H3("3.1  The Mindset Shift")
        + p("As a BA, you optimise for correctness. You want the right answer.")
        + p("As a leader under pressure, you optimise for <strong>the least-worst "
            "decision, made quickly enough to matter</strong>. In a crisis, the cost "
            "of indecision almost always exceeds the cost of a wrong decision that is "
            "promptly corrected. The perfect answer at 10 AM is worth less than the "
            "80%-right answer at 2 AM.")
        + table(
            ["Normal mode", "Crisis mode"],
            [
                ["Gather all information, then decide.",
                 "Decide with 60% information. Define what you will check to "
                 "confirm or reverse."],
                ["Consensus-driven — everyone agrees before we proceed.",
                 "Command-driven — one person decides, everyone executes, we "
                 "review later."],
                ["Mistakes are avoided.",
                 "Mistakes are expected, contained, and corrected. The sin is "
                 "not making a mistake — it is not catching it."],
                ["Communication is thorough and detailed.",
                 "Communication is short, clear, and frequent. Three sentences "
                 "every 30 minutes beats one email per hour."],
            ]
        )

        # --- Action ---
        + H3("3.2  Action — what to do in the next 30 days")
        + ol([
            "<strong>Ask to be on the incident bridge roster.</strong> Most "
            "organisations have a major-incident process. Ask to be added as a "
            "participant (not the lead — not yet). Your goal: observe how the "
            "bridge is run, who does what, how decisions are made, and what the "
            "communication rhythm looks like.",

            "<strong>After every incident you observe, write a personal "
            "after-action review.</strong> Three questions: (1) What was the "
            "decision point where the outcome was determined? (2) What information "
            "did the decision-maker have at that moment? (3) What would I have "
            "done, and why? Be honest. This is a private exercise in calibrating "
            "your own judgement against experienced operators.",

            "<strong>Study three real BFSI incidents in detail.</strong> Not from "
            "news articles — from FCA Final Notices, RBI penalty orders, or "
            "published post-incident reviews. These documents reveal what went "
            "wrong operationally, what the regulator expected, and what the "
            "consequences were. Google: 'FCA Final Notice [bank name]' or 'RBI "
            "penalty order [bank name]'. Read three. You will learn more about "
            "crisis management from these than from any textbook.",

            "<strong>Build a personal 'Decision Journal'.</strong> For every "
            "significant decision you make or observe, record: the decision, the "
            "options considered, the information available, the reasoning, and the "
            "outcome. Review quarterly. You are training your pattern recognition "
            "for the day when you will be the one deciding at 2 AM.",
        ])

        # --- How-To Playbook ---
        + H3("3.3  The How-To Playbook — operating under pressure")
        + H4("How to run a 2 AM crisis bridge")
        + p("A crisis bridge is not a discussion forum. It is a <strong>decision-making "
            "machine</strong>. Here is the operating protocol that experienced "
            "Programme Directors use:")
        + ol([
            "<strong>Open with the SITREP (Situation Report).</strong> The bridge "
            "lead speaks first, for no more than 90 seconds: <em>'Here is what we "
            "know. [System X] is [down / degraded / producing incorrect output]. "
            "The impact is [Y customers / Y transactions / Y revenue]. It started "
            "at [time]. Here is what we have done so far: [actions]. Here is what "
            "we are deciding now: [the specific decision].'</em> No backstory. No "
            "blame. Facts, impact, actions, decision.",

            "<strong>Assign four roles explicitly.</strong> (1) <em>Bridge Lead</em> — "
            "runs the bridge, makes decisions, sets the next check-in time. "
            "(2) <em>Technical Lead</em> — directs the investigation and fix. "
            "(3) <em>Comms Lead</em> — sends updates to stakeholders (client "
            "executives, regulators, operations) every 30 minutes. (4) <em>Scribe</em> — "
            "logs every decision, every action, every timeline in real time. If "
            "these roles are not assigned in the first two minutes, the bridge "
            "will descend into chaos.",

            "<strong>Establish the decision cadence.</strong> 'We will reconvene "
            "in 30 minutes. By then, I need [person A] to confirm [specific thing] "
            "and [person B] to have tried [specific action].' Never let a bridge "
            "call end without a specific next-action and a specific time.",

            "<strong>Make the call.</strong> When two options are both imperfect "
            "— and they always are — use this framework: (1) Which option is "
            "reversible? (2) Which option limits customer impact right now? "
            "(3) Which option preserves audit trail and regulatory defensibility? "
            "If all else is equal, choose the option that is easier to undo.",

            "<strong>Send the executive update.</strong> After the bridge, send a "
            "crisp update to the executive sponsor. Format: <em>'INCIDENT UPDATE "
            "[time]. Status: [ongoing/resolved/monitoring]. Impact: [X]. Root "
            "cause: [known/under investigation]. Next update: [time].'</em> "
            "Three lines. Executives at 2 AM do not want a paragraph.",
        ])
        + H4("How to negotiate a vendor escalation at crisis speed")
        + p("When a vendor's system or deliverable is the root cause of a crisis, "
            "you need rapid escalation — not a polite email chain.")
        + ol([
            "<strong>Call, do not email.</strong> Pick up the phone. Call your "
            "vendor delivery manager directly. If they do not answer, call their "
            "account manager. If they do not answer, send a message to both: "
            "<em>'P1 incident in progress. [System] is [impact]. I need your "
            "senior support engineer on a bridge call in 30 minutes. Sending "
            "bridge details now.'</em>",

            "<strong>Escalate in 30-minute increments.</strong> If the vendor has "
            "not responded meaningfully in 30 minutes, escalate to the next level. "
            "Vendor delivery manager → vendor engagement director → vendor country "
            "head → vendor global account partner. Each escalation includes: "
            "<em>'Incident started at [time]. Customer impact: [X]. Your team "
            "was contacted at [time]. Current response: [none / inadequate / "
            "pending]. I need [specific action] by [specific time].'</em>",

            "<strong>Follow every call with a contemporaneous email.</strong> "
            "This creates the audit trail. <em>'Confirming our call at [time]: "
            "[vendor name] committed to [action] by [deadline]. If not delivered, "
            "I will escalate to [next level].'</em> This email is not hostile — "
            "it is professional documentation that creates accountability.",

            "<strong>After the crisis, hold the vendor accountable "
            "constructively.</strong> In the post-incident review: <em>'During "
            "the incident, our agreed SLA was X. The actual response was Y. I "
            "want to understand what happened on your side and agree on what "
            "changes we make to prevent this response gap in future.'</em> Do "
            "not burn the relationship. You will need them again.",
        ])
        + H4("The decision framework for 'two bad options at 2 AM'")
        + p("When you face a decision where both options are painful, use this "
            "mental model:")
        + table(
            ["Question", "Why it matters"],
            [
                ["<strong>What is the blast radius of each option?</strong>",
                 "Choose the option that affects fewer customers, fewer systems, "
                 "and fewer downstream processes."],
                ["<strong>Which option is reversible?</strong>",
                 "A reversible bad decision is always better than an irreversible "
                 "one. If you can undo it in 2 hours, try it."],
                ["<strong>Which option preserves the audit trail?</strong>",
                 "Regulators will review your decisions. The option with better "
                 "documentation and traceability is safer even if technically "
                 "inferior."],
                ["<strong>What would the regulator say if they read about "
                 "this in the newspaper?</strong>",
                 "If either option creates a regulatory or reputational risk, "
                 "choose the one that demonstrates you prioritised customer "
                 "protection over commercial convenience."],
                ["<strong>Can I explain this decision to a non-technical "
                 "executive in one sentence?</strong>",
                 "If you cannot articulate the rationale simply, you do not "
                 "understand it well enough to decide. Simplify your thinking "
                 "first."],
            ]
        )

        # --- Seen the Movie ---
        + H3("3.4  The 'Seen the Movie' Reality Check")
        + red_flag(
            ul([
                "<strong>'We need to understand root cause before we "
                "communicate.'</strong> No. Communicate impact and actions "
                "<em>now</em>. Root cause can come later. Executives and regulators "
                "will forgive you for not knowing root cause at 2 AM. They will "
                "not forgive you for not telling them there was an incident until "
                "10 AM. DORA, FCA, and CERT-In all have explicit incident "
                "reporting timelines (4 hours for DORA, 6 hours for CERT-In). "
                "Silence is never an option.",

                "<strong>'Let me escalate this to my manager.'</strong> In a "
                "crisis, the person closest to the information should make the "
                "decision, not the most senior person. Escalate for resources, "
                "for air cover, for executive communication. Do not escalate "
                "for permission. If you are on the bridge, you are empowered to "
                "decide. If you are not, you should not be on the bridge.",

                "<strong>'The vendor says it is not their issue.'</strong> During "
                "a crisis, vendor finger-pointing is the default. Ignore it. Say: "
                "<em>'We will do root-cause attribution after the incident is "
                "resolved. Right now, I need your team to help us [specific "
                "action].'</em> Never let a bridge call turn into a blame debate. "
                "That is a post-mortem topic, not a crisis topic.",

                "<strong>'We should wait until the morning when more people are "
                "available.'</strong> If the incident is impacting customers or "
                "accumulating financial exposure, waiting is a decision — and a "
                "bad one. Every hour of delay is measurable in customer impact, "
                "regulatory exposure, and remediation cost. Act now, review later.",

                "<strong>The person who stays calm wins.</strong> This is not "
                "a platitude. In a crisis bridge with 15 stressed people, the "
                "person who speaks slowly, asks clear questions, and proposes "
                "specific actions becomes the de facto leader — regardless of "
                "their title. Practice this. Your voice, your pace, your "
                "specificity are leadership tools.",
            ])
        )
    )
    return TopicSection(
        "3.  Gap 3 — Decision-making under pressure: the 2 AM playbook",
        "advanced", body)


# ------------------------------------------------------------------ 4
def _sec4() -> TopicSection:
    body = (
        H3("Gap 4: Commercial Acumen")
        + p("P&amp;L ownership, contract negotiation, budgeting, and value delivery. "
            "Senior leaders are judged on business outcomes, not technical excellence.")

        # --- Mindset Shift ---
        + H3("4.1  The Mindset Shift")
        + p("As a BA or delivery manager, your success is measured by whether you "
            "delivered what was asked — on time, on quality, within scope. You are "
            "a cost centre: someone else decided the budget, someone else signed the "
            "contract, someone else set the commercial terms.")
        + p("As a senior leader, you are measured by whether the engagement <strong>makes "
            "money for HCLTech and delivers measurable value for the client</strong>. "
            "You own the P&amp;L — or at least a significant portion of it. You "
            "negotiate the SOW (Statement of Work). You decide the team shape. You "
            "manage the margin. You are responsible for the commercial outcome, not "
            "just the delivery outcome.")
        + table(
            ["Delivery mindset", "Commercial mindset"],
            [
                ["'I delivered the requirements on time.'",
                 "'I delivered the requirements on time, under budget, and the "
                 "client has already extended the engagement by six months.'"],
                ["'The team is working hard.'",
                 "'The team is running at 93% utilisation, we are tracking 2% "
                 "above target margin, and the offshore-onshore ratio is "
                 "optimised for this phase.'"],
                ["'The client is happy with our work.'",
                 "'The client has provided a reference, agreed to a case study, "
                 "and is discussing the next phase. The deal pipeline from this "
                 "account is £2M.'"],
                ["'We need more resources.'",
                 "'Adding two resources for eight weeks will cost £120K and "
                 "accelerate delivery by four weeks, avoiding a £200K penalty "
                 "clause. Net benefit: £80K. I am requesting approval.'"],
            ]
        )
        + callout("Why commercial acumen accelerates your career faster than anything else",
            p("In every services organisation — HCLTech, Accenture, Deloitte, TCS, "
              "Infosys, Wipro, Cognizant — the people who rise fastest are the people "
              "who understand <em>how the company makes money</em>. Not just how to "
              "deliver work, but how to grow revenue, protect margin, expand accounts, "
              "and create commercial structures that align client outcomes with "
              "HCLTech profitability. This is the gap most technologists never close. "
              "Close it, and you skip ahead of 90% of your peers."),
            "info")

        # --- Action ---
        + H3("4.2  Action — what to do in the next 30 days")
        + ol([
            "<strong>Ask your engagement manager to show you the SOW.</strong> Not "
            "the entire contract — just the commercial structure: T&amp;M (Time and "
            "Materials) or Fixed Price? What is the rate card? What are the penalty "
            "clauses? What are the SLAs? What is the target margin? Understanding "
            "these numbers transforms your perspective on every delivery decision.",

            "<strong>Learn to calculate utilisation and margin.</strong> "
            "<em>Utilisation = billable hours / total available hours.</em> "
            "<em>Margin = (revenue - cost) / revenue.</em> Ask: 'What is our "
            "utilisation target for this engagement? What is our margin target?' "
            "If you do not know these numbers, you are delivering blind.",

            "<strong>Start thinking in £/hour and $/day.</strong> When someone "
            "proposes a meeting that will take 10 people 2 hours, calculate the "
            "cost: 10 × 2 × average billing rate. Is that meeting worth £3,000? "
            "When a defect causes three days of rework for four people, that is "
            "12 person-days of cost. This mental habit changes how you prioritise "
            "and how you communicate.",

            "<strong>Ask to attend one commercial review.</strong> Every "
            "engagement has a monthly or quarterly commercial review — revenue "
            "recognition, margin tracking, forecasting, pipeline. Ask your "
            "engagement manager if you can attend as an observer. The language "
            "spoken in that room is the language of senior leadership.",

            "<strong>Read one consulting P&amp;L walkthrough.</strong> Search "
            "for 'HCL Technologies quarterly earnings investor presentation' or "
            "the equivalent for your organisation. Read the first 10 slides. "
            "Understand: revenue growth, margin by segment, deal pipeline, "
            "offshore-onshore mix. This is the context your senior leaders "
            "operate in.",
        ])

        # --- How-To Playbook ---
        + H3("4.3  The How-To Playbook — operating commercially")
        + H4("How to speak commercial language")
        + p("The moment you start using commercial language, senior leaders "
            "hear you differently. Here are the phrases that signal commercial "
            "maturity:")
        + table(
            ["Instead of saying...", "Say...", "Why it works"],
            [
                ["'We need more people.'",
                 "'Adding 2 senior resources for 8 weeks at an incremental "
                 "cost of £X will de-risk the Y milestone and protect the "
                 "£Z revenue recognition in Q3.'",
                 "You framed a resource request as a commercial decision."],
                ["'The timeline is tight.'",
                 "'At current velocity, we will miss the March milestone by "
                 "3 weeks. This triggers the penalty clause in §4.2 of the "
                 "SOW (£50K/week). Here are three options to mitigate.'",
                 "You connected timeline to commercial consequence."],
                ["'The client keeps changing requirements.'",
                 "'We have absorbed 14 change requests outside the original "
                 "SOW scope, worth approximately £180K. I recommend we raise "
                 "a formal Change Request for the next batch to protect both "
                 "the timeline and the margin.'",
                 "You converted scope creep into a commercial conversation."],
                ["'We delivered the project successfully.'",
                 "'We delivered 3 weeks early, saved £95K against budget, "
                 "achieved a 4.6/5 client satisfaction score, and the client "
                 "has signed a 12-month AMS extension worth £420K.'",
                 "You measured success in business outcomes, not just delivery."],
            ]
        )
        + H4("How to protect margin without damaging the client relationship")
        + ul([
            "<strong>Track scope creep from day one.</strong> Maintain a 'scope "
            "delta' log: every request that falls outside the original SOW. "
            "Quantify each in person-days. Review with the client monthly: "
            "<em>'These are the additional items we have delivered. So far, we "
            "have absorbed £40K of additional scope. For the next set, I would "
            "like to formalise a Change Request.'</em> The client respects this "
            "because it is transparent, not confrontational.",
            "<strong>Optimise the team shape, not the team size.</strong> The "
            "fastest way to improve margin is to shift work from expensive "
            "onshore resources to capable offshore resources. But do it carefully: "
            "client-facing roles stay onshore; deep technical execution moves "
            "offshore. The wrong move here damages quality and trust.",
            "<strong>Forecast attrition.</strong> People leave. Plan for it. If "
            "your team has 10 people and industry attrition is 15%, you will lose "
            "1-2 people during a 12-month engagement. Have a bench plan. Have "
            "knowledge transfer documentation. The cost of unplanned attrition "
            "is 3-4× the cost of planned replacement.",
        ])
        + H4("How to negotiate a Statement of Work (SOW)")
        + p("When you reach the level where you are shaping SOWs, these are the "
            "levers that experienced engagement managers use:")
        + ol([
            "<strong>Always prefer T&amp;M over Fixed Price for uncertain "
            "scope.</strong> Fixed Price transfers risk to HCLTech. If requirements "
            "are unclear (and they always are in BFSI transformation), Fixed Price "
            "means you absorb every change request and every delay. Argue for T&amp;M "
            "with a 'not-to-exceed' cap if the client insists on cost certainty.",
            "<strong>Build a contingency buffer into the estimate.</strong> "
            "Technical teams estimate based on the happy path. Reality includes "
            "environment delays, vendor dependencies, data quality issues, and "
            "client availability constraints. Add 15-20% contingency. If the "
            "client pushes back on the total, reduce scope — never reduce "
            "contingency.",
            "<strong>Define scope exclusions explicitly.</strong> What is NOT "
            "in the SOW is as important as what IS. Data cleansing, environment "
            "setup, third-party integration testing, production support "
            "hypercare, training, documentation — if these are not explicitly "
            "included, they should be explicitly excluded. Every ambiguity will "
            "be resolved in the client's favour.",
            "<strong>Include a change-control clause.</strong> Any changes to "
            "scope, timeline, or deliverables must go through a formal Change "
            "Request (CR) process with commercial impact assessment and mutual "
            "sign-off. Without this clause, scope creep is legalised.",
        ])

        # --- Seen the Movie ---
        + H3("4.4  The 'Seen the Movie' Reality Check")
        + red_flag(
            ul([
                "<strong>'I am a technologist, not a commercial person.'</strong> "
                "Every VP, Partner, and Practice Lead in every services company is "
                "measured on revenue and margin. If you want to stay technical, "
                "that is a valid choice — but it caps your career at a level below "
                "where the real decisions (and compensation) live. Commercial acumen "
                "is not selling. It is understanding the business model you operate "
                "in well enough to make it work.",

                "<strong>'The client will understand if we go over budget.'</strong> "
                "They will not. The client's procurement team tracks every penny. "
                "Their internal stakeholders are being measured on project cost. "
                "Going over budget without a formal Change Request destroys trust "
                "and opens contract disputes. Budget discipline is a trust signal.",

                "<strong>'Margin is the finance team's problem.'</strong> "
                "Margin is YOUR problem the moment you have any influence over "
                "team shape, utilisation, or scope. A delivery manager who "
                "consistently delivers at 5% above target margin is promoted. "
                "A delivery manager who consistently bleeds margin is moved. "
                "This is the unspoken reality of services organisations.",

                "<strong>'I will learn commercial skills when I get a commercial "
                "role.'</strong> You will never get a commercial role without "
                "demonstrating commercial thinking first. Start by asking your "
                "engagement manager one question: <em>'What is the margin on "
                "this engagement, and what can I do to help protect it?'</em> "
                "That one question signals more career intent than any "
                "certification you could earn.",

                "<strong>The real metric nobody tells you.</strong> In a services "
                "company, the single number that determines your career trajectory "
                "is <strong>revenue under management</strong> — how much revenue "
                "you are responsible for. A Lead BA managing a £200K stream is "
                "different from a Programme Director managing a £5M engagement. "
                "Everything you do should be aimed at increasing this number — "
                "by delivering well (so the engagement grows) and by being "
                "trusted with larger engagements.",
            ])
        )
    )
    return TopicSection(
        "4.  Gap 4 — Commercial acumen: speaking the language of money",
        "advanced", body)


# ------------------------------------------------------------------ 5
def _sec5() -> TopicSection:
    body = (
        H3("5.1  The integration framework — how the four gaps compound")
        + p("These four gaps are not independent. They compound. Programme experience "
            "gives you the context for stakeholder conversations. Stakeholder "
            "relationships give you the intelligence for crisis decisions. Crisis "
            "decision-making earns you the credibility for commercial ownership. "
            "Commercial ownership funds the next programme. It is a flywheel.")
        + mermaid(
            'flowchart LR\n'
            '  A["Programme experience"] --> B["Credible in stakeholder conversations"]\n'
            '  B --> C["Intelligence for crisis decisions"]\n'
            '  C --> D["Trusted with commercial responsibility"]\n'
            '  D --> E["Given larger programmes"]\n'
            '  E --> A',
            "The leadership flywheel — each gap, once closed, accelerates the "
            "others."
        )
        + H3("5.2  The 90-day acceleration plan")
        + table(
            ["Week", "Focus", "Specific actions"],
            [
                ["<strong>Weeks 1–2</strong>",
                 "Awareness",
                 "Build your Programme Anatomy document. Map your stakeholder "
                 "universe. Learn your engagement's commercial structure (SOW, "
                 "rates, margin). Start your Lessons Learned journal."],
                ["<strong>Weeks 3–4</strong>",
                 "Access",
                 "Get into three rooms you are not currently in (SteerCo, vendor "
                 "sync, test review). Schedule three non-agenda conversations. Ask "
                 "to attend a commercial review."],
                ["<strong>Weeks 5–8</strong>",
                 "Contribution",
                 "Volunteer for the hardest workstream. Offer to write the "
                 "SteerCo status update. Prepare a risk assessment for your area "
                 "using the decision framework in Gap 3. Start tracking scope "
                 "delta against the SOW."],
                ["<strong>Weeks 9–12</strong>",
                 "Visibility",
                 "Present at the SteerCo (even a 5-minute item). Send your first "
                 "executive pre-brief before a meeting. Deliver one specific "
                 "prediction ('I expect X will happen by Y'). Close the loop on "
                 "every action item within 24 hours."],
            ]
        )
        + H3("5.3  The one-page self-assessment")
        + p("Score yourself honestly on each dimension. Repeat quarterly.")
        + table(
            ["Dimension", "1 — Starting", "3 — Developing", "5 — Operating"],
            [
                ["<strong>Programme sense</strong>",
                 "I know my workstream. I cannot describe the programme's top "
                 "5 risks or governance structure.",
                 "I can describe the programme's key risks, milestones, and "
                 "decision points. I anticipate dependencies.",
                 "I see programme health signals before they appear in RAG "
                 "status. I influence the programme plan proactively."],
                ["<strong>Stakeholder network</strong>",
                 "I know my immediate team and SMEs.",
                 "I have relationships across client, vendor, and internal "
                 "teams. People take my calls.",
                 "CxOs and vendor directors know me by name. They call me when "
                 "they have a problem. I am introduced as 'the person who "
                 "knows' by others."],
                ["<strong>Pressure decisions</strong>",
                 "I escalate when things go wrong. I have not led a crisis "
                 "bridge.",
                 "I have participated in crisis bridges and contributed "
                 "meaningfully. I can run a SITREP.",
                 "I have led crisis responses. People turn to me when things "
                 "break. I am calm under fire and my decisions are "
                 "trusted."],
                ["<strong>Commercial acumen</strong>",
                 "I do not know the commercial terms of my engagement.",
                 "I understand SOW structure, utilisation, and margin. I track "
                 "scope delta and flag commercial risks.",
                 "I shape SOWs, negotiate CRs, manage P&amp;L, and grow "
                 "accounts. My recommendations include commercial impact "
                 "analysis."],
            ]
        )
        + H3("5.4  Final words from the Programme Director's desk")
        + callout("The one thing I wish someone had told me at your stage",
            p("The difference between a good BA and a great senior leader is not "
              "knowledge, not intelligence, and not work ethic. You already have "
              "those. The difference is <strong>the willingness to be "
              "uncomfortable</strong> — to sit in a room where you are the least "
              "experienced person and contribute anyway; to make a decision when "
              "you are not 100% sure and own the outcome; to have a commercial "
              "conversation when you have never owned a P&amp;L; to call a vendor's "
              "bluff when they know the product better than you do. Every senior "
              "leader you admire was once in your exact position, and the only "
              "thing that separated them from the people who stayed at the same "
              "level was that they <em>chose to do the uncomfortable thing</em> — "
              "again and again and again — until it became comfortable."),
            "info")
        + p("Now go build your Programme Anatomy document. Today.")
    )
    return TopicSection(
        "5.  The integration framework — compounding all four gaps",
        "intermediate", body)
