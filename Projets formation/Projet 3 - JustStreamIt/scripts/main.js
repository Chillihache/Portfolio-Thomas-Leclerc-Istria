import { loadBestMovie } from './loads/loadBestMovie.js'
import { loadBestMovies } from './loads/loadBestMovies.js'
import { loadGenre1 } from './loads/loadGenre1.js'
import { loadGenre2 } from './loads/loadGenre2.js'
import { loadAllGenres } from './loads/loadAllGenres.js'
import { loadSelectedGenre } from './loads/loadSelectedGenre.js'
import { loadDetails } from './loads/loadDetails.js'
import { showMoreOnTablet } from './helpers/showMoreOnTablet.js'
import { showLessOnTablet } from './helpers/showMoreOnTablet.js'
import { showMoreOnPhone } from './helpers/showMoreOnPhone.js'
import { showLessOnPhone } from './helpers/showMoreOnPhone.js'


function load() {
    loadBestMovie()
    loadBestMovies()
    loadGenre1()
    loadGenre2()
    loadAllGenres()
}

function listeners() {
    document.addEventListener("DOMContentLoaded", () => {
        const selectorButton = document.querySelector(".selectorButton");

        loadSelectedGenre(selectorButton.value);

        selectorButton.addEventListener("change", (event) => {

            loadSelectedGenre(selectorButton.value);
        });
    });

    const showMoreButtons = document.querySelectorAll(".buttonShowMore")

    showMoreButtons.forEach(button => {
        button.addEventListener("click", (event) => {
            if(button.textContent === "Voir plus") {
                button.textContent = "Voir moins"
                showMoreOnTablet(button.id.slice(8))
                showMoreOnPhone(button.id.slice(8))
            } else {
                button.textContent = "Voir plus"
                showLessOnTablet(button.id.slice(8))
                showLessOnPhone(button.id.slice(8))
            }
        })
    })
   
    const buttonCloseModalDetails = document.getElementById("buttonCloseModalDetails")

    buttonCloseModalDetails.addEventListener("click", () => {
        document.getElementById("modalDetails").style.display = "none"
    })

    const cross = document.querySelector(".cross")

    cross.addEventListener("click", (event) =>{
        document.getElementById("modalDetails").style.display = "none"
    })

    document.body.addEventListener("click", (event) => {
        if (event.target.classList.contains("buttonDetails")) {
            document.getElementById("modalDetails").style.display = "block"
            const title = event.target.previousElementSibling.textContent
            const imageUrl = event.target.parentNode.previousElementSibling.src
            loadDetails(title, imageUrl)
        }
    })

    const buttonBestMovie = document.getElementById("buttonBestMovie")

    buttonBestMovie.addEventListener("click", () => {
        document.getElementById("modalDetails").style.display = "block"
        const title = buttonBestMovie.parentNode.querySelector("h2").textContent
        const imageUrl = buttonBestMovie.parentNode.previousElementSibling.src
        loadDetails(title, imageUrl)
    } )

}


load()
listeners()



