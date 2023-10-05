============================
gitscribe
============================

gitscribe is a Python Discord bot that provides information about GitHub repositories and issues. It's designed to make it easier for users to retrieve details about GitHub projects directly within a Discord server.

Installation
------------

To deploy gitscribe, follow these steps:

       .. code-block:: bash
                
             pip install gitscribe

To build and develop gitscribe, follow these steps:

1. Clone the repository:

   .. code-block:: bash
   
      git clone https://github.com/oss-reva/gitscribe.git
      cd gitscribe

2. Create a virtual environment:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate

3. Install requirements:

   .. code-block:: bash

      pip install -r requirements.txt

4. Install the package in editable mode:

   .. code-block:: bash

      pip install -e .

Usage
-----

To use gitscribe, provide the Discord bot token as follows:

   .. code-block:: bash

      gitscribe --token DISCORD_BOT_TOKEN

Replace `DISCORD_BOT_TOKEN` with your actual Discord bot token.

Contributing
------------

If you'd like to contribute to this project, please read our `Contributing Guidelines`_.

License
-------

gitscribe is licensed under the MIT License. See the LICENSE_ file for details.

.. _LICENSE: https://github.com/oss-reva/gitscribe/blob/main/LICENSE
.. _Contributing Guidelines: https://github.com/oss-reva/gitscribe/blob/main/CONTRIBUTING.md
