function menuShow() {
  let menuMobile = document.querySelector(".mobile-menu");
  if (menuMobile.classList.contains("open")) {
    menuMobile.classList.remove("open");
    document.querySelector(".icon").src = "/static/img/menu_white_36dp.svg";
  } else {
    menuMobile.classList.add("open");
    document.querySelector(".icon").src = "/static/img/close_white_36dp.svg";
  }
}

function confirmDelete(animalId) {
  if (confirm("Tem certeza que deseja excluir este animal?")) {
    document.getElementById("delete-form-" + animalId).submit();
  }
}
