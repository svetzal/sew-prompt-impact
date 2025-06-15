"""
Utility functions for the assessor module.
"""

import re

def strip_thinking(text):
    """
    Strip out thinking text enclosed in <think>...</think> tags from the response.

    Args:
        text (str): The text to process

    Returns:
        str: The text with thinking sections removed
    """
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)