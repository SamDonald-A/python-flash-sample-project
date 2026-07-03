# 🐳 Sample Mini Flask App - Docker Practice

This project is a simple Flask application created for practicing Docker fundamentals, including building images, running containers, and publishing images to Docker Hub.

---

## 📌 Prerequisites

Before you begin, make sure you have:

- Python 3.x
- Git
- Docker Desktop (Windows) or Docker Engine (Linux/Ubuntu)
- Docker Hub Account

---

## 📂 Clone the Repository

Fork this repository to your GitHub account and then clone it.

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

Navigate into the project directory.

```bash
cd <repository-name>
```

---

## ▶️ Run the Application Locally

Install the required packages.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python app.py
```

Open your browser and visit:

```
http://localhost:5000
```

---

## 🐳 Create a Dockerfile

Create a file named `Dockerfile` in the project root.

Example:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## 🔨 Build the Docker Image

```bash
docker build -t flask-app .
```

Verify the image.

```bash
docker images
```

---

## 🚀 Run the Docker Container

```bash
docker run -d -p 5000:5000 flask-app
```

Open your browser:

```
http://localhost:5000
```

---

## 🏷️ Tag the Image

Replace `<dockerhub-username>` with your Docker Hub username.

```bash
docker tag flask-app <dockerhub-username>/flask-app:v1
```

---

## ☁️ Push the Image to Docker Hub

Login first.

```bash
docker login
```

Push the image.

```bash
docker push <dockerhub-username>/flask-app:v1
```

---

## 📥 Pull the Image

```bash
docker pull <dockerhub-username>/flask-app:v1
```

---

## ▶️ Run the Pulled Image

```bash
docker run -d -p 5000:5000 <dockerhub-username>/flask-app:v1
```

---

## 📁 Project Structure

```
project/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 📚 Learning Objectives

By completing this exercise, you will learn:

- Clone a GitHub repository
- Run a Python Flask application
- Create a Dockerfile
- Build a Docker image
- Run a Docker container
- Tag Docker images
- Push images to Docker Hub
- Pull images from Docker Hub
- Deploy an application using Docker

---

## 📖 Useful Commands

```bash
docker images
docker ps
docker ps -a
docker stop <container_id>
docker rm <container_id>
docker rmi <image_name>
docker logs <container_id>
docker exec -it <container_id> bash
```

---

## 🎯 Assignment

Complete the following tasks:

- Fork the repository
- Clone it to your local machine
- Run the application locally
- Create a Dockerfile
- Build the Docker image
- Run the container
- Push the image to Docker Hub
- Pull the image on another machine
- Run the pulled image successfully

Happy Learning! 🚀
