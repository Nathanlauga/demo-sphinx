How to create an advanced Sphinx page
#####################################

``reStructured Text`` Basics
****************************

Headings
========

.. code-block:: RST

    Heading 1
    ###########

    The top level heading on any file, underscored by #. use for the topic title.

    Heading 2
    **********

    The second level heading in a topic. Use for high-level concepts, tasks, or
    reference information.

    Heading 3
    ===========

    The 3rd level heading in a topic. Use for breaking down conceptual
    information into understandable chunks.


Table of Contents
=================

.. code-block:: RST

    .. toctree::
    :maxdepth: 2

    my_page.rst


Links
=====

.. code-block:: RST

    Get the latest news at `CNN`_.

    .. _CNN: http://cnn.com/

.. code-block:: RST

    `CNN <http://cnn.com>`_


Add images
==========

.. code-block:: RST

    .. image:: path/filename.png
    :width: 400
    :alt: Alternative text

Add code
========

.. code-block:: RST

    .. code-block:: language

    code

For example with a python code :

.. code-block:: Python

    def add(a: float, b: float):
        """Returns a+b
        """
        return a + b


Going further
*************

If you need more informations I recommend this website : `Create Documentation with RST, Sphinx, Sublime, and GitHub`_

.. _`Create Documentation with RST, Sphinx, Sublime, and GitHub`: https://sublime-and-sphinx-guide.readthedocs.io/en/latest/index.html


