# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import warnings
import re
from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath('sphinxext'))
import sphinx_gallery

# -- Project information -----------------------------------------------------

project = 'Sphinx Demo'
copyright = '2021, Nathan LAUGA'
author = 'Nathan LAUGA'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # ==== SPHINX NATIVE EXT ==== #
    # automated documentation
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    
    # 
    'sphinx.ext.autosectionlabel',
    
    # link code and Documentatoon
    'sphinx.ext.viewcode',
    
    # Print LaTeX string
    'sphinx.ext.mathjax',
    
    # Handle numpy, google and rst docstring format
    'sphinx.ext.napoleon',
    
    #
    'sphinx.ext.intersphinx',
    
    # ==== EXTERNAL EXT ==== #
    # Read The Docs template 
    "sphinx_rtd_theme",
    
    # Handle Numpy docstring
    'numpydoc',
    
    # Example Gallery
    # 'sphinx_gallery.gen_gallery',
    
    # Handle notebook as page
    'nbsphinx',
    
    # Handle Markdown as page
    'recommonmark',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# The suffix of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# from sphinx_rtd_theme package
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/logo_communaute.png'
html_favicon = '_static/favicon.ico'

# === CUSTOM INDEX ===
# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {
#     'index': 'index.html',
# }  # redirects to index

# If false, no index is generated.
# html_use_index = False


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Native extensions conf --------------------------------------------------

# -- sphinx.ext.autodoc -----
# For each autodocumentated code add this default options
autodoc_default_options = {
    'members': True, 
    'inherited-members': True
}


# -- sphinx.ext.autosummary -----
# Allows autosummary generation
autosummary_generate = True
autosummary_imported_members = True


# -- External extensions conf ------------------------------------------------

# -- numpydoc -----
# Whether to create a Sphinx table of contents for the lists of class methods and attributes. 
# If a table of contents is made, Sphinx expects each entry to have a separate page.
numpydoc_class_members_toctree = False

# -- recommark -----
source_parsers = {
    '.md': CommonMarkParser,
}


# the notebook files are converted to rst.
# process_examples = True




# -- Warnings -----------------------------------------------------------------
# Ignore some warnings
warnings.filterwarnings("ignore",
                        category=UserWarning,
                        message='Matplotlib is currently using agg, which is a'
                        ' non-GUI backend, so cannot show the figure.')
suppress_warnings = ['autosectionlabel.*']