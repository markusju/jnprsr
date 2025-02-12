import argparse

import jnprsr
from jnprsr.cli.cliutils import _read_from_file


def _argparser_simple_two_files():
    parser = argparse.ArgumentParser(
        prog="jnprsr-merge",
        description='Merges a given Juniper configuration file \'file2\' onto \'file1\'',
        epilog="jnprsr is a Parser for Juniper Configuration Files"
    )
    parser.add_argument('file1', help="Configuration file1, file that will be the merge target")
    parser.add_argument('file2', help="Configuration file2, file that will be the merge source")
    args = parser.parse_args()
    return args

def merge():
    args = _argparser_simple_two_files("jnprsr-merge")
    file1 = _read_from_file(args.file1)
    file2 = _read_from_file(args.file2)

    # Generate AST
    ast1 = jnprsr.get_ast(file1)
    ast2 = jnprsr.get_ast(file2)

    # Merge
    ast3 = jnprsr.merge(ast1, ast2)

    # Render Config again
    merged_config = jnprsr.render_config_from_ast(ast3)

    print(merged_config)