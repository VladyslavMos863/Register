from aiogram import types, executor, Bot, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import add_user, add_user_name, add_user_numb, delete_user, inf, check_user
from aiogram.types import ReplyKeyboardMarkup, BotCommand
from aiogram.types import ParseMode
from aiogram.utils import markdown
import sqlite3
from database import database


bot = Bot('6350548585:AAHbDHojgCXYRb9D4guWHocX-3aec6LR7QQ')
dp = Dispatcher(bot, storage=MemoryStorage())


main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Зарегестрироваться на игру').add('Удалить пост').add('Просмотреть зарегестрированых игроков')


class user_reg(StatesGroup):
    name = State()
    numb = State()


@dp.message_handler(state=user_reg.name)
async def add_name_(message: types.Message,state=FSMContext):
    chat_id = message.chat.id
    await state.finish()
    add_user_name(message)
    await bot.send_message(chat_id, "Время когда сможете прийти на игру:")
    await user_reg.numb.set()


@dp.message_handler(state=user_reg.numb)
async def add_numb_(message: types.Message,state=FSMContext):
    chat_id = message.chat.id
    add_user_numb(message)
    await state.finish()
    await bot.send_message(chat_id, "Register complite")


@dp.message_handler(text='Зарегестрироваться на игру')
async def start_message(message: types.Message, state=FSMContext):
    chat_id = message.chat.id
    add_user(message)
    await bot.send_message(chat_id, f"Hello {message.chat.first_name} !\n"
                           f"Ваше имя :",)
    await user_reg.name.set()


@dp.message_handler(text='Удалить пост')
async def delete_name(message: types.Message, state=FSMContext):
    delete_user(message)
    await message.answer("Ваш пост удален")


@dp.message_handler(commands=['start'])
async def start_kayboard(message: types.Message):
    await message.answer(message.from_user.first_name, reply_markup=main)


@dp.message_handler(text='Просмотреть зарегестрированых игроков')
async def information(message: types.Message):
    await message.answer(inf(message), parse_mode=ParseMode.MARKDOWN)


if __name__ == "__main__":
    executor.start_polling(dp)



