import requests


def test_some():
    req = requests.get("https://6795958b-b182-4407-a38b-200df0582b44.selcdn.net/e87aaae0fc7b5d20fa3e310aa58a23b66c622e55/vendor.css")
    print(req.status_code)
    print(req.text)