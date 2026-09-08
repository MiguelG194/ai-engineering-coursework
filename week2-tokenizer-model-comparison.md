# Week 2: Tokenizer and Model Comparison

## 1. Model Comparison

| Model | Hugging Face Link | Parameters | Architecture | License | Vocabulary Size | Context Window |
|---|---|---:|---|---|---:|---:|
| GPT-2 | [openai-community/gpt2](https://huggingface.co/openai-community/gpt2) | 124M | `GPT2LMHeadModel` | MIT | 50,257 | 1,024 tokens |
| Qwen2.5-1.5B-Instruct | [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) | 1.54B | `Qwen2ForCausalLM` | Apache-2.0 | 151,936 | 32,768 tokens |
| Spark-X2.5-4B | [XHToken/Spark-X2.5-4B](https://huggingface.co/XHToken/Spark-X2.5-4B) | 4B | `Spark2_5ForCausalLM` | Apache-2.0 | 131,072 | 1,048,576 tokens |

## 2. Tokenizer Comparison

The following sentences were passed through each model's tokenizer.

### English

`I love learning about artificial intelligence.`

### Spanish

`Me encanta aprender sobre inteligencia artificial.`

### Japanese

`私は人工知能について学ぶのが大好きです。`

| Sentence | GPT-2 | Qwen2.5-1.5B-Instruct | Spark-X2.5-4B |
|---|---:|---:|---:|
| English | 7 | 7 | 7 |
| Spanish | 12 | 9 | 10 |
| Japanese | 30 | 12 | 14 |

## 3. Context Window Analysis

| Model | Context Window |
|---|---:|
| GPT-2 | 1,024 tokens |
| Qwen2.5-1.5B-Instruct | 32,768 tokens |
| Spark-X2.5-4B | 1,048,576 tokens |

### Chapter 2 Token Estimate

The assignment estimates Chapter 2 at approximately 62 pages with 500–600 words per page.

#### Low Estimate

62 pages × 500 words/page = 31,000 words

31,000 words ÷ 0.75 words/token ≈ 41,333 tokens

#### High Estimate

62 pages × 600 words/page = 37,200 words

37,200 words ÷ 0.75 words/token = 49,600 tokens

Therefore, Chapter 2 is estimated to contain approximately **41,333–49,600 tokens**.

| Model | Context Window | Can Fit Chapter 2? |
|---|---:|---|
| GPT-2 | 1,024 | No |
| Qwen2.5-1.5B-Instruct | 32,768 | No |
| Spark-X2.5-4B | 1,048,576 | Yes |

## 4. Reflection
