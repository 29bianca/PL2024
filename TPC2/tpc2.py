import re

# Expressoes regulares
titulo = re.compile("^\#[^\#].+")
subtitulo = re.compile("^\#{2}[^\#].+")
subsubtitulo = re.compile("^\#{3}[^\#].+")

negrito = re.compile("^\*{2}.+\*{2}")
italico = re.compile("^\*[^\*].*\*$")

bquote = re.compile("^\>.+")

listaN = re.compile("^[0-9]+\..+")
listaT = re.compile("^\-[^\-].+")

codigo = re.compile ("^`.+`$")

linha = re.compile("^-{2}$")

link = re.compile("^\[(.+)\]\((.+)\)$")
imagem = re.compile("^!\[(\w+.*)\]\((.+)\)")

nome_ficheiro = "texto.md" # nome do ficheiro
html = """
<!DOCTYPE html>
<html>

"""

m = open(nome_ficheiro,"r") # abrir o ficheiro
linhas = m.readlines()  # ler as linhas todas para a variavel linhas

itensN = False
itensT = False

#ler linha a linha e vai adicionando à variável html o texto tratado
for linha in linhas:

    if not listaN.match(linha) and itensN == True:
        html += "\t</ol>\n"
        itensN = False

    if not listaT.match(linha) and itensT == True:
        html += "\t</ul>\n"
        itensT = False       

    if titulo.match(linha):
        html += "<h1>" + linha[2:-1] + "</h1>\n"
    elif subtitulo.match(linha):
        html += "<h2>" + linha[3:-1] + "</h2>\n"
    elif subsubtitulo.match(linha):
        html += "<h3>" + linha[4:-1] + "</h3>\n"
    elif negrito.match(linha):
        html += "<b>" + linha[2:-3] + "</b>\n"
    elif italico.match(linha):
        html += "<i>" + linha[1:-2] + "</i>\n"
    elif listaN.match(linha):
        if itensN == False:
            itensN = True
            html += "\t<ol>\n"
        html += "\t\t<li>" + linha[3: -1] + "</li>\n"
    elif listaT.match(linha):
        if itensT == False:
            itensT = True
            html += "\t<ul>\n"
        html += "\t\t<li>" + linha[2: -1] + "</li>\n"
    elif codigo.match(linha):
        html += "<code" + linha[1: -2] + "</code>\n"
    elif link.match(linha):
        html += "<a href=\"" + link.match(linha).group(2) + "\">" + link.match(linha).group(1) + "</a>\n"
    elif imagem.match(linha):
        html += "<img src=\"" + imagem.match(linha).group(2) + "\" alt=\"" + imagem.match(linha).group(1) + "\"/>\n"

    
# acrescenta o final do texto html
html+= """
</html>
"""

# criar um ficheiro html
f = open("nomeqq.html","w")
f.write(html)
f.close()

