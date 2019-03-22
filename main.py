from flask import Flask, render_template, url_for, session
app = Flask(__name__)
import sqlite3
from flask import g
from flask import request
import datetime
import tables


posts = [
        {
        'author': 'Name1',
        'title': 'title 1',
        'content': 'content1',
        'date': 'jan 1st 2019'        
        },
        {
        'author': 'Name2',
        'title': 'title2',
        'content': 'content2',
        'date': 'jan 2nd 2019'        
        }
]

app.secret_key = 'very secret string'



@app.route("/")
@app.route("/home")
def home():
    return my_render("home.html", posts=posts)

@app.route("/about")
def about():
    return my_render("about.html", title="About")

@app.route("/register")
def register():
    return my_render("register.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    print("-----------------------------username-----------------------------")
    print(request.form["username"])    
    c = get_db().cursor()
    c.execute('''
              SELECT name FROM users
              ''')
    x = 0
    for i in c:
        if i[0] == request.form["username"]:
             x += 1
    if x == 0:
        c.execute('''
                   INSERT INTO users
                   (name, password, email)
                   VALUES
                   (?, ?, ?);
                   ''',(request.form["username"],request.form["password"],request.form["email"]))
        
        get_db().commit()
        c.execute('''
                       SELECT * FROM users
                       ''')
        print("----------------------------------users----------------------------------")
        for i in c:
            print(i)
    
        return my_render("login.html")
    else:
        return my_render('register.html', success = False)


def get_user_id(user):
    ID = get_db().cursor().execute('''SELECT Id FROM Users WHERE name = ?''',user)
    return ID.fetchone()[0]

def get_login_status():
    return 'currentuser' in session

@app.route('/login')
def login():
    return my_render("login.html", title="Login")

@app.route('/login_try', methods=['POST'])
def login_try():
    pw = request.form['password']
    user = request.form['username']

    if login_success(user, pw):
        ID=get_user_id(user)
        session['currentuser'] = ID
        return my_render('home.html', posts=posts)
    else:
        session.pop('currentuser', None)
        return my_render('login.html', success = False) 

def login_success(user, pw):
    c = get_db().cursor()
    c.execute('''
              SELECT password FROM users WHERE name=?
              ''',user)
    for i in c:
        if i[0] == pw:
            return True
        else:
            return False

@app.route('/logout')
def logout():
    session.pop('currentuser', None)
    return my_render("home.html", posts=posts)

def my_render(template, **kwargs):
    login_status = get_login_status()
    tracks=get_tracks()
    if len(tracks) < 1:
        noTracks = True
    else:
        noTracks = False
    return render_template(template, tracks=tracks, noTracks=noTracks, loggedin=login_status, **kwargs)

@app.route('/create_track')
def create_track():
    return my_render("track.html", )

@app.route("/create_track_real", methods=["POST"])
def create_track_real(): 
    c = get_db().cursor()
    c.execute('''
              SELECT name FROM tracks WHERE user_id=?
              ''',str(session['currentuser']))
    x = 0
    for i in c:
        if i[0] == request.form["trackname"]:
             x += 1
    tracktype = request.form["type"]
    if x == 0:
        date = datetime.datetime.now().date()
        if tracktype == "0":
            c.execute('''
                       INSERT INTO tracks
                       (name, type, user_id, createdate, unit)
                       VALUES
                       (?, ?, ?, ?, ?);
                       ''',(request.form["trackname"],tracktype, session['currentuser'], date, request.form["unit"]))
            
            get_db().commit()
        elif tracktype == "1":
            c.execute('''
                       INSERT INTO tracks
                       (name, type, user_id, createdate)
                       VALUES
                       (?, ?, ?, ?);
                       ''',(request.form["trackname"],tracktype, session['currentuser'], date))
            
            get_db().commit()
        elif tracktype == "2":
            c.execute('''
                       INSERT INTO tracks
                       (name, type, user_id, createdate, scalesize)
                       VALUES
                       (?, ?, ?, ?, ?);
                       ''',(request.form["trackname"],tracktype, session['currentuser'], date, request.form["scale"]))
            
            get_db().commit()
            
            
            
        c.execute('''
                       SELECT * FROM tracks
                       ''')
        print("----Tracks----")
        for i in c:
            print(i)
        c.execute('''
                       SELECT * FROM users
                       ''')
        print("----Users----")
        for i in c:
            print(i)
    
        return my_render("my_tracks.html")
    else:
        return my_render('track.html', success = False)
    
@app.route("/my_tracks")
def my_tracks():
    return my_render("my_tracks.html")

def get_tracks():
    c = get_db().cursor()
    if 'currentuser' in session:
        c.execute('''
              SELECT * FROM tracks WHERE user_id=?
              ''',str(session['currentuser']))
    tracks = []
    for track in c:
        tracks.append(track)
        
    return tracks

@app.route("/create_var", methods=["GET","POST"])
def create_var():  
    
    c = get_db().cursor()
    c.execute('''
              SELECT type FROM tracks WHERE Id=? 
              ''',request.args.get("id"))
    tracktype = c.fetchone()[0]
    if tracktype == 0:
        c.execute('''
               INSERT INTO trackvars
               (track_id, value, postdate)
               VALUES
               (?, ?, ?);
               ''',(request.args.get("id"), request.form["var"], datetime.datetime.now().date()))
    elif tracktype == 1:
        c.execute('''
               INSERT INTO trackvars
               (track_id, starttime, postdate)
               VALUES
               (?, ?, ?);
               ''',(request.args.get("id"),request.form["dato"], datetime.datetime.now().date()))
    elif tracktype == 2:
        c.execute('''
               INSERT INTO trackvars
               (track_id, value, postdate)
               VALUES
               (?, ?, ?);
               ''',(request.args.get("id"), request.form["scale"], datetime.datetime.now().date()))
    
    
    get_db().commit()
    
    c.execute('''
                   SELECT * FROM users
                   ''')
    print("----Users----")
    for i in c:
        print(i)
    
    c.execute('''
                   SELECT * FROM tracks
                   ''')
    print("----Tracks----")
    for i in c:
        print(i)
    
        
    c.execute('''
              SELECT * FROM trackvars
              ''')
    
    print("----Trackvars----")
    for i in c:
        print(i)
    
    return my_render("my_tracks.html")

@app.route("/delete_track", methods=["GET", "POST"])
def delete_track():
    c = get_db().cursor()
    c.execute('''
               DELETE FROM tracks WHERE Id=?
               ''',(request.args.get("id"),))
    get_db().commit()
    
    return my_render("my_tracks.html")

@app.route("/my_tracks_show", methods=["GET", "POST"])
def my_tracks_show():
    c = get_db().cursor()
    c.execute('''
              SELECT * FROM trackvars WHERE track_id=?
              ''',(request.args.get("id"),))
    trackvars = []
    for i in c:
        trackvars.append(i)
        
    print(trackvars)
    return my_render("my_tracks_show.html", trackvars=trackvars)
   

            #TODO grafer i my_tracks. https://plot.ly/python/line-charts/
            #TODO liste over trackvars
            #TODO https://www.w3schools.com/howto/howto_css_custom_checkbox.asp

@app.route("/create_tables")
def create_tables():
    c = get_db().cursor()
    tables.create_tables(c)
    return "cool"                 

@app.route("/clear_tables")
def clear_tables():
    c = get_db().cursor()
    tables.clear_tables(c)
    return "cool"                 
                   
@app.route("/clear_users")
def clear_users():
    c = get_db().cursor()
    tables.clear_users(c)
    return "cool"
    
@app.route("/clear_tracks")
def clear_tracks():
    c = get_db().cursor()
    tables.clear_tracks(c)
    return "cool"
    
DATABASE = "ontrack.db"


def get_db():
    db = g.get("_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
        
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,"_database", None)
    if db is not None:
        db.close()



if __name__ == "__main__":
    app.run(debug=True)  
    