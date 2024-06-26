# !pip install transformers sentencepiece --quiet
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def sentiment_analyse(text):
    model_checkpoint = 'cointegrated/rubert-tiny-sentiment-balanced'
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)
    if torch.cuda.is_available():
        model.cuda()
        
    def get_sentiment(text, return_type='label'):
        """ Calculate sentiment of a text. `return_type` can be 'label', 'score' or 'proba' """
        with torch.no_grad():
            inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True).to(model.device)
            proba = torch.sigmoid(model(**inputs).logits).cpu().numpy()[0]
        if return_type == 'label':
            return model.config.id2label[proba.argmax()]
        elif return_type == 'score':
            return proba.dot([-1, 0, 1])
        return proba
    res = get_sentiment(text, 'label')
    print(res) #результат
    # print(get_sentiment(text, 'proba'))
    return res

# classify the text
# text = 'Я ненавиджу школу!'
# sentiment_analyse(text)

# score the text on the scale from -1 (very negative) to +1 (very positive)
# print(get_sentiment(text, 'score'))  # -0.5894946306943893
# calculate probabilities of all labels
# print(get_sentiment(text, 'proba'))  # [0.7870447  0.4947824  0.19755007]