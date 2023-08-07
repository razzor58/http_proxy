import logging

from aiohttp import web

logger = logging.getLogger(__name__)


@web.middleware
async def log_request_middleware(request: web.Request, handler) -> web.Response:
    response = await handler(request)
    request.app.counter.requests_processed += 1
    return response


def setup_middlewares(app):
    app.middlewares.append(log_request_middleware)
