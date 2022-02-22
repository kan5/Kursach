import json
import requests

with open('a.json', 'rb') as f:
    posts = json.load(f)
ex = {
    "title": "Heey_bioy",
    "posted": "2021-11-07",
    "link": "test",
    "html_body": "test",
    "text": "test",
    "server_path": "test",
    "language": 1,
    "source": 2,
    "author": 1,
    "topic": [1, 2, 3]
}
print(posts.__len__())
print(posts[0].keys())
# print(posts[0].get('text'))
for i in posts[1:]:
    body = {
        "title": i.get('title'),
        "posted": '-'.join(reversed(i.get('posted').split()[-1].split('.'))),
        "link": i.get('source_link'),
        "html_body": i.get('html_body'),
        "text": i.get('text'),
        "server_path": "/metanit/sql/postgresql/",
        "language": 1,
        "source": 2,
        "author": 1,
        "topic": [1]
    }
    response = requests.post('http://127.0.0.1:55555/article/', data=body)
    print(response.text)
