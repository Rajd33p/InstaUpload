# Working as of 20/12/2020

[![CodeFactor](https://www.codefactor.io/repository/github/rajd33p/instaupload/badge)](https://www.codefactor.io/repository/github/rajd33p/instaupload)
# InstaUpload

This Module Or Library can upload to your Instagram profile

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install selenium , pyautogui
```

## Usage

```python
from instagram import Insta #Importing the class

username = "" #Instagram's Username
password = "" #Instagram's password

user = Insta(username, password) # Create a object of the class


user.Login() #calling the Login method from the calss

data = {
    "PATH": "Path(user double slashes like c:\\Desktop\\something)",
    "Title": "Title of post",
    "PostLink": "Credits link"
}


user.post(data) #Calling the post function
user.exi() #exit the Browser

```

## Todo
* remove pyautogui with some light weight alternative
* Code optimization
