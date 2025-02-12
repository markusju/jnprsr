import argparse

from jnprsr import *
import prompt_toolkit
from jnprsr.prompt_toolkit_custom_nested_completer import CustomNestedCompleter
from jnprsr.cli.cliutils import _read_from_file
from anytree.resolver import ChildResolverError



def _argparser_simple_one_file():
    parser = argparse.ArgumentParser(
        prog="jnprsr-subtree",
        description='Opens an interactive CLI allowing to inspect a given configuration file.',
        epilog="jnprsr is a Parser for Juniper Configuration Files"
    )
    parser.add_argument('filename', help="Configuration file to open")
    args = parser.parse_args()
    return args

def subtree():
    args = _argparser_simple_one_file()
    input_data = _read_from_file(args.filename)

    ast = get_ast(input_data)
    session = prompt_toolkit.PromptSession()

    # Transform AST into dict for completer
    completer_dict = {
        "show": {
            "configuration":
                render_dict_from_ast(ast)["root"]
        }
    }

    # Instantiate completer from dict
    completer = CustomNestedCompleter.from_nested_dict(completer_dict)

    # Setup Command Prompt
    while True:
        path = session.prompt("jnprsr> ", completer=completer)
        path = path.replace("show configuration ", "")
        try:
            subast = get_sub_tree(ast, path)
            print(render_config_from_ast(subast))
        except ChildResolverError as e:
            print("Error", e)



