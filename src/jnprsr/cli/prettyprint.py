from jnprsr import *
from sys import stdin

def prettyprint():
    print("[Type CTRL+D or '!END' at a new line to end input]")
    input_data = ""
    for line in stdin:
        if line.startswith("!END"):
            break
        input_data += line
    # We simply generate an abstract syntax tree
    ast = get_ast(input_data)
    # ... and rendering the config again based on that!
    out = render_config_from_ast(ast)
    print(out)
