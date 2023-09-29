import requests


def get_repository_info(username, repo_name):
    url = f'https://api.github.com/repos/{username}/{repo_name}'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None


def get_issue_info(username, repo_name, issue_number):
    url = f'https://api.github.com/repos/{username}/{repo_name}/issues/{issue_number}'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None


def get_repo_issues(username, repo_name):
   label_name ='good%20first%20issue'
    url = f'https://api.github.com/repos/{username}/{repo_name}/issues?labels={label_name}'
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        issues = response.json()   
        print(issues)
        total_issues=0
        good_first_issue_count=0
        for issue in issues:
            for label in issue["labels"]:
                 description = label["description"]
                 if "good for newcomers" in description.lower():
                       good_first_issue_count += 1
        return total_issues,good_first_issue_count
    return None, None
