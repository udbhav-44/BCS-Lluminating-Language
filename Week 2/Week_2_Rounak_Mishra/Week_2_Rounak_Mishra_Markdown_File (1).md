# Directly using Pipeline API

   ### (i)Distilbert: 
                      Accuracy: 0.79
                      F1 Score: 0.7741935483870969
                      Recall Score: 0.75
                      Precision: 0.8
  ### (ii)Roberta:
                    Accuracy: 0.82
                    F1 Score: 0.7999999999999999
                    Recall Score: 0.75
                    Precision: 0.8571428571428571
 ### (iii)Albert:
  				  Accuracy: 0.44
                    F1 Score: 0.2
                    Recall Score: 0.14583333333333334
                    Precision: 0.3181818181818182

#### Clearly Roberta is the best.
# Using Custom Fine tuned models
### (i)Distilbert:
Metrics=
{'train_runtime':152.1309,'train_samples_per_second': 19.72,'train_steps_per_second':1.242,'total_flos':397402195968000.0,'train_loss':0.12410234521936488,'epoch':3.0}
  ### (ii)Roberta 
  Metrics={'train_runtime':505.2769,'train_samples_per_second':9.896,'train_steps_per_second':0.623,'total_flos':1315567088640000.0,'train_loss':0.392589605422247,'epoch':5.0}
  ### (iii)Albert 
Metrics=
{'train_runtime':522.5994,'train_samples_per_second':9.568,'train_steps_per_second':0.603,'total_flos':119490508800000.0,'train_loss': 0.5897342258029514,'epoch': 5.0}
#### Clearly Distilbert is the best here.
# References:
I used the hugging face api documentation as a reference for this assignment.
# Challenges faced:
- Firstly in the pretrained models,I had to define a function to decrease the number of words in each review as otherwise it was exceeding the maximum number of words
     that can be a evaluated by the models.I used the approach of character level truncation for this.
- Then during fine tuning cpu was taking a lot of time to train the models,so I used the T4 GPU.
- I had to change the dataset type to a type accepted by the models as the original type was giving errors.

### END




