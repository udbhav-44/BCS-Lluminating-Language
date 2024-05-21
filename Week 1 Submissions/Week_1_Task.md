# Week 1 : Basic of NLP

So, we'll start the project by covering the fundamental basics of Natural Language processing-

We'll do so with a small hands-on experience task and learn en route.

So, the Task is to make a **sentimental classifier** for the ImDB Movie reviews.


<u>*About the Data:*</u>

This dataset contains **40,000 IMDb Movie reviews**, tagged as 0/1 for Negative/Positive reviews. 

## What do we do?

1. **<u>EDA (Exploratory Data Analysis), primary processing, and data visualization :</u>**
    1. How does the data look?
    2. Are there any duplicate entries? If yes, then what to do?
    3. Are there any missing entries? If yes, then what to do?
    4. Is the data inconsistent somewhere? Is there any other value apart from 0/1 in the sentiment column.
    5. What is the distribution between positive and negative reviews? Is the data imbalanced or not?
    6. What does the length of reviews vs the sentiment graph look like?
    7. https://www.geeksforgeeks.org/what-is-exploratory-data-analysis/
    8. https://www.youtube.com/watch?v=-o3AxdVcUtQ
   
2. <u>**Data Pre-Processing:</u>** Getting your data ready to be fed into your classification algorithms. Which involves cleaning your data for any noise or unnecessary elements.
    1. Removing Stopwords
    2. Removing special characters like emojis, hashtags, etc
    3. Convert all the text into Lowercase for generalisation.
    4. Removing punctuations and any other thing you may think does not affect the text's sentiment.
    5. Tokenise the sentences : https://youtu.be/fNxaJsNG3-s?si=XRT_w6F8Fk7YMcJu
    6. Performing Stemming and Lemmatisation: 
       1. https://www.ibm.com/topics/stemming-lemmatization
       2. https://www.youtube.com/watch?v=HHAilAC3cXw
    7. Perform a Train/test Split.
   <br>
   </br>
3. <u>**Feature Extraction:</u>** Now you have cleaned text data, but the machine doesn't understand English, so you'll have to convert the text into meaningful numerical representation, which can be fed to your machine for predictions.
    1. **<u>Creating Embeddings:</u>** You can use different techniques to generate word embeddings, such as 
        
        1. [ One hot encoding ](https://www.geeksforgeeks.org/ml-one-hot-encoding/)

        2. Bag of Words 
        3. Count Vectorizer
        4. TF-IDF vectorizer
        5. Word2vec
        6. https://neptune.ai/blog/vectorization-techniques-in-nlp-guide
    2. Compare and contrast all these techniques and see which gives you the best results.
4. **<u> Model Selection:</u>** Now we have our input data ready to be fed to a neural network, but which? We'll try out different classification algorithms (this is a binary classification problem), from simple ones to complex ones, and then evaluate which one gives the best results. Models such as:
    1. Logistic Regression 
    2. Bernoulli Naive Bayes Classifier
    3. SVM (Support Vector Machine)
    4. Random Forests
    5. A simple Neural network with a few dense layers
    6. https://towardsdatascience.com/top-machine-learning-algorithms-for-classification-2197870ff501
5. **<u>Evaluation:</u>** To evaluate how well you performed(or your model), we will assess them on a set of metrics:
    1. Accuracy Score
    2. ROC-AUC
    3. F1 Score
    4. Confusion Matrix