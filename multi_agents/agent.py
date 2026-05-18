from google.adk import Agent
from dotenv import load_dotenv

load_dotenv()

MODEL = "gemini-2.5-flash"

root_agent  = Agent(name="travel_planner_agent",
               model=MODEL,
               description="An agent that helps users plan their travel itineraries",
               instruction="You are a travel planner agent.")