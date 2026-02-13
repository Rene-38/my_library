import uvicorn
from fastapi import FastAPI
from routers.books import router as books_router
from models.books import BookModel
from contextlib import asynccontextmanager
from database import engine, Model

@asynccontextmanager
async def lifespan(app: FastAPI):


    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

    print("База данных готова к работе")

    yield                                       #разделяет старт и выключение.

    print("Выключение сервера")

app = FastAPI(title="Book Manager API", description="Демонстрационное тестовое приложение по FastAPI, SQLAlchemy и Pydantic", lifespan=lifespan)
app.include_router(books_router)                #подключаем роутер к приложению.

