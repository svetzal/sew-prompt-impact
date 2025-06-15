"""
File processing utilities for the assessor module.
"""

import re
from pathlib import Path
from typing import Optional, Union

from assessor.file_gateway import FileGateway


def get_available_prompt_styles(
    folder_path: Union[str, Path],
    file_gateway: Optional[FileGateway] = None
):
    """
    Extract all available prompt styles from the folder.

    Args:
        folder_path: Path to the folder containing prompt files
        file_gateway: Optional FileGateway instance (defaults to a new instance)

    Returns:
        list: List of available prompt styles
    """
    # Use provided file gateway or create a new one
    file_gateway = file_gateway or FileGateway()

    styles = []

    # Get all markdown files that are not output or assessment files
    files = file_gateway.list_files_with_pattern(
        folder_path, 
        suffix='.md', 
        exclude_patterns=["output", "assessment"]
    )

    for file_path in files:
        # Extract style from prompt filename (pattern: "prompt-{style}.md")
        match = re.match(r'prompt-(.+)\.md$', file_path.name)
        if match:
            styles.append(match.group(1))

    return styles

def get_prompt_files(
    folder_path: Union[str, Path], 
    prompt_pattern: Optional[str] = None,
    file_gateway: Optional[FileGateway] = None
):
    """
    Get prompt files from the folder, optionally filtered by prompt pattern.

    Args:
        folder_path: Path to the folder containing prompt files
        prompt_pattern: Optional comma-separated list of style names to filter prompt files
        file_gateway: Optional FileGateway instance (defaults to a new instance)

    Returns:
        list: List of pathlib.Path objects for prompt files
    """
    # Use provided file gateway or create a new one
    file_gateway = file_gateway or FileGateway()

    # Ensure the folder exists
    if not file_gateway.folder_exists(folder_path):
        raise ValueError(f"The path {folder_path} does not exist or is not a directory")

    # Get all markdown files that are not output or assessment files
    files = file_gateway.list_files_with_pattern(
        folder_path, 
        suffix='.md', 
        exclude_patterns=["output", "assessment"]
    )

    prompt_files = []

    for file_path in files:
        # If prompt_pattern is provided, check if the file matches any of the specified styles
        if prompt_pattern:
            styles = [style.strip() for style in prompt_pattern.split(',')]
            if not any(file_path.stem == f"prompt-{style}" for style in styles):
                continue

        prompt_files.append(file_path)

    return prompt_files

def create_output_file_path(file_path: Union[str, Path], model_name: str) -> Path:
    """
    Create the output file path for a given file and model.

    Args:
        file_path: Path to the source file
        model_name: Name of the model

    Returns:
        Path object for the output file
    """
    path = Path(file_path)
    return path.with_name(
        f"{path.stem}-output-{model_name.replace(':','-')}{path.suffix}")

def create_assessment_file_path(file_path: Union[str, Path]) -> Path:
    """
    Create the assessment file path for a given file.

    Args:
        file_path: Path to the source file

    Returns:
        Path object for the assessment file
    """
    path = Path(file_path)
    return path.with_name(
        f"{path.stem}-assessment{path.suffix}")
