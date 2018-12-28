import sys #importa função que declara arquivo a ser escolhido
from string import uppercase as uc #importa letras maiusculas

enfreq='ETAOINSHRDLCUMWFGYPBVKJXQZ' #lista de frequencia UEA

ltcount={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'X':0,'W':0,'Y':0,'Z':0} #dicionario de frequencias

file = open(sys.argv[1],'r').read().upper() #nome do arquivo e transforma em letras maiusculas

for lt in file: #percorre o arquivo todo
	if lt in uc: #ignora os espaços
		ltcount[lt]+=1 #conta a quantidade e acrescenta em ltcount 
order=[] #cria indix vazio para ordernar as lestras
score=0 #cria um score 0

for w in sorted(ltcount, key=ltcount.get, reverse=True):#ordena as letras do maior para o menor.
	print w,ltcount[w] # mostra a letra e o numero do index 
	order.append(w) #acrescenta w que e a variavel da ordenação

order = ''.join(order)#conta vazio.order terminar video aula 

for clt in enfreq[:6]:#conta se as 6 primeiras letras do enfreq 'etaoin' aparecem em sequencia de frequencia. 
	if clt in order[:6]:
		score+=1 #acrescenta um ao score caso apareca na ordem
for ult in enfreq[-6:]:#conta se as 6 ultimas letras do enfreq 'vkjxqz' aparecem em sequencia de frequencia.
	if ult in order[-6:]:
		score+=1#acrescenta um ao score caso apareca na ordem
print 'score:',score,'out of 12' #quanto mais proximo do 12 mais proximo dessa frequencia ser da lingua analisada, no caso UEA.



