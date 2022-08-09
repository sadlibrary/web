const signUpButton = document.getElementById("signUp");
const signInButton = document.getElementById("signIn");
const container = document.getElementById("container");

signUpButton.addEventListener("click", () => {
  container.classList.add("right-panel-active");
});

signInButton.addEventListener("click", () => {
  container.classList.remove("right-panel-active");
});

const lis = document.querySelectorAll("li");
let wid = document.getElementById("id_username").offsetWidth;

for (let item of lis) {
  item.style.minWidth = wid + "px";
}
