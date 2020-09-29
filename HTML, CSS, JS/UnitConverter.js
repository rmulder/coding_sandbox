function toggleFromDropdown() {
console.log("Function reached");
  document.getElementById("from-dropdown").classList.toggle("show");
}

function filterFunction() {
  var input, filter, div, listItem, txtValue, i;

  input = document.getElementById("from-selector-input");
  filter = input.value.toUpperCase();
  div = document.getElementById("from-dropdown");
  listItem = div.getElementsByTagName("li");

  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}
