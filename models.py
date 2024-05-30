from datetime import date
from sqlalchemy import create_engine, Float
from sqlalchemy import String, Integer, ForeignKey, Date
from sqlalchemy.orm import mapped_column, Mapped, relationship, declarative_base, scoped_session, sessionmaker

from typing import List
from bot.settings import *

# for postgresql using psycopg2

engine = create_engine(DATABASE_URI)
db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))

Base = declarative_base()


class School(Base):
    __tablename__ = 'school'
    id_school: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nameschool: Mapped[str] = mapped_column(String(300), nullable=True)


class Cours(Base):
    __tablename__ = 'cours'
    id_cours: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    number_cours: Mapped[int] = mapped_column(Integer, nullable=False)


class Plan_pay(Base):
    __tablename__ = 'plan_pay'
    id_plan_pay: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    summa_b: Mapped[float] = mapped_column(Float, nullable=True)
    summa_vb: Mapped[float] = mapped_column(Float, nullable=True)
    plan_date: Mapped[date] = mapped_column(Date, nullable=True)
    id_cours: Mapped[int] = mapped_column(ForeignKey('cours.id_cours'), nullable=True)
    cours: Mapped["Cours"] = relationship("cours", backref="plan_pay")


class Ugroup(Base):
    __tablename__ = 'ugroup'
    id_group: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name_group: Mapped[str] = mapped_column(String(10), nullable=True)
    id_cours: Mapped[int] = mapped_column(ForeignKey('cours.id_cours'), nullable=True)
    cours: Mapped["Cours"] = relationship("cours", backref="plan_pay")


class Student(Base):
    __tablename__ = 'student'
    id_student: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    telegram_id: Mapped[int] = mapped_column(Integer, nullable=True)
    namee: Mapped[str] = mapped_column(String(100), nullable=True)
    secondname: Mapped[str] = mapped_column(String(100), nullable=True)
    midlename: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    numberphone: Mapped[str] = mapped_column(String(100), nullable=True)
    vidanpasport: Mapped[str] = mapped_column(String(100), nullable=True)
    propiska: Mapped[str] = mapped_column(String(100), nullable=True)
    projivanie: Mapped[str] = mapped_column(String(100), nullable=True)
    numberpasport: Mapped[str] = mapped_column(String(100), nullable=True)
    bazovoeobrazovanie: Mapped[str] = mapped_column(String(100), nullable=True)
    oplata: Mapped[str] = mapped_column(String(100), nullable=True)
    datepasport: Mapped[date] = mapped_column(Date, nullable=True)
    datehb: Mapped[date] = mapped_column(Date, nullable=True)
    srednocenka: Mapped[float] = mapped_column(Float, nullable=True)
    srednocenkaattestat: Mapped[float] = mapped_column(Float, nullable=True)
    id_school: Mapped[int] = mapped_column(ForeignKey("school.id_school"), nullable=True)
    id_group: Mapped[int] = mapped_column(ForeignKey("ugroup.id_group"), nullable=True)
    school: Mapped["School"] = relationship("school", backref="student")
    group: Mapped["Ugroup"] = relationship("ugroup", backref="student")


class Pay(Base):
    __tablename__ = 'pay'
    id_pay: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    summa: Mapped[float] = mapped_column(Float, nullable=True)
    pay_date: Mapped[date] = mapped_column(Date, nullable=True)
    id_student: Mapped[int] = mapped_column(ForeignKey('student.id_student'), nullable=True)
    student: Mapped["Student"] = relationship("student", backref="pay")


class Dogovor(Base):
    __tablename__ = 'dogovor'
    id_dogovor: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    numberdogovor: Mapped[str] = mapped_column(String(100), nullable=True)
    datedogovor: Mapped[date] = mapped_column(Date, nullable=True)
    placeBud: Mapped[str] = mapped_column(String(50), nullable=True)
    id_student: Mapped[int] = mapped_column(ForeignKey('student.id_student'), nullable=True)
    student: Mapped["Student"] = relationship("student", backref="pay")


class Ocenki(Base):
    __tablename__ = 'ocenki'
    id_ocenki: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    predmet: Mapped[str] = mapped_column(String(100), nullable=True)
    ocenka: Mapped[int] = mapped_column(Integer, nullable=True)
    id_student: Mapped[int] = mapped_column(ForeignKey('student.id_student'), nullable=True)
    student: Mapped["Student"] = relationship("student", backref="pay")


class Roditel(Base):
    __tablename__ = 'roditel'
    id_roditel: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    namee: Mapped[str] = mapped_column(String(100), nullable=True)
    secondname: Mapped[str] = mapped_column(String(100), nullable=True)
    midlename: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    numberphone: Mapped[str] = mapped_column(String(100), nullable=True)
    numberpasport: Mapped[str] = mapped_column(String(100), nullable=True)
    vidanpasport: Mapped[str] = mapped_column(String(100), nullable=True)
    propiska: Mapped[str] = mapped_column(String(100), nullable=True)
    projivanie: Mapped[str] = mapped_column(String(100), nullable=True)
    datepasport: Mapped[date] = mapped_column(Date, nullable=True)
    id_student: Mapped[int] = mapped_column(ForeignKey('student.id_student'), nullable=True)
    student: Mapped["Student"] = relationship("student", backref="pay")
