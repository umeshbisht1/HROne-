E-commerce Backend API (FastAPI + MongoDB)
This project is a simple backend application built using FastAPI and MongoDB Atlas, designed for an e-commerce platform similar to Flipkart/Amazon.

🚀 Features
✅ Create Product API (POST /products)

✅ List Products API (GET /products)

✅ Create Order API (POST /orders)

✅ List Orders by User API (GET /orders/{user_id})

🛠 Tech Stack
FastAPI (Python 3.10+)

MongoDB Atlas

PyMongo

Uvicorn

📁 Project Structure
bash
Copy
Edit
.
├── main.py            # FastAPI app with all routes
├── models.py          # Pydantic models (schemas)
├── database.py        # MongoDB connection setup
├── requirements.txt   # Dependencies
├── .env               # MongoDB URI (not committed)
└── README.md          # Project documentation
