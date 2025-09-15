def mostrar_opcoes():
  print() # Pular uma linha
  print('(1) Incluir.')
  print('(2) Listar.')
  print('(3) Atualizar.')
  print('(4) Excluir.')
  print('(9) Voltar ao menu principal.')
  print() # Pular uma linha

escolha_numero = ""
lista_de_estudantes = []
while escolha_numero != "9":
  print('----- MENU PRINCIPAL -----')
  print() # Pular uma linha
  print('(1) Gerenciar estudantes.')
  print('(2) Gerenciar professores.')
  print('(3) Gerenciar disciplinas.')
  print('(4) Gerenciar turmas.')
  print('(5) Gerenciar matrículas.')
  print('(9) Sair.')
  print() # Pular uma linha
  escolha_numero = input('Informe a opção desejada: ')
  print() # Pular uma linha
  if escolha_numero == "1": 
    escolha_estudantes = "" # Declaração de varíavel
    while escolha_estudantes != "9":
      print('***** [ESTUDANTES] MENU DE OPERAÇÕES *****') 
      mostrar_opcoes()
      escolha_estudantes = input('Informe a opção desejada: ')
      print() # Pular linha
      if escolha_estudantes == "1":
        print('===== INCLUSÃO =====')
        print()
        nome = input('Informe o nome do estudante: ')
        print() # Pular linha
        lista_de_estudantes.append(nome)
      elif escolha_estudantes == "2":
        print('===== LISTAGEM =====')
        print()
        if len(lista_de_estudantes) == 0: #caso lista_de_estudantes esteja vazia 
          print('Não há estudantes cadastrados.')
        else: # Caso o lista de estudantes n esteja vazio
          for estudante in lista_de_estudantes:
            print(f' - {estudante}')
        print() # Pular linha
      elif escolha_estudantes == "3":
        print('AREA ATUALIZAR EM DESENVOLVIMENTO')
        print() # Pular linha
      elif escolha_estudantes == "4":
        print('AREA EXCLUIR EM DESENVOLVIMENTO')
        print() # Pular linha

  elif escolha_numero == "2": 
    print('AREA DE PROFESSORES EM DESENVOLVIMENTO.')
    print() # Pular a linha
  elif escolha_numero == "3":
    print('AREA DE DISCIPLINAS EM DESENVOLVIMENTO.')
    print() # Pular a linha
  elif escolha_numero == "4":
    print('AREA DE TURMAS EM DESENVOLVIMENTO.')
    print() # Pular a linha
  elif escolha_numero == "5":
    print('AREA DE MATRÍCULAS EM DESENVOLVIMENTO.')
    print() # Pular a linha
  elif escolha_numero != "9": 
    print('Opção invalida.')

print() # Pular uma linha
print('===== ATUALIZAÇÃO =====')
print() # Pular uma linha
print('Finalizando aplicação...')