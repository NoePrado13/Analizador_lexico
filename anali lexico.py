import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['IF','WHILE','RETURN','ELSE','INT','FLOAT']


tokens = reservadas+['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
          'LT','LTE','GT','GTE','DIF','EQUS',
          'LPARENT','RPARENT','SEMMICOLOM','OPAND','ORR','NOTT','KEY','KEYS'
]


t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_DIF = r'!='
t_EQUS = r'=='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_SEMMICOLOM = r';'
t_OPAND = r'&&'
t_ORR = r'\|\|'
t_NOTT = r'\!'
t_KEY = r'\{'
t_KEYS = r'\}'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\# .*'
    pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return  t

def t_error(t):
    print("caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print (str(cont)+". "+file)
        cont = cont+1

    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break
    print("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

    return files[int(numArchivo)-1]



directorio = 'test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok : break
    print(tok)





