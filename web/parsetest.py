import json
import requests
import re
import textract
from flask import Flask, render_template, request,jsonify,redirect,url_for
from werkzeug import secure_filename

dl='.',',','!','\n','\t',' ','/'
app = Flask(__name__)


dict1={'skill':["java","python","c","c++"]}
e={}
l=[]
g={}
sk={}
s={}
a=[]
f={}
so={}

@app.route('/', methods=['GET', 'POST'])
def loginn():
   
    return render_template('loginn.html')
@app.route('/upload_file' ,methods=['GET', 'POST'])
def upload_file():
     if request.method == 'POST':
         if request.form['username'] == 'user' or request.form['password'] == 'user':
            return render_template('up.html')
            
         elif request.form['username'] == 'hr' or request.form['password'] == 'hr':
            return render_template('KIB.html')
         else:
            return redirect( url_for('loginn'))
            

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
  if request.method == 'POST':
      
         
     
            global g
            g={ 'name' :request.form['name'] ,
	       'dob'  :request.form['dob']  ,
                'email':request.form['email']}


                                        
	    f=request.files['file']
            
             
          
           
            for lines in f:
		lines=lines.lower()
		regexPattern = '|'.join(map(re.escape, dl))
		a.append(re.split(regexPattern,lines))
            print(a)
            s['text']=a
	       
      
            target_url='http://localhost:5001/uploader_s'
           
            
            
            
           
           
            r = requests.post(target_url,data=json.dumps(s))
            
            global e
            e= json.loads(r.text)
          
            
           
#f is a dict
      
   



      
      
  return render_template('result.html',result=e)  
              
@app.route('/load', methods = ['POST'])
def load():
	
	if request.method == 'POST':
           global f	
	   for i in request.form.keys():
               
	       f.update({i : request.form[i]})
	       
           
          
	   g.update({'skill_rating': f })
           global l
           for k in f:
              l.append(k)
           
           g['skills']=l
          
           target_url='http://localhost:5001/load_s'
           r = requests.post(target_url,data=json.dumps(g))
	   
           
           

	return render_template('parse.html',parse=f)


@app.route('/samp', methods = ['POST'])
def samp():
	if request.method == 'POST':
		text = request.form.get('name')
                y=0
                e[text]=y
		
                target_url='http://localhost:5001/samp_s'
                r = requests.post(target_url,data=json.dumps(e))
                first=json.loads(r.text)
                
                
                     
	return render_template('result.html',result=e)
@app.route('/stats',methods=['GET'])
def stats():
    return render_template('KIB.html')
@app.route('/search', methods = ['GET'])
def search():
   if request.method == 'GET':
	h={
		"aggs" : {
        	"skills_aggs" : {
		"terms" : { "field" : "skills.keyword" }
        			}
    			 }
	   }
        target_url='http://localhost:5001/search_s'
	r = requests.post(target_url,data=json.dumps(h))
	second=json.loads(r.text)
	
   return render_template("search.html",sec=second)
@app.route('/name/<key>', methods = ['GET'])
def name(key):
   if request.method == 'GET':
	k={
        "query" : {
        "term" : {"skills":key} 
                   }
          }

        target_url='http://localhost:5001/name_s'
	r = requests.post(target_url,data=json.dumps(k))
	third=json.loads(r.text)
	print(third)
   return render_template("name.html",t=third,a=key)
      
      
if __name__ == '__main__':
   app.run(debug = True)
