TOKEN_API = "" #YOUR TOKEN FROM @BotFather

help_text = """Привіт! Я бот analyser. Щоб використовувати мої функції,
треба писати по інструкції "/назва_функції текст". Також підтримую англійську мову і не тільки!
Тримай список того, що можу:

/sentimental - визначити настрій тексту.
/toxicity_check - перевірка тексту на токсичність.
/answer_by_context - скидуй мені текст, а потім задавай запитання по ньому.
/word_in_context - вставлю слово у наданий тобой контекст у вибране тобою місце. (місце, куди треба вставити слово познач як: "?", наприклад: я "?" котів.)
/describe_photo - кидай мені посилання на зображення, а я його опишу. 

/help - список команд, на які я реагую.
"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

help_markup = ReplyKeyboardMarkup(resize_keyboard=True,)
help_markup.add(KeyboardButton("/help"))

