from sys import path as sys_path
from os.path import abspath
from pathlib import Path
from json import loads


ROOT = Path(__file__).resolve().parent

sys_path.insert(0, abspath('.'))


# ==============================================================================
# Project information
# ==============================================================================
project =   "Electronic Design Automation Abstraction"
copyright = "2016-2021 Patrick Lehmann, Unai Martinez-Corral and contributors"
author =    "Patrick Lehmann"


# ==============================================================================
# Versioning
# ==============================================================================
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


# ==============================================================================
# Miscellaneous settings
# ==============================================================================
# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
	"_build",
	"_logo",
	"_themes",
	"Thumbs.db",
	".DS_Store",
	".github",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'stata-dark'


# ==============================================================================
# Restructured Text settings
# ==============================================================================
prologPath = "prolog.inc"
try:
	with open(prologPath, "r") as prologFile:
		rst_prolog = prologFile.read()
except Exception as ex:
	print("[ERROR:] While reading '{0!s}'.".format(prologPath))
	print(ex)
	rst_prolog = ""


# ==============================================================================
# Options for HTML output
# ==============================================================================

html_context = {}
ctx = ROOT / 'context.json'
if ctx.is_file():
	html_context.update(loads(ctx.open('r').read()))

if (ROOT / "_theme").is_dir():
	html_theme_path = ["."]
	html_theme = "_theme"
	html_theme_options = {
		'logo_only': True,
		'home_breadcrumbs': False,
		'vcs_pageview_mode': 'blob',
	}
	html_css_files = [
		'theme_overrides.css',
	]
else:
	html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = str(Path(html_static_path[0]) / "logo" / "edaa_banner_white.svg")
html_favicon = str(Path(html_static_path[0]) / "logo" / "edaa.svg")

# Output file base name for HTML help builder.
htmlhelp_basename = 'EDAADoc'

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
html_last_updated_fmt = "%d.%m.%Y"


# ==============================================================================
# Options for LaTeX / PDF output
# ==============================================================================
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


# ==============================================================================
# Extensions
# ==============================================================================
extensions = [
# Standard Sphinx extensions
	'sphinx.ext.extlinks',
	'sphinx.ext.intersphinx',
	'sphinx.ext.todo',
	'sphinxcontrib.bibtex',
# Local extensions
	'exec',
]

bibtex_default_style = 'plain'
bibtex_bibfiles = ['refs.bib']


# ==============================================================================
# Sphinx.Ext.InterSphinx
# ==============================================================================
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


# ==============================================================================
# Sphinx.Ext.ExtLinks
# ==============================================================================
extlinks = {
	'ghrepo':  ('https://github.com/%s', ''),
	'ghissue': ('https://github.com/edaa-org/edaa-org.github.io/issues/%s', 'issue #'),
	'ghpull':  ('https://github.com/edaa-org/edaa-org.github.io/pull/%s', 'pull request #'),
	'ghsrc':   ('https://github.com/edaa-org/edaa-org.github.io/blob/main/%s', ''),
	'awesome': ('https://hdl.github.io/awesome/items/%s', ''),
}


# ==============================================================================
# Sphinx.Ext.ToDo
# ==============================================================================
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
todo_link_only = True
