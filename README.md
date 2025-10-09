🧾 Step-by-Step: Document Your API with Postman
1. ✅ Open Postman and Create a New Collection
Launch Postman

Click "Collections" → "New Collection"

Name it something like Library API or Django Backend

2. 📌 Add API Requests to the Collection
For each endpoint in your Django API (e.g., /api/books/, /api/register/, /api/login/):

Example: Add Book (POST)
Method: POST

URL: https://yourusername.pythonanywhere.com/api/books/

Headers:

json
Content-Type: application/json
Authorization: Token your_token_here  // if using token auth
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

Any other custom endpoints

3. 🧪 Test Each Request
Click Send to verify each request works

Save the request to your collection

Add example responses and descriptions for clarity

4. 📤 Export the Collection
Click the three dots next to your collection → Export

Choose Collection v2.1 format

Save the .json file

5. 📚 Share or Submit the Documentation
You can submit the .json file as part of your project

Or share a public Postman link:

Click Share Collection → Get public link
