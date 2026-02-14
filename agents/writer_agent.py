from core.llm import generate_response


def write_report(topic: str, analysis: str):
    """
    Generates final research report.
    """

    system_prompt = """
    You are an academic research writer.
    Write a structured research report with:
    - Introduction
    - Key Findings
    - Discussion
    - Conclusion
    """

    user_prompt = f"""
    Topic: {topic}

    Research Analysis:
    {analysis}
    """

    return generate_response(system_prompt, user_prompt)
