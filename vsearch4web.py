"""
Módulo do Flask.
"""
from flask import Flask, render_template, request  # pylint: disable=import-error
from mymodules.vsearch import search4letters


app = Flask(__name__)

# Com redirect importado
# @app.route('/')
# def hello() -> '302':
#     """
#     Realiza um apontamento para /entry.
#     """
#     return redirect('/entry')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """
    Retorna resultado do search4letters.
    """
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Aqui está o resultado:'
    results = str(search4letters(phrase, letters))

    return render_template(
        'results.html',
        the_phrase=phrase,
        the_letters=letters,
        the_title=title,
        the_results=results,
    )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """
    Renderiza a página de entrada de valores.
    """
    return render_template(
        'entry.html',
        the_title='Procurando por letras!?'
    )

app.run(debug=True)
