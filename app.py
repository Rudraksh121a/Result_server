from flask import Flask, request,jsonify
from fatch_res import scrap

app = Flask(__name__)

@app.route('/get_input')  
def get_input():
    
    enrollment = request.args.get('enrollment', default='No enrollment provided',type=str)
    sem = request.args.get('sem', default='No SEM provided',type=str)  
    return jsonify(scrap(enrollment=enrollment,sem=sem))


if __name__ == '__main__':
    app.run()
