import json

import requests
from requests import Response

# Insert your cookies
KC_ACCESS = ""
KC_STATE = ""

# Insert your URL for Talisman framework
TALISMAN_URL = "https://isdct.talisman.ispras.ru"
TALISMAN_GRAPHQL_URL = TALISMAN_URL + "/graphql"


def send_message(message) -> Response:
    cookies = {"kc-access": KC_ACCESS, "kc-state": KC_STATE}

    # Depending on your browser, change this settings
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Content-Type": "application/json",
        "tz-offset": "28800",
        "x-trace-id": "53d3a734c1dd4c569d2988f0079480a6",
        "Origin": TALISMAN_URL,
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }

    json_data = {
        "operationName": "createPipelineTopicMessage",
        "variables": {
            "message": f"{message}",
            "priority": "Normal",
            "topic": "comment-courts-processing"
        },
        "extensions": {},
        "query": "mutation createPipelineTopicMessage($topic: String!, $priority: MessagePriority!, $message: JSON!) {\n createPipelineTopicMessage: addMessage(\n topic: $topic\n priority: $priority\n message: $message\n ) {\n id\n __typename\n }\n }"
    }

    return requests.post(TALISMAN_GRAPHQL_URL, cookies=cookies, headers=headers, json=json_data)


if __name__ == "__main__":
    with open("./data.json", "r") as f:
        data = json.load(f)
        for line in data:
            string, new_line = f"{line}", ""
            for char in string:
                if char == "'":
                    new_line += '\"'
                else:
                    new_line += char
            res = send_message(new_line)
            print(res)
