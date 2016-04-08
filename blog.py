import pip
try:
    from weppy import App,Field, Form
    from pydblite import Base
except:
    pip.main(['install','weppy'])
    pip.main(['install','pydblite'])
    from weppy import App,Field, Form
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
def a():
    simple_form = Post.Form({
        'topic' : Field(),
        'text' : Field('text'),
        'name': Field(),
        'email': Field(),
        )
    })
    if simple_form.accepted:
        inserted_number = form.params.number
        #do something
    return dict(form=simple_form)
@app.route("/")
def hello():
    return """hi
    
    
    
    """

if __name__ == "__main__":
    app.run()
