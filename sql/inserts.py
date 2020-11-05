"""
Módulo que manipulas as inserções dentro do banco de dados.
"""
from mysql import connector
from sql.settings import dbconfig  # pylint: disable=import-error
from sql.dbcm import UseDatabase  # pylint: disable=import-error


def insert_into_log(request, results):
    """
    O nome já fala.

    args:
        request : flask request : conteúdo da consulta do usuário.
        results: str : Conteúo do resultado da pesquisa.
    """

    with UseDatabase(dbconfig) as cursor:
        _SQL = '''insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)
        '''
        
        values = (
            request.form['phrase'],
            request.form['letters'],
            request.remote_addr,
            request.user_agent.browser,
            results
        )
        
        cursor.execute(_SQL, values)
