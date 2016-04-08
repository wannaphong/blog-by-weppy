import pip
try:
    from weppy import App
    from pydblite import Base
except:
    pip.main(['install','weppy'])
    pip.main(['install','pydblite'])
    from weppy import App
    from pydblite import Base
import os
if (not os.path.isfile("db.pydb")):
    db = Base('db.pydb') # สร้างไฟล์ฐานข้อมูล test.pydb
    db.create('name', 'age', 'size') # สร้าง field เก็บข้อมูล
    print("install ok")
else:
    db = Base('db.pydb')

db = Base('db.pydb') # สร้างไฟล์ฐานข้อมูล test.pydb
db.create('name', 'age', 'size') # สร้าง field เก็บข้อมูล
app = App(__name__)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    app.run()
