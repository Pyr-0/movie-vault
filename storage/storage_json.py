import json
from typing import Dict, Any
from .istorage import IStorage

class StorageJson(IStorage):
	"""JSON implementation of the movie storage interface."""
		
	def __init__(self, file_path: str):
		"""Initialize the JSON storage.
		
		Args:
			file_path: Path to the JSON file that stores the movies
		"""
		self._file_path = file_path
		
	def _read_data(self) -> Dict[str, Dict[str, Any]]:
		"""Helper method to read data from the JSON file.
		
		Returns:
			Dictionary containing the movie data
		"""
		try:
			with open(self._file_path, 'r') as file:
				return json.load(file)
		except FileNotFoundError:
			return {}
			
	def _write_data(self, data: Dict[str, Dict[str, Any]]) -> None:
		"""Helper method to write data to the JSON file.
		
		Args:
			data: Dictionary containing the movie data to write
		"""
		with open(self._file_path, 'w') as file:
			json.dump(data, file, indent=4)
			
	def list_movies(self) -> Dict[str, Dict[str, Any]]:
		"""Returns all movies from the JSON storage.
		
		Returns:
			Dictionary containing all stored movies
		"""
		return self._read_data()
		
	def add_movie(self, title: str, year: int, rating: float, poster: str) -> None:
		"""Adds a new movie to the JSON storage.
		
		Args:
			title: The title of the movie
			year: The release year of the movie
			rating: The rating of the movie
			poster: URL to the movie poster
		"""
		movies = self._read_data()
		movies[title] = {
			"year": year,
			"rating": rating,
			"poster": poster,
			"notes": ""  # Initialize with empty notes
		}
		self._write_data(movies)
		
	def delete_movie(self, title: str) -> None:
		"""Deletes a movie from the JSON storage.
		
		Args:
			title: The title of the movie to delete
		"""
		movies = self._read_data()
		if title in movies:
			del movies[title]
			self._write_data(movies)
			
	def update_movie(self, title: str, notes: str) -> None:
		"""Updates a movie's notes in the JSON storage.
		
		Args:
			title: The title of the movie to update
			notes: The new notes for the movie
		"""
		movies = self._read_data()
		if title in movies:
			movies[title]["notes"] = notes
			self._write_data(movies) 