from core.llm import generate_response
from core.prompts import ANALYSIS_SYSTEM_PROMPT


def analyze_content(content: str):
    """
    Extract key insights from research content.
    """

    return generate_response(
        ANALYSIS_SYSTEM_PROMPT,
        f"Analyze the following content:\n\n{content}"
    )
