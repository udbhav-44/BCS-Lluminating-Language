
So we've created a basic LLM RAG chatbot, with everything we've learned so far. But how do we compare how good or bad our model or pipeline is working ?

So we need an evaluation criterion for our RAG approach.
We will see how reliable the results generated from our large language model are.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aGIhV2AwW-04cr7wgrswuw.png)


We should note that, we may often you the terms benchmarking and evaluation interchangeably, but these terms have 2 different meaning.

Benchmarking - **Standardized testing**. It involves using predefined datasets and metrics to assess an LLM’s performance on specific tasks.

Evaluation - Has a broader scope. It goes beyond just running tests and involves a more holistic assessment of the LLM’s capabilities. Such as:

**Real-world applicability:** How well does the LLM perform in situations that mimic real-world use cases?  
**Fairness and bias:** Does the LLM exhibit any biases in its outputs?  
**Interpretability:** Can researchers understand how the LLM arrives at its answers?

# LLM Benchmarking

LLM benchmarks are a set of standardized tests designed to evaluate the performance of LLMs on various skills, such as reasoning and comprehension, and utilize specific scorers or metrics to measure these abilities.

Different benchmarks assess various aspects of a model’s capabilities, including:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*58jq50wQ7CUVB2cJ.png)


It's like, making an LLM going through JEE and on the basis of the result, giving it a ranking :)

## Language Understanding and QA Benchmarks

### [TruthfulQA](https://arxiv.org/abs/2210.09261)
- Evaluate models based on their ability to provide accurate and truthful answers.
- Original dataset consists of 817 questions across 38 categories. Questions target areas where humans might provide incorrect answers due to false beliefs or misconceptions.
- The best-performing model in the original paper, GPT-3, achieved only a 58% success rate compared to the human baseline of 94%.
- A fine-tuned GPT-3, referred to as “GPT-Judge”, is used to determine the truthfulness of an answer.

### [MMLU](https://arxiv.org/abs/2009.03300)
- Evaluate models based on their pre-training knowledge, focusing on zero-shot and few-shot settings.
- Multiple choice questions across 57 subjects, including STEM, humanities, social sciences, etc., with difficulty levels ranging from elementary to advanced.
- MMLU scores a Large Language Model (LLM) simply based on the proportion of correct answers. The output must be an exact match to be considered correct (‘D’ for the above example).

## Common-sense and Reasoning Benchmarks

### [ARC](https://arxiv.org/abs/1803.05457)
- The AI2 Reasoning Challenge (ARC) tests LLMs with grade-school level, multiple-choice science questions, ranging from simple to complex. For example, a question could be “What does photosynthesis produce to help plants grow?” with options (a) water (b) oxygen (c) protein (d) sugar.
- To score, the Accuracy over 3548 questions, of which 33% are designated as challenging is considered.

### [HellaSwag](https://arxiv.org/abs/1905.07830)
- Evaluates the common-sense reasoning capabilities of LLM models through sentence completion. It tests whether LLM models can select the appropriate ending from a set of 4 choices across **10,000 sentences.**
- GPT-4 achieved a record-high of 95.3% with just 10-shot prompting in 2023.

## Coding Benchmarks
### [HumanEval](https://arxiv.org/abs/2107.03374)
- Consists of **164 unique programming tasks** designed to evaluate a model’s code-generation abilities. These tasks cover a broad spectrum, from algorithms to the comprehension of programming languages.
- HumanEval scores the quality of generated code using the [Pass@k Metric](https://deepgram.com/learn/humaneval-llm-benchmark), which is designed to emphasize functional correctness in addition to basic textual similarity.

### [CodeXGLUE](https://arxiv.org/abs/2102.04664)
- Offers 14 datasets across **10 different tasks** to test and compare models directly in various coding scenarios such as code completion, code translation, code summarization, and code search.

## Chatbot Benchmarks

### [Chatbot Arena](https://arxiv.org/abs/2403.04132)
- The **Chatbot Arena** is an open platform for ranking language models using over 200K human votes. Users can anonymously quiz and judge pairs of AI models like ChatGPT or Claude without knowing their identities, and votes are counted towards rankings only if the model identities stay hidden.

### [MT Bench](https://arxiv.org/pdf/2306.05685v4.pdf)

- **MT-bench** evaluates chat assistants’ quality by presenting them with a series of multi-turn open-ended questions, utilizing LLMs as judges. This approach tests chat assistants’ ability to handle complex interactions. MT-Bench uses GPT-4 to score on a conversation on a scale of 10, and compute the average score on all turns to get the final score.


# LLM Evaluation Metrics

LM evaluation metrics score an LLM’s output based on criteria we care about. For example, if our LLM application is designed to summarize pages of news articles, we’ll need an LLM evaluation metric that scores based on:

1. Whether the summary contains enough information from the original text.
2. Whether the summary contains any contradictions or hallucinations from the original text.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*6Kg3kguOR1jXzkgt.png)


## Statistical Scorers

- Statistical scoring methods are non-essential to learn about, This is because statistical methods perform poorly whenever reasoning is required, making it too inaccurate as a scorer for most LLM evaluation criteria.

- Namely :
	- Word Error Rate
	- Exact Match
	- Perplexity
	- BLEU (Translation Tasks)
	- ROGUE (Summarization and Machine Translation Tasks)
	- METEOR 

## Model Based Scorers

- These scorers, that purely rely on NLP models are comparably more accurate, but are also more unreliable due to their probabilistic nature.

These scorers are of two broad types:
	1. Non LLM Scorers (Perform poorly)
	2. LLM Scorers

Among the Non-LLM Scorers are:
	1. Entailment Score
	2. BLEURT
	3. QA-QG


### LLM- Evals

#### G-Eval
**Uses LLMs to evaluate LLM outputs..**

- G-Eval first generates a series of evaluation steps using chain of thoughts (CoTs) before using the generated steps to determine the final score via a form-filling paradigm (this is just a fancy way of saying G-Eval requires several pieces of information to work).
- For example
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*0EUxV1oGqL9gTi3a.png)


#### Prometheus
- Prometheus is a fully open-source LLM that is comparable to GPT-4’s evaluation capabilities when the appropriate reference materials (reference answer, score rubric) are provided.
- Prometheus follows the same principles as G-Eval. However, there are several differences:

1. While G-Eval is a framework that uses GPT-3.5/4, Prometheus is an LLM fine-tuned for evaluation.
2. While G-Eval generates the score rubric/evaluation steps via CoTs, the score rubric for Prometheus is provided in the prompt instead.
3. Prometheus requires reference/example evaluation results.

Prometheus is available on HuggingFace, so you can try it out!!

## Hybrid Scorers

Basically, using best of both worlds and combining the statistical scorers and the Model-based Scorers.

1. **BERTScore** - The candidate text and reference text are fed into the DL model separately to obtain embeddings. The token-level embeddings are then used to calculate the pairwise cosine similarity matrix. Then similarity scores of most similar tokens from reference to candidates are selected and used to calculate precision, recall, and f1 score.
2. **MoverScore** - Uses the concept of word movers distance which suggests that distances between embedded word vectors are to some degree semantically meaningful ( vector(king) — vector(queen) = vector(man) ) and uses contextual embeddings to calculate Euclidean similarity between n-grams.
3. **GPTScore** - Based on the G-Eval technique,GPTScore uses the conditional probability of generating the target text as an evaluation metric. 

4. **QAG Score** - Uses answers (usually either a ‘yes’ or ‘no’) to close-ended questions (which can be generated or preset) to compute a final metric score. It is reliable because it does NOT use LLMs to directly generate scores.

![[RAG/assets/1.png]]

----

**High-quality LLM outputs are the product of a great retriever and generator.**
For this reason, great RAG metrics focus on evaluating either our RAG retriever or generator reliably and accurately.

There are majorly 2 frameworks, used for RAG evaluation, their features and metric are almost similiar:
1. DeepEval
2. Ragas

## Faithfulness

Faithfulness is an RAG metric that evaluates whether the LLM/generator in our RAG pipeline is generating LLM outputs that factually align with the information presented in the retrieval context.

We can calculate faithfulness using QAG by following this algorithm:

1. Use LLMs to extract all claims made in the output.
2. For each claim, check whether it agrees or contradicts each node in the retrieval context. In this case, the close-ended question in QAG will be something like: “Does the given claim agree with the reference text”, where the “reference text” will be each individual retrieved node. (_Note that we need to confine the answer to either a ‘yes’, ‘no’, or ‘idk’. The ‘idk’ state represents the edge case where the retrieval context does not contain relevant information to give a yes/no answer.)_
3. Add up the total number of truthful claims (‘yes’ and ‘idk’), and divide it by the total number of claims made.

## Answer Relevancy

Answer relevancy is an RAG metric that assesses whether our RAG generator outputs concise answers, and can be calculated by determining the proportion of sentences in an LLM output that a relevant to the input (ie. dividing the number of relevant sentences by the total number of sentences).

## Contextual Precision

- Contextual Precision is an RAG metric that assesses the quality of our RAG pipeline’s retriever. When we’re talking about contextual metrics, we’re mainly concerned about the relevancy of the retrieval context.
- A high contextual precision score means nodes that are relevant in the retrieval context are ranked higher than irrelevant ones. This is important because LLMs give more weight to information in nodes that appear earlier in the retrieval context, which affects the quality of the final output.

## Contextual Recall 
- Contextual Recall is an additional metric for evaluating a Retriever-Augmented Generator (RAG). It is calculated by determining the proportion of sentences in the expected output or ground truth that can be attributed to nodes in the retrieval context.
- A higher score represents a greater alignment between the retrieved information and the expected output, indicating that the retriever is effectively sourcing relevant and accurate content to aid the generator in producing contextually appropriate responses.
