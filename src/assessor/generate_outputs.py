from mojentic.llm import LLMBroker
from mojentic.llm.gateways import LLMGateway
from mojentic.llm.gateways.models import LLMMessage

from assessor.output_processors.strip_thinking import strip_thinking


def generate_outputs(gateway: LLMGateway, models: list[str], folder, output_files, prompt_pattern):
    """
    Process files in the given folder using the specified LLM gateway and models.

    Args:
        gateway: The LLM gateway to use (e.g., OpenAIGateway, OllamaGateway)
        models: List of model names to use with the gateway
        folder: Path object pointing to the folder containing files to process
        output_files: Dictionary to collect output file paths
        prompt_pattern: Optional comma-separated list of style names to filter prompt files
    """
    for llm_model_name in models:
        llm = LLMBroker(model=llm_model_name, gateway=gateway)

        # Process each file in the folder
        for file_path in folder.iterdir():
            # Skip directories, non-markdown files, and output/assessment files
            if (file_path.is_dir() or
                    file_path.suffix.lower() != '.md' or
                    "output" in str(file_path) or
                    "assessment" in str(file_path)):
                continue

            # If prompt_pattern is provided, check if the file matches any of the specified styles
            if prompt_pattern:
                styles = [style.strip() for style in prompt_pattern.split(',')]
                if not any(file_path.stem == f"prompt-{style}" for style in styles):
                    continue

            # Read the file contents
            with open(file_path, 'r') as file:
                file_contents = file.read()

            # Create an LLMMessage with the file contents
            message = LLMMessage(content=file_contents)

            # Send the message to the LLM
            response = llm.generate(messages=[message])

            # Strip out thinking text
            response = strip_thinking(response)

            # Create the output file path
            output_file_path = file_path.with_name(
                f"{file_path.stem}-output-{llm_model_name.replace(':', '-')}{file_path.suffix}")

            # Write the response to the output file
            with open(output_file_path, 'w') as output_file:
                output_file.write(response)

            # Store the output file path for later assessment
            output_files[file_path].append(output_file_path)

            print(f"Processed {file_path.name} -> {output_file_path.name}")
