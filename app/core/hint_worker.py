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
            "На основе данных уровня, где указаны координаты игрока и объектов, сформулируй одну краткую подсказку для прохождения игры. "
            "Если в данных уровня присутствуют объекты, для которых действуют семантические связи (например, дверь и ключ, мост и рычаг), учитывай их: "
            "указывай, что для открытия двери нужен ключ или для активации моста необходим рычаг. "
            "Если же такие объекты отсутствуют, опирайся только на фактические данные уровня и не придумывай объекты. "
            "Сформулируй итоговый ответ как единое предложение без промежуточных шагов, без нумерации и без лишних заголовков. "
            "Данные уровня: {description}"
        )



        chat_prompt = ChatPromptTemplate.from_messages(
            [HumanMessagePromptTemplate.from_template(template)]
        )

        self.__chain = LLMChain(
            llm=ChatOpenAI(model="gpt-4o-mini", api_key=config.OPENAI_API_KEY),
            prompt=chat_prompt,
        )

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
