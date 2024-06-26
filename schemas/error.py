from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Define a estrutura de uma mensagem de erro.
    """
    message: str
