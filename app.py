from flask import Flask, render_template, Request

app=Flask(__name__)

@app.route('/', methods=["get","post"])
def index():
  return render_template('index.html')

  if __name__=='__main__':
    #app.run()
    app.run(host='0.0.0.0', port=3000, debug=True)
