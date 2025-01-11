# BIBLIOTECA UTILIZADA PARA GERAR CÓDIGO DO ATENDENTE
import random

# BIBLIOTECA IMPORTADA PARA ARQUIVOS
import json
import os

# DICIONARIO DE VACINAS DOS PACIENTES
basevacinas = {}
# ARQUIVO JSON PARA PACIENTES
arquivojsonps = "Dadospaciente.json"
# ARQUIVO JSON PARA ATENDENTES
arquivojsonat = "Dadosatendente.json"
# LISTA PARA ATENDENTES
baseatendentes = []

# LISTA QUE CONTÉM TODOS DICIONARIOS PACIENTES
pacientes_cadastrado = []


# MENU DE OPÇÕES
def menu():
    print('[1], cadastrar atendentes')
    print('[2], cadastrar pacientes')
    print('[3], visualizar status de vacinas dos pacientes')
    print('[4], visualizar atendentes disponiveis')
    print('[5], remover registros de pacientes')
    print('[6], remover resgistros de atendentes')
    print('[7], Sair')
    opcao = int(input('opção:'))
    return opcao


# CARREGA ATENDENTES DENTRO DO ARQUIVO JSON
def carregar_atendentes():
    if os.path.exists(arquivojsonat):
        with open(arquivojsonat, "r+") as arqjson:
            global baseatendentes
            baseatendentes = json.load(arqjson)


# GRAVA ATENDENTES DENTRO DO ARQUIVO JSON
def gravar_dados_JSON_AT():
    with open("Dadosatendente.json", "w+") as arqjson:
        json.dump(baseatendentes, arqjson, indent=True)


# LÊ DADOS DO ARQUIVO
def ler_dados_json_AT():
    with open("Dadosatendente.json", "r+") as arqjson:
        global baseatendentes
        baseatendentes = json.load(arqjson)


# CADASTRO DOS ATENDENTES
def cadastramento_atendentes():
    # carrega atendentes no arquivo
    carregar_atendentes()
    cpfat = int(input('Qual seu número de CPF?'))
    nomeat = input('Qual seu nome completo?')
    codigo = random.randint(0, 99)
    print(f'seu codigo é:{codigo}')

    atendente = [cpfat, nomeat, codigo]
    # ADICIONA DADOS A LISTA
    baseatendentes.append(atendente)
    # GRAVA DADOS NO ARQUIVO
    gravar_dados_JSON_AT()


def listar_dados_at():
    # ATUALIZA DADOS DENTRO DA LISTA
    ler_dados_json_AT()
    for atendente in baseatendentes:
        print(f' CPF: {atendente[0]}')
        print(f' Nome:{atendente[1]}')
        print(f' Código:{atendente[2]}')


# CARREGA PACIENTE DENTRO DO ARQUIVO
def carregar_paciente():
    if os.path.exists(arquivojsonps):
        with open(arquivojsonps, "r+") as arqJson:
            global basevacinas
            baseavacinas = json.load(arqJson)


# GRAVA DADOS DO PACIENTE DENTRO DO ARQUIVO
def gravar_dados_JSON_PC():
    with open("Dadospaciente.json", "w+") as arqJson:
        json.dump(basevacinas, arqJson, indent=True)


# LÊ DADOS DO PACIENTE DENTRO DO ARQUIVO
def ler_dados_json_PC():
    with open("Dadospaciente.json", "r+") as arqJson:
        global basevacinas
        basevacinas = json.load(arqJson)

# CADASTRO DO PACIENTE
def cadastramento_paciente():
    # ADICIONA DADOS DENTRO DO ARQUIVO
    carregar_paciente()

    cpf = int(input('Qual número do seu CPF?'))
    nome = input('Qual seu nome completo?')
    sus = int(input('Qual seu número do sus?'))
    vacina = input('Qual vacina a ser registrada?')
    doses = int(input('quantas doses ministradas?'))

    pacienteX = {"cpf": cpf, "nome": nome, "sus": sus, "vacina": vacina, "doses": doses}

    # ADICIONA DICIONARIO PACIENTE NA LISTA
    pacientes_cadastrado.append(pacienteX)
    grava_Dados_Json()

# CARREGA OS DADOS DENTRO DO ARQUIVO
def grava_Dados_Json():
    with open("Dadospaciente.json", "w+") as arqJson:
        json.dump(pacientes_cadastrado, arqJson, indent=True)

# LISTA STATUS DE VACINA DOS PACIENTES
def listar_status_pc():
    # ATUALIZA DADOS JA INSERIDOS DENTRO DO ARQUIVO
    ler_dados_json_PC()

    for paciente in basevacinas:
        print('Nome:', paciente.get("nome"))
        print('SUS:', paciente.get("sus"))
        print('CPF:', paciente.get("cpf"))
        print('Vacina:', paciente.get("vacina"))
        print('Doses', paciente.get("doses"))
        print('\n')

# REMOVE DADOS DO PACIENTE PELO CPF
def remover_por_cpf_pc():
    cpf_pesquisa = int(input('Digite o CPF do paciente ao qual deseja excluir:'))
    # ABRE ARQUIVO PRA LEITURA
    with open("Dadospaciente.json", 'r') as arqJson:
        pacientes_cadastrado = json.load(arqJson)

        for pacient in pacientes_cadastrado:
            if pacient["cpf"] == cpf_pesquisa:
                print("Sucesso! Paciente {}, com CPF {} excluído.".format(pacient["nome"], pacient["cpf"]))
                pacientes_cadastrado.remove(pacient)
                break
        else:
            print("PACIENTE NÃO ENCONTRADO")

    # GRAVA OS DADOS NOVAMENTE, ATUALIZANDO ELES
    with open("Dadospaciente.json", "w+") as arqJson:
        json.dump(pacientes_cadastrado, arqJson, indent=True)


# REMOVE DADOS DOS ATENDENTES PELO CPF
def remover_por_cpf_at():
    cpf_pesq = int(input('Digite o CPF do atendente ao qual deseja excluir:'))
    # ABRE ARQUIVO PARA LEITURA
    with open('Dadosatendente.json') as arqJson:
        lista_atendentes = json.load(arqJson)

        for atendente in lista_atendentes:
            if atendente[0] == cpf_pesq:
                print("Sucesso! Atendente removido.")
                lista_atendentes.remove(atendente)
                break
        else:
            print("ATENDENTE NÃO ENCONTRADO!")

    # GRAA OS DADOS NOVAMENTE, ATUALIZANDO ELES
    with open("Dadosatendente.json", "w+") as arqJson:
        json.dump(lista_atendentes, arqJson, indent=True)

# FUNÇÃO MAIN PARA CHAMAR OUTRAS FUNÇÕES
def main():
    while True:
        opcaoMenu = menu()
        if opcaoMenu == 1:
            cadastramento_atendentes()
        elif opcaoMenu == 2:
            cadastramento_paciente()
        elif opcaoMenu == 3:
            listar_status_pc()
        elif opcaoMenu == 4:
            listar_dados_at()
        elif opcaoMenu == 5:
            remover_por_cpf_pc()
            pass
        elif opcaoMenu == 6:
            remover_por_cpf_at()
        elif opcaoMenu == 7:
            print('finalizado!')
            break
        else:
            print('opção inválida')


main()