
from flask import Flask, redirect, url_for, request



app = Flask(__name__)


@app.route('/success/<dep>/<arr>', )
def success(dep, arr):
    return 'departure: arrival: {}'.format(arr)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form
        dep = data['origin']
        arr = data['destination']
        print(arr, 0)
        return redirect(url_for('success', dep=dep, arr=arr))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)
