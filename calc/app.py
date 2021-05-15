# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_op():
    """Adds a & b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)

@app.route("/sub")
def sub_op():
    """Subtracts b from a"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)

@app.route("/mult")
def mult_op():
    """Multiplies a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)

@app.route("/div")
def div_op():
    """Divides a by b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)

ops = {
    "add" : add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<op>")
def operation(op):
    """specific operation done on a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = ops[op](a,b)

    return str(result)
