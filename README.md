# Potato Disease Classification

This project classifies potato leaf images into different disease categories using deep learning.

---

## Project Description

The goal of this project is to build a machine learning model that can detect diseases in potato leaves based on images. It helps farmers or agricultural experts to identify the type of disease affecting the plant early on.

---

## Dataset

The dataset consists of images of potato leaves labeled with their corresponding disease category. The categories include:

- Early Blight
- Late Blight
- Healthy

---

## Setup and Installation

### Setup for Python

1. Install Python (if not already installed).  
   [Python Download & Installation Guide](https://www.python.org/downloads/)

2. Install required Python packages for training and API:

```bash
pip3 install -r training/requirements.txt
pip3 install -r api/requirements.txt

Setup for ReactJS Frontend
Install Node.js and npm:
Node.js Download & Installation

Navigate to the frontend folder and install dependencies:
cd frontend
npm install --from-lock-json
npm audit fix
Copy the example environment file and update API URL:

bash
Copy
Edit
cp .env.example .env
Update REACT_APP_API_URL in .env to point to your API server URL.
Running the API
Using FastAPI
Go inside the API folder:

bash
Copy
Edit
cd api
Run the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload --host 0.0.0.0
Your API will be running at http://0.0.0.0:8000.
