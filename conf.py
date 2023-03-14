from sys import path as sys_path
from os import environ
from os.path import abspath
from pathlib import Path
from json import loads


ROOT = Path(__file__).resolve().parent

sys_path.insert(0, abspath('.'))

from status import createShieldsAndStatusTable


# -- Generate Status.inc -----------------------------------------------------------------------------------------------

with (ROOT/'Status.inc').open('w') as wfptr:
	wfptr.write(createShieldsAndStatusTable())


# -- Project information -----------------------------------------------------------------------------------------------

project =   "Electronic Design Automation Abstraction"
copyright = "2016-2023 Patrick Lehmann, Unai Martinez-Corral and contributors"
author =    "Patrick Lehmann"


# -- Versioning --------------------------------------------------------------------------------------------------------

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
from subprocess import check_output

def _IsUnderGitControl():
	return (check_output(["git", "rev-parse", "--is-inside-work-tree"], universal_newlines=True).strip() == "true")

def _LatestTagName():
	return check_output(["git", "describe", "--abbrev=0", "--tags"], universal_newlines=True).strip()

# The full version, including alpha/beta/rc tags
version = "latest"  # The short X.Y version.
release = "latest"  # The full version, including alpha/beta/rc tags.
try:
	if _IsUnderGitControl:
		latestTagName = _LatestTagName()[1:]		# remove prefix "v"
		versionParts =  latestTagName.split("-")[0].split(".")

		version = ".".join(versionParts[:2])
		release = latestTagName   # ".".join(versionParts[:3])
except:
	pass


# -- Miscellaneous settings --------------------------------------------------------------------------------------------

exclude_patterns = [
	"_build",
	"_logo",
	"Thumbs.db",
	".DS_Store",
	".github",
]

master_doc = "index"


# -- Restructured Text settings ----------------------------------------------------------------------------------------

prologPath = "prolog.inc"
try:
	with open(prologPath, "r") as prologFile:
		rst_prolog = prologFile.read()
except Exception as ex:
	print("[ERROR:] While reading '{0!s}'.".format(prologPath))
	print(ex)
	rst_prolog = ""


# -- Options for HTML output -------------------------------------------------------------------------------------------

html_context = {}
ctx = ROOT / 'context.json'
if ctx.is_file():
	html_context.update(loads(ctx.open('r').read()))

html_theme = "furo"

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
    "theme_overrides.css",
]

html_theme_options = {
    "source_repository": "https://github.com/edaa-org/edaa-org.github.io",
    "source_branch": environ.get("GITHUB_REF_NAME", "main"),
    "source_directory": "",
    "sidebar_hide_name": True,
    "footer_icons": [
        {
            "name": "GitHub edaa-org/edaa-org.github.io",
            "url": "https://github.com/edaa-org/edaa-org.github.io",
            "html": "",
            "class": "fa-solid fa-brands fa-github",
        },
    ],
}

html_static_path = ['_static']

html_logo = str(Path(html_static_path[0]) / "logo" / "edaa_banner_gray.svg")
html_favicon = str(Path(html_static_path[0]) / "logo" / "edaa.svg")

htmlhelp_basename = 'EDAADoc'

html_last_updated_fmt = "%d.%m.%Y"


# -- Options for LaTeX / PDF output ------------------------------------------------------------------------------------

from textwrap import dedent

latex_elements = {
	# The paper size ('letterpaper' or 'a4paper').
	'papersize': 'a4paper',

	# The font size ('10pt', '11pt' or '12pt').
	#'pointsize': '10pt',

	# Additional stuff for the LaTeX preamble.
	'preamble': dedent(r"""
		% ================================================================================
		% User defined additional preamble code
		% ================================================================================
		% Add more Unicode characters for pdfLaTeX.
		% - Alternatively, compile with XeLaTeX or LuaLaTeX.
		% - https://github.com/sphinx-doc/sphinx/issues/3511
		%
		\ifdefined\DeclareUnicodeCharacter
			\DeclareUnicodeCharacter{2265}{$\geq$}
			\DeclareUnicodeCharacter{21D2}{$\Rightarrow$}
		\fi


		% ================================================================================
		"""),

	# Latex figure (float) alignment
	#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
	( master_doc,
		'EDAA.tex',
		'The Electronic Design Automation Abstraction Documentation',
		'Patrick Lehmann',
		'manual'
	),
]


# -- Extensions --------------------------------------------------------------------------------------------------------

extensions = [
	'sphinx.ext.extlinks',
	'sphinx.ext.intersphinx',
	'sphinx.ext.todo',
	'sphinxcontrib.bibtex',
]

bibtex_default_style = 'plain'
bibtex_bibfiles = ['refs.bib']


# -- Sphinx.Ext.InterSphinx --------------------------------------------------------------------------------------------

intersphinx_mapping = {
	'python':          ('https://docs.python.org/3', None),
	'pytooling':       ('https://pytooling.github.io/pyTooling', None),
	'cliabstraction':  ('https://pytooling.github.io/pyTooling.CLIAbstraction', None),
	'osvb':            ('https://umarcor.github.io/osvb', None),
	'ghdl':            ('https://ghdl.github.io/ghdl', None),
	'vhdlmodel':       ('https://vhdl.github.io/pyVHDLModel', None),
	'svmodel':         ('https://edaa-org.github.io/pySVModel', None),
	'projectmodel':    ('https://edaa-org.github.io/pyEDAA.ProjectModel', None),
	'ipxact':          ('https://edaa-org.github.io/pyEDAA.IPXACT', None),
	'ucis':            ('https://edaa-org.github.io/pyEDAA.UCIS', None),
	'reports':         ('https://edaa-org.github.io/pyEDAA.Reports', None),
	'outputfilter':    ('https://edaa-org.github.io/pyEDAA.OutputFilter', None),
	'clitool':         ('https://edaa-org.github.io/pyEDAA.CLITool', None),
	'toolsetup':       ('https://edaa-org.github.io/pyEDAA.ToolSetup', None),
	'launcher':        ('https://edaa-org.github.io/pyEDAA.Launcher', None),
	'siliconcompiler': ('https://docs.siliconcompiler.com/en/latest', None),
}


# -- Sphinx.Ext.ExtLinks -----------------------------------------------------------------------------------------------

extlinks = {
	'gh':      ('https://github.com/%s', 'gh:%s'),
	'ghissue': ('https://github.com/edaa-org/edaa-org.github.io/issues/%s', 'issue #%s'),
	'ghpull':  ('https://github.com/edaa-org/edaa-org.github.io/pull/%s', 'pull request #%s'),
	'ghsrc':   ('https://github.com/edaa-org/edaa-org.github.io/blob/main/%s', '%s'),
	'awesome': ('https://hdl.github.io/awesome/items/%s', '%s'),
	'pypi':    ('https://pypi.org/project/%s', 'pypi:%s')
}


# -- Sphinx.Ext.ToDo ---------------------------------------------------------------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
todo_link_only = True
