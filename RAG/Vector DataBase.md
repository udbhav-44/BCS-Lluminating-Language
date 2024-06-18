# Vector DataBase

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hLvtb1volMlV3P5RIpRcUw.png)

We created the embeddings out data, now we need to store the embeddings so that they can be accessed on demand. For this purpose, we use a special kind of database called a **vector database.**

Efficient storage and retrieval of embeddings with capabilities like CRUD operations, metadata filtering, and horizontal scaling are crucial for large-scale applications using Retrieval-Augmented Generation(RAGs). Vector databases like ChromaDB, Pinecone, and Weaviate specialize in this, offering fast retrieval and similarity searches.

Different types of databases are available:
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*sMPRee-_3KtXuF8o.png)



## How does a vector DataBase work?

Traditional databases store strings, numbers, and other types of **scalar** data in rows and columns. On the other hand, a vector database operates on **vectors**, so the way it’s optimized and queried is quite different.

In vector databases, we apply a similarity metric to find a vector that is the **most similar** to our query.
A vector database uses a combination of different algorithms that all participate in the Approximate Nearest Neighbor (ANN) search. These algorithms optimize the search through various indexing techniques.

So there are three major steps in the common pipeline for a VectorDB:
- Indexing -> Mapping the things (your vectors which you got from the embedding models) into a data structure for faster searching.
- Querying -> The vector database compares the indexed query vector to the indexed vectors in the dataset to find the nearest neighbours (applying a similarity metric used by that index)
- Post Processing -> In some cases, the vector database retrieves the final nearest neighbours from the dataset and post-processes them to return the final results. This step can include re-ranking the nearest neighbours using a different similarity measure.

Whenever working with a vectorDB we have to maintain a tradeoff between the speed and accuracy (How fast you want the results and how good you want the results), keeping other things such as memory in mind.

## Indexing Methods 
1. **Tree Based Methods**** 
	1. **Efficient for Low Dimensional Data
	2. Require Substantial Memory
2. **Quantization Methods**
	1. Memory efficient and fast by compressing vectors into compact codes.
	2. But compression leads to loss of information, so accuracy is compromised
	3. Also computationally expensive.
3. **Hashing Methods**
	1. Fast and memory efficient 
	2. Maps similar vectors to same hash bucket
	3. Perform well in high-dimensional data and large dataset
	4. But Hash collisions can happen so accuracy is low
4. **Clustering Methods**
	1. Fast but quality of answers is based on the quality of the clustering
	2. Should not be used for dynamic data(where new data is being constantly added or some data is removed)
5. **Graph Methods:** 
	1. Good balance between accuracy and speed.
	2. Can be memory extensive as they need to store the graphs structures, also making the graphs is also computationally expensive.

Most current day vectordbs use a hybrid of these techniques to maintain a delicate balance.


## Algorithms

### Flat Indexing

1. Exact match algorithm
2. Flat indexes are ‘flat’ because we do not modify the vectors that we feed into them.
3. These indexes produce the most accurate results. We have perfect search quality, but this comes at the cost of significant search times.
4. With flat indexes, we introduce our query vector **xq** and compare it against every other full-size vector in our index — calculating the distance to each. After calculating all of these distances, we will return the nearest k of those as our nearest matches. A k-nearest neighbors (kNN) search.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*F8R3tayT_fJMYFhT.png)

5. Flat indexes are 100% search-quality but 0% search-speed.
6. To make it go any faster, we have 2 approaches:
	1. Reduce vector size — through dimensionality reduction or reducing the number of bits representing our vectors values.
	2. Reduce search scope — we can do this by clustering or organizing vectors into tree structures based on certain attributes, similarity, or distance — and restricting our search to closest clusters or filter through most similar branches.

### ANNOY (Approximate Nearest Neighbour Oh Yeah)

1. Tree based algorithms
2. Read More about it ->. [ANNOY ](https://sds-aau.github.io/M3Port19/portfolio/ann/)
3. The algorithm projects points onto random hyperplanes and partitions the space according to which side of the hyperplane the points fall on. This process is repeated recursively, resulting in a binary tree of partitions.
4. When a query point is received, the algorithm traverses down each tree in the forest to find the leaf node where the point would belong. The nearest neighbors are then approximated by collecting a list of points in the leaf nodes found in all trees and returning the top-k points from this list that are closest to the query point.
5. Good for high dimensional data

### **Inverted File (IVF) Indexing**

The Inverted File Index (IVF) index consists of search scope reduction through clustering. It’s a very popular index as it’s easy to use, with high search quality and reasonable search speed.

It works on the concept of Voronoi diagrams — also called Dirichlet tessellation (a much cooler name).

Check them out.

## [Random Projection (RP)](https://www.pinecone.io/learn/locality-sensitive-hashing-random-projection/)

## [Product Quantization (PQ)](https://www.pinecone.io/learn/product-quantization/)

## [Hierarchical Navigable Small World (HNSW)](https://www.pinecone.io/learn/hnsw/)



## Similarity Metrics/ Distance Metrics


![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*HtLPZbiJD35mEQe_.png)

### How to chose a similarity Metric?
It’s a general best practice to use the same similarity measure for the search that the embeddings were trained on; however, the choice of similarity measure also depends on the specific characteristics of the data and the context of the problem you are trying to solve.


## Filtering 

Every vector stored in the database also includes metadata. In addition to the ability to query for similar vectors, vector databases can also filter the results based on a metadata query. To do this, the vector database usually maintains two indexes: a vector index and a metadata index. It then performs the metadata filtering either before or after the vector search itself, but in either case, there are difficulties that cause the query process to slow down

Filtering can be:
1. Post : In this approach, metadata filtering is done before the vector search. While this can help reduce the search space, it may also cause the system to overlook relevant results that don’t match the metadata filter criteria. Additionally, extensive metadata filtering may slow down the query process due to the added computational overhead.
2. Pre : the metadata filtering is done after the vector search. This can help ensure that all relevant results are considered, but it may also introduce additional overhead and slow down the query process as irrelevant results need to be filtered out after the search is complete.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*DL2BRaVbe4B4gEK2.png)

You can check out this blog by Pinecone on [Filtering](https://www.pinecone.io/learn/vector-search-filtering/)


## Which DB?

We will use this benchmarking to decide:

[Benchmark hu mai](https://benchmark.vectorview.ai/vectordbs.html)

