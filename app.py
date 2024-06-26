from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import redirect
from schemas import *
from model import Session
from model.livro import Livro
from model.observacao import Observacao
from logger import logger
from sqlalchemy.exc import IntegrityError

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
livro_tag = Tag(name="Livro", description="Adição, visualização e remoção de produtos na base de dados")
comentario_tag = Tag(name="Observação", description="Adição de uma observação à um livro cadastrado na base de dados")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, uma página que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/biblioteca', tags=[livro_tag],
          responses={"200": LivroViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_livro(data: LivroSchema):
    """Adiciona um novo livro à base de dados

    Retorna uma representação do livro juntamente com suas observações associadas.
    """
    livro = Livro(
        titulo=data.titulo,
        autor=data.autor,
        editora=data.editora,
        data_publicacao=data.data_publicacao,
        genero=data.genero,
        lido=data.lido)
    logger.debug(f"O livro '{livro.titulo}' foi adicionado a sua biblioteca!")
    try:
        # estabelecendo conexão com a base de dados
        session = Session()
        # adicionando livro à biblioteca
        session.add(livro)
        # confirmando a inserção do novo item na tabela
        session.commit()
        logger.debug(f"O livro '{livro.titulo}' foi adicionado a sua biblioteca!")
        return apresenta_livro(livro), 200

    except IntegrityError as e:
        # A duplicidade do nome é provavelmente a causa do IntegrityError
        error_msg = "Já existe um livro com este título na sua biblioteca!"
        logger.warning(f"Erro ao adicionar o livro '{livro.titulo}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar o novo livro na sua biblioteca :("
        logger.warning(f"Erro ao adicionar o livro '{livro.titulo}', {error_msg}")
        return {"message": error_msg}, 400