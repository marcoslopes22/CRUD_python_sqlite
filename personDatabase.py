import sqlite3

# ESCOLA TÉCNICA ESTADUAL PORTO DIGITAL;
# ALUNO: MARCOS AURÉLIO LOPES DE ARAÚJO;
# DESENVOLVIMENTO DE SISTEMAS, MÓDULO II;
# DISCIPLINA: LÓDIGA DE PROGRAMAÇÃO - PROFESSOR CLOVIS ROCHA;

# ATIVIDADE: CRUD COM PYTHON E SQLITE3;

class Pessoa:

    # CONSTRUTOR;
    def __init__(self):
        try: 
            self.__conn = sqlite3.connect('persons_db.db');
            self.__cur = self.__conn.cursor();
            self.criarTabela();
        except:
            print("Erro na conexão!");

    # CRIAR TABELA SE A MESMA NÃO EXISTIR;
    def criarTabela(self):
        try:
            self.__cur.execute("CREATE TABLE IF NOT EXISTS pessoas (id INTEGER PRIMARY KEY, nome VARCHAR(45) NOT NULL, idade VARCHAR(3) NOT NULL)");
            self.__conn.commit();
        except:
            print("Erro ao tentar criar tabela!");

    # CADASTRAR;
    def cadastrar(self, nome, idade):
        self.__cur.execute(f"INSERT INTO pessoas (nome,idade) VALUES ('{nome}','{idade}')");
        self.__conn.commit();

    # LER;
    def ler(self):
        self.__cur.execute(f"SELECT * FROM pessoas ORDER BY id");
        self.__conn.commit();
        result = self.__cur.fetchall();
        print("=====================================================================");
        print("\nLISTA DE ALUNOS CADASTRADOS:\n");
        for i in result: print(f"ID: {i[0]}, Nome: {i[1]}, Idade: {i[2]} anos");
        print("\n");
    
    # VERIFICAR SE HÁ REGISTROS NA LISTA;  
    def verificarLista(self):
        self.__cur.execute("SELECT * FROM pessoas");
        self.__conn.commit();
        result = self.__cur.fetchall();
        if result == []: return False;
        elif result != []: return True;

    # ATUALIZAR;
    def atualizar(self, propriedades, idRegistro, nome, idade):
        if propriedades == 1:
            self.__cur.execute(f"UPDATE pessoas SET nome='{nome}' WHERE id='{idRegistro}'");
            self.__conn.commit();
        elif propriedades == 2:
            self.__cur.execute(f"UPDATE pessoas SET idade='{idade}' WHERE id='{idRegistro}'");
            self.__conn.commit();
        elif propriedades == 3:
            self.__cur.execute(f"UPDATE pessoas SET nome='{nome}', idade='{idade}' WHERE id='{idRegistro}'");
            self.__conn.commit();

    # DELETAR;
    def deletar(self, idRegistro):
        self.__cur.execute(f"DELETE FROM pessoas WHERE id='{idRegistro}'");
        self.__conn.commit();
    
    # PESQUISAR;
    def pesquisar(self, idRegistro, nome, idade):
        # ESCOLHER O PARÂMETRO DE PESQUISA;
        if idRegistro != "" and nome == "" and idade == "":
            self.__cur.execute(f"SELECT * FROM pessoas WHERE id='{idRegistro}'");
            self.__conn.commit();
            result = self.__cur.fetchall();
            if result == []: return False;
            elif result != []: return result;

        elif idRegistro == "" and nome != "" and idade != "":
            self.__cur.execute(f"SELECT * FROM pessoas WHERE nome='{nome}' and idade='{idade}'");
            self.__conn.commit();
            result = self.__cur.fetchall();
            if result == []: return False;
            elif result != []: return True;
                
