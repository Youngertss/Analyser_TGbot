from transformers import AutoModelForMaskedLM, AutoTokenizer
import torch
from random import choice

def input_word_in_context(question):
    tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-uncased")
    model = AutoModelForMaskedLM.from_pretrained("bert-base-multilingual-uncased")
    def get_answer(question):
        # Маскування питання
        masked_question = question.replace('"?"', tokenizer.mask_token)

        # Кодування замаскованого питання
        input_ids = tokenizer.encode(masked_question, return_tensors="pt")

        # Визначення індексів маски
        mask_indices = torch.where(input_ids == tokenizer.mask_token_id)

        # Отримання відповіді від моделі
        output = model(input_ids)
        token_logits = output.logits

        predicted_words = []
        for mask_index in mask_indices:
            mask_token_logits = token_logits[0, mask_index, :]
            # Отримання топ кращих 3 відповідей
            top_3_tokens = torch.topk(
                mask_token_logits, 3, dim=1).indices[0].tolist()
            predicted_words.append([tokenizer.decode([token])
                                for token in top_3_tokens])

        return predicted_words
    # Приклад використання
    predicted_answers = get_answer(question)
    print("Predicted answers:", predicted_answers[-1])
    return choice(predicted_answers[-1])

# question = 'Слава "?"! Героям слава! Україна понад усе!'
# input_word_in_context(question)

