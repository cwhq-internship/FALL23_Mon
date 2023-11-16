window.addEventListener('load', init);

// levels
const levels = {
    easy: 5,
    medium: 3,
    hard: 1
}

// change level
const currentLevel = levels.easy;

// global variables
let time = currentLevel;
let score = 0;
let isPlaying;

// dom elements
const wordInput = document.querySelector('#word-input');

const scoreDisplay = document.querySelector('#score');
const timeDisplay = document.querySelector('#time');
const message = document.querySelector('#message');
const seconds = document.querySelector('#seconds');

const words = [
    'hat',
    'river',
    'lucky',
    'statue',
    'generate',
    'stubborn',
    'cocktail',
    'runaway',
    'joke',
    'developer',
    'establishment',
    'hero',
    'javascript',
    'nutrition',
    'revolver',
    'echo',
    'siblings',
    'investigate',
    'horrendous',
    'symptom',
    'laughter',
    'magic',
    'master',
    'space',
    'definition'
  ];


function getRandomWord() {
    return words[Math.floor(Math.random() * words.length)];
}
 
let firstWord = getRandomWord();
let newWord = getRandomWord();
// init
function init() {
    seconds.innerHTML = currentLevel;
    updateWords;
    wordInput.addEventListener('input', startMatch);
    setInterval(countdown, 1000);
    setInterval(checkStatus, 50);
}

//start match
function startMatch() {
    
    const inputField = document.getElementById('inputField');
  inputField.addEventListener('input', function(event) {
    const typedWord = event.target.value.trim().toLowerCase();

    if (typedWord === currentWord.toLowerCase()) {
      currentWord = nextWord;
      nextWord = getRandomWord();
      updateWords();
      inputField.value = ''; // Clear the input field
    }

    if(score === -1) {
      scoreDisplay.innerHTML = 0;
    } else {
      scoreDisplay.innerHTML = score;  
    }   
});
}

function matchWords() {
    if(wordInput.value === currentWord.innerHTML) {
        message.innerHTML = 'correct';
        return true;
    } else {
        message.innerHTML = '';
        return false;
    }
}

// this gets the words and then updates them
function updateWords() {
    const currentWord = document.querySelector('#current-word');
    currentWord.textContent = firstWord;

    const nextWord = document.querySelector('#next-word');
    nextWord.textContent = nextWord;
}

//countdown timer
function countdown() {
    // make sure time no run out
    if(time > 0) {
        // dec
        time--;
    } else if(time === 0) {
        //game over
        isPlaying = false;
    }
    // show time
    timeDisplay.innerHTML = time;
}

// game status
function checkStatus() {
    if(!isPlaying && time === 0) {
        message.innerHTML = 'game over!!';
        score = -1;
    }
}