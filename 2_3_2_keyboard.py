from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from config import TOKEN_API, help_text, help_markup
from functions import (sentiment_analyse, toxicity_analyse,
input_word_in_context, reply_by_context, img_to_text)

bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot)

async def on_startup(_):
    print("Bot online...")

curr_text = ""

@dp.message_handler(commands=["help", "start"])
async def help(message: types.Message):
    await message.answer(help_text, reply_markup=help_markup)


@dp.message_handler(commands=["sentimental"])
async def sentimental(message: types.Message):
    text = message.text[12:].strip()
    print(text)
    if text=="":
        await message.answer(
            'Щоб використовувати мої функції, треба писати по інструкції\
                            "/назва_функції текст", наприклад: /sentimental Я люблю котів.')
    else:
        result = sentiment_analyse.sentiment_analyse(text)
        await message.answer(result)


@dp.message_handler(commands=["toxicity_check"])
async def toxicity_check(message: types.Message):
    text = message.text[15:].strip()
    print(text)
    if text=="":
        await message.answer(
            'Щоб використовувати мої функції, треба писати по інструкції\
                            "/назва_функції текст", наприклад: /sentimental Я люблю котів.')
    else:
        result = toxicity_analyse.toxicity_analyse(text)
        await message.answer(result)


@dp.message_handler(commands=["answer_by_context"])
async def answer_by_context(message: types.Message):
    global curr_text
    text = message.text[18:].strip()
    print(text)
    if text=="":
        await message.answer(
            'Щоб використовувати мої функції, треба писати по інструкції\
                            "/назва_функції текст", наприклад: /sentimental Я люблю котів.')
    else:
        curr_text = text
        await message.answer("Добре, я отримав твій текст. Тепер задавай питання. Якщо хочеш поміняти текст, викличи наново цю команду")


@dp.message_handler(commands=["word_in_context"])
async def word_in_context(message: types.Message):
    text = message.text[16:].strip()
    print(text)
    if text=="":
        await message.answer(
            'Щоб використовувати мої функції, треба писати по інструкції\
                            "/назва_функції текст", наприклад: /sentimental Я люблю котів.')
    else:
        result = input_word_in_context.input_word_in_context(text)
        text = text.replace('"?"', result)
        await message.answer(text)


@dp.message_handler(commands=["describe_photo"])
async def photo_describe(message: types.Message):
    url = message.text[15:].strip()
    print(url)
    if url=="":
        await message.answer('Щоб я описав зображення, надай через пробіл після команди посилання на нього')
    else:
        await message.answer("Добряче роздивлюсь і опишу на англійскій...")
        result = img_to_text.img_to_text(url)
        await message.answer(result)

@dp.message_handler(content_types=["text"])
async def reply_to_text(message: types.Message):
    global curr_text
    if curr_text!="":
        result = reply_by_context.reply_by_context(curr_text, message.text)
        await message.answer(result["answer"])

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup = on_startup)

