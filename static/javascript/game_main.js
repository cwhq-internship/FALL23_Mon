// Defines newWord with a random word
export function getRandomWord(wordList, previousWord) {
    let newWord = wordList[Math.floor(Math.random() * wordList.length)];
    while (newWord === previousWord) {
      newWord = wordList[Math.floor(Math.random() * wordList.length)];
    }
    previousWord = newWord;
    return newWord;
  }

// Takes newWord pushes it into currentWord and nextWord

export function updateWords() {
    const currentWordElement = document.getElementById('currentWord');
    currentWordElement.textContent = currentWord;
  
    const nextWordElement = document.getElementById('nextWord');
    nextWordElement.textContent = nextWord;
  }
// Good old fasioned timer, pulled it from a stack overflow, only triggers after first word is correctly inputted
export function startTimer(score) {
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
        inner.style.flexDirection = 'column';
        myInput.disabled = true;
      }
    }, 1000);
  }

  // Checking input, makes everything lowercase for consistency
export function checkInput(wordList,score) {
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
          startTimer(score);
        }
        currentWord = nextWord;
        nextWord = getRandomWord(wordList);
        score++;
        document.getElementById('score').textContent = score;
        updateWords();
        inputField.value = '';
        typedWordElement.innerHTML = '';
        document.getElementById('gameOver').style.display = 'none';
        checkScore();
      }
    });
  }

// This judges you based on your score ofc :)
export function checkScore () {
    if (score > 35) {
      message = " fantastic ";
    } else if (score > 20) {
      message = " meh ";
    } else {
      message = " bad ";
    }
    document.getElementById("typingMessage").textContent = message;
  }
  
  // Hitting space, it switches current word with a new, random word. Doesn't affect next word at all.
  // -1 from the skipCount
export function skipWord(wordList) {
    if (skipCount > 0) {
      currentWord = getRandomWord(wordList);
      updateWords();
      skipCount--;
      inputField.value = '';
      document.getElementById("skipCount").textContent = skipCount;
    }
  }


  // Makes the "Click here and type a word to start!" disappear when clicked
export function hideElementOnClick(inputId, elementId) {
    const inputField = document.getElementById(inputId);
    const elementToHide = document.getElementById(elementId);
  
    inputField.addEventListener('click', function() {
      elementToHide.style.display = 'none';
    });
  }