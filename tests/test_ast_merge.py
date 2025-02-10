import unittest
import jnprsr.utils

class TestASTMerge(unittest.TestCase):
    def read_test_file(self, name):
        with open(name, "r") as f:
            return f.read()

    def test_1(self):
        ast1 = jnprsr.utils.get_ast(self.read_test_file("test-conf1.txt"))
        ast2 = jnprsr.utils.get_ast(self.read_test_file("test-conf2.txt"))
        ast3 = jnprsr.utils.merge(ast1, ast2)
        out = jnprsr.utils.render_config_from_ast(ast3)
        self.assertEqual(self.read_test_file("test-conf1-conf2-merged.txt"), out)

    def test_2(self):
        ast1 = jnprsr.utils.get_ast(self.read_test_file("test-conf1.txt"))
        ast2 = jnprsr.utils.get_ast(self.read_test_file("test-conf3.txt"))
        ast3 = jnprsr.utils.merge(ast1, ast2)
        out = jnprsr.utils.render_ascii_tree_from_ast(ast3)
        print(out)
        print(jnprsr.utils.render_config_from_ast(ast3))

    def test_3(self):
        ast1 = jnprsr.utils.get_ast(self.read_test_file("test-conf4.txt"))
        ast2 = jnprsr.utils.get_ast(self.read_test_file("test-conf5.txt"))
        ast3 = jnprsr.utils.merge(ast1, ast2)
        out = jnprsr.utils.render_config_from_ast(ast3)
        self.assertEqual(self.read_test_file("test-conf4-conf5-merged.txt"), out)