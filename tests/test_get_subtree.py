import unittest
import jnprsr.utils

class TestGetSubtree(unittest.TestCase):
    def read_test_file(self, name):
        with open(name, "r") as f:
            return f.read()

    def test_1(self):
        ast1 = jnprsr.utils.get_ast(self.read_test_file("test-conf1.txt"))
        ast2 = jnprsr.utils.get_sub_tree(ast1, "interfaces ge-0/0/0")
        out = jnprsr.utils.render_ascii_tree_from_ast(ast2)
        print(out)
