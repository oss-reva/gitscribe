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
    url = f'https://api.github.com/repos/{username}/{repo_name}/issues'
    response = requests.get(url)
    if response.status_code == 200:
        issues = response.json()
        total_issues = len(issues)
        good_first_issue_count = sum(
            1 for issue in issues if 'good first issue' in issue.get('title', '').lower())
        return total_issues, good_first_issue_count
    return None, None
