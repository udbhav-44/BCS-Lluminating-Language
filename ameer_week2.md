Used 2 models in my project:  
distilbert/distilbert-base-uncased-finetuned-sst-2-english  
siebert/sentiment-roberta-large-english  

# Pre-trained


### Distilbert  

accuracy: 0.875  
precesion: 0.92736077481f18402  
f1: 0.8597081930415263  

### Siebert

accuracy: 0.93  
precesion: 0.9183673469387755  
f1: 0.9278350515463918  


# Fine-tuned


### Distilbert

{'eval_loss': 0.9865542650222778,
 'eval_accuracy': 0.85,
 'eval_f1': 0.8421052631578947,
 'eval_precision': 0.8333333333333334,
 'eval_recall': 0.851063829787234,
 'eval_runtime': 1.8795,
 'eval_samples_per_second': 53.206,
 'eval_steps_per_second': 13.301,
 'epoch': 3.0}

 ### Siebert

 {'eval_loss': 0.9865542650222778,
 'eval_accuracy': 0.85,
 'eval_f1': 0.8421052631578947,
 'eval_precision': 0.8333333333333334,
 'eval_recall': 0.851063829787234,
 'eval_runtime': 1.8795,
 'eval_samples_per_second': 53.206,
 'eval_steps_per_second': 13.301,
 'epoch': 3.0}

 # Challenges Faced

 - only fine tuned on 1000 rows of data as it was taking a lot of time  
 - Adam optimizer facing issues  
 - Fine-tuned data producing lesser accuracy somehow  


 *fin*