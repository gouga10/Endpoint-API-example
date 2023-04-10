import os 
from flask import request
from detect_func import model
from flask import Flask
from flask import render_template
app=Flask(__name__)
UPLOAD_FOLDER=r'C:/Users/abder/Desktop/api/static'

@app.route("/",methods=["GET","POST"])
def upload_predict():
    pred=0
    if request.method=='POST':
        image_file=request.files['image']
        if image_file:
            image_location=os.path.join(
                UPLOAD_FOLDER,
                image_file.filename
            )
            image_file.save(image_location)
            pred=model(image_location)
            print('pred is ',pred)
            return render_template("index.html",pred=int(pred))
            
    return render_template("index.html",pred=int(pred))

if __name__=="__main__":
    app.run(port=12000,debug=True)