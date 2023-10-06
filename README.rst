============================
gitscribe
============================

gitscribe is a Python Discord bot that provides information about GitHub repositories and issues. It's designed to make it easier for users to retrieve details about GitHub projects directly within a Discord server.

Hacktoberfest Contribution Guidelines
--------------------------------------

Thank you for considering contributing to our project during Hacktoberfest! We appreciate your time and effort to help improve our open-source project. To ensure a smooth and productive contribution process, please follow these guidelines:

       Warning: Contributions not following project guidelines may be marked as spam or invalid.

Issues
^^^^^^^
- **Check for Existing Issues**: Before creating a new issue, check if a similar one already exists. If you find an issue that matches your concern, you can comment on it to provide additional information or discuss potential solutions.

- **Create Clear and Descriptive Issues**: When creating a new issue, provide a clear and detailed description of the problem or enhancement you're proposing. Include steps to reproduce issues if applicable.

- **Label Properly**: Use appropriate labels when creating issues to categorize them correctly. This helps maintain a well-organized issue tracker.

Pull Requests
^^^^^^^^^^^^^^

1. **Fork, Branch, Code, Test, Commit, Push**
   
   - Fork the repository, create a branch.
   - Make changes, test, commit with clear messages, and push.

2. **Pull Request, Respond**
   
   - Create a pull request with a clear title.
   - Be responsive to feedback.



Thank you for your contributions, and happy Hacktoberfest!

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
