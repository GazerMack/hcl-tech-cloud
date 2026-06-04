# Domain Adapters Reference

How to adapt the organizing framework, part structure, and tone for different types of
subjects. The writing rhythm (problem → analogy → plain English → formal → example →
limits → connection) is universal and never changes. What this file governs is everything
else: what the spine of the notes looks like, how parts are sequenced, and what the
reader needs first.

---

## Step 1 — Identify the Primary Domain

Read the user's keywords. Ask three questions in order:

1. Is there formal logic, quantification, or algorithmic process involved?
   → **Quantitative / Technical**

2. Is the subject about how something in the natural world actually *works* physically
   or biologically?
   → **Life Sciences / Mechanistic**

3. Is the subject primarily about human behaviour, decisions, events, or systems?
   → **Social / Historical / Interpretive**

4. Is the primary goal to enable the user to *do something well* (a skill or applied field)?
   → **Applied / Process / Skill-based**

If the topic clearly spans two types (e.g., "epidemiology" = mechanistic + quantitative,
"behavioural economics" = quantitative + social), identify the *primary* one and import
elements from the secondary. The primary domain determines the organizing framework.

---

## Domain Type 1: Quantitative / Technical

**Examples:** Mathematics, statistics, finance, machine learning, computer science,
physics, chemistry, engineering, algorithms, data science, econometrics

### What the reader needs first

The *problem* the field is trying to solve, stated in non-mathematical language. Then:
what the core *objects of study* are (returns, matrices, probability distributions,
particles, functions). Only then: notation, which is a compressed language for
describing things the reader already conceptually understands.

Never start with notation. Notation is the last thing to introduce, not the first.

### Organizing framework (default)

Build the spine around the decisions or tensions a practitioner navigates:

```
What are we trying to measure, model, or predict?
What assumptions does this require?
What does "working correctly" look like? How do we know?
What breaks it, and what do we do when it breaks?
```

Choose specific language for the domain:

| Domain | Organizing framework |
|---|---|
| Finance / Investing | What to buy / How much / What can go wrong / When to change |
| Machine Learning | What the model learns / What it cannot see / When it fails / How we validate |
| Statistical modelling | Data-generating process / What we estimate / Identification assumptions / Diagnostic checks |
| Software / Systems | What problem this solves / How it works / When it fails / When to use something else |
| Physics / Engineering | The phenomenon / The governing equations / Boundary conditions / Experimental validation |
| Algorithms | The problem to solve / The approach / Time and space complexity / Edge cases and failures |

### Part structure template

```
Part 0: Foundations — vocabulary, the problem the field addresses, core objects of study,
         and the mathematical/logical language used (introduced after concepts, not before)

Part 1: The simplest model — usually linear, usually named, usually taught first for a reason.
         Why it works, what it assumes, what it produces.

Part 2: Where the simple model fails + the next model that fixes it. The failure is the
         motivation; the new model is the solution. Structure: problem → solution → tradeoff.

Part 3: More realistic models — adding time-variation, nonlinearity, multiple dimensions,
         or uncertainty. Each addition motivated by a failure of the previous version.

Part 4: Measurement, validation, and inference — how do we know if any of this is working?
         How do we estimate parameters? How do we test assumptions?

Part 5: The full applied workflow — end-to-end, with real constraints, real data, and
         real decisions. This is where isolated concepts become integrated practice.

Part N+: Domain-specific advanced topics as needed. Each motivated by a gap in Part N.
```

### Tone

Precise and intellectually honest. Show genuine appreciation for why the mathematics
works out the way it does — elegance in technical subjects is real and worth conveying.
"The remarkable thing about this formula is that..." is appropriate. Avoid false
informality that sacrifices precision.

When introducing abstract concepts, always ground them in the concrete first.
Move from specific to general, never from general to specific.

---

## Domain Type 2: Life Sciences / Mechanistic

**Examples:** Biology, medicine, physiology, neuroscience, pharmacology, biochemistry,
ecology, genetics, immunology, evolutionary biology, chemistry

### What the reader needs first

The *normal state*. You cannot understand disease without understanding health. You
cannot understand what a drug does without understanding the receptor it targets in
its baseline state. You cannot understand an ecological disruption without understanding
the baseline ecosystem. Always begin with the baseline before introducing perturbations.

### Organizing framework (default)

```
Normal state: What does this look like when everything is functioning correctly?
Mechanism of disruption: What goes wrong, and exactly how does it happen, step by step?
Detection: How do we recognise that something has gone wrong?
Intervention: What do we do, and why does that specific intervention work at the mechanistic level?
Outcomes and limits: What can we fully correct, what can we only manage, and what remains beyond reach?
```

This framework applies whether the topic is a disease, a drug, an ecological relationship,
a metabolic pathway, a developmental process, or an organ system.

### Part structure template

```
Part 0: The baseline — normal anatomy, normal physiology, normal biochemistry, or normal
         ecology as relevant. The reader must know the healthy/normal state before any
         perturbation makes sense.

Part 1: The key players — the molecules, cells, tissues, organisms, or systems that
         matter specifically for this topic. What they are, what they normally do,
         and how they interact under normal conditions.

Part 2: The normal process in full detail — step by step, mechanism by mechanism.
         This is the most important part for mechanistic understanding. Never summarise
         this; walk through it completely.

Part 3: Disruption — what disturbs this process, how the disruption propagates through
         the system, and what the downstream consequences are.

Part 4: Detection and measurement — how we observe what we cannot directly see. The
         tools, biomarkers, signals, and diagnostic criteria.

Part 5: Intervention — what we can do and why it works at the mechanistic level. For
         medicine: drugs, procedures, lifestyle. For ecology: conservation, management.

Part 6: Limits, open questions, and the frontier — what remains unknown, contested,
         or beyond current capability.
```

### Tone

Wonder at the complexity of living systems. The appropriate attitude is: "The remarkable
thing is that this works at all, given how many things have to go right simultaneously."
Biological and medical systems are deeply interesting — let this come through. Avoid
clinical detachment that reduces living processes to abstract diagrams.

For human biology and medicine specifically: remember the reader is often thinking
about themselves or someone they care about. The stakes are personal. Write accordingly.

### Analogy strategy for life sciences

Engineering analogies work exceptionally well:
- Receptors and ligands → lock and key
- Feedback regulation (hormones, blood glucose) → household thermostat
- Protein synthesis → assembly line with quality control
- Immune system → border security with memory of prior threats
- Neural signal propagation → electrical wiring with relay stations
- Kidney filtration → water treatment with selective membranes

Use these freely. They make abstract molecular and cellular processes tangible.

---

## Domain Type 3: Social / Historical / Interpretive

**Examples:** History, economics, political science, law, sociology, philosophy,
anthropology, ethics, literature, cultural studies

### What the reader needs first

*Context.* A historical event, a philosophical argument, or a legal doctrine cannot be
understood in isolation. It has a before and an after; it was produced by specific people
with specific motivations under specific conditions. Establishing that context is not
optional background — it is the foundation on which everything else rests.

### Organizing framework (default — general)

```
What happened, was argued, or was decided?
Why did this emerge here and now? (the forces, conditions, and actors)
Who was affected, and how did different groups experience it differently?
What changed as a result — immediately and in the long run?
What does this tell us about human behaviour, institutions, power, or ideas?
```

**For law specifically:**
```
What is the rule? (the black-letter law or doctrine)
Why does this rule exist? (the policy rationale, the problem it was designed to solve)
How is it applied? (the tests, standards, cases, and their interpretation)
Where are the edges and disputes? (ambiguities, competing interpretations, evolving application)
What happens when it fails or is abused? (enforcement gaps, perverse incentives, historical failures)
```

**For philosophy / ethics:**
```
What is the central question or problem?
What are the main positions and their strongest arguments?
What is the strongest objection to each position?
Where does the debate currently stand, and why has it not been resolved?
What practical implications follow from each position?
```

### Part structure template

```
Part 0: The world before — what was the state of affairs before this topic emerged?
         What problem, tension, or situation prompted the development of this event,
         idea, institution, or doctrine?

Part 1: The central phenomenon — what exactly is this? Define it precisely while
         acknowledging genuine complexity or contested definitions.

Part 2: Origins and causes — where did it come from, why did it emerge when and where
         it did, and what forces produced it?

Part 3: Mechanics and development — how does it work, how did it unfold, what were
         its key phases, turning points, or internal logic?

Part 4: Consequences — what did it produce, both intended and unintended?
         Who gained and who lost?

Part 5: Debates and interpretations — where do serious thinkers or practitioners
         genuinely disagree, and why has the debate not been resolved?

Part 6: Legacy and present relevance — why does this still matter, what has changed
         since, and what has stayed the same?
```

### Tone

Engaged, intellectually honest, and genuinely curious about disagreement. Social science
and history involve real uncertainty — do not paper over it. "Historians disagree about
this because..." is not a failure of the notes; it is an important truth about the subject.

Show the reader *how to think* about contested questions, not just what the consensus
view is. A reader who finishes these notes should be able to construct and evaluate
arguments, not just repeat positions.

Avoid false certainty. Avoid false equivalence. Both are failures of intellectual
honesty in different directions.

### Analogy strategy for social / historical topics

Use everyday social situations: negotiations, reputation dynamics, collective action
problems, incentive structures, group identity formation. Avoid technical analogies —
they make social phenomena feel more mechanistic than they are, and they alienate readers
who are less technically inclined.

---

## Domain Type 4: Applied / Process / Skill-based

**Examples:** Investing and portfolio management, business strategy, product management,
design, negotiation, writing, cooking, project management, any field where the goal is
*competence at doing something*

### What the reader needs first

A clear picture of what *doing this well* looks like, and what *doing it badly* costs.
Applied learning is goal-oriented — the reader wants capability, not just knowledge.
Opening with real success and failure cases sets the stakes and motivates everything
that follows.

### Organizing framework (default)

```
What am I trying to achieve and under what constraints?
What does the situation look like right now? (diagnosis and assessment)
What are my options, and how do I evaluate them?
What do I actually do — specifically, step by step?
How do I know if it worked?
What do I do when it doesn't work?
How do I improve over time?
```

### Part structure template

```
Part 0: What this field is really about — the actual goal (not the stated goal), the real
         constraints, the key decisions that distinguish good from poor practitioners,
         and what failure actually looks like.

Part 1: The diagnostic — how to read a situation correctly before acting. Most applied
         failures stem from misdiagnosis, not from wrong technique applied to correct diagnosis.

Part 2: The core toolkit — the main methods, frameworks, heuristics, and mental models.
         Each introduced with its use case, its assumptions, and its failure modes.

Part 3: The full process — how a practitioner actually works through a complete real problem,
         from diagnosis through decision through execution. Show the messy reality,
         not the idealised textbook version.

Part 4: Common failures — what goes wrong, why it goes wrong, and what it looks like
         before it becomes obvious. Prevention is always more effective than recovery.

Part 5: Edge cases and advanced situations — the scenarios that beginner frameworks
         handle poorly, and what experienced practitioners do differently.

Part 6: Getting better — deliberate practice, feedback loops, what to measure, and
         how to build the pattern recognition that separates novices from experts.
```

### Tone

Practical, direct, honest about difficulty. "This sounds simple but it is not, because..."
is the right register. Respect the reader's goal of actually being able to do the thing.
Do not just describe the skill — put the reader in situations where they can see
themselves applying it.

The reader of applied notes is trying to build capability, not pass a test. Write as
if they will close the document and immediately try to do what they just read about.
What do they most need to know in that moment?

---

## Mixed Domains — How to Handle

Many real topics span two domain types. Examples:

| Topic | Primary | Secondary | How to blend |
|---|---|---|---|
| Immunotherapy for cancer | Life Sciences | Applied (medicine) | Use life sciences framework; add clinical evidence evaluation and treatment decision logic from applied |
| Monetary policy | Quantitative (economics) | Social (political economy) | Use quantitative framework; add sections on political constraints and distributional effects |
| Constitutional law | Social (law) | Applied (advocacy) | Use law framework; add applied sections on how to construct and evaluate arguments |
| Climate science | Life Sciences / Quantitative | Social (policy) | Mechanistic core; add quantitative modelling section and social/policy implications |
| Behavioural economics | Social (economics) | Quantitative | Social and historical origins of the field; quantitative methods for measuring biases |

**Process for mixed domains:**
1. Identify which domain drives the *core mechanism or logic* (this is primary)
2. Identify which domain the user cares about for *application* (this shapes the endpoint)
3. Structure the notes around the primary domain's framework
4. Import the secondary domain's concerns explicitly into Part 5 or 6 as a dedicated section
5. Tell the reader at the start of Part 0 which framework you chose and why

---

## Calibrating Depth

The user has specified: default to depth sufficient for independent real-world application.
This means different things in different domains:

**Quantitative / Technical:**
The reader should be able to implement from scratch, interpret results, detect assumption
violations, and know what to do when the model breaks. Not just "know what GARCH is" —
but be able to specify, estimate, interpret, and critique a GARCH model.

**Life Sciences:**
The reader should be able to explain the mechanism in full detail (not just the outcome),
recognize when the normal process is going wrong before it becomes obvious, and understand
why an intervention works at the mechanistic level (not just that it is prescribed).

**Social / Historical:**
The reader should be able to construct a well-reasoned argument, evaluate competing
interpretations with appropriate scepticism, and apply the historical or theoretical
lesson to new situations they have not been shown. Not just recall what happened —
but understand *why* it happened and *what that implies* for analogous situations.

**Applied:**
The reader should be able to make real decisions in real situations, recognize common
failure patterns *before* they fully develop, and improve their performance through
deliberate feedback. Not just "know the framework" — but be able to apply it under
conditions of ambiguity, time pressure, and incomplete information.

**When uncertain about depth:** Go deeper. The user can skim sections they already know.
Shallowness cannot be corrected without rewriting. Depth is always recoverable; its
absence never is.

---

## The Framework Summary Table — Format by Domain

Every part ends with a `framework_summary` object. The columns change by domain:

**Quantitative:**
```js
{ type: 'framework_summary', rows: [
  ['What we are measuring / modelling', 'How this part\'s concepts contribute'],
  ['Key assumption introduced', 'What this part assumes that must hold'],
  ['Failure mode introduced', 'When this part\'s tools break down'],
  ['Fix or next step', 'What comes next to address the failure'],
]}
```

**Life Sciences:**
```js
{ type: 'framework_summary', rows: [
  ['Normal state', 'What this part adds to the baseline picture'],
  ['Mechanism of disruption', 'What this part explains about how things go wrong'],
  ['Detection', 'What observable signals or diagnostics this part introduces'],
  ['Intervention / Response', 'What this part suggests we can do about it'],
]}
```

**Social / Historical:**
```js
{ type: 'framework_summary', rows: [
  ['What happened or was argued', 'This part\'s specific contribution'],
  ['Why it emerged', 'The forces and conditions this part explains'],
  ['Who was affected', 'The groups and differential impacts covered'],
  ['Long-run significance', 'Why what this part covers still matters today'],
]}
```

**Applied:**
```js
{ type: 'framework_summary', rows: [
  ['Goal and constraints', 'What this part clarifies about what we are trying to achieve'],
  ['Diagnosis', 'What this part teaches the reader to recognise and assess'],
  ['Decision and action', 'What this part says to actually do'],
  ['Evaluation and improvement', 'How this part helps the reader get better over time'],
]}
```
