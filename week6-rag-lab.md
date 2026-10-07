**Name:** Miguel Gomez

**Link to your completed Kaggle notebook:** https://www.kaggle.com/code/mgome23/day2-ai?scriptVersionId=355918318

## Part 1: Complete the RAG Codelab (30 pts)

Find the Day 2 codelab that builds a **RAG question-answering system over documents**. Copy it into your own Kaggle account and run it from top to bottom, with every cell executing successfully.

Record what the pipeline uses:

| | Value |
|---|---|
| Embedding model | gemini-embedding-001 |
| Where the embeddings are stored (vector store/database) | ChromaDB |
| Generation model | gemini-flash-lite-latest |
| Number of passages retrieved per query | 1 |

**In 2–3 sentences, describe what happens between the moment a question is asked and the moment an answer comes back:** 

When a user asks a question, the system converts the question into an embedding and searches the ChromaDB vector store for the most relevant passage. That passage is then included as context in a prompt sent to the generation model, which uses the retrieved information to generate the answer.

---

## Part 2: Make It Yours (40 pts)

In your copy of the notebook, **replace the sample documents with 3–5 short documents of your own.** Documents related to your term project are recommended. Course materials, public documentation for a tool you use, or articles on a topic you know well also work. Avoid anything private or sensitive.

Keep the rest of the pipeline the same. Your notebook should show your documents, your questions, and the outputs.

**Your documents:**

| | Value |
|---|---|
| What the documents are | Short Windows networking troubleshooting documents covering ipconfig, ping, and nslookup. |
| Number of documents | 3 |
| Why you chose them | They are relevant to my help-desk assistant project because these commands can be used to diagnose common network and DNS problems. |

Write **5 test questions** and run each through the pipeline. Your set must include:

- **2 keyword questions** that use exact names, terms, numbers, or codes from your documents
- **2 paraphrase questions** that ask about something in your documents without using its wording
- **1 unanswerable question** whose answer is **not** in your documents

| # | Question (short) | Type | Retrieved the right passage? (Yes / No / N/A) | Generated answer (correct / partly / wrong / correctly declined) |
|---|---|---|---|---|
| 1 | What does ipconfig /all display? | Keyword | Yes | Correct |
| 2 | How can I see whether my computer is getting its network settings automatically? | Paraphrase | Yes | Correct |
| 3 | What does the "-type=mx" option do in nslookup? | Keyword | Yes | Correct |
| 4 | How can I send a specific number of network test messages to another computer? | Paraphrase | Yes | Correct |
| 5 | How do I reset a user's Active Directory password from the command line? | Unanswerable | No | Correctly declined |

**Pick one question where the result wasn't fully correct (or, if everything worked, the one that came closest to failing). Was the weak point retrieval or generation? How can you tell from the notebook's output?**

Question 5 had retrieval failure because the system retrieved the nslookup document even though the question was about Active Directory password resets. However, the generation step handled the bad retrieval appropriately because it recognized that the retrieved passage did not contain the requested information and declined to answer.

---

## Part 3: Reflection (30 pts, 250–350 words)

Answer all four:

- Huyen describes two families of retrievers: term-based and embedding-based. Which kind does the codelab use? Based on your keyword questions, where might the other kind have done better or worse?
- How did the pipeline handle your unanswerable question? What would happen in a real application if it handled that badly, and what would you change to fix it?
- The codelab was designed to work well on its own sample documents. What, if anything, got harder when you switched to yours?
- Your project evaluation plan is due next week with Milestone 1. Does your project need RAG? If so, what would the documents be, and if not, why not?

**Your reflection:**

The codelab uses an embedding-based retriever. The documents are converted into embeddings and stored in ChromaDB, which allows the system to retrieve passages based on semantic similarity rather than only matching exact words. My keyword questions worked correctly, but a term-based retriever could potentially perform better when searching for exact technical commands such as ipconfig /all or -type=mx, since those terms are specific. However, the embedding-based approach is useful for paraphrased questions because the question does not need to use exactly the same wording as the document.

My unanswerable question asked how to reset an Active Directory password. The retriever returned the nslookup document, which was not relevant to the question. However, the model correctly recognized that the retrieved passage did not contain the requested information and declined to provide an answer. In a real help-desk application, an incorrect procedure could waste a technician's time by leading them through steps that do not produce a meaningful result. I would improve this by adding a relevance threshold so that the system can reject retrieved passages that are not sufficiently related to the question.

Using my own documents was somewhat harder because I had to decide how to divide the information into separate documents and create questions that tested different types of retrieval. The sample documents were already designed for the codelab, while I had to think about what information would actually be useful for a help-desk assistant.

My help-desk assistant could benefit from RAG. Its documents could include Windows troubleshooting documentation, approved network diagnostic procedures, Microsoft 365 documentation, and company-specific help-desk procedures. RAG would allow the assistant to retrieve relevant and current information rather than relying only on the model's general knowledge.