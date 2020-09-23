# Grammar Rules:
# -----------------------------------------------------------------------------
# Statements: statements statement | statement
# Statement : ID EQ expr | PRINT LPAREN expr RPAREN
# Expr : expr PLUS expr | expr TIMES expr | NUM

# -----------------------------------------------------------------------------

from sly import Lexer, Parser

class MyLexer(Lexer):
    tokens = { ID, NUM, EQ, PRINT, PLUS, TIMES, LPAREN, RPAREN }
    ignore = ' \t'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUM = r'[0-9]+'
    EQ = r'='
    ID['print'] = PRINT
    PLUS = r'\+'
    TIMES = r'\*'
    LPAREN = r'\('
    RPAREN = r'\)'

    def NUM(self, t):
        t.value = int(t.value)
        return t


class MyParser(Parser):
    tokens = MyLexer.tokens

    @_('statements statement')
    def statements(self, p):
        return p.statements + [ p.statement ]

    @_('statement')
    def statements(self, p):
        return [ p.statement ]

    @_('ID EQ expr')
    def statement(self, p):
        return ('assign', p.ID, p.expr)

    @_('NUM')
    def expr(self, p):
        return ('num', p.NUM)

    @_('ID')
    def expr(self, p):
        return ('id', p.ID)

    @_('PRINT LPAREN expr RPAREN')
    def statement(self, p):
        return ('print', p.expr)

    @_('expr PLUS expr',
        'expr TIMES expr')
    def expr(self, p):
        return (p[1], p.expr0, p.expr1) # return the value, operator, expr on the right and left

    precedence = (
        ('left', 'PLUS'),
        ('left', 'TIMES')
    )

if __name__ == '__main__':
    lexer = MyLexer()
    #for tok in lexer.tokenize('2 + 3 * 4'):
    #    print(tok)
    parser = MyParser()
    result = parser.parse(lexer.tokenize("a = 2 a = 3"))
    print(result)

#    while True:
#        try:
#            text = input('calc > ')
#        except EOFError:
#            break
#        if text:
#            parser.parse(lexer.tokenize(text))
