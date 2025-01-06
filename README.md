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
   env\Scripts\activate
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply database migrations:
   ```bash
   python manage.py migrate
5. Start the Django development server:
   ```bash
   python manage.py runserver


### **Usage**
Test the API Endpoints using Postman

1. User Registration
- Endpoint: http://127.0.0.1:8000/api/register/
- Method: POST
- Input:
   ```json
   {
       "username": "your_username",
       "password": "your_password"
   }
- Output:
   - Output:
      ```json
      {
          "message": "User registered successfully"
      }

2. User Login
- Endpoint: http://127.0.0.1:8000/api/login/
- Method: POST
- Body: json
   - Input:
      ```json
      {
          "username": "your_username",
          "password": "your_password"
      }
   - Output:
      ```json
      {
          "refresh": "<refresh_token>",
          "access": "<access_token>",
          "user": {
              "id": 4,
              "username": "your_username",
              "email": "",
              "tokens": 3900
          }
      }
3. Chat with AI
- Endpoint: http://127.0.0.1:8000/api/chat/
- Method: POST
- Headers:
   - Key: Authorization
   - Value: Bearer <access_token> #copy the aceess token from user login
- Body: json
   - Input: 
      ```json
      {
          "message": "Hello AI"
      }
   - Output:
      ```json
      {
          "id": 8,
          "user": 4,
          "message": "Hello AI",
          "response": "This is a dummy AI response.",
          "timestamp": "2025-01-06T15:14:43.872619Z"
      }
      
4. Token Balance
- Endpoint: http://127.0.0.1:8000/api/tokens/
- Method: GET
- Headers:
   - Key: Authorization
   - Value: Bearer <access_token> #copy the aceess token from user login
- Output:
   ```json
   {
       "tokens": 3900
   }




### **Challenges Encountered**

- During testing, tokens expired quickly especially when testing the `Chat` and `Token Balance` APIs. So, the `ACCESS_TOKEN_LIFETIME` in the settings was adjusted to 1 hour to provide a more convenient testing environment.
- While testing in Postman, it was unclear how to properly pass the `Authorization` header with the Bearer token. Misconfigurations led to 401 Unauthorized errors.

- The token deduction logic was difficult to test initially and ensure that the `User` model's `tokens` field was updated and saved after every token deduction. Added tests to verify this behavior.
 
- The Chat API needed to provide AI-generated responses, but integrating with a real AI model was out of scope for this assignment.
