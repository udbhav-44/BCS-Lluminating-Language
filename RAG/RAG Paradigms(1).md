# PART 10
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



### Re-Ranking

- Large no of context may be retrived but may not be required.
- This technique, allows reordering and filtering of documents, placing the relevant one at the forefront, to increase the effectiveness of RAG.
- 
![[Screenshot 2024-06-29 at 9.19.47 PM.png]]

- Very Relevant -> Red Boxes 
- Slightly Related -> Green
- Unrelated -> Blue 
**In simpler terms, re-ranking is like helping us choose the most relevant references from a pile of study materials during an open-book exam**

Re-Ranking can be done in 2 ways :
	1. Re-Ranking Models
	2. LLM


1. Re-Ranker Model:
	1. The re-ranking model, unlike the embedding model, takes query and contexts as inputs and directly outputs similarity scores instead of embeddings.
	2. THe most popular re ranking model is Cohere(which is the best, but also paid), which is accessed through API.
	3. Just for comparision:
	![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*TDmPXppuH1l3oux5.png)

2. LLM as re-ranker
	1. Fine-tuning LLM with re-ranking Task:
	2. Prompting LLM for re-ranking:
		1. [RankGPT](https://arxiv.org/pdf/2304.09542.pdf)
		2. ![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Z6aX3QJB2dOSgWpL.png)
		3. The third method, permutation generation, is proposed in this paper. **Specifically, instead of relying on an external score, the model directly performs end-to-end sorting of the passages.** In other words, it directly utilizes the semantic understanding ability of LLM to perform relevance ranking on all candidate passages.
	3. Using LLM for data augmentation during training:


### Filtering

- Self-RAG introduces a self reflection mechanism to efficiently filter out irrelevant content.
- By employing critique tokens, this approach evaluates the relevance, supportiveness, and utility of retrieved passages, ensuring the integration of only high-quality information into the content generation process.

### Self-RAG
Let’s consider a common scenario: taking an open-book exam. We usually have two strategies:

- Method 1: For familiar topics, answer quickly; for unfamiliar ones, open the reference book to look them up, quickly find the relevant parts, sort and summarize them in our mind, then answer on the exam paper.
- Method 2: For every topic, refer to the book. Locate the pertinent sections, mentally collate and summarize them, then write our response on the exam paper.

Evidently, method 1 is the preferred approach. Method 2 can consume time and potentially introduce irrelevant or erroneous information, this may lead to confusion and mistakes, even in areas we originally understood.

- Method 2 is the classic RAG
- Method 1 is Self-RAG

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*AZjB_cdty-FJUvO9.png)


Self-RAG consists of three steps:

1. **Retrieval as Needed**: When the model requires retrieval, such as the query “How did US states get their names?” (the top right of above figure), the model’s output will contain a `**[Retrieve]**` token. This indicates that content related to the query needs to be retrieved. Conversely, when asked to write “Write an essay on your best summer vacation” (the bottom right of above figure), the model opts to generate the answer directly, without retrieval.
2. **Parallel Generation**: The model uses both the prompt and the retrieved content to generate outputs. Throughout this process, three types of reflection tokens indicate the relevance of the retrieved content.
3. **Evaluation and Selection**: The content generated in step 2 is evaluated and the best segment is chosen as the output.


### Corrective-RAG

Again, lets consider a open book exam, now we have 3 stratergies:

- Method 1: Answer quickly for familiar topics. For unfamiliar ones, refer to the reference book. Quickly locate the relevant sections, organize and summarize them mentally, then write our answer on the exam paper.
- Method 2: For each topic, refer to the book. Identify the relevant sections, summarize them in our mind, and then write our response on the exam paper.
- Method 3: For each topic, consult the book and identify relevant sections. Before forming an opinion, categorize the gathered information into three groups: **Correct**, **Incorrect**, and **Ambiguous**. Process each type of information separately. Then, based on this processed information, compile and summarize it mentally. Write our response on the exam paper.

Method 1 -> Self-RAG
Method 2 -> Classic RAG
Method 3 -> Corrective RAG (CRAG)


CRAG has designed a lightweight retrieval evaluator to assess the overall quality of documents retrieved for specific queries. It also uses web search as a supplementary tool to improve retrieval results.

CRAG is plug-and-play, allowing for seamless integration with various methods based on RAG.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*-yWFEPkKv9Go0sZM.png)
There are 3 possible judgment results.

- If it is **correct**, this implies that the retrieved documents contains the necessary content as required by the query, then employ a knowledge refinement algorithm to rewrite the retrieved documents.
- If the retrieved documents is **incorrect**, this means that the query and the retrieved documents are irrelevant. Consequently, we can’t send the document to LLM. In CRAG, a web search engine is used to retrieve external knowledge.
- For **ambiguous** cases, this implies that the retrieved documents might be close but insufficient to provide an answer. In such cases, additional information would need to be sourced through web search. So both the knowledge refinement algorithm and the search engine are employed

### Diff betn Self- RAG and C-RAG

From how they work:
- Self-RAG can give answers directly using a large language model without needing to look anything up first, while CRAG has to find relevant information before it can add a layer to check the answer's quality.

From how they're built:
- Self-RAG is more complex than CRAG. It needs a more detailed training process and involves creating and checking multiple answers during the answer-making phase, which makes it slower and more expensive to use. On the other hand, CRAG is simpler and faster because it doesn't do as much.

In terms of performance:
- As shown in the figure below, CRAG usually works better than self-RAG in most cases.


### RAG Fusion

- **Starting off:** RAG-Fusion begins by creating several new questions from the original question using a large language model. This helps to fully understand the user's initial input by looking at the topic from different angles.

- **Finding information:** Next, it searches for documents that match not only the original question but also the new questions. This helps gather a wide variety of information on the topic.

- **Organizing the information:** Once the documents are gathered, the Reciprocal Rank Fusion (RRF) algorithm sorts these documents by how relevant they are. This way, the most useful documents are prioritized.

- **Combining everything:** These sorted documents are then brought together to make a detailed and relevant source of information.

- **Final response:** In the last step, all the collected documents and questions are processed by a large language model. The model uses this information to create a clear and well-informed response.

Through these steps, RAG-Fusion makes sure the answers provided are both thorough and accurate, greatly improving the quality of the responses to user questions.

![](https://miro.medium.com/v2/resize:fit:640/format:webp/0*OtAKy84U01L_Uf0Y.png)

### Final Conclusion
![](https://miro.medium.com/v2/resize:fit:786/format:webp/1*STe7AABlaRXYnS5E4UfV5A.png)

## Generation Techniques
### Enhancement

Demonstrate-Search-Predict (DSP): This method uses multiple search queries to gather information from various sources to provide a well-rounded answer. It calculates the combined likelihood of different passages being relevant, helping to build a comprehensive response.

Pluggable Reward-Driven Contextual Adapter (PRCA): PRCA improves the context used for generating responses by learning from feedback. It uses reinforcement learning to refine how context is selected and presented, aiming to match the specific needs of the response generator.

REtrieve and PLUG (REPLUG): REPLUG adds retrieved documents to the input context before generating a response, overcoming the usual length limitations of LMs. This helps the LM consider more relevant information and improves accuracy.

RECITE: This method generates multiple responses independently and uses a voting system to choose the most reliable one. This increases the accuracy and credibility of the final answer.

### Customization Techniques

Parametric Knowledge Guiding (PKG): PKG customizes responses by generating necessary background knowledge directly within the model, eliminating the need to look for information externally. This integration allows the model to produce responses that are closely tailored to specific tasks or contexts.

Self-RAG: This strategy uses special tokens that reflect on the model's own process to adjust how it retrieves and generates information. It can be tuned to prioritize either accuracy or creativity, offering flexibility in how responses are crafted based on the task's demands.

SUbgraph Retrieval-augmented GEneration (SURGE): SURGE uses a technique that combines graph-based and text-based information to ensure that responses are highly relevant and specific to the given context. It aligns the knowledge from a retrieved graph with the generated text, resulting in precise and contextually relevant responses.


## Chat Engine

When building a robust RAG system that can handle multiple interactions from a single query, a key component is the chat logic. 
This logic must account for the ongoing conversation, similar to how older chatbots worked before large language models (LLMs) like ChatGPT became popular. This feature is crucial to handle follow-up questions, references to earlier parts of the conversation, and other user commands that depend on what was previously discussed. The technique used to manage this is known as "query compression," which involves compressing the dialogue context and the user's current query.

There are different methods to implement this:

1. **ContextChatEngine**: This is a straightforward method where the system first finds information relevant to the user's question and then combines this information with the chat history stored in memory. This helps the LLM remember the previous context while generating the next response.

2. **CondensePlusContextMode**: This approach is a bit more advanced. Each time the user interacts, the chat history and the most recent message are compressed into a new query. This new query is used to retrieve relevant information, and then both the retrieved context and the original user message are used to generate a response.

Additionally, there are specialized frameworks like LlamaIndex and Langchain that support OpenAI models. These frameworks offer flexible modes for integrating chat functionalities with the powerful capabilities of OpenAI’s LLMs.

![](https://miro.medium.com/v2/resize:fit:786/format:webp/0*hlR7CMHvuSd7Mw2T.png)

## Agents in RAG


1. **What Agents Do**: An agent in this context is like a smart assistant that can perform complex tasks. It not only talks and reasons but can also use other tools or functions, such as accessing external APIs or running other software components. The idea is that these agents can work together (what Langchain calls "LLM chaining") to complete tasks more efficiently.

2. **OpenAI Assistants**: Recently, OpenAI introduced a new kind of tool called OpenAI Assistants at a developer conference. These assistants enhance the abilities of LLMs by providing additional features that were previously available in open-source projects. For example, they can manage chat histories, store information, upload documents, and even convert natural language instructions into API calls. This makes them very versatile for different applications.

3. **Integration in LlamaIndex**: In systems like LlamaIndex, there’s a special component called OpenAIAgent. This component combines the functions of chatting, querying, and calling multiple OpenAI functions in a single conversation. It's like having a super-smart chatbot that can access a vast amount of information and tools in one go.

4. **Multi-Document Agents Setup**: This setup involves multiple agents, each assigned to a specific document. These document agents can summarize documents or answer questions based on them. There’s also a top agent that coordinates all these document agents. It directs questions to the right document agent and synthesizes the final answers from their inputs.

   - **Tools Used**: Each document agent uses tools to decide how to handle queries—either summarizing the document or looking up specific details.
   - **Coordination**: The top agent acts as a manager, directing queries to the appropriate document agents and combining their responses.

This advanced setup allows for detailed and nuanced interactions with multiple documents, making it possible to handle complex queries that involve different sources. However, this complexity can make the system slower because it involves many steps and interactions with the LLMs, which are typically the most time-consuming part of the process.

![](https://miro.medium.com/v2/resize:fit:786/format:webp/0*OYrOYV2ss_7L75Ds.png)

## Encoder and LLM fine-tuning

In our RAG system, we use two main types of deep learning models:

1. **Transformer Encoder**: This model handles creating embeddings (detailed text representations) to help retrieve relevant information when needed.
  
2. **Large Language Model (LLM)**: Models like GPT-4 use the provided context to answer user queries. They learn quickly from a few examples, which is useful for specific tasks.

**Fine-Tuning Models**: We fine-tune these models to improve their performance for particular tasks. For example, you might adjust the Transformer Encoder to better create embeddings or the LLM to use the context more effectively.

**Using Synthetic Datasets**: We can use models like GPT-4 to create synthetic datasets for training. However, fine-tuning a model with a small synthetic dataset can limit its overall capabilities. The model might excel in tasks similar to the dataset but perform poorly in other areas because it's overly specialized.

Types of fine-tuning are
--> Encoder Fine-Tuning
--> Ranker Fine-Tuning
--> LLM Fine-Tuning

