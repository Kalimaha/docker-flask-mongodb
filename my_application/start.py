from flask import Flask
from flask.ext.cors import CORS
from blueprint import bp

app = Flask(__name__)
cors = CORS(app,
            resources={
                r'/*': {
                    'origins': '*',
                    'headers': ['Content-Type']
                }
            })
app.register_blueprint(bp, url_prefix='/blueprint')

@app.route('/', methods=['GET'])
def say_hello():
    return 'Hello, Start!'

if __name__ == '__main__':
    app.run(debug=True)
