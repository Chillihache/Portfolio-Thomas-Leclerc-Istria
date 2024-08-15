import { fetchData } from '../helpers/fetchData.js'

export async function loadSelectedGenre(genre) {

    const urlSelectedGenre = `http://localhost:8000/api/v1/titles/?genre=${genre}&sort_by=-imdb_score`
    let listeUrlSelectedGenre = []
    let dataSelectedGenre = await fetchData(urlSelectedGenre)
    let selectedGenreBoxes = document.querySelectorAll("#selectedGenreBoxes .box")
    let button = document.getElementById("showMoreSelectedGenre")
    
    button.classList.remove("hideButtonShowMore")
    
    for (let i = 0; i < selectedGenreBoxes.length; i++) {
        selectedGenreBoxes[i].remove()
    }

    for (let i = 0; i < dataSelectedGenre.results.length; i++){

        let urlMovieDetails = "http://localhost:8000/api/v1/titles/" + dataSelectedGenre.results[i].id

        let dataMovieDetails = await fetchData(urlMovieDetails)

        let container = document.getElementById("selectedGenreBoxes")

        let divBox = document.createElement("div")
        divBox.classList.add("box")
        if (i === 4) {
            divBox.classList.add("hideOnTablet")
        }
        if (i > 1){
            divBox.classList.add("hideOnPhone")
        }

        let img = document.createElement("img")
        img.id = `imgSelectedGenreMovie${i+1}`
        img.src = dataMovieDetails.image_url
        img.alt = `img selected category movie ${i+1}`
        img.classList.add("background")

        let divRectangleMovie = document.createElement("div")
        divRectangleMovie.classList.add("rectangleMovie")

        let pTitle = document.createElement("p")
        pTitle.id = `titleSelectedGenreMovie${i+1}`
        pTitle.textContent = dataMovieDetails.title

        let buttonDetails = document.createElement("button")
        buttonDetails.textContent = "Détails"
        buttonDetails.classList.add("buttonDetails")

        divRectangleMovie.appendChild(pTitle);
        divRectangleMovie.appendChild(buttonDetails)

        divBox.appendChild(img)
        divBox.appendChild(divRectangleMovie)

        container.appendChild(divBox)
    }

    if (dataSelectedGenre.next !== null) {
        const urlSelectedGenrePage2 = dataSelectedGenre.next
        let dataSelectedGenrePage2 = await fetchData(urlSelectedGenrePage2)
        let urlMovieDetails = "http://localhost:8000/api/v1/titles/" + dataSelectedGenrePage2.results[0].id
        let dataMovieDetails = await fetchData(urlMovieDetails)

        let container = document.getElementById("selectedGenreBoxes")

        let divBox = document.createElement("div")
        divBox.classList.add("box")
        divBox.classList.add("hideOnTablet")
        divBox.classList.add("hideOnPhone")

        let img = document.createElement("img")
        img.id = `imgSelectedGenreMovie6`
        img.src = dataMovieDetails.image_url
        img.alt = `img selected category movie 6`
        img.classList.add("background")

        let divRectangleMovie = document.createElement("div")
        divRectangleMovie.classList.add("rectangleMovie")

        let pTitle = document.createElement("p")
        pTitle.id = `titleSelectedGenreMovie6`
        pTitle.textContent = dataMovieDetails.title

        let buttonDetails = document.createElement("button")
        buttonDetails.textContent = "Détails"
        buttonDetails.classList.add("buttonDetails")

        divRectangleMovie.appendChild(pTitle);
        divRectangleMovie.appendChild(buttonDetails)

        divBox.appendChild(img)
        divBox.appendChild(divRectangleMovie)

        container.appendChild(divBox)
    }

    if (dataSelectedGenre.results.length < 5) {
        let button = document.getElementById("showMoreSelectedGenre")
        button.classList.add("hideButtonShowMore")
    }
}