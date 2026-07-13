from crud_mongo import conectar_mongo


#-----------------CURSO

#funcão para aplicar validação na coleção de cursos
def aplicar_validacao_cursos():
    banco = conectar_mongo()
    try:
        banco.command("collMod", "cursos", validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["nome", "turno"],
                "properties": {
                    "nome": {
                        "bsonType": "string",
                        "description": "nome é obrigatório e deve ser string"
                    },
                    "grau": {
                        "enum": ["Bacharelado", "Licenciatura Plena", None],
                        "description": "grau deve ser um dos valores permitidos"
                    },
                    "turno": {
                        "bsonType": "string",
                        "enum": ["Matutino", "Vespertino", "Noturno", "Turno Indefinido"],
                        "description": "turno é obrigatório e deve ser um dos valores permitidos"
                    },
                    "campus": {
                        "bsonType": ["string", "null"],
                        "description": "campus deve ser string"
                    },
                    "nivel": {
                        "enum": ["Graduação", "Mestrado", "Doutorado", "Lato", None],
                        "description": "nivel deve ser um dos valores permitidos"
                    }
                }
            }
        })
        print("Validação aplicada com sucesso na coleção 'cursos'!")
    except Exception as e:
        print(f"Erro ao aplicar validação: {e}")


#-----------------ESTUDANTE


#funcão para aplicar validação na coleção de estudantes
def aplicar_validacao_estudantes():
    banco = conectar_mongo()
    try:
        banco.command("collMod", "estudantes", validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["nome", "cpf"],
                "properties": {
                    "nome": {
                        "bsonType": "string",
                        "description": "nome é obrigatório e deve ser string"
                    },
                    "cpf": {
                        "bsonType": "string",
                        "description": "cpf é obrigatório e deve ser string"
                    },
                    "data_nascimento": {
                        "bsonType": ["string", "null"],
                        "description": "data_nascimento deve ser string"
                    },
                    "email": {
                        "bsonType": ["array", "null"],
                        "description": "email deve ser uma lista"
                    },
                    "telefone": {
                        "bsonType": ["array", "null"],
                        "description": "telefone deve ser uma lista"
                    },
                    "login": {
                        "bsonType": ["string", "null"],
                        "description": "login deve ser string"
                    },
                    "senha": {
                        "bsonType": ["string", "null"],
                        "description": "senha deve ser string"
                    },
                    "mc": {
                        "bsonType": ["int", "double", "null"],
                        "minimum": 0,
                        "maximum": 10,
                        "description": "mc deve ser numérico entre 0 e 10"
                    },
                    "ano_ingresso": {
                        "bsonType": ["int", "null"],
                        "description": "ano_ingresso deve ser inteiro"
                    }
                }
            }
        })
        print("Validação aplicada com sucesso na coleção 'estudantes'!")
    except Exception as e:
        print(f"Erro ao aplicar validação: {e}")


#funcão para aplicar validação em indices unicos cpf e login na coleção de estudantes
def aplicar_indices_unicos_estudantes():
    banco = conectar_mongo()
    colecao = banco["estudantes"]
    try:
        colecao.create_index("cpf", unique=True)
        colecao.create_index("login", unique=True)
        print("Índices únicos criados com sucesso em 'estudantes' (cpf, login)!")
    except Exception as e:
        print(f"Erro ao criar índices: {e}")



#-----------------VINCULO



#funcão para aplicar validação na coleção de vinculos
def aplicar_validacao_vinculos():
    banco = conectar_mongo()
    try:
        banco.command("collMod", "vinculos", validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["mat_estudante", "curso_id"],
                "properties": {
                    "status": {
                        "enum": ["Ativo", "Cancelada", "Formando", "Graduado", None],
                        "description": "status deve ser um dos valores permitidos"
                    },
                }
            }
        })
        print("Validação aplicada com sucesso na coleção 'vinculos'!")
    except Exception as e:
        print(f"Erro ao aplicar validação: {e}")


if __name__ == "__main__":
    aplicar_validacao_vinculos()