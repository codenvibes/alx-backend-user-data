<h1 align="center"><b>0x01. BASIC AUTHENTICATION</b></h1>
<div align="center"><code>Back-end</code> <code>Authentification</code></div>

<br>

## Background Context
<p>In this project, you will learn what the authentication process means and implement a <strong>Basic Authentication</strong> on a simple API.</p>

<p>In the industry, you should <strong>not</strong> implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="https://flask-httpauth.readthedocs.io/en/latest/" title="Flask-HTTPAuth" target="_blank">Flask-HTTPAuth</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>

<br><div align="center"><img src="https://github.com/codenvibes/alx-backend-user-data/blob/master/0x01-Basic_authentication/images/6ccb363443a8f301bc2bc38d7a08e9650117de7c.png"></div>


<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->

<br>

## Resources
<details>
<summary><b><a href="https://www.youtube.com/watch?v=501dpx2IjGY">REST API Authentication Mechanisms</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://docs.python.org/3.7/library/base64.html">Base64 in Python</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization">HTTP header Authorization</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://palletsprojects.com/p/flask/">Flask</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://en.wikipedia.org/wiki/Base64">Base64 - concept</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<!-- <br>

**man or help:**
- `` -->

<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a>What authentication means</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What Base64 is</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to encode a string in Base64</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What Basic authentication means</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to send the Authorization header</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

## Requirements
### Python Scripts
<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>


<!-- <br>

## More Info -->

<br>

## Tasks
<details>
<summary>

### 0. Simple-basic-API
`mandatory`

Directory: [0x01-Basic_authentication]()
</summary>

<p>Download and start your project from this <a href="https://intranet.alxswe.com/rltoken/2o4gAozNufil_KjoxKI5bA" title="archive.zip" target="_blank">archive.zip</a></p>

<p>In this archive, you will find a simple API with one model: <code>User</code>. Storage of these users is done via a serialization/deserialization in files.</p>

<h4>Setup and start server</h4>

<pre><code>bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app "app" (lazy loading)
...
bob@dylan:~$
</code></pre>

<h4>Use the API <em>(in another tab or in your browser)</em></h4>

<pre><code>bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; GET /api/v1/status HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; 
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Content-Length: 16
&lt; Access-Control-Allow-Origin: *
&lt; Server: Werkzeug/1.0.1 Python/3.7.5
&lt; Date: Mon, 18 May 2020 20:29:21 GMT
&lt; 
{"status":"OK"}
* Closing connection 0
bob@dylan:~$
</code></pre>

</details>

<details>
<summary>

### 1. Error handler: Unauthorized
`mandatory`

File: [api/v1/app.py](), [api/v1/views/index.py]()
</summary>

<p>What the HTTP status code for a request unauthorized? <code>401</code> of course!</p>

<p>Edit <code>api/v1/app.py</code>:</p>

<ul>
<li>Add a new error handler for this status code, the response must be:

<ul>
<li>a JSON: <code>{"error": "Unauthorized"}</code></li>
<li>status code <code>401</code></li>
<li>you must use <code>jsonify</code> from Flask</li>
</ul></li>
</ul>

<p>For testing this new error handler, add a new endpoint in <code>api/v1/views/index.py</code>:</p>

<ul>
<li>Route: <code>GET /api/v1/unauthorized</code></li>
<li>This endpoint must raise a 401 error by using <code>abort</code> - <a href="https://intranet.alxswe.com/rltoken/RH0gY_XQuSB75Q-JbI-fdg" title="Custom Error Pages" target="_blank">Custom Error Pages</a></li>
</ul>

<p>By calling <code>abort(401)</code>, the error handler for 401 will be executed.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized"
{
  "error": "Unauthorized"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; GET /api/v1/unauthorized HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; 
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 401 UNAUTHORIZED
&lt; Content-Type: application/json
&lt; Content-Length: 30
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Sun, 24 Sep 2017 22:50:40 GMT
&lt; 
{
  "error": "Unauthorized"
}
* Closing connection 0
bob@dylan:~$
</code></pre>

</details>

<details>
<summary>

### 2. Error handler: Forbidden
`mandatory`

File: [api/v1/app.py](), [api/v1/views/index.py]()
</summary>

<p>What the HTTP status code for a request where the user is authenticate but not allowed to access to a resource? <code>403</code> of course!</p>

<p>Edit <code>api/v1/app.py</code>:</p>

<ul>
<li>Add a new error handler for this status code, the response must be:

<ul>
<li>a JSON: <code>{"error": "Forbidden"}</code></li>
<li>status code <code>403</code></li>
<li>you must use <code>jsonify</code> from Flask</li>
</ul></li>
</ul>

<p>For testing this new error handler, add a new endpoint in <code>api/v1/views/index.py</code>:</p>

<ul>
<li>Route: <code>GET /api/v1/forbidden</code></li>
<li>This endpoint must raise a 403 error by using <code>abort</code> - <a href="https://intranet.alxswe.com/rltoken/RH0gY_XQuSB75Q-JbI-fdg" title="Custom Error Pages" target="_blank">Custom Error Pages</a></li>
</ul>

<p>By calling <code>abort(403)</code>, the error handler for 403 will be executed.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/forbidden"
{
  "error": "Forbidden"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/forbidden" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; GET /api/v1/forbidden HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; 
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 403 FORBIDDEN
&lt; Content-Type: application/json
&lt; Content-Length: 27
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Sun, 24 Sep 2017 22:54:22 GMT
&lt; 
{
  "error": "Forbidden"
}
* Closing connection 0
bob@dylan:~$
</code></pre>

</details>

<details>
<summary>

### 3. Auth class
`mandatory`

File: [api/v1/auth](), [api/v1/auth/__init__.py](), [api/v1/auth/auth.py]()
</summary>

<p>Now you will create a class to manage the API authentication.</p>

<ul>
<li>Create a folder <code>api/v1/auth</code></li>
<li>Create an empty file <code>api/v1/auth/__init__.py</code></li>
<li>Create the class <code>Auth</code>:

<ul>
<li>in the file <code>api/v1/auth/auth.py</code></li>
<li>import <code>request</code> from <code>flask</code></li>
<li>class name <code>Auth</code></li>
<li>public method <code>def require_auth(self, path: str, excluded_paths: List[str]) -&gt; bool:</code> that returns <code>False</code> - <code>path</code> and <code>excluded_paths</code> will be used later, now, you don’t need to take care of them</li>
<li>public method <code>def authorization_header(self, request=None) -&gt; str:</code> that returns <code>None</code> - <code>request</code> will be the Flask request object</li>
<li>public method <code>def current_user(self, request=None) -&gt; TypeVar('User'):</code> that returns <code>None</code> - <code>request</code> will be the Flask request object</li>
</ul></li>
</ul>

<p>This class is the template for all authentication system you will implement.</p>

<pre><code>bob@dylan:~$ cat main_0.py
#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.authorization_header())
print(a.current_user())

bob@dylan:~$ 
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_0.py
False
None
None
bob@dylan:~$
</code></pre>

</details>

<details>
<summary>

### 4. Define which routes don't need authentication
`mandatory`

File: [api/v1/auth/auth.py]()
</summary>

<p>Update the method <code>def require_auth(self, path: str, excluded_paths: List[str]) -&gt; bool:</code> in <code>Auth</code> that returns <code>True</code> if the <code>path</code> is not in the list of strings <code>excluded_paths</code>:</p>

<ul>
<li>Returns <code>True</code> if <code>path</code> is <code>None</code></li>
<li>Returns <code>True</code> if <code>excluded_paths</code> is <code>None</code> or empty</li>
<li>Returns <code>False</code> if <code>path</code> is in <code>excluded_paths</code></li>
<li>You can assume <code>excluded_paths</code> contains string path always ending by a <code>/</code></li>
<li>This method must be slash tolerant: <code>path=/api/v1/status</code> and <code>path=/api/v1/status/</code> must be returned <code>False</code> if <code>excluded_paths</code> contains <code>/api/v1/status/</code></li>
</ul>

<pre><code>bob@dylan:~$ cat main_1.py
#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth(None, None))
print(a.require_auth(None, []))
print(a.require_auth("/api/v1/status/", []))
print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_1.py
True
True
True
False
False
True
True
bob@dylan:~$
</code></pre>

</details>

<details>
<summary>

### 5. Request validation!
`mandatory`

File: [api/v1/app.py](), [api/v1/auth/auth.py]()
</summary>

<p>Now you will validate all requests to secure the API:</p>

<p>Update the method <code>def authorization_header(self, request=None) -&gt; str:</code> in <code>api/v1/auth/auth.py</code>:</p>

<ul>
<li>If <code>request</code> is <code>None</code>, returns <code>None</code> </li>
<li>If <code>request</code> doesn’t contain the header key <code>Authorization</code>, returns <code>None</code></li>
<li>Otherwise, return the value of the header request <code>Authorization</code></li>
</ul>

<p>Update the file <code>api/v1/app.py</code>:</p>

<ul>
<li>Create a variable <code>auth</code> initialized to <code>None</code> after the <code>CORS</code> definition</li>
<li>Based on the environment variable <code>AUTH_TYPE</code>, load and assign the right instance of authentication to <code>auth</code>

<ul>
<li>if <code>auth</code>:

<ul>
<li>import <code>Auth</code> from <code>api.v1.auth.auth</code></li>
<li>create an instance of <code>Auth</code> and assign it to the variable <code>auth</code></li>
</ul></li>
</ul></li>
</ul>

<p>Now the biggest piece is the filtering of each request. For that you will use the Flask method <a href="https://intranet.alxswe.com/rltoken/kzBrJT9aaokbD6aWYyQzXg" title="before_request" target="_blank">before_request</a></p>

<ul>
<li>Add a method in <code>api/v1/app.py</code> to handler <code>before_request</code>

<ul>
<li>if <code>auth</code> is <code>None</code>, do nothing</li>
<li>if <code>request.path</code> is not part of this list <code>['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']</code>, do nothing - you must use the method <code>require_auth</code> from the <code>auth</code> instance</li>
<li>if <code>auth.authorization_header(request)</code> returns <code>None</code>, raise the error <code>401</code> - you must use <code>abort</code></li>
<li>if <code>auth.current_user(request)</code> returns <code>None</code>, raise the error <code>403</code> - you must use <code>abort</code></li>
</ul></li>
</ul>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=auth python3 -m api.v1.app
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

### 6. Basic auth
`mandatory`

File: [api/v1/app.py](), [api/v1/auth/basic_auth.py]()
</summary>

<p>Create a class <code>BasicAuth</code> that inherits from <code>Auth</code>. For the moment this class will be empty.</p>

<p>Update <code>api/v1/app.py</code> for using <code>BasicAuth</code> class instead of <code>Auth</code> depending of the value of the environment variable <code>AUTH_TYPE</code>, If <code>AUTH_TYPE</code> is equal to <code>basic_auth</code>:</p>

<ul>
<li>import <code>BasicAuth</code> from <code>api.v1.auth.basic_auth</code></li>
<li>create an instance of <code>BasicAuth</code> and assign it to the variable <code>auth</code></li>
</ul>

<p>Otherwise, keep the previous mechanism with <code>auth</code> an instance of <code>Auth</code>.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
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

### 7. Basic - Base64 part
`mandatory`

File: [api/v1/auth/basic_auth.py]()
</summary>

<p>Add the method <code>def extract_base64_authorization_header(self, authorization_header: str) -&gt; str:</code> in the class <code>BasicAuth</code> that returns the Base64 part of the <code>Authorization</code> header for a Basic Authentication:</p>

<ul>
<li>Return <code>None</code> if <code>authorization_header</code> is <code>None</code></li>
<li>Return <code>None</code> if <code>authorization_header</code> is not a string</li>
<li>Return <code>None</code> if <code>authorization_header</code> doesn’t start by <code>Basic</code> (with a space at the end)</li>
<li>Otherwise, return the value after <code>Basic</code> (after the space)</li>
<li>You can assume <code>authorization_header</code> contains only one <code>Basic</code></li>
</ul>

<pre><code>bob@dylan:~$ cat main_2.py
#!/usr/bin/env python3
""" Main 2
"""
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_base64_authorization_header(None))
print(a.extract_base64_authorization_header(89))
print(a.extract_base64_authorization_header("Holberton School"))
print(a.extract_base64_authorization_header("Basic Holberton"))
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))
print(a.extract_base64_authorization_header("Basic1234"))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_2.py
None
None
None
Holberton
SG9sYmVydG9u
SG9sYmVydG9uIFNjaG9vbA==
None
bob@dylan:~$
</code></pre>

</details>

<details>
<summary>

### 8. Basic - Base64 decode
`mandatory`

File: [api/v1/auth/basic_auth.py]()
</summary>

<p>Add the method <code>def decode_base64_authorization_header(self, base64_authorization_header: str) -&gt; str:</code> in the class <code>BasicAuth</code> that returns the decoded value of a Base64 string <code>base64_authorization_header</code>:</p>

<ul>
<li>Return <code>None</code> if <code>base64_authorization_header</code> is <code>None</code></li>
<li>Return <code>None</code> if <code>base64_authorization_header</code> is not a string</li>
<li>Return <code>None</code> if <code>base64_authorization_header</code> is not a valid Base64 - you can use <code>try/except</code></li>
<li>Otherwise, return the decoded value as UTF8 string - you can use <code>decode('utf-8')</code></li>
</ul>

<pre><code>bob@dylan:~$ cat main_3.py
#!/usr/bin/env python3
""" Main 3
"""
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.decode_base64_authorization_header(None))
print(a.decode_base64_authorization_header(89))
print(a.decode_base64_authorization_header("Holberton School"))
print(a.decode_base64_authorization_header("SG9sYmVydG9u"))
print(a.decode_base64_authorization_header("SG9sYmVydG9uIFNjaG9vbA=="))
print(a.decode_base64_authorization_header(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA==")))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_3.py
None
None
None
Holberton
Holberton School
Holberton School
bob@dylan:~$
</code></pre>

</details>

<details>
<summary>

### 9. Basic - User credentials
`mandatory`

File: [api/v1/auth/basic_auth.py]()
</summary>

<p>Add the method <code>def extract_user_credentials(self, decoded_base64_authorization_header: str) -&gt; (str, str)</code> in the class <code>BasicAuth</code> that returns the user email and password from the Base64 decoded value.</p>

<ul>
<li>This method must return 2 values</li>
<li>Return <code>None, None</code> if <code>decoded_base64_authorization_header</code> is <code>None</code></li>
<li>Return <code>None, None</code> if <code>decoded_base64_authorization_header</code> is not a string</li>
<li>Return <code>None, None</code> if <code>decoded_base64_authorization_header</code> doesn’t contain <code>:</code></li>
<li>Otherwise, return the user email and the user password - these 2 values must be separated by a <code>:</code></li>
<li>You can assume <code>decoded_base64_authorization_header</code> will contain only one <code>:</code></li>
</ul>

<pre><code>bob@dylan:~$ cat main_4.py
#!/usr/bin/env python3
""" Main 4
"""
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_user_credentials(None))
print(a.extract_user_credentials(89))
print(a.extract_user_credentials("Holberton School"))
print(a.extract_user_credentials("Holberton:School"))
print(a.extract_user_credentials("bob@gmail.com:toto1234"))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_4.py
(None, None)
(None, None)
(None, None)
('Holberton', 'School')
('bob@gmail.com', 'toto1234')
bob@dylan:~$
</code></pre>

</details>

<details>
<summary>

### 10. Basic - User object
`mandatory`

File: [api/v1/auth/basic_auth.py]()
</summary>

<p>Add the method <code>def user_object_from_credentials(self, user_email: str, user_pwd: str) -&gt; TypeVar('User'):</code> in the class <code>BasicAuth</code> that returns the <code>User</code> instance based on his email and password.</p>

<ul>
<li>Return <code>None</code> if <code>user_email</code> is <code>None</code> or not a string</li>
<li>Return <code>None</code> if <code>user_pwd</code> is <code>None</code> or not a string</li>
<li>Return <code>None</code> if your database (file) doesn’t contain any <code>User</code> instance with email equal to <code>user_email</code> - you should use the class method <code>search</code> of the <code>User</code> to lookup the list of users based on their email. Don’t forget to test all cases: “what if there is no user in DB?”, etc.</li>
<li>Return <code>None</code> if <code>user_pwd</code> is not the password of the <code>User</code> instance found - you must use the method <code>is_valid_password</code> of <code>User</code></li>
<li>Otherwise, return the <code>User</code> instance</li>
</ul>

<pre><code>bob@dylan:~$ cat main_5.py
#!/usr/bin/env python3
""" Main 5
"""
import uuid
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
user_email = str(uuid.uuid4())
user_clear_pwd = str(uuid.uuid4())
user = User()
user.email = user_email
user.first_name = "Bob"
user.last_name = "Dylan"
user.password = user_clear_pwd
print("New user: {}".format(user.display_name()))
user.save()

""" Retreive this user via the class BasicAuth """

a = BasicAuth()

u = a.user_object_from_credentials(None, None)
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(89, 98)
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials("email@notfound.com", "pwd")
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(user_email, "pwd")
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(user_email, user_clear_pwd)
print(u.display_name() if u is not None else "None")

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_5.py 
New user: Bob Dylan
None
None
None
None
Bob Dylan
bob@dylan:~$
</code></pre>

</details>

<details>
<summary>

### 11. Basic - Overload current_user - and BOOM!
`mandatory`

File: [api/v1/auth/basic_auth.py]()
</summary>

<p>Now, you have all pieces for having a complete Basic authentication.</p>

<p>Add the method <code>def current_user(self, request=None) -&gt; TypeVar('User')</code> in the class <code>BasicAuth</code> that overloads <code>Auth</code> and retrieves the <code>User</code> instance for a request:</p>

<ul>
<li>You must use <code>authorization_header</code></li>
<li>You must use <code>extract_base64_authorization_header</code></li>
<li>You must use <code>decode_base64_authorization_header</code></li>
<li>You must use <code>extract_user_credentials</code></li>
<li>You must use <code>user_object_from_credentials</code></li>
</ul>

<p>With this update, now your API is fully protected by a Basic Authentication. Enjoy!</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ cat main_6.py
#!/usr/bin/env python3
""" Main 6
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
print("New user: {} / {}".format(user.id, user.display_name()))
user.save()

basic_clear = "{}:{}".format(user_email, user_clear_pwd)
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_6.py 
New user: 9375973a-68c7-46aa-b135-29f79e837495 / bob@hbtn.io
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
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{
  "error": "Forbidden"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic test"
{
  "error": "Forbidden"
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
</code></pre>

</details>

<details>
<summary>

### 12. Basic - Allow password with ":"
`#advanced`

File: [api/v1/auth/basic_auth.py]()
</summary>


</details>

<details>
<summary>

### 13. Require auth with stars
`#advanced`

File: [api/v1/auth/auth.py]()
</summary>


</details>

