import { fetchData } from '../helpers/fetchData.js'


export async function loadAllGenres() {
    let urlGenres = "http://localhost:8000/api/v1/genres"
    let genres = []
    let numberPage = 1

    let dataGenres = await fetchData(urlGenres)
    for (let i = 0; i < dataGenres.results.length; i++) {
        genres.push(dataGenres.results[i].name)
    }

    while (dataGenres.next !== null) {
        numberPage++
        urlGenres = `http://localhost:8000/api/v1/genres/?page=${numberPage}`
        dataGenres = await fetchData(urlGenres)
        for (let i = 0; i < dataGenres.results.length; i++) {
            genres.push(dataGenres.results[i].name)
        }
    }
    let selectorButton = document.querySelector(".selectorButton")

    for (let i = 0; i < genres.length; i++) {

        let newOption = document.createElement("option")
        newOption.value = genres[i]
        newOption.text = genres[i]

        selectorButton.appendChild(newOption)
    }
}
