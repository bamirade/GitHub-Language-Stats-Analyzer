import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_language_stats(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    repos = response.json()

    language_stats = {}

    for repo in repos:
        languages_url = repo['languages_url']
        languages_response = requests.get(languages_url)
        repo_languages = languages_response.json()

        for language, bytes_used in repo_languages.items():
            if language in language_stats:
                language_stats[language] += bytes_used
            else:
                language_stats[language] = bytes_used

    total_bytes = sum(language_stats.values())
    language_percentages = {language: (bytes_used / total_bytes) * 100 for language, bytes_used in language_stats.items()}

    return language_percentages

username = os.getenv("USERNAME")
language_percentages = get_language_stats(username)

for language, percentage in language_percentages.items():
    print(f"{language}: {percentage:.2f}%")
