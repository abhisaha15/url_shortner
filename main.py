from flask import Flask,render_template,url_for,request,redirect,session,jsonify
from datamodel import db,User,Url


app = Flask(__name__)
app.secret_key = '987123456abcd@@'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:12345@localhost/url_shortner'
db.init_app(app)


@app.route('/',methods=['GET','POST'])
def home():
    if 'user' in session:
        urldata = Url.query.filter_by(owner=session['uid']).order_by(Url.rid.desc()).all()
        rid,url_nm, url_st_nm = [],[],[]

        data = []
        for i in urldata:
            d = {}
            d['rid']=i.rid,
            d['u_st_nm']=i.url_short_name,
            d['a_url']= i.url_name,
            d['creation_time'] = i.creation_date
            data.append(d)


        return render_template('index.html',rdata=data,uemail = session['user'])

    return redirect(url_for('login'))
@app.route('/addnewdata',methods=['POST'])
def addnewdata():
    if 'user' in session:
        if request.method == 'POST':

            urlnm = request.form.get('url_nm')
            urlstnm = request.form.get('url_st_nm')

            new_row = Url(url_name=urlnm,url_short_name=urlstnm,owner=session['uid'])

            db.session.add(new_row)
            db.session.commit()

            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/updatedata',methods=['POST'])
def updatedata():
    if 'user' in session:
        if request.method == 'POST':

            urlnm = request.form.get('url_nm')
            urlstnm = request.form.get('url_st_nm')
            sl_rid = request.form.get('selected_rid')

            old_row = Url.query.filter_by(rid=sl_rid)

            old_row.update({'url_name':urlnm, 'url_short_name':urlstnm})
            db.session.commit()
            return redirect(url_for('home'))

    else:
        return redirect(url_for('login'))


@app.route('/deletedata',methods=['POST'])
def deletedata():
    if 'user' in session:
        if request.method == 'POST':
            sl_rid = request.form.get('selected_rid')
            old_row = Url.query.filter_by(rid=sl_rid).first()
            db.session.delete(old_row)
            db.session.commit()
            return redirect(url_for('home'))

    else:
        return redirect(url_for('login'))


@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        u_nm = request.form['usernm']
        u_dob = request.form['dob']
        u_mail = request.form['umail']
        u_password = request.form['upass']

        dataflag_1 = User.query.filter_by(username=u_nm).first()
        dataflag_2 = User.query.filter_by(email=u_mail).first()

        if(dataflag_1 or dataflag_2):
            return render_template('signup.html',mesg="Usernbame or Email Exists Already Exists.")
        else:
            new_row = User(username=u_nm,email=u_mail,password=u_password,dob=u_dob)
            db.session.add(new_row)
            db.session.commit()
            return redirect(url_for('login'))

    if 'user' in session:
        return redirect(url_for('home'))
    return render_template('signup.html',mesg="")

@app.route('/forgetpassword',methods=['GET','POST'])
def forget_password():
    if request.method == 'POST':
        u_dob = request.form['dob']
        u_mail = request.form['umail']
        u_password = request.form['upass']

        dataflag = User.query.filter_by(dob=u_dob,email=u_mail)


        if(dataflag):
            dataflag.update({'password':u_password})
            db.session.commit()
            return redirect(url_for('login'))

        else:
            return render_template('forget.html',mesg="DOB Or Email Doesn't Match")



    return render_template('forget.html',mesg="")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        udata_email = request.form['uemail']
        udata_password = request.form['upassword']

        try:
            dbdata = User.query.filter_by(email=udata_email).first()
        except:
            dbdata = None

        if (dbdata) and (dbdata.password==udata_password):
            session['user'] = dbdata.username
            session['uid'] = dbdata.rid

            return redirect(url_for('home'))

        elif (dbdata) and(dbdata.password!=udata_password):
            return render_template('login.html',mesg="Failed Login | Password Wrong ")
        elif(dbdata==None):
            return render_template('login.html',mesg="Failed Login | User dosen't exists")

    if 'user' in session:
        return redirect(url_for('home'))

    return render_template('login.html',mesg="")

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user',None)
        session.pop('uid', None)
        return redirect(url_for('home'))
    return redirect(url_for('login'))

# @app.route('/get_user_url')
# def get_user_url():
#     if 'user' in session:
#         urldata = Url.query.filter_by(owner=session['uid']).order_by(Url.rid.desc()).all()
#         for i in urldata:
#             print(i)

@app.route('/<string:usernm>/<string:stnm>')
def gettheurl(usernm,stnm):
    u_data = User.query.filter_by(username=usernm).first()
    url_data = Url.query.filter_by(url_short_name=stnm,owner=u_data.rid).first()
    return redirect(url_data.url_name)

@app.route('/validuserdata',methods=['POST'])
def valid_user():
    if request.method == "POST":
        useremail= request.form['useremail']
        userpassword = request.form['userpassword']

        checkdata = User.query.filter_by(email=useremail,password=userpassword).first()

        if(checkdata):
            return '1'
        else:
            return '0'
    return '0'



if __name__ == "__main__":
    app.run()

