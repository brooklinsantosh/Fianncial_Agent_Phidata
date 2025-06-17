from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

web_search_agent = Agent(
    name= "Web Search Agent",
    role= "Search the web and fetch the information",
    model= Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[DuckDuckGoTools()],
    instructions= ["Always include the source"],
    show_tool_calls= True,
    markdown= True,
)

financial_agent = Agent(
    name= "Financial Agent",
    role= "You are a financial analyst",
    model= Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[
            YFinanceTools(
                stock_price=True, 
                analyst_recommendations=True, 
                stock_fundamentals=True,
                company_news= True,
                technical_indicators= True
            )
        ],
    instructions= ["Use tables to display the data"],
    show_tool_calls= True,
    markdown= True,
)

agent_team = Agent(
    team= [web_search_agent, financial_agent],
    model= Groq(id="deepseek-r1-distill-llama-70b"),
    instructions= ["Always include sources", "Use tables to display the data"],
    show_tool_calls= True,
    markdown= True,
)


agent_team.print_response("Analyze magnificient 7 companies in NASDAQ US stock market and suggest one for long term investment.")