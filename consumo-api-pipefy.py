###########################################################################################################
#                                                                                                         #
#                                       INTERAÇÃO API PIPEFY - 2022                                       #
#                                                                                                         #
###########################################################################################################
#                                                                                                         #
#       - 1 - Realizado a conexão com o PIPEFY                                                            #
#       - 2 -                                                                                             #
#       - 3 -                                                                                             #
#       - 4 -                                                                                             #
#                                                                                                         #
#                                                                                                         #
#                                                          Implementado dia: /01/2022  - Lucas Estefano   #
###########################################################################################################
#                                                                                                         #     
#                                           FORMATO JSON                                                  #
#                                                 |                                                       #
#                                                 |                                                       #
#                                                 ↓                                                       #
###########################################################################################################
#                                                                                                         #
#                                                                                                         #
#                                                                                                         #
###########################################################################################################


# -*- coding: utf-8 -*-
import json
import requests
import time

#Timer de execução do Robô
timerCod = time.time()

#Conexão com o Pipefy





#POST API Python
data = {
    "data": {
                "IBGE": "1100051",
                "IBGE7": "1100023",
                "UF": "RO",
                "Municipio": "Alta Floresta D´oeste",
                "Municipio_sem_titulo": "Alta Floresta Doeste",
                "Regiao": "Região Norte",
                "Populcao": "24392",
                "Porte": "Pequeno II",
                "Capital": ""
    }
}


autenticacao = ('token', 'exemplo')
url = 'endpoint'
r = requests.post(url, json= data, auth=autenticacao)
#print('Dados inseridos: ', i1, '  Status code:', r.status_code)
#print(f"Status Code: {r.status_code}, Response: {r.json()}")


print('*--------------------------------------------------------------------*')
#print('Foram inseridos no total:', i1 ,'dados na API.')
print('*---------------------------------------------------------------------*')


#tempoExec = time.time() -timerCod
#print('O tempo de execução do robô foi de: {} Segundos.'.format(tempoExec))
print('*---------------------------------------------------------------------*')

 
    


    


##############################################################################

#######GET API Python
#requisicao = requests.get("http://10.61.228.86:1337/api/contato-parceiros")
#print(requisicao)
#print(requisicao.json())
