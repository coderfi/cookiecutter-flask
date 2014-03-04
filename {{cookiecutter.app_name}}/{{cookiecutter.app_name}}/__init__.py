from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import pkg_resources
pkg_resources.declare_namespace(__name__)

__description__ = "{{cookiecutter.project_short_description}}"
__version__ = "{{cookiecutter.project_version}}"
__author__ = "{{cookiecutter.github_username}}"
__email__ = "{{cookiecutter.email}}"
__license__ = "All rights reserved."
