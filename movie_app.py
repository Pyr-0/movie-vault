import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv
from storage.istorage import IStorage

class MovieApp:
	"""Main movie application class that handles user interaction and movie operations."""
		
	def __init__(self, storage: IStorage):
		"""Initialize the movie application.
		
		Args:
			storage: An implementation of IStorage to use for data persistence
			
		Raises:
			ValueError: If OMDB_API_KEY environment variable is not set
		"""
		# Load environment variables
		load_dotenv()
		
		self._storage = storage
		self._api_key = os.getenv("OMDB_API_KEY")
		
		if not self._api_key:
			raise ValueError(
				"OMDB_API_KEY environment variable is not set. "
				"Please create a .env file with your API key."
			)
		
	def _fetch_movie_info(self, title: str) -> Dict[str, Any] | None:
		"""Fetch movie information from OMDB API.
		
		Args:
			title: The title of the movie to search for
			
		Returns:
			Dictionary containing movie information or None if movie not found
			
		Raises:
			ConnectionError: If unable to connect to the OMDB API
		"""
		url = f"http://www.omdbapi.com/?apikey={self._api_key}&t={title}"
		try:
			response = requests.get(url)
			response.raise_for_status()
			data = response.json()
			
			if data.get("Response") == "True":
				return {
					"title": data["Title"],
					"year": int(data["Year"]),
					"rating": float(data["imdbRating"]),
					"poster": data["Poster"]
				}
			return None
		except requests.RequestException as e:
			raise ConnectionError(f"Failed to fetch movie data: {str(e)}")
			
	def _generate_website(self):
		"""Generate a static website displaying the movie collection."""
		movies = self._storage.list_movies()
		
		# Read the template
		with open("templates/index_template.html", "r") as file:
			template = file.read()
			
		# Generate movie grid HTML
		movie_grid = ""
		for title, info in movies.items():
			movie_grid += f'''
			<div class="movie">
				<div class="movie-poster-container">
					<img class="movie-poster" src="{info['poster']}" alt="{title} poster">
					<div class="movie-notes">{info.get('notes', '')}</div>
				</div>
				<div class="movie-info">
					<div class="movie-title">{title}</div>
					<div class="movie-year">{info['year']}</div>
					<div class="movie-rating">Rating: {info['rating']}/10</div>
				</div>
			</div>
			'''
			
		# Replace placeholders in template
		html_content = template.replace("__TEMPLATE_TITLE__", "My Movie Collection")
		html_content = html_content.replace("__TEMPLATE_MOVIE_GRID__", movie_grid)
		
		# Write the generated HTML
		with open("index.html", "w") as file:
			file.write(html_content)
			
		print("Website was generated successfully.")
		
	def _command_list_movies(self):
		"""List all movies in the storage."""
		movies = self._storage.list_movies()
		if not movies:
			print("No movies found.")
			return
			
		print("\nMovie Collection:")
		print("-" * 40)
		for title, info in movies.items():
			print(f"Title: {title}")
			print(f"Year: {info['year']}")
			print(f"Rating: {info['rating']}/10")
			print("-" * 40)
			
	def _command_add_movie(self):
		"""Add a new movie using OMDB API."""
		title = input("Enter movie title: ").strip()
		
		try:
			movie = self._fetch_movie_info(title)
			if movie:
				self._storage.add_movie(
					movie["title"],
					movie["year"],
					movie["rating"],
					movie["poster"]
				)
				print(f"\nMovie '{movie['title']}' added successfully!")
			else:
				print(f"\nMovie '{title}' not found in OMDB database.")
		except ConnectionError as e:
			print(f"\nError: {str(e)}")
			
	def _command_delete_movie(self):
		"""Delete a movie from storage."""
		title = input("Enter movie title to delete: ").strip()
		self._storage.delete_movie(title)
		print(f"\nMovie '{title}' deleted successfully!")
		
	def _command_update_rating(self):
		"""Update a movie's notes."""
		title = input("Enter movie title: ").strip()
		notes = input("Enter movie notes: ").strip()
		try:
			self._storage.update_movie(title, notes)
			print(f"\nMovie '{title}' notes updated successfully!")
		except KeyError:
			print(f"\nError: Movie '{title}' not found.")
			
	def run(self):
		"""Run the movie application's main loop."""
		while True:
			print("\nMovie App Menu:")
			print("1. List movies")
			print("2. Add movie")
			print("3. Delete movie")
			print("4. Update movie")
			print("5. Generate website")
			print("0. Exit")
			
			choice = input("\nEnter choice (0-5): ").strip()
			
			if choice == "1":
				self._command_list_movies()
			elif choice == "2":
				self._command_add_movie()
			elif choice == "3":
				self._command_delete_movie()
			elif choice == "4":
				self._command_update_rating()
			elif choice == "5":
				self._generate_website()
			elif choice == "0":
				print("\nGoodbye!")
				break
			else:
				print("\nInvalid choice. Please try again.") 