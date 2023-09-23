document.addEventListener("DOMContentLoaded", function () {
  console.log("\n\n\n------------------------------\n");
  console.log("static/js/scrollChecker.js\n\n");
  // Continuos scrolling
  window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
      console.log("You Reach the Bottom");
    }
  };

  console.log("User Scrolling: ");
  console.log(window.scrollY);
  console.log(window.innerHeight);
  console.log("\n------------------------------\n");
});
