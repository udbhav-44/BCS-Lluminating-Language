
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*m4AXQjCnKe4Dz9pl2r6BaQ.png)


Retrieval Augmented Generation can be summarized into 3 recently developed paradigms:
1. Naive RAG
2. Advanced RAG
3. Modular RAG


## Naive RAG

We have seen what the naive RAG is, now let us discuss its shortcomings and how it can be made more efficient.

![All the red dotted boxes are faults in Naive RAG](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MofEwsFkb-4iYKpiX9LCHg.png)

Although this diagram is self explanatory, let us analyse the shortcoming in all the 3 steps of a RAG pipeline:
1. Indexing:
	1. Information extraction is incomplete, as it does not effectively process useful information in images and tables within unstructured files such as PDF.
	2. The chunking process uses a “one-size-fits-all” strategy instead of selecting optimal strategies based on the characteristics of different file types. This has led to each chunk containing incomplete semantic information.
	3. The indexing structure is not sufficiently optimized, leading to inefficient retrieval functionality.
	4. The embedding model’s semantic representation capability is weak.

2. Retrieval: 
	1. The relevance of the recalled contexts is inadequate and the accuracy is low.
	2. The query may be inaccurate or the semantic representation capability of the embedding model may be weak, resulting in the inability to retrieve valuable information.
	3. The retrieval algorithm is limited because it does not incorporate different types of retrieval methods or algorithms, such as combining keyword, semantic, and vector retrieval.
	4. Information redundancy occurs when multiple retrieved contexts contain similar information, leading to repetitive content in the generated answers.

3. Generation:
	1. Inconsistent outputs.
	2. Outputs may simply repeat the retrieved content without providing valuable information.
	3. The LLM may generate incorrect, irrelevant, harmful, or biased responses.

All this pushes us to move forward, toward an approach that tries to solve these issues to some extent.

## Advanced RAG
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*CWV7H7prr7ZlvIYV4qLv6g.png)

In the Advanced RAG paradigm, we introduce 2 new steps:
1. Pre-Retrieval 
2. Post-Retrival

### Pre- Retrieval Optimisation

Focuses mainly on Data indexing optimisations and query optimisations.

1. Query Manipulation:
	1. Adjust the user queries for a better match with the indexed data.
	2. This involves:
		1. **Query Reformulation:** Rewrites the query to align more closely with the user’s intention
		2. **Query Expansion:** Which extends the query to capture more relevant results through synonyms or related terms.
		3. **Query Normalization:** Resolves differences in spelling or terminology for consistent query matching.

2. Data Modification:
	1. Includes preprocessing techniques like removing irrelevant or redundant information to improve the quality of results.
	2. Enriching the data with additional information such as metadata to boost the relevance and diversity of the retrieved content.

### Retrieval Optimisation

Retrieval optimization techniques revolve around the embedding models :

1. Search and Ranking:
	1. It focuses on selecting and prioritizing documents from a dataset to enhance the quality of the generation model’s outputs.
	2. This stage employs search algorithms to navigate through the indexed data, finding documents that match a user’s query.
	3. After identifying relevant documents, the process of initially ranking these documents starts to sort them according to their relevance to the query
2. **Fine-tuning embedding models**:
	1. Customizes embedding models
	2. Long shot optimization.
3. **Dynamic Embedding**: 
	1. Adapts to the context in which words are used, unlike static embedding, which uses a single vector for each word.
	2. OpenAI’s `embeddings-ada-02` is a sophisticated dynamic embedding model that captures contextual understanding.


### Post- retrieval Optimisation:

Refine the initially retrieved documents to improve the quality of text generation -

1. **Prompt compression**:
	1. Reduces the overall prompt length by removing irrelevant and highlighting important context.
2. **Re-Ranking:**
	1. the documents previously retrieved are reassessed, scored, and reorganized
	2. The objective is to more accurately highlight the documents most relevant to the query and diminish the importance of the less relevant ones.
	3. This step involves incorporating additional metrics and external knowledge sources to enhance precision
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*KBIMbCvXlSLjp3qN.png)


3. **Filtering**:
	1. Remove documents that fail to meet specified quality or relevance standards.
	2. This can be done through several approaches, such as establishing a minimum relevance score threshold to exclude documents below a certain relevance level.


## Techniques:

#### PRE-RETRIEVAL TECHNIQUES:

##### PDF Parsing:
In practical work, unstructured data(text with images, tables, graphs etc.) is much more abundant than structured data. If these massive amounts of data cannot be parsed, their tremendous value will not be realised.

And most of the Unstructured Data is present as PDF so we will look into it:

**Instead of being a data format, it is more accurate to describe PDF as a collection of printing instructions**.

How to parse it:

1. PyPDF (Rule Based Method) - it treats each line of the document as a sequence separated by newline characters “`\n`”, which prevents accurate identification of paragraphs or tables.
2. Unstructured (Deep Learning Based Method) 
3. Layout Parser (Deep Learning Based Method)
4. PP-StructureV2 (Deep Learning Based Method)

##### Context Enrichment:

**The concept here is to retrieve smaller chunks for better search quality**, **but add up surrounding context for LLM to reason upon**.

1. Sentence Window Retrieval :

In this scheme each sentence in a document is embedded separately which provides great accuracy of the query to context cosine distance search.

In order to better reason upon the found context after fetching the most relevant single sentence we extend the context window by _k_ sentences before and after the retrieved sentence and then send this extended context to LLM.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*vwmebXIBv93iwSHp.png)


2. Auto Merging Retriever :

Documents are split into smaller child chunks referring to larger parent chunks.
Documents are splitted into an hierarchy of chunks and then the smallest leaf chunks are sent to index. At the retrieval time we retrieve k leaf chunks, and if there is n chunks referring to the same parent chunk, we replace them with this parent chunk and send it to LLM for answer generation.


3. Query Rewriting :

User's original queries may have incorrect wording or lack semantic information. Query rewriting is a key technique for aligning the semantics of queries and documents.

Methods to do so:

1. **Hypothetical Document Embeddings (HyDE)** :
	1. We use another LLM, like ChatGPT, to do a specific task, such as creating a summary on a specific question or subject.
	2. While this artificially created document might contain inaccuracies, it encapsulates patterns and nuances that resonate with similar documents in a reliable knowledge base.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*k1Oi665_c7Nmb0o0.png)

2. **Rewrite-Retrieve-Read** :
	1. original query, particularly in real-world scenarios, may not always be optimal for retrieval by a LLM.
	2. We should first use an LLM to rewrite the queries. The retrieval and answer generation should then follow, rather than directly retrieving content and generating answers from the original query.

3.  **Step-Back Prompting** :
	1. If a query contains a lot of details, it is difficult for the LLM to retrieve relevant facts to solve the task.
	2. **The idea is to define “step-back problems” as more abstract problems derived from the original problem.**
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*GqV_MR0g60kmrmKo.png)


4. **Query2Doc**
	1. It generates pseudo-documents using a few prompts from LLMs, and then combines them with the original query to create a new one,
	2. It is somewhat similar to HyDE.
	3. However, Currently, in Langchain or LlamaIndex, no replication of query2doc has been found.

5. I**TER-RETGEN** :
	1. iteratively implements “retrieval-enhanced generation” and “generation-enhanced retrieval” within a Retrieve-Read-Retrieve-Read flow.
	2. ![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*yOTGxyEND5jbZaul.png)



###### 4. Semantic Chunking :

After parsing the document, we can obtain structured or semi-structured data. The main task now is to break them down into smaller chunks to extract detailed features, and then embed these features to represent their semantics.

**the most elegant method is obviously to chunk based on semantics**. **Semantic chunking aims to ensure that each chunk contains as much semantically independent information as possible.**

We will introduce three types of methods:

- Embedding-based : Both [LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/node_parsers/semantic_chunking.html) and [Langchain](https://python.langchain.com/docs/modules/data_connection/document_transformers/semantic-chunker) provide a semantic chunker based on embedding.
- Model-based 
- LLM-based

###### **5. Query Routing** :

**Query routing is the step of LLM-powered decision making upon what to do next given the user query**

**Defining the query router includes setting up the choices it can make.**  
The selection of a routing option is performed with an LLM call, returning its result in a predefined format, used to route the query to the given index.

Both [LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/querying/router/root.html) and [LangChain](https://python.langchain.com/docs/expression_language/how_to/routing?ref=blog.langchain.dev) have support for query routers.





#### RETRIEVAL TECHNIQUES:

##### Fusion Retrieval :

**Take the best from both worlds — keyword-based old school search** — sparse retrieval algorithms like [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) or search industry standard [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) — **and modern** semantic or **vector search and combine it in one retrieval result.**

The only trick here is to properly combine the retrieved results with different similarity scores — this problem is usually solved with the help of the [Reciprocal Rank Fusion](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) algorithm, reranking the retrieved results for the final output.

In LangChain this is implemented in the [Ensemble Retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/ensemble) class, combining a list of retrievers we define, for example a faiss vector index and a BM25 based retriever and using RRF for reranking.


#### POST- RETRIEVAL TECHNIQUES

##### Prompt Compression :

- Large Language Model(LLM) typically has a context length limit. Therefore, the longer the input text, the more time-consuming and costly the process becomes. 
- Also, The retrieved contexts may not always be useful. It’s possible that only a small portion of a larger chunk is relevant to the answer. In some cases, it may be necessary to combine multiple chunks to answer a specific question. This problem persists even with re-ranking.

1. Selective Context :

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*9tHQ5YpeDvxdO1s9.png)

- Selective Context employs a small language model(SLM) to determine the self-information of lexical units, such as sentences, phrases, or tokens, in the given context. It then uses this self-information to evaluate their informativeness. By selectively keeping content with higher self-information, Selective Context offers a more concise and efficient context representation for LLM.

2. LLMLingua:

	- [Selective Context](https://arxiv.org/pdf/2304.12102.pdf) often disregards the interconnection among compressed contents and the correlation between LLM and the small language model used for prompt compression. LLMLingua precisely addresses these issues.
	- LLMLingua employs a budget controller to dynamically allocate different compression ratios to various components of the original prompts, like instructions, demonstrations, and questions. It also performs coarse-grained, demonstration-level compression to maintain semantic integrity even at high compression ratios.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*5cpY5vL0Wf1Z0-J-.png)


- LLMLingua has introduced the Iterative Token-level Prompt Compression (ITPC) algorithm. Rather than relying solely on its independent probability, this method evaluates each token’s significance more precisely during prompt compression. It does this by iteratively processing each segment in the prompt and considering each token’s conditional probability within the current context. This approach aids in better preserving the dependency between tokens.


3. AutoCompressor

	- [AutoCompressor](https://arxiv.org/pdf/2305.14788.pdf) is a soft prompt-based approach.
	- It smartly fine-tunes the existing model by expanding the vocabulary and utilizing “summary tokens” and “summary vectors” to condense context information.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*DJ4yI_gn5jJDb7Su.png)


![[Screenshot 2024-06-28 at 10.26.26 AM.png]]

