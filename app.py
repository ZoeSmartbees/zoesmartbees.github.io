from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/next")
def next_page():
    return render_template("next.html")

if __name__ == "__main__":
    app.run(debug=True)



# le site se trouve sur http://dev.monsite.local:5000/


#je fais u test