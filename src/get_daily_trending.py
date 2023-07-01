import requests
import json
import time

def fetch_trending_repos():
    url = "https://api.gitterapp.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # make sure to raise an error if the request fails
    return response.json()

def save_as_markdown(repos):
    today = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    with open('trending.md', 'a+', encoding='utf-8') as f:
        f.write("*********{}*********\n".format(today))
        f.write("|名称|Stars|简介|备注|\n")
        f.write("|---|---|---|---|\n")
        for repo in repos:
            name = repo['author'] + '/' + repo['name']
            url = 'https://github.com/' + name
            stars = '![GitHub Repo stars](https://badgen.net/github/stars/' + name + ')'
            description = repo['description'] or 'No Description'
            f.write(f"|[{name}]({url})|{stars}|{description}|-|\n")
        f.write("*********{}*********\n".format(today))

def main():
    repos = fetch_trending_repos()
    save_as_markdown(repos)

if __name__ == "__main__":
    main()
