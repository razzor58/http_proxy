import aiohttp

from engine.config import settings
from engine.service.security import create_token
from engine.tools import WrongContentTypeException, handle_payload

routes = aiohttp.web.RouteTableDef()


@routes.view("/{tail:.*}")
class Proxy(aiohttp.web.View):
    async def post(self):
        try:
            payload = await handle_payload(self.request)
        except WrongContentTypeException as e:
            return aiohttp.web.Response(text=str(e))

        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=settings.TIMEOUT)
        ) as session:
            async with session.post(
                settings.target_url,
                headers={"x-my-jwt": create_token()},
                json=payload,
                verify_ssl=False,
            ) as response:
                text = await response.text()

        return aiohttp.web.Response(text=text)
