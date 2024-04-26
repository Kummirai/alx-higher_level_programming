#!/usr/bin/python3
"""
A script that fetches the 10 most recent commits from the "rails" repository by the user "rails".
Prints each commit in the format: <sha>: <author name>
"""
import requests
import sys

if __name__ == '__main__':
    repo_name = sys.argv[1]  # Repository name (e.g., "rails")
    owner_name = sys.argv[2]  # Owner name (e.g., "rails")

    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]  # Get the 10 most recent commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error fetching commits. Status code: {response.status_code}")
