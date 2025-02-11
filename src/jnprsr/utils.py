import antlr4
from jnprsr.parser.JuniperParser import JuniperParser
from jnprsr.parser.JuniperLexer import JuniperLexer
from jnprsr.parser.JuniperAST import JuniperAST, JuniperASTNode
from jnprsr.parser.JuniperASTRenderer import JuniperASTRenderer
from anytree import RenderTree, Resolver
from jnprsr.anytree_custom_dict_exporter import CustomDictExporter

def get_ast(input_data: str) -> JuniperASTNode:
    # Get Raw Data
    raw_input = antlr4.InputStream(input_data)

    # Run through Lexer
    tok_stream = antlr4.CommonTokenStream(
        JuniperLexer(raw_input)
    )
    # Pass stream of Tokens to Parser
    parser = JuniperParser(tok_stream)

    # Parse Tree
    tree = parser.juniper_configuration()

    # Init AST Generator Listener
    listener = JuniperAST()

    # Walk Tree
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.root

def render_config_from_ast(ast: JuniperASTNode) -> str:
    renderer = JuniperASTRenderer()
    return renderer.render(ast)

def render_ascii_tree_from_ast(ast: JuniperASTNode) -> str:
    buffer = ""
    for pre, _, node in RenderTree(ast):
        buffer += pre + node.name + "\n"
    return buffer

def render_dict_from_ast(ast: JuniperASTNode) -> dict:
    exporter = CustomDictExporter()
    return exporter.export(ast)

def __intersection(lst1, lst2):
    return list(set(lst1).intersection(lst2))

def __difference(lst1, lst2):
    return list(set(lst1).difference(lst2))

def merge(ast1, ast2):
    __merge(ast1, ast2)
    return ast1

def __merge(ast1: JuniperASTNode, ast2: JuniperASTNode):
    """
    Merges two JuniperASTs, ast2 is merged onto ast1. Similar to a "load merge" operation.
    :param ast1:
    :param ast2:
    :return:
    """
    EXCEPT_KEYS = ["interface"]
    print("merge", ast1, ast2)
    # Get Names of all the children at current level
    ast1_children = list(map(lambda x:x.name, ast1.children))
    ast2_children = list(map(lambda x:x.name, ast2.children))
    # Find common children
    common_children = __intersection(ast1_children, ast2_children)
    # Find missing children
    different_children = __difference(ast2_children, ast1_children)
    # Iterate over both lists for both trees

    # In case there are no children, just add them
    if len(ast1.children) == 0:
        for child_ast2 in ast2.children:
            child_ast2.parent = ast1

    # Follow paths and descend to common config items
    for child_ast1 in ast1.children:
        for child_ast2 in ast2.children:

            # If there is an identical path, go down -> Recursion
            if child_ast1.key == child_ast2.key and child_ast1.value == child_ast2.value and child_ast1.name in common_children:
                __merge(child_ast1, child_ast2)

            # If we are at the sub-tree where something needs to be added to AST1 for a pre-existing node, add it
            if child_ast2.name in different_children and child_ast1.key == child_ast2.key:
                # Make ast2 node parent reference the reference of ast1 node
                child_ast2.parent = child_ast1.parent

                # Remove from list of different children
                different_children.remove(child_ast2.name)

                # If it is a leaf node and not a bracketed clause and its key is not on the exception list, replace it!
                if child_ast1.is_juniper_leaf_node() and not child_ast1.is_juniper_bracketed_clause() and child_ast1.key not in EXCEPT_KEYS:
                    # Make child_ast1 node an orphan
                    child_ast1.parent = None

                # If it is a leaf node and a bracketed clause insert elements!
                if child_ast1.is_juniper_leaf_node() and child_ast1.is_juniper_bracketed_clause():
                   child_ast2.append_value(child_ast1.value)
                   # Make ast1 node an orphan
                   child_ast1.parent = None

    # Add non-existing items at this level to AST1 that have no pre-existing nodes on AST1
    for missing_children in different_children:
        for child_ast2 in ast2.children:
            if child_ast2.name == missing_children:
                # AST1 can simply adopt them
                child_ast2.parent = ast1



def get_sub_tree(ast: JuniperASTNode, path: str) -> JuniperASTNode:
    resolver = Resolver()
    return resolver.get(ast, path)