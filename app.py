from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
host = "localhost:5000"

@app.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == 'get':
        return redirect(host + '/sign_in')
    return render_template('menu.html')


@app.route('/sign_in', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'post':
        data = request.form['username']
        print(data)
        return '<h1>Data saved</h1>'
    else:
        return render_template('sign_in.html')


if __name__ == "__main__":
    app.run()
