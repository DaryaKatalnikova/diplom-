import logging, asyncio
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.bot import bot, dp
from bot.tasks import *
from bot.settings import BOT_WEBHOOK

""" PATTERN - APPLICATION FACTORY """


def create_app() -> web.Application:
    # Create aiohttp.web.Application instance
    bot.set_webhook(BOT_WEBHOOK)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot
    )
    webhook_requests_handler.register(app, path='/web')
    setup_application(app, dp, bot=bot)
    # init logger
    logging.basicConfig(filename='./log/actions.log', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    scheduler = make_sheduler()
    scheduler.start()
    return app


def make_sheduler() -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler()
    scheduler.add_job(func=sendNotification, trigger="interval", day_of_week='1', args=())
    return scheduler


async def main() -> None:
    try:
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


def run() -> None:
    asyncio.run(main())
