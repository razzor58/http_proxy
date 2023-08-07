import json


async def test_get_status(cli):
    for i in range(2):
        resp = await cli.get("/status")
    data = json.loads(await resp.text())
    assert data["requests_processed"] == 1


async def test_ok_request(cli):
    response = await cli.post(
        "/api/user", json={"login": "test123@test.com", "password": "test"}
    )

    print(await response.text())
    assert response.status == 200


async def test_bad_request(cli):
    response = await cli.get("/api/user")
    assert response.status == 405


async def test_wrong_content_type(cli):
    response = await cli.post(
        "/api/user",
        data={"login": "test123@test.com", "password": "test"},
        headers={"Content-Type": "application/xml"},
    )

    txt = await response.text()
    assert "content type is accessible" in txt
