
## What is Retrieval Augmented Generation?
- RAG for short is the architecture popularized by Meta in 2020 that aims to improve the performance of LLMs by passing relevant information to the model along with the question/task details.

## Why RAG?
- LLMs are trained on large corpora of data and can answer any questions or complete tasks using their parameterized memory. These models have knowledge cutoff dates depending on when they were last trained.
- When asked a question out of its knowledge base or about events that happened after the knowledge cutoff date, there is a high chance that the model will hallucinate.
- So we provide extra context information to the model for answering.
- If the model is being asked about an event that happened after the cutoff date, providing information about this event as context and then asking the question will help the model answer the question correctly.

## RAG Architecture :

1. Indexing 
2. Retrieval
3. Generation


## 1.  INDEXING:

- There are 3 steps in indexing:
	1. Loading : First we need to load our data. This is done with DocumentLoaders.
	2. Splitting : Text splitters break large Documents into smaller chunks. This is useful both for indexing data and for passing it into a model, since large chunks are harder to search over and won’t fit in a model’s finite context window.
	3. Storing : We need somewhere to store and index our splits so that they can later be searched. This is often done using a VectorStore and Embeddings model.

## 2. RETRIEVAL:

Given a user input,(which is also converted into embedding using the embedding model) relevant splits(chunks) are retrieved from storage(vector store) using a Retriever.

## 3. GENERATION:

A ChatModel / LLM produces an answer using a prompt(set of directions that the model will follow while answering the queries) that includes the question and the retrieved data.![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*JnLO2hzuwwd9_Q3i.png)