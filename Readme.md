# SecurePay Online Payment Platform

## Overview

SecurePay is an advanced online payment platform designed to facilitate secure and efficient transactions. Leveraging cutting-edge machine learning algorithms for fraud detection, the platform scrutinizes each transaction for suspicious activity. This project consists of two main components: a frontend payment platform built with Streamlit and a backend fraud detection system developed using FastAPI.

## Project Structure

The project is organized into two main directories:

- `frontend/`: Contains the Streamlit application (`payment_platform.py`), Dockerfile, and requirements.
- `backend/`: Hosts the FastAPI application (`app.py`), Dockerfile, the machine learning model (`model.pkl`), and requirements.
- `notebooks`: Contains the modelling process.

A `docker-compose.yml` file at the root of the project directory orchestrates the deployment of both the frontend and backend services.

The modelling dataset was gotten from: https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Docker
- A good internet network

## Setup Instructions

### Clone the Repository

Start by cloning the repository to your local machine:

```sh
git clone https://github.com/AdeTeslim/AI-Based-Fraud-Detection-.git
cd AI-Based-Fraud-Detection-
```

### Build and Run with Docker Compose
To build and run the application using Docker Compose, execute the following command from the root of the project:

```sh
docker-compose up --build
```
This command builds the images for both the frontend and backend components and starts the containers. The --build flag ensures that Docker builds the images before starting the containers, which is useful for the first run or when changes are made to the Dockerfiles.

### Accessing the Application
Once the containers are up and running, you can access:

The frontend payment platform at    `http://localhost:8501`
The backend FastAPI application (with Swagger UI) at `http://localhost:8000/docs`


### Contributors
This project was developed by students from the Computer Science department of Babcock University as part of their final year project. The team members include:

- Momodu Teslim Oluwaseun (20/2564)
- Achugwo Stephanie Chidumebi (20/1464)
- Nelson Davidson Oremiloluwa (19/0852)
- Bailey Chidera Akinlolu (20/3244)
