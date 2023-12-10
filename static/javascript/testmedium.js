function checkScore () {
  if (score > 20) {
    message = " fantastic ";
  } else if (score > 15) {
    message = " meh ";
  } else {
    message = " bad ";
  }
  document.getElementById("typingMessage").textContent = message;
}
