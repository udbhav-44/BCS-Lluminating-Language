
# Week 2

 This is a brief description of the Week 2 of the project Luminating Languages Offered By Brain and Cognitive Society, IIT kanpur.


## Task
The Task is to make a sentimental classifier for the ImDB Movie reviews using Transformers.

Transformers from huggingface can be inferenced using 2 methods:

1. Using the HuggingFace Pipeline API directly 
2. Making a custom pipeline to inference models 

In this week's assignment we need to perform sentiment analysis on last weeks dataset using:
1. Pretrained Transformer models (atleast 2)
2. Fine-tuned models(same as above) on our dataset( We'll have to finetune them)

## Part-1 & Part-2 Statistics
Due to the huge number of rows, I reduced the testing of my model to a fixed no. of rows from the top. For all the following calculation, I took the number of rows to be 5000 out of 37000.
I classified the sentiment and evaluated them for the following models:



| Model Name                  | Type of Pipeline | Time taken to predict | Accuracy | Truncation of reviews(If any) | Time to train finetune the models |
| --------------------- | ----------- | -------------- | -------------- | -------------- | -------------- |
| distilbert-base-uncased-finetuned-sst-2-english     | Custom Pipeline      | 13 Minutes 22 Seconds            |     88.94%         | Token-Based Truncation till 512 Tokens |
| distilbert-base-uncased-finetuned-sst-2-english      | Direct Pipeline      | 9 Minutes 11 Seconds            |     86.9%         | Character-Based Truncation till 1000 Characters |
| distilbert-base-uncased-finetuned-sst-2-english      | Direct Pipeline      | 10 Minutes 35 Seconds            |     88.38%         | Word-Based Truncation till 270 Words| 
| distilbert-base-uncased-finetuned-sst-2-english      | Direct Pipeline      | 12 Minutes 24 Seconds            |     88.86%         | Token-Based Truncation till 470 Tokens|
| AurrieMartinez/distilbert-base-uncased-lora-text-classification-by-finetuning-distilbert-1(FINETUNED)      | Custom Pipeline      | 34 Minutes 51 Seconds            |     87.04%         | Token-Based Truncation till 512 Tokens| 7 Minutes 53 seconds |
| textattack/roberta-base-SST-2      | Direct Pipeline      | 16 Minutes 58 Seconds            |     51.6%         | Character-Based Truncation till 1000 Characters |
| textattack/roberta-base-SST-2      | Direct Pipeline      | 18 Minutes 20 Seconds            |     51.6%         | Word-Based Truncation till 270 Words| 
| textattack/roberta-base-SST-2      | Direct Pipeline      | 23 Minutes 14 Seconds            |     51.6%         | Token-Based Truncation till 460 Tokens|
| twitter_roberta_base_sentiment(This classifies as 0/1/2 But for the sake of original dataset, I took only Polar Ones,i.e., 0 and 2)      | Custom Pipeline      | 125 Minutes approx(I did for 100 reviews as more than 500 reviews was taking too much time, it took somewhere 5 minutes of time)            |     88.6%         | Token-Based Truncation till 512 Tokens|
| AurrieMartinez/roberta-base-lora-text-classification-by-finetuning-roberta (FINETUNED)      | Custom Pipeline      | 81 Minutes (I did for 1000 data sets and 4 epochs because it did take a lot of time, almost 16 Minutes 16 Seconds in this case)            |     91.6%         | Token-Based Truncation till 512 Tokens| 14 Minutes 45 Seconds

## Observations
From this data, we can notice that 
1. Direct and Custom Pipelines take almost similar time, while custom ones take a little bit more time and have almost the same accuracy.
2. The number of tokens in my test cases are Character based truncation < Word based Truncation < Token based Truncation [ Derived from the time it took to act ]
3. Roberta is a very big model with respect to distilbert, proven by the time it takes to fine-tune and apply.
4. Customly made (made by me) fine-tuned model takes a lot more time than the pre-trained finetuned models in both of the cases of roberta and distilbert
5. The pre-finetuned roberta model by textattack gives very little accuracy. However, I expected it to score better because its base model(roberta-base) is heavier than the distilbert-base-uncased. This proves that this model hasn't been trained well enough.
6. Pre-finetuned roberta by Twitter is exceptionally well trained, which proves the accuracy it gives with just only 100 samples, out of which approximately 1/3rd got removed due to binary classifications. Obviously, with more no. of data, the accuracy would increase finitely, which proves if it could have been trained with 5000 rows of data like the distilbert pre-trained ones, it must have produced better accuracy than them, proving that this heavier model is better in terms of performance (accuracy and effectiveness), efficiency (speed within a reasonable limit).
7. The same goes for the Customly made (made by me) fine-tuned roberta model, its accuracy is far better the Customly made (made by me) fine-tuned distilbert model

## Acknowledgements

 - [Fine-tuning Large Language Models (LLMs)](https://www.youtube.com/watch?v=eC6Hd1hFvos&ab_channel=ShawTalebi)
 - [Fine-Tuning Large Language Models (LLMs)](https://towardsdatascience.com/fine-tuning-large-language-models-llms-23473d763b91)
 - [HuggingFace](https://huggingface.co/)
 - [Google Search](https://www.google.com/)




