#!/usr/bin/env python3
import re
import discord
from discord.ext import commands
from discord import app_commands
from gitscribe.apis.github import get_repository_info, get_issue_info, get_repo_issues
from gitscribe.utils import format_github_info


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

    for guild in bot.guilds:
        try:
            synced = await bot.tree.sync()
            
        except Exception as e:
            print(str(e))
        

@bot.event
async def on_message(message):  
    if message.author.id == bot.user.id:
        return           
    await bot.process_commands(message)


# Hybrid commands
@bot.hybrid_command(name="repo", with_app_command=True, description="Create wallets for all members (initialize)")
async def repo(ctx: commands.Context, repo_link):
    # In case of prefixed command repo_link can be null
    if not repo_link:
        await ctx.send('Please provide a valid repo link')
        return 
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


@bot.hybrid_command(name="issue", with_app_command=True, description="Get info about an issue")
async def issue(ctx: commands.Context, issue_link):

    # In case of prefixed command issue_link can be null
    if not issue_link:
        await ctx.send('Please provide a valid repo link')
        return
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


# Error handling
@bot.event   
async def on_command_error(ctx, error):
    print(error)
    embed = discord.Embed(title=error, color=0x00ff00)
    await ctx.send(embed=embed)