const language_selectors = document.querySelectorAll(".fr-translate__language")

language_selectors.forEach(el => el.addEventListener("click", event => {
    document.cookie = "django_language=" + el.lang;
    window.location.reload()
}));
