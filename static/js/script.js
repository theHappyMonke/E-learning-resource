// This script is used to hide the navbar when the user scrolls down and show the navbar when the user scrolls up.
const navbar = document.getElementById('navbar');
let lastScrollY = window.scrollY;

window.addEventListener('scroll', () => {
    if (window.scrollY > lastScrollY) {
        // User scrolls down, hide the navbar
        navbar.classList.add('navbar-hidden');
    } else {
        // User scrolls up, show the navbar
        navbar.classList.remove('navbar-hidden');
    }
    lastScrollY = window.scrollY;  // Update last scroll position
});