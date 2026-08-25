document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".abstract-toggle").forEach(function (button) {
    button.addEventListener("click", function () {
      var copy = button.closest(".research-copy");
      var abstract = copy.querySelector(".research-abstract");
      if (!abstract && button.dataset.abstractUrl) {
        button.disabled = true;
        button.textContent = "Loading abstract…";
        fetch(button.dataset.abstractUrl + ".html")
          .then(function (response) { return response.text(); })
          .then(function (html) {
            var page = new DOMParser().parseFromString(html, "text/html");
            var content = page.querySelector(".page__content");
            var card = content && content.querySelector(".research-item");
            if (!content) throw new Error("Publication content not found");
            if (card) card.remove();
            abstract = document.createElement("div");
            abstract.className = "research-abstract";
            abstract.textContent = content.innerText.trim();
            copy.appendChild(abstract);
            abstract.hidden = false;
            button.disabled = false;
            button.setAttribute("aria-expanded", "true");
            button.textContent = "Hide abstract";
          })
          .catch(function () { button.disabled = false; button.textContent = "Abstract unavailable"; });
        return;
      }
      if (!abstract) return;
      var isExpanded = button.getAttribute("aria-expanded") === "true";
      abstract.hidden = isExpanded;
      button.setAttribute("aria-expanded", String(!isExpanded));
      button.textContent = isExpanded ? (button.dataset.show || "Abstract") : (button.dataset.hide || "Hide abstract");
    });
  });
});
