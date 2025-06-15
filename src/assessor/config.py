"""
Configuration module for the assessor package.

This module centralizes configuration settings and provides factory functions
for creating gateway instances, making the system more testable.
"""

import os
from typing import Dict, List, Optional, Any

from mojentic.llm import LLMBroker
from mojentic.llm.gateways import OpenAIGateway, OllamaGateway

# Default model configurations
DEFAULT_OPENAI_MODELS = [
    "gpt-4o", 
    "gpt-4.1", 
    "gpt-4.1-mini", 
    "gpt-4.1-nano", 
    "o3-mini", 
    "o4-mini"
]

DEFAULT_OLLAMA_MODELS = [
    "qwen3:32b", 
    "qwen3:30b", 
    "qwen3:30b-a3b-q4_K_M", 
    "qwen2.5:32b", 
    "qwen2.5-coder:32b", 
    "qwen2.5-coder:7b", 
    "qwen2.5:72b", 
    "llama3.3-70b-32k"
]

DEFAULT_ASSESSMENT_MODEL = "o1"

class Config:
    """Configuration class for the assessor package."""
    
    def __init__(
        self,
        openai_api_key: Optional[str] = None,
        openai_models: Optional[List[str]] = None,
        ollama_models: Optional[List[str]] = None,
        assessment_model: str = DEFAULT_ASSESSMENT_MODEL,
        custom_config: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize the configuration.
        
        Args:
            openai_api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            openai_models: List of OpenAI models to use
            ollama_models: List of Ollama models to use
            assessment_model: Model to use for assessments
            custom_config: Additional custom configuration options
        """
        self.openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        self.openai_models = openai_models or DEFAULT_OPENAI_MODELS
        self.ollama_models = ollama_models or DEFAULT_OLLAMA_MODELS
        self.assessment_model = assessment_model
        self.custom_config = custom_config or {}
        
    def get_openai_gateway(self) -> OpenAIGateway:
        """Get an instance of the OpenAI gateway."""
        return OpenAIGateway(api_key=self.openai_api_key)
        
    def get_ollama_gateway(self) -> OllamaGateway:
        """Get an instance of the Ollama gateway."""
        return OllamaGateway()
        
    def get_assessment_llm(self) -> LLMBroker:
        """Get an LLM broker for generating assessments."""
        return LLMBroker(model=self.assessment_model, gateway=self.get_openai_gateway())

# Default configuration instance
default_config = Config()