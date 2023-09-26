#!/usr/bin/env python3
import re
import discord
from discord.ext import commands

from gbot.apis.github import get_repository_info, get_issue_info, get_repo_issues
from gbot.utils import format_github_info


__all__ = ['bot']


# Bot's intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True


# Bot instance
bot = commands.Bot(
    command_prefix='!',
    intents=intents,
    disable_auto_responses=True
)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def repo(ctx, repo_link):
    # Extract the GitHub username and repository name from the link
    match = re.match(r'https://github.com/([^/]+)/([^/]+)', repo_link)
    if not match:
        await ctx.send('Invalid GitHub repo link format. Please provide a valid link.')
        return

    username, repo_name = match.group(1), match.group(2)

    repo_data = get_repository_info(username, repo_name)

    if repo_data:
        total_issues, good_first_issue_count = get_repo_issues(
            username, repo_name)
        await ctx.send(format_github_info(repo_data, total_issues, good_first_issue_count))
    else:
        await ctx.send('Repository not found or an error occurred.')


@bot.command()
async def issue(ctx, issue_link):
    # Use Regex to extract the GitHub username, repository name, and issue number from the link
    match = re.match(
        r'https://github.com/([^/]+)/([^/]+)/issues/(\d+)', issue_link)
    if not match:
        await ctx.send('Invalid GitHub issue link format. Please provide a valid link.')
        return

    username, repo_name, issue_number = match.group(
        1), match.group(2), match.group(3)

    repo_data = get_repository_info(username, repo_name)
    issue_data = get_issue_info(username, repo_name, issue_number)

    if repo_data and issue_data:
        await ctx.send(format_github_info(repo_data, None, None, issue_data))
    else:
        await ctx.send('Issue or repository not found or an error occurred.')
