#secure-web-app-test INSECURE

##NCI 2024 Bogdan Munteanu x21126097@student.ncirl.ie

Installation Instructions:




adduser.py -- will  add a user to the database 

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


## HOW TO EXPLOIT SQL INJECT? 


You can try to use the fallowing for login:
- **Username**: `' UNION SELECT 1, 'hacker', 'anything'; --`
- **Password**: (leave it empty)

The query becomes:

`SELECT * FROM users WHERE username = '' UNION SELECT 1, 'hacker', 'anything'; --' AND password = ''`

This query can be used to check if the database allows **UNION SELECT** statements, which can be used to extract information from other parts of the database, depending on the privileges.

It will display login succefuly :) 



## HOW TO EXPLOIT XSS?

- Go to `http://127.0.0.1:5000/comment_insecure`.
- In the "Comment" field, enter the following JavaScript payload:
    
    html
    
    Copy code
    
    `<script>alert('XSS Attack');</script>`
    
- Click "Submit".

**Expected Outcome**: You should see an alert message pop up with `'XSS Attack'`. This happens because the input is directly reflected back into the response, leading to JavaScript execution in the user's browser.


