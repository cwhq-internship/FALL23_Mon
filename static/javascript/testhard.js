function checkScore () {
  if (score > 9) {
    message = " powerful wizard ";
  } else if (score > 5) {
    message = " rising sorcerer ";
  } else {
    message = " novice magician  ";
  }
  document.getElementById("typingMessage").textContent = message;
}