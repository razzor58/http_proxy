from aiohttp import web

routes = web.RouteTableDef()


@routes.view("/status")
async def get(self):
    return web.json_response(
        {
            "requests_processed": self.app.counter.requests_processed,
            "uptime": self.app.counter.uptime,
        }
    )
