import pip
try:
    from weppy import App
    from pydblite import Base
except:
    pip.main(['install','weppy'])
    pip.main(['install','pydblite'])
    from weppy import App
    from pydblite import Base

db = Base('test.pydb') # สร้างไฟล์ฐานข้อมูล test.pydb
db.create('name', 'age', 'size') # สร้าง field เก็บข้อมูล
app = App(__name__)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    app.run()
