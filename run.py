from github3 import login

from common.organization import (
    organization_issues_comments_count,
    organization_issues_count,
    organization_pull_requests_count,
    organization_pull_requests_review_comments_count,
    organization_merged_pull_requests_count,
    organization_stargazers_count,
    organization_forks_count, organization_commits_count,
)

UBUNTUKYLINORGANIZATIONANALYSIS_TOKEN = "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"

if __name__ == '__main__':
    gitHub = login(token=UBUNTUKYLINORGANIZATIONANALYSIS_TOKEN)
    ukuiOrganization = gitHub.organization('ukui')
    ubuntuKylinOrganization = gitHub.organization('UbuntuKylin')

    print("UKUI:")
    print("Issues comments: " + str(organization_issues_comments_count(ukuiOrganization)))
    print("Open Issues: " + str(organization_issues_count(ukuiOrganization)))
    print("Pull Requests: " + str(organization_pull_requests_count(ukuiOrganization)))
    print("Pull Requests review comments: " + str(organization_pull_requests_review_comments_count(ukuiOrganization)))
    print("Merged Pull Requests: " + str(organization_merged_pull_requests_count(ukuiOrganization)))
    print("Stargazers: " + str(organization_stargazers_count(ukuiOrganization)))
    print("Forks: " + str(organization_forks_count(ukuiOrganization)))
    print("Commits: " + str(organization_commits_count(ukuiOrganization)))

    print("Ubuntu Kylin:")
    print("Issues comments: " + str(organization_issues_comments_count(ubuntuKylinOrganization)))
    print("Open Issues: " + str(organization_issues_count(ubuntuKylinOrganization)))
    print("Pull Requests: " + str(organization_pull_requests_count(ubuntuKylinOrganization)))
    print("Pull Requests review comments: " + str(
        organization_pull_requests_review_comments_count(ubuntuKylinOrganization)))
    print("Merged Pull Requests: " + str(organization_merged_pull_requests_count(ubuntuKylinOrganization)))
    print("Stargazers: " + str(organization_stargazers_count(ubuntuKylinOrganization)))
    print("Forks: " + str(organization_forks_count(ubuntuKylinOrganization)))
    print("Commits: " + str(organization_commits_count(ubuntuKylinOrganization)))
