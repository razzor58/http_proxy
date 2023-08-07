import logging

from aiohttp import web

from engine.config import settings
from engine.middleware import setup_middlewares
from engine.routes import setup_routes
from engine.service.counter import setup_counter

logging.basicConfig(level=logging.getLevelName(settings.LOG_LEVEL))
logger = logging.getLogger(__name__)


async def startup(app: web.Application):
    pass


async def on_shutdown(app: web.Application):
    pass


def create_app():
    app = web.Application(client_max_size=settings.max_body_in_bytes)
    setup_counter(app)
    setup_routes(app)
    setup_middlewares(app)

    app.on_startup.append(startup)
    app.on_shutdown.append(on_shutdown)

    return app


def start():
    logger.info("=== Initialize HTTP Proxy ===")
    app = create_app()
    web.run_app(app, port=settings.HTTP_PORT)
