import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_language_stats(username, token):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://api.github.com/users/{username}/repos?type=all"
    response = requests.get(url, headers=headers)
    repos = response.json()

    language_stats = {}

    for repo in repos:
        repo_languages = get_repo_languages(repo, headers)
        for language, bytes_used in repo_languages.items():
            if language in language_stats:
                language_stats[language] += bytes_used
            else:
                language_stats[language] = bytes_used

    total_bytes = sum(language_stats.values())
    language_percentages = {language: (bytes_used / total_bytes) * 100 for language, bytes_used in language_stats.items()}

    return language_percentages

def get_repo_languages(repo, headers):
    languages_url = repo['languages_url']
    languages_response = requests.get(languages_url, headers=headers)
    return languages_response.json()

username = os.getenv("USERNAME")
github_token = os.getenv("GITHUB_ACCESS_TOKEN")
language_percentages = get_language_stats(username, github_token)

for language, percentage in language_percentages.items():
    print(f"{language}: {percentage:.2f}%")
