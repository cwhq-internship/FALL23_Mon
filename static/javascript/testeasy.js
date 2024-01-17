function checkScore () {
  if (score > 35) {
    message = " powerful wizard ";
  } else if (score > 25) {
    message = " rising sorcerer ";
  } else {
    message = " novice magician  ";
  }
  document.getElementById("typingMessage").textContent = message;
}
