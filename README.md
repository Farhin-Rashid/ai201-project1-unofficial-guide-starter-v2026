# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **Name:** Farhin Rashid
>
> **Corpus used:** city_guides

---

# Unit 1

## What This Does

I used the city_guides corpus to complete this unit. The questions this system answers are things a tourist would look up before visiting these cities. It tells you which cities are walkable, which seasons are the best time to visit, and how to get there.

## Chunking Strategy

**Chunk size:** ~1 sentence of variable lenght  
**Overlap:** 0 characters

When inspecting the city_guides corpus in Milestone 1, I noticed the documents are forum-style responses consisting of factual sentences rather than opinion-based like in advice_threads. Initially, it seemed straightforward to have entire documents as chunks, as they were very short, but later I decided that sentence-level splitting works better for vector similarity matching because each sentence answers a distinct factual question, such as "June and September are the sweet spots for visiting Halden Bay."

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: ` guide_accessibility.md#0 ` — produced by: `chunker.py::split_documents`

```
# Getting around the region with limited mobility

An honest assessment rather than a promotional one.
```

**Chunk 2** — source: ` guide_corry_vale.md#7` — produced by: ` chunker.py::split_documents`

```
There is one taxi, based in the largest village, and it must be booked a day ahead.
```

**Chunk 3** — source: `  guide_elder_ness.md#25` — produced by: `chunker.py::split_documents`

```
The nearest full hospital is in Brightwater; there is
a minor injuries unit locally with limited hours.
```

**Chunk 4** — source: ` guide_kestrelford.md#18` — produced by: `chunker.py::split_documents`

```
## When to go

Late spring and early autumn.
```

**Chunk 5** — source: `guide_regional_transport.md#10 ` — produced by: `chunker.py::split_documents`

```
## Driving

Roads are good between the towns and poor on the approaches to both Kestrelford
and Halden Bay.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
"Is Brightwater walkable?"
**Answer:**

```

Yes, Brightwater is walkable; the town can be crossed end to end in about 35 minutes. This information comes from `guide_brightwater.md`.

Sources retrieved: guide_brightwater.md, guide_kestrelford.md, guide_regional_transport.md, guide_walking.md
```

**My relevance cutoff:** 0.5

I tested the system with questions that are answered in the corpus and questioned that are not. The first group where a correct response was given all had a best distance below 0.5, and that is how I picked my relevance cutoff. The later group all had high best distance scores (above 0.8).

| Question | In corpus? | Best distance |
|---|---|---|
|What is the least accessible city?  | yes | 0.555 |
|"Several riverside businesses in Brightwater close entirely during which months?" | yes | 0.178 |
|"How to get to Halden Bay?" | yes | 0.295 |
|"When is it best to visit Halden Bay?" | yes | 0.347 |
|"What to see in Corry Vale?" | yes | 0.451 |
|"Is Brightwater walkable?" | yes | 0.435 |
|"What is the capital of Mongolia?" | no | 0.887 |
|"What is the recommended dosage of ibuprofen for a headache?" | no | 0.829 |
|"How do I change the oil in a diesel engine?" | no | 0.897 | 
|"Who won the 1994 World Cup?" | no | 0.903 |
|"How do I write a for loop in Rust?" | no | 0.853 |


## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I asked Gemini about certain commands to use since I'm not completely familiar with the command prompt.
I used it when typing the wrong commands gave some unintended output, for example, when I didn't pull from origin before committing my changes.
This helped me remember to do so next time.

**2.**
I asked Gemini to write the chunking function that I wanted and how to execute it. It explained what functions to use and what each line did.
It used different variable names, so I had to read through chunker.py myself and name the variables correctly.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 1/5 | 1/5 | 1/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks are clear and concise | 4 of 5 | 5/5| 5/5 | 5/5 | MET |
| 5. Answers are generated reasonably quickly | 4 of 5 | 3/5 | 3/5 | 4/5 | MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 1/5 | 1/5 | 1/5 | MISSED |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks are clear and concise | 4 of 5 | | | | |
| 5. Answers are generated reasonably quickly | 4 of 5 | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
