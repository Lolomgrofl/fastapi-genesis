from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class BaseDao(ABC):
    def __init__(self, session: AsyncSession):
        self.session = session

    @abstractmethod
    async def create(self, request):
        pass

    @abstractmethod
    async def get_by_id(self, id):
        pass

    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def delete_all(self):
        pass
