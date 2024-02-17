from flask import Flask, request, jsonify
app = Flask(__name__)

from algo.search import mySearch
from algo.summary import mySummary
from algo.recommendation import myRec
from algo.category import myCategory
from algo.all import get_all


@app.route('/search', methods=['POST'])
def get_search():
    data = request.get_json()
    
    searched_data = mySearch(data['query'])
    return jsonify({'output': searched_data})


@app.route('/summary', methods=['POST'])
def get_summary():
    data = request.get_json()
    
    getSum = mySummary(data.get('bigText', ''))
    return jsonify({'output': getSum})


@app.route('/recommendation', methods=['POST'])
def get_recc():
    data = request.get_json()
    
    getRec = myRec(data['keys'])
    return jsonify({'output': getRec})

@app.route('/category', methods=['POST'])
def get_cat():
    data = request.get_json()
    
    getCat = myCategory(data['catList'])
    return jsonify({'output': getCat})


@app.route('/all', methods = ['GET'])
def all_api():
    newsList = get_all()
    return jsonify({'output': newsList})


if __name__ == '__main__':
    app.run(debug=True)
