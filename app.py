from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    home_team = request.form['home-team']
    away_team = request.form['away-team']

    # 경기 데이터를 로드하고 전처리
    df = pd.read_csv('mlb_data.csv')
    X = df[['HomeScore', 'AwayScore']].values
    y = df['HomeWin'].values

    # 로지스틱 회귀 분류기 모델 생성 및 학습
    model = LogisticRegression()
    model.fit(X, y)

    # 입력된 팀의 점수를 생성
    home_score = int(request.form['home-score'])
    away_score = int(request.form['away-score'])

    # 예측
    prediction = model.predict([[home_score, away_score]])

    result = f'{home_team} vs {away_team}: '

    if prediction == 1:
        result += f'{home_team} 팀이 이길 것으로 예측됩니다.'
    else:
        result += f'{away_team} 팀이 이길 것으로 예측됩니다.'

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()
