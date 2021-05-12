from typing import Optional, List

from github3 import GitHub
from github3.orgs import ShortOrganization
from github3.repos import ShortRepository

from common.project import (
    project_issues_count,
    project_issues_comments_count,
    project_pull_requests_count,
    project_pull_requests_review_comments_count,
    project_merged_pull_requests_count,
    project_stargazers_count,
    project_forks_count,
    project_commits_count,
)


def organization_get_projects(session: Optional[GitHub], name: str) -> List[ShortRepository]:
    org = session.organization(name)
    return [repo for repo in org.repositories()]


def organization_issues_comments_count(organization: ShortOrganization) -> int:
    return sum(project_issues_comments_count(project) for project in list(organization.repositories()))


def organization_issues_count(organization: ShortOrganization) -> int:
    return sum(project_issues_count(project) for project in list(organization.repositories()))


def organization_pull_requests_count(organization: ShortOrganization) -> int:
    return sum(project_pull_requests_count(project) for project in list(organization.repositories()))


def organization_pull_requests_review_comments_count(organization: ShortOrganization) -> int:
    return sum(project_pull_requests_review_comments_count(project) for project in list(organization.repositories()))


def organization_merged_pull_requests_count(organization: ShortOrganization) -> int:
    return sum(project_merged_pull_requests_count(project) for project in list(organization.repositories()))


def organization_stargazers_count(organization: ShortOrganization) -> int:
    return sum(project_stargazers_count(project) for project in list(organization.repositories()))


def organization_forks_count(organization: ShortOrganization) -> int:
    return sum(project_forks_count(project) for project in list(organization.repositories()))


def organization_commits_count(organization: ShortOrganization) -> int:
    return sum(project_commits_count(project) for project in list(organization.repositories()))


def organization_contributors_count(organization: ShortOrganization) -> int:
    organization_projects = organization.repositories()
    contributors = list()
    for project in organization_projects:
        project_contributors = [contributor.id for contributor in project.contributors()]
        contributors.extend(project_contributors)
        contributors = list(set(contributors))
    return len(contributors)
