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