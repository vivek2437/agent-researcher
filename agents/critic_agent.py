from core.llm import generate_response
from core.prompts import CRITIC_SYSTEM_PROMPT


def critique_content(content: str):
    """
    Critically evaluate research output.
    """

    return generate_response(
        CRITIC_SYSTEM_PROMPT,
        f"Critique the following research output:\n\n{content}"
    )
