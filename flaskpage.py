# Jake Grangier, 11/11/22
# Photo Album
# Inspired by w3 schools
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homp():
    return render_template('home.html')

@app.route('/l')
def lakeboi():
    return render_template('Lake Gallery.html')

@app.route('/m')
def mounty():
    return render_template('mountain.html')
    
if __name__ == '__main__':
    app.run()
    