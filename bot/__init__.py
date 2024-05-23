import logging
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from bot.bot import bot, dp
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
    return app
