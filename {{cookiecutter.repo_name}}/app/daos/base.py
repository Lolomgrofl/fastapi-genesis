from abc import abstractmethod, ABC
from sqlalchemy.orm import Session


class BaseDao(ABC):
    def __init__(self, session: Session):
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
