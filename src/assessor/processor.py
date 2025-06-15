"""
Main processing logic for the assessor module.
"""

from collections import defaultdict
from typing import Optional

from assessor.assessment import generate_assessment
from assessor.config import default_config, Config
from assessor.file_gateway import FileGateway
from assessor.file_processor import get_prompt_files, create_output_file_path, \
    create_assessment_file_path
from assessor.llm_handler import process_with_model


def process_folder(
    folder_path: str, 
    use_openai: bool = True, 
    use_ollama: bool = True, 
    prompt_pattern: str = None,
    config: Optional[Config] = None,
    file_gateway: Optional[FileGateway] = None
):
    """
    Process all files in the given folder:
    1. Read each file's contents
    2. Send the contents to the LLM (both OpenAI and Ollama models if specified)
    3. Write the output to a new file with "-output" suffix
    4. After all outputs are created, assess them using the assessment model
    5. Write the assessment to a new file with "-assessment" suffix

    Args:
        folder_path: Path to the folder containing files to process
        use_openai: Whether to use OpenAI models
        use_ollama: Whether to use Ollama models
        prompt_pattern: Optional comma-separated list of style names to filter prompt files (e.g., "plain,fancy").
                       Files are expected to follow the pattern "prompt-{style}.md"
        config: Optional Config instance (defaults to default_config)
        file_gateway: Optional FileGateway instance (defaults to a new instance)

    Returns:
        dict: Dictionary mapping source files to their output files
    """
    # Use provided config or default
    config = config or default_config

    # Use provided file gateway or create a new one
    file_gateway = file_gateway or FileGateway()

    # Get prompt files to process
    prompt_files = get_prompt_files(folder_path, prompt_pattern)

    # Dictionary to store output files for each source document
    output_files = defaultdict(list)

    # Process OpenAI models if specified
    if use_openai:
        # Get OpenAI gateway
        openai_gateway = config.get_openai_gateway()

        for model_name in config.openai_models:
            for file_path in prompt_files:
                # Process the file with the model
                response = process_with_model(file_path, model_name, openai_gateway, file_gateway)

                # Create the output file path
                output_file_path = create_output_file_path(file_path, model_name)

                # Write the response to the output file
                file_gateway.write_file(output_file_path, response)

                # Store the output file path for later assessment
                output_files[file_path].append(output_file_path)

                print(f"Processed {file_path.name} -> {output_file_path.name}")

    # Process Ollama models if specified
    if use_ollama:
        # Get Ollama gateway
        ollama_gateway = config.get_ollama_gateway()

        for model_name in config.ollama_models:
            for file_path in prompt_files:
                # Process the file with the model
                response = process_with_model(file_path, model_name, ollama_gateway, file_gateway)

                # Create the output file path
                output_file_path = create_output_file_path(file_path, model_name)

                # Write the response to the output file
                file_gateway.write_file(output_file_path, response)

                # Store the output file path for later assessment
                output_files[file_path].append(output_file_path)

                print(f"Processed {file_path.name} -> {output_file_path.name}")

    # Generate assessments for each source file
    for source_file, outputs in output_files.items():
        if not outputs:
            continue

        # Generate assessment
        assessment = generate_assessment(source_file, outputs, config, file_gateway)

        if assessment:
            # Create assessment file path
            assessment_file_path = create_assessment_file_path(source_file)

            # Write the assessment to a file
            file_gateway.write_file(assessment_file_path, assessment)

            print(f"Created assessment for {source_file.name} -> {assessment_file_path.name}")

    return output_files
