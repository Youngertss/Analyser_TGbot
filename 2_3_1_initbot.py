#імпортування
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

#створення екземплярів класа бота та диспетчера
bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot)

#при успішному запуску бота побачимо напис у консолі
async def on_startup(_):
    print("Bot online...")

#обробка всіх повідомлень
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

#запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup = on_startup)

