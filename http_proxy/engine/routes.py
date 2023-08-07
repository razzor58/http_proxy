import logging

from engine.api import proxy, status

logger = logging.getLogger(__name__)


def setup_routes(app):
    app.router.add_routes(status.routes)
    app.router.add_routes(proxy.routes)

    logger.info("Registered API methods: ")
    for resource in app.router.resources():
        logger.info(resource)
