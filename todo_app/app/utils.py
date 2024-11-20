import requests
GITHUB_TOKEN = 'your_github_token'

def export_as_gist(project):

    """
    Exports project details as a secret GitHub Gist.
    """
    pending_todos = [todo for todo in project.todos if not todo.status]
    completed_todos = [todo for todo in project.todos if todo.status]

    summary=f"#{project.title}\n\n"
    summary +=f"*Summary*:{len([t for t in project.todos if t.status == 'COMPLETE'])}/{len(project.todos)} completed.\n\n"
    summary +="##Pending Todos : \n"
    summary +="".join(f"-[]{todo.description}\n"for todo in project.todos if todo.status == 'PENDING')
    summary +="\n ## Completed Todos: \n"
    summary +="".join(f"-[x]{todo.description}\n" for todo in project.todos if todo.status=='COMPLETE')
    response = requests.post(
        'https://api.github.com/gists',
        headers={'Authorization':f'token {GITHUB_TOKEN}'},
        json={
            "files":{project.title:{"content":summary}},
            "public":False
        }
    )

    if response.status_code==201:
        return response.json().get('html_url')
    else:
        raise Exception(f"Failed to create gist: {response.status_code},{response.json()}")