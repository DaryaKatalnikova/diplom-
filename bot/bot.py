from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, \
    ErrorEvent, KeyboardButton
from datetime import datetime, timedelta
from bot.models import *
from bot.settings import *
from bot.states import *

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
async def start(message: Message, state: FSMContext) -> None:
    await bot.send_message(message.from_user.id, "Привет! Я бот, который отправляет оповещения, напиши свою почту!")
    await state.set_state(States.register)


@dp.message(States.register)
async def register(message: Message, state: FSMContext) -> None:
    student: Student = db.query(Student).filter(Student.email == message.text).first()
    if student:
        student.telegram_id = message.from_user.id
        await bot.send_message(message.from_user.id, "Вы зарегистрированы в системе!")
        await state.set_state(States.debt)
    else:
        await bot.send_message(message.from_user.id, "Не существует такого пользователя!")


@dp.message(States.debt)
async def debt(message: Message, state: FSMContext) -> None:
    student = db.query(Student).filter(Student.telegram_id == message.from_user.id).first()
    dogovor: Dogovor = db.query(Dogovor).filter(Dogovor.id_student == student.id_student).first()
    plan: Plan_pay = db.query(Plan_pay).filter(
        Plan_pay.id_cours == db.query(Ugroup).get(student.id_group).first().id_cours).first()
    debt = plan.summa_b if dogovor.placeBud == "Бюджет" else plan.summa_vb
    pays: list[Pay] = db.query(Pay).filter(Pay.id_student == student.id_student,
                                           Pay.pay_date <= datetime.strptime(plan.plan_date, '%Y-%m-%d') - timedelta(
                                               weeks=24)).all()
    for pay in pays:
        debt -= pay.summa
    await bot.send_message(student.telegram_id, f"Ваша текущая задолженность - {debt} руб.")

