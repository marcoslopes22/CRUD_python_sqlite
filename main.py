import personDatabase;

def imprimirTela():
    pessoa = personDatabase.Pessoa();
    print("=====================================================================");
    print("\nMENU DE FUNCIONALIDADES\n");
    statusLista = pessoa.verificarLista();
    if statusLista: print("1. Ler registros\n2. Cadastrar aluno\n3. Atualizar dados\n4. Deletar registros\n5. Sair");
    else: print("1. Ler registros\n2. Cadastrar aluno\n5. Sair");

if(__name__=="__main__"):

    funcionalidade = int(0);

    while(funcionalidade != 5):
        pessoa = personDatabase.Pessoa();
        imprimirTela();
        try:
            funcionalidade = int(input("\nEscolha a funcionalidade: "));
            match funcionalidade:
                case 1:
                    print("1. Ler cadastros...");
                    statusLista = pessoa.verificarLista();
                    if statusLista: pessoa.ler();
                    else: print("\nNão há alunos cadastrados no sistema!");

                case 2:
                    print("2. Cadastrar aluno...");
                    nome    = str(input("\nDigite o nome do aluno: "));
                    idade   = str(input("Digite a idade do aluno: "));
                    print(f"\nAluno(a): {nome} Idade: {idade} anos");
                    pessoa.cadastrar(nome, idade);
                    idRegistro  = str("");
                    confirmar   = pessoa.pesquisar(idRegistro, nome, idade);
                    if confirmar: print("Cadastrado com sucesso!");
                    else: print("Não foi possível cadastrar esse aluno!");

                case 3:
                    statusLista = pessoa.verificarLista();
                    if statusLista:
                        print("Atualizar dados...");
                        pessoa.ler();
                        idRegistro  = str(input("Informe o Id de registro: "));
                        nome    = str("");
                        idade   = str("");
                        resultadoPesquisa = pessoa.pesquisar(idRegistro, nome, idade);
                        while resultadoPesquisa == False:
                            print("Id de registro não está cadastrado! Tente novamente.");
                            idRegistro = str(input("Informe o Id de registro: "));
                            nome    = str("");
                            idade   = str("");
                            resultadoPesquisa = pessoa.pesquisar(idRegistro, nome, idade);
                        for i in resultadoPesquisa:
                            print(f"Registro encontrado: ID: {i[0]}, Nome: {i[1]}, Idade: {i[2]} anos");
                        print("\n");
                        propriedades = int(0);
                        while propriedades < int(1) or propriedades > int(3):
                            propriedades = int(input("Quais propriedades você deseja atualizar?\n1. Apenas nome\n2. Apenas idade\n3. Ambos\n\nEscolher: "));
                            match propriedades:
                                case 1:
                                    idade   = str("");
                                    nome    = str(input("Digite o novo nome: "));
                                    pessoa.atualizar(propriedades, idRegistro, nome, idade);
                                case 2:
                                    nome    = str("");
                                    idade   = str(input("Digite a nova idade: "));
                                    pessoa.atualizar(propriedades, idRegistro, nome, idade);
                                case 3:
                                    nome    = str(input("Digite o novo nome: "));
                                    idade   = str(input("Digite a nova idade: "));
                                    pessoa.atualizar(propriedades, idRegistro, nome, idade);
                                case _: print("\nOperação inválida! Tente novamente.");
                    else: print("Operação Inválida! Não há alunos cadastrados no sistema!");
                case 4:
                    statusLista = pessoa.verificarLista();
                    if statusLista:
                        print("4. Deletar dados...");
                        pessoa.ler();
                        idRegistro = str(input("Informe o Id de registro: "));
                        nome    = str("");
                        idade   = str("");
                        resultadoPesquisa = pessoa.pesquisar(idRegistro, nome, idade);
                        while resultadoPesquisa == False:
                            print("Id de registro não está cadastrado! Tente novamente.");
                            idRegistro = str(input("Informe o Id de registro: "));
                            nome    = str("");
                            idade   = str("");
                            resultadoPesquisa = pessoa.pesquisar(idRegistro, nome, idade);
                        for i in resultadoPesquisa:
                            print(f"Confirmar registro: ID: {i[0]}, Nome: {i[1]}, Idade: {i[2]} anos");
                        print("\n");
                        confirmar = int(0);
                        while confirmar < 1 and confirmar > 2:
                            confirmar = int(input("Tem certeza que deseja excluir o registro?\n1. Sim\n2. Não, cancelar: "));
                            match confirmar:
                                case 1: pessoa.deletar(idRegistro);
                                case 2: print("Exclusão de registro cancelada com sucesso...");
                                case _: print("Operação inválida! Tente novamente.");
                    else: print("Operação Inválida! Não há alunos cadastrados no sistema!");
                case 5: print("5. Saindo do sistema...");
                case _: print("ERRO: Esta funcionalidade não existe. Tente novamente.");
        except:
            print("Por favor, escolha somente números.");