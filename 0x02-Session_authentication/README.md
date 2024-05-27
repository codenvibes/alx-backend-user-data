<h1 align="center"><b>0X02. SESSION AUTHENTICATION</b></h1>
<div align="center"><code>Back-end</code> <code>Authentification</code></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Background Context
In this project, you will implement a <strong>Session Authentication</strong>. You are not allowed to install any other module.

In the industry, you should <strong>not</strong> implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="https://intranet.alxswe.com/rltoken/_ZTQTaMKjx1S_xATshexkA" target="_blank" title="Flask-HTTPAuth">Flask-HTTPAuth</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.


<!--==================================================-->
<br>

## Resources
<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/oofk0VhuS0ZFZTNTVrQeaQ">REST API Authentication Mechanisms - Only the session auth part</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/peLV8xuJ4PDJMOVFqk-d2g">HTTP Cookie</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/AI1tFR5XriGfR8Tz7YTYQA">Flask</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/QYfI5oW6OHUmHDzwKV1Qsw">Flask Cookie</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!--==================================================-->
<br>

## Learning Objectives
<h3>General</h3>

<details>
<summary><b><a href=" "> </a>What authentication means</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What session authentication means</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What Cookies are</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to send Cookies</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to parse Cookies </b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!--==================================================-->
<br>

## Requirements
<h3>Python Scripts</h3>

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly <code>#!/usr/bin/env python3</code>
- A <code>README.md</code> file, at the root of the folder of the project, is mandatory
- Your code should use the <code>pycodestyle</code> style (version 2.5)
- All your files must be executable
- The length of your files will be tested using <code>wc</code>
- All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)
- All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)
- All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. Et moi et moi et moi!
`mandatory`

File: [api/v1/app.py](), [api/v1/views/users.py]()
</summary>

<p>Copy all your work of the <strong>0x06. Basic authentication</strong> project in this new folder.</p>

<p>In this version, you implemented a <strong>Basic authentication</strong> for giving you access to all User endpoints:</p>

<ul>
<li><code>GET /api/v1/users</code></li>
<li><code>POST /api/v1/users</code></li>
<li><code>GET /api/v1/users/&lt;user_id&gt;</code></li>
<li><code>PUT /api/v1/users/&lt;user_id&gt;</code></li>
<li><code>DELETE /api/v1/users/&lt;user_id&gt;</code></li>
</ul>

<p>Now, you will add a new endpoint: <code>GET /users/me</code> to retrieve the authenticated <code>User</code> object.</p>

<ul>
<li>Copy folders <code>models</code> and <code>api</code> from the previous project <code>0x06. Basic authentication</code></li>
<li>Please make sure all mandatory tasks of this previous project are done at 100% because this project (and the rest of this track) will be based on it.</li>
<li>Update <code>@app.before_request</code> in <code>api/v1/app.py</code>:

<ul>
<li>Assign the result of <code>auth.current_user(request)</code> to <code>request.current_user</code></li>
</ul></li>
<li>Update method for the route <code>GET /api/v1/users/&lt;user_id&gt;</code> in <code>api/v1/views/users.py</code>:

<ul>
<li>If <code>&lt;user_id&gt;</code> is equal to <code>me</code> and <code>request.current_user</code> is <code>None</code>: <code>abort(404)</code></li>
<li>If <code>&lt;user_id&gt;</code> is equal to <code>me</code> and <code>request.current_user</code> is not <code>None</code>: return the authenticated <code>User</code> in a JSON response (like a normal case of <code>GET /api/v1/users/&lt;user_id&gt;</code> where <code>&lt;user_id&gt;</code> is a valid <code>User</code> ID)</li>
<li>Otherwise, keep the same behavior</li>
</ul></li>
</ul>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ cat main_0.py
#!/usr/bin/env python3
""" Main 0
"""
import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
user_email = "bob@hbtn.io"
user_clear_pwd = "H0lbertonSchool98!"

user = User()
user.email = user_email
user.password = user_clear_pwd
print("New user: {}".format(user.id))
user.save()

basic_clear = "{}:{}".format(user_email, user_clear_pwd)
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth ./main_0.py 
New user: 9375973a-68c7-46aa-b135-29f79e837495
Basic Base64: Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
[
  {
    "created_at": "2017-09-25 01:55:17", 
    "email": "bob@hbtn.io", 
    "first_name": null, 
    "id": "9375973a-68c7-46aa-b135-29f79e837495", 
    "last_name": null, 
    "updated_at": "2017-09-25 01:55:17"
  }
]
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{
  "created_at": "2017-09-25 01:55:17", 
  "email": "bob@hbtn.io", 
  "first_name": null, 
  "id": "9375973a-68c7-46aa-b135-29f79e837495", 
  "last_name": null, 
  "updated_at": "2017-09-25 01:55:17"
}
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 1. Empty session
`mandatory`

File: [api/v1/auth/session_auth.py](), [api/v1/app.py]()
</summary>

<p>Create a class <code>SessionAuth</code> that inherits from <code>Auth</code>. For the moment this class will be empty. It’s the first step for creating a new authentication mechanism:</p>

<ul>
<li>validate if everything inherits correctly without any overloading</li>
<li>validate the “switch” by using environment variables</li>
</ul>

<p>Update <code>api/v1/app.py</code> for using <code>SessionAuth</code> instance for the variable <code>auth</code> depending of the value of the environment variable <code>AUTH_TYPE</code>, If <code>AUTH_TYPE</code> is equal to <code>session_auth</code>:</p>

<ul>
<li>import <code>SessionAuth</code> from <code>api.v1.auth.session_auth</code></li>
<li>create an instance of <code>SessionAuth</code> and assign it to the variable <code>auth</code></li>
</ul>

<p>Otherwise, keep the previous mechanism.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status/"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{
  "error": "Forbidden"
}
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 2. Create a session
`mandatory`

File: [api/v1/auth/session_auth.py]()
</summary>

<p>Update <code>SessionAuth</code> class:</p>

<ul>
<li>Create a class attribute <code>user_id_by_session_id</code> initialized by an empty dictionary</li>
<li>Create an instance method <code>def create_session(self, user_id: str = None) -&gt; str:</code> that creates a Session ID for a <code>user_id</code>:

<ul>
<li>Return <code>None</code> if <code>user_id</code> is <code>None</code></li>
<li>Return <code>None</code> if <code>user_id</code> is not a string</li>
<li>Otherwise:

<ul>
<li>Generate a Session ID using <code>uuid</code> module and <code>uuid4()</code> like <code>id</code> in <code>Base</code></li>
<li>Use this Session ID as key of the dictionary <code>user_id_by_session_id</code> - the value for this key must be <code>user_id</code></li>
<li>Return the Session ID</li>
</ul></li>
<li>The same <code>user_id</code> can have multiple Session ID - indeed, the <code>user_id</code> is the value in the dictionary <code>user_id_by_session_id</code></li>
</ul></li>
</ul>

<p>Now you an “in-memory” Session ID storing. You will be able to retrieve an <code>User</code> id based on a Session ID.</p>

<pre><code>bob@dylan:~$ cat  main_1.py 
#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

print("{}: {}".format(type(sa.user_id_by_session_id), sa.user_id_by_session_id))

user_id = None
session = sa.create_session(user_id)
print("{} =&gt; {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = 89
session = sa.create_session(user_id)
print("{} =&gt; {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "abcde"
session = sa.create_session(user_id)
print("{} =&gt; {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "fghij"
session = sa.create_session(user_id)
print("{} =&gt; {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "abcde"
session = sa.create_session(user_id)
print("{} =&gt; {}: {}".format(user_id, session, sa.user_id_by_session_id))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_1.py 
&lt;class 'dict'&gt;: {}
None =&gt; None: {}
89 =&gt; None: {}
abcde =&gt; 61997a1b-3f8a-4b0f-87f6-19d5cafee63f: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde'}
fghij =&gt; 69e45c25-ec89-4563-86ab-bc192dcc3b4f: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde', '69e45c25-ec89-4563-86ab-bc192dcc3b4f': 'fghij'}
abcde =&gt; 02079cb4-6847-48aa-924e-0514d82a43f4: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde', '02079cb4-6847-48aa-924e-0514d82a43f4': 'abcde', '69e45c25-ec89-4563-86ab-bc192dcc3b4f': 'fghij'}
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 3. User ID for Session ID
`mandatory`

File: [api/v1/auth/session_auth.py]()
</summary>

<p>Update <code>SessionAuth</code> class:</p>

<p>Create an instance method <code>def user_id_for_session_id(self, session_id: str = None) -&gt; str:</code> that returns a <code>User</code> ID based on a Session ID:</p>

<ul>
<li>Return <code>None</code> if <code>session_id</code> is <code>None</code></li>
<li>Return <code>None</code> if <code>session_id</code> is not a string</li>
<li>Return the value (the User ID) for the key <code>session_id</code> in the dictionary <code>user_id_by_session_id</code>.</li>
<li>You must use <code>.get()</code> built-in for accessing in a dictionary a value based on key</li>
</ul>

<p>Now you have 2 methods (<code>create_session</code> and <code>user_id_for_session_id</code>) for storing and retrieving a link between a <code>User</code> ID and a Session ID.</p>

<pre><code>bob@dylan:~$ cat main_2.py 
#!/usr/bin/env python3
""" Main 2
"""
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

user_id_1 = "abcde"
session_1 = sa.create_session(user_id_1)
print("{} =&gt; {}: {}".format(user_id_1, session_1, sa.user_id_by_session_id))

user_id_2 = "fghij"
session_2 = sa.create_session(user_id_2)
print("{} =&gt; {}: {}".format(user_id_2, session_2, sa.user_id_by_session_id))

print("---")

tmp_session_id = None
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} =&gt; {}".format(tmp_session_id, tmp_user_id))

tmp_session_id = 89
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} =&gt; {}".format(tmp_session_id, tmp_user_id))

tmp_session_id = "doesntexist"
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} =&gt; {}".format(tmp_session_id, tmp_user_id))

print("---")

tmp_session_id = session_1
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} =&gt; {}".format(tmp_session_id, tmp_user_id))

tmp_session_id = session_2
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} =&gt; {}".format(tmp_session_id, tmp_user_id))

print("---")

session_1_bis = sa.create_session(user_id_1)
print("{} =&gt; {}: {}".format(user_id_1, session_1_bis, sa.user_id_by_session_id))

tmp_user_id = sa.user_id_for_session_id(session_1_bis)
print("{} =&gt; {}".format(session_1_bis, tmp_user_id))

tmp_user_id = sa.user_id_for_session_id(session_1)
print("{} =&gt; {}".format(session_1, tmp_user_id))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_2.py 
abcde =&gt; 8647f981-f503-4638-af23-7bb4a9e4b53f: {'8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde'}
fghij =&gt; a159ee3f-214e-4e91-9546-ca3ce873e975: {'a159ee3f-214e-4e91-9546-ca3ce873e975': 'fghij', '8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde'}
---
None =&gt; None
89 =&gt; None
doesntexist =&gt; None
---
8647f981-f503-4638-af23-7bb4a9e4b53f =&gt; abcde
a159ee3f-214e-4e91-9546-ca3ce873e975 =&gt; fghij
---
abcde =&gt; 5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee: {'a159ee3f-214e-4e91-9546-ca3ce873e975': 'fghij', '8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde', '5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee': 'abcde'}
5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee =&gt; abcde
8647f981-f503-4638-af23-7bb4a9e4b53f =&gt; abcde
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 4. Session cookie
`mandatory`

File: [api/v1/auth/auth.py]()
</summary>

<p>Update <code>api/v1/auth/auth.py</code> by adding the method <code>def session_cookie(self, request=None):</code> that returns a cookie value from a request:</p>

<ul>
<li>Return <code>None</code> if <code>request</code> is <code>None</code></li>
<li>Return the value of the cookie named <code>_my_session_id</code> from <code>request</code> - the name of the cookie must be defined by the environment variable <code>SESSION_NAME</code></li>
<li>You must use <code>.get()</code> built-in for accessing the cookie in the request cookies dictionary</li>
<li>You must use the environment variable <code>SESSION_NAME</code> to define the name of the cookie used for the Session ID</li>
</ul>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ cat main_3.py
#!/usr/bin/env python3
""" Cookie server
"""
from flask import Flask, request
from api.v1.auth.auth import Auth

auth = Auth()

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    return "Cookie value: {}\n".format(auth.session_cookie(request))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_3.py 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl "http://0.0.0.0:5000"
Cookie value: None
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000" --cookie "_my_session_id=Hello"
Cookie value: Hello
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000" --cookie "_my_session_id=C is fun"
Cookie value: C is fun
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000" --cookie "_my_session_id_fake"
Cookie value: None
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 5. Before request
`mandatory`

File: [api/v1/app.py]()
</summary>

<p>Update the <code>@app.before_request</code> method in <code>api/v1/app.py</code>:</p>

<ul>
<li>Add the URL path <code>/api/v1/auth_session/login/</code> in the list of excluded paths of the method <code>require_auth</code> - this route doesn’t exist yet but it should be accessible outside authentication</li>
<li>If <code>auth.authorization_header(request)</code> and <code>auth.session_cookie(request)</code> return <code>None</code>, <code>abort(401)</code></li>
</ul>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" # not found but not "blocked" by an authentication system
{
  "error": "Not found"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me"
{
  "error": "Unauthorized"
}
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh" # Won't work because the environment variable AUTH_TYPE is equal to "session_auth"
{
  "error": "Forbidden"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=5535d4d7-3d77-4d06-8281-495dc3acfe76" # Won't work because no user is linked to this Session ID
{
  "error": "Forbidden"
}
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 6. Use Session ID for identifying a User
`mandatory`

File: [api/v1/auth/session_auth.py]()
</summary>

<p>Update <code>SessionAuth</code> class:</p>

<p>Create an instance method <code>def current_user(self, request=None):</code> (overload) that returns a <code>User</code> instance based on a cookie value:</p>

<ul>
<li>You must use <code>self.session_cookie(...)</code> and <code>self.user_id_for_session_id(...)</code> to return the User ID based on the cookie <code>_my_session_id</code></li>
<li>By using this User ID, you will be able to retrieve a <code>User</code> instance from the database - you can use <code>User.get(...)</code> for retrieving a <code>User</code> from the database.</li>
</ul>

<p>Now, you will be able to get a User based on his session ID.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ cat main_4.py
#!/usr/bin/env python3
""" Main 4
"""
from flask import Flask, request
from api.v1.auth.session_auth import SessionAuth
from models.user import User

""" Create a user test """
user_email = "bobsession@hbtn.io"
user_clear_pwd = "fake pwd"

user = User()
user.email = user_email
user.password = user_clear_pwd
user.save()

""" Create a session ID """
sa = SessionAuth()
session_id = sa.create_session(user.id)
print("User with ID: {} has a Session ID: {}".format(user.id, session_id))

""" Create a Flask app """
app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    request_user = sa.current_user(request)
    if request_user is None:
        return "No user found\n"
    return "User found: {}\n".format(request_user.id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_4.py
User with ID: cf3ddee1-ff24-49e4-a40b-2540333fe992 has a Session ID: 9d1648aa-da79-4692-8236-5f9d7f9e9485
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl "http://0.0.0.0:5000/"
No user found
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/" --cookie "_my_session_id=Holberton"
No user found
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/" --cookie "_my_session_id=9d1648aa-da79-4692-8236-5f9d7f9e9485"
User found: cf3ddee1-ff24-49e4-a40b-2540333fe992
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 7. New view for Session Authentication
`mandatory`

File: [api/v1/views/session_auth.py](), [api/v1/views/__init__.py]()
</summary>

<p>Create a new Flask view that handles all routes for the Session authentication.</p>

<p>In the file <code>api/v1/views/session_auth.py</code>, create a route <code>POST /auth_session/login</code> (= <code>POST /api/v1/auth_session/login</code>):</p>

<ul>
<li>Slash tolerant (<code>/auth_session/login</code> == <code>/auth_session/login/</code>)</li>
<li>You must use <code>request.form.get()</code> to retrieve <code>email</code> and <code>password</code> parameters</li>
<li>If <code>email</code> is missing or empty, return the JSON <code>{ "error": "email missing" }</code> with the status code <code>400</code> </li>
<li>If <code>password</code> is missing or empty, return the JSON <code>{ "error": "password missing" }</code> with the status code <code>400</code> </li>
<li>Retrieve the <code>User</code> instance based on the <code>email</code> - you must use the class method <code>search</code> of <code>User</code> (same as the one used for the <code>BasicAuth</code>)

<ul>
<li>If no <code>User</code> found, return the JSON <code>{ "error": "no user found for this email" }</code> with the status code <code>404</code> </li>
<li>If the <code>password</code> is not the one of the <code>User</code> found, return the JSON <code>{ "error": "wrong password" }</code> with the status code <code>401</code> - you must use <code>is_valid_password</code> from the <code>User</code> instance</li>
<li>Otherwise, create a Session ID for the <code>User</code> ID:

<ul>
<li>You must use <code>from api.v1.app import auth</code> - <strong>WARNING: please import it only where you need it</strong> - not on top of the file (can generate circular import - and break first tasks of this project)</li>
<li>You must use <code>auth.create_session(..)</code> for creating a Session ID</li>
<li>Return the dictionary representation of the <code>User</code> - you must use <code>to_json()</code> method from User </li>
<li>You must set the cookie to the response - you must use the value of the environment variable <code>SESSION_NAME</code> as cookie name - <a href="https://intranet.alxswe.com/rltoken/3WDlzYbVvdJJAf70IjWK6g" target="_blank" title="tip">tip</a></li>
</ul></li>
</ul></li>
</ul>

<p>In the file <code>api/v1/views/__init__.py</code>, you must add this new view at the end of the file.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XGET
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;405 Method Not Allowed&lt;/title&gt;
&lt;h1&gt;Method Not Allowed&lt;/h1&gt;
&lt;p&gt;The method is not allowed for the requested URL.&lt;/p&gt;
bob@dylan:~$
bob@dylan:~$  curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST
{
  "error": "email missing"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=guillaume@hbtn.io"
{
  "error": "password missing"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=guillaume@hbtn.io" -d "password=test"
{
  "error": "no user found for this email"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=test"
{
  "error": "wrong password"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; POST /api/v1/auth_session/login HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; Content-Length: 42
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Set-Cookie: _my_session_id=df05b4e1-d117-444c-a0cc-ba0d167889c4; Path=/
&lt; Access-Control-Allow-Origin: *
&lt; Content-Length: 210
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Mon, 16 Oct 2017 04:57:08 GMT
&lt; 
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
* Closing connection 0
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=df05b4e1-d117-444c-a0cc-ba0d167889c4"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
</code></pre>

<p>Now you have an authentication based on a Session ID stored in cookie, perfect for a website (browsers love cookies).</p>


</details>

<details>
<summary>

### 8. Logout
`mandatory`

File: [api/v1/auth/session_auth.py](), [api/v1/views/session_auth.py]()
</summary>

<p>Update the class <code>SessionAuth</code> by adding a new method <code>def destroy_session(self, request=None):</code> that deletes the user session / logout:</p>

<ul>
<li>If the <code>request</code> is equal to <code>None</code>, return <code>False</code></li>
<li>If the <code>request</code> doesn’t contain the Session ID cookie, return <code>False</code> - you must use <code>self.session_cookie(request)</code></li>
<li>If the Session ID of the request is not linked to any User ID, return <code>False</code> - you must use <code>self.user_id_for_session_id(...)</code></li>
<li>Otherwise, delete in <code>self.user_id_by_session_id</code> the Session ID (as key of this dictionary) and return <code>True</code></li>
</ul>

<p>Update the file <code>api/v1/views/session_auth.py</code>, by adding a new route <code>DELETE /api/v1/auth_session/logout</code>:</p>

<ul>
<li>Slash tolerant</li>
<li>You must use <code>from api.v1.app import auth</code></li>
<li>You must use <code>auth.destroy_session(request)</code> for deleting the Session ID contains in the request as cookie:

<ul>
<li>If <code>destroy_session</code> returns <code>False</code>, <code>abort(404)</code></li>
<li>Otherwise, return an empty JSON dictionary with the status code 200</li>
</ul></li>
</ul>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; POST /api/v1/auth_session/login HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; Content-Length: 42
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Set-Cookie: _my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721; Path=/
&lt; Access-Control-Allow-Origin: *
&lt; Content-Length: 210
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Mon, 16 Oct 2017 04:57:08 GMT
&lt; 
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;405 Method Not Allowed&lt;/title&gt;
&lt;h1&gt;Method Not Allowed&lt;/h1&gt;
&lt;p&gt;The method is not allowed for the requested URL.&lt;/p&gt;
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721" -XDELETE
{}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
{
  "error": "Forbidden"
}
bob@dylan:~$
</code></pre>

<p>Login, logout… what’s else?</p>

<p>Now, after getting a Session ID, you can request all protected API routes by using this Session ID, no need anymore to send User email and password every time.</p>


</details>



<details>
<summary>

### 9. Expiration?
`#advanced`

File: [api/v1/auth/session_exp_auth.py](), [api/v1/app.py]()
</summary>

<p>Actually you have 2 authentication systems:</p>

<ul>
<li>Basic authentication</li>
<li>Session authentication</li>
</ul>

<p>Now you will add an expiration date to a Session ID.</p>

<p>Create a class <code>SessionExpAuth</code> that inherits from <code>SessionAuth</code> in the file <code>api/v1/auth/session_exp_auth.py</code>:</p>

<ul>
<li>Overload <code>def __init__(self):</code> method:

<ul>
<li>Assign an instance attribute <code>session_duration</code>:

<ul>
<li>To the environment variable <code>SESSION_DURATION</code> casts to an integer</li>
<li>If this environment variable doesn’t exist or can’t be parse to an integer, assign to 0</li>
</ul></li>
</ul></li>
<li>Overload <code>def create_session(self, user_id=None):</code>
<ul>
<li>Create a Session ID by calling <code>super()</code> - <code>super()</code> will call the <code>create_session()</code> method of <code>SessionAuth</code></li>
<li>Return <code>None</code> if <code>super()</code> can’t create a Session ID</li>
<li>Use this Session ID as key of the dictionary <code>user_id_by_session_id</code> - the value for this key must be a dictionary (called “session dictionary”):

<ul>
<li>The key <code>user_id</code> must be set to the variable <code>user_id</code></li>
<li>The key <code>created_at</code> must be set to the current datetime - you must use <code>datetime.now()</code></li>
</ul></li>
<li>Return the Session ID created</li>
</ul></li>
<li>Overload <code>def user_id_for_session_id(self, session_id=None):</code>
<ul>
<li>Return <code>None</code> if <code>session_id</code> is <code>None</code></li>
<li>Return <code>None</code> if <code>user_id_by_session_id</code> doesn’t contain any key equals to <code>session_id</code></li>
<li>Return the <code>user_id</code> key from the session dictionary if <code>self.session_duration</code> is equal or under 0</li>
<li>Return <code>None</code> if session dictionary doesn’t contain a key <code>created_at</code></li>
<li>Return <code>None</code> if the <code>created_at</code> + <code>session_duration</code> seconds are before the current datetime.  <a href="https://intranet.alxswe.com/rltoken/mwc3EnlWLNJ2rvzvgZT8eA" target="_blank" title="datetime - timedelta">datetime - timedelta</a></li>
<li>Otherwise, return <code>user_id</code> from the session dictionary</li>
</ul></li>
</ul>

<p>Update <code>api/v1/app.py</code> to instantiate auth with <code>SessionExpAuth</code> if the environment variable <code>AUTH_TYPE</code> is equal to <code>session_exp_auth</code>.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_exp_auth SESSION_NAME=_my_session_id SESSION_DURATION=60 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; POST /api/v1/auth_session/login HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; Content-Length: 42
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Set-Cookie: _my_session_id=eea5d963-8dd2-46f0-9e43-fd05029ae63f; Path=/
&lt; Access-Control-Allow-Origin: *
&lt; Content-Length: 210
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Mon, 16 Oct 2017 04:57:08 GMT
&lt; 
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=eea5d963-8dd2-46f0-9e43-fd05029ae63f"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
bob@dylan:~$ sleep 10
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=eea5d963-8dd2-46f0-9e43-fd05029ae63f"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$ 
bob@dylan:~$ sleep 51 # 10 + 51 &gt; 60
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=eea5d963-8dd2-46f0-9e43-fd05029ae63f"
{
  "error": "Forbidden"
}
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 10. Sessions in database
`#advanced`

File: [api/v1/auth/session_db_auth.py](), [api/v1/app.py](), [models/user_session.py]()
</summary>

<p>Since the beginning, all Session IDs are stored in memory. It means, if your application stops, all Session IDs are lost.</p>

<p>For avoid that, you will create a new authentication system, based on Session ID stored in database (for us, it will be in a file, like <code>User</code>).</p>

<p>Create a new model <code>UserSession</code> in <code>models/user_session.py</code> that inherits from <code>Base</code>:</p>

<ul>
<li>Implement the <code>def __init__(self, *args: list, **kwargs: dict):</code> like in <code>User</code> but for these 2 attributes:

<ul>
<li><code>user_id</code>: string</li>
<li><code>session_id</code>: string</li>
</ul></li>
</ul>

<p>Create a new authentication class <code>SessionDBAuth</code> in <code>api/v1/auth/session_db_auth.py</code> that inherits from <code>SessionExpAuth</code>:</p>

<ul>
<li>Overload <code>def create_session(self, user_id=None):</code> that creates and stores new instance of <code>UserSession</code> and returns the Session ID</li>
<li>Overload <code>def user_id_for_session_id(self, session_id=None):</code> that returns the User ID by requesting <code>UserSession</code> in the database based on <code>session_id</code></li>
<li>Overload <code>def destroy_session(self, request=None):</code> that destroys the <code>UserSession</code> based on the Session ID from the request cookie</li>
</ul>

<p>Update <code>api/v1/app.py</code> to instantiate <code>auth</code> with <code>SessionDBAuth</code> if the environment variable <code>AUTH_TYPE</code> is equal to <code>session_db_auth</code>.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_db_auth SESSION_NAME=_my_session_id SESSION_DURATION=60 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; POST /api/v1/auth_session/login HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; Content-Length: 42
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Set-Cookie: _my_session_id=bacadfad-3c3b-4830-b1b2-3d77dfb9ad13; Path=/
&lt; Access-Control-Allow-Origin: *
&lt; Content-Length: 210
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Mon, 16 Oct 2017 04:57:08 GMT
&lt; 
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=bacadfad-3c3b-4830-b1b2-3d77dfb9ad13"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
bob@dylan:~$ sleep 10
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=bacadfad-3c3b-4830-b1b2-3d77dfb9ad13"
{
  "created_at": "2017-10-16 04:23:04", 
  "email": "bobsession@hbtn.io", 
  "first_name": null, 
  "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992", 
  "last_name": null, 
  "updated_at": "2017-10-16 04:23:04"
}
bob@dylan:~$
bob@dylan:~$ sleep 60
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=bacadfad-3c3b-4830-b1b2-3d77dfb9ad13"
{
  "error": "Forbidden"
}
bob@dylan:~$
</code></pre>


</details>

