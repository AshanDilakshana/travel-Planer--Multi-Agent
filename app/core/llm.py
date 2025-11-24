from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from app.config import settings

llm  = ChatOpenAI(model=settings.OPENAI_MODEL_NAME, api_key=SecretStr(settings.OPENAI_API_KEY))
