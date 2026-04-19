import requests
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor

username = "octocat"  # change this

headers = {"User-Agent": "Mozilla/5.0"}

base_url = f"https://github.com/{username}?tab=repositories"


# ---------- Step 1: Get repo links ----------
response = requests.get(base_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

repo_links = soup.select("h3 a")

repos = []

for link in repo_links:
    repos.append({
        "name": link.text.strip(),
        "url": "https://github.com" + link["href"]
    })


# ---------- Step 2: Fetch repo details FAST ----------
def fetch_details(repo):
    try:
        r = requests.get(repo["url"], headers=headers)
        s = BeautifulSoup(r.text, "html.parser")

        # description
        desc = s.select_one("p.f4")
        description = desc.text.strip() if desc else "None"

        # languages
        lang_tags = s.select("li.d-inline span[itemprop='programmingLanguage']")
        languages = [l.text.strip() for l in lang_tags]

        # stars
        stars_tag = s.select_one("a[href$='/stargazers']")
        stars = stars_tag.text.strip() if stars_tag else "0"

        return {
            "name": repo["name"],
            "repo_link": repo["url"],
            "description": description,
            "languages": languages,
            "stars": stars
        }

    except:
        return None


# ---------- Run in parallel (FAST PART) ----------
all_repos = []

with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(fetch_details, repos)

    for r in results:
        if r:
            all_repos.append(r)


# ---------- Save JSON ----------
with open("github_repos.json", "w", encoding="utf-8") as f:
    json.dump(all_repos, f, indent=4)

# ---------- Save TXT ----------
with open("github_repos.txt", "w", encoding="utf-8") as f:
    for repo in all_repos:
        f.write(f"Name: {repo['name']}\n")
        f.write(f"Link: {repo['repo_link']}\n")
        f.write(f"Description: {repo['description']}\n")
        f.write(f"Languages: {', '.join(repo['languages'])}\n")
        f.write(f"Stars: {repo['stars']}\n")
        f.write("-" * 50 + "\n")

