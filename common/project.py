from typing import List
from github3.issues import ShortIssue
from github3.pulls import ShortPullRequest
from github3.repos import ShortRepository


def project_get_issues(repo: ShortRepository) -> List[ShortIssue]:
    return list(repo.issues(state='all'))


def project_get_pull_requests(repo: ShortRepository) -> List[ShortPullRequest]:
    return list(repo.pull_requests(state='all'))


def project_get_merged_pull_requests(repo: ShortRepository) -> List[ShortPullRequest]:
    return list(repo.pull_requests(state='closed'))


def project_issues_count(repo: ShortRepository) -> int:
    return len(project_get_issues(repo))


def project_pull_requests_count(repo: ShortRepository) -> int:
    return len(project_get_pull_requests(repo))


def project_merged_pull_requests_count(repo: ShortRepository) -> int:
    return len(project_get_merged_pull_requests(repo))


def project_stargazers_count(repo: ShortRepository) -> int:
    return repo.stargazers_count


def project_forks_count(repo: ShortRepository) -> int:
    return repo.forks_count


def project_issues_comments_count(repo: ShortRepository) -> int:
    return sum(issue.comments_count for issue in project_get_issues(repo))


def project_pull_requests_review_comments_count(repo: ShortRepository) -> int:
    return sum(len(list(pull_request.review_comments())) for pull_request in project_get_pull_requests(repo))


def project_commits_count(repo: ShortRepository) -> int:
    return len([commit for commit in repo.commits()])
