🧾 Step-by-Step: Document Your API with Postman
1.Open Postman and Create a New Collection
Launch Postman

Click "Collections" → "New Collection"

Name it something like Library API or Django Backend

2.Add API Requests to the Collection
For each endpoint in your Django API (e.g., /api/books/, /api/register/, /api/login/):

Example: Add Book (POST)
Method: POST

URL: https://yourusername.pythonanywhere.com/api/books/

Headers

json
Authorization: Token your_token_here(like this 647be37deca15e190257dfcab4761818578a233e)
Body (raw JSON):

json
{

  "name": "The Alchemist",
  "author": "Paulo Coelho"
  
}
Repeat this for:

GET /api/books/

POST /api/register/

POST /api/login/


3.Test Each Request
Click Send to verify each request works

Save the request to your collection

