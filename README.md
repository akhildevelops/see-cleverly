## Development:
Install `uv` python package manager by running `curl -LsSf https://astral.sh/uv/install.sh | sh` and run `uv sync`

cp `env.example` from docker to `.env` and rename the env values if needed.
Run `docker compose -f docker/docker-compose.yml up -d` to setup infra.

Run Migrations `yoyo apply --database postgresql+psycopg://see_cleverly:see_cleverly@localhost:5432/see_cleverly` using defaults from [env.example](docker/env.example)

[know More on yoyo at](https://web.archive.org/web/20240126170305/https://ollycope.com/software/yoyo/latest/)