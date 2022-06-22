from flask import Flask, request, jsonify
app = Flask(__name__)
import crawl 

@app.route('/')
def index():
    return 'hello'

@app.route('/main', methods=['post'])
def main():
    id = request.json.get('id')
    answer_data = crawl.action(id)
    return {
        'answer': answer_data
    }