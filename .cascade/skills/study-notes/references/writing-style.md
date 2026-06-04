# Writing Style Reference

The exact sentence-level patterns that produce study notes people can actually learn from —
not just look things up in. Read this entirely before writing any content. Every pattern
here exists because its opposite reliably produces notes that feel thorough but leave the
reader unable to use what they have read.

---

## The Core Distinction

Every concept can be taught in two ways:

**Way 1 — Reference style (produces recognition):**
> Entropy: H(X) = −Σ P(x) log P(x). Measures average uncertainty of a random variable.
> High entropy = high uncertainty. Shannon developed this in 1948.

After reading this, the user can recognise the term and repeat the definition.
They cannot explain *why this formula works*, *what it feels like to have high or low
entropy*, or *when they would actually use it*.

**Way 2 — Understanding style (produces comprehension):**
> Before Shannon, there was no way to put a number on how "informative" a message was.
> Consider two weather forecasts: "Tomorrow will be sunny or rainy" vs. "There will be
> a solar eclipse at 3:47 PM tomorrow." Both statements are true. But the second one
> tells you far more — because it describes something you had no reason to expect.
> Shannon's insight was that *surprise* and *information* are the same thing. A message
> that tells you what you already knew communicates nothing. A message that tells you
> something that had only a 1-in-10,000 chance of being true communicates a great deal.
> Entropy makes this precise: it measures the average amount of surprise in a random
> variable. A fair coin has maximum entropy — you are maximally surprised by every flip,
> because either outcome was equally likely. A coin that always lands heads has zero
> entropy — you are never surprised at all.

After reading this, the user understands *why entropy is measured the way it is*, can
*generate examples of high and low entropy situations*, and could *explain it to someone
else without using the formula*.

The second version is always longer. It is always worth it.

---

## Pattern 1: Problem Before Solution

The most common error in technical note-writing: introducing a concept before the user
feels the need for it. Without the need, the concept feels arbitrary.

**Structure:**
1. Describe a situation where you would be *stuck without this concept*
2. Show what the old approach produced and why it was insufficient
3. *Then* introduce the concept as the solution to the problem you just created

**Anti-pattern:**
> GARCH is a model for time-varying volatility. It accounts for volatility clustering
> in financial time series.

**Correct:**
> For decades, analysts modelling financial markets made one silent assumption: that
> the variance of returns was stable over time. Monday and Friday were treated as
> equally uncertain. Calm 2006 and chaotic 2008 were treated as having the same
> underlying riskiness. The problem became unmistakable during the 2008 financial
> crisis: risk models calibrated on quiet periods predicted that a 5% single-day
> decline was essentially impossible — yet the market produced such moves repeatedly,
> week after week. The models were wrong not because the math was bad, but because
> the assumption of constant variance was wrong. GARCH was built to fix this specific
> failure.

Notice: the concept is introduced in the last sentence, *after the reader has been made
to feel the problem*. At this point, they want the solution. Before this point, they
would not have understood why it mattered.

---

## Pattern 2: Analogies That Teach, Not Just Name

A weak analogy gives a concept a new name without adding understanding:
> "Think of beta as a sensitivity dial — turn it up, and everything gets louder."

This is decorative. It tells you beta amplifies, but not what, why, or when it matters.

A strong analogy reveals the *structural relationship* — the reader can derive properties
of the concept from the analogy alone:

> "Think of beta as a lever. The market is the force applied at the handle. Your stock
> is the weight at the other end. If the lever arm ratio (beta) is 1.5, every unit of
> market movement produces 1.5 units of stock movement — in either direction. The lever
> does not care whether you push down or lift up. A market that rises 10% moves a beta-1.5
> stock up 15%. A market that falls 10% moves the same stock down 15%. The amplification
> is perfectly symmetric — and this is the property that most people initially miss. They
> think high-beta stocks are great to own in bull markets, which is true. They forget that
> the same lever works just as powerfully in the other direction."

Test for a good analogy: *Can the reader derive at least one non-obvious property of
the concept from the analogy, without any additional explanation?* Here: the reader can
derive symmetry of amplification, the fact that leverage works against you as much as for
you, and that the leverage ratio stays constant regardless of direction. The lever analogy
teaches all three without stating them explicitly.

If you cannot pass this test, the analogy is decorative. Find a different one.

**Good analogy sources by domain:**

| Domain | Useful analogy territory |
|---|---|
| Quantitative / Mathematical | Physical systems (levers, thermostats, springs, waves, pressure) |
| Biological / Medical | Engineering systems (assembly lines, locks and keys, thermostats, postal systems) |
| Historical / Social | Human social situations (negotiations, reputation, collective action problems) |
| Applied / Process | Sports, cooking, navigation, construction, medicine |

Avoid using concepts from within the domain as analogies for other concepts in the same
domain. (Don't explain options using futures. Don't explain proteins using DNA. The
reader doesn't understand either of them well enough for the analogy to work.)

---

## Pattern 3: Formula Decomposition — No Orphaned Symbols

**Rule:** Every symbol, subscript, operator, and parameter that appears in a formula
must be explained immediately after the formula. Then at least one sentence about what
happens when each key parameter increases or decreases.

**Anti-pattern:**
> σ²_t = ω + α ε²_{t-1} + β σ²_{t-1}

**Correct:**
> Today's variance is built from three ingredients:
>
>   σ²_t = ω  +  α × ε²_{t-1}  +  β × σ²_{t-1}
>
> ω (omega) — the baseline. How much variance you would expect on any ordinary day
> if nothing dramatic had recently happened. The market's "resting heart rate."
>
> α × ε²_{t-1} — the shock response. α controls how strongly variance reacts to
> the most recent return surprise (ε, the residual from yesterday's return). If
> yesterday's move was large, this term spikes. High α = a market that reacts violently
> to fresh news. Low α = a market that absorbs surprises without much volatility change.
>
> β × σ²_{t-1} — the memory. β controls how much of yesterday's variance forecast
> carries forward into today. High β = volatility is persistent — once the market
> becomes stormy, it stays stormy for many days. Low β = shocks die out quickly.
>
> The sum α + β is called volatility persistence. If it equals 1, volatility becomes
> a random walk and never mean-reverts (IGARCH). In practice for equities, α + β ≈
> 0.97–0.99 — volatility shocks die out very slowly, taking weeks rather than days.

Apply this pattern to every formula. Even if a symbol seems obvious (like T for time or
N for sample size), state it. Readers build confidence from seeing that nothing is hidden.

---

## Pattern 4: Worked Examples — Fully Realised

**Rules for every worked example:**
1. Use a realistic scenario with a name (a company, a city, a person, a specific date)
2. Use realistic magnitudes (returns in the right ballpark, prices plausible, timeframes real)
3. Show every calculation step, including intermediate steps that seem obvious
4. State the plain-English interpretation of every numerical result
5. State counter-intuitive findings explicitly ("Notice that..." or "The surprising thing is...")
6. End with: "What would change if [one condition were different]?" — to extend understanding

**Anti-pattern:**
> Example: μ = 8%, σ = 15%, r_f = 3%. Sharpe = (8–3)/15 = 0.33.

**Correct:**
> Let's evaluate two real strategies side by side.
>
> Strategy A — a mid-cap equity fund:
>   Annual return over 5 years: 16%
>   Annual volatility over 5 years: 24%
>   Risk-free rate (Indian T-bill): 6.5%
>   Excess return: 16% − 6.5% = 9.5%
>   Sharpe ratio: 9.5% / 24% = 0.396
>
> Strategy B — a balanced equity-debt fund:
>   Annual return over 5 years: 11%
>   Annual volatility over 5 years: 9%
>   Excess return: 11% − 6.5% = 4.5%
>   Sharpe ratio: 4.5% / 9% = 0.500
>
> Strategy A earned nearly 5% more per year in raw returns. Most investors would
> choose it. But on a risk-adjusted basis, Strategy B was the better deal: for every
> unit of risk accepted, it returned 0.50 units of excess profit, vs. only 0.40 for
> Strategy A.
>
> What this means practically: Strategy A was taking on 2.7 times more risk than
> Strategy B, but only earning 1.5 times more return. The extra risk was not being
> fairly compensated. An investor who had leveraged Strategy B modestly (1.5×)
> would have achieved similar absolute returns with less total risk than Strategy A.
>
> Notice: Sharpe ratio makes invisible leverage visible. A strategy with high returns
> but even higher risk can appear impressive until you account for what risk those
> returns cost.

Notice what the correct version does that the anti-pattern does not:
- Uses real names (India, T-bill) not placeholders (μ, r_f)
- Explains what the number *means*, not just what it *is*
- Draws a practical implication ("what this means practically")
- Surfaces a counter-intuitive finding ("notice: Sharpe makes invisible leverage visible")

---

## Pattern 5: Failure Modes — Making Knowledge Robust

Understanding when a concept fails is as important as understanding when it works.
A student who knows only the successes will be blindsided at exactly the wrong moment.

**Structure for every failure mode section:**

1. State the assumption explicitly (use the word "assumes")
2. Describe a realistic situation where that assumption breaks
3. Show what the model/concept produces when the assumption is violated
4. State the real-world consequence of trusting the wrong output
5. Name the fix: what to use instead, or how to adjust

**Example (correlation failing in a financial crisis):**

> Correlation assumes that the relationship between two assets is stable across market
> conditions — that the same co-movement you observed in calm markets will hold in
> turbulent ones.
>
> This assumption breaks in financial crises. Between 2004 and 2006, Indian IT stocks
> and real estate stocks had a correlation of roughly 0.25 — modest positive co-movement.
> Portfolio risk models called them modestly diversified. But during the 2008 global
> crisis, both fell together in a pattern consistent with correlation above 0.80.
> The "diversification" recorded in the risk model essentially vanished.
>
> What the model produced: a portfolio that appeared to have 30% diversification
> benefit turned out to have almost none — at exactly the moment the investor needed
> protection most.
>
> Real-world consequence: banks and funds that sized positions based on calm-period
> correlations found themselves far more concentrated than they believed when markets
> crashed. Losses far exceeded what risk models had projected as worst-case.
>
> The fix: copulas — specifically the Student-t copula — model *tail dependence*
> separately from average co-movement. They can capture the empirical fact that assets
> become more correlated in extremes, even if they appear uncorrelated in normal markets.

---

## Pattern 6: Connecting Forward — Building the Chain

Every major concept and every part must end with a forward connection. Not "next we
will cover X" — but *why X was invented and what gap it fills*.

**Anti-pattern:**
> In the next section, we will look at copulas.

**Correct:**
> Standard correlation — as we have just seen — captures the *average* relationship
> between two assets, measured across all market conditions. But in practice, the
> relationship that matters most is not the average: it is what happens in the extremes,
> when one or both assets are in crisis. Correlation, by construction, cannot tell you
> this. Copulas were developed specifically to model this tail behaviour — to separate
> "how assets usually co-move" from "how they co-move when things go badly wrong."
> That distinction, as we are about to see, is the difference between a risk model that
> survives a crisis and one that accelerates it.

This version tells the user: (1) what was just learned and its limitation, (2) the name
of the next concept, (3) why it was invented, and (4) why it matters that the reader
understands it. The reader now wants to continue.

---

## Callout Box Standards

Callout boxes interrupt flow. Use them only for genuinely important content that would
be buried or missed in the prose.

**`teal` — Insight / Implication:**
Something the reader would not have concluded on their own. A consequence of what was
just explained that reveals a non-obvious truth. "This means that..." or "The implication
is..." Do *not* use this to restate the main point of the section.

**`red` — Warning / Common Mistake:**
A specific, named error that is easy to make and has real consequences. If possible,
use a historical example of when this mistake caused a real failure. "This is exactly
what caused X to fail when Y happened."

**`navy` — Formal Definition:**
The precise, technical version of something that was just explained informally. Use
this *after* the informal explanation, never before. The reader is ready for precision
once they understand the concept.

**`purple` — Going Deeper:**
An advanced extension, nuance, or connection to related concepts. Optional for the
reader who wants more. Should feel like a reward. Clearly optional — the reader who
skips it misses nothing essential.

**Anti-pattern (avoid these):**
```
💡 Key Insight: Diversification reduces risk.   ← This is the headline, not an insight
⚠️ Warning: Don't use this incorrectly.         ← Too vague to be useful
```

**Correct:**
```
💡 Key Insight: The Kelly criterion and mean-variance optimization produce the same
   portfolio weights in continuous time — they are mathematically identical.
   This means every MVO practitioner is implicitly running Kelly whether they know it or not.

⚠️ Warning: The Gaussian copula assumes zero tail dependence — that assets become
   *less* correlated in extreme events. In practice, the opposite is true. Using it
   for credit portfolio risk (as banks did pre-2008) produces CVaR estimates that are
   catastrophically too low. Li's Gaussian copula model is credited with playing a
   significant role in mispricing CDO risk before the financial crisis.
```

---

## Tone

**Voice:** A knowledgeable friend who is also a great teacher. Not a textbook author.
Not a Wikipedia editor. Not a lecturer reading from slides.

**This means:**
- Sentences can open with "But," "And," or "So" when that is the natural flow
- Questions direct the reader: "Why does this matter? Because..."
- First-person plural is welcome: "Now that we have established X, we can see that..."
- Brief parenthetical asides for quick clarifications are fine
- Acknowledging difficulty is honest and helpful: "This is the subtle part..."

**This does not mean:**
- Imprecision in service of accessibility (accuracy is never sacrificed)
- Avoiding technical depth to maintain a conversational tone
- Using emoji in the main body text (only in callout titles as defined)
- Skipping failure modes because they are uncomfortable

**The goal:** A student should feel they are being taught by the most knowledgeable
person they know — one who respects their intelligence enough to give them the full
picture, and cares enough about their understanding to make every step accessible.

---

## Length

There is no upper bound on section length when content is genuinely needed. There is a
lower bound:

| Element | Minimum to be useful |
|---|---|
| Explanation of any major concept | 3 full paragraphs |
| Analogy section | 2–3 sentences showing structural similarity |
| Worked example | 5 explicit steps with interpretation |
| Failure mode section | All 5 elements (assumption, break, output, consequence, fix) |
| Forward connection | 2–3 sentences — what was learned, what comes next, why it matters |
| Callout box | At least 2 sentences — if you cannot say 2 sentences, it should not be a callout |

If you find yourself writing very short sections across multiple concepts, you are
producing a glossary. A glossary is not the goal. Merge short concepts into a section
with proper depth, or expand each until it genuinely teaches.

---

## What to Actively Avoid

**"This is important."** — Show *why* it is important. Let the reader conclude it.

**Orphaned concepts.** — Every concept introduced must connect to at least one other
concept explicitly. If it stands alone with no connection, either it does not belong or
it needs the surrounding context written.

**Lists of definitions.** — Five terms with one-sentence definitions is the worst
format for building understanding. If concepts must be introduced in a batch, introduce
each with at least its problem statement and analogy before moving to the next.

**"Obviously" (implicit or explicit).** — If something seems obvious to write, ask:
*is it actually obvious to someone encountering it for the first time?* If not, explain
it. If yes, you do not need to state it at all.

**Passive voice for key claims.** — "Correlation was found to be unreliable in crises"
is weaker than "Correlation fails precisely when you need it most — during crises."
Active voice makes the mechanism clear. Passive voice obscures who does what to whom.

**Summarising what was just explained in the body.** — Callout boxes are for new
implications and warnings, not for repeating the main point of the section. If the
callout could have been written before the reader read the section, it is a summary,
not an insight. Move it into the body.
