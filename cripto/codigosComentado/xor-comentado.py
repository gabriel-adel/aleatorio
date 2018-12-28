import sys, binascii #importa sys que permite dar comandos e importa binascii que trasnforma hexa ou binario em letra ascii ou vice e versa


key = sys.argv[2] #agurmento da chave
mode = sys.argv[3] #agumento do modo enc ou dec
keyidx =0 #index da chave 0
xored = '' #criacao de variavel vazia

if mode == 'enc':
	msg= sys.argv[1] #modo enc recebe testo puro
elif mode =='dec':
	msg=binascii.unhexlify(sys.argv[1]) #modo dec recebe texto hexadecimal

for msgchar in msg: #le a string
	xored += chr(ord(key[keyidx%len(key)]) ^ ord(msgchar))#faz a chave e a frase com o mesmo tamanho "ord(key[keyidx%len(key]". Trasnforma o caractere em binario e faz a função xor " ord(key[keyidx%len(key]) ^ ord(msgchar)". Recebe o resultado dela mesmo de cada palava "xored +="
	keyidx +=1 #acrescenta 1. 
if mode == 'enc': #imprime mensagem em modo binario
	print binascii.hexlify(xored)
elif mode == 'dec':
	print xored #imprime mensagem em modo normal




