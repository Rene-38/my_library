from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from typing import Annotated
from fastapi import Depends

#Настройка URL. Создание файла базы данных library.db в корне директории.
DATABASE_URL = "sqlite+aiosqlite:///library.db"

#Создание движка.
engine = create_async_engine(DATABASE_URL)

#Создание фабрики сессий.
new_session = async_sessionmaker(engine, expire_on_commit=False)

#Базовый класс для моделей.
#MappeAsDataclass - позволяет использовать простой синтаксис типов (int, str) и избавляет от написания __init__ вручную".
#DeclarativeBase - сообщает SQLAlchemy что наследники этого класса - это таблицы БД".
class Model(MappedAsDataclass, DeclarativeBase):
    pass
async def get_db():
    async with new_session() as session:
        yield session

#Создаем аннотацию для типа, которая говорит о том, что это переменная типа AsyncSession и чтобы ее получить, нужно выполнить функцию get_db.
SessionDep = Annotated[AsyncSession, Depends(get_db)]


