

document.addEventListener("DOMContentLoaded", function() {
    const darkModeToggle = document.getElementById("dark-mode-toggle");
    const navbar = document.getElementById("navbar");
    const darkmodetext = document.querySelector(".darkmodetext");
  
    // Function to set dark mode styles
    function enableDarkMode() {
        document.body.style.backgroundImage = "url('/static/img/darkbackground.png')";
        navbar.classList.remove("navbar-light");
        navbar.classList.add("navbar-dark");
        darkmodetext.classList.add("darkmodetext2");
        // Save dark mode preference to localStorage
        localStorage.setItem("darkModeEnabled", "true");
    }
  
    // Function to set light mode styles
    function disableDarkMode() {
        document.body.style.backgroundImage = "url('/static/img/background.png')";
        navbar.classList.remove("navbar-dark");
        navbar.classList.add("navbar-light");
        darkmodetext.classList.remove("darkmodetext2");
        // Save light mode preference to localStorage
        localStorage.setItem("darkModeEnabled", "false");
    }
  
    // Event listener for dark mode toggle change
    darkModeToggle.addEventListener("change", () => {
        if (darkModeToggle.checked) {
            // Enable dark mode
            enableDarkMode();
        } else {
            // Disable dark mode
            disableDarkMode();
        }
    });
  
    // Function to apply navbar styles based on dark mode preference
    function applyNavbarStyles(isDarkMode) {
        if (isDarkMode) {
            navbar.classList.remove("navbar-light");
            navbar.classList.add("navbar-dark");
        } else {
            navbar.classList.remove("navbar-dark");
            navbar.classList.add("navbar-light");
        }
    } 
    // Check and apply dark mode setting from localStorage on page load
    const isDarkModeEnabled = localStorage.getItem("darkModeEnabled") === "true";
    if (isDarkModeEnabled) {
        darkModeToggle.checked = true;
        enableDarkMode(); // Apply dark mode styles if enabled in localStorage
        applyNavbarStyles(true); // Apply navbar styles based on dark mode preference
    } else {
        disableDarkMode(); // Apply light mode styles by default
        applyNavbarStyles(false); // Apply navbar styles based on light mode preference
    }
  });