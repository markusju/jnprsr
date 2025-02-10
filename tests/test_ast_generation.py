import unittest
import jnprsr.utils

class TestASTGeneration(unittest.TestCase):
    def read_test_file(self, name):
        with open(name, "r") as f:
            return f.read()

    def test_parser(self):
        ast = jnprsr.utils.get_ast(self.read_test_file("test-conf1.txt"))
        self.assertEqual(ast.name, "root")
        self.assertEqual(len(ast.children), 3)
        self.assertEqual(list(map(lambda x: x.name, ast.children)), ["system", "protocols", "interfaces"])
        self.assertEqual(list(map(lambda x: x.name, ast.children[2].children)), ["ge-0/0/0"])

    def test_config_renderer(self):
        ast = jnprsr.utils.get_ast(self.read_test_file("test-conf1.txt"))
        rendered_config = jnprsr.utils.render_config_from_ast(ast)
        self.assertEqual(self.read_test_file("test-conf1.txt"), rendered_config)

    def test_ascii_tree_renderer(self):
        ast = jnprsr.utils.get_ast(self.read_test_file("test-conf1.txt"))
        expected_ascii_tree = self.read_test_file("ascii-tree1.txt")
        self.assertEqual(expected_ascii_tree, jnprsr.utils.render_ascii_tree_from_ast(ast))