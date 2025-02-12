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

def _read_from_file(filename):
    with open(filename, 'r') as file:
        file_content = file.read()

    return file_content