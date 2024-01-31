#lista de fatores primos para futura fatoração
fatores = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,
211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,
307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,
401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,
503,509,521,523,541,547,557,563,569,571,577,587,593,599,
601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,
701,709,719,727,733,739,743,751,757,761,769,773,787,797,
809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,
907,911,919,929,937,941,947,953,967,971,977,983,991,997]

#quantidade de casos de teste
casoTeste = int(input())

#loop 'for' para executar cada caso de teste 1 a 1
for i in range(casoTeste):
    #entrada de caso de teste
    casoTeste = input().split(' ')
    
    #guardando os valores do caso de teste dentro de variaveis separadas
    #numerador 1
    N1 = int(casoTeste[0])
    #denominador 1
    D1 = int(casoTeste[2])
    #numerador 2
    N2 = int(casoTeste[4])
    #denominador 2
    D2 = int(casoTeste[6])
    
    #operador aritmético
    op = casoTeste[3]

    #função para fatoração do valor racional
    def simplifica(numerador, denominador, racional):
        
        #loop 'for' para percorrer cada elemento da lista de fatores primos
        for i in fatores:
            
            #loop 'while' é executado enquanto o numerador e o denominador forem ambos divisiveis pelo mesmo fator
            while (numerador % i == 0 and denominador % i == 0):
                
                #fatoração do numerador
                numerador //= i
                #fatoração do denominador
                denominador //= i
                #condição que para o loop se o denominador e o numerador forem primos
        
        #saída do resultado formatado com o valor racional e o valor fatorado
        print('{} = {}/{}'.format(racional, numerador, denominador))
    
    #método para realizar a operação aritmética
    def tdaRacional():
        
        #cada condição é um operador aritmético diferente (+. -, *, /)
        #cada condição realiza a chamada do função de fatoração 
        if op == '+':
            racional = '{}/{}'.format(N1*D2 + N2*D1, D1*D2)
            simplifica((N1*D2 + N2*D1), (D1*D2), racional)
        elif op == '-':
            racional = '{}/{}'.format((N1*D2 - N2*D1), (D1*D2))
            simplifica((N1*D2 - N2*D1), (D1*D2), racional)
        elif op == '*':
            racional = '{}/{}'.format((N1*N2), (D1*D2))
            simplifica((N1*N2), (D1*D2), racional)
        elif op == '/':
            racional = '{}/{}'.format((N1*D2), (N2*D1))
            simplifica((N1*D2), (N2*D1), racional)
    
    #chamada do método para realizar o cálculo e a fatoração
    tdaRacional()
