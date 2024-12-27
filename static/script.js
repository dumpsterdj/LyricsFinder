// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
    // Apply fade-in animation to the header
    const header = document.querySelector(".header");
    header.style.opacity = "0";
    header.style.transform = "translateY(-20px)";
    setTimeout(() => {
        header.style.transition = "opacity 1s ease, transform 1s ease";
        header.style.opacity = "1";
        header.style.transform = "translateY(0)";
    }, 100);

    // Apply fade-in animation to the form or lyrics container
    const mainContent = document.querySelector("main");
    mainContent.style.opacity = "0";
    mainContent.style.transform = "translateY(20px)";
    setTimeout(() => {
        mainContent.style.transition = "opacity 1s ease, transform 1s ease";
        mainContent.style.opacity = "1";
        mainContent.style.transform = "translateY(0)";
    }, 300);

    // Add hover effect to all buttons
    const buttons = document.querySelectorAll("button");
    buttons.forEach((button) => {
        button.addEventListener("mouseover", () => {
            button.style.transform = "scale(1.05)";
            button.style.transition = "transform 0.2s ease";
        });

        button.addEventListener("mouseout", () => {
            button.style.transform = "scale(1)";
        });
    });

    // Add hover effect to all links
    const links = document.querySelectorAll("a");
    links.forEach((link) => {
        link.addEventListener("mouseover", () => {
            link.style.textDecoration = "underline";
            link.style.transition = "text-decoration 0.2s ease";
        });

        link.addEventListener("mouseout", () => {
            link.style.textDecoration = "none";
        });
    });

    // Add a scroll-to-top animation when clicking "Search Another Song" link
    const actionLinks = document.querySelectorAll(".action-links a");
    actionLinks.forEach((link) => {
        link.addEventListener("click", (event) => {
            event.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: "smooth",
            });
            setTimeout(() => {
                window.location.href = link.href;
            }, 500); // Redirect after smooth scroll
        });
    });
});
