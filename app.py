from flask import Flask, request
app = Flask(__name__)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    error = request.args.get('error')
    if error:
        return f'Error received: {error}'
    if not code:
        return 'No code received'
    return f'Authorization code: {code}'

if __name__ == '__main__':
    app.run(port=3000)
