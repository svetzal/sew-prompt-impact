import pathlib
import re


def enumerate_available_prompt_styles(folder_path: str):
    """
    Extract all available prompt styles from the folder.

    Args:
        folder_path (str): Path to the folder containing prompt files

    Returns:
        list: List of available prompt styles
    """
    folder = pathlib.Path(folder_path)
    styles = []

    for file_path in folder.iterdir():
        if (file_path.is_dir() or
                file_path.suffix.lower() != '.md' or
                "output" in str(file_path) or
                "assessment" in str(file_path)):
            continue

        # Extract style from prompt filename (pattern: "prompt-{style}.md")
        match = re.match(r'prompt-(.+)\.md$', file_path.name)
        if match:
            styles.append(match.group(1))

    return styles
