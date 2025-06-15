"""
File gateway module for the assessor package.

This module provides a gateway for file operations, making the system more testable
by isolating I/O operations behind a mockable interface.
"""

import pathlib
from typing import List, Optional, Union


class FileGateway:
    """Gateway for file operations."""
    
    def read_file(self, file_path: Union[str, pathlib.Path]) -> str:
        """
        Read the contents of a file.
        
        Args:
            file_path: Path to the file to read
            
        Returns:
            The contents of the file as a string
        """
        with open(file_path, 'r') as file:
            return file.read()
            
    def write_file(self, file_path: Union[str, pathlib.Path], content: str) -> None:
        """
        Write content to a file.
        
        Args:
            file_path: Path to the file to write
            content: Content to write to the file
        """
        with open(file_path, 'w') as file:
            file.write(content)
            
    def list_files(self, folder_path: Union[str, pathlib.Path]) -> List[pathlib.Path]:
        """
        List all files in a folder.
        
        Args:
            folder_path: Path to the folder to list files from
            
        Returns:
            List of pathlib.Path objects for files in the folder
        """
        folder = pathlib.Path(folder_path)
        return [file for file in folder.iterdir() if file.is_file()]
            
    def list_files_with_pattern(
        self, 
        folder_path: Union[str, pathlib.Path], 
        suffix: Optional[str] = None,
        exclude_patterns: Optional[List[str]] = None
    ) -> List[pathlib.Path]:
        """
        List files in a folder, optionally filtered by suffix and excluding patterns.
        
        Args:
            folder_path: Path to the folder to list files from
            suffix: Optional suffix to filter files by (e.g., '.md')
            exclude_patterns: Optional list of patterns to exclude from results
            
        Returns:
            List of pathlib.Path objects for files matching the criteria
        """
        folder = pathlib.Path(folder_path)
        exclude_patterns = exclude_patterns or []
        
        files = []
        for file_path in folder.iterdir():
            if not file_path.is_file():
                continue
                
            if suffix and file_path.suffix.lower() != suffix.lower():
                continue
                
            if any(pattern in str(file_path) for pattern in exclude_patterns):
                continue
                
            files.append(file_path)
            
        return files
        
    def ensure_folder_exists(self, folder_path: Union[str, pathlib.Path]) -> pathlib.Path:
        """
        Ensure a folder exists, creating it if necessary.
        
        Args:
            folder_path: Path to the folder
            
        Returns:
            pathlib.Path object for the folder
        """
        folder = pathlib.Path(folder_path)
        folder.mkdir(parents=True, exist_ok=True)
        return folder
        
    def file_exists(self, file_path: Union[str, pathlib.Path]) -> bool:
        """
        Check if a file exists.
        
        Args:
            file_path: Path to the file
            
        Returns:
            True if the file exists, False otherwise
        """
        return pathlib.Path(file_path).exists() and pathlib.Path(file_path).is_file()
        
    def folder_exists(self, folder_path: Union[str, pathlib.Path]) -> bool:
        """
        Check if a folder exists.
        
        Args:
            folder_path: Path to the folder
            
        Returns:
            True if the folder exists, False otherwise
        """
        return pathlib.Path(folder_path).exists() and pathlib.Path(folder_path).is_dir()