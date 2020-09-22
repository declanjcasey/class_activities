# token TYPENAME
# token VARNAME
# token KA
# token DOT

# statement -> expr
# expr -> KA | expr.VARTYPE | ka.VARNAME

from sly import Lexer, Parser

class ExampleLexer(Lexer):
    # TODO: Add Lexing

if __name__ == '__main__':
    lexer = ExampleLexer()
    for tok in lexer.tokenize("ka.var.Int"):
        print('type=%r, value=%r' % (tok.type, tok.value))
