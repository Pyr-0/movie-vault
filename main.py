import os
from storage.storage_json import StorageJson
from storage.storage_csv import StorageCsv
from movie_app import MovieApp

def main():
	"""Main entry point of the movie application."""
		
	# Create data directory if it doesn't exist
	os.makedirs("data", exist_ok=True)
		
	# Initialize storage (you can switch between JSON and CSV)
	storage = StorageJson("data/movies.json")  # or StorageCsv("data/movies.csv")
		
	# Create and run the movie app
	app = MovieApp(storage)
	app.run()

if __name__ == "__main__":
	main() 