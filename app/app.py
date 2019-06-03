import flask
from flask import request, jsonify
import redis
import pandas
from pandas import read_csv
import numpy
from numpy import int64
from Database import Database
from Client import Client

app = flask.Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
df_limits = read_csv('limits.csv', dtype={'COUNTRY': str, 'CURRENCY': str, 'MAX_AMOUNT': int64},
                     index_col=['COUNTRY', 'CURRENCY'])


@app.route('/validate', methods=['POST'])
def validate():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.get_json()
        client = Client(
                    data['client_id'],
                    data['date'],
                    data['amount'],
                    data['currency'],
                    data['country'])
        limit = df_limits.loc[client.country, client.currency].at['MAX_AMOUNT']
        hashKey = hash(client.client_id + client.country + client.currency)
        totalAmount = 0
        if cache.exists(hashKey):
            totalAmount = cache.get(hashKey)
        else:
            sql = f"SELECT SUM(AMOUNT) FROM flask.limits \
                                                WHERE COUNTRY={client.country!r} AND \
                                                CUR={client.currency!r} AND \
                                                OP_DATE<={client.date!r};"
            totalAmount = db.exec_query(sql)
            cache.set(hashKey, totalAmount)

        if totalAmount > limit:
            return jsonify({'answer': 'operation is refused: over the limit'})
        return jsonify({'answer': 'OK'})


if __name__ == "__main__":
    db = Database()
    db.connect_db()
    app.run(host='0.0.0.0')