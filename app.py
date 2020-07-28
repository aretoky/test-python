# [start gae_python37_app]
from flask import Flask
app = Flask(__name__)

@app.route("/")
def extract_text_from_autochess_image():
    return 'hello world!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

# [end gae_python37_app]
