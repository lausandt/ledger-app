from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from tortoise import Tortoise
# from tortoise.contrib.fastapi import register_tortoise


# from src.database.config import TORTOISE_ORM


# # allows queries made on any object can get the data from the related table.
# Tortoise.init_models(["src.database.models"], "models")

# # The import needs to be here otherwise generate pydantic models before the Tortoise ORM is initialised.
# from src.routers import users, entries  # noqa: E402


app = FastAPI(title="ledger-app", summary="A household-ledger app.")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # vue front end
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.include_router(users.router)
# app.include_router(entries.router)

# register_tortoise(app=app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
def root() -> dict[str, str]:
    return {"George": "George is an async rhino, very lazy indeed!"}