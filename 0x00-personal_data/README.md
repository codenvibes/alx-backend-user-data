<h1 align="center"><b>0X00. PERSONAL DATA</b></h1>
<div align="center"><code>Back-end</code> <code>Authentification</code></div>

<br><div align="center"><img src="https://github.com/codenvibes/alx-backend-user-data/blob/master/0x00-personal_data/images/5c48d4f6d4dd8081eb48.png"></div>

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->


<!--==================================================-->
<br>

## Resources
<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/jf71oYqiETchcVhPzQVnyg">What Is PII, non-PII, and Personal Data?</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/W2JiHD6cbJY1scJORyLqnw">logging documentation</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/41oaQXfzwnF1i-wT8W0vHw">bcrypt package</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://intranet.alxswe.com/rltoken/XCpI9uvguxlTCsAeRCW6SA">Logging to Files, Setting Levels, and Formatting</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!--==================================================-->
<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a>Examples of Personally Identifiable Information (PII)</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to implement a log filter that will obfuscate PII fields</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to encrypt a password and check the validity of an input password</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to authenticate to a database using environment variables</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!--==================================================-->
<br>

## Requirements
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
- All your functions should be type annotated

<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. Regex-ing
`mandatory`

File: [filtered_logger.py]()
</summary>

<p>Write a function called <code>filter_datum</code> that returns the log message obfuscated: </p>

<ul>
<li>Arguments:

<ul>
<li><code>fields</code>: a list of strings representing all fields to obfuscate</li>
<li><code>redaction</code>: a string representing by what the field will be obfuscated</li>
<li><code>message</code>: a string representing the log line</li>
<li><code>separator</code>: a string representing by which character is separating all fields in the log line (<code>message</code>)</li>
</ul></li>
<li>The function should use a regex to replace occurrences of certain field values.</li>
<li><code>filter_datum</code> should be less than 5 lines long and use <code>re.sub</code> to perform the substitution with a single regex.</li>
</ul>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

bob@dylan:~$
bob@dylan:~$ ./main.py
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 1. Log formatter
`mandatory`

File: [filtered_logger.py]()
</summary>

<p>Copy the following code into <code>filtered_logger.py</code>.</p>

<pre><code class="python">import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -&gt; str:
        NotImplementedError
</code></pre>

<p>Update the class to accept a list of strings <code>fields</code> constructor argument.</p>

<p>Implement the <code>format</code> method to filter values in incoming log records using <code>filter_datum</code>. Values for fields in <code>fields</code> should be filtered.</p>

<p>DO NOT extrapolate <code>FORMAT</code> manually. The <code>format</code> method should be less than 5 lines long.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

import logging
import re

RedactingFormatter = __import__('filtered_logger').RedactingFormatter

message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))

bob@dylan:~$
bob@dylan:~$ ./main.py
[HOLBERTON] my_logger INFO 2019-11-19 18:24:25,105: name=Bob; email=***; ssn=***; password=***;
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 2. Create logger
`mandatory`

File: [filtered_logger.py]()
</summary>

<p>Use <a href="https://intranet.alxswe.com/rltoken/cVQXXtttuAobcFjYFKZTow" target="_blank" title="user_data.csv">user_data.csv</a> for this task</p>

<p>Implement a <code>get_logger</code> function that takes no arguments and returns a <code>logging.Logger</code> object.</p>

<p>The logger should be named <code>"user_data"</code> and only log up to <code>logging.INFO</code> level. It should not propagate messages to other loggers.
It should have a <code>StreamHandler</code> with <code>RedactingFormatter</code> as formatter.</p>

<p>Create a tuple <code>PII_FIELDS</code> constant at the root of the module containing the fields from <code>user_data.csv</code> that are considered PII. 
<code>PII_FIELDS</code> can contain only 5 fields - choose the right list of fields that can are considered as “important” PIIs or information that you <strong>must hide</strong> in your logs.
Use it to parameterize the formatter.</p>

<p><strong>Tips:</strong></p>

<ul>
<li><a href="https://intranet.alxswe.com/rltoken/jf71oYqiETchcVhPzQVnyg" target="_blank" title="What Is PII, non-PII, and personal data?">What Is PII, non-PII, and personal data?</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/HznI8kpvBxdnRM92BRoUmQ" target="_blank" title="Uncovering Password Habits">Uncovering Password Habits</a></li>
</ul>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

import logging

get_logger = __import__('filtered_logger').get_logger
PII_FIELDS = __import__('filtered_logger').PII_FIELDS

print(get_logger.__annotations__.get('return'))
print("PII_FIELDS: {}".format(len(PII_FIELDS)))

bob@dylan:~$
bob@dylan:~$ ./main.py
&lt;class 'logging.Logger'&gt;
PII_FIELDS: 5
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 3. Connect to secure database
`mandatory`

File: [filtered_logger.py]()
</summary>

<p>Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variable on the application server.</p>

<p>In this task, you will connect to a secure <code>holberton</code> database to read a <code>users</code> table. 
The database is protected by a username and password that are set as environment variables on the server named <code>PERSONAL_DATA_DB_USERNAME</code> (set the default as “root”), <code>PERSONAL_DATA_DB_PASSWORD</code> (set the default as an empty string) and <code>PERSONAL_DATA_DB_HOST</code> (set the default as “localhost”). </p>

<p>The database name is stored in <code>PERSONAL_DATA_DB_NAME</code>. </p>

<p>Implement a <code>get_db</code> function that returns a connector to the database (<code>mysql.connector.connection.MySQLConnection</code> object). </p>

<ul>
<li>Use the <code>os</code> module to obtain credentials from the environment</li>
<li>Use the module <code>mysql-connector-python</code> to connect to the MySQL database (<code>pip3 install mysql-connector-python</code>)</li>
</ul>

<pre><code>bob@dylan:~$ cat main.sql
-- setup mysql server
-- configure permissions
CREATE DATABASE IF NOT EXISTS my_db;
CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON my_db.* TO 'root'@'localhost';

USE my_db;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    email VARCHAR(256)
);

INSERT INTO users(email) VALUES ("bob@dylan.com");
INSERT INTO users(email) VALUES ("bib@dylan.com");

bob@dylan:~$ 
bob@dylan:~$ cat main.sql | mysql -uroot -p
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db
Enter password: 
2
bob@dylan:~$ 
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

get_db = __import__('filtered_logger').get_db

db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()

bob@dylan:~$
bob@dylan:~$ PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./main.py
2
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 4. Read and filter data
`mandatory`

File: [filtered_logger.py]()
</summary>

<p>Implement a <code>main</code> function that takes no arguments and returns nothing.</p>

<p>The function will obtain a database connection using <code>get_db</code> and retrieve all rows in the <code>users</code> table and display each row under a filtered format like this:</p>

<pre><code class="python">[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b; last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);
</code></pre>

<p>Filtered fields:</p>

<ul>
<li>name</li>
<li>email</li>
<li>phone</li>
<li>ssn</li>
<li>password</li>
</ul>

<p>Only your <code>main</code> function should run when the module is executed.</p>

<pre><code>bob@dylan:~$ cat main.sql
-- setup mysql server
-- configure permissions
CREATE DATABASE IF NOT EXISTS my_db;
CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON my_db.* TO root@localhost;

USE my_db;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    name VARCHAR(256), 
        email VARCHAR(256), 
        phone VARCHAR(16),
    ssn VARCHAR(16), 
        password VARCHAR(256),
    ip VARCHAR(64), 
        last_login TIMESTAMP,
    user_agent VARCHAR(512)
);

INSERT INTO users(name, email, phone, ssn, password, ip, last_login, user_agent) VALUES ("Marlene Wood","hwestiii@att.net","(473) 401-4253","261-72-6780","K5?BMNv","60ed:c396:2ff:244:bbd0:9208:26f2:93ea","2019-11-14 06:14:24","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36");
INSERT INTO users(name, email, phone, ssn, password, ip, last_login, user_agent) VALUES ("Belen Bailey","bcevc@yahoo.com","(539) 233-4942","203-38-5395","^3EZ~TkX","f724:c5d1:a14d:c4c5:bae2:9457:3769:1969","2019-11-14 06:16:19","Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30");

bob@dylan:~$ 
bob@dylan:~$ cat main.sql | mysql -uroot -p
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db
Enter password: 
2
bob@dylan:~$ 
bob@dylan:~$ PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,621: name=***; email=***; phone=***; ssn=***; password=***; ip=f724:c5d1:a14d:c4c5:bae2:9457:3769:1969; last_login=2019-11-14 06:16:19; user_agent=Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 5. Encrypting passwords
`mandatory`

File: [encrypt_password.py]()
</summary>

<p>User passwords should NEVER be stored in plain text in a database.</p>

<p>Implement a <code>hash_password</code> function that expects one string argument name <code>password</code> and returns a salted, hashed password, which is a byte string.</p>

<p>Use the <code>bcrypt</code> package to perform the hashing (with <code>hashpw</code>).</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

hash_password = __import__('encrypt_password').hash_password

password = "MyAmazingPassw0rd"
print(hash_password(password))
print(hash_password(password))

bob@dylan:~$
bob@dylan:~$ ./main.py
b'$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO'
b'$2b$12$xSAw.bxfSTAlIBglPMXeL.SJnzme3Gm0E7eOEKOVV2OhqOakyUN5m'
bob@dylan:~$
</code></pre>


</details>

<details>
<summary>

### 6. Check valid password
`mandatory`

File: [encrypt_password.py]()
</summary>

<p>Implement an <code>is_valid</code> function that expects 2 arguments and returns a boolean.</p>

<p>Arguments:</p>

<ul>
<li><code>hashed_password</code>:  <code>bytes</code> type</li>
<li><code>password</code>: string type</li>
</ul>

<p>Use <code>bcrypt</code> to validate that the provided password matches the hashed password.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid

password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(encrypted_password)
print(is_valid(encrypted_password, password))

bob@dylan:~$
bob@dylan:~$ ./main.py
b'$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO'
True
bob@dylan:~$
</code></pre>


</details>

