from flask import Flask, render_template
import time
app = Flask(__name__)

##cc= time.ctime()
@app.route('/')
def home():
   return render_template('Untitled-1.html')
if __name__ == '__main__':
   app.run()

