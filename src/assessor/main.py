import os
import pathlib
import sys
from collections import defaultdict

from mojentic.llm import LLMBroker, MessageBuilder
from mojentic.llm.gateways import OpenAIGateway, OllamaGateway
from mojentic.llm.gateways.models import LLMMessage

openai = OpenAIGateway(api_key=os.getenv("OPENAI_API_KEY"))
ollama = OllamaGateway()


def process_folder(folder_path: str, use_ollama: bool = False):
    """
    Process all files in the given folder:
    1. Read each file's contents
    2. Send the contents to the LLM
    3. Write the output to a new file with "-output" suffix
    4. After all outputs are created, assess them using the o1-pro model
    5. Write the assessment to a new file with "-assessment" suffix

    Args:
        folder_path (str): Path to the folder containing files to process
    """
    folder = pathlib.Path(folder_path)

    # Ensure the folder exists
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"The path {folder_path} does not exist or is not a directory")

    # Dictionary to store output files for each source document
    output_files = defaultdict(list)

    # Process files with different models
    openai_models = ["gpt-4o", "gpt-4.1", "gpt-4.1-mini", "gpt-4.1-nano", "o3-mini", "o4-mini"]
    ollama_models = ["qwen3:32b", "qwen3:30b", "qwen3:30b-a3b-q4_K_M", "qwen2.5:32b", "qwen2.5-coder:32b", "qwen2.5-coder:7b", "qwen2.5:72b", "llama3.3-70b-32k"]
    # models = ["gpt-4o", "gpt-4.1-nano"]

    if use_ollama:
        models = ollama_models
        gateway = ollama
    else:
        models = openai_models
        gateway = openai

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

            # Read the file contents
            with open(file_path, 'r') as file:
                file_contents = file.read()

            # Create an LLMMessage with the file contents
            message = LLMMessage(content=file_contents)

            # Send the message to the LLM
            response = llm.generate(messages=[message])

            # Create the output file path
            output_file_path = file_path.with_name(
                f"{file_path.stem}-output-{llm_model_name.replace(":","-")}-{file_path.suffix}")

            # Write the response to the output file
            with open(output_file_path, 'w') as output_file:
                output_file.write(response)

            # Store the output file path for later assessment
            output_files[file_path].append(output_file_path)

            print(f"Processed {file_path.name} -> {output_file_path.name}")

    # Assess all outputs using o1-pro model
    llm = LLMBroker(model="o1", gateway=openai)

    for source_file, outputs in output_files.items():
        if not outputs:
            continue

        # Create assessment prompt
        assessment_prompt = f"""
        Please assess the quality and differences between the following outputs generated for the 
        source document '{source_file.name}'.
        In the assessment refer to each output by its filename.
        """

        mb = MessageBuilder(assessment_prompt)
        mb.add_file(source_file)
        mb.add_files(*outputs)

        assessment = llm.generate(messages=[mb.build()])

        assessment_file_path = source_file.with_name(
            f"{source_file.stem}-assessment{source_file.suffix}")
        with open(assessment_file_path, 'w') as assessment_file:
            assessment_file.write(assessment)

        print(f"Created assessment for {source_file.name} -> {assessment_file_path.name}")


if __name__ == "__main__":
    # If a folder path is provided as a command-line argument, use it
    # Otherwise, default to the 'prompts' folder
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = "prompts"

    process_folder(folder_path=folder_path, use_ollama=True)
    print(f"Successfully processed files in {folder_path}")
