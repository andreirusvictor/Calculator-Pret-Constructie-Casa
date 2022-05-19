from flask import Flask, render_template

app = Flask('calculator')


@app.route('/first_page/')
def first_page():
    return render_template('first_page.html', title='Formular de calcul')


@app.route('/second_page/')
def second_page():
    return render_template('second_page.html', title='Detaliere Costuri')


if __name__ == '__main__':
    app.run(debug=True)
