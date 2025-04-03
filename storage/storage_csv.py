import csv
from typing import Dict, Any
from .istorage import IStorage

class StorageCsv(IStorage):
	"""CSV implementation of the movie storage interface."""
		
	def __init__(self, file_path: str):
		"""Initialize the CSV storage.
		
		Args:
			file_path: Path to the CSV file that stores the movies
		"""
		self._file_path = file_path
		self._headers = ['title', 'year', 'rating', 'poster']
		
	def _read_data(self) -> Dict[str, Dict[str, Any]]:
		"""Helper method to read data from the CSV file.
		
		Returns:
			Dictionary containing the movie data
		"""
		movies = {}
		try:
			with open(self._file_path, 'r', newline='') as file:
				reader = csv.DictReader(file)
				for row in reader:
					title = row['title']
					movies[title] = {
						'year': int(row['year']),
						'rating': float(row['rating']),
						'poster': row['poster']
					}
		except FileNotFoundError:
			# Create the file with headers if it doesn't exist
			with open(self._file_path, 'w', newline='') as file:
				writer = csv.writer(file)
				writer.writerow(self._headers)
		return movies
			
	def _write_data(self, data: Dict[str, Dict[str, Any]]) -> None:
		"""Helper method to write data to the CSV file.
		
		Args:
			data: Dictionary containing the movie data to write
		"""
		with open(self._file_path, 'w', newline='') as file:
			writer = csv.DictWriter(file, fieldnames=self._headers)
			writer.writeheader()
			for title, info in data.items():
				writer.writerow({
					'title': title,
					'year': info['year'],
					'rating': info['rating'],
					'poster': info['poster']
				})
			
	def list_movies(self) -> Dict[str, Dict[str, Any]]:
		"""Returns all movies from the CSV storage.
		
		Returns:
			Dictionary containing all stored movies
		"""
		return self._read_data()
		
	def add_movie(self, title: str, year: int, rating: float, poster: str) -> None:
		"""Adds a new movie to the CSV storage.
		
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
			"poster": poster
		}
		self._write_data(movies)
		
	def delete_movie(self, title: str) -> None:
		"""Deletes a movie from the CSV storage.
		
		Args:
			title: The title of the movie to delete
		"""
		movies = self._read_data()
		if title in movies:
			del movies[title]
			self._write_data(movies)
			
	def update_movie(self, title: str, rating: float) -> None:
		"""Updates a movie's rating in the CSV storage.
		
		Args:
			title: The title of the movie to update
			rating: The new rating for the movie
		"""
		movies = self._read_data()
		if title in movies:
			movies[title]["rating"] = rating
			self._write_data(movies) 