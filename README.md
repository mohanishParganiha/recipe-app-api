# Recipe App API

This is my first full project using **Django**, **Docker**, and **Git**.  
It is a simple API backend for managing recipes, created while following a course and learning best practices.

---

## 🛠️ Tech Stack

- **Python 3.9**
- **Django**
- **Docker + Docker Compose**
- **Flake8** for linting
- **GitHub Actions** for CI

---

## 🚀 Features

- Modular Django project with custom app structure
- Dockerized development environment
- Linting and tests with CI
- Clean and extendable setup

---

## ⚙️ Getting Started

### 🔧 Build and run the container

```bash
docker-compose build
docker-compose up

### 🧪 Run tests

```bash 
docker-compose run --rm app sh -c "python manage.py test"

### 🧼 Lint the code

```bash
docker-compose run --rm app sh -c "flake8"

## 📁 Project Structure

recipe-app-api/
├── app/           # Django project (settings, urls, etc.)
├── core/          # Custom app for models and features
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements.dev.txt
└── .github/workflows/  # GitHub Actions CI

## 👨‍💻 Author
Mohanish Parganiha
Learning Django, Docker, and backend development from scratch.

## 📚 Notes
This is a learning project based on a Udemy course.
More features and improvements will be added as I continue learning.

---

### ✅ How to use:

Save it as `README.md` in your root directory, then:

```bash
git add README.md
git commit -m "Add project README"
git push origin main
