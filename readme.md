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

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
