from src import app, logger

@app.route('/a')
def a():
    logger.info('测试logger')
    return 'hello flask'

if __name__ == '__main__':
    app.run(debug=True)
