"""
Prompt Impact Assessment Tool

This script processes prompt files with various LLM models and generates assessments.
It supports comparing different prompt styles (e.g., plain vs fancy) across multiple models
to answer questions like:
1. "Does this fancier prompt give me better results than the plain one?"
2. "What models respond best to the directives in the fancier prompt?"

Usage:
    python cli.py [options]

Options:
    --folder FOLDER     Folder containing prompt files (default: 'prompts')
    --openai            Include OpenAI models in the assessment (default: True)
    --ollama            Include Ollama models in the assessment (default: True)
    --prompt STYLE      Filter prompts by style name (e.g., "plain" or "fancy")
                        Files are expected to follow the pattern "prompt-{style}.md"
    --compare STYLES    Generate cross-prompt assessments for specified prompt styles
                        Example: --compare plain fancy

Example usage:
    # Process all prompts with both OpenAI and Ollama models
    python cli.py

    # Process only plain prompts with OpenAI models
    python cli.py --prompt plain --ollama False

    # Compare plain and fancy prompts across all models
    python cli.py --compare plain fancy
"""

import argparse
import os
import pathlib
import sys
from collections import defaultdict
from typing import Optional

from mojentic.llm import LLMBroker
from mojentic.llm.gateways import OpenAIGateway, OllamaGateway

from assessor.cross_model_assessments import generate_cross_model_assessments
from assessor.cross_prompt_assessments import generate_cross_prompt_assessments
from assessor.generate_outputs import generate_outputs
from assessor.utils import enumerate_available_prompt_styles


def runner(folder_path: str, openai_models: list[str] = None, ollama_models: list[str] = None,
           prompt_pattern: Optional[str] = None, styles_to_compare: Optional[list[str]] = None):
    """
    Process all files in the given folder:
    1. Read each file's contents
    2. Send the contents to the LLM (using the provided OpenAI and Ollama models)
    3. Write the output to a new file with "-output" suffix
    4. After all outputs are created, assess them using the o1 model
    5. Write the assessment to a new file with "-assessment" suffix

    Args:
        folder_path (str): Path to the folder containing files to process
        openai_models (list[str]): List of OpenAI models to use
        ollama_models (list[str]): List of Ollama models to use
        prompt_pattern (str): Optional comma-separated list of style names to filter prompt files
        (e.g., "plain,fancy").
                             Files are expected to follow the pattern "prompt-{style}.md"
        styles_to_compare (list[str]): List of prompt styles to compare
    """
    folder = pathlib.Path(folder_path)
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"The path {folder_path} does not exist or is not a directory")

    openai = OpenAIGateway(api_key=os.getenv("OPENAI_API_KEY"))
    ollama = OllamaGateway()

    output_files_collector = defaultdict(list)

    generate_outputs(openai, openai_models, folder, output_files_collector, prompt_pattern)
    generate_outputs(ollama, ollama_models, folder, output_files_collector, prompt_pattern)

    llm = LLMBroker(model="o1", gateway=openai)

    print(
        f"Generating cross-model assessments for models: "
        f"{', '.join(openai_models + ollama_models)}")
    generate_cross_model_assessments(llm=llm, output_files_collector=output_files_collector)

    print(f"Generating cross-prompt assessments for styles: "
          f"{', '.join(styles_to_compare)}")
    generate_cross_prompt_assessments(llm=llm, folder_path=folder_path,
                                      prompt_styles=styles_to_compare)

    print("All assessments completed")


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Process prompts with LLMs and generate assessments')
    parser.add_argument('--folder', type=str, default='prompts',
                        help='Folder containing prompt files')
    parser.add_argument('--openai', action='store_true', default=True,
                        help='Include OpenAI models in the assessment')
    parser.add_argument('--ollama', action='store_true', default=True,
                        help='Include Ollama models in the assessment')
    parser.add_argument('--prompt', type=str,
                        help='Filter prompts by comma-separated style names (e.g., "plain,'
                             'fancy"). Files are expected to follow the pattern "prompt-{'
                             'style}.md"')
    parser.add_argument('--compare', nargs='+',
                        help='Generate cross-prompt assessments for specified prompt styles')

    args = parser.parse_args()

    # Define models
    openai_models = ["gpt-4o", "gpt-4.1", "gpt-4.1-mini", "gpt-4.1-nano", "o3-mini", "o4-mini"]
    ollama_models = ["qwen3:32b", "qwen3:30b", "qwen3:30b-a3b-q4_K_M", "qwen2.5:32b",
                     "qwen2.5-coder:32b", "qwen2.5-coder:7b", "qwen2.5:72b", "llama3.3-70b-32k"]

    # Determine which models to use based on args
    openai_models_to_use = openai_models if args.openai else []
    ollama_models_to_use = ollama_models if args.ollama else []

    # Determine which prompt styles to compare
    styles_to_compare = []

    if args.compare:
        # Use explicitly specified styles
        styles_to_compare = args.compare
    elif args.prompt:
        # Use styles from the prompt filter
        styles_to_compare = [style.strip() for style in args.prompt.split(',')]
    else:
        # Use all available styles
        styles_to_compare = enumerate_available_prompt_styles(args.folder)

    # Ensure we have at least two styles to compare
    if len(styles_to_compare) < 2:
        print("Error: At least two prompt styles are required for comparison.")
        sys.exit(1)

    # Process prompts with LLMs
    runner(folder_path=args.folder, openai_models=openai_models_to_use,
           ollama_models=ollama_models_to_use,
           prompt_pattern=args.prompt, styles_to_compare=styles_to_compare)
    print(f"Successfully processed files in {args.folder}")


if __name__ == "__main__":
    main()
