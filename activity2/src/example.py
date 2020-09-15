# http://cs.indstate.edu/~jkinne/cs420-s2019/code/?view=./sly-calc.py
# -----------------------------------------------------------------------------
# calc1.py
# 4 + 5
# -----------------------------------------------------------------------------

from sly import Lexer, Parser

class MyLexer(Lexer):
    tokens = { ID, NUM, EQ }
    ignore = ' \t'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUM = r'[0-9]+'
    EQ = r'='

    def NUM(self, t):
        t.value = int(t.value)
        return t


class MyParser(Parser):
    tokens = MyLexer.tokens

    @_('statements statement')
    def statements(self, p):
        return p.statement + [ p.statement ]

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

if __name__ == '__main__':
    lexer = MyLexer()
    for tok in lexer.tokenize('a = 3'):
        print(tok)
    #parser = MyParser()
    #result = parser.parse(lexer.tokenize("a = 3"))
    #print(result)

#    while True:
#        try:
#            text = input('calc > ')
#        except EOFError:
#            break
#        if text:
#            parser.parse(lexer.tokenize(text))
