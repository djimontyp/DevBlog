up:
	docker-compose -f docker-compose.yml up

up-d:
	docker-compose -f docker-compose.yml up -d

stop:
	docker-compose -f docker-compose.yml stop

build:
	docker-compose -f docker-compose.yml build

down:
	docker-compose -f docker-compose.yml down

down-v:
	docker-compose -f docker-compose.yml down -v

down-full:
	docker-compose -f docker-compose.yml down -v --rmi local

init-db:
	docker-compose -f docker-compose.yml run --rm web bash -c 'python -c "import utils;utils.fill_database()"'

test:
	docker-compose -f docker-compose.yml run --rm web bash -c 'python -m pytest -v --disable-warnings'
