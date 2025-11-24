from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


from app.agent.prompts import RequirementsAgentPrompt
from app.agent.response_model import RequirementsAgentResponseModel
from app.agent.tools import search_flight_availability

llm = ChatOpenAI(model="gpt-4.1", temperature=0)

agenet = create_agent()