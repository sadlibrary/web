const LibListItems = document.getElementsByClassName("library-list-item");


const currentLibraryButton = document.getElementById("current-library-button");
const currentLibraryInput = document.getElementById("add-file-current-library-input");

let currentLibrary = '';

function deactivateAllLibItems() {
  for (let i = 0; i < LibListItems.length; i++) {
    try {
      LibListItems[i].classList.remove("active");
    } catch (e) {}
  }
}

Array.from(LibListItems).forEach((item) => {
  item.addEventListener("click", function () {
    deactivateAllLibItems();
    this.classList.add("active");
    console.log("before: " + currentLibraryInput.name + " " + currentLibraryInput.value);
    currentLibraryInput.value = this.getElementsByClassName("library-name-text")[0].innerHTML;
    console.log("after: " + currentLibraryInput.name + " " + currentLibraryInput.value);
    sessionStorage.setItem('activeLib', this.getElementsByClassName("library-name-text")[0].innerHTML);
    // console.log(current)
    currentLibraryButton.click();
  });
});

window.onload = function () {
  let element = sessionStorage.getItem('activeLib');
  console.log(element);
  Array.from(LibListItems).forEach((item) => {
    if (item.getElementsByClassName("library-name-text")[0].innerHTML === element) {
      item.classList.add("active");
    }
  });
}
