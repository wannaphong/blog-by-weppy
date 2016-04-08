import pip
try:
    from weppy import App,Field, Form,request, session, url, redirect, abort
    from weppy.dal import DAL, Field, Model, belongs_to, has_many
    from weppy.tools import requires
    from weppy.tools.auth import Auth, AuthUser
    from weppy.sessions import SessionCookieManager
    #from weppy.dal import Field, Model
    from pydblite import Base
except:
    pip.main(['install','weppy'])
    pip.main(['install','pydblite'])
    from weppy import App,Field, Form,request, session, url, redirect, abort
    from weppy.dal import DAL, Field, Model, belongs_to, has_many
    from weppy.tools import requires
    from weppy.tools.auth import Auth, AuthUser
    from weppy.sessions import SessionCookieManager
    #from weppy.dal import Field, Model
    from pydblite import Base
import os
if (not os.path.isfile("db.pydb")):
    db = Base('db.pydb') # สร้างไฟล์ฐานข้อมูล test.pydb
    db.create('topic','text','name','email') # สร้าง field เก็บข้อมูล
    print("install ok")
else:
    db = Base('db.pydb')
app = App(__name__)
nameblog = "My Blog"
@app.route('/form')
class User(Model):
    name = Field('string')
    has_many('posts')

    validation = {
        'email': {'is': 'email'}
    }

class Post(Model):
    belongs_to('user')
    body = Field('text')

    validation = {
        'body': {'presence': True}
    }
          
@app.route("/")
def hello():
    return """hi
    
    
    
    """

if __name__ == "__main__":
    app.run()
