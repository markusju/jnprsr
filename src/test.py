import jnprsr.utils

from sys import stdin

input_data = ""
for line in stdin:
    if line.startswith("END"):
        break
    input_data += line

ast = jnprsr.utils.get_ast(input_data)


while True:
    path = input("> ")
    subast = jnprsr.utils.get_sub_tree(ast, path)
    print(jnprsr.utils.render_config_from_ast(subast))




