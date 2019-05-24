#!/usr/local/bin/python3
from git.repo import Repo
import os

def clone_git_repo(git_url):
    '''
    Name    : clone_git_repo
    Input   : git_url - url for the git repository
    Ouptput : None
    Description: This function takes git url and local path as input and clone the git repo to that local dir
    '''
    #BASE CASE
    #check for empty input
    if not len(git_url):
        print('Empty git repo url.Please enter a valid git url')
        return
    #clone the repo
    try:
        print('Git clone is in progress...')
        #local code repo path
        repo_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'git_code_repo')
        if not os.path.isdir(repo_dir):
            os.mkdir(repo_dir)
        #clone the repo
        Repo.clone_from(git_url, repo_dir)
        print('{giturl} is cloned succesfully to {repodir}'.format(giturl=git_url,repodir=repo_dir))
    except Exception as e:
        print('Git clone failed with error - {error} - for giturl:{giturl}'.format(error=e,giturl=git_url))


def main():
    git_url = input('Input git url of the repo -') #'https://github.com/palakrishnateja/JDA_PROGRAMMING_ASSESMENT.git'
    clone_git_repo(git_url)

if __name__ == '__main__':
    main()
    