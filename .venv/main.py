import requests

response = requests.get("https://api.github.com/repos/wijamw/api-request")
projects = response.json()

# Menampilkan informasi proyek
print(f"repo ID: {projects['id']}")
print(f"Owner ID: {projects['owner']['id']}")
print(f"Git URL: {projects['git_url']}")

