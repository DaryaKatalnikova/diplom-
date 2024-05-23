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
    nameschool: Mapped[str] = mapped_column(String(300), nullable=False)


class Cours(Base):
    __tablename__ = 'cours'
    id_cours: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    number_cours: Mapped[int] = mapped_column(Integer, nullable=False)


class Plan_pay(Base):
    __tablename__ = 'plan_pay'
    id_plan_pay: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    summa_b: Mapped[float] = mapped_column(Float, nullable=False)
    summa_vb: Mapped[float] = mapped_column(Float, nullable=False)
    plan_date: Mapped[date] = mapped_column(Date, nullable=False)
    id_cours: Mapped[int] = mapped_column(ForeignKey('cours.id_cours'), nullable=False)
    cours: Mapped["Cours"] = relationship("cours", backref="plan_pay")


class Ugroup(Base):
    __tablename__ = 'ugroup'
    id_group: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name_group: Mapped[str] = mapped_column(String(10), nullable=False)
    id_cours: Mapped[int] = mapped_column(ForeignKey('cours.id_cours'), nullable=False)
    cours: Mapped["Cours"] = relationship("cours", backref="plan_pay")


class Student(Base):
    __tablename__ = 'student'
    id_student: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    telegram_id: Mapped[int] = mapped_column(Integer, nullable=False)
    namee: Mapped[str] = mapped_column(String(100), nullable=False)
    secondname: Mapped[str] = mapped_column(String(100), nullable=False)
    midlename: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    numberphone: Mapped[str] = mapped_column(String(100), nullable=False)
    vidanpasport: Mapped[str] = mapped_column(String(100), nullable=False)
    propiska: Mapped[str] = mapped_column(String(100), nullable=False)
    projivanie: Mapped[str] = mapped_column(String(100), nullable=True)
    numberpasport: Mapped[str] = mapped_column(String(100), nullable=False)
    bazovoeobrazovanie: Mapped[str] = mapped_column(String(100), nullable=False)
    oplata: Mapped[str] = mapped_column(String(100), nullable=False)
    datepasport: Mapped[date] = mapped_column(Date, nullable=False)
    datehb: Mapped[date] = mapped_column(Date, nullable=False)
    srednocenka: Mapped[float] = mapped_column(Float, nullable=False)
    srednocenkaattestat: Mapped[float] = mapped_column(Float, nullable=False)
    id_school: Mapped[int] = mapped_column(ForeignKey("school.id_school"), nullable=True)
    id_group: Mapped[int] = mapped_column(ForeignKey("ugroup.id_group"), nullable=True)
    school: Mapped["School"] = relationship("school", backref="student")
    group: Mapped["Ugroup"] = relationship("ugroup", backref="student")


class Pay(Base):
    __tablename__ = 'pay'
    id_pay: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    summa: Mapped[float] = mapped_column(Float, nullable=False)
    pay_date: Mapped[date] = mapped_column(Date, nullable=False)
    id_student: Mapped[int] = mapped_column(ForeignKey('student.id_student'), nullable=False)
    student: Mapped["Student"] = relationship("student", backref="pay")


class Dogovor(Base):
    __tablename__ = 'dogovor'
    id_dogovor: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    numberdogovor: Mapped[str] = mapped_column(String(100), nullable=False)
    datedogovor: Mapped[date] = mapped_column(Date, nullable=False)
    placeBud: Mapped[str] = mapped_column(String(50), nullable=False)
    id_student: Mapped[int] = mapped_column(ForeignKey('student.id_student'), nullable=False)
    student: Mapped["Student"] = relationship("student", backref="pay")


class Ocenki(Base):
    __tablename__ = 'ocenki'
    id_ocenki: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    predmet: Mapped[str] = mapped_column(String(100), nullable=False)
    ocenka: Mapped[int] = mapped_column(Integer, nullable=False)
    id_student: Mapped[int] = mapped_column(ForeignKey('student.id_student'), nullable=False)
    student: Mapped["Student"] = relationship("student", backref="pay")


class Roditel(Base):
    __tablename__ = 'roditel'
    id_roditel: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    namee: Mapped[str] = mapped_column(String(100), nullable=False)
    secondname: Mapped[str] = mapped_column(String(100), nullable=False)
    midlename: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    numberphone: Mapped[str] = mapped_column(String(100), nullable=False)
    numberpasport: Mapped[str] = mapped_column(String(100), nullable=False)
    vidanpasport: Mapped[str] = mapped_column(String(100), nullable=False)
    propiska: Mapped[str] = mapped_column(String(100), nullable=False)
    projivanie: Mapped[str] = mapped_column(String(100), nullable=False)
    datepasport: Mapped[date] = mapped_column(Date, nullable=False)
    id_student: Mapped[int] = mapped_column(ForeignKey('student.id_student'), nullable=False)
    student: Mapped["Student"] = relationship("student", backref="pay")
