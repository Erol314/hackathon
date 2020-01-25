from excel2json import convert_from_file
import xlrd
from flask import Flask, render_template
import xmltodict
import json
# from pprint import pprint
#
app = Flask(__name__)
#

from excel2json import convert_from_file




@app.route('/')
def index():
    EXCEL_FILE = r'C:\Users\sezgh\Downloads\Telegram Desktop\Hackathon\FCIM BUGET.xlsx'
    # foo = convert_from_file(EXCEL_FILE, )


    # //workbook = xlrd.open_workbook(r'C:\Users\sezgh\Downloads\Telegram Desktop\Hackathon\FCIM BUGET.xlsx')
    f = open("demofile.txt", "r")
    for x in f:
        print(x)

    return render_template('index.html', foo=foo)



if __name__ == '__main__':
    app.run(debug=True)
