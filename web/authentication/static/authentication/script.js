const signUpButton = document.getElementById("signUp");
const signInButton = document.getElementById("signIn");
const container = document.getElementById("container");

var renderType = document.getElementById("typeVar").value;

if (renderType == "register") {
  try {
    container.classList.add("right-panel-active");
  } catch (e) {}
} else {
  try {
    container.classList.remove("right-panel-active");
  } catch (e) {}
}

signUpButton.addEventListener("click", () => {
  container.classList.add("right-panel-active");
});

signInButton.addEventListener("click", () => {
  container.classList.remove("right-panel-active");
});
