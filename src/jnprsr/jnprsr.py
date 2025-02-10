import utils
from JuniperAST import JuniperASTNode


class jnprsr:
    def __init__(self, juniper_configuration: str):
        self.juniper_configuration = juniper_configuration
        self.ast = utils.get_ast(juniper_configuration)

    def get_ast(self) -> JuniperASTNode:
        return self.ast
