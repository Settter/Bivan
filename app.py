from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main_page.html')


if __name__ == '__main__':
    app.run(debug=False)
