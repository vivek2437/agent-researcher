
from core.llm import generate_response
from core.prompts import RESEARCH_SYSTEM_PROMPT


def plan_research(topic: str):
    """
    Creates a research plan for a given topic.
    """

    system_prompt = """
    You are a research planner.
    Break the topic into structured research steps.
    """

    user_prompt = f"Create a research plan for: {topic}"

    return generate_response(system_prompt, user_prompt)
