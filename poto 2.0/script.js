const clickSound = document.getElementById("clickSound");
const navLinks = document.querySelectorAll(".nav-Link");

navLinks.forEach((link) => {
    link.addEventListener("click", () => {
    clickSound.currentTime = 0;
    clickSound.play();
    });
});


