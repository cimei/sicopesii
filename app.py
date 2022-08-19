from project import app
from flask import render_template
import webbrowser
from threading import Timer
import locale

# filtro cusomizado para o jinja
#
@app.template_filter('converte_para_real')
def converte_para_real(valor):
  return locale.currency(valor, symbol=False, grouping = True )

@app.route('/')
def index():
    return render_template('home.html')

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5003/')

if __name__ == '__main__':
    Timer(1, open_browser).start();
    app.run(port = 5003)