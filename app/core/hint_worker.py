from app.application.interfaces.hint_worker import IHintWorker


class HintWorker(IHintWorker):

    async def generate_hint(self, level_description: str) -> str:
        pass
