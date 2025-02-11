import datetime

import jupyter_forward


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'myst_nb',
    'sphinxext.opengraph',
    'sphinx_copybutton',
    'sphinx_inline_tabs',
]


autodoc_member_order = 'groupwise'

# MyST config
myst_enable_extensions = ['amsmath', 'colon_fence', 'deflist', 'html_image']
myst_url_schemes = ['http', 'https', 'mailto']

jupyter_execute_notebooks = 'cache'
execution_timeout = 600
execution_allow_errors = True

# sphinx-copybutton configurations
copybutton_prompt_text = r'>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: '
copybutton_prompt_is_regexp = True

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = []
autodoc_typehints = 'none'
autodoc_preserve_defaults = True

# Napoleon configurations

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = False
napoleon_use_rtype = False
napoleon_preprocess_types = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = 'index'

# General information about the project.
current_year = datetime.datetime.now().year
project = 'jupyter-forward'
copyright = f'2020-{current_year}, the jupyter-forward development team'
author = 'jupyter-forward developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = jupyter_forward.__version__.split('+')[0]
# The full version, including alpha/beta/rc tags.
release = jupyter_forward.__version__


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'Thumbs.db', '.DS_Store']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'furo'
html_title = ''

html_context = {
    'github_user': 'NCAR',
    'github_repo': 'jupyter-forward',
    'github_version': 'main',
    'doc_path': 'docs',
}
html_theme_options = dict()


# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '../_static/images/NSF_4-Color_bitmap_Logo.png'

html_static_path = ['../_static']

html_last_updated_fmt = '%b %d, %Y'


# Output file base name for HTML help builder.
htmlhelp_basename = 'jupyter_forwarddoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}


latex_documents = [
    ('index', 'jupyter-forward.tex', 'jupyter-forward Documentation', author, 'manual')
]

man_pages = [('index', 'jupyter-forward', 'jupyter-forward Documentation', [author], 1)]

texinfo_documents = [
    (
        'index',
        'jupyter-forward',
        'jupyter-forward Documentation',
        author,
        'jupyter-forward',
        'One line description of project.',
        'Miscellaneous',
    )
]


intersphinx_mapping = {'python': ('https://docs.python.org/3/', None)}
