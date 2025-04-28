import requests
from requests.auth import HTTPBasicAuth

class BitbucketAPI:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = "https://api.bitbucket.org/2.0"
    
    def get_repositories(self, workspace):
        url = f"{self.base_url}/repositories/{workspace}"
        response = requests.get(url, auth=HTTPBasicAuth(self.username, self.password))
        return response.json()
    
    def get_commits(self, workspace, repo_slug):
        url = f"{self.base_url}/repositories/{workspace}/{repo_slug}/commits"
        response = requests.get(url, auth=HTTPBasicAuth(self.username, self.password))
        return response.json()
    
    def create_pull_request(self, workspace, repo_slug, title, source_branch, dest_branch):
        url = f"{self.base_url}/repositories/{workspace}/{repo_slug}/pullrequests"
        data = {
            "title": title,
            "source": {"branch": {"name": source_branch}},
            "destination": {"branch": {"name": dest_branch}},
        }
        response = requests.post(url, json=data, auth=HTTPBasicAuth(self.username, self.password))
        return response.json()

# Example usage
if __name__ == "__main__":
    bitbucket = BitbucketAPI("your_username", "your_password")
    repos = bitbucket.get_repositories("your_workspace")
    print(repos)
