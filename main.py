from flask import Flask, render_template, url_for, session
app = Flask(__name__)
import sqlite3
from flask import g
from flask import request

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
    print(get_login_status())
    return my_render("home.html", posts=posts)

@app.route("/about")
def about():
    return my_render("about.html", title="About")

@app.route("/register")
def register():
    #TODO fix visning
    return my_render("register.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    print(request.form["username"])    
    c = get_db().cursor()
    c.execute('''
              SELECT name FROM users
              ''')
    x = 0
    for i in c:
        print(i)
        if i[0] == request.form["username"]:
             x += 1
    print(x)
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
        for i in c:
            print(i)
    
        return my_render("login.html")
    else:
        return my_render('register.html', success = False)


def get_user_id(user):
    ID = get_db().cursor().execute('''SELECT Id FROM Users WHERE name = ?''',user)
    print("-------------------------------------------------------------------------------------")
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
        #TODO create user object, store in session.
        ID=get_user_id(user)
        print(ID)
        session['currentuser'] = ID
        return my_render('home.html', posts=posts, tracks=get_tracks())
    else:
        session.pop('currentuser', None)
        return my_render('login.html', success = False) 

def login_success(user, pw):
    c = get_db().cursor()
    c.execute('''
              SELECT password FROM users WHERE name=?
              ''',user)
    print(c)
    for i in c:
        print(i)
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
    return render_template(template, loggedin=login_status, **kwargs)

@app.route('/create_track')
def create_track():
    return my_render("track.html", tracks=get_tracks())

@app.route("/create_track_real", methods=["POST"])
def create_track_real():
    print(request.form["trackname"])    
    c = get_db().cursor()
    c.execute('''
              SELECT name FROM tracks WHERE user_id=?
              ''',str(session['currentuser']))
    x = 0
    for i in c:
        print(i)
        if i[0] == request.form["trackname"]:
             x += 1
    print(x)
    if x == 0:
        c.execute('''
                   INSERT INTO tracks
                   (name, type, user_id)
                   VALUES
                   (?, ?, ?);
                   ''',(request.form["trackname"],request.form["type"], session['currentuser']))
        
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
    
        return my_render("my_tracks.html", tracks=get_tracks())
    else:
        return my_render('track.html', success = False, tracks=get_tracks())
    
@app.route("/my_tracks")
def my_tracks():
    return my_render("my_tracks.html", tracks=get_tracks())

def get_tracks():
    c = get_db().cursor()
    c.execute('''
              SELECT * FROM tracks WHERE user_id=?
              ''',str(session['currentuser']))
    tracks = []
    for track in c:
        print(track[4])
        tracks.append(track)
        
    return tracks

@app.route("/create_tables")
def create_tables():
    #TODO hide
    c = get_db().cursor()
    try:
        c.execute(''' 
                               CREATE TABLE users(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name TEXT,
                               age INTEGER,
                               gender INTEGER,
                               password TEXT,
                               email TEXT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE tracks(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                               name TEXT,
                               active INTEGER,
                               type INTEGER,
                               date TEXT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE trackvars(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               track_id INTEGER,
                               starttime TEXT,
                               endtime TEXT,
                               value INT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)

    return "cool"                 

@app.route("/clear_tables")
def clear_tables():
    c = get_db().cursor()
    try:
        c.execute(''' 
                               DROP TABLE users;
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               DROP TABLE tracks;
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               DROP TABLE trackvars;
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE users(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name TEXT,
                               age INTEGER,
                               gender INTEGER,
                               password TEXT,
                               email TEXT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE tracks(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                               name TEXT,
                               active INTEGER,
                               type INTEGER,
                               date TEXT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE trackvars(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               track_id INTEGER,
                               starttime TEXT,
                               endtime TEXT,
                               value INT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)

    return "cool"                 
@app.route("/clear_users")
def clear_users():
    c = get_db().cursor()
    try:
        c.execute(''' 
                               DROP TABLE users;
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)

    try:
        c.execute(''' 
                               CREATE TABLE users(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name TEXT,
                               age INTEGER,
                               gender INTEGER,
                               password TEXT,
                               email TEXT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)


    return "cool"
@app.route("/clear_tracks")
def clear_tracks():
    c = get_db().cursor()
    try:
        c.execute(''' 
                               DROP TABLE tracks;
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               DROP TABLE trackvars;
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE tracks(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                               name TEXT,
                               active INTEGER,
                               type INTEGER,
                               date TEXT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE trackvars(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               track_id INTEGER,
                               starttime TEXT,
                               endtime TEXT,
                               value INT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)

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
    