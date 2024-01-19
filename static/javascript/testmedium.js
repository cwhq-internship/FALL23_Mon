function checkScore () {
  if (score > 20) {
    message = " powerful wizard ";
  } else if (score > 10) {
    message = " rising sorcerer ";
  } else {
    message = " novice magician  ";
  }
  document.getElementById("typingMessage").textContent = message;
}

function onTestComplete() {
  $.post('/increment_test_count', function(data) {
    console.log('Test counter incremented');
  });
  var wpmValue = document.getElementById('WPM').innerText;
  var difficultyValue = "Medium";
  testCount = 1;

  $.ajax({
      type: 'POST',
      url: '/submit_test_result',
      data: { wpm: wpmValue, difficulty: difficultyValue, count: testCount},
      success: function (response) {
          console.log('Test result submitted successfully');
      },
      error: function (error) {
          console.error('Error submitting test result:', error);
      }
  });
}