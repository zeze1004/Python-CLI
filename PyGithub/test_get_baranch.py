from github import Github
import git_pull_request as gpr
import os
from dotenv import load_dotenv
load_dotenv()

access_token = os.environ.get("access_token")

g = Github(access_token)
repo = g.get_repo("zeze1004/AWS_K8s")
for branch in repo.get_branches():
    print(branch)

