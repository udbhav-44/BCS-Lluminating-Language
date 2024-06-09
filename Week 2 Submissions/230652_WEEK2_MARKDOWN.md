Using the pretrained transformer models from the huggingface library and making sentimental analysis model using the imdb dataset.

# Using the HuggingFace Pipeline API directly

### 1. Model1- siebert/sentiment-roberta-large-english:
               F1 Score: 0.9199999999999999
               Accuracy: 0.92
               AUC Score: 0.921474358974359

### 2. Model2- distilbert/distilbert-base-uncased-finetuned-sst-2-english:
               F1 Score: 0.7741935483870969
               Accuracy: 0.79
               AUC Score: 0.7884615384615384

 Model1 is better in this case.

 # Making a custom pipeline by fine-tuning
 We are the using the same two models 
 ### 1. Model1:
 Epoch	Training Loss	Validation Loss	Accuracy
1	0.784600	0.724169	0.466667
2	0.736400	0.692987	0.533333
3	0.697800	0.692865	0.533333

Metrics:
 TrainOutput(global_step=1500, training_loss=0.7395897420247396, metrics={'train_runtime': 1341.4569, 'train_samples_per_second': 2.236, 'train_steps_per_second': 1.118, 'total_flos': 2795794089984000.0, 'train_loss': 0.7395897420247396, 'epoch': 3.0})

 Here for the first model, I have taken the batch size as only 2( first took then 16 then 8 then 2) because the model chosen is large and there was problem of ram going out of memory.

 ### 2. Model2:
Epoch	Training Loss	Validation Loss	Accuracy
1	No log	0.552134	0.883333
2	No log	0.682082	0.870000
3	No log	0.803732	0.890000
4	0.081000	0.877845	0.863333
5	0.081000	0.878528	0.866667

Metrics:
TrainOutput(global_step=625, training_loss=0.06590934038162231, metrics={'train_runtime': 277.1385, 'train_samples_per_second': 18.042, 'train_steps_per_second': 2.255, 'total_flos': 662336993280000.0, 'train_loss': 0.06590934038162231, 'epoch': 5.0})

Model2 is providing better results here.

# CHALLENGES FACED:
1. on google colab, there was limited time for using GPU, usage limits crossed causing a lot of time.
2. For some steps, there was exessive runtime because of which the session crashed.
3. Need to restart the kernel after installation of some particular modules.
4. For the first model after fine tuning it, rams's memory usage was exceeding its limits. Reducing batch size and epochs helped but then it compromised with the accuracy of the model.

               

