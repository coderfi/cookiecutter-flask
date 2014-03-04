===============================
{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.project_short_description}}


Quickstart
----------

First, install `Virtualenv Wrapper<http://virtualenvwrapper.readthedocs.org/en/latest/>`_
(and `Virtualenv<http://www.virtualenv.org/en/latest/>`_)

::

    git clone https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.app_name }}
    cd {{cookiecutter.app_name}}

    mkvirtualenv {{cookiecutter.app_name}}

    python setup.py develop

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server



Deployment
----------

In your production environment, make sure the ``{{cookiecutter.app_name|upper}}_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``.
In addition to a SQLAlchemy ``db`` instance and the SQLAlchemy ``User`` model.
As well as a MongoKit ``dbm`` instance and the MongoKit ``Task`` model
(accessible via ``dbm.Task``)


Running Tests
-------------

To run all tests, run ::

    python manage.py test


Migrations
----------

Whenever a database migration needs to be made. Run the following commmands:
::

    python manage.py db migrate

This will generate a new migration script. Then run:
::

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.
