import os

def everything():
    os.system("git add *")
    commit_msg = input("Enter Commit Message:")
    os.system("git commit -m" + '"' + commit_msg + '"')
    os.system("git push --all")


everything()