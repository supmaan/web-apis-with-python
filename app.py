from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)
# Define what the app does
@app.route("/greet")
def index():
    res = 0
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    if not fname and not lname:
        return jsonify({'status':'error'})
    if not lname and fname:
        res = jsonify({'data':f'Привет, {fname}!'})
    if not fname and lname:
        res = jsonify({'data':f'Здравствуйте, {lname}!'})
    if fname and lname:
        res = jsonify({'data':f'Ваше имя - {fname} {lname}?'})
        
        

    # name = request.args.get('name')
    # res = {'data':f"Hello, {name}!"}
    # if not name:
    #     return jsonify({'status':'error'})
    return res
    # """
    # TODO:
    # 1. Capture first name & last name
    # 2. If either is not provided: respond with an error
    # 3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    # 4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    # 5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    # """
    # return jsonify("TODO")
