  // Get Word List from python
  wordList2 = document.querySelector('#data_wl').value
  newString = wordList2.replace("[", "");
  n1 = newString.replace("]","")
  n2 = n1.replace(/"/g, '');
  n3 = n2.replace(/,/g, '');

  const wordList = n3.split(" ")
// Constants and definitions 

const inputField = document.getElementById('inputField');
const inner = document.querySelector('.inner');
let previousWord = '';
let currentWord = getRandomWord();
let nextWord = getRandomWord();
let score = 0;
let timeLeft = 30;
let timer;
let skipCount = 3;
let WPM = score * 2;

// Defines newWord with a random word
function getRandomWord() {
  let newWord = wordList[Math.floor(Math.random() * wordList.length)];
  while (newWord === previousWord) {
    newWord = wordList[Math.floor(Math.random() * wordList.length)];
  }
  previousWord = newWord;
  return newWord;
}

// Takes newWord pushes it into currentWord and nextWord
function updateWords() {
  const currentWordElement = document.getElementById('currentWord');
  currentWordElement.textContent = currentWord;

  const nextWordElement = document.getElementById('nextWord');
  nextWordElement.textContent = nextWord;
}

// Good old fasioned timer, pulled it from a stack overflow, only triggers after first word is correctly inputted
function startTimer() {
  timer = setInterval(() => {
    if (timeLeft > 0) {
      document.getElementById('timer').textContent = timeLeft;
      timeLeft--;
    } else {
      clearInterval(timer);
      inputField.value = '';
      document.getElementById('timer').textContent = '0';
      document.getElementById('gameOver').style.display = 'flex';
      document.getElementById("WPM").textContent = score * 2;
      document.getElementById('typingMessage').style.display = 'block';
      document.getElementById('retry').style.display = 'block';
      document.getElementById('nextWord').style.display = 'none';
      document.getElementById('currentWord').style.display = 'none';
      onTestComplete();
      inner.style.flexDirection = 'column';
      myInput.disabled = true;
    }
  }, 1000);
}
// Checking input, makes everything lowercase for consistency
function checkInput() {
  const inputField = document.getElementById('inputField');
  const typedWordElement = document.getElementById('typedWord');
  const currentWordElement = document.getElementById('currentWord');

  inputField.addEventListener('input', function(event) {
    const typedWord = event.target.value.trim().toLowerCase();
    const displayedWord = currentWordElement.textContent.trim().toLowerCase();
// This checks to see if the words are matching, and then changes the colors of the letter if wrong
    let comparedWord = '';
    for (let i = 0; i < displayedWord.length; i++) {
      if (typedWord[i] === displayedWord[i]) {
        comparedWord += typedWord[i];
      } else {
        comparedWord += `<span>${typedWord[i] || '_'}</span>`;
      }
    }
    typedWordElement.innerHTML = comparedWord;
// Checking if word matches, then it displays another, adds score, etc etc.
    if (typedWord === displayedWord) {
      if (!timer) {
        startTimer();
      }
      currentWord = nextWord;
      nextWord = getRandomWord();
      score++;
      document.getElementById('score').textContent = score;
      updateWords();
      inputField.value = '';
      typedWordElement.innerHTML = '';
      if (timer > 0) {
        document.getElementById('gameOver').style.display = 'none';
      }    
      inputField.maxLength = currentWord.length;
      checkScore();
    }
  });
}

// Hitting space, it switches current word with a new, random word. and next word too ofc.
// -1 from the skipCount
function skipWord() {
  const typedWordElement = document.getElementById('typedWord');
  if (skipCount > 0) {
    skipCount--;
    document.getElementById("skipCount").textContent = skipCount;
    currentWord = nextWord;
    nextWord = getRandomWord();
    updateWords();
    inputField.value = '';
    typedWordElement.innerHTML = '';
    inputField.maxLength = currentWord.length;
  }
}

// Shift = activate skipWord
document.addEventListener("keydown", function(event) {
  if (event.code === "ShiftLeft" || event.code === "ShiftRight") {
    skipWord();
  }
});



// Esc = immediate gameOver
document.addEventListener('keydown', function(event) {
  if (event.code === 'Escape') {
    clearInterval(timer);
    document.getElementById('timer').textContent = '0';
    document.getElementById('gameOver').style.display = 'flex';
    document.getElementById('WPM').textContent = score * 2;
    document.getElementById('typingMessage').style.display = 'block';
    document.getElementById('retry').style.display = 'block';
    document.getElementById('nextWord').style.display = 'none';
    document.getElementById('currentWord').style.display = 'none';
    inner.style.flexDirection = 'column';
    myInput.disabled = true;
  }
});
    
// Keyboard script, so it all words and stuff
document.addEventListener('keydown', function(event) {
  const keyPressed = event.key.toUpperCase();
  const keyElement = document.querySelector(`[data-key="${keyPressed}"]`);
  if (keyElement) {
    keyElement.classList.add('lit');
   }
});

document.addEventListener('keyup', function(event) {
  const keyPressed = event.key.toUpperCase();
  const keyElement = document.querySelector(`[data-key="${keyPressed}"]`);
    if (keyElement) {
    keyElement.classList.remove('lit');
  }
});
// end of Keyboard script

// Makes the "Click here and type a word to start!" disappear when clicked
function hideElementOnClick(inputId, elementId) {
  const inputField = document.getElementById(inputId);
  const elementToHide = document.getElementById(elementId);

  inputField.addEventListener('click', function() {
    elementToHide.style.display = 'none';
  });
}
hideElementOnClick('inputField', 'typeHere');

// this just runs the stuff beforehand so everything functions
updateWords();
checkInput();
checkScore();