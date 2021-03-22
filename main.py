from cliente import Cliente
from cliente import c1
from cliente import c2
from conta import Conta
from conta import ct1
from conta import ct2
from banco import Banco
from banco import b1
from banco import b2
from imovel import Imovel
from imovel import i1
from imovel import i2
from financiamento import Financiamento
from financiamento import f1
from financiamento import f2

contas = []
contas.append(ct1)
contas.append(ct2)

financiamentos = []
financiamentos.append(c1.financiamento)
financiamentos.append(c2.financiamento)

print("====================\n"+str(c1.nome),"\n"+"N°Conta:",ct1.id,"\n"+"Saldo: R${:.2f}".format(ct1.saldo),"\n====================")

resposta = ''
lista_resposta = ['CLIENTE','CONTA','BANCO','FINANCIAMENTO']

while (resposta != 'SAIR'):
    resposta = str(input("\nVOCÊ QUER ACESSAR O *CLIENTE, A *CONTA, O *BANCO, OS FINANCIAMENTO OU *SAIR? ")).upper()

    if(resposta == 'CLIENTE'):
        print(f'{c1}')

        resposta_cliente = ''
        lista_cliente = ['FINANCIAMENTO TOTAL','ADICIONAR FINANCIAMENTO']

        while (resposta_cliente != 'VOLTAR'):
            resposta_cliente = str(input("\nVOCÊ QUER O *FINANCIAMENTO TOTAL, *ADICIONAR FINANCIAMENTO OU *VOLTAR? ")).upper()

            if(resposta_cliente == 'FINANCIAMENTO TOTAL'):
                print(c1.total_financiado())
            
            elif(resposta_cliente == 'ADICIONAR FINANCIAMENTO'):
                novo_financiamento=int(input('Insira o valor do novo financiamento:'))
                print(c1.add_financiamento(novo_financiamento))
            
            else:
                print('Erro, tente novamente.')
        
    elif(resposta == 'CONTA'):
        print(f'{ct1}')

        resposta_conta = ''
        lista_conta = ['DEBITAR, CREDITAR, TRANSFERÊNCIA']

        while (resposta_conta != 'VOLTAR'):
            resposta_conta = str(input("\nVOCÊ QUER *DEBITAR, *CREDITAR, REALIZAR UMA *TRANSFERÊNCIA OU *VOLTAR? ")).upper()

            if(resposta_conta == 'DEBITAR'):
                valor=float(input('Insira o valor a ser debitado de sua conta:'))
                print(ct1.debitar(valor))
            
            elif(resposta_conta == 'CREDITAR'):
                valor=float(input('Insira o valor a ser creditado de sua conta:'))
                print(ct1.creditar(valor))
            
            elif(resposta_conta == 'TRANSFERÊNCIA'):
                conta_origem = int(input('Insira o ID da conta origem:'))
                outra_conta = int(input('Insira o ID da conta destino:'))
                valor = float(input('Insira o valor da transferência:'))

                for i in range(0, len(contas)):
                    if outra_conta == contas[i].id:
                        id_outra_conta = contas[i]
                        break
                    
                for i in range(0, len(contas)):
                    if conta_origem == contas[i].id:
                        contas[i].transferencia(valor, id_outra_conta)
                        break
                
                print(f'Transferência realizada com sucesso!\nSaldo da conta {contas[0].id}: {contas[0].saldo}\nSaldo da conta {contas[1].id}: {contas[1].saldo}')


    elif(resposta == 'BANCO'):
        print(f'{b1}')

        resposta_banco = ''
        lista_banco = ['SALDO TOTAL','FINANCIAMENTO CLIENTE']

        while (resposta_banco != 'VOLTAR'):
            resposta_banco = str(input("\nVOCÊ QUER ACESSAR O *SALDO TOTAL, *FINANCIAMENTO CLIENTE OU *VOLTAR? ")).upper()

            if(resposta_banco == 'SALDO TOTAL'):
                print(b1.total_valor_contas())
            
            elif(resposta_banco == 'FINANCIAMENTO CLIENTE'):
                cpf=str(input('Digite o CPF para ver a lista de financiamentos do cliente:'))
                print(b1.financiamentos_cliente(cpf))
            
            else:
                print('Erro, tente novamente.')

    elif(resposta == 'FINANCIAMENTO'):
        print(f'{f1}')

        resposta_financiamento = ''
        lista_financiamento = ['RECEBER APORTE']

        while (resposta_financiamento != 'VOLTAR'):
            resposta_financiamento = str(input("\nVOCÊ QUER *RECEBER APORTE OU *VOLTAR? ")).upper()

            if(resposta_financiamento == 'RECEBER APORTE'):
                valor=float(input('Insira o valor a ser retirado do financiamento:'))
                print(f1.receber_aporte(valor))

    elif(resposta not in lista_resposta):
        print("\nTENTE NOVAMENTE. . .")