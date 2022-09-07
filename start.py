from application import create_app
from application.extensions import db

app = create_app("development")

@app.route('/')
def hello_world():
    res = list(db.session.execute("select 1"))
    return res

if __name__ == '__main__':
    app.run()
