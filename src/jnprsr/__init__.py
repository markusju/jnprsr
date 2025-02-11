"""jnprsr is a Parser for Juniper Configuration Files"""

__version__ = "0.0.6"
__author__ = "markusju"
__author_email__ = "markus.jungbluth@gmail.com"

from .utils import get_ast, render_config_from_ast, render_ascii_tree_from_ast, merge, get_sub_tree