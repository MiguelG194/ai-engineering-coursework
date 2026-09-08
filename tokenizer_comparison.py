from transformers import AutoTokenizer

gpt2 = AutoTokenizer.from_pretrained("openai-community/gpt2")
qwen = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")
spark = AutoTokenizer.from_pretrained("XHToken/Spark-X2.5-4B")

sentences = [
    "I love learning about artificial intelligence.",
    "Me encanta aprender sobre inteligencia artificial.",
    "私は人工知能について学ぶのが大好きです。"
]

tokenizers = {
    "GPT-2": gpt2,
    "Qwen": qwen,
    "Spark": spark
}

for sentence in sentences:
    print("\n\nSentence: ", sentence)

    token_ids = {}
    token_ids["GPT-2"] = gpt2.encode(sentence)
    token_ids["Qwen"] = qwen.encode(sentence)
    token_ids["Spark"] = spark.encode(sentence)

    for model, ids in token_ids.items():
        tokens = tokenizers[model].convert_ids_to_tokens(ids)
        print(model)
        print("IDs:", ids)
        print("Tokens:", tokens)
        print("Count:", len(ids))
        print()