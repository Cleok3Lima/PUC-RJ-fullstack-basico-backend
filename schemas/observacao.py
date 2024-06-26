from pydantic import BaseModel


class ObservacaoSchema(BaseModel):
    """ Define a representação de uma nova observação a ser inserida.
    """
    livro_id: int = 1
    texto: str = "Leitura envolvente, com ótimas descrições e muito amor e determinação."
