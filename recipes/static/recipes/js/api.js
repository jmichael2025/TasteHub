// TasteHub API JavaScript

console.log("TasteHub API JavaScript loaded");

const apiSearchInput = document.querySelector("#api-search");

if (apiSearchInput) {

    apiSearchInput.addEventListener("input", function () {

        if (apiSearchInput.value.trim() === "") {
            window.location.href = window.location.pathname;
        }

    });

}