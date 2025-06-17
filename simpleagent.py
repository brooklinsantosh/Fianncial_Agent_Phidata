from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

agent = Agent(
    model= Groq(id= 'deepseek-r1-distill-llama-70b'),
    description= "Yoa are an assistant please answer the questions",
    tools= [DuckDuckGoTools()],
    markdown= True
)

agent.print_response("can you find list jobs posted for Financial Planning & Analysis Manager in top companies in India from linkedin ")