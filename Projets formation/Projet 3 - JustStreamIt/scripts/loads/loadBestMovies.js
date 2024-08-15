import { fetchData } from '../helpers/fetchData.js'


export function loadBestMovies() {

    const urlBestMovies = "http://localhost:8000/api/v1/titles/?sort_by=-imdb_score"

    fetchData(urlBestMovies).then(dataBestMovies => {
        const urlBestMoviesPage2 = "http://localhost:8000/api/v1/titles/?page=2&sort_by=-imdb_score"

        fetchData(urlBestMoviesPage2).then(dataBestMoviesPage2 => {
            let listeUrlBestMovies = []
            listeUrlBestMovies.push("http://localhost:8000/api/v1/titles/" + dataBestMovies.results[0].id)
            listeUrlBestMovies.push("http://localhost:8000/api/v1/titles/" + dataBestMovies.results[1].id)
            listeUrlBestMovies.push("http://localhost:8000/api/v1/titles/" + dataBestMovies.results[2].id)
            listeUrlBestMovies.push("http://localhost:8000/api/v1/titles/" + dataBestMovies.results[3].id)
            listeUrlBestMovies.push("http://localhost:8000/api/v1/titles/" + dataBestMovies.results[4].id)
            listeUrlBestMovies.push("http://localhost:8000/api/v1/titles/" + dataBestMoviesPage2.results[0].id)
            
            for (let i = 0; i < 6; i++ ) {
                fetchData(listeUrlBestMovies[i]).then(dataBestMovieDetails => {
                    let imgBestMovies = document.getElementById(`imgBestMoviesMovie${i+1}`)
                    imgBestMovies.src = dataBestMovieDetails.image_url

                    let titleBestMovies = document.getElementById(`titleBestMoviesMovie${i+1}`)
                    titleBestMovies.textContent = dataBestMovieDetails.title
                })
            }
        
    })
})
}