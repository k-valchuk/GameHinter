from abc import ABC, abstractmethod


class IHintWorker(ABC):

    @abstractmethod
    async def generate_hint(self, level_id: int) -> str:
        raise NotImplementedError
