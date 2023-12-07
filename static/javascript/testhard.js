function checkScore () {
  if (score > 9) {
    message = " fantastic ";
  } else if (score > 5) {
    message = " meh ";
  } else {
    message = " bad ";
  }
  document.getElementById("typingMessage").textContent = message;
}
