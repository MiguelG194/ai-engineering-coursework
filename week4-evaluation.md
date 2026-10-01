# Week 4 Assignment: Evaluating and Comparing Two Models

## Part 1: Set Up Your Comparison

Choose two models that differ in a way worth comparing: two sizes, two providers, etc.

| | Model | Provider | Why you picked it |
|---|---|---|---|
| Model A | qwen3.5-27b | Novita | I chose this model as the base to test how having larger parameters affects performance while keeping the model family and provider the same. |
| Model B | qwen3.5-397b-a17b | Novita | I chose a much larger model to see if there are any noticeable differences with performance or output quality. |

Write one prompt for the task and use it, unchanged, for both models on every ticket. If the prompt varies between models, you won't know whether a difference in results came from the model or the prompt. Keep the prompt simple; tuning it isn't the goal this week as that will be part of our next weeks topic. You will need to include enough details though that the model knows what should be returned, given a support ticket.

```
Categorize the provided support ticket.

Return ONLY json as your answer using this format:

{"category": "billing", "urgency": "high", "needs_human": true}

category: The type of support ticket. It can be either billing, technical, account_access, feature_request, or other.

urgency: How urgent the ticket is. It can be either low, medium, or high.

needs_human: Set to true if the ticket needs a human agent rather than an automated reply. 

Support ticket:
[Insert Here]
```

---

## Part 2: Define Your Criteria

Write three evaluation criteria for this task. At least one should be about something other than raw correctness, such as speed or how clean the output format is. Give a measurement method for each and the threshold you'd consider good enough to ship.

Set the thresholds now, before you run anything. Deciding what counts as success after you've seen the results defeats the purpose.

| # | Criterion | How you'd measure it | "Good enough" threshold |
|---|---|---|---|
| 1 | Classification Correctness | Compeare each model's category, urgency, and needs_human evaluation aganist the provided reference answers. 1 point for each correct field, with a total of 3 points possible per ticket. | At least 15 of 18 points are required for the model to be ready to be shipped. |
| 2 | JSON/Output Format Correctness | Check whether every response is valid JSON and contains exactly the three required fields with allowed values. | To be considered good enough, the model must correctly format all of the 6 tickets. |
| 3 | Consistency | Repeat the exact same ticket with the model three times and check whether it produces the same classification each time. | The model must produce the same classification across all three attempts for at least 5 of the 6 tickets to be considered good enough to ship. |

---

## Part 3: Run Both Models

Here are six tickets with the correct answer for each. Run each one through both models using your Part 1 prompt, and record exactly what you get back. Copy it verbatim, including any extra words or formatting quirks. Those details matter for scoring. Do not give the model the refernece, that is meant for you.

| ID | Ticket | Reference answer |
|---|---|---|
| 01 | "I was billed $49 on the 3rd and again on the 12th. I only have one subscription. Please refund the duplicate." | `{"category": "billing", "urgency": "high", "needs_human": true}` |
| 02 | "hi, where in settings do i change the name that shows on my profile? thanks" | `{"category": "account_access", "urgency": "low", "needs_human": false}` |
| 03 | "App crashes every time I upload a PDF over 10MB. Been happening for three days." | `{"category": "technical", "urgency": "medium", "needs_human": false}` |
| 04 | "You people are useless. I've emailed four times about my refund and gotten nothing. I want my money NOW." | `{"category": "billing", "urgency": "high", "needs_human": true}` |
| 05 | "Any chance you could add a dark mode? The white background is rough at night." | `{"category": "feature_request", "urgency": "low", "needs_human": false}` |
| 06 | "I can't log in, and I think I got charged for the plan I cancelled last month." (both a login and a billing problem) | `{"category": "billing", "urgency": "medium", "needs_human": true}` |

Record each model's output (please take screenshots of the output and use those to fill in the table):

| ID | Model A output (verbatim) | Model B output (verbatim) |
|---|---|---|
| 01 | {"category": "billing", "urgency": "high", "needs_human": true} | {"category": "billing", "urgency": "high", "needs_human": true} |
| 02 | {"category": "account_access", "urgency": "low", "needs_human": false} | {"category": "account_access", "urgency": "low", "needs_human": false} |
| 03 | {"category": "technical", "urgency": "medium", "needs_human": true} | {"category": "technical", "urgency": "high", "needs_human": true} |
| 04 | {"category": "billing", "urgency": "high", "needs_human": true} | {"category": "billing", "urgency": "high", "needs_human": true} |
| 05 | {"category": "feature_request", "urgency": "low", "needs_human": false} | {"category": "feature_request", "urgency": "low", "needs_human": false} |
| 06 | {"category": "billing", "urgency": "high", "needs_human": true} | {"category": "billing", "urgency": "high", "needs_human": true} |

Note which model felt slower to respond.

Both took about the same amount of time, but certain tickets took longer. For example, ticket 6 took model 2 40 seconds longer than model 1. It could've been because it was thinking longer for a better response. However, both produced the same output despite the difference in time.

---

## Part 4: Score What You Got

Score the outputs two ways. Here's what each one means:

**Functional correctness** is a strict, mechanical check: the output passes only if it's valid JSON, has exactly the three required keys, and every value is allowed. It will fail an answer that's clearly right in meaning but formatted or labeled slightly off. Watch for that as you go.

**Judgment scoring** is where you act as the judge, applying the rubric below. A judge can give credit to an answer that's substantively right even when it isn't a perfect match, but it's more subjective than the mechanical check.

Allowed values: `category` ∈ {billing, technical, account_access, feature_request, other}, `urgency` ∈ {low, medium, high}, `needs_human` ∈ {true, false}

### 4a. Functional-correctness check

Mark each output pass or fail. Where it fails, say why.

| ID | A: pass/fail | A — reason if fail | B: pass/fail | B — reason if fail |
|---|---|---|---|---|
| 01 | pass | _____ | pass | _____ |
| 02 | pass | _____ | pass | _____ |
| 03 | pass | _____ | pass | _____ |
| 04 | pass | _____ | pass | _____ |
| 05 | pass | _____ | pass | _____ |
| 06 | pass | _____ | pass | _____ |

Functional-correctness score — Model A: 6 / 6   Model B: 6 / 6

### 4b. Judgment scoring

Score each output 1–5:

> **5** — Correct classification, clean and usable output.
> **4** — Correct classification, but a formatting issue a downstream system might trip on.
> **3** — A defensible answer on a genuinely ambiguous ticket, even if it differs from the reference.
> **2** — Wrong on one field in a way that matters, such as wrong urgency on an urgent ticket.
> **1** — Wrong category, or unusable output.

| ID | A: judge score | B: judge score |
|---|---|---|
| 01 | 5 | 5 |
| 02 | 5 | 5 |
| 03 | 5 | 2 |
| 04 | 5 | 5 |
| 05 | 5 | 5 |
| 06 | 2 | 2 |

Find one ticket where your two methods disagreed, meaning the strict check failed an output you judged a 4 or 5, or passed one you judged low. Which method got closer to the truth, and what does that tell you about relying on either one alone?

Tickets 3 and 6 caused differences in the evaluaton methods. Each model produced correct JSON with no extra test/explanation included. However, model B failed the comparison test with the reference answer on ticket 3. Both models failed the comparison with the reference answer to ticket 6.

Even though correct JSON format was returned, some answers were not the same as the reference answer. Having the correct format is important, but it is not very useful if the generated response is not correct in meaning.

---

## Part 5: Recommendation and Reflection (200–300 words)

Address each of these:

- Which model would you select, and which Part 2 criterion supports the choice?
- What did you give up by choosing it (the tradeoff)?
- You just scored twelve outputs by hand. Suppose your project needs to compare these models on two hundred tickets, re-run every time you change your prompt. What goes wrong if you keep doing it by hand? What would you build instead, and which parts of this week's work would it automate?
- Give one reason six tickets isn't enough to trust this decision.

Based on the results, I would go with Qwen3.5-27B. It is smaller, yet it still produced results similar to the much larger Qwen3.5-397B-A17B. In the functional correctness section, both models produced valid JSON for every ticket, earning full scores. However, both models incorrectly classified the urgency of some tickets in the second test. Qwen3.5-27B performed slightly better in classifying the tickets and was also faster at generating its results. Based on these results, Qwen3.5-27B demonstrated better efficiency in the experiment.

Even though I chose Qwen3.5-27B, Qwen3.5-397B-A17B has a much larger parameter size. It is possible that the sample size was too small to demonstrate the larger model’s advantages. By choosing the smaller model, I may be sacrificing some of the larger model’s potential capabilities, particularly when dealing with more difficult tickets.

One problem I might encounter when testing hundreds of tickets is accidentally mistyping a prompt or reusing a ticket. It would also be time-consuming to manually review each model’s output and compare it against the reference answer. Instead, I could use the Hugging Face API to automate sending prompts to each model. I could keep the main prompt consistent while changing the ticket being evaluated. I could also automate the evaluation process by using another LLM as a judge to compare the outputs against the reference answers. However, this would introduce additional challenges, such as potential bias and inaccuracies in the judge model. Automating these tasks would make the evaluation process more consistent, efficient, and reproducible.

One reason six tickets is not enough to trust this decision is that the sample size is very small. While having some tests is better than nothing, six tickets may not represent the full range of tickets the system could encounter. We also did not account for the difficulty of the tickets. If the test included a larger and more varied set of tickets, especially harder ones, we might see different results or see the larger model perform better.