# Analysis of Sentiment Analysis Models

## Pre-trained Models

### DistilBert Pre-trained
- **Accuracy**: 0.898
- **Precision**: 0.8988714075938745
- **Recall**: 0.898
- **F1 Score**: 0.8978242022248917

### James Pre-trained
- **Accuracy**: 0.52
- **Precision**: 0.27040000000000003
- **Recall**: 0.52
- **F1 Score**: 0.35578947368421054

## Fine-tuned Models

### DistilBert Custom Pipeline
- **Accuracy**: 0.867
- **Precision**: 0.8674045963949369
- **Recall**:  0.867
- **F1 Score**: 0.8668176847179333
### DistilBert Custom Pipeline with fine tuning Timings
-**eval_loss**: 1.535650372505188,
-**eval_accuracy**: 0.81,
-**eval_runtime**: 10.7124,
-**eval_samples_per_second**: 18.67,
-**eval_steps_per_second**: 1.214,,
-**epoch**: 3.0
-**global_step**=189
-**training_loss**=0.027055094481776,
-**metrics**='train_runtime': 469.2939, 'train_samples_per_second': 6.393, 'train_steps_per_second': 0.403, 'total_flos': 155235232800000.0, 'train_loss': 0.027055094481776, 'epoch': 3.0

### James Custom Pipeline
- **Accuracy**: 0.522
- **Precision**: 0.27248400000000006
- **Recall**:  0.522
- **F1 Score**: 0.3580604467805519
### James Custom Pipeline with fine tuning Timings
-**eval_loss**: 0.48442450165748596,
-**eval_accuracy**: 0.885,
-**eval_runtime**: 25.0138,
-**eval_samples_per_second**: 7.996,
-**eval_steps_per_second**: 0.52,
-**epoch**: 3.0
-**global_step**=189,
-**training_loss**=0.17187736147925967,
-**metrics**='train_runtime': 1335.9152, 'train_samples_per_second': 2.246, 'train_steps_per_second': 0.141, 'total_flos': 308338797600000.0, 'train_loss': 0.17187736147925967

### Observations
-**As we can see fine tuning increases accuracy of james model highly**
-**Distilbert decreases as we use very less no. of epochs which can cause underfitting**

### Challenges I faced
- **First of all i used jupyter hence i am getting a lot of errors**
- **FThen i used google colab but it doesn't uses gpu**
- **FAt last i used my laptop gpu which finally saved my time slightly**
- **One more problem faced is in choosing of model**
- **fixing no. of epochs and batch size for decreasing the time**