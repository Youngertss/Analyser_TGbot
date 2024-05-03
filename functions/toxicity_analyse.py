import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def toxicity_analyse(text):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer = AutoTokenizer.from_pretrained("FredZhang7/one-for-all-toxicity-v3")
    model = AutoModelForSequenceClassification.from_pretrained("FredZhang7/one-for-all-toxicity-v3").to(device)
    encoding = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=208,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )
    # print('device:', device)
    input_ids = encoding["input_ids"].to(device)
    attention_mask = encoding["attention_mask"].to(device)
    
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        predicted_labels = torch.argmax(logits, dim=1)

    if predicted_labels[0] == 1:
        print("Toxic")
        return "toxic"
    else:
        print("kind")
        return "kind"

# text = "Ти годишься лиш щоб мити підлогу у туалеті"
# toxicity_analyse(text)

