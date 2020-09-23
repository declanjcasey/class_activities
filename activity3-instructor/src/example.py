# token TYPENAME
# token VARNAME
# token KA
# token DOT

# statement -> expr
# expr -> KA | rval | rval.VARTYPE
# rval -> KA DOT VARNAME

from sly import Lexer, Parser

class ExampleLexer(Lexer):
    tokens = { TYPENAME, VARNAME, KA, DOT }

    ignore = ' \t '
    TYPENAME = r'[A-Z][a-zA-Z0-9_!]*'
    VARNAME = r'[a-z][a-zA-Z0-9_!]*'
    VARNAME['ka'] = KA
    DOT = r'\.'

class ExampleParser(Parser):
    debugfile = 'parser.out'
    tokens = ExampleLexer.tokens

    @_('expr')
    def statement(self, p):
        return [ p.expr ]

    @_('KA')
    def expr(self, p):
        return ('ka', p.KA)

    @_('rval')
    def expr(self, p):
        return (p.rval)

    @_('rval DOT TYPENAME')
    def expr(self, p):
        return (p[1], p.rval, p.TYPENAME)

    @_('KA DOT VARNAME')
    def rval(self, p):
        return (p[1], p.KA, p.VARNAME)

if __name__ == '__main__':
    lexer = ExampleLexer()
    for tok in lexer.tokenize("ka.var.Int"):
        print('type=%r, value=%r' % (tok.type, tok.value))

    parser = ExampleParser()
    result = parser.parse(lexer.tokenize("ka.var!.Int_"))
    print(result)
