"""
Módulo para criação de Logs.
"""

from datetime import datetime


def log_request(req: 'flask_request', res: str) -> None:
    """
    Salva logs de request no arquivo de logs.
    """
    with open('vsearch.log', 'a') as log:
        # Salva conteúdo no arquivo de logs com argumentos especiais do print.
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
