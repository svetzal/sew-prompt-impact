"""
Assessor package for processing prompt files with various LLM models and generating assessments.
"""

from assessor.assessment import generate_assessment, generate_cross_prompt_assessment
from assessor.cli import main
from assessor.file_processor import get_available_prompt_styles, get_prompt_files
from assessor.processor import process_folder
from assessor.utils import strip_thinking

__all__ = [
    'process_folder',
    'generate_assessment',
    'generate_cross_prompt_assessment',
    'get_available_prompt_styles',
    'get_prompt_files',
    'strip_thinking',
    'main',
]