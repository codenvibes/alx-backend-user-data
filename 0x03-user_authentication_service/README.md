<h1 align="center"><b>0X03. USER AUTHENTICATION SERVICE</b></h1>
<div align="center"><code>Back-end</code> <code>Authentification</code></div>

<!--==================================================-->
<br><div align="center"><img src="https://github.com/codenvibes/alx-backend-user-data/blob/master/0x03-user_authentication_service/images/4cb3c8c607afc1d1582d.jpg"></div><br>

<p>In the industry, you should <strong>not</strong> implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="https://intranet.alxswe.com/rltoken/9nVfotMI_1zpEzihMzBeTA" title="Flask-User" target="_blank">Flask-User</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>


<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Resources
<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/lKExyvivrrW4eh0eI8UV6A">Flask documentation</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/py7LuuD1u2MUwcaf8wnDzQ">Requests module</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/cj-mc5ZHp_KyXn1yikHC0A">HTTP status codes</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!--==================================================-->
<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a>How to declare API routes in a Flask app</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to get and set cookies</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to retrieve request form data</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to return various HTTP status codes</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<br>

<!--==================================================-->
<br>

## Requirements
- Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly <code>#!/usr/bin/env python3</code>
- A <code>README.md</code> file, at the root of the folder of the project, is mandatory
- Your code should use the <code>pycodestyle</code> style (version 2.5)
- You should use <code>SQLAlchemy</code> 1.3.x
- All your files must be executable
- The length of your files will be tested using <code>wc</code>
- All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)
- All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)
- All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions should be type annotated
- The flask app should only interact with <code>Auth</code> and never with <code>DB</code> directly.
- Only public methods of <code>Auth</code> and <code>DB</code> should be used outside these classes

<!--==================================================-->
<br>

## Setup
You will need to install <code>bcrypt</code>

<pre><code>pip3 install bcrypt
</code></pre>


<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. User model
`mandatory`

File: [user.py]()
</summary>

<p>In this task you will create a SQLAlchemy model named <code>User</code> for a database table named <code>users</code> (by using the <a href="https://intranet.alxswe.com/rltoken/-a69l-rGqoFdXnnu6qfKdA" target="_blank" title="mapping declaration">mapping declaration</a> of SQLAlchemy). </p>

<p>The model will have the following attributes:</p>

<ul>
<li><code>id</code>, the integer primary key</li>
<li><code>email</code>, a non-nullable string</li>
<li><code>hashed_password</code>, a non-nullable string</li>
<li><code>session_id</code>, a nullable string</li>
<li><code>reset_token</code>, a nullable string</li>
</ul>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))

bob@dylan:~$ python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
bob@dylan:~$ 
</code></pre>


</details>

<details>
<summary>

### 1. create user
`mandatory`

File: [db.py]()
</summary>

<p>In this task, you will complete the <code>DB</code> class provided below to implement the <code>add_user</code> method.</p>

<pre><code class="python">"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -&gt; None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -&gt; Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
</code></pre>

<p>Note that <code>DB._session</code> is a private property and hence should NEVER be used from outside the <code>DB</code> class.</p>

<p>Implement the <code>add_user</code> method, which has two required string arguments: <code>email</code> and <code>hashed_password</code>, and returns a <code>User</code> object. The method should save the user to the database. No validations are required at this stage.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)

bob@dylan:~$ python3 main.py
1
2
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 2. Find user
`mandatory`

File: [db.py]()
</summary>

<p>In this task you will implement the <code>DB.find_user_by</code> method. This method takes in arbitrary keyword arguments and returns the first row found in the <code>users</code> table as filtered by the method’s input arguments. No validation of input arguments required at this point.</p>

<p>Make sure that SQLAlchemy’s <code>NoResultFound</code> and <code>InvalidRequestError</code> are raised when no results are found, or when wrong query arguments are passed, respectively.</p>

<p><strong>Warning:</strong></p>

<ul>
<li> <code>NoResultFound</code> has been moved from <code>sqlalchemy.orm.exc</code> to <code>sqlalchemy.exc</code> between the version 1.3.x and 1.4.x of SQLAchemy - please make sure you are importing it from <code>sqlalchemy.orm.exc</code></li>
</ul>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

find_user = my_db.find_user_by(email="test@test.com")
print(find_user.id)

try:
    find_user = my_db.find_user_by(email="test2@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")        

bob@dylan:~$ python3 main.py
1
1
Not found
Invalid
bob@dylan:~$ 
</code></pre>


</details>

<details>
<summary>

### 3. update user
`mandatory`

File: [db.py]()
</summary>

<p>In this task, you will implement the <code>DB.update_user</code> method that takes as argument a required <code>user_id</code> integer and arbitrary keyword arguments, and returns <code>None</code>.</p>

<p>The method will use <code>find_user_by</code> to locate the user to update, then will update the user’s attributes as passed in the method’s arguments then commit changes to the database.</p>

<p>If an argument that does not correspond to a user attribute is passed, raise a <code>ValueError</code>.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

email = 'test@test.com'
hashed_password = "hashedPwd"

user = my_db.add_user(email, hashed_password)
print(user.id)

try:
    my_db.update_user(user.id, hashed_password='NewPwd')
    print("Password updated")
except ValueError:
    print("Error")

bob@dylan:~$ python3 main.py
1
Password updated
bob@dylan:~$ 
</code></pre>


</details>

<details>
<summary>

### 4. Hash password
`mandatory`

File: [auth.py]()
</summary>

<p>In this task you will define a <code>_hash_password</code> method that takes in a <code>password</code> string arguments and returns bytes.</p>

<p>The returned bytes is a salted hash of the input password, hashed with <code>bcrypt.hashpw</code>.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from auth import _hash_password

print(_hash_password("Hello Holberton"))

bob@dylan:~$ python3 main.py
b'$2b$12$eUDdeuBtrD41c8dXvzh95ehsWYCCAi4VH1JbESzgbgZT.eMMzi.G2'
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 5. Register user
`mandatory`

File: [auth.py]()
</summary>

<p>In this task, you will implement the <code>Auth.register_user</code> in the <code>Auth</code> class provided below:</p>

<pre><code class="python">from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
</code></pre>

<p>Note that <code>Auth._db</code> is a private property and should NEVER be used from outside the class.</p>

<p><code>Auth.register_user</code> should take mandatory <code>email</code> and <code>password</code> string arguments and return a <code>User</code> object.</p>

<p>If a user already exist with the passed email, raise a <code>ValueError</code> with the message <code>User &lt;user's email&gt; already exists</code>.</p>

<p>If not, hash the password with <code>_hash_password</code>, save the user to the database using <code>self._db</code> and return the <code>User</code> object.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))        

bob@dylan:~$ python3 main.py
successfully created a new user!
could not create a new user: User me@me.com already exists
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 6. Basic Flask app
`mandatory`

File: [app.py]()
</summary>

<p>In this task, you will set up a basic Flask app.</p>

<p>Create a Flask app that has a single <code>GET</code> route (<code>"/"</code>) and use <code>flask.jsonify</code> to return a JSON payload of the form:</p>

<pre><code class="json">{"message": "Bienvenue"}
</code></pre>

<p>Add the following code at the end of the module:</p>

<pre><code>if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
</code></pre>


</details>

<details>
<summary>

### 7. Register user
`mandatory`

File: [app.py]()
</summary>

<p>In this task, you will implement the end-point to register a user. Define a <code>users</code> function that implements the <code>POST /users</code> route.</p>

<p>Import the <code>Auth</code> object and instantiate it at the root of the module as such:</p>

<pre><code class="python">from auth import Auth


AUTH = Auth()
</code></pre>

<p>The end-point should expect two form data fields: <code>"email"</code> and <code>"password"</code>. If the user does not exist, the end-point should register it and respond with the following JSON payload:</p>

<pre><code class="json">{"email": "&lt;registered email&gt;", "message": "user created"}
</code></pre>

<p>If the user is already registered, catch the exception and return a JSON payload of the form</p>

<pre><code class="json">{"message": "email already registered"}
</code></pre>

<p>and return a 400 status code</p>

<p>Remember that you should only use <code>AUTH</code> in this app. <code>DB</code> is a lower abstraction that is proxied by <code>Auth</code>.</p>

<p><em>Terminal 1:</em></p>

<pre><code>bob@dylan:~$ python3 app.py 
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

</code></pre>

<p>Terminal 2:</p>

<pre><code>bob@dylan:~$ curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
&gt; POST /users HTTP/1.1
&gt; Host: localhost:5000
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; Content-Length: 40
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 40 out of 40 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Content-Length: 52
&lt; Server: Werkzeug/1.0.1 Python/3.7.3
&lt; Date: Wed, 19 Aug 2020 00:03:18 GMT
&lt; 
{"email":"bob@me.com","message":"user created"}

bob@dylan:~$
bob@dylan:~$ curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
&gt; POST /users HTTP/1.1
&gt; Host: localhost:5000
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; Content-Length: 40
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 40 out of 40 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 400 BAD REQUEST
&lt; Content-Type: application/json
&lt; Content-Length: 39
&lt; Server: Werkzeug/1.0.1 Python/3.7.3
&lt; Date: Wed, 19 Aug 2020 00:03:33 GMT
&lt; 
{"message":"email already registered"}
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 8. Credentials validation
`mandatory`

File: [auth.py]()
</summary>

<p>In this task, you will implement the <code>Auth.valid_login</code> method. It should expect <code>email</code> and <code>password</code> required arguments and return a boolean.</p>

<p>Try locating the user by email. If it exists, check the password with <code>bcrypt.checkpw</code>. If it matches return <code>True</code>. In any other case, return <code>False</code>.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.valid_login(email, password))

print(auth.valid_login(email, "WrongPwd"))

print(auth.valid_login("unknown@email", password))

bob@dylan:~$ python3 main.py
True
False
False
bob@dylan:~$ 
</code></pre>


</details>

<details>
<summary>

### 9. Generate UUIDs
`mandatory`

File: [auth.py]()
</summary>

<p>In this task you will implement a <code>_generate_uuid</code> function in the <code>auth</code> module. The function should return a string representation of a new UUID. Use the <code>uuid</code> module.</p>

<p>Note that the method is private to the <code>auth</code> module and should <strong>NOT</strong> be used outside of it.</p>


</details>

<details>
<summary>

### 10. Get session ID
`mandatory`

File: [auth.py]()
</summary>

<p>In this task, you will implement the <code>Auth.create_session</code> method. It takes an <code>email</code> string argument and returns the session ID as a string.</p>

<p>The method should find the user corresponding to the email, generate a new UUID and store it in the database as the user’s <code>session_id</code>, then return the session ID.</p>

<p>Remember that only public methods of <code>self._db</code> can be used.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.create_session(email))
print(auth.create_session("unknown@email.com"))

bob@dylan:~$ python3 main.py
5a006849-343e-4a48-ba4e-bbd523fcca58
None
bob@dylan:~$ 
</code></pre>


</details>

<details>
<summary>

### 11. Log in
`mandatory`

File: [app.py]()
</summary>

<p>In this task, you will implement a <code>login</code> function to respond to the <code>POST /sessions</code> route.</p>

<p>The request is expected to contain form data with <code>"email"</code> and a <code>"password"</code> fields.</p>

<p>If the login information is incorrect, use <code>flask.abort</code> to respond with a 401 HTTP status.</p>

<p>Otherwise, create a new session for the user, store it the session ID as a cookie with key <code>"session_id"</code> on the response and return a JSON payload of the form</p>

<pre><code class="json">{"email": "&lt;user email&gt;", "message": "logged in"}
</code></pre>

<pre><code>bob@dylan:~$ curl -XPOST localhost:5000/users -d 'email=bob@bob.com' -d 'password=mySuperPwd'
{"email":"bob@bob.com","message":"user created"}
bob@dylan:~$ 
bob@dylan:~$  curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
&gt; POST /sessions HTTP/1.1
&gt; Host: localhost:5000
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; Content-Length: 37
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 37 out of 37 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Content-Length: 46
&lt; Set-Cookie: session_id=163fe508-19a2-48ed-a7c8-d9c6e56fabd1; Path=/
&lt; Server: Werkzeug/1.0.1 Python/3.7.3
&lt; Date: Wed, 19 Aug 2020 00:12:34 GMT
&lt; 
{"email":"bob@bob.com","message":"logged in"}
* Closing connection 0
bob@dylan:~$ 
bob@dylan:~$ curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=BlaBla' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
&gt; POST /sessions HTTP/1.1
&gt; Host: localhost:5000
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; Content-Length: 34
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 34 out of 34 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 401 UNAUTHORIZED
&lt; Content-Type: text/html; charset=utf-8
&lt; Content-Length: 338
&lt; Server: Werkzeug/1.0.1 Python/3.7.3
&lt; Date: Wed, 19 Aug 2020 00:12:45 GMT
&lt; 
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;401 Unauthorized&lt;/title&gt;
&lt;h1&gt;Unauthorized&lt;/h1&gt;
&lt;p&gt;The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required.&lt;/p&gt;
* Closing connection 0
bob@dylan:~$ 
</code></pre>


</details>

<details>
<summary>

### 12. Find user by session ID
`mandatory`

File: [auth.py]()
</summary>

<p>In this task, you will implement the <code>Auth.get_user_from_session_id</code> method. It takes a single <code>session_id</code> string argument and returns the corresponding <code>User</code> or <code>None</code>.</p>

<p>If the session ID is <code>None</code> or no user is found, return <code>None</code>. Otherwise return the corresponding user.</p>

<p>Remember to only use public methods of <code>self._db</code>.</p>


</details>

<details>
<summary>

### 13. Destroy session
`mandatory`

File: [auth.py]()
</summary>

<p>In this task, you will implement <code>Auth.destroy_session</code>. The method takes a single <code>user_id</code> integer argument and returns <code>None</code>.</p>

<p>The method updates the corresponding user’s session ID to <code>None</code>.</p>

<p>Remember to only use public methods of <code>self._db</code>.</p>


</details>

<details>
<summary>

### 14. Log out
`mandatory`

File: [app.py]()
</summary>

<p>In this task, you will implement a <code>logout</code> function to respond to the <code>DELETE /sessions</code> route.</p>

<p>The request is expected to contain the session ID as a cookie with key <code>"session_id"</code>.</p>

<p>Find the user with the requested session ID. If the user exists destroy the session and redirect the user to <code>GET /</code>. If the user does not exist, respond with a 403 HTTP status.</p>


</details>

<details>
<summary>

### 15. User profile
`mandatory`

File: [app.py]()
</summary>

<p>In this task, you will implement a <code>profile</code> function to respond to the <code>GET /profile</code> route.</p>

<p>The request is expected to contain a <code>session_id</code> cookie. Use it to find the user. If the user exist, respond with a 200 HTTP status and the following JSON payload:</p>

<pre><code class="json">{"email": "&lt;user email&gt;"}
</code></pre>

<p>If the session ID is invalid or the user does not exist, respond with a 403 HTTP status.</p>

<pre><code>bob@dylan:~$ curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
&gt; POST /sessions HTTP/1.1
&gt; Host: localhost:5000
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; Content-Length: 37
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 37 out of 37 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Content-Length: 46
&lt; Set-Cookie: session_id=75c89af8-1729-44d9-a592-41b5e59de9a1; Path=/
&lt; Server: Werkzeug/1.0.1 Python/3.7.3
&lt; Date: Wed, 19 Aug 2020 00:15:57 GMT
&lt; 
{"email":"bob@bob.com","message":"logged in"}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl -XGET localhost:5000/profile -b "session_id=75c89af8-1729-44d9-a592-41b5e59de9a1"
{"email": "bob@bob.com"}
bob@dylan:~$ 
bob@dylan:~$ curl -XGET localhost:5000/profile -b "session_id=nope" -v
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
&gt; GET /profile HTTP/1.1
&gt; Host: localhost:5000
&gt; User-Agent: curl/7.58.0
&gt; Accept: */*
&gt; Cookie: session_id=75c89af8-1729-44d9-a592-41b5e59de9a
&gt; 
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 403 FORBIDDEN
&lt; Content-Type: text/html; charset=utf-8
&lt; Content-Length: 234
&lt; Server: Werkzeug/1.0.1 Python/3.7.3
&lt; Date: Wed, 19 Aug 2020 00:16:43 GMT
&lt; 
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;403 Forbidden&lt;/title&gt;
&lt;h1&gt;Forbidden&lt;/h1&gt;
&lt;p&gt;You don't have the permission to access the requested resource. It is either read-protected or not readable by the server.&lt;/p&gt;
* Closing connection 0

bob@dylan:~$ 
</code></pre>


</details>

<details>
<summary>

### 16. Generate reset password token
`mandatory`

File: [auth.py]()
</summary>

<p>In this task, you will implement the <code>Auth.get_reset_password_token</code> method. It take an <code>email</code> string argument and returns a string.</p>

<p>Find the user corresponding to the email. If the user does not exist, raise a <code>ValueError</code> exception. If it exists, generate a UUID and update the user’s <code>reset_token</code> database field. Return the token.</p>


</details>

<details>
<summary>

### 17. Get reset password token
`mandatory`

File: [app.py]()
</summary>

<p>In this task, you will implement a <code>get_reset_password_token</code> function to respond to the <code>POST /reset_password</code> route.</p>

<p>The request is expected to contain form data with the <code>"email"</code> field.</p>

<p>If the email is not registered, respond with a 403 status code. Otherwise, generate a token and respond with a 200 HTTP status and the following JSON payload:</p>

<pre><code class="json">{"email": "&lt;user email&gt;", "reset_token": "&lt;reset token&gt;"}
</code></pre>


</details>

<details>
<summary>

### 18. Update password
`mandatory`

File: [auth.py]()
</summary>

<p>In this task, you will implement the <code>Auth.update_password</code> method. It takes <code>reset_token</code> string argument and a <code>password</code> string argument and returns <code>None</code>.</p>

<p>Use the <code>reset_token</code> to find the corresponding user. If it does not exist, raise a <code>ValueError</code> exception.</p>

<p>Otherwise, hash the password and update the user’s <code>hashed_password</code> field with the new hashed password and the <code>reset_token</code> field to <code>None</code>.</p>


</details>

<details>
<summary>

### 19. Update password end-point
`mandatory`

File: [app.py]()
</summary>

<p>In this task you will implement the <code>update_password</code> function in the <code>app</code> module to respond to the <code>PUT /reset_password</code> route.</p>

<p>The request is expected to contain form data with fields <code>"email"</code>, <code>"reset_token"</code> and <code>"new_password"</code>.</p>

<p>Update the password. If the token is invalid, catch the exception and respond with a 403 HTTP code.</p>

<p>If the token is valid, respond with a 200 HTTP code and the following JSON payload:</p>

<pre><code class="json">{"email": "&lt;user email&gt;", "message": "Password updated"}
</code></pre>


</details>

<details>
<summary>

### 20. End-to-end integration test
`#advanced`

File: [main.py]()
</summary>

<p>Start your app. Open a new terminal window.</p>

<p>Create a new module called <code>main.py</code>. Create one function for each of the following tasks. Use the <code>requests</code> module to query your web server for the corresponding end-point. Use <code>assert</code> to validate the response’s expected status code and payload (if any) for each task.</p>

<ul>
<li><code>register_user(email: str, password: str) -&gt; None</code></li>
<li><code>log_in_wrong_password(email: str, password: str) -&gt; None</code></li>
<li><code>log_in(email: str, password: str) -&gt; str</code></li>
<li><code>profile_unlogged() -&gt; None</code></li>
<li><code>profile_logged(session_id: str) -&gt; None</code></li>
<li><code>log_out(session_id: str) -&gt; None</code></li>
<li><code>reset_password_token(email: str) -&gt; str</code></li>
<li><code>update_password(email: str, reset_token: str, new_password: str) -&gt; None</code></li>
</ul>

<p>Then copy the following code at the end of the <code>main</code> module:</p>

<pre><code class="python">EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
</code></pre>

<p>Run <code>python main.py</code>. If everything is correct, you should see no output.</p>


</details>

