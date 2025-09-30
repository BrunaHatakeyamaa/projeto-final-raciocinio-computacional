'''
BRUNA HATAKEYAMA 
MATRICULA: 1112025201420
ANALISE E DESENVOLVIMENTO DE SISTEMAS
SISTEMA DE GERENCIAMENTO ESCOLAR
'''
import json

nome_arquivo_estudantes = "arquivo_do_estudante.json"
nome_arquivo_professores = "arquivo_do_professor.json"
nome_arquivo_disciplinas = "arquivo_da_disciplina.json"
nome_arquivo_turmas = "arquivo_da_turma.json"
nome_arquivo_matriculas = "arquivo_de_matricula.json"

def mostrar_menu():
  print('----- MENU PRINCIPAL -----')
  print() # Pular uma linha
  print('(1) Gerenciar estudantes.')
  print('(2) Gerenciar professores.')
  print('(3) Gerenciar disciplinas.')
  print('(4) Gerenciar turmas.')
  print('(5) Gerenciar matrículas.')
  print('(9) Sair.')
  print() # Pular uma linha

def mostrar_opcoes():
  print() # Pular uma linha
  print('(1) Incluir.')
  print('(2) Listar.')
  print('(3) Atualizar.')
  print('(4) Excluir.')
  print('(9) Voltar ao menu principal.')
  print() # Pular uma linha

def escrever_arquivo(nome_arquivo, conteudo):
  with open(nome_arquivo, "w") as f:
    json.dump(conteudo, f)

def ler_arquivo(nome_arquivo):
  try: 
    with open(nome_arquivo, "r") as f:
      return json.load(f)
  except Exception as e:
    return []

def listar(nome_arquivo):
  lista = ler_arquivo(nome_arquivo)
  if len(lista) == 0: #caso lista esteja vazia 
    print('Não há dados cadastrados.')
  else: # Caso o lista n esteja vazio
    for objeto in lista:
      print(f' - {objeto}')

def esta_cadastrado_codigo(codigo, nome_arquivo):
  lista = ler_arquivo(nome_arquivo)
  for objeto in lista:
    if objeto['codigo'] == codigo:
      return True
  return False 

def incluir(objeto, nome_arquivo):
  lista = ler_arquivo(nome_arquivo)
  lista.append(objeto)
  escrever_arquivo(nome_arquivo, lista)

def incluir_estudante():
  print('===== INCLUSÃO =====')
  print()
  try:
    codigo = int(input('Informe o código do estudante: '))
    nome = input('Informe o nome do estudante: ')
    cpf = input('Informe o CPF do estudante: ')
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')
  else:
    print() # Pular linha
    novo_estudante = {'codigo': codigo, 'nome': nome, 'cpf': cpf }
    if esta_cadastrado_codigo(codigo, nome_arquivo_estudantes):
      print('CÓDIGO JÁ CADASTRADO. TENTE NOVAMENTE.')
    else:
      incluir(novo_estudante, nome_arquivo_estudantes)

def incluir_professor():
  print('===== INCLUSÃO =====')
  print()
  try:
    codigo = int(input('Informe o código do professor: '))
    nome = input('Informe o nome do professor: ')
    cpf = input('Informe o CPF do professor: ')
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')
  else:
    print() # Pular linha
    novo_professor = {'codigo': codigo, 'nome': nome, 'cpf': cpf }
    if esta_cadastrado_codigo(codigo, nome_arquivo_professores):
      print('CÓDIGO JÁ CADASTRADO. TENTE NOVAMENTE.')
    else:
      incluir(novo_professor, nome_arquivo_professores)

def incluir_disciplinas():
  print('===== INCLUSÃO =====')
  print()
  try:
    codigo = int(input('Informe o código da disciplina: '))
    nome = input('Informe o nome da disciplina: ')
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')
  else:
    print() # Pular linha
    nova_disciplina = {'codigo': codigo, 'nome': nome }
    if esta_cadastrado_codigo(codigo, nome_arquivo_disciplinas):
      print('CÓDIGO JÁ CADASTRADO. TENTE NOVAMENTE.')
    else:
      incluir(nova_disciplina, nome_arquivo_disciplinas)

def incluir_turmas():
  print('===== INCLUSÃO =====')
  print()
  try:
    codigo = int(input('Informe o código da turma: '))
    codigo_professor = int(input('Informe o código do professor: '))
    codigo_disciplina = int(input('Informe o código da disciplina: '))
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')
  else:
    print() # Pular linha
    nova_turma = {'codigo': codigo, 'codigo_professor': codigo_professor, 'codigo_disciplina': codigo_disciplina }
    if esta_cadastrado_codigo(codigo, nome_arquivo_turmas):
      print('CÓDIGO JÁ CADASTRADO. TENTE NOVAMENTE.')
    else:
     incluir(nova_turma, nome_arquivo_turmas)

def incluir_matricula():
  print('===== INCLUSÃO =====')
  print()
  try:
    codigo = int(input('Informe o código da matricula: '))
    codigo_turma = int(input('Informe o código da turma: '))
    codigo_estudante = int(input('Informe o código do estudante: '))
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')
  else:
    print() # Pular linha
    nova_matricula = {'codigo': codigo, 'codigo_turma': codigo_turma, 'codigo_estudante': codigo_estudante }
    if esta_cadastrado_codigo(codigo, nome_arquivo_matriculas):
      print('CÓDIGO JÁ CADASTRADO. TENTE NOVAMENTE.')
    else:
      incluir(nova_matricula, nome_arquivo_matriculas)

def atualizar(codigo, novo_objeto, nome_arquivo):
  lista = ler_arquivo(nome_arquivo)
  index_codigo = -1
  for objeto in lista:
    if objeto['codigo'] == codigo:
      index_codigo = lista.index(objeto)
  if index_codigo >= 0:
    lista[index_codigo] = novo_objeto
  else:
    print('CÓDIGO NÃO ENCONTRADO')
  escrever_arquivo(nome_arquivo, lista)

def atualizar_estudante():
  print('===== ATUALIZAR =====')
  print() # Pular linha
  try:
    codigo = int(input('Informe o código do estudante: '))
    novo_codigo = int(input('Informe o novo código do estudante: '))
    novo_nome = input('Informe o novo nome do estudante: ')
    novo_cpf = input('Informe o novo CPF do estudante: ')
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')
  else:
    novo_estudante = {'codigo': novo_codigo, 'nome': novo_nome, 'cpf': novo_cpf }
    if novo_codigo != codigo and esta_cadastrado_codigo(novo_codigo, nome_arquivo_estudantes):
      print('CÓDIGO JÁ CADASTRADO. TENTE NOVAMENTE.')
    else:
      atualizar(codigo, novo_estudante, nome_arquivo_estudantes)

def atualizar_professor():
  print('===== ATUALIZAR =====')
  print() # Pular linha
  try:
    codigo = int(input('Informe o código do professor: '))
    novo_codigo = int(input('Informe o novo código do professor: '))
    novo_nome = input('Informe o novo nome do professor: ')
    novo_cpf = input('Informe o novo CPF do professor: ')
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')
  else:
    novo_professor = {'codigo': novo_codigo, 'nome': novo_nome, 'cpf': novo_cpf }
    if novo_codigo != codigo and esta_cadastrado_codigo(novo_codigo, nome_arquivo_professores):
      print('CÓDIGO JÁ CADASTRADO. TENTE NOVAMENTE.')
    else:
      atualizar(codigo, novo_professor, nome_arquivo_professores)

def atualizar_disciplinas():
  print('===== ATUALIZAR =====')
  print() # Pular linha
  try:
    codigo = int(input('Informe o código da disciplina: '))
    novo_codigo = int(input('Informe o novo código da disciplina: '))
    novo_nome = input('Informe o novo nome da disciplina: ')
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')
  else:
    nova_disciplina = {'codigo': novo_codigo, 'nome': novo_nome }
    if novo_codigo != codigo and esta_cadastrado_codigo(novo_codigo, nome_arquivo_disciplinas):
      print('CÓDIGO JÁ CADASTRADO. TENTE NOVAMENTE.')
    else:
      atualizar(codigo, nova_disciplina, nome_arquivo_disciplinas)

def atualizar_turmas():
  print('===== ATUALIZAR =====')
  print() # Pular linha
  try:
    codigo = int(input('Informe o código da turma: '))
    novo_codigo = int(input('Informe o novo código da turma: '))
    novo_codigo_professor = int(input('Informe o novo código do professor: '))
    novo_codigo_disciplina = int(input('Informe o novo código da disciplina: '))
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')
  else:
    nova_turma = {'codigo': novo_codigo, 'codigo_professor': novo_codigo_professor, 'codigo_disciplina': novo_codigo_disciplina }
    if novo_codigo != codigo and esta_cadastrado_codigo(novo_codigo, nome_arquivo_turmas):
      print('CÓDIGO JÁ CADASTRADO. TENTE NOVAMENTE.')
    else:
      atualizar(codigo, nova_turma, nome_arquivo_turmas)

def atualizar_matriculas():
  print('===== ATUALIZAR =====')
  print() # Pular linha
  try:
    codigo = int(input('Informe o código da matricula: '))
    novo_codigo = int(input('Informe o novo código da matricula: '))
    novo_codigo_turma = int(input('Informe o novo código da turma: '))
    novo_codigo_estudante = int(input('Informe o novo código do estudante: '))
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')
  else:
    nova_matricula = {'codigo': novo_codigo, 'codigo_turma': novo_codigo_turma, 'codigo_estudante': novo_codigo_estudante }
    if novo_codigo != codigo and esta_cadastrado_codigo(novo_codigo, nome_arquivo_matriculas):
      print('CÓDIGO JÁ CADASTRADO. TENTE NOVAMENTE.')
    else:
      atualizar(codigo, nova_matricula, nome_arquivo_matriculas)

def remover(codigo, nome_arquivo):
  lista = ler_arquivo(nome_arquivo)
  for objeto in lista:
    if objeto['codigo'] == codigo:
      lista.remove(objeto)
  escrever_arquivo(nome_arquivo, lista)

def remover_estudante():
  print('===== EXCLUSÃO =====')
  print() # Pular linha
  try:
    codigo = int(input('Informe o código do estudante: '))
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')  
  else:
    if not esta_cadastrado_codigo(codigo, nome_arquivo_estudantes):
      print('CÓDIGO NÃO ENCONTRADO. TENTE NOVAMENTE.')
    else:
      remover(codigo, nome_arquivo_estudantes)
  

def remover_professor():
  print('===== EXCLUSÃO =====')
  print() # Pular linha
  try:
    codigo = int(input('Informe o código do professor: '))
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')  
  else:
    if not esta_cadastrado_codigo(codigo, nome_arquivo_professores):
      print('CÓDIGO NÃO ENCONTRADO. TENTE NOVAMENTE.')
    else:
      remover(codigo, nome_arquivo_professores)

def remover_disciplinas():
  print('===== EXCLUSÃO =====')
  print() # Pular linha
  try:
    codigo = int(input('Informe o código da disciplina: '))
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')  
  else:
    if not esta_cadastrado_codigo(codigo, nome_arquivo_disciplinas):
      print('CÓDIGO NÃO ENCONTRADO. TENTE NOVAMENTE.')
    else:
      remover(codigo, nome_arquivo_disciplinas)

def remover_turma():
  print('===== EXCLUSÃO =====')
  print() # Pular linha
  try:
    codigo = int(input('Informe o código da turma: '))
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')  
  else:
    if not esta_cadastrado_codigo(codigo, nome_arquivo_turmas):
      print('CÓDIGO NÃO ENCONTRADO. TENTE NOVAMENTE.')
    else:
      remover(codigo, nome_arquivo_turmas)

def remover_matricula():
  print('===== EXCLUSÃO =====')
  print() # Pular linha
  try:
    codigo = int(input('Informe o código da matricula: '))
  except Exception as e:
    print('DADOS INVÁLIDOS. TENTE NOVAMENTE.')  
  else:
    if not esta_cadastrado_codigo(codigo, nome_arquivo_matriculas):
      print('CÓDIGO NÃO ENCONTRADO. TENTE NOVAMENTE.')
    else:
      remover(codigo, nome_arquivo_matriculas)

escolha_numero = ""
while escolha_numero != "9":
  mostrar_menu()
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
        incluir_estudante()
      elif escolha_estudantes == "2":
        print('===== LISTAGEM =====')
        print()
        listar(nome_arquivo_estudantes)
        print() # Pular linha
      elif escolha_estudantes == "3":
        atualizar_estudante()
      elif escolha_estudantes == "4":
        remover_estudante()
  elif escolha_numero == "2": 
    escolha_professores = "" # Declaração de varíavel
    while escolha_professores != "9":
      print('***** [PROFESSORES] MENU DE OPERAÇÕES *****') 
      mostrar_opcoes()
      escolha_professores = input('Informe a opção desejada: ')
      print() # Pular linha
      if escolha_professores == "1":
        incluir_professor()
      elif escolha_professores == "2":
        print('===== LISTAGEM =====')
        print()
        listar(nome_arquivo_professores)
        print() # Pular linha
      elif escolha_professores == "3":
        atualizar_professor()
      elif escolha_professores == "4":
        remover_professor()
  elif escolha_numero == "3":
    escolha_disciplinas = "" # Declaração de varíavel
    while escolha_disciplinas != "9":
      print('***** [DISCIPLINAS] MENU DE OPERAÇÕES *****') 
      mostrar_opcoes()
      escolha_disciplinas = input('Informe a opção desejada: ')
      print() # Pular linha
      if escolha_disciplinas == "1":
        incluir_disciplinas()
      elif escolha_disciplinas == "2":
        print('===== LISTAGEM =====')
        print()
        listar(nome_arquivo_disciplinas)
        print() # Pular linha
      elif escolha_disciplinas == "3":
        atualizar_disciplinas()
      elif escolha_disciplinas == "4":
        remover_disciplinas()
  elif escolha_numero == "4":
    escolha_turmas = "" # Declaração de varíavel
    while escolha_turmas != "9":
      print('***** [TURMAS] MENU DE OPERAÇÕES *****') 
      mostrar_opcoes()
      escolha_turmas = input('Informe a opção desejada: ')
      print() # Pular linha
      if escolha_turmas == "1":
        incluir_turmas()
      elif escolha_turmas == "2":
        print('===== LISTAGEM =====')
        print()
        listar(nome_arquivo_turmas)
        print() # Pular linha
      elif escolha_turmas == "3":
        atualizar_turmas()
      elif escolha_turmas == "4":
        remover_turma()
  elif escolha_numero == "5":
    escolha_matriculas = "" # Declaração de varíavel
    while escolha_matriculas != "9":
      print('***** [MATRICULAS] MENU DE OPERAÇÕES *****') 
      mostrar_opcoes()
      escolha_matriculas = input('Informe a opção desejada: ')
      print() # Pular linha
      if escolha_matriculas == "1":
        incluir_matricula()
      elif escolha_matriculas == "2":
        print('===== LISTAGEM =====')
        print()
        listar(nome_arquivo_matriculas)
        print() # Pular linha
      elif escolha_matriculas == "3":
        atualizar_matriculas()
      elif escolha_matriculas == "4":
        remover_matricula()
  elif escolha_numero != "9": 
    print('Opção invalida.')

print() # Pular uma linha
print('===== ATUALIZAÇÃO =====')
print() # Pular uma linha
print('Finalizando aplicação...')