const LibListItems = document.getElementsByClassName("library-list-item");

function deactivateAllLibItems() {
  for (let i = 0; i < LibListItems.length; i++) {
    try {
      LibListItems[i].classList.remove("active");
    } catch (e) {}
  }
}

// 2. loop through the options and add the event listener to each element
Array.from(LibListItems).forEach((item) => {
  item.addEventListener("click", function () {
    deactivateAllLibItems();
    this.classList.add("active");
  });
});
