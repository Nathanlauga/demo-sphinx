.. Sphinx Demo documentation master file, created by
   sphinx-quickstart on Tue Mar 16 15:09:32 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Sphinx Demo's documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   pages/tuto.rst
   pages/whoosh.rst
   pages/my_page.md
   pages/plot_0_sin.ipynb

.. toctree::
   :maxdepth: 2
   :caption: Code
   :hidden:

   api/code.rst
   auto_examples/index.rst


What is Whoosh?
---------------

Whoosh is a fast, pure Python search engine library.

The primary design impetus of Whoosh is that it is pure Python. You should be able to
use Whoosh anywhere you can use Python, no compiler or Java required.

Like one of its ancestors, Lucene, Whoosh is not really a search engine, it's a programmer
library for creating a search engine [1]_.

Practically no important behavior of Whoosh is hard-coded. Indexing
of text, the level of information stored for each term in each field, parsing of search queries,
the types of queries allowed, scoring algorithms, etc. are all customizable, replaceable, and
extensible.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
