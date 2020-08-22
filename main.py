from instagram import Insta

username = ""
password = ""

user = Insta(username, password)


user.Login()
data = {
    "PATH": "Path(user double slashes like c:\\Desktop\\something",
    "Title": "Title of post",
    "PostLink": "Credits link"
}


user.post(data)
user.exi()
