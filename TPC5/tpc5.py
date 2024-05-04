import json
import ply.lex as lex

with open('stock.json') as stock:
	dados = json.load(stock)

moedas = {
	"2e": 2.00,
	"1e": 1.00,
	"50c": 0.50,
	"20c": 0.20,
	"10c": 0.10,
	"5c": 0.05,
	"2c": 0.02,
	"1c": 0.01
}

saldo = 0

def para_int(str):
	valor = None
	if(str in moedas):
		valor = moedas[str]
	else:
		print("A moeda não é válida")
		valor = 0
	return valor

def de_int(v):
	inteiro, decimal = str("{:.2f}".format(v)).split('.')
	return f"{inteiro}e{decimal}c"


tokens = (
	'LISTAR',
	'MOEDA',
	'DINHEIRO',
	'SELECIONAR',
	'SAIR',
	'VIRGULA',
	'PONTO',
	'NOME_PRODUTO'
)

t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_DINHEIRO = r'\d{1,2}[ec]'
t_SELECIONAR = r'SELECIONAR'
t_SAIR = r'SAIR'
t_VIRGULA = r','
t_PONTO = r'\.'
t_NOME_PRODUTO = r'A\d{2} '

t_ignore = ' \t\n'

def t_error(t):
	print("Inválido: ", t.value[0])
	t.lexer.skip(1)

lexer = lex.lex()

on = True

while on:
    comando = input('>> ')
    lexer.input(comando)
    tok = lexer.token()
    if tok.type=="MOEDA":
        for tok in lexer:
            if(tok.type == "DINHEIRO"):
                saldo += para_int(tok.value)
        saldo_str = f'maq: Saldo {de_int(saldo)}'
        print(saldo_str)
    elif tok.type=="LISTAR":
        print (f"{'cod':<10} | {'nome':<20} | {'quant':<10} | {'preco':<10}")
        print ('-' * 60)
        for p in dados["stock"]:
            print(f"{p['cod']:<10} | {p['nome']:<20} | {p['quant']:<10} | {p['preco']:<10.2f}")
    elif tok.type=="SELECIONAR":
        tok = lexer.token()
        id = tok.value
        for prod in dados['stock']: 
            if prod['cod'] == id:
                if prod['preco'] <= saldo:
                    if prod['quant'] > 0:
                        troco = saldo - prod['preco']
                        prod['quant'] -= 1
                        print(f"Retire o produto: {prod['nome']}")
                        if troco >= 0:
                            print(f"Retire o troco: {de_int(troco)}")
                        saldo = 0
                        troco = 0
                    else:
                        print("Não há stock deste produto")
                else:
                    print(f"O saldo não é suficiente: \nSaldo: {saldo}\nPreço do produto: {prod['preco']}")
    elif tok.type=="SAIR":
        on = False
    else:
        print("Inválido")

with open('stock.json', 'w') as stock_json:
    json.dump(dados, stock_json, indent=4)