from Config.config import model

def ask_ai(task: str) -> str:
    """
    Ask Gemini to break down task into automation steps.
    """
    response = model.generate_content(
        f"Break down this automation task step by step: {task}"
    )
    return response.text
