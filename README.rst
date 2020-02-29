# Starsky
Natural Language Processing NLP into email body into email subject tags.
It uses snips-nlu (https://github.com/snipsco/snips-nlu) for NLP.

So after cloning repo you need to install language pack.

------------
Installation
------------

.. code-block:: python

    pip install snips-nlu

We currently have pre-built binaries (wheels) for ``snips-nlu`` and its
dependencies for MacOS (10.11 and later), Linux x86_64 and Windows.

For any other architecture/os `snips-nlu` can be installed from the source
distribution. To do so, `Rust <https://www.rust-lang.org/en-US/install.html>`_
and `setuptools_rust <https://github.com/PyO3/setuptools-rust>`_ must be
installed before running the ``pip install snips-nlu`` command.

------------------
Language resources
------------------

Snips NLU relies on `external language resources`_ that must be downloaded before the
library can be used. You can fetch resources for a specific language by
running the following command:

.. code-block:: sh

    python -m snips_nlu download en

Or simply:

.. code-block:: sh

    snips-nlu download en


The list of supported languages is available at
`this address <https://snips-nlu.readthedocs.io/en/latest/languages.html>`_.