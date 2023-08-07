build:
	docker-compose build proxy

run:
	docker-compose up

test:
	docker-compose run proxy pytest --disable-pytest-warnings