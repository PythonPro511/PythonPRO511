import requests

repo_url = 'https://api.github.com/repos/requests/requests'  # Официальный репозиторий библиотеки requests
group_repo_url = 'https://api.github.com/repos/toppython425/PythonPRO511GitPycharm'

response = requests.get(repo_url)
if response.status_code == 200:
    repo_data = response.json()
    print(f'Репозиторий: {repo_data['name']}')
    print(f'Звезд: {repo_data['stargazers_count']}')
    print(f'Описание: {repo_data['description']}')
else:
    print(f'Ошибка: {response}')
