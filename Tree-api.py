# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:59:40 2018

@author: pgood
"""

from flask import Flask, jsonify, request


def get_data(base, column, where, rows):
    import requests
    
    query = {
            '$select': column,
            '$where': where,
            '$limit': rows
            }
    #if where == None:
     #   url = 'https://data.cityofnewyork.us/resource/nwxe-4ae8.json?$select={}&$limit={}'.format(column, rows)
    #else:
     #   url = 'https://data.cityofnewyork.us/resource/nwxe-4ae8.json?$select={}&$limit={}&$where={}'.format(column, rows, where)
    return requests.get(base, params = query).json()
    
app = Flask(__name__)



@app.route('/tree_data/<string:column>', methods=['GET'])
def return_data(column):
    
    base_url = 'https://data.cityofnewyork.us/resource/nwxe-4ae8.json'
    
    where_clause = request.args.get('where')
    limit = request.args.get('limit')
    if limit == None:
        limit = 10
    print(where_clause)
    
    data = get_data(base_url, column, where_clause, limit)
    
    return jsonify({'response': data})


if __name__ == '__main__':
    app.run()
