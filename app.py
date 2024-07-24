from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/writing')
def writing():
    return render_template('writing.html')

@app.route('/books')
def books():
    return render_template('books.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)