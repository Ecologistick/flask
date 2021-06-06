from flask import Flask, jsonify, request
from datetime import datetime


now = datetime.now()
app = Flask(__name__)


client = app.test_client()


ads = [
    {
        'id': 1,
        'user': 'admin',
        'title': 'Ad #1',
        'description': 'description #1',
        'time': now
    },
    {
        'id': 2,
        'user': 'admin',
        'title': 'Ad #2',
        'description': 'description #2',
        'time': now
    }
]


@app.route('/ads', methods=['GET'])
def get_list():
    return jsonify(ads)


@app.route('/ads', methods=['POST'])
def update_list():
    new_one = request.json
    ads.append(new_one)
    return jsonify(ads)


@app.route('/ads/<int:ad_id>', methods=['PUT'])
def update_ads(ad_id):
    item = next((x for x in ads if x['id'] == ad_id), None)
    params = request.json
    if not item:
        return {'message': 'No ads with this id'}, 400
    item.update(params)
    return item


@app.route('/ads/<int:ad_id>', methods=['DELETE'])
def delete_ads(ad_id):
    idx, _ = next((x for x in enumerate(ads)
                   if x[1]['id'] == ad_id), (None, None))

    ads.pop(idx)
    return '', 204


if __name__ == '__main__':
    app.run()
