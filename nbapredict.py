<!DOCTYPE html>
<html>
<head>
  <title>NBA 팀 경기 예측</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
  <h1>NBA 팀 경기 예측</h1>

  <div>
    <label for="home-team">Home Team:</label>
    <input type="text" id="home-team">
  </div>

  <div>
    <label for="away-team">Away Team:</label>
    <input type="text" id="away-team">
  </div>

  <div>
    <button id="predict-button">예측</button>
  </div>

  <div id="prediction-result"></div>

  <script>
    $(document).ready(function() {
      $('#predict-button').click(function() {
        var homeTeam = $('#home-team').val();
        var awayTeam = $('#away-team').val();

        // 경기 예측 알고리즘
        var prediction = predictMatch(homeTeam, awayTeam);

        // 예측 결과 출력
        $('#prediction-result').text(prediction);
      });

      function predictMatch(homeTeam, awayTeam) {
        var random = Math.random(); // 0과 1 사이의 난수 생성

        if (random < 0.5) {
          return homeTeam + ' 팀이 이길 것으로 예측됩니다.';
        } else {
          return awayTeam + ' 팀이 이길 것으로 예측됩니다.';
        }
      }
    });
  </script>
</body>
</html>
