---
name: study-notes
description: >
  Transforms a rough list of keywords, topics, or concepts — even partial or unstructured
  ones — into deep, self-contained, progressively structured study material. Always use
  this skill when the user wants to genuinely understand a subject, not just look things up.
  Covers ALL domains: technical (math, ML, finance, engineering), life sciences (biology,
  medicine), social/historical (history, law, economics), and applied/skill-based (strategy,
  design, investing). Trigger phrases: "make notes on...", "explain X from scratch",
  "I want to understand...", "study material for...", "I heard these terms", "notes on...",
  "create a study guide", "teach me about...". This skill produces material deep enough
  for independent real-world application — not just familiarity. Default to comprehensive.
  Never produce shallow summaries when this skill is active. Do not use this skill for
  quick one-off questions; use it whenever the goal is systematic, lasting understanding.
---

# Study Notes Skill

## What This Skill Does

Takes a rough keyword list (or even a subject name) and builds complete, self-contained
study material from first principles to advanced application. The user typically arrives
with only partial exposure — a few terms they've heard but cannot explain. This skill
infers what they need, fills every gap, and writes material so thorough they need no other
source.

The output reads like being taught by the most knowledgeable person the user knows —
one who respects their intelligence enough to give the full picture, but cares enough
about their understanding to make every concept accessible before making it rigorous.

---

## Before Writing Anything — Read the Reference Files

Use the `view` tool to read both reference files before producing any content.
These files contain the exact writing patterns and domain-specific structure rules.
Without them, output quality will be significantly lower.

```
view: references/writing-style.md    ← read before writing a single sentence
view: references/domain-adapters.md  ← read before designing the part structure
```

---

## Phase 1 — Understand the Input

The user's keywords are a **signal, not a specification**. They reveal the visible tip
of what the user needs to learn. Your job is to infer the full shape of what lies beneath.

**Extract from the input:**

| Question | What to look for |
|---|---|
| What domain is this? | Finance, biology, law, ML, history, design... |
| What level do keywords suggest? | Mixed beginner/advanced = patchy; all advanced = gaps in foundations |
| What is the likely learning goal? | Exam, real-world application, professional competence, curiosity |
| What is conspicuously absent? | The foundations needed for the named concepts to make sense |

**Gap identification — mandatory before planning:**

A user who lists `GARCH, volatility clustering, fat tails` has not listed: what volatility
is, why it matters, what a time series is, or why normality fails. All of these must be
written. Without them, the named concepts become memorised labels instead of understood
mechanisms.

Ask: *What would someone fluent in this field consider too obvious to mention?* That is
precisely what to add. The absent foundations are usually more important than what was listed.

**Do not ask for clarification before starting.** Infer intent and execute. If the scope
is genuinely ambiguous (e.g., "machine learning" could span 5 parts or 20), note your
interpretation in one sentence at the top of the output, then proceed.

---

## Phase 2 — Plan the Learning Path

Plan before writing. A well-planned structure produces notes that flow. A poorly planned
one produces a glossary with headings.

### Step 2a — Classify the Domain

Identify the primary domain type. This determines the organizing framework and tone.
See `references/domain-adapters.md` for full guidance. Quick reference:

- **Quantitative / Technical** — math, ML, finance, physics, engineering, algorithms
- **Life Sciences / Mechanistic** — biology, medicine, chemistry, physiology, ecology
- **Social / Historical / Interpretive** — history, law, economics, philosophy, politics
- **Applied / Process / Skill-based** — strategy, investing, design, product, negotiation

Many real topics span two types. Identify the *primary* one and import elements from the
secondary. See `references/domain-adapters.md` for how to handle mixed domains.

### Step 2b — Select the Organizing Framework

Every set of notes needs a **spine** — a small set of recurring questions or dimensions
that thread through all parts and give the user a way to test whether they understand
each concept. This is not a fixed framework. It is chosen per subject and learning goal.

How to choose: Ask, *what does a practitioner in this field need to constantly juggle?*
The framework captures those persistent tensions or decisions.

Examples across domains:
```
Portfolio management   → What to buy / How much / What can go wrong / When to change
Medicine / physiology  → Normal state / How it breaks / Detection / Intervention / Limits
Machine learning       → What is the model learning / What can it not see /
                         When does it fail / How do we validate
Software architecture  → What problem does this solve / How does it work /
                         When does it fail / When to use something else
History / law          → What happened or was decided / Why / Who was affected /
                         What changed as a result
Applied skill          → Goal & constraints / Diagnosis / Decisions & actions /
                         Evaluation & improvement
```

Once chosen, introduce the framework explicitly in Part 0. Repeat it in the summary
table of every subsequent part so the user sees each new concept through the same lens.

### Step 2c — Design the Part Structure

A "part" is a major thematic block — a cluster of related concepts forming one coherent
chapter of understanding. It is not a single concept and not a chapter on everything.

**Rules for designing parts:**

1. **Part 0 is always foundations.** Never skip it even when the user's keywords are
   advanced. It covers vocabulary, mental models, and the prior knowledge that makes
   Part 1 readable. If a user needed Part 1 without Part 0, they would already know
   the topic.

2. **Each part prepends on the previous one.** A reader who has only read up to Part N
   must be fully equipped for Part N+1. No concept in Part N+1 may rely on something
   not covered in Parts 0 through N.

3. **Each part has a one-sentence purpose.** "After reading this part, the user can
   [do specific thing]." If you cannot state this, the part boundaries are wrong.

4. **Group by mechanism, not by alphabet or popularity.** Concepts that share
   underlying logic belong together even if they seem superficially unrelated.

5. **End every part with a framework summary table.** Map the part's concepts to the
   chosen organizing framework dimensions. This reinforces the spine across all parts.

**Typical scope → part count:**
```
Sub-topic deep dive (e.g., "the GARCH family of models")    → 2–4 parts
Single focused topic (e.g., "neural networks")              → 4–7 parts
Broad domain (e.g., "quantitative finance")                 → 10–16 parts
Full discipline (e.g., "immunology")                        → 12–20 parts
```

### Step 2d — Write the Internal Plan

Before producing any content, internally create this plan for each part:
- Part title
- One-sentence purpose
- Key concepts included
- What gap (from Phase 1) this part fills
- What organizing framework dimensions it addresses

Do not show this plan to the user. Use it to write. Proceed immediately to Phase 3.

---

## Phase 3 — Write the Notes

### Output Format

**Default: JS files** — unless the user explicitly requests another format.

One file per 3–4 parts for long topics, or one file per part for very deep topics.

**File naming:**
```
part0_foundations.js
part1_<descriptive_name>.js
part2_<descriptive_name>.js
...
```

**Every JS file opens with:**
```js
// ============================================================
// PART N: TITLE IN CAPS
// One-sentence description of what this part covers.
// ============================================================

module.exports = [
  // content objects here
];
```

---

### JS Object Types — Complete Schema

```js
// ── STRUCTURE ──────────────────────────────────────────────────

// Marks the start of a new part (major division)
{ type: 'part', text: 'PART 0: TITLE OF PART' }

// Major section within a part (h2 level)
{ type: 'h2', text: 'Section Title' }

// Sub-section (h3 level — a specific concept or angle within a section)
{ type: 'h3', text: 'Concept Name or Angle' }


// ── CONTENT ────────────────────────────────────────────────────

// Core explanatory prose — the main teaching text
// Use template literals. Write in full paragraphs. No bullet lists here.
{ type: 'body', text: `Explanation goes here. Multiple sentences. Full paragraphs.` }

// Worked example — always real numbers, real names, no placeholders
// Show every calculation step. Interpret every result.
{ type: 'example',
  title: 'Descriptive title (what scenario, what question)',
  content: `Step-by-step working here. Interpret each result. Show the "this means..." conclusion.` }

// Callout box — for genuinely non-obvious insights, warnings, and definitions
// color: 'teal' = insight/implication   'red' = warning/mistake   
//        'navy' = formal definition     'purple' = advanced extension
{ type: 'callout',
  color: 'teal',
  title: '💡 What this actually implies',
  lines: [
    'First insight line — something the reader would not have concluded on their own.',
    'Second line only if needed — do not restate what was just explained in the body.'
  ]
}

// Comparison or summary table
{ type: 'table',
  headers: ['Column A', 'Column B', 'Column C'],
  rows: [
    ['row 1 col 1', 'row 1 col 2', 'row 1 col 3'],
    ['row 2 col 1', 'row 2 col 2', 'row 2 col 3']
  ]
}

// Optional: process or flow diagram (when a sequence or relationship needs visualising)
// Use plain text art — no Mermaid inside JS strings. Keep it simple and readable.
{ type: 'diagram',
  title: 'Title of diagram',
  content: `
  Input → [Step 1: name] → [Step 2: name] → Output
                                  ↓
                            [Branch condition]
                           /                  \\
                [Path A: result]        [Path B: result]
  ` }

// Framework summary — appears at the END of every part
// Columns match the chosen organizing framework dimensions
{ type: 'framework_summary',
  rows: [
    ['Framework dimension 1', 'How this part\'s concepts address it'],
    ['Framework dimension 2', 'How this part\'s concepts address it'],
    ['Framework dimension 3', 'How this part\'s concepts address it']
  ]
}
```

---

### When to Use Which Object Type

| Situation | Use |
|---|---|
| Teaching a concept | `body` — full paragraphs, no bullet lists |
| Showing a calculation or process step by step | `example` |
| A conclusion the reader would miss without prompting | `callout: teal` |
| A mistake that is easy to make and costly | `callout: red` |
| The precise technical/legal/formal definition | `callout: navy` |
| An advanced nuance or extension for the curious reader | `callout: purple` |
| Comparing multiple things on the same dimensions | `table` |
| A process, flow, or relationship that needs spatial layout | `diagram` |
| Mapping part concepts to the organizing framework | `framework_summary` |

**Never use `body` for bullet lists.** If the natural form of information is a list,
convert it to a `table`. If it cannot be a table, write it as connected prose.

---

### Markdown Output Mode

When the user explicitly requests markdown or `.md` output:

- Use standard headings: `#` for part title, `##` for h2, `###` for h3
- Callout boxes become blockquotes with bold title: `> **💡 Title:** text`
- Tables use standard markdown table syntax
- Diagrams use fenced code blocks with no language tag
- Framework summaries become tables with a `**Framework Check**` label above them
- File naming: `part0-foundations.md`, `part1-name.md` etc.

All writing rhythm rules (analogy → plain English → formal → example → limits →
connection) apply identically regardless of output format. Format is a container.
Understanding is the content.

---

### The Writing Rhythm — Non-Negotiable

Every concept must follow this rhythm. Full patterns, anti-patterns, and examples are
in `references/writing-style.md`. Summary here:

**1. Name the problem the concept solves**
Before introducing the concept, describe the situation where you would *need* it and
*feel its absence*. "Before X existed, the problem was..." The user must understand
the gap before the concept fills it.

**2. The analogy (mandatory)**
An everyday comparison requiring zero domain knowledge. The analogy must reveal the
*structure* of the concept — not just give it a name. Test: could the user derive one
non-obvious property of the concept from the analogy alone? If not, find a better analogy.

**3. Plain English explanation**
Explain the concept completely in natural language *before* introducing any formula,
symbol, or technical term. If the user cannot re-explain it in their own words after
reading this section, it is not plain enough yet.

**4. The formal version**
Now introduce the math, formula, technical definition, or precise terminology.
Immediately decompose every symbol, parameter, and operator. Never leave a formula
without explaining what each piece means and what happens when each piece changes.

**5. Worked example with real numbers**
A concrete, realistic scenario. Real names (companies, cities, people). Real magnitudes.
Walk through every calculation step. State the interpretation of every result:
"This means..." State counter-intuitive findings explicitly: "Notice that..."

**6. Limitations and failure modes**
State the assumptions the concept makes. Describe a realistic situation where each
assumption breaks. Explain what happens to the concept's output when it breaks.
State what to use instead. A student who only knows when a tool works will be
blindsided by its failures.

**7. Connection forward**
End with one sentence connecting this concept to the next. Name the next concept and
explain *why it was invented* — what gap it fills that this concept left open.

---

## Phase 4 — Completeness Check

Run this mentally before producing any file.

**Coverage:**
- Every user-provided keyword is covered, understood, and connected to the bigger picture
- Prerequisite concepts the user didn't mention have been added
- Part 0 → Part N is an unbroken chain — no concept relies on something unintroduced

**Depth:**
- After reading this, can the user apply each concept independently?
- Is there at least one worked example for every quantitative or process-oriented concept?
- Is every "why" (mechanism) explained, not just every "what" (definition)?

**Flow:**
- Each part depends on and builds from all previous parts
- The organizing framework appears in every part's summary table
- Every major section ends with a forward connection

**Style:**
- Every abstract concept has an everyday analogy
- Every formula is decomposed immediately (no orphaned symbols)
- Worked examples use real names, real numbers, realistic scenarios
- Every major concept documents its assumptions and failure modes

---

## Coverage Standards

These are non-negotiable regardless of domain.

**Every major concept must have:**
- The problem it solves (stated before the definition)
- An everyday analogy that reveals structure
- A worked example with real numbers or names
- Its key assumptions — explicit, not implied
- At least one failure mode: what breaks it and what happens when it breaks
- A forward connection to the next concept

**Every part must have:**
- An opening motivation paragraph ("Why are we learning this now, and how does it
  connect to what came before?")
- At least one example that spans multiple concepts from within the part
- A `framework_summary` table at the close

**The full document must have:**
- Part 0 as pure foundations — always, even for advanced keyword inputs
- At least one applied synthesis section every 4–5 parts — a realistic scenario
  where the user sees multiple concepts working together in practice
- Forward connections at the end of every major section and every part

---

## Key Principles

**The user's keyword list is the minimum, not the maximum.** Add everything a competent
practitioner would need that wasn't listed. The gaps are usually more important than
what was given.

**Never write a definition without a reason.** Every concept is introduced because it
solves a specific problem that the reader has already been made to feel.

**The analogy must do real work.** If you cannot state what structural property the
analogy shares with the concept, the analogy is decoration. Find one that teaches.

**Comprehensiveness is the default.** A long, complete document that can be studied
once is worth more than a short summary that requires constant supplementation.

**Adapt the framework and structure. Never adapt the writing rhythm.** Domain type
determines the organizing framework, part structure template, and tone. The seven-step
writing rhythm (problem → analogy → plain English → formal → example → limits →
connection) is universal. It never changes.
