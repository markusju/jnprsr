from jnprsr import *
import prompt_toolkit
from jnprsr.prompt_toolkit_custom_nested_completer import CustomNestedCompleter
from jnprsr.cli.cliutils import _read_from_stdin, _argparser
from anytree.resolver import ChildResolverError

def subtree():
    args = _argparser("jnprsr-subtree")
    input_data = _read_from_stdin(silent=args.silent)

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



