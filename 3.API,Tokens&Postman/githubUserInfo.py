import requests

# Public GitHub API endpoint
url = "https://api.github.com/users/Harsh21-design"  

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  
    print("GitHub User Information:")
    print(f"Login: {data['login']}")
    print(f"ID: {data['id']}")
    print(f"Name: {data['name']}")
    print(f"Public Repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
    print(f"Following: {data['following']}")
else:
    print("Error:", response.status_code)
