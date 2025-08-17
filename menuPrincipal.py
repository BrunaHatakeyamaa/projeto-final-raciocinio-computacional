def mostrar_opcoes():
  print()
  print('(1) Incluir.')
  print('(2) Listar.')
  print('(3) Atualizar.')
  print('(4) Excluir.')
  print('(9) Voltar ao menu principal.')
  print()

escolha_numero = ""
while escolha_numero != "9":
  print('----- MENU PRINCIPAL -----')
  print()
  print('(1) Gerenciar estudantes.')
  print('(2) Gerenciar professores.')
  print('(3) Gerenciar disciplinas.')
  print('(4) Gerenciar turmas.')
  print('(5) Gerenciar matrículas.')
  print('(9) Sair.')
  print()
  escolha_numero = input('Informe a opção desejada: ')
  print()
  if escolha_numero == "1": 
    escolha_estudantes = ""
    while escolha_estudantes != "9":
      print('***** [ESTUDANTES] MENU DE OPERAÇÕES *****')
      mostrar_opcoes()
      escolha_estudantes = input('Informe a opção desejada:')
  elif escolha_numero == "2":
    escolha_professores = ""
    while escolha_professores != "9": 
      print('***** [PROFESSORES] MENU DE OPERAÇÕES *****')
      mostrar_opcoes()
      escolha_professores = input('Informe a opção desejada:')
  elif escolha_numero == "3":
    escolha_disciplinas = ""
    while escolha_disciplinas != "9":
      print('***** [DISCIPLINAS] MENU DE OPERAÇÕES *****')
      mostrar_opcoes()
      escolha_disciplinas = input('Informe a opção desejada:')
  elif escolha_numero == "4":
    escolha_turmas = ""
    while escolha_turmas != "9":
      print('***** [TURMAS] MENU DE OPERAÇÕES *****')
      mostrar_opcoes()
      escolha_turmas = input('Informe a opção desejada:')
  elif escolha_numero == "5":
    escolha_matriculas = ""
    while escolha_matriculas != "9":
      print('***** [MATRÍCULAS] MENU DE OPERAÇÕES *****')
      mostrar_opcoes()
      escolha_matriculas = input('Informe a opção desejada:')
  elif escolha_numero != "9": 
    print('Opção invalida.')

print()
print('===== ATUALIZAÇÃO =====')
print()
print('Finalizando aplicação...')