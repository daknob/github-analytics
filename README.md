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
