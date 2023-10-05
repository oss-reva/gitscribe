import requests


def get_repository_info(username, repo_name) -> dict:
    url = f'https://api.github.com/repos/{username}/{repo_name}'
    response = requests.get(url)

    return response.json() if response.status_code == 200 else None


def get_issue_info(username, repo_name, issue_number) -> dict:
    url = f'https://api.github.com/repos/{username}/{repo_name}/issues/{issue_number}'
    response = requests.get(url)

    return response.json() if response.status_code == 200 else None


def get_repo_issues(username, reponame, auth_token=None) -> list[dict]:
    issues = []

    page_n = 1
    while 1:
        rs = requests.get(
            url=f"https://api.github.com/repos/{username}/{reponame}/issues",
            params={
                "filter": "all",
                "per_page": 100,
                "page": page_n
            },
            headers={
                "Authorization": f"Bearer {auth_token}" if auth_token else None
            }
        )

        if rs.status_code == 200:
            sue = rs.json()

            issues.extend(sue)
            if len(sue) < 100:
                break
        else:
            break

        page_n += 1
    return issues


def issue_get_labels(issue: dict) -> dict:
    rs = {
        "labels": []
    }

    if issue.get("labels"):
        rs["labels"] = [l["name"] for l in issue["labels"]]

    return rs


def issues_label_stats(issues: list[dict]) -> dict:
    rs = {}

    for i in issues:
        for l in issue_get_labels(i):
            if l not in rs:
                rs[l] = 0
            rs[l] += 1
    return rs
