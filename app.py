from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Imports the Flask library.
# Creates a web application.
# Defines one endpoint (/).
# Returns "Hello from Docker!" when someone visits the website.
# Starts the web server on port 5000.

# Dockerfile
# FROM python:3.12

# WORKDIR /app

# COPY . .

# RUN pip install -r requirements.txt

# CMD ["python", "app.py"]