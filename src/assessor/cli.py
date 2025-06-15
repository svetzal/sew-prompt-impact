"""
Prompt Impact Assessment Tool

This script processes prompt files with various LLM models and generates assessments.
It supports comparing different prompt styles (e.g., plain vs fancy) across multiple models
to answer questions like:
1. "Does this fancier prompt give me better results than the plain one?"
2. "What models respond best to the directives in the fancier prompt?"

Usage:
    assessor [options]

Options:
    --folder FOLDER     Folder containing prompt files (default: 'prompts')
    --openai            Use OpenAI models (default: True)
    --ollama            Use Ollama models (default: True)
    --prompt STYLE      Filter prompts by style name (e.g., "plain" or "fancy")
                        Files are expected to follow the pattern "prompt-{style}.md"
    --compare STYLES    Generate cross-prompt assessments for specified prompt styles
                        Example: --compare plain fancy

Example usage:
    # Process all prompts with both OpenAI and Ollama models
    assessor

    # Process only plain prompts with OpenAI models
    assessor --prompt plain --ollama False

    # Compare plain and fancy prompts across all models
    assessor --compare plain fancy
"""

import argparse
import sys

from assessor.assessment import generate_cross_prompt_assessment
from assessor.config import default_config
from assessor.file_gateway import FileGateway
from assessor.file_processor import get_available_prompt_styles
from assessor.processor import process_folder


def main():
    """
    Main entry point for the assessor CLI.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process prompts with LLMs and generate assessments')
    parser.add_argument('--folder', type=str, default='prompts', help='Folder containing prompt files')
    parser.add_argument('--openai', action='store_true', default=True, help='Use OpenAI models')
    parser.add_argument('--ollama', action='store_true', default=True, help='Use Ollama models')
    parser.add_argument('--prompt', type=str, help='Filter prompts by comma-separated style names (e.g., "plain,fancy"). Files are expected to follow the pattern "prompt-{style}.md"')
    parser.add_argument('--compare', nargs='+', help='Generate cross-prompt assessments for specified prompt styles')

    args = parser.parse_args()

    # Create file gateway and use default config
    file_gateway = FileGateway()
    config = default_config

    # Process prompts with LLMs
    process_folder(
        folder_path=args.folder, 
        use_openai=args.openai, 
        use_ollama=args.ollama, 
        prompt_pattern=args.prompt,
        config=config,
        file_gateway=file_gateway
    )
    print(f"Successfully processed files in {args.folder}")

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
        styles_to_compare = get_available_prompt_styles(args.folder, file_gateway)

    # Ensure we have at least two styles to compare
    if len(styles_to_compare) < 2:
        print("Error: At least two prompt styles are required for comparison.")
        sys.exit(1)

    # Generate cross-prompt assessments
    print(f"Generating cross-prompt assessments for styles: {', '.join(styles_to_compare)}")
    assessment_files = generate_cross_prompt_assessment(
        folder_path=args.folder, 
        prompt_styles=styles_to_compare,
        config=config,
        file_gateway=file_gateway
    )

    if assessment_files:
        print(f"Created {len(assessment_files)} cross-prompt assessments")
        for model_name, file_path in assessment_files.items():
            print(f"  - {model_name}: {file_path.name}")
    else:
        print("No cross-prompt assessments were generated")

    print("Cross-prompt assessments completed")

if __name__ == "__main__":
    main()
