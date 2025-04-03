# 🎬 MovieVault

<div align="center">

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A modern, feature-rich movie collection manager built with Python, featuring OMDB API integration and a sleek web interface.

[Features](#✨-features) •
[Demo](#🚀-demo) •
[Installation](#💻-installation) •
[Usage](#📖-usage) •
[Architecture](#🏗️-architecture) •
[Security](#🔒-security)

</div>

## ✨ Features

- 🎯 **Smart Movie Search**: Automatically fetch movie details from OMDB API
- 💾 **Flexible Storage**: Choose between JSON or CSV storage backends
- 🌐 **Web Interface**: Generate a beautiful, responsive website to showcase your collection
- 🔄 **CRUD Operations**: Full Create, Read, Update, Delete functionality
- 📝 **Movie Notes**: Add personal notes to movies and view them on hover
- 🔐 **Secure Design**: Environment-based configuration management
- 🎨 **Modern UI**: Clean, responsive design with smooth hover effects

## 🚀 Demo

<div align="center">
Your movie collection comes to life with a modern, grid-based layout:

- 🖼️ Movie posters with hover effects
- 📊 Ratings displayed prominently
- 📝 Personal notes visible on hover
- 🎨 Consistent, professional styling
</div>

## 💻 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/movie-vault.git
   cd movie-vault
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your OMDB API key
   ```

## 📖 Usage

1. **Start the Application**
   ```bash
   python main.py
   ```

2. **Available Commands**
   ```
   1️⃣ List movies    - View your collection
   2️⃣ Add movie     - Add new movies (auto-fetches details)
   3️⃣ Delete movie  - Remove movies
   4️⃣ Update movie  - Add personal notes
   5️⃣ Generate web  - Create HTML showcase
   0️⃣ Exit         - Close application
   ```

## 🏗️ Architecture

```
movie-vault/
├── 📁 data/           # Storage directory
├── 📁 storage/        # Storage implementations
│   ├── 📄 istorage.py    # Storage interface
│   ├── 📄 storage_json.py # JSON storage
│   └── 📄 storage_csv.py  # CSV storage
├── 📁 templates/      # HTML templates
├── 📄 .env           # Configuration
├── 📄 main.py        # Entry point
├── 📄 movie_app.py   # Core logic
└── 📄 README.md      # Documentation
```

## 🔧 Storage Options

Choose your preferred storage backend:

```python
# JSON Storage (default)
storage = StorageJson("data/movies.json")

# CSV Storage
storage = StorageCsv("data/movies.csv")
```

## 🔒 Security

- ✅ Secure API key storage using environment variables
- ✅ `.env` file excluded from version control
- ✅ Example configuration provided in `.env.example`
- ✅ No sensitive data exposed in the generated website

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

## 📜 License

This project is licensed under the MIT License - making it perfect for both personal and commercial use.

---

<div align="center">

Made with ❤️ by [Your Name]

</div> 