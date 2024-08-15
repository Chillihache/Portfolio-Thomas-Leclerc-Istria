import { fetchData } from '../helpers/fetchData.js'

export function loadGenre1() {

    const urlGenres = "http://localhost:8000/api/v1/genres"

    fetchData(urlGenres).then(dataGenres => {
        let titleGenre1 = document.getElementById("h1Genre1")
        titleGenre1.textContent = dataGenres.results[0].name

        const urlGenre1 = `http://localhost:8000/api/v1/titles/?genre=${dataGenres.results[0].name}&sort_by=-imdb_score`

        fetchData(urlGenre1).then(dataGenre1 => { 
            const urlGenre1Page2 = `http://localhost:8000/api/v1/titles/?genre=${dataGenres.results[0].name}&page=2&sort_by=-imdb_score`

            fetchData(urlGenre1Page2).then(dataGenre1Page2 => {
                let listeUrlGenre1 = []
                listeUrlGenre1.push("http://localhost:8000/api/v1/titles/" + dataGenre1.results[0].id)
                listeUrlGenre1.push("http://localhost:8000/api/v1/titles/" + dataGenre1.results[1].id)
                listeUrlGenre1.push("http://localhost:8000/api/v1/titles/" + dataGenre1.results[2].id)
                listeUrlGenre1.push("http://localhost:8000/api/v1/titles/" + dataGenre1.results[3].id)
                listeUrlGenre1.push("http://localhost:8000/api/v1/titles/" + dataGenre1.results[4].id)
                listeUrlGenre1.push("http://localhost:8000/api/v1/titles/" + dataGenre1Page2.results[0].id)

                for (let i = 0; i < 6; i++ ) {
                    fetchData(listeUrlGenre1[i]).then(dataGenre1Details => {
                        let imgGenre1 = document.getElementById(`imgGenre1Movie${i+1}`)
                        imgGenre1.src = dataGenre1Details.image_url
    
                        let titleGenre1 = document.getElementById(`titleGenre1Movie${i+1}`)
                        titleGenre1.textContent = dataGenre1Details.title
                    })
                }
            })
        
        })
    })
}