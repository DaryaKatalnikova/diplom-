from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ErrorEvent
from datetime import datetime, timedelta
from models import *
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


@dp.message(Command("menu"))
async def menu(message: Message, state: FSMContext) -> None:
    kb = [[InlineKeyboardButton(text='Заказать справку', callback_data='inquiry'),
           InlineKeyboardButton(text='Узнать долг', callback_data='debt'), ]]
    markup = InlineKeyboardMarkup(inline_keyboard=kb)
    await bot.send_message(message.from_user.id, 'Что вы хотите сделать?', reply_markup=markup)


@dp.callback_query(F.data == 'debt')
async def debt(message: CallbackQuery, state: FSMContext) -> None:
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
    await bot.edit_message_text(chat_id=message.from_user.id, text=f"Ваша текущая задолженность - {debt} руб.")


@dp.callback_query(F.data == 'go_back')
async def go_back(message: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    kb = [[InlineKeyboardButton(text='Заказать справку', callback_data='inquiry'),
           InlineKeyboardButton(text='Узнать долг', callback_data='debt'), ], ]
    markup = InlineKeyboardMarkup(inline_keyboard=kb)
    await bot.edit_message_text(message_id=message.message.message_id, chat_id=message.from_user.id,
                                text='Что вы хотите сделать?', reply_markup=markup)


@dp.callback_query(F.data == 'inquiry')
async def inquiry(message: CallbackQuery, state: FSMContext) -> None:
    kb = [[InlineKeyboardButton(text='Для военкомата', callback_data='inquiry_rectal'),
           InlineKeyboardButton(text='По месту требования', callback_data='inquiry_request'), ],
          [InlineKeyboardButton(text='Назад', callback_data='go_back')]]
    markup = InlineKeyboardMarkup(inline_keyboard=kb)
    await bot.edit_message_text(message_id=message.message.message_id, chat_id=message.from_user.id,
                                text="Для чего вам нужна справка?", reply_markup=markup)


@dp.callback_query(F.data == 'inquiry_request')
async def inquiry_request(message: CallbackQuery, state: FSMContext) -> None:
    kb = [[InlineKeyboardButton(text='Назад', callback_data='go_back')]]
    markup = InlineKeyboardMarkup(inline_keyboard=kb)
    user: Student = db.query(Student).filter(Student.telegram_id == message.from_user.id).first()
    birthday = datetime.strptime(user.datehb, "%Y-%m-%d").strftime("%d.%m.%Y")
    message_text = (f"Заявка на справку по месту требования\n"
                    f"ФИО: {user.secondname} {user.namee} {user.midlename}\n"
                    f"Дата рождения: {birthday}\n")
    #file = create_inquiry(user)
    await bot.edit_message_text(message_id=message.message.message_id, chat_id=message.from_user.id,
                                text="Заявка успешно создана!", reply_markup=markup)
    await bot.send_message(224852677, text=message_text)


@dp.callback_query(F.data == 'inquiry_rectal')
async def inquiry_recal(message: CallbackQuery, state: FSMContext) -> None:
    kb = [[InlineKeyboardButton(text='Назад', callback_data='go_back')]]
    markup = InlineKeyboardMarkup(inline_keyboard=kb)
    await bot.edit_message_text(message_id=message.message.message_id, chat_id=message.from_user.id,
                                text="Введите наименование военкомата", reply_markup=markup)
    await state.set_state(States.rectal_input)
    message_id = message.message.message_id
    await state.update_data(dict(msg=message_id))


@dp.message(States.rectal_input)
async def inquiry_rectal_input(message: Message, state: FSMContext) -> None:
    kb = [[InlineKeyboardButton(text='Назад', callback_data='go_back')]]
    markup = InlineKeyboardMarkup(inline_keyboard=kb)
    user: Student = db.query(Student).filter(Student.telegram_id == message.from_user.id).first()
    birthday = datetime.strptime(user.datehb, "%Y-%m-%d").strftime("%d.%m.%Y")
    message_text = (f"Заявка на справку в военкомат\n"
                    f"Военкомат: {message.text}n"
                    f"ФИО: {user.secondname} {user.namee} {user.midlename}\n"
                    f"Дата рождения: {birthday}\n")
    # file = create_inquiry(user)
    data = await state.get_data()
    await bot.edit_message_text(message_id=data["message_id"], chat_id=message.from_user.id,
                                text="Заявка успешно создана!", reply_markup=markup)
    await bot.send_message(224852677, text=message_text)
    await state.clear()
