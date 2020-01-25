# from lib2to3.pytree import convert

from flask import Flask, render_template, request
# import xmltodict
# import json
# from pprint import pprint
#
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    colours = ['Facultatea Electronică și Telecomunicații', 
        'Facultatea Energetică și Inginerie Electrică', 
        'Facultatea Calculatoare, Informatică şi Microelectronică', 
        'Facultatea Tehnologia Alimentelor',
        'Facultatea Inginerie Mecanică',
        'Industrială şi Transporturi',
        'Facultatea Urbanism şi Arhitectură',
        'Facultatea Construcții, Geodezie şi Cadastru',
        'Facultatea Inginerie Economică şi Business',
        'Facultatea Textile și Poligrafie']
    return render_template('index.html', colours=colours)



if __name__ == '__main__':
    app.run(debug=True)
