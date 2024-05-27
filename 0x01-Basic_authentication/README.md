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


</details>

<details>
<summary>

### 6. Basic auth
`mandatory`

File: [api/v1/app.py](), [api/v1/auth/basic_auth.py]()
</summary>


</details>

<details>
<summary>

### 7. Basic - Base64 part
`mandatory`

File: [api/v1/auth/basic_auth.py]()
</summary>


</details>

<details>
<summary>

### 8. Basic - Base64 decode
`mandatory`

File: [api/v1/auth/basic_auth.py]()
</summary>


</details>

<details>
<summary>

### 9. Basic - User credentials
`mandatory`

File: [api/v1/auth/basic_auth.py]()
</summary>


</details>

<details>
<summary>

### 10. Basic - User object
`mandatory`

File: [api/v1/auth/basic_auth.py]()
</summary>


</details>

<details>
<summary>

### 11. Basic - Overload current_user - and BOOM!
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 12. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 13. 
`#advanced`

File: []()
</summary>


</details>

