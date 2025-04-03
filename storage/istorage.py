from abc import ABC, abstractmethod
from typing import Dict, Any

class IStorage(ABC):
	"""Interface for movie storage implementations.
		
	This interface defines the contract that all storage implementations must follow.
	It provides methods for basic CRUD operations on movie data.
	"""
		
	@abstractmethod
	def list_movies(self) -> Dict[str, Dict[str, Any]]:
		"""Returns a dictionary of dictionaries containing movie information.
		
		Returns:
			Dict containing movie information in the format:
			{
				"Movie Title": {
					"rating": float,
					"year": int,
					"poster": str,
					"notes": str
				},
				...
			}
		"""
		pass

	@abstractmethod
	def add_movie(self, title: str, year: int, rating: float, poster: str) -> None:
		"""Adds a movie to the storage.
		
		Args:
			title: The title of the movie
			year: The release year of the movie
			rating: The rating of the movie
			poster: URL to the movie poster
		"""
		pass

	@abstractmethod
	def delete_movie(self, title: str) -> None:
		"""Deletes a movie from the storage.
		
		Args:
			title: The title of the movie to delete
		"""
		pass

	@abstractmethod
	def update_movie(self, title: str, notes: str) -> None:
		"""Updates a movie's notes in the storage.
		
		Args:
			title: The title of the movie to update
			notes: The notes to add to the movie
		"""
		pass 