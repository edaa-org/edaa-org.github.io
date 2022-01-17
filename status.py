from tabulate import tabulate


def statusTable():
    columns = [
        "CI:Pipeline",
        "Code",
        "Code:License",
        "Documentation",
        "Documentation:License",
        "PyPI:Tag",
        "PyPI:Status",
        "PyPI:PythonVersions",
        "Codecov:Coverage",
        "Codacy:Coverage",
        "Codacy:Quality",
        "Tag",
        "Release",
        "Date",
        "GitHub:CommitsSinceLatest",
        "GitHub:Stars",
        "GitHub:Contributors",
        "GitHub:Watchers",
        "GitHub:Forks",
        "LibrariesIO:Status",
        "LibrariesIO:Rank",
        "LibrariesIO:DependentRepos",
        "RequiresIO:Status"
    ]
    return tabulate(
        [
            ([prj] + [f"|SHIELD:svg:{prj}:{label}|" for label in columns])
            for prj in [
                "ProjectModel",
                "pyVHDLModel",
                "pySVModel",
                "Reports",
                "UCIS",
                "IPXACT",
                "OutputFilter",
                "CLITool",
                "ToolSetup",
                "Launcher"
            ]
        ],
        tablefmt="rst",
        headers=["Project"] + [label.replace(':', ' ') for label in columns]
    )


def createShield(alt, identifier, target, shield, attrs=None, isRaster=False):
    return f"""\
.. |SHIELD:{'png' if isRaster else 'svg'}:{identifier}| image:: https://{'raster' if isRaster else 'img'}.shields.io/{shield}?longCache=true&style=flat-square{"" if attrs is None else f"&{attrs}"}
   :alt: {alt}
   :height: 22
   :target: {target}
   :class: shield
"""


def createDualShields(alt, identifier, target, shield, attrs):
    content = f".. # {alt}\n"
    print(target)
    for isRaster in [False, True]:
        content += createShield(alt, identifier, target, shield, attrs, isRaster)
    return f"{content}\n"


def createProjectShields(
    label,
    identifier,
    color,
    repo=None,
    mainBranch="main",
    codacy=None
):
    colors = [
        ["c62828", "8e24aa", "0277bd", "558b2f", "ff8f00", "37474f"],
        ["ef5350", "ba68c8", "29b6f6", "9ccc65", "ffca28", "78909c"],
    ]
    darkColor = colors[0][color]
    lightColor = colors[1][color]
    repoSpace = "edaa-org" if label == "pyEDAA" else label
    repo = f"{label}.{identifier}" if repo is None else repo
    pypi = repo
    fullRepoName=f"{repoSpace}/{repo}"
    return createDualShields(
        alt="Code on GitHub",
        identifier=f"{identifier}:Code",
        shield=f"badge/{label}-{identifier}-{lightColor}",
        attrs=f"logo=github&labelColor={darkColor}",
        target=f"https://github.com/{fullRepoName}",
    ) + createDualShields(
        alt="Code license",
        identifier=f"{identifier}:Code:License",
        shield=f"pypi/l/{pypi}" if pypi is not None else "",
        attrs="logo=Apache&label=Code",
        target=f"https://github.com/{fullRepoName}/blob/{mainBranch}/LICENSE.md",
    ) + createDualShields(
        alt="Documentation (GitHub Pages) - Read Now!",
        identifier=f"{identifier}:Documentation",
        shield="website",
        attrs=f"label={repoSpace}.github.io%2F{repo}&logo=GitHub&logoColor=fff&up_color=blueviolet&up_message=Read%20now%20%E2%9E%9A&url=https%3A%2F%2F{repoSpace}.github.io%2F{repo}%2Findex.html",
        target=f"https://{repoSpace}.github.io/{repo}",
    ) + createDualShields(
        alt="Documentation License",
        identifier=f"{identifier}:Documentation:License",
        shield=f"badge/Doc-CC--BY%204.0-green",
        attrs=f"logo=CreativeCommons&logoColor=fff",
        target=f"https://github.com/{fullRepoName}/blob/{mainBranch}/doc/Doc-License.rst",
    ) + createDualShields(
        alt="GitHub Actions Pipeline",
        identifier=f"{identifier}:CI:Pipeline",
        shield=f"github/workflow/status/{fullRepoName}/Pipeline/{mainBranch}",
        attrs=f"label=Pipeline&logo=GitHub%20Actions&logoColor=FFFFFF",
        target=f"https://github.com/{fullRepoName}/actions/workflows/Pipeline.yml",
    ) + createDualShields(
        alt="GitHub - Contributors",
        identifier=f"{identifier}:GitHub:Contributors",
        shield=f"github/contributors/{fullRepoName}",
        attrs="logo=GitHub",
        target=f"https://github.com/{fullRepoName}/graphs/contributors",
    ) + createDualShields(
        alt="GitHub - Forks",
        identifier=f"{identifier}:GitHub:Forks",
        shield=f"github/forks/{fullRepoName}",
        attrs="logo=GitHub",
        target=f"https://github.com/{fullRepoName}/network/members",
    ) + createDualShields(
        alt="GitHub - Stars",
        identifier=f"{identifier}:GitHub:Stars",
        shield=f"github/stars/{fullRepoName}",
        attrs="logo=GitHub",
        target=f"https://github.com/{fullRepoName}/stargazers",
    ) + createDualShields(
        alt="GitHub - Watchers",
        identifier=f"{identifier}:GitHub:Watchers",
        shield=f"github/watchers/{fullRepoName}",
        attrs="logo=GitHub",
        target=f"https://github.com/{fullRepoName}/watchers",
    ) + createDualShields(
        alt="GitHub - Commits to branch 'dev' since latest",
        identifier=f"{identifier}:GitHub:CommitsSinceLatest",
        shield=f"github/commits-since/{fullRepoName}/latest/dev",
        attrs="logo=GitHub",
        target=f"https://github.com/{fullRepoName}/commits",
    ) + createDualShields(
        alt="GitHub Tag - latest SemVer incl. pre-release",
        identifier=f"{identifier}:Tag",
        shield=f"github/v/tag/{fullRepoName}",
        attrs="logo=GitHub&include_prereleases",
        target=f"https://github.com/{fullRepoName}/tags",
    ) + createDualShields(
        alt="GitHub Release - latest SemVer incl. including pre-releases",
        identifier=f"{identifier}:Release",
        shield=f"github/v/release/{fullRepoName}",
        attrs="logo=GitHub&include_prereleases",
        target=f"https://github.com/{fullRepoName}/releases/latest",
    ) + createDualShields(
        alt="GitHub Release Date",
        identifier=f"{identifier}:Date",
        shield=f"github/release-date/{fullRepoName}",
        attrs="logo=GitHub",
        target=f"https://github.com/{fullRepoName}/releases",
    ) + createDualShields(
        alt="PyPI - Tag",
        identifier=f"{identifier}:PyPI:Tag",
        shield=f"pypi/v/{pypi}",
        attrs="logo=PyPI&logoColor=FBE072",
        target=f"https://pypi.org/project/{pypi}",
    ) + createDualShields(
        alt="PyPI - Project Status",
        identifier=f"{identifier}:PyPI:Status",
        shield=f"pypi/status/{pypi}",
        attrs="logo=PyPI&logoColor=FBE072",
        target=f"https://pypi.org/project/{pypi}",
    ) + createDualShields(
        alt="PyPI - Python Versions",
        identifier=f"{identifier}:PyPI:PythonVersions",
        shield=f"pypi/pyversions/{pypi}",
        attrs="logo=PyPI&logoColor=FBE072",
        target=f"https://pypi.org/project/{pypi}",
    ) + createDualShields(
        alt="Codecov - Coverage",
        identifier=f"{identifier}:Codecov:Coverage",
        shield=f"codecov/c/github/{fullRepoName}",
        attrs="logo=Codecov",
        target=f"https://codecov.io/gh/{fullRepoName}",
    ) + createDualShields(
        alt="Codacy - Coverage",
        identifier=f"{identifier}:Codacy:Coverage",
        shield=f"codacy/coverage/{codacy}",
        attrs="logo=codacy",
        target=f"https://www.codacy.com/gh/{fullRepoName}",
    ) + createDualShields(
        alt="Codacy - Quality",
        identifier=f"{identifier}:Codacy:Quality",
        shield=f"codacy/grade/{codacy}",
        attrs="logo=codacy",
        target=f"https://www.codacy.com/gh/{fullRepoName}",
    ) + createDualShields(
        alt="Libraries.io - Dependencies Status",
        identifier=f"{identifier}:LibrariesIO:Status",
        shield=f"librariesio/release/pypi/{pypi}",
        attrs="logo=Libraries.io&logoColor=fff",
        target=f"https://libraries.io/github/{fullRepoName}",
    ) + createDualShields(
        alt="Libraries.io - Rank",
        identifier=f"{identifier}:LibrariesIO:Rank",
        shield=f"librariesio/sourcerank/pypi/{pypi}",
        attrs="logo=Libraries.io&logoColor=fff",
        target=f"https://libraries.io/github/{fullRepoName}/sourcerank",
    ) + createDualShields(
        alt="Libraries.io - Dependent Repos",
        identifier=f"{identifier}:LibrariesIO:DependentRepos",
        shield=f"librariesio/dependent-repos/pypi/{pypi}",
        attrs="logo=Libraries.io&logoColor=fff",
        target=f"https://github.com/{fullRepoName}/network/dependents",
    ) + createDualShields(
        alt="Requires.io - Status",
        identifier=f"{identifier}:RequiresIO:Status",
        shield=f"requires/github/{fullRepoName}",
        attrs="",
        target=f"https://requires.io/github/{fullRepoName}/requirements/?branch={mainBranch}",
    )


def createAllShields():
    return createProjectShields(
        label="pyEDAA", identifier="ProjectModel", color=1,
        codacy="c2635df20fa840bc85639ca2fa1d9cb4"
    ) + createProjectShields(
        label="VHDL", identifier="pyVHDLModel", color=2,
        repo="pyVHDLModel",
        codacy="2286426d2b11417e90010427b7fed8e7"
    ) + createProjectShields(
        label="pyEDAA", identifier="pySVModel", color=2,
        repo="pySVModel",
        codacy="39d312bf98244961975559f141c3e000"
    ) + createProjectShields(
        label="pyEDAA", identifier="Reports", color=2,
        codacy="f8142b422c1742bdba38e8ac1893870c"
    ) + createProjectShields(
        label="pyEDAA", identifier="UCIS", color=2,
        codacy="63bd2bd65585447a9f6d7ad4e7d82a35"
    ) + createProjectShields(
        label="pyEDAA", identifier="IPXACT", color=2,
        codacy="c924eeffd4cc49ed9ebbbe3a89b6fa76"
    ) + createProjectShields(
        label="pyEDAA", identifier="CLITool", color=4,
        codacy="7cc5334a04924f77ae75bbffbf48ff98"
    ) + createProjectShields(
        label="pyEDAA", identifier="OutputFilter", color=4,
        codacy="4918480c41594ffbb62f8ff98433b800"
    ) + createProjectShields(
        label="pyEDAA", identifier="ToolSetup", color=4,
        codacy="2245747238a94667b25f75970b86a333"
    ) + createProjectShields(
        label="pyEDAA", identifier="Launcher", color=4,
        codacy="83936550d5094383bb89bb117c0abbfe"
    )


def createShieldsAndStatusTable():
    return createAllShields() + statusTable()


if __name__ == '__main__':
    print(createAllShields())
