        
import requests
import  json
from collections import defaultdict 
from flask import Flask,render_template
from flask_restful import Resource, Api, reqparse
from flask import jsonify
from jinja2 import Template, escape
from collections import Counter

#creat an instance flask
app=Flask(__name__)
api = Api(app)
keys=dict()
data=defaultdict(list)
c=list()    
    
app.route("/")

class ReposData(Resource):
        uri='''https://api.github.com/search/repositories?q= created:>2020-08-08&sort=stars&order=desc
''' 
        res = requests.get(uri).json()
        for item in res['items']:

            if item['language'] in keys.keys():
                
                keys[item['language']]  =keys[item['language']] +1
                
                data['listof',item['language']].append(item['html_url'])
            else:
                keys.update({item['language'] : 1})
                data['listof',item['language']].append(item['html_url'])
                           
        def get(self):
          
       

               return render_template('index.html', title='Home', keys=keys, data=data)


api.add_resource( ReposData, '/')

print(keys.values())
print(data.values())
