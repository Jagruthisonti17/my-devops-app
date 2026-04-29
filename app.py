from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>DevOps App</title>
    </head>
    <body style="background-color:black; color:white; text-align:center; margin-top:100px;">
        <h1>🚀 My First DevOps App Running!</h1>
        <p>Deployed using Jenkins + Docker + Nginx</p>
    </body>
    </html>
    """

app.run(host='0.0.0.0', port=5000)
