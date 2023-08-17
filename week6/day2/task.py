import requests
import json

URL = 'https://jsonplaceholder.typicode.com'

def handle_response(response: requests.Response) -> None:
    print(response.status_code)
    print()
    print(response.headers)
    print()
    for i in response.json():
        print(i)
        print()


try:
    get_response = requests.get(f'{URL}/posts')
    handle_response(get_response)

    post_body = json.dumps({
        "title": "foo",
        "body": "bar",
        "userId": 1
    })
    post_headers = {
        "Content-type": "application/json; charset=UTF-8",
    }
    post_response = requests.post(f'{URL}/posts', data=post_body, headers=post_headers)
    handle_response(post_response)

except (requests.ConnectionError, requests.JSONDecodeError, requests.RequestException) as e:
    print(e)