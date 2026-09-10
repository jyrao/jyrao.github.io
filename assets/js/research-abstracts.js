document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".abstract-toggle").forEach(function (button, index) {
    var copy = button.closest(".research-copy");
    var abstract = copy.querySelector(".research-abstract");
    var panel;

    function prepare(content) {
      panel = document.createElement("div");
      panel.className = "abstract-panel";
      panel.id = "research-abstract-" + index;
      panel.setAttribute("aria-hidden", "true");
      panel.inert = true;
      var inner = document.createElement("div");
      inner.className = "abstract-panel__inner";
      content.hidden = false;
      inner.appendChild(content);
      panel.appendChild(inner);
      copy.appendChild(panel);
      button.setAttribute("aria-controls", panel.id);
    }

    function setExpanded(expanded) {
      // Commit the collapsed grid before opening freshly fetched content.
      panel.getBoundingClientRect();
      panel.classList.toggle("is-expanded", expanded);
      panel.setAttribute("aria-hidden", String(!expanded));
      panel.inert = !expanded;
      button.setAttribute("aria-expanded", String(expanded));
      button.textContent = expanded ? (button.dataset.hide || "Hide abstract") : (button.dataset.show || "Abstract");
    }

    button.setAttribute("aria-expanded", "false");
    if (abstract) prepare(abstract);

    button.addEventListener("click", function () {
      if (panel) {
        setExpanded(button.getAttribute("aria-expanded") !== "true");
        return;
      }
      if (!button.dataset.abstractUrl) return;
      button.disabled = true;
      button.textContent = "Loading abstract…";
      fetch(button.dataset.abstractUrl + ".html")
        .then(function (response) {
          if (!response.ok) throw new Error("Publication request failed");
          return response.text();
        })
        .then(function (html) {
          var page = new DOMParser().parseFromString(html, "text/html");
          var content = page.querySelector(".page__content");
          var card = content && content.querySelector(".research-item");
          if (!content) throw new Error("Publication content not found");
          if (card) card.remove();
          var text = content.textContent.trim();
          if (!text) throw new Error("Abstract is empty");
          abstract = document.createElement("div");
          abstract.className = "research-abstract";
          abstract.textContent = text;
          prepare(abstract);
          button.disabled = false;
          setExpanded(true);
        })
        .catch(function () {
          button.disabled = false;
          button.textContent = "Abstract unavailable — retry";
        });
    });
  });
});
