document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".abstract-toggle").forEach(function (button) {
    button.addEventListener("click", function () {
      var abstract = button.closest(".research-copy").querySelector(".research-abstract");
      var isExpanded = button.getAttribute("aria-expanded") === "true";
      abstract.hidden = isExpanded;
      button.setAttribute("aria-expanded", String(!isExpanded));
      button.textContent = isExpanded ? (button.dataset.show || "Abstract") : (button.dataset.hide || "Hide abstract");
    });
  });
});
