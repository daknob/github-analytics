#!bin/python
# Imports
from flask import *
import requests as r
from os import getenv

# Globals
app = Flask(__name__)
REPO_U = getenv("GH_USER")
REPO_R = getenv("GH_REPO")
LABEL = getenv("GH_ISSUE_LABEL")
STATE = getenv("GH_ISSUE_STATE")
REACTION = getenv("GH_ISSUE_REACTION")
MAX_STR = getenv("GH_ISSUE_TITLE_MAX_CHARS")
ACCESS_TOKEN = getenv("GH_ACCESS_TOKEN")

# Check initialization environment
try:
    REPO = REPO_U + "/" + REPO_R
    print("Repository Loaded: " + REPO)
except:
    print("Please specify GH_USER and GH_REPO to continue.")
    exit(1)
try:
    LABEL = LABEL + ""
    print("Issue Label Loaded: " + LABEL)
except:
    print("Please specify GH_ISSUE_LABEL to continue.")
    exit(2)
try:
    STATE = STATE + ""
    print("Issue State Loaded: " + STATE)
except:
    print("Please specify GH_ISSUE_STATE to continue.")
    exit(3)
try:
    REACTION = REACTION + ""
    print("Issue Reaction Loaded: " + REACTION)
except:
    print("Please specify GH_ISSUE_REACTION to continue.")
    exit(4)
try:
    MAX_STR = int(MAX_STR)
    print("Max Title Text Loaded: " + str(MAX_STR))
except:
    MAX_STR = 25
    print("GH_ISSUE_TITLE_MAX_CHARS not set. Defaulting to 25.")
try:
    ACCESS_TOKEN = "&access_token=" + ACCESS_TOKEN
    print("Access Token Loaded.")
except:
    ACCESS_TOKEN = ""
    print(
        "GH_ACCESS_TOKEN not set. Defaulting to none. Up to 60 visits / " +
        "hour allowed."
    )


# Router
@app.route('/')
def index():

    # Get the list of all Issues
    IssueList = getIssueList()

    # Sort by most votes
    IssueList = sorted(IssueList, key=lambda k: k['votes'], reverse=True)

    # Show the page to the user
    return render_template(
        "votes.html",
        page="count",
        repo=REPO,
        label=LABEL,
        state=STATE,
        reaction=REACTION,
        issuelist=IssueList,
        ill=len(IssueList)
    )


@app.route('/vid/')
def votesById():

    # Get the list of all Issues
    IssueList = getIssueList()
    # No need to sort: they're already sorted

    # Show the page to the user
    return render_template(
        "votes.html",
        page="ids",
        repo=REPO,
        label=LABEL,
        state=STATE,
        reaction=REACTION,
        issuelist=IssueList,
        ill=len(IssueList)
    )


@app.route('/about/')
def showAbout():
    # Show the About page
    return render_template(
        "about.html",
        page="about"
    )


def getIssueList():
    # Make an API call to GitHub
    f = r.get(
        "https://api.github.com/repos/" + REPO + "/issues?labels=" +
        LABEL + "&state=" + STATE + "&per_page=100" + ACCESS_TOKEN,
        # The following is needed to the use beta API
        headers={"Accept": "application/vnd.github.squirrel-girl-preview"}
    ).json()

    # Create a blank array to store the properly formatted results here
    IssueList = []

    # For every issue returned by GitHub,
    # add it with the internal format to IssueList
    for issue in f:
        IssueList.append(
            {
                # Issue Number
                "id": issue['number'],
                # The reaction we want
                "votes": issue['reactions'][REACTION],
                # The Issue's Title
                "title": issue['title'],
                # The trimmed down Issue Title
                "shorttitle": issue['title'][0:MAX_STR],
                # The Issue URL
                "url": issue['html_url']
            }
        )

    return IssueList

# Execution
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
