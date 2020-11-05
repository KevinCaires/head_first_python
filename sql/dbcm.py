from mysql import connector


class UseDatabase:
    """
    Contex Manager para conexão com o banco de dados.
    """
    def __init__(self, config: dict) -> None:
        """
        Inicia o context manager.
        """
        self.configuration = config

    def __enter__(self) -> 'cursor':
        """
        Entrada das configurações e dados.
        """
        self.conn = connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()

        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        """
        Fechamento das conexões e destruição dos dados.
        """
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
