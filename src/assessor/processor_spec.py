"""
Tests for the processor module.
"""

from pathlib import Path

from assessor.config import Config
from assessor.file_gateway import FileGateway
from assessor.processor import process_folder


class DescribeProcessFolder:
    """Tests for the process_folder function."""

    def should_process_files_with_openai_models(self, mocker):
        """It should process files with OpenAI models."""
        # Arrange
        # Mock dependencies
        mock_config = mocker.Mock(spec=Config)
        mock_config.openai_models = ["test-model"]
        mock_config.get_openai_gateway.return_value = "openai-gateway"

        mock_file_gateway = mocker.Mock(spec=FileGateway)

        # Mock get_prompt_files to return a list of files
        mock_get_prompt_files = mocker.patch("assessor.processor.get_prompt_files")
        mock_get_prompt_files.return_value = [Path("test_file.md")]

        # Mock process_with_model to return a response
        mock_process_with_model = mocker.patch("assessor.processor.process_with_model")
        mock_process_with_model.return_value = "test response"

        # Mock create_output_file_path to return an output file path
        mock_create_output_file_path = mocker.patch("assessor.processor.create_output_file_path")
        mock_create_output_file_path.return_value = Path("test_file-output-test-model.md")

        # Mock generate_assessment to return an assessment
        mock_generate_assessment = mocker.patch("assessor.processor.generate_assessment")
        mock_generate_assessment.return_value = "test assessment"

        # Mock create_assessment_file_path to return an assessment file path
        mock_create_assessment_file_path = mocker.patch("assessor.processor.create_assessment_file_path")
        mock_create_assessment_file_path.return_value = Path("test_file-assessment.md")

        # Act
        result = process_folder(
            folder_path="test_folder",
            use_openai=True,
            use_ollama=False,
            config=mock_config,
            file_gateway=mock_file_gateway
        )

        # Assert
        # Verify that get_prompt_files was called with the correct arguments
        mock_get_prompt_files.assert_called_once_with("test_folder", None, mock_file_gateway)

        # Verify that process_with_model was called with the correct arguments
        mock_process_with_model.assert_called_once_with(
            Path("test_file.md"), 
            "test-model", 
            "openai-gateway", 
            mock_file_gateway
        )

        # Verify that create_output_file_path was called with the correct arguments
        mock_create_output_file_path.assert_called_once_with(Path("test_file.md"), "test-model")

        # Verify that file_gateway.write_file was called with the correct arguments
        mock_file_gateway.write_file.assert_called_with(
            Path("test_file-output-test-model.md"), 
            "test response"
        )

        # Verify that generate_assessment was called with the correct arguments
        mock_generate_assessment.assert_called_once_with(
            Path("test_file.md"), 
            [Path("test_file-output-test-model.md")],
            mock_config,
            mock_file_gateway
        )

        # Verify that create_assessment_file_path was called with the correct arguments
        mock_create_assessment_file_path.assert_called_once_with(Path("test_file.md"))

        # Verify that file_gateway.write_file was called with the correct arguments for the assessment
        mock_file_gateway.write_file.assert_called_with(
            Path("test_file-assessment.md"), 
            "test assessment"
        )

        # Verify that the result is correct
        assert len(result) == 1
        assert Path("test_file.md") in result
        assert result[Path("test_file.md")] == [Path("test_file-output-test-model.md")]
