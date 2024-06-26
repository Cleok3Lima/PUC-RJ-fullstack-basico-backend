from model import Base
from model.observacao import Observacao
from sqlalchemy import Column, String, Integer, DateTime, Boolean, Enum
from enums import GeneroEnum
from sqlalchemy.orm import relationship
from typing import Union


class Livro(Base):
    __tablename__ = 'livro'

    id = Column("pk_livro", Integer, primary_key=True)
    titulo = Column(String(140), unique=True, nullable=False)
    autor = Column(String(140), nullable=False)
    editora = Column(String(140), nullable=True)
    data_publicacao = Column(DateTime, nullable=True)
    genero = Column(Enum(GeneroEnum), nullable=False)
    lido = Column(Boolean, default=False, nullable=False)

    # Definição do relacionamento entre o produto e o comentário.
    # Essa relação é implicita, não está salva na tabela 'produto',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    observacoes = relationship("Observação")


    def __init__(self, titulo:str, autor:str, editora:str, genero:GeneroEnum, lido:bool,
                 data_publicacao:Union[DateTime, None] = None):
        """
        Cria um Livro

        Parâmetros:
            titulo: o título do livro.
            autor: o autor do livro.
            editora: a editora do livro.
            genero: o gênero do livro.
            data_publicacao: a data de publicação do livro.
            lido: indica se o livro já foi lido (True) ou não (False).
        """
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.genero = genero
        self.lido = lido
        self.data_publicacao = data_publicacao

    def adiciona_observacao(self, observacao:Observacao):
        """ Adiciona uma observação ao Livro.
        """
        self.comentarios.append(observacao)