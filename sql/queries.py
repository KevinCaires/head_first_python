"""
Módulo que manipula consultas no banco de dados.
"""

from  mysql import connector
from sql.settings import dbconfig  # pylint: disable=import-error


def select_all():
    """
    O nome já diz tudo.
    """
    conn = connector.connect(**dbconfig)
    cursor = conn.cursor()
    # Literalmente o sql
    _SQL="""
        select * from log;
    """
    cursor.execute(_SQL)
    response = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return [row for row in response]
