from flask import Flask

"""__name__ : The idea of the first parameter is to give Flask an idea of what
    belongs to your application.  This name is used to find resources
    on the filesystem, can be used by extensions to improve debugging
    information and a lot more.

    So it's important what you provide there.  If you are using a single
    module, `__name__` is always the correct value.  If you however are
    using a package, it's usually recommended to hardcode the name of
    your package there.

    ABOVE text is from flask/app.py"""

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def hello():
    return "Hello Mathu"


@app.route("/contact")
def contact():
    return "This is contact page"

if __name__ == "__main__":
    app.run()