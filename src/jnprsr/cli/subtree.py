from sys import stdin
from jnprsr import *
import prompt_toolkit
from jnprsr.prompt_toolkit_custom_nested_completer import CustomNestedCompleter
import pprint
from anytree.resolver import ChildResolverError

def subtree():
    print("[Type CTRL+D or '!END' at a new line to end input]")
    input_data = ""
    for line in stdin:
        if line.startswith("!END"):
            break
        input_data += line


    ast = get_ast(input_data)
    session = prompt_toolkit.PromptSession()

    pprint.pprint(render_dict_from_ast(ast))

    completer_dict = {
        "show": {
            "configuration":
                render_dict_from_ast(ast)["root"]
        }
    }

    completer = CustomNestedCompleter.from_nested_dict(completer_dict)

    while True:
        path = session.prompt("jnprsr> ", completer=completer)
        path = path.replace("show configuration ", "")
        try:
            subast = get_sub_tree(ast, path)
            print(render_config_from_ast(subast))
        except ChildResolverError as e:
            print("Error", e)



