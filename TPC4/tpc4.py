import ply.lex as lex
import re

tokens = (
	'SELECT',
	'FROM',
	'WHERE',
	'VARIABLE',
	'COMMA',
	'NUMBER',
	'GREATER_THAN',
	'LESS_THAN',
	'GREATER_THAN_EQUALS',
	'LESS_THAN_EQUALS',
	'EQUALS',
)

t_SELECT = r'[Ss][Ee][Ll][Ee][Cc][Tt]'
t_FROM = r'[Ff][Rr][Oo][Mm]'
t_WHERE = r'[Ww][Hh][Ee][Rr][Ee]'
t_VARIABLE = r'id|nome|salario|empregados'
t_COMMA = r','
t_NUMBER = r'\d+'
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_THAN_EQUALS = r'\>\='
t_LESS_THAN_EQUALS = r'\<\='
t_EQUALS = r'\='

t_ignore = ' \t'	#ignorar os espaços em branco

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_error(t):
	print(f"Inválido: '{t.value[0]}'")
	t.lexer.skip(1)

lexer = lex.lex()

# testar
text = "Select id, nome, salario From empregados Where salario >= 820"
lexer.input(text)

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)
