from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_prefixed_env()


@app.route('/')
def index():
    return 'Hello, world'