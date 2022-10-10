import requests
# r = requests.get("https://gorest.co.in/public/v2/users")
# print(r.text)
# print((r.status_code))
# print(r.json)

# r = requests.post('https://httpbin.org/post', data={'key': 'value'})

# r = requests.put('https://httpbin.org/put', data={'key': 'value'})
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)


# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url)

# r = requests.get('https://api.github.com/events')
# print(r.text)
# print(r.encoding)
# r.encoding = 'ISO-8859-1'
# print(r.encoding)
# print(r.text)
# print(r.content)

# from PIL import Image
# from io import BytesIO
#
# i = Image.open(BytesIO(r.content))

# print(r.json())

# r = requests.get('https://api.github.com/events', stream=True)
# # print(r.raw)
# print(r.raw.read(10))

# with open("request_stream.txt", 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=128):
#         fd.write(chunk)

# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
#
# r = requests.get(url, headers=headers)
# print(r.text)

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("https://httpbin.org/post", data=payload)
# print(r.text)

# payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
# r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
# payload_dict = {'key1': ['value1', 'value2']}
# r2 = requests.post('https://httpbin.org/post', data=payload_dict)
# print(r1.text)
#
# print(r1.text == r2.text)

# re = requests.get("https://gorest.co.in/public/v2/users")
# print(re.text)

# url = "https://gorest.co.in/public/v2/users"
# headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
# r = requests.get(url, headers=headers)
# print(r.json())

url = "https://api.github.com/users"
data = {
    "user": 1,
    "password" : 78
    }
r = requests.get(url=url, data=data)
with open("request_stream.txt", 'wb') as fd:
    for stream in r.iter_content(chunk_size=128):
        fd.write(stream)