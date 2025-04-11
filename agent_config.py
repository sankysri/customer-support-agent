# customer_support_agent/agent_config.py
import os
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from tools import search_knowledge_base, create_support_ticket

# ✅ Set your OpenAI API Key here
os.environ["OPENAI_API_KEY"] = ""

# Define available tools for the agent
tools = [
    Tool(
        name="search_knowledge_base",
        func=search_knowledge_base,
        description="Useful for answering user support queries by searching the company FAQ."
    ),
    Tool(
        name="create_support_ticket",
        func=create_support_ticket,
        description="Use this when the user's issue cannot be resolved from the KB."
    )
]

# Load LLM (use GPT-4 or GPT-3.5-turbo)
llm = ChatOpenAI(model_name="gpt-4", temperature=0.3)

# Initialize agent with ReAct style
agent_executor = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)
