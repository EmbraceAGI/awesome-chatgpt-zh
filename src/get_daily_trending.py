import requests
import json

def fetch_trending_repos():
    url = "https://api.gitterapp.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # make sure to raise an error if the request fails
    return response.json()

def save_as_markdown(repos):
    with open('trending.md', 'w', encoding='utf-8') as f:
        f.write("|名称|Stars|简介|备注|\n")
        f.write("|---|---|---|---|\n")
        for repo in repos:
            name = repo['author'] + '/' + repo['name']
            url = 'https://github.com/' + name
            stars = '![GitHub Repo stars](https://badgen.net/github/stars/' + name + ')'
            description = repo['description'] or 'No Description'
            f.write(f"|[{name}]({url})|{stars}|{description}|-|\n")

def main():
    repos = fetch_trending_repos()
    save_as_markdown(repos)

if __name__ == "__main__":
    main()
