from lark import Lark
from lark_transformer import LarkLarkTransformer
from lark_interpreter import LarkLarkInterpreter
from lark_source import source_code
from lark_grammar import lark_lark_grammar


# Step 0 define the grammar
# Located in lark_grammar.py

# Step 1
# Parse the grammar
lark_parser = Lark(lark_lark_grammar, start='start', parser='lalr')
parse_tree = lark_parser.parse(source_code)

print(parse_tree.pretty())


# Step 2
# Instantiate the transformer and use it to transform the parse tree
transformer = LarkLarkTransformer()
ast = transformer.transform(parse_tree)
print(ast)

# Step 3
# Instantiate the interpreter and use it to execute the AST
interpreter = LarkLarkInterpreter()
interpreter.run(ast)

