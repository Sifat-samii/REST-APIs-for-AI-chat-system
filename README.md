# AI Chat System APIs

This repository contains a Django-based REST API for an AI-powered chat system. Users can register, log in, interact with a chatbot, and check their token balance. 

---

## **Features**

- User Registration: Create an account with a unique username and password.  
- User Login: Authenticate with a JWT token.  
- Chat with AI: Interact with a chatbot, which deducts tokens for each query.  
- Token Balance: Check the remaining tokens in the user account.  

---

## **Installation Instructions**

### **Prerequisites**
- Python 3.9+
- pip (Python package installer)
- SQLite (default database for Django)

### **Setup**

1. Clone this repository:
   ```bash
   git clone https://github.com/Sifat-samii/REST-APIs-for-AI-chat-system.git
   cd path/to/REST-APIs-for-AI-chat-system
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   venv\Scripts\activate
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply database migrations:
   ```bash
   python manage.py migrate
5. Start the Django development server:
   ```bash
   python manage.py runserver



