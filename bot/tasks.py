from datetime import datetime, timedelta
from bot.bot import bot
from models import *


async def sendNotification():
    for student in db.query(Student).all():
        dogovor: Dogovor = db.query(Dogovor).filter(Dogovor.id_student == student.id_student).first()
        plan: Plan_pay = db.query(Plan_pay).filter(Plan_pay.id_cours == db.query(Ugroup).get(student.id_group).first().id_cours).first()
        debt = plan.summa_b if dogovor.placeBud == "Бюджет" else plan.summa_vb
        pays: list[Pay] = db.query(Pay).filter(Pay.id_student == student.id_student,
                                               Pay.pay_date <= datetime.strptime(plan.plan_date, '%Y-%m-%d')-timedelta(weeks=24)).all()
        for pay in pays:
            debt -= pay.summa
        await bot.send_message(student.telegram_id, f"Ваша текущая задолженность - {debt} руб.")
