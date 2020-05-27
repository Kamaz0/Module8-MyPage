from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/mypage/me', methods=['GET'])
def me():
    return render_template('o_mnie.html')

# @app.route('/mypage/contact', methods=['GET', 'POST'])
# def zapis_form():
#     if request.method == 'POST':
#         print(request.form)    
#     return render_template('zapis_form.html')


@app.route('/mypage/contact', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("zapis_form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/mypage/me")



if __name__ == '__main__':
    app.run(debug=True)
