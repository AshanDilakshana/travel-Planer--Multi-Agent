# agent creation part reffer langchain documentation
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

from app.agent.prompts.travel_system import (
    REQUIREMENTS_AGENT_SYSTEM_PROMPT,
    PLANNER_AGENT_SYSTEM_PROMPT,
    BOOKER_AGENT_SYSTEM_PROMPT,
)   

from app.agent.response_model import (
    RequirementsAgentResponseModel,
    PlannerAgentResponseModel,
    BookerAgentResponseModel,
)
    
from app.agent.tools.flight_tools import search_flight_availability
from app.agent.tools.planner_tools import web_search
from app.agent.tools.booking_tool import search_hotels, book_flight, book_hotel
from app.core.llm import llm

from app.config import settings

from app.core.llm import llm



requirements_agent = create_agent(
    model=llm,
    tools=[search_flight_availability],
    system_prompt=REQUIREMENTS_AGENT_SYSTEM_PROMPT,
    response_format=ToolStrategy(RequirementsAgentResponseModel),
)

planner_agent = create_agent(
    model=llm,
    name="planner",
    tools=[web_search],
    response_format=ToolStrategy(PlannerAgentResponseModel),
    system_prompt=PLANNER_AGENT_SYSTEM_PROMPT,
)

booker_agent = create_agent(
    model=llm,
    name="booker",
    tools=[book_flight, book_hotel, search_hotels],
    response_format=ToolStrategy(BookerAgentResponseModel),
    system_prompt=BOOKER_AGENT_SYSTEM_PROMPT,
)


if __name__ == "__main__":
    for chunk in agent.stream(  
        input={
            "messages": [
                "I want to go to Seoul(ICN) from Tokyo(NRT). My dates are flexible."
            ]
        },
        stream_mode="updates",
    ):
        print(chunk)

#gent.run("I want to book a flight from Colombo to Bangkok for 10th November 2025")