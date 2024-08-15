import { fetchData } from '../helpers/fetchData.js'


export function loadBestMovie() {

    const urlBestMovies = "http://localhost:8000/api/v1/titles/?sort_by=-imdb_score"

    fetchData(urlBestMovies).then(dataBestMovies => {
        const UrlBestMovieDetails = "http://localhost:8000/api/v1/titles/" + dataBestMovies.results[0].id

        fetchData(UrlBestMovieDetails).then(dataBestMovieDetails =>{
            let imageBestMovie = document.querySelector(".rectangleBestMovie img")
            imageBestMovie.src = dataBestMovieDetails.image_url

            let titleBestMovie = document.querySelector(".elementsBestMovie h2")
            titleBestMovie.textContent = dataBestMovieDetails.title

            let descriptionBestMovie = document.querySelector(".elementsBestMovie p")
            descriptionBestMovie.textContent = dataBestMovieDetails.description
        })
    })
}
