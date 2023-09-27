import re


def format_github_info(repo_data, total_issues=None, good_first_issue_count=None, issue_data=None):
    description = repo_data['description'] or '*No description*'
    stars = repo_data['stargazers_count']
    forks = repo_data['forks_count']
    url = repo_data['html_url']

    formatted_info = (
        f"__**Repository Info**__\n"
        f"**Repository Name:** {repo_data['name']}\n"
        f"**Description:** {description}\n"
        f"**Stars:** {stars}\n"
        f"**Forks:** {forks}\n"
        f"**URL:** {url}\n"
    )

    if total_issues is not None:
        formatted_info += (
            f"**Total Issues:** {total_issues}\n"
            f"**Good First Issues:** {good_first_issue_count}\n"
        )

    if issue_data:
        title = issue_data['title']
        number = issue_data['number']
        created_by = issue_data['user']['login']
        state = 'Open' if issue_data['state'] == 'open' else 'Closed'
        assigned = issue_data['assignee']['login'] if issue_data['assignee'] else '*Not assigned*'
        description = re.sub(
            r'(https?://[^\s]+)', r'`\1`', issue_data['body'][:1000])

        formatted_info += (
            f"\n__**Issue Info**__\n"
            f"**Issue Title:** {title}\n"
            f"**Issue Number:** {number}\n"
            f"**Created By:** {created_by}\n"
            f"**Status:** {state}\n"
            f"**Assigned:** {assigned}\n"
            f"\n__**Description (Partial)**__\n{description}\n"
            f"\nFor the full description, please view the issue on GitHub."
        )

    return formatted_info
