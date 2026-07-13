import os
import psycopg2
from dotenv import load_dotenv

#Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

#função para conectar ao PostgreSQL
def conectar():
    conexao = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conexao

#------------- USUARIO

#função para criar a tabela usuario C
def criar_usuario(cpf, nome, data_nascimento, email, telefone, login, senha):
    #insere um novo usuário no banco
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO universidade.usuario (cpf, nome, data_nascimento, email, telefone, login, senha)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (cpf, nome, data_nascimento, email, telefone, login, senha)
        )
        conexao.commit()
        print(f"Usuário {nome} criado com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao criar usuário: {e}")
    finally:
        cursor.close()
        conexao.close()


#função para listar os usuários R
def listar_usuarios():
    #retorna todos os usuários do banco
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT cpf, nome, data_nascimento, email, telefone, login FROM universidade.usuario")
        resultado = cursor.fetchall() #fetchall retorna todas as linhas encontradas
        for linha in resultado:
            print(linha)
            return resultado
    except Exception as e:
        print(f"Erro ao listar usuários: {e}")
    finally:
        cursor.close()
        conexao.close()


#função para buscar um usuário pelo CPF R
def buscar_usuario_por_cpf(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT cpf, nome, data_nascimento, email, telefone, login FROM universidade.usuario WHERE cpf = %s", (cpf,))
        resultado = cursor.fetchone() #fetchone retorna apenas uma linha se encontrada ou NONE
        if resultado:
            print(resultado)
        else:
            print("Usuário não encontrado.")
        return resultado
    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")
    finally:
        cursor.close()
        conexao.close()


#função para atualizar um usuário U
def atualizar_usuario(cpf, nome=None, data_nascimento=None, email=None, telefone= None, login=None, senha=None):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
               """
            UPDATE universidade.usuario
            SET nome = COALESCE(%s, nome),
                data_nascimento = COALESCE(%s, data_nascimento),
                email = COALESCE(%s, email),
                telefone = COALESCE(%s, telefone),
                login = COALESCE(%s, login),
                senha = COALESCE(%s, senha)
            WHERE cpf = %s
            """,
            (nome, data_nascimento, email, telefone, login, senha, cpf)
        )
        if cursor.rowcount == 0:
            print("Usuário não encontrado.")
        else:
            conexao.commit()
            print(f"Usuário {cpf} atualizado com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao atualizar usuário: {e}")
    finally:
        cursor.close()
        conexao.close()


#função para deletar um usuário D
def deletar_usuario(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(  
            "DELETE FROM universidade.usuario WHERE cpf = %s",
            (cpf,)
        )
        if cursor.rowcount == 0:
            print("Usuário não encontrado.")
        else:
            conexao.commit()
            print(f"Usuário {cpf} deletado com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao deletar usuário: {e}")
    finally:
        cursor.close()
        conexao.close()

#------------- CURSO

#função para criar a tabela curso C
def criar_curso(nome, grau, turno, campus, nivel):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO universidade.curso (nome, grau, turno, campus, nivel)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (nome, grau, turno, campus, nivel)
        )
        conexao.commit()
        print(f"Curso {nome} criado com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao criar curso: {e}")
    finally:
        cursor.close()
        conexao.close()


#função para listar os cursos R
def listar_cursos():
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT idcurso, nome, grau, turno, campus, nivel FROM universidade.curso")
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha)
        return resultado
    except Exception as e:
        print(f"Erro ao listar cursos: {e}")
    finally:
        cursor.close()
        conexao.close()


#função para buscar um curso pelo ID R
def buscar_curso_por_id(idcurso):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT idcurso, nome, grau, turno, campus, nivel FROM universidade.curso WHERE idcurso = %s", (idcurso,))
        resultado = cursor.fetchone()
        if resultado:
            print(resultado)
        else:
            print("Curso não encontrado.")
        return resultado
    except Exception as e:
        print(f"Erro ao buscar curso: {e}")
    finally:
        cursor.close()
        conexao.close()


#função para atualizar um curso U
def atualizar_curso(idcurso, nome=None, grau=None, turno=None, campus=None, nivel=None):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            """
            UPDATE universidade.curso
            SET nome = COALESCE(%s, nome),
                grau = COALESCE(%s, grau),
                turno = COALESCE(%s, turno),
                campus = COALESCE(%s, campus),
                nivel = COALESCE(%s, nivel)
            WHERE idcurso = %s
            """,
            (nome, grau, turno, campus, nivel, idcurso)
        )
        if cursor.rowcount == 0:
            print("Curso não encontrado.")
        else:
            conexao.commit()
            print(f"Curso {idcurso} atualizado com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao atualizar curso: {e}")
    finally:
        cursor.close()
        conexao.close()


#função para deletar um curso D
def deletar_curso(idcurso):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "DELETE FROM universidade.curso WHERE idcurso = %s",
            (idcurso,)
        )
        if cursor.rowcount == 0:
            print("Curso não encontrado.")
        else:
            conexao.commit()
            print(f"Curso {idcurso} deletado com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao deletar curso: {e}")
    finally:
        cursor.close()
        conexao.close()

#------------- ESTUDANTE

#função para criar um estudante C
def criar_estudante(mat_estudante, cpf, mc, ano_ingresso):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO universidade.estudante (mat_estudante, cpf, mc, ano_ingresso)
            VALUES (%s, %s, %s, %s)
            """,
            (mat_estudante, cpf, mc, ano_ingresso)
        )
        conexao.commit()
        print(f"Estudante {mat_estudante} criado com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao criar estudante: {e}")
    finally:
        cursor.close()
        conexao.close()


#função para listar todos os estudantes R
def listar_estudantes():
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT mat_estudante, cpf, mc, ano_ingresso FROM universidade.estudante")
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha)
        return resultado
    except Exception as e:
        print(f"Erro ao listar estudantes: {e}")
    finally:
        cursor.close()
        conexao.close()


#função para buscar um estudante pela matrícula R
def buscar_estudante_por_matricula(mat_estudante):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "SELECT mat_estudante, cpf, mc, ano_ingresso FROM universidade.estudante WHERE mat_estudante = %s",
            (mat_estudante,)
        )
        resultado = cursor.fetchone()
        if resultado:
            print(resultado)
        else:
            print("Estudante não encontrado.")
        return resultado
    except Exception as e:
        print(f"Erro ao buscar estudante: {e}")
    finally:
        cursor.close()
        conexao.close()


#função para atualizar um estudante U
def atualizar_estudante(mat_estudante, cpf=None, mc=None, ano_ingresso=None):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            """
            UPDATE universidade.estudante
            SET cpf = COALESCE(%s, cpf),
                mc = COALESCE(%s, mc),
                ano_ingresso = COALESCE(%s, ano_ingresso)
            WHERE mat_estudante = %s
            """,
            (cpf, mc, ano_ingresso, mat_estudante)
        )
        if cursor.rowcount == 0:
            print("Estudante não encontrado.")
        else:
            conexao.commit()
            print(f"Estudante {mat_estudante} atualizado com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao atualizar estudante: {e}")
    finally:
        cursor.close()
        conexao.close()


#função para deletar um estudante D
def deletar_estudante(mat_estudante):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "DELETE FROM universidade.estudante WHERE mat_estudante = %s",
            (mat_estudante,)
        )
        if cursor.rowcount == 0:
            print("Estudante não encontrado.")
        else:
            conexao.commit()
            print(f"Estudante {mat_estudante} deletado com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao deletar estudante: {e}")
    finally:
        cursor.close()
        conexao.close()

#------------- VINCULO
#função para criar um vínculo C
def criar_vinculo(mat_estudante, curso, data_entrada, status, data_saida=None):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO universidade.vinculo (mat_estudante, curso, data_entrada, status, data_saida)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (mat_estudante, curso, data_entrada, status, data_saida)
        )
        conexao.commit()
        print(f"Vínculo do estudante {mat_estudante} criado com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao criar vínculo: {e}")
    finally:
        cursor.close()
        conexao.close()

#função para listar todos os vínculos R
def listar_vinculos():
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT idvinculo, mat_estudante, curso, data_entrada, status, data_saida FROM universidade.vinculo")
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha)
        return resultado
    except Exception as e:
        print(f"Erro ao listar vínculos: {e}")
    finally:
        cursor.close()
        conexao.close()

#função para buscar um vínculo pelo ID R
def buscar_vinculo_por_id(idvinculo):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "SELECT idvinculo, mat_estudante, curso, data_entrada, status, data_saida FROM universidade.vinculo WHERE idvinculo = %s",
            (idvinculo,)
        )
        resultado = cursor.fetchone()
        if resultado:
            print(resultado)
        else:
            print("Vínculo não encontrado.")
        return resultado
    except Exception as e:
        print(f"Erro ao buscar vínculo: {e}")
    finally:
        cursor.close()
        conexao.close()

#função para atualizar um vínculo U
def atualizar_vinculo(idvinculo, mat_estudante=None, curso=None, data_entrada=None, status=None, data_saida=None):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            """
            UPDATE universidade.vinculo
            SET mat_estudante = COALESCE(%s, mat_estudante),
                curso = COALESCE(%s, curso),
                data_entrada = COALESCE(%s, data_entrada),
                status = COALESCE(%s, status),
                data_saida = COALESCE(%s, data_saida)
            WHERE idvinculo = %s
            """,
            (mat_estudante, curso, data_entrada, status, data_saida, idvinculo)
        )
        if cursor.rowcount == 0:
            print("Vínculo não encontrado.")
        else:
            conexao.commit()
            print(f"Vínculo {idvinculo} atualizado com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao atualizar vínculo: {e}")
    finally:
        cursor.close()
        conexao.close()

#função para deletar um vínculo D
def deletar_vinculo(idvinculo):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "DELETE FROM universidade.vinculo WHERE idvinculo = %s",
            (idvinculo,)
        )
        if cursor.rowcount == 0:
            print("Vínculo não encontrado.")
        else:
            conexao.commit()
            print(f"Vínculo {idvinculo} deletado com sucesso!")
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao deletar vínculo: {e}")
    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    deletar_vinculo(999)      # não existe, deve avisar
    deletar_vinculo(1)        # existe, deve remover
    listar_vinculos()         # deve vir vazio