from src import app

@app.route('/a')
def a():
    return 'hello flask'

if __name__ == '__main__':
    app.run(debug=True)
