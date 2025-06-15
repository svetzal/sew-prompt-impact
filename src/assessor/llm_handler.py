"""
LLM interaction utilities for the assessor module.
"""

from pathlib import Path
from typing import Union

from mojentic.llm import LLMBroker
from mojentic.llm.gateways.models import LLMMessage

from assessor.config import default_config
from assessor.file_gateway import FileGateway
from assessor.utils import strip_thinking


def process_with_model(
    file_path: Union[str, Path], 
    model_name: str, 
    gateway, 
    file_gateway: FileGateway = None
):
    """
    Process a file with a specific LLM model.

    Args:
        file_path: Path to the file to process
        model_name: Name of the model to use
        gateway: LLM gateway (OpenAI or Ollama)
        file_gateway: Optional FileGateway instance (defaults to a new instance)

    Returns:
        str: The processed response
    """
    # Use provided file gateway or create a new one
    file_gateway = file_gateway or FileGateway()

    # Read the file contents
    file_contents = file_gateway.read_file(file_path)

    # Create an LLMMessage with the file contents
    message = LLMMessage(content=file_contents)

    # Create LLM broker with the specified model and gateway
    llm = LLMBroker(model=model_name, gateway=gateway)

    # Send the message to the LLM
    response = llm.generate(messages=[message])

    # Strip out thinking text
    response = strip_thinking(response)

    return response

def get_assessment_llm(config=None):
    """
    Get the LLM broker for generating assessments.

    Args:
        config: Optional Config instance (defaults to default_config)

    Returns:
        LLMBroker: The LLM broker for assessments
    """
    config = config or default_config
    return config.get_assessment_llm()
