from flask import Flask, render_template, request
from sports_prop import player_props

app = Flask(__name__)

app.config["SECRET_KEY"] = "APRKJGBAJPGDFHOH"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sport = request.form['sport']
        over_list, under_list = player_props(sport)
        return render_template('results.html', over_list=over_list, under_list=under_list)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)