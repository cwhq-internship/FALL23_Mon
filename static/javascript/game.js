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
const currentWord = document.querySelector('#current-word');
const scoreDisplay = document.querySelector('#score');
const timeDisplay = document.querySelector('#time');
const message = document.querySelector('#message');
const seconds = document.querySelector('#seconds');

const words = [
    'crazy? i was crazy once locked me into a room i jumped out the window And landed on the grass grass makes me crazy',
    'nincompoop',
    'poppycock',
    'astronomical',
    'tame impala',
    'bjork'
];

// init
function init() {
    seconds.innerHTML = currentLevel;
    showWord(words);
    wordInput.addEventListener('input', startMatch);
    setInterval(countdown, 1000);
    setInterval(checkStatus, 50);
}

//start match
function startMatch() {
    if(matchWords()) {
       isPlaying = true;
       time = currentLevel + 1;
       showWord(words);
       wordInput.value = '';
       score++;
    }

    if(score === -1) {
      scoreDisplay.innerHTML = 0;
    } else {
      scoreDisplay.innerHTML = score;  
    }   
}

// match current werd
function matchWords() {
    if(wordInput.value === currentWord.innerHTML) {
        message.innerHTML = 'correct';
        return true;
    } else {
        message.innerHTML = '';
        return false;
    }
}

// pick and show rand word
function showWord(words) {
    //generate random array
    const randIndex = Math.floor(Math.random() * words.length);
    //output random word
    currentWord.innerHTML = words[randIndex];
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
        message.innerHTML = 'Test complete';
        score = -1;
    }
}