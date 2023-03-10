# True/False Question Generator
This is a Streamlit app that generates True/False questions based on input text. The app uses a pre-trained BERT model for sequence classification to predict the label of the input text, and generates a true/false question based on the predicted label.

### Requirements
The app requires the following dependencies:

- Streamlit
- Torch
- Transformers
The app also requires a pre-trained BERT model for sequence classification. In this implementation, the "bert-base-uncased" model is used, but other models can also be used.

### Usage
To use the app, simply enter some text into the text area and click the "Generate" button. The app will generate a true/false question based on the input text.

### How it works
The app uses the pre-trained BERT model for sequence classification to predict the label of the input text (true or false). The app then generates a true/false question based on the predicted label, using the input text as the statement in the question.

The BERT model and tokenizer are loaded using the AutoTokenizer and AutoModelForSequenceClassification classes from the Transformers library. The generate_tf_question function tokenizes the input text, makes a prediction using the BERT model, and generates a true/false question based on the predicted label.

The app is built using Streamlit, which provides a simple way to create web apps with Python. The app includes a text area for entering input text, a "Generate" button to generate the true/false question, and a text area for displaying the generated question.

![image](https://user-images.githubusercontent.com/87160848/224267576-66b958c7-e42d-4aa7-b290-bf80f609fff7.png)


![image](https://user-images.githubusercontent.com/87160848/224266961-4d1d733a-0f5e-44dc-ad75-51d70043a0f4.png)
