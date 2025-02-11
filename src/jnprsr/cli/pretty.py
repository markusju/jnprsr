from jnprsr import *
from jnprsr.cli.cliutils import _read_from_stdin, _argparser
import argparse

def pretty():
    args = _argparser("jnprsr-pretty")

    input_data = _read_from_stdin(silent=args.silent)
    # We simply generate an abstract syntax tree
    ast = get_ast(input_data)
    # ... and rendering the config again based on that!
    out = render_config_from_ast(ast)
    print(out)


