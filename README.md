# lab45 - Dockerized Web App

This repository contains a simple web application that is automatically built into a Docker image and pushed to Docker Hub on every commit to the `main` branch.

## 🔧 Technologies

- HTML + CSS (web page)  
- Docker  
- GitHub Actions (CI/CD)  
- Docker Hub  

---

## 🚀 CI/CD Pipeline

Automation is implemented using GitHub Actions.

### 🔄 What happens on every `push` to `main`:

1. The repository is cloned  
2. Login to Docker Hub happens  
3. The Docker image is built from the `Dockerfile`  
4. The image is pushed to Docker Hub (`yourusername/lab45:latest`)  
