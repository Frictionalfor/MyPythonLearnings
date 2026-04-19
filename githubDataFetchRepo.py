import requests
from bs4 import BeautifulSoup
import json
import time

username = "FrictionalFor"  # change this
base_url = f"https://github.com/{username}?tab=repositories"

all_repos = []
page = 1

while True:
    url = f"{base_url}&page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    repo_list = soup.find_all("h3")

    if not repo_list:
        break

    for repo in repo_list:
        link_tag = repo.find("a")
        repo_name = link_tag.text.strip()
        repo_link = "https://github.com" + link_tag["href"]

        #repo details
        repo_page = requests.get(repo_link)
        repo_soup = BeautifulSoup(repo_page.text, "html.parser")

        # Description
        desc_tag = repo_soup.find("p")
        description = desc_tag.text.strip() if desc_tag else "None"

        # Languages (all)
        lang_tags = repo_soup.find_all("span", {"class": "color-fg-default text-bold mr-1"})
        languages = [lang.text.strip() for lang in lang_tags]

        # Stars
        star_tag = repo_soup.find("a", {"href": f"{link_tag['href']}/stargazers"})
        stars = star_tag.text.strip() if star_tag else "0"

        repo_info = {
            "name": repo_name,
            "repo_link": repo_link,
            "description": description,
            "languages": languages,
            "stars": stars
        }

        all_repos.append(repo_info)

        time.sleep(1)  # be polite to GitHub

    page += 1

# -------- Save JSON --------
with open("github_repos.json", "w", encoding="utf-8") as f:
    json.dump(all_repos, f, indent=4)

# -------- Save TXT --------
with open("github_repos.txt", "w", encoding="utf-8") as f:
    for repo in all_repos:
        f.write(f"Name: {repo['name']}\n")
        f.write(f"Link: {repo['repo_link']}\n")
        f.write(f"Description: {repo['description']}\n")
        f.write(f"Languages: {', '.join(repo['languages'])}\n")
        f.write(f"Stars: {repo['stars']}\n")
        f.write("-" * 50 + "\n")

