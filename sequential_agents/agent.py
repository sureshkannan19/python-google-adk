from dotenv import load_dotenv
from google.adk import Agent
from google.adk.agents import SequentialAgent
from google.adk.tools import google_search

load_dotenv()

MODEL = "gemini-2.5-flash"

# -- Sequential Agent ---
# Destination Research Agent - Researches location information
destination_research_agent = Agent(
    name="DestinationResearchAgent",
    model=MODEL,
    tools=[google_search],
    description="An agent that researches travel destinations and gathers essential information",
    instruction="""
    You are a travel researcher. You will be given a destination and travel preferences, and you will research:
    - Best time to visit and weather patterns
    - Top attractions and must-see locations
    - Local culture, customs, and etiquette tips
    - Transportation options within the destination
    - Safety considerations and travel requirements
    Provide comprehensive destination insights for trip planning.
    """,
    output_key="destination_research",
)

# Itinerary Builder Agent - Creates detailed travel schedule
itinerary_builder_agent = Agent(
    model=MODEL,
    name="ItineraryBuilderAgent",
    description="An agent that creates structured travel itineraries with daily schedules",
    instruction="""
    You are a professional travel planner. Using the research from "destination_research" output, create a detailed itinerary that includes:
    - Day-by-day schedule with recommended activities
    - Suggested accommodation areas or districts
    - Estimated time requirements for each activity
    - Meal recommendations and dining suggestions
    - Budget estimates for major expenses
    Structure it logically for easy following during the trip.
    """,
    output_key="travel_itinerary",
)

# Travel Optimizer Agent - Adds practical tips and optimizations
travel_optimizer_agent = Agent(
    model=MODEL,
    name="TravelOptimizerAgent",
    description="An agent that optimizes travel plans with practical advice and alternatives",
    instruction="""
    You are a seasoned travel consultant. Using the itinerary from "travel_itinerary" output, optimize it by adding:
    - Money-saving tips and budget alternatives
    - Packing recommendations specific to the destination
    - Backup plans for weather or unexpected situations
    - Local apps, websites, or resources to download
    - Cultural do's and don'ts for respectful travel

    Format the final output as:

    ITINERARY: {travel_itinerary}

    OPTIMIZATION TIPS: [your money-saving and practical tips here]

    TRAVEL ESSENTIALS: [packing and preparation advice here]

    BACKUP PLANS: [alternative options and contingencies here]
    """,
)

root_agent = SequentialAgent(
    name="TravelPlanningSystem",
    description="A comprehensive system that researches destinations, builds itineraries, and optimizes travel plans",
    sub_agents=[
        destination_research_agent,
        itinerary_builder_agent,
        travel_optimizer_agent,
    ],
)
