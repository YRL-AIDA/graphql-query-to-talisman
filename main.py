import requests
import json

def send_data(message) -> None:
    # Вставить свои куки
    cookies = {
        'kc-access':'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlcHo3WVNCeXM4Y1NzdzhnajZURk1iR2lhVlhPRzhkLUpKak1xUnhYV2tZIn0.eyJleHAiOjE3MjU4NTYzMzUsImlhdCI6MTcyNTg1NjAzNSwianRpIjoiNGE3ZjdlMGYtY2RhNy00YTRiLWE2MjEtMTk1YmU0MDAzMzY4IiwiaXNzIjoiaHR0cHM6Ly9pc2RjdC50YWxpc21hbi5pc3ByYXMucnUvYXV0aC9yZWFsbXMvY29yZSIsImF1ZCI6WyJ3ZWItdWkiLCJyZWFsbS1tYW5hZ2VtZW50IiwiYWNjb3VudCJdLCJzdWIiOiJhYWNmODcxZC1iM2Q5LTQ2M2MtYmUyZS1mZDFkYzU2NDYwMzkiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ3ZWItdWkiLCJzZXNzaW9uX3N0YXRlIjoiYmUzMWEzMjUtODcyMC00NTBkLWFiMjYtNTU0YjczYzUxOWVmIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJyZWFsbS1tYW5hZ2VtZW50Ijp7InJvbGVzIjpbIm1hbmFnZS1yZWFsbSIsImltcGVyc29uYXRpb24iLCJ2aWV3LWV2ZW50cyIsIm1hbmFnZS11c2VycyIsInZpZXctY2xpZW50cyIsInF1ZXJ5LWNsaWVudHMiXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiJiZTMxYTMyNS04NzIwLTQ1MGQtYWIyNi01NTRiNzNjNTE5ZWYiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiQHVzZXIiOnsiaXNBZG1pbiI6dHJ1ZX0sInByZWZlcnJlZF91c2VybmFtZSI6ImFkbWluIiwibG9jYWxlIjoicnUifQ.TATS0vLVqJMySsAK_WC9CYpbZ-U52aHnzGqSjDYeIQDocsLXeUussy8LdYv_tHW23QUCoNh7z_UuJUUuZuTYM5K7r1p7NiT9HuxG7DjRnaeUkgh-F_a50jipOY0fJFopJk-ZhnWdKuehPUYHOB9VT77_vV1VNGw8gEkGC6Xl_45MuSEDpWAg0Lvyfq6TJebYCmPh5KuDQYAdKXS9A7gpgMg9wrPqByz9pnjGPurTO_VnLaoC092_gW6RS37hbLNuekIHUXfGedZnt4tBZ05snpfQdHIazEVh8bLaJ93KL8gvKVkdXDgFVoaQHhTcwKnCwBWCXYHg57Dy54LV6JMH1Q',
        'kc-state':'4jIxm9d2PryD7xfuIOvNCiTghr8aVhD/WJAW8PMAkZ3ZJmwupZHn7hQlolcCXpxl5alDZ0F8HuYumCJLHlUGmV11/ggxwud5Ubk1zqzT9vVGW6yCtm9PBWCzPsOyO/HfuDh2IOjo0f1Q77JFjHsvXTE8AelpZGd/j5ZPUVm0eH3AK8ciyul7m0sH5HG6PIbA/R7TuPaiJ8FFnc60mjZuMYh+7XV0W7daK65unKkpWzlrcSxCrvs0gDsAGO4saeh367mgGGyymQoTBMLRD+etRYdS1mvdLgGiAIauasLp5HGoo/nTJrlM19RvmgqE4zCbVb75g0/bd0bqof7aeEs5HqZcLBKX4y68F2Try8MZDSSCY1Us1u6Ze03znqrNai4WOo3fu3QfdLtYG41nEPPLfZjEwYBBdbIcgPoTjPPhB42ng4ODZTXI8pnRjwr3yzq69sqciHGvwFOekMYNyt07I8JKE8Cdy42veFGIXEbcy5XlR0Jslr7NjgCnr1HkMMJNCBMm2T0hoP3VQm9FOjSzjFKgAT5qkpoKHaz60uykgplnuTQqtTOubIq2WFyoTBz9P651HdER6eLvitZXRmaUZMK8IXVe/qMW11IR+DacaL7kB+e9Kcx/frxnzlY6YYT/QhAvyczQT0h6hPL9KBjYFzu0F7YVRhmXLKnzDMrrOMTYb6jBJlDMGLdggE335by1yXg4ZMjF0DsLBZjAktwLNBZPlo4LP7J2cryr0UsaJTcT3jDkK/Z18XoU5DvPTeXuWHs1E/tYzPX2KmVVWrshMwHq8OD+ZBQP1bgxRwNfA+lvCJSYxU0oD1rz8dEYzgKaX7gchgRySlqbgTF5YpVznTI5ieeHXASdSEKM1pix3wHMfArNUS1eUBS03pivFKhJybe/tpW9RYb4CsyGBz5ncIE9n+N4K3grAGO9JPWwsikqzuc5iHioCJU'}
    
    # В зависимости от браузера поменять парметры 
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'application/json',
        'tz-offset': '28800',
        'x-trace-id': '53d3a734c1dd4c569d2988f0079480a6',
        'Origin': 'https://isdct.talisman.ispras.ru',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    json_data = {
        'operationName': 'createPipelineTopicMessage',
        'variables': {
            'message':f"{message}",
            'priority': 'Normal',
            'topic':'comment-courts-processing'
        },
        'extensions': {},
        'query':'mutation createPipelineTopicMessage($topic: String!, $priority: MessagePriority!, $message: JSON!) {\n createPipelineTopicMessage: addMessage(\n topic: $topic\n priority: $priority\n message: $message\n ) {\n id\n __typename\n }\n }'
        }

    return requests.post('https://isdct.talisman.ispras.ru/graphql', cookies=cookies, headers=headers,
                         json=json_data)


with open("./items.json", "r") as f:
    data = json.load(f)
         
    for line in data:
        string = f"{line}"
        new_line = ""
        for char in string:
            # print(char)
            if char == "'":
                new_line += '\"'
            else:
                new_line += char
        # print(new_line)
        res = send_data(new_line)
        print(res)
        
        