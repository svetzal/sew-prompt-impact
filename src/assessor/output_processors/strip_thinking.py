import re


def strip_thinking(text):
    """
    Strip out thinking text enclosed in <think>...</think> tags from the response.

    Args:
        text (str): The text to process

    Returns:
        str: The text with thinking sections removed
    """
    result = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    return result.strip()
