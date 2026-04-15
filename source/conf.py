# Configuration file for the Sphinx documentation builder.

project = 'はじめてのPython勉強会'
copyright = '2026'
author = 'Makino'
release = '1.0'

extensions = [
    'sphinxcontrib.mermaid',
    'sphinx_nekochan',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ja'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_title = 'はじめてのPython勉強会'
