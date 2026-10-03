/* jshint esversion: 6 */
// TasteHub JavaScript

console.log("TasteHub JavaScript loaded");

const searchInput = document.querySelector("#recipe-search");
const searchButton = document.querySelector("#search-button");
const recipeItems = document.querySelectorAll(".recipe-item");
const noResults = document.querySelector("#no-results");

function filterRecipes() {
    const searchTerm = searchInput.value.toLowerCase().trim();
    let visibleRecipes = 0;
    recipeItems.forEach(recipe => {
        const recipeName = recipe.querySelector(".card-title").textContent.toLowerCase().trim();

        const matchesSearch =
            searchTerm === "" || recipeName.includes(searchTerm);

        if (matchesSearch) {
            recipe.style.display = "block";
            visibleRecipes++;
        } else {
            recipe.style.display = "none";
        }

    });

    if (visibleRecipes === 0) {
        noResults.style.display = "block";
    } else {
        noResults.style.display = "none";
    }
}


if (searchButton && searchInput) {

    searchButton.addEventListener("click", function () {
        filterRecipes();
    });

    searchInput.addEventListener("input", function () {
        filterRecipes();
    });

}