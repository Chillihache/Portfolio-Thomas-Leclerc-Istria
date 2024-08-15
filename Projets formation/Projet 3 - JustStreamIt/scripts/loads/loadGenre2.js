import { fetchData } from '../helpers/fetchData.js'

export function loadGenre2() {

    const urlGenres = "http://localhost:8000/api/v1/genres"

    fetchData(urlGenres).then(dataGenres => {
        let titleGenre2 = document.getElementById("h1Genre2")
        titleGenre2.textContent = dataGenres.results[2].name

        const urlGenre2 = `http://localhost:8000/api/v1/titles/?genre=${dataGenres.results[2].name}&sort_by=-imdb_score`

        fetchData(urlGenre2).then(dataGenre2 => { 
            const urlGenre2Page2 = `http://localhost:8000/api/v1/titles/?genre=${dataGenres.results[2].name}&page=2&sort_by=-imdb_score`

            fetchData(urlGenre2Page2).then(dataGenre2Page2 => {
                let listeUrlGenre2 = []
                listeUrlGenre2.push("http://localhost:8000/api/v1/titles/" + dataGenre2.results[0].id)
                listeUrlGenre2.push("http://localhost:8000/api/v1/titles/" + dataGenre2.results[1].id)
                listeUrlGenre2.push("http://localhost:8000/api/v1/titles/" + dataGenre2.results[2].id)
                listeUrlGenre2.push("http://localhost:8000/api/v1/titles/" + dataGenre2.results[3].id)
                listeUrlGenre2.push("http://localhost:8000/api/v1/titles/" + dataGenre2.results[4].id)
                listeUrlGenre2.push("http://localhost:8000/api/v1/titles/" + dataGenre2Page2.results[0].id) 
                

                for (let i = 0; i < 6; i++ ) {
                    fetchData(listeUrlGenre2[i]).then(dataGenre2Details => {
                        let imgGenre2 = document.getElementById(`imgGenre2Movie${i+1}`)
                        imgGenre2.src = dataGenre2Details.image_url
    
                        let titleGenre2 = document.getElementById(`titleGenre2Movie${i+1}`)
                        titleGenre2.textContent = dataGenre2Details.title
                    })
                }
            })
        
        })
    })
}