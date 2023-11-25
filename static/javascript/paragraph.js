document.addEventListener("DOMContentLoaded", function () {
    const quotes = [
        "Lorem ipsum dolor sit amet...",
        "The quick brown fox jumps over the lazy dog.",
        "To be or not to be, that is the question.",
        // Add more quotes as needed
    ];

    const textElement = document.getElementById("text-to-type");
    const userInput = document.getElementById("user-input");
    const timerElement = document.getElementById("time");
    const wpmElement = document.getElementById("wpm");
    const countdownElement = document.getElementById("countdown");
    const retryButton = document.getElementById("retry-btn");

    let timerInterval;
    let countdownInterval;

    function startCountdown() {
        countdownElement.innerText = "3";
        let countdown = 3;

        countdownInterval = setInterval(function () {
            countdown--;

            if (countdown <= 0) {
                clearInterval(countdownInterval);
                countdownElement.style.display = "none";
                startGame();
            } else {
                countdownElement.innerText = countdown;
            }
        }, 1000);
    }

    function startGame() {
        const randomIndex = Math.floor(Math.random() * quotes.length);
        const randomQuote = quotes[randomIndex];

        textElement.innerText = randomQuote;
        userInput.removeAttribute("disabled");
        userInput.value = "";
        userInput.style.color = "black"; // Reset to default color
        userInput.focus();

        retryButton.style.display = "none";
        timerInterval = setInterval(function () {
            updateTimer();
        }, 1000);
    }

    function endGame() {
        clearInterval(timerInterval);
        clearInterval(countdownInterval);
        userInput.setAttribute("disabled", "true");
        retryButton.style.display = "block";
        retryButton.addEventListener("click", handleRetryButtonClick);
    }

    function updateTimer() {
        const timerValue = parseInt(timerElement.innerText);
        timerElement.innerText = timerValue + 1 + "s";
    }

    function handleRetryButtonClick() {
        retryButton.style.display = "none";

        setTimeout(function () {
            retryButton.style.display = "block";
        }, 2000);

        startCountdown();
    }

    userInput.addEventListener("input", function () {
        const userInputText = userInput.value.trim();
        const targetText = textElement.innerText.trim();

        if (userInputText === targetText) {
            userInput.style.color = "black"; // Reset to default color
        } else {
            userInput.style.color = "red";
        }

        const words = userInputText.split(/\s+/);
        const wordCount = words.length;

        if (userInputText === targetText) {
            const wpm = calculateWPM(wordCount, parseInt(timerElement.innerText));
            wpmElement.innerText = "WPM: " + wpm;
            endGame();
        }
    });

    function calculateWPM(words, time) {
        const minutes = time / 60;
        const wpm = Math.round(words / minutes);
        return wpm;
    }

    retryButton.addEventListener("click", handleRetryButtonClick);

    startCountdown();
});