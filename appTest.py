from flask import Flask, redirect, url_for, request, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name





@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        df = pd.DataFrame({"Name": ['Anurag', 'Manjeet', 'Shubham',
                            'Saurabh', 'Ujjawal'],

                   "Address": ['Patna', 'Delhi', 'Coimbatore',
                               'Greater noida', 'Patna'],

                   "ID": [20123, 20124, 20145, 20146, 20147],

                   "Sell": [140000, 300000, 600000, 200000, 600000]})

        return render_template("test_table.html")
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)


