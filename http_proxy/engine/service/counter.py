import logging

from datetime import datetime

logger = logging.getLogger(__name__)


class StatCounter:
    def __init__(self):
        self.requests_processed: int = 0
        self.start_time: datetime = datetime.now()

    @property
    def uptime(self) -> str:
        return str(datetime.now() - self.start_time)


def setup_counter(app):
    app.counter = StatCounter()
