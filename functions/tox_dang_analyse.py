import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def is_sigma_tox(text):
    
    model_checkpoint = 'cointegrated/rubert-tiny-toxicity'
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)
    if torch.cuda.is_available():
        model.cuda()
        
    def text2toxicity(text, aggregate=True):
        """ Calculate toxicity of a text (if aggregate=True) or a vector of toxicity aspects (if aggregate=False)"""
        with torch.no_grad():
            inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True).to(model.device)
            proba = torch.sigmoid(model(**inputs).logits).cpu().numpy()
        if isinstance(text, str):
            proba = proba[0]
        if aggregate:
            return 1 - proba.T[0] * (1 - proba.T[-1])
        return proba
    
    res = text2toxicity(text, False)
    print(text)
    print(res)
    if max(res[1:]) > 0.1 or res[-1] > 0.05 or res[0]<0.9995  :
        return True
    return False

# is_sigma_tox("Я хочу тебя see")

# non-toxic  : 0.9937
# insult     : 0.9912
# obscenity  : 0.9881
# threat     : 0.9910
# dangerous  : 0.8295






# model_name = "IlyaGusev/rubertconv_toxic_clf"
# pipe = pipeline("text-classification", model=model_name, tokenizer=model_name, framework="pt") 
# text = "Ты молодец"
# print(pipe([text])[0]["label"])

# async def is_sigma_tox(text):
#     model_name = "IlyaGusev/rubertconv_toxic_clf"
#     pipe = pipeline("text-classification", model=model_name, tokenizer=model_name, framework="pt")
#     print(pipe([text]))
#     if pipe([text])[0]["label"]!="neutral":
#         return True
#     return False



