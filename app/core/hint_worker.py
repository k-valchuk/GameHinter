from langchain.chains.llm import LLMChain
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from loguru import logger

from app.application.interfaces.hint_worker import IHintWorker
from app.application.interfaces.level_storage import ILevelStorage
from app.application.interfaces.level_translator import ILevelTranslator
from app.config import Config


class HintWorker(IHintWorker):

    def __init__(
        self,
        config: Config,
        level_storage: ILevelStorage,
        level_translator: ILevelTranslator,
    ):

        template = (
            "На основе данных уровня, где указаны координаты игрока и ключевых объектов, выполни следующие шаги:\n"
            "1. Определи координаты игрока.\n"
            "2. Для каждого ключевого объекта вычисли расстояние от игрока до него, используя формулу евклидова расстояния: √((x_объекта - x_игрока)^2 + (y_объекта - y_игрока)^2).\n"
            "3. Выбери объект с минимальным расстоянием.\n"
            "4. Сформулируй одну краткую подсказку: укажи выбранный объект, его координаты и для чего он может пригодиться. Не раскрывай других деталей.\n"
            "\n"
            "В итоговом ответе выведи **только конечную подсказку без промежуточных рассуждений и пунктов, не выводя заголовки типа \"Выбранный объект:\"**.\n"
            "Данные уровня: {description}"
        )

        chat_prompt = ChatPromptTemplate.from_messages(
            [HumanMessagePromptTemplate.from_template(template)]
        )

        llm = ChatOpenAI(model="gpt-4o-mini", api_key=config.OPENAI_API_KEY)
        logger.info(llm.model_name)
        self.__chain = LLMChain(llm=llm, prompt=chat_prompt)

        self.__level_storage = level_storage
        self.__translator = level_translator

    async def __get_level_description(self, level_id: int) -> str:
        return await self.__translator.translate_level(
            self.__level_storage.get_level(level_id)
        )

    async def generate_hint(self, level_id: int) -> str:
        level_description = await self.__get_level_description(level_id)
        logger.info(level_description)
        return self.__chain.run(description=level_description)
