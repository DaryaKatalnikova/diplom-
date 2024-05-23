DB
-----
-----
Driver - MySQL <br>
ORM - SQLAlchemy <br>
Migrations - alembic


Migrations
------
------
MAKE MIGRATIONS IN *bot/migrations* <br>
alembic init migrations <br>
alembic revision --autogenerate -m 'your message' <br> 
alembic stamp *id migration*

ORM
----
----
all models is mapped in bot/models.py

BOT
----
----
Bot is based on webhook, deployment on wsgi/gunicorn<br> if you dont need an backend http server, then rewrite bot from webhook to polling