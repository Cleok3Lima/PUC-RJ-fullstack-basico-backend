from model import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

class Observacao(Base):
    __tablename__ = 'observacao'

    id = Column(Integer, primary_key=True)
    texto = Column(String(4000))
    data_publicacao = Column(DateTime, default=datetime.now())

    # Definindo o relacionamento entre observacao e livro.
    # A coluna 'livro' armazena a referência ao livro correspondente,
    # usando uma chave estrangeira que relaciona uma observacao a um livro.
    livro = Column(Integer, ForeignKey("livro.pk_livro"), nullable=False)

    def __init__(self, texto:str, data_publicacao:Union[DateTime, None] = None):
        """
        Cria uma Obsercação

        Parâmetros:
            texto: o conteúdo textual da observação.
            data_publicacao: a data em que a observação foi feita ou adicionada
            à base de dados.
        """
        self.texto = texto
        if data_publicacao:
            self.data_publicacao = data_publicacao