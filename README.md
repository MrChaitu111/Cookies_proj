🍪 Set Cookie (Expires in 5 Seconds)

A simple Django web application that demonstrates how to create, store, and automatically delete cookies after a short expiration time.
This project is perfect for beginners learning about cookies, HTTP headers, and session management in Django.


---

🚀 Features

Sets a cookie in the user’s browser that expires after 5 seconds.

Demonstrates Django’s built-in methods for handling cookies (HttpResponse.set_cookie()).

Shows how to read and delete cookies using Django views.

Great for understanding state management and temporary data storage in web applications.



---

⚙️ How It Works

1. When the user visits the page or clicks “Set Cookie”, Django sends a response with a cookie header.


2. The cookie is stored in the browser and will automatically expire after 5 seconds.


3. You can view it in Developer Tools → Application → Cookies.


4. Once expired, the browser deletes it automatically.

🧩 Tech Stack

Framework: Django 5.x

Language: Python 3.x

Frontend: HTML (optional)

Hosting: Render / Vercel / Railway



---

🧰 Setup Instructions

# 1️⃣ Clone the repository
git clone https://github.com/MrChaitu111
Cookies_proj/cookies-proj.git
cd cookies-proj

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run migrations (if needed)
python manage.py migrate

# 4️⃣ Start the server
python manage.py runserver


-----------------------------------------------
🍪 Set Cookie (Expires in 5 Seconds)

Full Django Example (Backend + Frontend)


---

🗂 Folder Structure

cookies-proj/
│
├── manage.py
├── cookiesproj/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── cookiesapp/
    ├── __init__.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   └── index.html
    └── static/
        └── style.css

Live Server :-
https://cookies-proj.onrender.com/

🌟 Author

Developed by: [Chaitanya]
GitHub: @Mr_Chaitu111





