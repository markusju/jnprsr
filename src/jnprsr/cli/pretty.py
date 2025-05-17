from jnprsr import *
from jnprsr.cli.cliutils import _read_from_stdin
import argparse


def _argparser_simple_direct_input():
    parser = argparse.ArgumentParser(
        prog="jnprsr-pretty",
        description='Pretty prints a given Juniper Configuration read from STDIN. End input with CTRL+D or sequence \'!END\'',
        epilog="jnprsr is a Parser for Juniper Configuration Files"
    )
    parser.add_argument('-s', '--silent', action="store_true", help="Silent mode: Silences any additional output. Recommended when used in scripts")
    args = parser.parse_args()
    return args

def pretty():
    args = _argparser_simple_direct_input()

    input_data = _read_from_stdin(silent=args.silent)
    # We simply generate an abstract syntax tree
    ast = get_ast(input_data)
    # ... and rendering the config again based on that!
    out = render_config_from_ast(ast)
    print(out)


