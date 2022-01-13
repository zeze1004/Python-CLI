from github import Github
import os

from dotenv import load_dotenv

load_dotenv()
access_token = os.environ.get("access_token")
g = Github(access_token)

# Github Enterprise with custom hostname
g = Github(login_or_token=access_token)
for repo in g.get_user().get_repos():
    print(repo.name)

