# Data Preparation

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*f5r_zM_HqY7Rm9r--Jg0Lw.png)


##  Data Loading:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*6srgrlB4Qqsmb3ow.png)
When we load the data using the DataLoaders, every page of our files transforms into a **Document object** and has two important components **page_content** and **metadata**

> The **metadata** is a vital ensemble of additional details, like the document’s source (the file it originates from), the page number, file type, and other information.

There are multiple kinds of data loaders, which support various file formats, ranging from PDF, CSV, HTML, Markdown etc.

## Data Chunking:

Due to the limited context window size of the LLMs, we cannot fed in the entire data to the model, so we create small chunks of data to help us increase the efficiency.

Chunk size:
	1. Small -> Low Contextual information for generation (Single sentences)
	2. Large -> Chunks cover more information, which could increase the effectiveness of generation with more context. (Paragraphs, pages etc)


**Context Window:**

There are multiple items which are covered in the in this context window.

1. User Query
2. Instruction Prompt
3. Chat History
4. Retrieved Chunks

- High context length can cause a quadratic increase in time & memory due to the transformer model’s self-attention mechanism.

We need to select the chunk size carefully.
For Example->
![](https://miro.medium.com/v2/resize:fit:1324/format:webp/0*JNPcun70SopFtVdH.png)



### Different Chunking Methods:

1. Fixed-size chunking
2. "Context Aware" chunking
5. Multi-Modal Chunking

#### Fixed Size Chunking
- Vanilla flavoured chunking
- Computationally cheap and easy to use.
- We just set the chunk size and overlap size(To ensure that the richness of semantic context remains intact across the chunks.) to go ahead 

#### Context-Aware Chunking

##### Sentence Spliting 
Many models are optimized for embedding sentence-level content. Naturally, we would use sentence chunking, and there are several approaches and tools available to do this, including:
1. Naive Splitting 
2. NLTK (NLTKTextSplitter)
3. spaCy (SpacyTextSplitter)

##### Recursive Chunking
The **RecursiveCharacterTextSplitter** from LangChain splits text based on chosen characters, preserving semantic context

Just pass the Document and specify your desired chunk length (let’s say 1000 words). You can  fine-tune the overlap between chunks.

##### Specialised Chunking
As discussed, Markdown and LaTeX are two examples of structured and formatted content you might run into. In these cases, we can use specialized chunking methods to preserve the original structure of the content during the chunking process.


- Markdown (MarkdownTextSplitter from langchain)
- Latex (LatexTextSplitter)


## Tokenization

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*efaJuXITcOHg7Wg_.png)

To get an overview, you should read and watch -> [Summary by HuggingFace](https://huggingface.co/docs/transformers/tokenizer_summary)


## Vector Embeddings

As we need to search for relevant contextual chunks during RAG, we have to convert the data from textual format to vector embeddings.
So we'll explore the most efficient way to convert the text into vector embeddings by capturing the maximum semantic meaning.

If you wanna go through the documentation -> [S-bert](https://sbert.net/)


![](https://miro.medium.com/v2/resize:fit:1260/format:webp/1*teNmeq5T0WTn25SNswPqyA.png)

We have already seen a lot of them, now we'll work on a specific class of Transformer based - context dependent embedding models.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*FKH-Uo8_LK8b3Maq.png)


![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*myMlwnFjS-4Y_YtP.png)


#### Bert Based Models

BERT takes as input sequences that are composed of sentences or pairs of sentences (e.g.,<Question, Answer>) in one token sequence for question-answering tasks.

Input sequences are prepared before being fed to the model using _WordPiece Tokenizer_ with a 30k vocabulary size token. It works by splitting a word into several _subwords (Tokens)_.

#### Why Sentence BERT (S-BERT) Over BERT?
These transformer models had one issue when building sentence vectors: Transformers work using word or _token_-level embeddings, _not_ sentence-level embeddings.

Before sentence transformers, the approach to calculating _accurate_ sentence similarity with BERT was to use a **cross-encoder structure**.

The cross-encoder network does produce very accurate similarity scores (better than SBERT), but it’s not scalable. If we wanted to perform a similarity search through a small 100K sentence dataset, we would need to complete the cross-encoder inference computation 100K times.

Since the SBERT paper, many more sentence transformer models have been built using similar concepts that went into training the original SBERT. They’re all trained on many similar and dissimilar sentence pairs.


## Sentence Transformers


To understand how the S-Bert Model works read -> [Why S-bert](https://towardsdatascience.com/sbert-deb3d4aef8a4)
Research paper -> [Paper](https://arxiv.org/pdf/1908.10084)

### How to chose a model?

Trying and testing different model can help you chose the best embedding model for your task.

To simplify your decision-making process, Hugging Face offers the remarkable [Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard).

Further ahead, [Picking the Best Embedding & Reranker models](https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83) this article will help in understanding optimal combination of embedding and reranker(will discuss afterwards)
