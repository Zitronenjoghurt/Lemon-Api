from flask import Flask, request, abort
from flask_limiter import Limiter
from src.resources.hello import hello

app = Flask(__name__)
app.register_blueprint(hello, url_prefix="/")

VALID_API_KEYS = {"sjkdalkjdhajs": True}

def get_api_key():
    return request.args.get('api_key')

limiter = Limiter(app=app, key_func=get_api_key, default_limits=["5 per minute"])

def validate_api_key():
    api_key = get_api_key()
    if api_key in VALID_API_KEYS:
        return True
    else:
        abort(401)

@app.before_request
def do_before_request():
    validate_api_key()

if __name__ == '__main__':
    app.run()