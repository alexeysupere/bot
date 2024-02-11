import asyncio
import random
import logging
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher, F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6746742912:AAFt9Jl0JQXShvvl0pxRuN2hnNZnEJe4wfk")
# Диспетчер
dp = Dispatcher()



@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )
@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(random.randint(1, 10)))
    await callback.answer(
        text="Спасибо, что воспользовались ботом!",
        show_alert=True
    )









# @dp.message(Command("reply_builder"))
# async def reply_builder(message: types.Message):
#     builder = ReplyKeyboardBuilder()
#     for i in range(1, 17):
#         builder.add(types.KeyboardButton(text=str(i)))
#     builder.adjust(4)
#     await message.answer(
#         "Выберите число:",
#         reply_markup=builder.as_markup(resize_keyboard=True),
#     )

# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Hello!")

    

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())