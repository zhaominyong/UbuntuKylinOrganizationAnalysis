from github3 import login

UBUNTUKYLINORGANIZATIONANALYSIS_TOKEN = "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"

if __name__ == '__main__':
    gitHub = login(token=UBUNTUKYLINORGANIZATIONANALYSIS_TOKEN)
    ukuiOrganization = gitHub.organization('ukui')
    ubuntuKylinOrganization = gitHub.organization('UbuntuKylin')

    ukuiProjects = [repo for repo in ukuiOrganization.repositories()]
    ubuntuKylinOrganizationProjects = [repo for repo in ubuntuKylinOrganization.repositories()]

    contributors = list()

    for project in ukuiProjects:
        projectContributors = [contributor.id for contributor in project.contributors()]
        contributors.extend(projectContributors)
        contributors = list(set(contributors))

    print("UKUI Contributors: " + str(len(contributors)))

    contributors = list()

    for project in ubuntuKylinOrganizationProjects:
        projectContributors = [contributor.id for contributor in project.contributors()]
        contributors.extend(projectContributors)
        contributors = list(set(contributors))

    print("Ubuntu Kylin Contributors: " + str(len(contributors)))
