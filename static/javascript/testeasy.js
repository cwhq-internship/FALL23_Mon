function checkScore () {
  if (score > 35) {
    message = " fantastic ";
  } else if (score > 25) {
    message = " meh ";
  } else {
    message = " bad ";
  }
  document.getElementById("typingMessage").textContent = message;
}
