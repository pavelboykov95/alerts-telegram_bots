from aiogram import Bot, Dispatcher, executor, types

from auth_data import ML_ALERT_BOT_TOKEN


bot = Bot(token=ML_ALERT_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.reply("Hi!")


if __name__ == '__main__':
    executor.start_polling(dp)
