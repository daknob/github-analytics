# GitHub Analytics

GitHub Analytics is an Open Source Tool available on GitHub.
It has been created by Antonios A. Chariton for the DevStaff
community in Crete, Greece. It is written in Python, using
Flask. The original GitHub Analytics was written by @kabitakis
and was in NodeJS.

The main difference between the two versions is that this
one uses the new GitHub Reactions, while Nikos' searches for
a substring in every issue comment. That means this one is
much faster since it only makes one single request to GitHub,
as opposed to as many requests as there are issues.

However, this speed benefit comes at a cost: the Reactions
API is still in beta, and therefore it may stop working or
change at any time. That means this tool may also stop
functioning and comes without any warranty, express or implied.
The developer(s) will do as much as they can to support this
software, however time and resources are limited. If you see
the software misbehaving, please open an issue on GitHub.

## Installation
You can install GitHub Analytics either directly or in a
`virtualenv`. In order to do that, you need to run:

```
git clone https://github.com/DaKnOb/github-analytics.git
cd github-analytics
pip install -r requirements.txt
```

## Running GitHub Analytics
In order to run GitHub Analytics, it is recommended to
use a production web server and not the built-in one
that is included by Flask. This is crucial, since by default,
Development mode is activated. There's nothing out of the
ordinary when running the software since it is pretty
simple.

### Docker
You can run GitHub Analytics by using `docker` to avoid
downloading and installing anything. A `Dockerfile` is
included in the repository but the built image is also
available on DockerHub. To run it, simply execute:

```
docker run -p 80:80 -e 'GH_ISSUE_TITLE_MAX_CHARS=20' [...] daknob/github-analytics
```

## Environment Variables
For the successful execution of GitHub Analytics, some
Environment Variables are required. In no particular order,
they are:

* `GH_USER`: The user / organization that owns the GitHub
Repository to monitor.
* `GH_REPO`: A repository of `GH_USER` that GitHub Analytics
will work in.
* `GH_ISSUE_LABEL`: A specific label to filter issues by.
* `GH_ISSUE_STATE`: A state of an issue to filter by (i.e. 'open').
* `GH_ISSUE_REACTION`: The reaction to count. Currently `+1`, `-1`,
`heart`, `confused`, `hooray`, `laugh`.
* `GH_ISSUE_TITLE_MAX_CHARS`: An optional environment variable that
limits the characters of the issues' titles to include in the chart.
* `GH_ACCESS_TOKEN`: An optional variable. You can set a GitHub Personal
Access Token here to increase the rate limit from 60 r/hr to 5000 r/hr.
