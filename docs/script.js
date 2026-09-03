(function () {
  "use strict";

  var root = document.documentElement;
  var header = document.querySelector(".site-header");
  var nav = document.getElementById("site-nav");
  var navToggle = document.querySelector("[data-nav-toggle]");
  var themeToggle = document.querySelector("[data-theme-toggle]");
  var storedTheme = null;

  try {
    storedTheme = window.localStorage.getItem("theme");
  } catch (err) {
    storedTheme = null;
  }

  if (storedTheme === "light" || storedTheme === "dark") {
    root.setAttribute("data-theme", storedTheme);
  }

  function setExpanded(isOpen) {
    if (!header || !navToggle) return;
    header.classList.toggle("is-open", isOpen);
    navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
  }

  if (navToggle) {
    navToggle.addEventListener("click", function () {
      setExpanded(!header.classList.contains("is-open"));
    });
  }

  if (nav) {
    nav.addEventListener("click", function (event) {
      if (event.target.closest("a")) setExpanded(false);
    });
  }

  if (themeToggle) {
    themeToggle.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      if (!root.getAttribute("data-theme")) {
        var prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
        next = prefersDark ? "light" : "dark";
      }
      root.setAttribute("data-theme", next);
      try {
        window.localStorage.setItem("theme", next);
      } catch (err) {
        /* ignore quota / private mode */
      }
    });
  }

  document.querySelectorAll("[data-copy]").forEach(function (button) {
    button.addEventListener("click", function () {
      var value = button.getAttribute("data-copy") || "";
      var done = function () {
        var previous = button.textContent;
        button.textContent = "已复制";
        window.setTimeout(function () {
          button.textContent = previous;
        }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(value).then(done).catch(function () {
          window.prompt("复制提取码", value);
        });
      } else {
        window.prompt("复制提取码", value);
      }
    });
  });

  var tabButtons = Array.prototype.slice.call(document.querySelectorAll('[role="tab"]'));
  var tabPanels = {
    "tab-read": document.getElementById("panel-read"),
    "tab-raw": document.getElementById("panel-raw")
  };

  function selectTab(nextId) {
    tabButtons.forEach(function (button) {
      var selected = button.id === nextId;
      button.setAttribute("aria-selected", selected ? "true" : "false");
      button.tabIndex = selected ? 0 : -1;
      var panel = tabPanels[button.id];
      if (panel) panel.hidden = !selected;
    });
  }

  tabButtons.forEach(function (button, index) {
    button.addEventListener("click", function () {
      selectTab(button.id);
    });
    button.addEventListener("keydown", function (event) {
      var dest = null;
      if (event.key === "ArrowRight" || event.key === "ArrowDown") {
        dest = tabButtons[(index + 1) % tabButtons.length];
      } else if (event.key === "ArrowLeft" || event.key === "ArrowUp") {
        dest = tabButtons[(index - 1 + tabButtons.length) % tabButtons.length];
      } else if (event.key === "Home") {
        dest = tabButtons[0];
      } else if (event.key === "End") {
        dest = tabButtons[tabButtons.length - 1];
      }
      if (dest) {
        event.preventDefault();
        dest.focus();
        selectTab(dest.id);
      }
    });
  });

  var sectionIds = ["source", "pipeline", "examples", "usage", "limits"];
  var navLinks = sectionIds
    .map(function (id) {
      return {
        id: id,
        el: document.getElementById(id),
        link: nav ? nav.querySelector('a[href="#' + id + '"]') : null
      };
    })
    .filter(function (item) {
      return item.el && item.link;
    });

  if ("IntersectionObserver" in window && navLinks.length) {
    var visible = new Set();
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) visible.add(entry.target.id);
          else visible.delete(entry.target.id);
        });
        var current = sectionIds.find(function (id) {
          return visible.has(id);
        });
        navLinks.forEach(function (item) {
          if (item.id === current) item.link.setAttribute("aria-current", "true");
          else item.link.removeAttribute("aria-current");
        });
      },
      { rootMargin: "-30% 0px -60% 0px", threshold: 0.01 }
    );
    navLinks.forEach(function (item) {
      observer.observe(item.el);
    });
  }
})();
