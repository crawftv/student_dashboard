import requests
import re

students = [
    "will-cotton-4",
    "Rice-from-data",
    "NicoMontoya",
    "Nolanole",
    "TheJoys2019",
    "danhorsley",
    "mkirby1995",
]


def get_repos(student):
    r = requests.get("https://api.github.com/users/" + student + "/repos")
    return r


def get_sha(student, repo_name):
    sha = requests.get(
        "https://api.github.com/repos/" + student + "/" + repo_name + "/commits"
    )
    sha = sha.json()[0]["sha"]
    return sha


def get_files(student, repo_name, sha):
    tree = requests.get(
        "https://api.github.com/repos/"
        + student
        + "/"
        + repo_name
        + "/git/trees/"
        + sha
        + "?recursive=1"
    )
    tree = tree.json()
    tree = [t["path"] for t in tree["tree"]]
    tree = check_file_type(tree)
    return tree


def check_file_type(list_string):
    new_list = []
    for s in list_string:
        if re.match(r"^.*(node_modules|solutions|elm-stuff)", s):
            pass
        elif re.match(r"^.*\.(py|ipynb)", s):
            new_list.append(s)
    return new_list
