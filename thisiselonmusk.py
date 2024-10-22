#desafio
from time import sleep
import random

#declarando as variáveis 
game=True                                       
jog=['papel','tesoura','pedra']                 
res=['empate','você venceu','CPU venceu']    
res_cont=[0,0,0]

while game==True:

    #Jogada do usuário
    print('Faça sua jogada:\n1:Papel\n2:Tesoura\n3:Pedra')
    jog_user=int(input())
    if jog_user<=0 or jog_user>=4:
        print('Você digitou um número inválido, tente novamente!')
        continue

    #Jogada da CPU
    jog_cpu=random.randint(1,3)

    #Verifica quem ganhou   
    if jog_user==jog_cpu:
        Resultado=0                     #empate
    elif (jog_user==1 and jog_cpu==3) or (jog_user==2 and jog_cpu==1) or (jog_user==3 and jog_cpu==2):  
        Resultado=1                     #games edu vence
    else:
        Resultado=2  #caso nao der green, lógicamente a cpu venceu
    print('Você jogou '+jog[jog_user-1]+', CPU jogou '+jog[jog_cpu-1]+', Resultado: '+res[Resultado])

    res_cont[Resultado]=res_cont[Resultado]+1
    print('Tivemos até agora '+str(res_cont[0])+' empates, '+str(res_cont[1])+' vitórias suas e '+str(res_cont[2])+' vitórias da CPU.')

    print('Vamos jogar novamente? (S/N)')
    x=input()
    if x=='N' or x=='n':
        game=False
    elif x=='S' or x=='s':
        game=True
    else:
        print('Resposta inválida, digitou '+x)
        break

print('Obrigado por jogar!')

#Caso queira dar um tempo de resposta maior, adicione sleep(2) que fica bom.
