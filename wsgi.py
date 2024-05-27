from bot import create_app
from aiohttp import web

app = create_app()

if __name__ == '__main__':
    web.run_app(app)