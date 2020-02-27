from __future__ import unicode_literals
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy#
from flask_mysqldb import MySQL
#from flask_wtf import Form
app=Flask(__name__,template_folder='Templates')
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] ='forms'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'
emp_id=""
mysql=MySQL(app)

@app.route('/tt5', methods=['GET', 'POST'])
def tt5():
    if request.method == "POST":
        global emp_id
        details = request.form
        n_o_t = details['name']
        emp_id = details['id']
        evalua = details['evalua1']
        d_o_d = details['d_o_d']
        score = details['score']
        level = details['level']
        topic = details['topic']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO t_details5(n_o_t, emp_id, evalua, d_o_d, score, level, topic) values (%s, %s, %s, %s, %s,%s, %s)",(n_o_t,emp_id,evalua,d_o_d,score,level,topic))
        mysql.connection.commit()
        cur.close()
    return render_template('tt5.html')
if __name__ == "__main__":
    app.run(debug=True)