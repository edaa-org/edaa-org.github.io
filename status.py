import re
from tabulate import tabulate


def statusTable():
    labels = ["github", "src-license", "ghp-doc", "doc-license", "tag", "release", "date"]
    return tabulate(
        [
            ([prj] + [f"|SHIELD:svg:{prj}-{label}|" for label in labels])
            for prj in ["pyVHDLModel", "pySVModel", "Reports", "IPXACT", "ProjectModel"]
        ],
        tablefmt="rst",
        headers=["Project"] + labels
    )


def createShield(identifier, alt, target, shield, attrs=None, isRaster=False):
    return f"""\
.. |SHIELD:{'png' if isRaster else 'svg'}:{identifier}| image:: https://{'raster' if isRaster else 'img'}.shields.io/{shield}?longCache=true&style=flat-square{"" if attrs is None else f"&{attrs}"}
   :alt: {alt}
   :height: 22
   :target: {target}
   :class: shield
"""


def createDualShields(comment, identifier, alt, target, shield, attrs):
    content = f".. # {comment}\n"
    print(target)
    for isRaster in [False, True]:
        content += createShield(identifier, alt, target, shield, attrs, isRaster)
    return f"{content}\n"


def createProjectShields(
    identifier,
    label,
    content,
    repoSpace,
    repoName,
    darkColor,
    lightColor,
    mainBranch,
    pypi=None
):
    fullRepoName=f"{repoSpace}/{repoName}"
    return createDualShields(
        comment="Sourcecode link to GitHub",
        identifier=f"{identifier}-github",
        alt="Sourcecode on GitHub",
        target=f"https://github.com/{fullRepoName}",
        shield=f"badge/{label}-{content}-{lightColor}",
        attrs=f"logo=github&labelColor={darkColor}"
    ) + createDualShields(
        comment="Sourcecode license",
        identifier=f"{identifier}-src-license",
        alt="Code license",
        target=f"https://github.com/{fullRepoName}/blob/{mainBranch}/LICENSE.md",
        shield=f"pypi/l/{pypi}" if pypi is not None else "",
        attrs="logo=Apache&label=code%20license",
    ) + createDualShields(
        comment="GitHub tag",
        identifier=f"{identifier}-tag",
        alt="GitHub tag - latest SemVer incl. pre-release",
        target=f"https://github.com/{fullRepoName}/tags",
        shield=f"github/v/tag/{fullRepoName}",
        attrs="logo=GitHub&include_prereleases"
    ) + createDualShields(
        comment="GitHub release",
        identifier=f"{identifier}-release",
        alt="GitHub release - latest SemVer incl. including pre-releases",
        target=f"https://github.com/{fullRepoName}/releases/latest",
        shield=f"github/v/release/{fullRepoName}",
        attrs="logo=GitHub&include_prereleases"
    ) + createDualShields(
        comment="GitHub release date",
        identifier=f"{identifier}-date",
        alt="GitHub release date",
        target=f"https://github.com/{fullRepoName}/releases",
        shield=f"github/release-date/{fullRepoName}",
        attrs="logo=GitHub"
    ) + createDualShields(
        comment="GHPages - read now",
        identifier=f"{identifier}-ghp-doc",
        alt="Documentation - Read Now!",
        target=f"https://{repoSpace}.github.io/{repoName}",
        shield="website",
        attrs=f"label={repoSpace}.github.io%2F{repoName}&logo=GitHub&logoColor=fff&up_color=blueviolet&up_message=Read%20now%20%E2%9E%9A&url=https%3A%2F%2F{repoSpace}.github.io%2F{repoName}%2Findex.html"
    ) + createDualShields(
        comment="Documentation license",
        identifier=f"{identifier}-doc-license",
        alt="Documentation License",
        target=f"https://github.com/{fullRepoName}/blob/{mainBranch}/doc/Doc-License.rst",
        shield=f"badge/doc%20license-CC--BY%204.0-green",
        attrs=f"logo=CreativeCommons&logoColor=fff"
    )


def createAllShields():
    return createProjectShields(
        identifier="pyVHDLModel",
        label="VHDL",
        content="pyVHDLModel",
        repoSpace="VHDL",
        repoName="pyVHDLModel",
        darkColor="0277bd",
        lightColor="29b6f6",
        mainBranch="master",
        pypi="pyVHDLModel",
    ) + createProjectShields(
        identifier="pySVModel",
        label="pyEDAA",
        content="pySVModel",
        repoSpace="edaa-org",
        repoName="pySVModel",
        darkColor="0277bd",
        lightColor="29b6f6",
        mainBranch="main",
        pypi="pySVModel",
    ) + createProjectShields(
        identifier="Reports",
        label="pyEDAA",
        content="Reports",
        repoSpace="edaa-org",
        repoName="pyEDAA.Reports",
        darkColor="0277bd",
        lightColor="29b6f6",
        mainBranch="master",
    ) + createProjectShields(
        identifier="IPXACT",
        label="pyEDAA",
        content="IPXACT",
        repoSpace="edaa-org",
        repoName="pyEDAA.IPXACT",
        darkColor="0277bd",
        lightColor="29b6f6",
        mainBranch="master",
    ) + createProjectShields(
        identifier="ProjectModel",
        label="pyEDAA",
        content="ProjectModel",
        repoSpace="edaa-org",
        repoName="pyEDAA.ProjectModel",
        darkColor="6a1b9a",
        lightColor="ab47bc",
        mainBranch="master",
        pypi="pyEDAA.ProjectModel",
    )


def createShieldsAndStatusTable():
    return createAllShields() + statusTable()


if __name__ == '__main__':
    print(createAllShields())
