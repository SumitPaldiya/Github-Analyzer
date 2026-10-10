from github import Github, GithubException
from github import Auth
import os
from dotenv import load_dotenv

load_dotenv()

def github_init():
    try:
        auth = Auth.Token(os.getenv("ACCESS_TOKEN"))
        g = Github(auth=auth)

        return g
        
    except GithubException as e:
        print(f"Encountered some error: status code={e.status}")

