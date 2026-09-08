# Week 2 Assignment: Hugging Face Hub Scavenger Hunt

**Graduate Extension Included**

## Overview

Same fields I walked through in Monday's demo: parameter count/size, architecture family, license, tokenizer/vocab size. Pick 3 models, record those fields, run a tokenizer comparison across languages, check context window against this week's reading, then write a short reflection tying it back to a real project decision.

*Same order I used in Monday's demo: parameter count/size near the top of the card, architecture family in the description, license in the metadata, tokenizer/vocab size in tokenizer_config.json (or just test the model directly in a tokenizer tool).*

## How to Submit

1. Fill out this file directly (replace the `_____` placeholders and bracketed instructions with your answers).
2. Commit this file to the same GitHub repo you created for Assignment 1, using this exact filename: `week2-tokenizer-model-comparison.md`.
3. Push your commit, then submit a link to the file as instructed for this course.

---

## Part 1: Choose 3 Models

1. Go to huggingface.co/models.
2. Pick 3 models that actually make a meaningful comparison — not three near-identical variants of the same model. At least 2 different organizations/families, ideally a mix of sizes (small under ~3B, mid-size, larger).
3. Pick based on your own interests. Got a project idea? Use models you'd actually consider for it.

## Part 2: Record Your Findings

Where to find each field, if you get stuck:
- **Parameter count / size** — near the top of the card, sometimes right in the model's name (e.g. "7B" = 7 billion parameters).
- **Architecture family** — in the description text, or config.json under "Files and Versions."
- **License** — shown as a tag near the top, and always in the YAML metadata block.
- **Tokenizer / vocab size** — check tokenizer_config.json or config.json under "Files and Versions" for vocab_size. Can't find it? Note "not published" — that's a useful observation on its own.

| Model | Link | Parameter count / size | Architecture family | License | Tokenizer / vocab size |
|---|---|---|---|---|---|
| Model 1:  https://huggingface.co/openai-community/gpt2 | 124M | GPT2LMHeadModel | MIT | 50,257 | 1,024 tokens |
| Model 2: https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct | 1.54B | Qwen2ForCausalLM | Apache-2.0 | 151,936 | 32,768 tokens |
| Model 3: https://huggingface.co/XHToken/Spark-X2.5-4B | 4B | Spark2_5ForCausalLM | Apache-2.0 | 131,072 | 1,048,576 tokens |

## Part 3: Tokenizer Comparison Exercise

Use a tokenizer tool that supports multiple model families (tiktokenizer.vercel.app works) and test all 3 models with the same three inputs:

- **Test sentence (use this exact sentence for all 3 models):** "I love learning about artificial intelligence."
- **Language A:** translate the test sentence into a Latin-script European language — Spanish, French, German, whatever. Same translation across all 3 models.
- **Language B:** translate it into a non-Latin-script language — Japanese, Arabic, Korean, Hindi, your call. Same translation across all 3 models.

| Model | Test sentence tokens | Language A used | Language A tokens | Language B used | Language B tokens |
|---|---|---|---|---|---|
| Model 1 | 7 | Spanish | 12 | Japanese | 30 |
| Model 2 | 7 | Spanish | 9 | Japanese | 12 |
| Model 3 | 7 | Spanish | 10 | Japanese | 14 |

## Part 4: Context Window Check

For each model, look up its context window — the max tokens it can handle in one request. Usually on the card or in the config file.

| Model | Context window (tokens) | Source (URL or where you found it) |
|---|---|---|
| Model 1 | 1,024 | https://huggingface.co/openai-community/gpt2/blob/main/config.json |
| Model 2 | 32,768 | https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct/blob/main/config.json |
| Model 3 | 1,048,576 | https://huggingface.co/XHToken/Spark-X2.5-4B/blob/main/config.json |

**Now do the math for at least one model:** Chapter 2 is roughly 62 pages. Using ~500–600 words/page and ~0.75 words/token, estimate the total token count. Would the whole reading fit in that model's context window in one API call, with room left for a response? Show your work and your conclusion.

### Chapter 2 Token Estimate

The assignment estimates Chapter 2 at approximately 62 pages with 500–600 words per page.

#### Low Estimate

62 pages × 500 words/page = 31,000 words

31,000 words ÷ 0.75 words/token = 41,333 tokens

#### High Estimate

62 pages × 600 words/page = 37,200 words

37,200 words ÷ 0.75 words/token = 49,600 tokens

Therefore, Chapter 2 is estimated to contain approximately **41,333–49,600 tokens**.

| Model | Context Window | Can Fit Chapter 2? |
|---|---:|---|
| GPT-2 | 1,024 | No |
| Qwen2.5-1.5B-Instruct | 32,768 | No |
| Spark-X2.5-4B | 1,048,576 | Yes |

## Part 5: Comparison Reflection (300–400 words)

Answer all four:

- What's the biggest difference between your 3 models — size, architecture, license, tokenizer, something else?
- If you had to pick one for a real project, which one and why? Don't just say "the biggest one" — factor in license restrictions and whether the project actually needs that much size.
- Would your pick change for a multilingual or cost-sensitive use case, based on what you found in Part 3? Why or why not?
- Would your pick change for a use case involving long documents (full reports, long transcripts), based on the context window math in Part 4? Why or why not?

For this week's assignment, I chose these three models because they represent a small, medium, and large model. GPT-2 has 124 million parameters, Qwen2.5-1.5B has 1.54 billion, and Spark-X2.5-4B has 4 billion. The biggest difference that I noticed was how much the context windows varied between the models. GPT-2 has a 1,024-token context window, Qwen has a 32,768-token context window, and Spark has an extremely large 1,048,576-token context window. Before this assignment, I did not realize how quickly a context window of 1,024 or even 32,768 tokens could be used up by a large amount of text.

The tokenizer comparison also showed meaningful differences. After running the Python script, I found that all three models used 7 tokens for the English sentence, but GPT-2 used more tokens for both Spanish and Japanese. GPT-2 used 12 tokens for Spanish and 30 for Japanese. For comparison, Qwen used 9 and 12 tokens and Spark used 10 and 14.

For a general project, I would choose Qwen because it provides a good middle ground. It is much smaller than Spark while having a much larger context window than GPT-2. Its tokenizer also performed well in the Spanish and Japanese tests. If size and resource efficiency were the most important concerns, I would choose GPT-2 instead because its 124 million parameters make it a lot smaller and potentially easier to run on limited hardware.

For multilingual projects, however, I would favor Qwen or Spark over GPT-2 based on the tokenizer results. But for tasks involving larger documents, I would choose Spark. The estimated length of Chapter 2 is approximately 41,333 to 49,600 tokens, which is too large for both GPT-2 and Qwen's context windows. Spark's 1,048,576-token context window could fit the entire chapter while leaving more than enough tokens for the model's response. This makes Spark particularly useful for full reports, long transcripts, or other documents where keeping the entire document in one request is important.


## Part 6: Graduate Extension — Paper / Technical Report Analysis (300–400 words)

*Graduate students required.*

Pick one of your 3 models that has a linked paper or technical report on its card (most do). Read enough of it to answer:

- One real detail from the paper that's not on the model card — training data composition, a specific benchmark, a stated limitation, whatever you find.
- At least one limitation or tradeoff the authors admit to themselves.
- Your own take: does reading the paper change how much you'd trust this model for a real project vs. just reading the card? Why or why not?

> [Write your analysis here]

## Grading (10 pts total)

| Component | Undergrad | Grad |
|---|---|---|
| Findings table (Part 2, incl. tokenizer field) | 3 pts | 3 pts |
| Tokenizer comparison exercise (Part 3) | 2 pts | 1 pt |
| Context window check (Part 4) | 2 pts | 1 pt |
| Comparison reflection (Part 5) | 3 pts | 2 pts |
| Graduate extension (Part 6) | — | 3 pts |
| **Total** | **10 pts** | **10 pts** |

*If a model's license, architecture, or vocab size isn't clearly labeled, say so in your reflection — not every card is well documented, and noticing that is a useful takeaway on its own.*
