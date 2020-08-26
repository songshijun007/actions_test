from github import Github
import base64
import os

git_token = os.environ["git_token"]

g = Github(git_token)  # safer alternative, if you have an access token
u = g.get_user()

repo = u.create_repo("jd_by_api")

origin_repo = g.get_repo("songshijun007/scripts")
target_repo = g.get_repo("songshijun007/jd_by_api")

contents = origin_repo.get_contents('')
workflows_contents = origin_repo.get_contents('.github/workflows')
icon_contents = origin_repo.get_contents('icon')

# while contents:
#     file_content = contents.pop(0)
#     if file_content.type == "dir":
#         contents.extend(origin_repo.get_contents(file_content.path))
#     else:
#         print(file_content)
#         target_repo.create_file(path=file_content.path, 
#                                 content=base64.b64decode(file_content.content).decode("utf-8"), 
#                                 message="create")
for content_ in contents:
    try:
        if content_.content:
            target_repo.create_file(path=content_.path, 
                                    content=base64.b64decode(content_.content).decode("utf-8"), 
                                    message="create")
    except Exception as e:
        print(content_)
        print(e)

for content_ in workflows_contents:
    try:
        if content_.content:
            target_repo.create_file(path=content_.path, 
                                    content=base64.b64decode(content_.content).decode("utf-8"), 
                                    message="create")
    except Exception as e:
        print(content_)
        print(e)
        
for content_ in icon_contents:
    try:
        if content_.content:
            target_repo.create_file(path=content_.path, 
                                    content=base64.b64decode(content_.content).decode("gbk"), 
                                    message="create")
    except Exception as e:
        print(content_)
        print(e)
        
for content_ in icon_contents:
    try:
        if content_.content:
            target_repo.create_file(path=content_.path, 
                                    content=base64.b64decode(content_.content).decode("gbk"), 
                                    message="create")
    except Exception as e:
        print(content_)
        print(1)
        print(e)
