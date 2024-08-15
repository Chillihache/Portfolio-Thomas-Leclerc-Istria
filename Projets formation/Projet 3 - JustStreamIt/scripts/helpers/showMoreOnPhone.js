export function showMoreOnPhone(categoryBoxId) {
    for (let i = 3; i < 7; i++) {
        let box = document.getElementById("img" + categoryBoxId + `Movie${i}`).parentNode
        box.classList.remove("hideOnPhone")
    }
    let categoryBox = document.getElementById("img" + categoryBoxId + "Movie1").parentNode.parentNode
    categoryBox.classList.remove("categoryBox")
    categoryBox.classList.add("categoryBoxShowMore")   
}

export function showLessOnPhone(categoryBoxId) {
    for (let i = 3; i < 7; i++) {
        let box = document.getElementById("img" + categoryBoxId + `Movie${i}`).parentNode
        box.classList.add("hideOnPhone")
    }
    let categoryBox = document.getElementById("img" + categoryBoxId + "Movie1").parentNode.parentNode
    categoryBox.classList.add("categoryBox")
    categoryBox.classList.remove("categoryBoxShowMore")  
}