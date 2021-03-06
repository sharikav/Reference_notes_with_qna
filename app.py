from flask import Flask,render_template,redirect,url_for,flash,request
from summary import generate_summary
import storedata as sd
app = Flask(__name__)

app.secret_key = "HBCJSBJH454546SSCHJSBHCJBKSBKNCJAASnadn"

@app.route("/",methods=["POST","GET"])
def index():
    sd.create_table()
    return render_template('index.html')

@app.route("/getchaptersummary",methods= ["POST","GET"])
def getsummary():
    if request.method == "POST":
        topic = request.form['topic']
        text = request.form["text"]
        data = generate_summary(text)
        sd.add_data(text,topic,data)
        all_data = sd.get_all_records()
        return render_template("getchapsum.html",data= data,text=text,all_data = all_data)
    return render_template("getchapsum.html")
if __name__ == "__main__":
    app.run(debug=True)