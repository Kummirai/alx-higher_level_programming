#!/usr/bin/python3
"""
A script that uses Basic Authentication with a personal access token to fetch your GitHub user ID.
"""
import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]  # Your GitHub username
    token = sys.argv[2]  # Your personal access token (password)

    url = 'https://api.github.com/user'
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(f"Your GitHub user ID: {user_id}")
    else:
        print(f"Error fetching user data. Status code: {response.status_code}")
