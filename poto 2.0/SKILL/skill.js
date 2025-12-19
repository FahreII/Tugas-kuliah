const clickSound = document.getElementById("clickSound");
const navLinks = document.querySelectorAll(".nav-link");

navLinks.forEach((link) => {
  link.addEventListener("click", () => {
    clickSound.currentTime = 0;
    clickSound.play();
  });
});
