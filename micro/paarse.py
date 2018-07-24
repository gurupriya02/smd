import json
import re
import requests
from flask import Flask, render_template, request,jsonify
from werkzeug import secure_filename

dl='.',',','!','\n','\t',' ','/'
app = Flask(__name__)
dict1={'skill':["java","python","c","c++"]}
e={}

@app.route('/uploader_s',methods=["POST"])
def uploader_s():
  if request.method == "POST":
     i=0       
     a=json.loads(request.data)
     print(a['text'])
     
     for b in a['text']:
          for y in b:
	          
     	          for value in dict1['skill']:
         
                      if (value==y):
                         e[value]=i
                         i+=1
     print(e)
      
     return(jsonify(e))
    



@app.route('/load_s', methods = ['POST'])
def load_s():
   if request.method == 'POST':
       header={"Content-Type":"application/json"}
       a=requests.post("http://localhost:9200/skills/skill",data=request.data,headers=header)
       print(a.text)
       return a.text

@app.route('/samp_s', methods = ['POST'])
def samp_s():
	if request.method == 'POST':
             
             return(request.data)

@app.route('/search_s', methods = ['POST'])
def search_s():
  if request.method == 'POST':
      header={"Content-Type":"application/json"}
      a=requests.post("http://localhost:9200/skills/skill/_search",data=request.data,headers=header)
      
  return a.text
@app.route('/name_s', methods = ['POST'])
def name_s():
  if request.method == 'POST':
      header={"Content-Type":"application/json"}
      a=requests.post("http://localhost:9200/skills/skill/_search",data=request.data,headers=header)
      print(a.text)
  return a.text

if __name__ == '__main__':
   app.run(port = 5001)

