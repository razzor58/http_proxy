from typing import Dict

from aiohttp.web import Request

ACCEPTED_CONTENT_TYPE = ["application/json", "multipart/form-data"]


class WrongContentTypeException(Exception):
    pass


async def handle_payload(request: Request) -> Dict[str, str]:
    content_type = request.headers.get("Content-Type", "").lower()

    if "application/json" in content_type:
        return await request.json()

    if "multipart/form-data" in content_type:
        return dict(await request.post())

    raise WrongContentTypeException(
        "Only {} content type is accessible".format(ACCEPTED_CONTENT_TYPE)
    )
