from sys import stdin
import argparse


def _read_from_stdin(silent=False):
    if not silent:
        print("[Type CTRL+D or '!END' at a new line to end input]")
    input_data = ""
    for line in stdin:
        if line.startswith("!END"):
            break
        input_data += line
    return input_data

def _argparser(name: str):
    parser = argparse.ArgumentParser(
        prog=name,
        description='Pretty prints a given Juniper Configuration read from STDIN. End input with CTRL+D or sequence \'!END\'',
        epilog="jnprsr is a Parser for Juniper Configuration Files"
    )
    parser.add_argument('-s', '--silent', action="store_true", help="Silent mode: Silences any additional output. Recommended when used in scripts")
    args = parser.parse_args()
    return args