"""Storage package for movie data persistence.

This package provides different storage implementations for the movie application.
Available implementations:
- JSON storage
- CSV storage
"""

from .istorage import IStorage
from .storage_json import StorageJson
from .storage_csv import StorageCsv

__all__ = ['IStorage', 'StorageJson', 'StorageCsv'] 