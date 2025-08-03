document.addEventListener("DOMContentLoaded", function () {
  const primaryColor = "#02d0e1";
  const backgroundColor = "#0f1c2e";
  const cardBg = "#1e2f45";
  const textColor = "#ffffff";
  const accentColor = "#C0F751";

  // Set overall theme
  document.body.style.backgroundColor = backgroundColor;
  document.body.style.color = textColor;

  // Animate Logo (if exists)
  const logo = document.querySelector("img[alt='Recofy logo']");
  if (logo) {
    logo.style.transition = "transform 0.3s ease";
    logo.addEventListener("mouseenter", () => {
      logo.style.transform = "scale(1.05)";
    });
    logo.addEventListener("mouseleave", () => {
      logo.style.transform = "scale(1)";
    });
  }

  // Buttons Styling Observer
  const observer = new MutationObserver(() => {
    document.querySelectorAll("button").forEach((btn) => {
      btn.style.backgroundColor = primaryColor;
      btn.style.color = "#fff";
      btn.style.border = "none";
      btn.style.borderRadius = "8px";
      btn.style.padding = "10px 20px";
      btn.style.fontWeight = "600";
      btn.style.transition = "all 0.3s ease";
      btn.onmouseover = () => {
        btn.style.backgroundColor = accentColor;
        btn.style.color = "#000";
      };
      btn.onmouseout = () => {
        btn.style.backgroundColor = primaryColor;
        btn.style.color = "#fff";
      };
    });
  });

  observer.observe(document.body, { childList: true, subtree: true });

  // Apply fade-in animation to main app content
  const main = document.querySelector(".main");
  if (main) {
    main.style.opacity = 0;
    main.style.transition = "opacity 0.8s ease";
    setTimeout(() => {
      main.style.opacity = 1;
    }, 300);
  }

  // Card Animation on Scroll (if needed)
  const cards = document.querySelectorAll(".recommend-box, .home-card");
  cards.forEach((card) => {
    card.style.transition = "transform 0.3s ease, box-shadow 0.3s ease";
    card.addEventListener("mouseenter", () => {
      card.style.transform = "translateY(-4px)";
      card.style.boxShadow = "0 6px 20px rgba(2, 208, 225, 0.2)";
    });
    card.addEventListener("mouseleave", () => {
      card.style.transform = "translateY(0)";
      card.style.boxShadow = "0 4px 12px rgba(2, 208, 225, 0.15)";
    });
  });
});
