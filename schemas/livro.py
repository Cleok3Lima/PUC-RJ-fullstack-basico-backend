from pydantic import BaseModel
from typing import Optional, List
from model.livro import Livro
from datetime import datetime
from enums import GeneroEnum
from schemas import ObservacaoSchema


class LivroSchema(BaseModel):
    """ Define a representação de um novo livro a ser inserido.
    """
    titulo: str = "Corte de espinhos e rosas"
    autor: str = "Sarah J. Maas"
    editora: Optional[str] = None
    data_publicacao: Optional[datetime] = None
    genero: GeneroEnum
    lido: bool = False

class LivroBuscaSchema(BaseModel):
    """ Define a estrutura para a busca de livros, que pode ser feita com base
        no título do livro, nome do autor, gênero, editora ou status de leitura.
    """
    titulo: Optional[str] = None
    autor: Optional[str] = None
    genero: Optional[GeneroEnum] = None
    editora: Optional[str] = None
    lido: Optional[bool] = None

class ListagemLivrosSchema(BaseModel):
    """ Define a estrutura para o retorno de uma lista de livros.
    """
    livros:List[LivroSchema]

def apresenta_livros(livros: List[Livro]):
    """ Retorna uma representação do livro conforme definido no LivroViewSchema.
    """
    result = []
    for livro in livros:
        result.append({
            "titulo": livro.titulo,
            "autor": livro.autor,
            "editora": livro.editora,
            "data_publicacao": livro.data_publicacao,
            "genero": livro.genero,
            "lido": livro.lido,
        })

    return {"livros": result}

class LivroViewSchema(BaseModel):
    """ Define a estrutura de retorno de um livro juntamente com suas observações.
    """
    id: int = 1
    titulo: str = "Corte de espinhos e rosas"
    autor: str = "Sarah J. Maas"
    editora: Optional[str] = None
    data_publicacao: Optional[datetime] = None
    genero: GeneroEnum
    lido: bool = False
    observacoes:List[ObservacaoSchema]

class LivroDeleteSchema(BaseModel):
    """ Define a estrutura dos dados retornados após uma solicitação de remoção.
    """
    message: str
    titulo: str

def apresenta_livro(livro: Livro):
    """ Retorna a representação de um livro conforme definido no LivroViewSchema.
    """
    return {
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "editora": livro.editora,
        "data_publicacao": livro.data_publicacao,
        "genero": livro.genero,
        "lido": livro.lido,
        "observacoes": [{"texto": observacao.texto} for observacao in livro.observacoes]
    }
