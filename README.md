# CSE406DictionaryAttack
Dictionary Attack Term Project

## 1. What is Dictionary attack?
In cryptanalysis and computer security, a dictionary attack is a form of brute force attack technique for defeating a cipher or authentication mechanism by trying to determine its decryption key or passphrase by trying hundreds or sometimes millions of likely possibilities, such as words in a dictionary.

![Dictionary Attack](../assets/intro.jpg?raw=true)

## 2.	What is the basic strategy?
A dictionary attack is based on trying all the strings in a pre-arranged listing, typically derived from a list of words such as in a dictionary (hence the phrase dictionary attack). In contrast to a brute force attack, where a large proportion of the key space is searched systematically, a dictionary attack tries only those possibilities which are deemed most likely to succeed. 

![Dictionary Attack](../assets/flow.png?raw=true)

It is possible to achieve a time–space tradeoff by pre-computing a list of hashes of dictionary words, and storing these in a database using the hash as the key. This requires a considerable amount of preparation time, but allows the actual attack to be executed faster. Pre-computed dictionary attacks are particularly effective when a large number of passwords are to be cracked. The pre-computed dictionary need be generated only once, and when it is completed, password hashes can be looked up almost instantly at any time to find the corresponding password.

## 3.	How many types?
There are mainly 2 types of dictionary attack. 
1.	Online Dictionary Attack
2.	Offline Dictionary Attack

## 4.	Which attacks will I implement?
1)	Attack on FTP Server (Online)
2)	Attack on Login form (Online)
3)	Attack on offline password protected files (Offline)

## 5.	Dictionary Attack on FTP Server
### What is an FTP Server?
An FTP server is a computer which has a file transfer protocol (FTP) address and is dedicated to receiving an FTP connection.

### What is the authentication system of FTP Server?
1.	FTP’s regular authentication scheme is quite rudimentary: it is a simple “username / password” login scheme, shown in Figure. Most of us are familiar with this type of authentication for various types of access, on the Internet and elsewhere. First, the user is identified by sending a user name from the User-PI to the Server-PI using the USER command. Then, the user's password is sent using the PASS command.
2.	The server checks the user name and password against its user database, to verify that the connecting user has valid authority to access the server. If the information is valid, the server sends back a greeting to the client to indicate that the session is opened. If the user improperly authenticates (by specifying an incorrect user name or password), the server will request that the user attempt authorization again.
3.	After successful authentication, the server then sets up the connection to allow the type of access to which the user is authorized.

![Dictionary Attack](../assets/ftp.png?raw=true)

### What are the steps to crack FTP Server password?
1.	Establishing TCP connection to the server.
2.	Generate the dictionary file.
3.	Send the username that we are cracking password for.
4.	Try the passwords in the dictionary file and check if login successful and show the cracked password.

### Which tools are we using?
1.	Python Programming Language for scripting
2.	ftplib library for making TCP connection with the FTP Server
3.	For simulation purpose, we are using windows default FTP Server.

![Dictionary Attack](../assets/ftpserver.png?raw=true)

## 6.	Dictionary Attack on Login page
### What is a Login page?
The login page allows a user to gain access to an application by entering their username and password or by authenticating using a social media login.

![Dictionary Attack](../assets/login.jpg?raw=true)

### How passwords are sent from Login pages?
Passwords are taken through the forms.  The passwords are posted through HTTP Post method. A general HTTP POST method in the website will send the password in the HTTP header and a response will come from the other side. 

![Dictionary Attack](../assets/httpheader.png?raw=true)

### What is a HTTP Request?
An HTTP client sends an HTTP request to a server in the form of a request message which includes following format:
1.	A Request-line which begins with a method token followed by the Request-URI and the protocol version, and ending with CRLF.
2.	Zero or more header fields followed by CRLF. There are many header fields for this.
3.	An empty line indicating the end of the header fields.
4.	Optionally a message-body
A sample HTTP request is shown below:

![Dictionary Attack](../assets/httprequest.png?raw=true)

### What are the steps of the attack?
1.	First, we will have to get the url of the login page.
2.	Then, we will have to inspect the login page and find the username and password field. We will need the id and class name for the username and password field.
3.	We need to figure out the password success and failure response from the website.
4.	Then we will construct a HTTP request header for the login page and try to login using username and passwords from our dictionary.
5.	If we become successful, then we will show the password for the username.

### Which tools are we using?
1.	Python Programming Language.
2.	requests standard library for constructing HTTP request for the website.
3.	We will host a dummy website on a local server to test our attack. Our dummy login page will look like following:

![Dictionary Attack](../assets/target.png?raw=true)

4.	For local server, we will use wampserver.

## 7.	Dictionary Attack on Offline Password Protected Files
### What is a password protected file?
When a document like pdf, docs or zip is encrypted with a password, then it is called password protected document.

![Dictionary Attack](../assets/filepass.png?raw=true)

### What are the steps of the attack?
1.	For the password protected files, we will generate a password dictionary.
2.	Guess the password for the file.
3.	If we become successful then the password is cracked.

### Which tools are we using?
1.	Python Programming Language
2.	zip, pypdf2 library for opening and entering passwords for zip and pdf files.

## 8.	When will we be successful on dictionary attack?
Dictionary attacks often succeed because many people have a tendency to choose short passwords that are ordinary words or common passwords, or simple variants obtained, for example, by appending a digit or punctuation character. So, we can exploit this ignorance of many people of using weak passwords. By guessing the common passwords, there is a chance of cracking the authentication system.

## 9.	How can we prevent Dictionary attack? 
1.	The first is to implement an account lockout policy. For example, after three failed login attempts, the account is locked out until an administrator unlocks it.
2.	We should use a challenge-response test to prevent automated submissions of the login page. Tools such as the free reCAPTCHA can be used to require the user to enter a word or solve a simple math problem to ensure the user is, in fact, a person.
3.	Any Web application should enforce the use of strong passwords. At a minimum, requiring users to choose passwords of eight letters or more with some complexity (letters and numbers, or requiring one special character) is an excellent defense against brute force attacks.
