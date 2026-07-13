import os
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId

#Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

#função para conectar ao MongoDB
def conectar_mongo():
    cliente = MongoClient(
        host=os.getenv("MONGO_HOST"),
        port=int(os.getenv("MONGO_PORT")),
        username=os.getenv("MONGO_USER"),
        password=os.getenv("MONGO_PASSWORD"),
        authSource=os.getenv("MONGO_AUTH_SOURCE")
    )
    banco = cliente[os.getenv("MONGO_DB")]
    return banco

#------------- ESTUDANTES

#função para criar um estudante C
def criar_estudante(mat_estudante, cpf, nome, data_nascimento, email, telefone,
                     login, senha, mc, ano_ingresso):
    banco = conectar_mongo()
    colecao = banco["estudantes"]
    try:
        documento = {
            "_id": mat_estudante,
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "email": email,
            "telefone": telefone,
            "login": login,
            "senha": senha,
            "mc": mc,
            "ano_ingresso": ano_ingresso
        }
        colecao.insert_one(documento)
        print(f"Estudante {mat_estudante} criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar estudante: {e}")


#função para listar um estudante R
def listar_estudantes():
    banco = conectar_mongo()
    colecao = banco["estudantes"]
    try:
        resultado = list(colecao.find())
        for documento in resultado:
            print(documento)
        return resultado
    except Exception as e:
        print(f"Erro ao listar estudantes: {e}")


#função para buscar um estudante R
def buscar_estudante_por_matricula(mat_estudante):
    banco = conectar_mongo()
    colecao = banco["estudantes"]
    try:
        resultado = colecao.find_one({"_id": mat_estudante})
        if resultado:
            print(resultado)
        else:
            print("Estudante não encontrado.")
        return resultado
    except Exception as e:
        print(f"Erro ao buscar estudante: {e}")


#função para atualizar um estudante U
def atualizar_estudante(mat_estudante, cpf=None, nome=None, data_nascimento=None, email=None, telefone=None, login=None, senha=None, mc=None, ano_ingresso=None):
    banco = conectar_mongo()
    colecao = banco["estudantes"]
    try:
        campos_atualizados = {}
        if cpf is not None:
            campos_atualizados["cpf"] = cpf
        if nome is not None:
            campos_atualizados["nome"] = nome
        if data_nascimento is not None:
            campos_atualizados["data_nascimento"] = data_nascimento
        if email is not None:
            campos_atualizados["email"] = email
        if telefone is not None:
            campos_atualizados["telefone"] = telefone
        if login is not None:
            campos_atualizados["login"] = login
        if senha is not None:
            campos_atualizados["senha"] = senha
        if mc is not None:
            campos_atualizados["mc"] = mc
        if ano_ingresso is not None:
            campos_atualizados["ano_ingresso"] = ano_ingresso

        if not campos_atualizados:
            print("Nenhum campo para atualizar.")
            return

        resultado = colecao.update_one({"_id": mat_estudante}, {"$set": campos_atualizados})
        if resultado.matched_count == 0:
            print("Estudante não encontrado.")
        else:
            print(f"Estudante {mat_estudante} atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar estudante: {e}")


#função para deletar um estudante D
def deletar_estudante(mat_estudante):
    banco = conectar_mongo()
    colecao = banco["estudantes"]
    try:
        resultado = colecao.delete_one({"_id": mat_estudante})
        if resultado.deleted_count == 0:
            print("Estudante não encontrado.")
        else:
            print(f"Estudante {mat_estudante} deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar estudante: {e}")


#------------- CURSOS  
def criar_curso(idCurso, nome, grau, turno, campus, nivel):
    banco = conectar_mongo()
    colecao = banco["cursos"]
    try:
        documento = {
            "_id": idCurso,
            "nome": nome,
            "grau": grau,
            "turno": turno,
            "campus": campus,
            "nivel": nivel
        }
        colecao.insert_one(documento)
        print(f"Curso {idCurso} criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar curso: {e}")


#função para listar cursos R
def listar_cursos():
    banco = conectar_mongo()
    colecao = banco["cursos"]
    try:
        resultado = list(colecao.find())
        for documento in resultado:
            print(documento)
        return resultado
    except Exception as e:
        print(f"Erro ao listar cursos: {e}")


#função para buscar um curso R
def buscar_curso_por_id(idCurso):
    banco = conectar_mongo()
    colecao = banco["cursos"]
    try:
        resultado = colecao.find_one({"_id": idCurso})
        if resultado:
            print(resultado)
        else:
            print("Curso não encontrado.")
        return resultado
    except Exception as e:
        print(f"Erro ao buscar curso: {e}")


#função para atualizar um curso U
def atualizar_curso(idCurso, nome=None, grau=None, turno=None, campus=None, nivel=None):
    banco = conectar_mongo()
    colecao = banco["cursos"]
    try:
        campos_atualizados = {}
        if nome is not None:
            campos_atualizados["nome"] = nome
        if grau is not None:
            campos_atualizados["grau"] = grau
        if turno is not None:
            campos_atualizados["turno"] = turno
        if campus is not None:
            campos_atualizados["campus"] = campus
        if nivel is not None:
            campos_atualizados["nivel"] = nivel

        if not campos_atualizados:
            print("Nenhum campo para atualizar.")
            return

        resultado = colecao.update_one({"_id": idCurso}, {"$set": campos_atualizados})
        if resultado.matched_count == 0:
            print("Curso não encontrado.")
        else:
            print(f"Curso {idCurso} atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar curso: {e}")


#função para deletar um curso D
def deletar_curso(idCurso):
    banco = conectar_mongo()
    colecao = banco["cursos"]
    try:
        resultado = colecao.delete_one({"_id": idCurso})
        if resultado.deleted_count == 0:
            print("Curso não encontrado.")
        else:
            print(f"Curso {idCurso} deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar curso: {e}")


#------------- VINCULO
def criar_vinculo(mat_estudante, curso_id, data_entrada, status, data_saida=None):
    banco = conectar_mongo()
    colecao = banco["vinculos"]
    try:
        # Checagem manual de integridade referencial, pois não há suporte nativo no MongoDB
        if banco["estudantes"].find_one({"_id": mat_estudante}) is None:
            print(f"Erro ao criar vínculo: matrícula '{mat_estudante}' não encontrada em 'estudantes'.")
            return
        if banco["cursos"].find_one({"_id": curso_id}) is None:
            print(f"Erro ao criar vínculo: curso '{curso_id}' não encontrado em 'cursos'.")
            return

        documento = {
            "mat_estudante": mat_estudante,
            "curso_id": curso_id,
            "data_entrada": data_entrada,
            "status": status,
            "data_saida": data_saida
        }
        resultado = colecao.insert_one(documento)
        print(f"Vínculo do estudante {mat_estudante} com o curso {curso_id} criado com sucesso! ID: {resultado.inserted_id}")
    except Exception as e:
        print(f"Erro ao criar vínculo: {e}")


#função para listar vínculos R
def listar_vinculos():
    banco = conectar_mongo()
    colecao = banco["vinculos"]
    try:
        resultado = list(colecao.find())
        for documento in resultado:
            print(documento)
        return resultado
    except Exception as e:
        print(f"Erro ao listar vínculos: {e}")
    

#função para buscar um vínculo R
def buscar_vinculo(id_vinculo):
    banco = conectar_mongo()
    colecao = banco["vinculos"]
    try:
        resultado = colecao.find_one({"_id": ObjectId(id_vinculo)})
        if resultado:
            print(resultado)
        else:
            print("Vínculo não encontrado.")
        return resultado
    except Exception as e:
        print(f"Erro ao buscar vínculo: {e}")


#função para atualizar um vínculo U
def atualizar_vinculo(id_vinculo, mat_estudante=None, curso_id=None, data_entrada=None, status=None, data_saida=None):
    banco = conectar_mongo()
    colecao = banco["vinculos"]
    try:
        campos_atualizados = {}
        if mat_estudante is not None:
            campos_atualizados["mat_estudante"] = mat_estudante
        if curso_id is not None:
            campos_atualizados["curso_id"] = curso_id
        if data_entrada is not None:
            campos_atualizados["data_entrada"] = data_entrada
        if status is not None:
            campos_atualizados["status"] = status
        if data_saida is not None:
            campos_atualizados["data_saida"] = data_saida

        if not campos_atualizados:
            print("Nenhum campo para atualizar.")
            return

        resultado = colecao.update_one({"_id": ObjectId(id_vinculo)}, {"$set": campos_atualizados})
        if resultado.matched_count == 0:
            print("Vínculo não encontrado.")
        else:
            print(f"Vínculo {id_vinculo} atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar vínculo: {e}")


#função para deletar um vínculo D
def deletar_vinculo(id_vinculo):
    banco = conectar_mongo()
    colecao = banco["vinculos"]
    try:
        resultado = colecao.delete_one({"_id": ObjectId(id_vinculo)})
        if resultado.deleted_count == 0:
            print("Vínculo não encontrado.")
        else:
            print(f"Vínculo {id_vinculo} deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar vínculo: {e}")


