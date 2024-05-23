from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, \
    ErrorEvent, KeyboardButton
from bot.models import *
from bot.settings import *

""" INITING BOT """

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot)

""" EXEPTION HANDLER """


@dp.error()
async def error_handler(event: ErrorEvent) -> None:
    db.rollback()


""" MAIN LOGIC """


@dp.message(F.text, Command('start'))
async def start(message: Message) -> None:
    msg = await bot.send_message(message.from_user.id, "Привет! Я бот, который отправляет оповещения, напиши свою почту!")
    student: Student = db.query(Student).filter(Student.email == msg.text).first()
    if student:
        student.telephone = msg.from_user.id
        await bot.send_message(message.from_user.id, "Вы зарегистрированы в системе!")
    else:
        await bot.send_message(message.from_user.id, "Не существует такого пользователя!")
