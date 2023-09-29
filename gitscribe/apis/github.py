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
    LABEL_NAME ='good%20first%20issue'
    first_good_issue_url = f'https://api.github.com/repos/{username}/{repo_name}/issues?labels={LABEL_NAME}'
    response = requests.get(first_good_issue_url)
    #print(response)
    if response.status_code == 200:
        #for getting total number of issue with label 'good first issue' in respective repo
        json_data = response.json()   
        good_first_issue_count=0
        page=1
        while True: 
            first_good_issue_url = f'https://api.github.com/repos/{username}/{repo_name}/issues?labels={LABEL_NAME}&page={page}'
            response = requests.get(first_good_issue_url)
            json_data = response.json()   
            for issue in json_data:
                 labels = issue.get('labels', [])
                 for label in labels:
                    if label.get('name') == 'good first issue':
                        good_first_issue_count += 1
            if len(json_data)<30:
              break
            page += 1
        print("Total open first_good_issues:",good_first_issue_count)
        ##number of pull request
        total_pull_requests = 0
        page = 1
        while True:
            pulls_url = f'https://api.github.com/repos/{username}/{repo_name}/pulls?page={page}'
            response=requests.get(pulls_url)
            if response.status_code == 200:
                pull_requests = response.json()
                page_pull_request_count = len(pull_requests)
                total_pull_requests += page_pull_request_count
                if page_pull_request_count < 30:
                    break
                page += 1
       # print(total_pull_requests)
        #for getting number number of issue in respective repo
        open_issues1 = 0
        page = 1
        while True:
              open_issue_url = f'https://api.github.com/repos/{username}/{repo_name}/issues?state=open&page={page}'
              session1 = requests.Session()
              response = session1.get(open_issue_url)
              if response.status_code == 200:
                   json_data = response.json()
                   open_issues1 += len(json_data)
                   if len(json_data) < 30:
                          break
                   page += 1
              else:
                 print(f'Failed to fetch data from GitHub API. Status code: {response.status_code}')
                 break
        total_issue=open_issues1-total_pull_requests
        print(f'Total open_issues in {total_issue}')
        return total_issue,good_first_issue_count
    return None, None

