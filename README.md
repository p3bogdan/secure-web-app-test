# secure-web-app-test
Installation Instructions:
# NCI 2024 Bogdan Munteanu x21126097@student.ncirl.ie
# Below is an example of a simple Flask web application in Python with SQLite3 as the database.
# The purpose is to demonstrate insecure coding practices.
# Why Python and Flask? Because is fast! 




## Installation
1. Clone the repository:
git clone https://github.com/your-username/secure-web-app.git
2. Navigate to the directory:
cd secure-web-app
3. Install dependencies:

pip install Flask

Running the Application:

python3 app-secure.py

or 

python3 app-insecure.py


Instructions for starting the server:
## Running the Application
To start the Flask server, run:

python3 app-secure.py
OR 
python3 app-insecure.py

Accessing Different Pages:

http://127.0.0.1:5000/login_insecure - Insecure login (only in the insecure branch).

http://127.0.0.1:5000/login_secure - Secure login (only in the secure/main branches).

http://127.0.0.1:5000/comment_insecure - Insecure comment submission.

http://127.0.0.1:5000/comment_secure - Secure comment submission.
