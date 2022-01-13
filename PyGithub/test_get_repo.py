from github import Github
import os

from dotenv import load_dotenv

load_dotenv()
access_token = os.environ.get("access_token")
g = Github(access_token)

g = Github(access_token)
repo = g.get_repo("GET", "https://api.github.com/repos/zeze1004/AWS_K8s/pulls")
PRs = repo.get_pulls(state="all")
print(repo.id)
