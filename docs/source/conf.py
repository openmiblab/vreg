from pathlib import Path

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'vreg'
copyright = '2024-2025, vreg maintainers'
author = 'vreg maintainers'
release = '0.0.10'

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

# -- pyvista configuration ---------------------------------------------------
import pyvista

# necessary when building the sphinx gallery
pyvista.BUILDING_GALLERY = True
os.environ['PYVISTA_BUILDING_GALLERY'] = 'true'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones
extensions = [
    'sphinx.ext.napoleon', # parsing of NumPy and Google style docstrings
    'sphinx.ext.autodoc', # sphinx autodocumentation generation
    'sphinx.ext.autosummary', # generates function/method/attribute summary lists
    'sphinx.ext.viewcode', # viewing source code
    'sphinx.ext.intersphinx', # generate links to the documentation of objects in external projects
    'autodocsumm',
    'myst_parser', # parser for markdown language
    'sphinx_copybutton', # copy button for code blocks
    'sphinx_design', # sphinx web design components
    #'sphinx_remove_toctrees', # selectively remove toctree objects from pages
    'sphinx_gallery.gen_gallery', # thumbnail galleries
    'sphinx_exec_code', # To execute code in rst files.

    # Cannot be used together with pyvista plot directive at the moment
    # Use pyvista to show matplotlib plots in docstrings
    # https://github.com/pyvista/pyvista/discussions/5951
    # 'matplotlib.sphinxext.plot_directive', # to show plots in docstrings

    #generate static and interactive scenes of pyvista plots
    "pyvista.ext.plot_directive",
    "pyvista.ext.viewer_directive",
]



# Settings for sphinx-gallery, see
# https://sphinx-gallery.github.io/stable/getting_started.html#create-simple-gallery


sphinx_gallery_conf = {
    # path to the example scripts relative to conf.py
    'examples_dirs': '../examples',   

    # path to where to save gallery generated output
    'gallery_dirs': 'generated/examples',  
    
    # directory where function/class granular galleries are stored
    'backreferences_dir': 'generated/backreferences',

    # Modules for which function/class level galleries are created. 
    'doc_module': ('vreg', ),

    # objects to exclude from implicit backreferences. The default option
    # is an empty set, i.e. exclude nothing.
    'exclude_implicit_doc': {},

    # thumbnail for examples that do not generate any plot
    #'default_thumb_file': '_static/tristan-logo.jpg',

    # Disabling download button of all scripts
    'download_all_examples': False,

    # Default setting disables animations. Set to True to enable
    'matplotlib_animations': (True, 'jshtml'),

    # Image scrapers are plugins that allow Sphinx-Gallery to detect images
    'image_scrapers': ('pyvista', 'matplotlib'),
}

# This way a link to other methods, classes, or modules can be made with back ticks so that you don't have to use qualifiers like :class:, :func:, :meth: and the likes
default_role = 'obj'

# Add any paths that contain templates here, relative to this directory
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path
exclude_patterns = []

# show syntax color coding for code samples
#pygments_style = 'sphinx'

# -- Extension configuration -------------------------------------------------
# Map intersphinx to pre-existing documentation from other projects used in this project
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    #'matplotlib': ('https://matplotlib.org/stable/', None),
    #'pydicom': ('https://pydicom.github.io/pydicom/stable/', None),
    #'nibabel': ('https://nipy.org/nibabel/', None),
    #'pandas': ('https://pandas.pydata.org/docs/', None),
    #'skimage': ('https://scikit-image.org/docs/stable/', None),
    "scipy": ('https://docs.scipy.org/doc/scipy/', None),
}

autosummary_generate = True # enable autosummary extension

# Tell sphinx-autodoc-typehints to generate stub parameter annotations including types, even if the parameters aren't explicitly documented.
always_document_param_types = True

# Remove auto-generated API docs from sidebars.
#remove_from_toctrees = ["_autosummary/*"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of builtin themes
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "github_url": "https://github.com/QIB-Sheffield/vreg",
    "collapse_navigation": True,
    }

# Add any paths that contain custom static files (such as style sheets) here, relative to this directory. They are copied after the builtin static files, so a file named "default.css" will overwrite the builtin "default.css"
html_static_path = ['_static']

# Add anyc CSS files placed in _static here so they can be found when building the documentation
html_css_files = [
    'teams.css', # templates for the teams mosaic in About
]

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/ibeat-logo.png'

# The base URL which points to the root of the HTML documentation. 
# It is used to indicate the location of document
# html_baseurl = "https://qib-sheffield.github.io/vreg/"

# Autodoc configuration
# autoclass_content = 'both'  # Direct autoclass to include both Class and __init__ doc strings 

# Instruction to autoclass: do NOT document __init__
autodoc_default_flags = ['members', 'private-members', 'special-members','show-inheritance']

def autodoc_skip_member(app, what, name, obj, skip, options):
    # Ref: https://stackoverflow.com/a/21449475/
    # return True if (skip or exclude) else None  # Can interfere with subsequent skip functions.
    exclude = ['__init__']
    return True if name in exclude else None
 
def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)
    app.add_css_file("custom.css")
