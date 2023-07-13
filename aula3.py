#a string ou str so é reconhecida no programa com '' aspas simpes ou "" aspas duplas 

"""
porem quando é preciso usar aspas simples no meio de uma str é bom utilizar as aspas duplas nesse caso
"""
#exemplo
#nome = 'In today's lesson'
#no exemplo acima daria um erro no programa entao para evitar isso usa-se
#nome = "In today's lesson"
"""
da mesma maneira com aspas duplas nao funcionaria no meio de uma str com aspas duplas
"""
#exemplo 
#nome = "hoje eu nao vou ao "trabalho""
#no exemplo acima daria outro erro no programa entao para evitar o problema devemos usar aspas simples 
#nome = 'hoje eu nao vou ao "trabalho"'

#aspas tripas tambem pode ser uma str com varias linhas exemplo


msg = """
oi mana como vai?

quer jogar uma partida de duel links?
ou runeterra?

amanhã as 14:30 que tal? 

"""
print(msg)
"""
nome = 'izabela'
nome = "izabela"
print(nome)
"""
frase = "Hoje esta sol"
print(frase[0:4])