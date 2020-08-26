from github import Github
import base64
import os

g = Github(git_token)  # safer alternative, if you have an access token
u = g.get_user()

repo = u.create_repo("jd_by_api")

origin_repo = g.get_repo("songshijun007/scripts")
target_repo = g.get_repo("songshijun007/jd_by_api")

contents = origin_repo.get_contents('')

while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(origin_repo.get_contents(file_content.path))
    else:
        print(file_content)
        target_repo.create_file(path=file_content.path, 
                                content=base64.b64decode(file_content.content).decode("utf-8"), 
                                message="create")
