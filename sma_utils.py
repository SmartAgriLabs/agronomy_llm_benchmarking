import requests


def query_centeotl(formatted_prompts: dict[str, str], url: str, api_key: str) -> str:
    message = formatted_prompts["system_prompt"] + '\n###\n' + formatted_prompts["user_prompt"]
    headers = {
        "X-API-Key": api_key,
        "Content-Type": "application/json",
    }
    data = {
        "question": message,
    }
    try:
        response = requests.post(
            url=url,
            headers=headers,
            json=data,
        )
        answer = response.json()['answer']
        return answer
    except Exception as e:
        print(f'Exception querying Сenteōtl: {e}')
        return ''
