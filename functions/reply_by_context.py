from transformers import pipeline

def reply_by_context(context, question):
    qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")
    res = qa_model(question=question, context=context)
    return res

# question1 = "Як звуть людину?"
# question2 = "Що робить ця людина?"
# context = "Я Ілон маск. Я багато працюю і багато заробляю. Також роблю великий внесок в розвиток технологій."

# reply_by_context(context, question1)
# reply_by_context(context, question2)


