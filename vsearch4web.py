"""
Módulo do Flask.
"""
from flask import Flask, render_template, request, escape  # pylint: disable=import-error
from mymodules.vsearch import search4letters
from utils.logs import log_request
from sql.inserts import insert_into_log


app = Flask(__name__)

# Com redirect importado
# @app.route('/')
# def hello() -> '302':
#     """
#     Realiza um apontamento para /entry.
#     """
#     return redirect('/entry')

# Define a rota principal.
@app.route('/')
# Define a rota onde tem entrada de dados.
@app.route('/entry')
def entry_page() -> 'html':
    """
    Renderiza a página de entrada de valores.
    """
    # Renderiza o template passando um conteúdo para a variável do jinja.
    return render_template(
        'entry.html',
        the_title='Procurando por letras!?'
    )


# Rota com chamada do método POST
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """
    Retorna resultado do search4letters.
    """
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Aqui está o resultado:'
    results = str(search4letters(phrase, letters))
    # log_request(request, results)
    insert_into_log(request, results)

    return render_template(
        'results.html',
        the_phrase=phrase,
        the_letters=letters,
        the_title=title,
        the_results=results,
    )


@app.route('/viewlog')
def view_log() -> 'html':
    """
    Retorna o conteúdo do log para uma página.
    """
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                # Escape retira os caracteres especiais que possam zoar o html (eg, '<' e '>'   
                contents[-1].append(escape(item))

    titles = ('Form Data', 'Remote Address', 'User Agent', 'Results')

    return render_template(
        'viewlog.html',
        the_title='View Logs',
        the_row_titles=titles,
        the_data=contents,
    )


if __name__=='__main__':
    app.run(debug=True)
