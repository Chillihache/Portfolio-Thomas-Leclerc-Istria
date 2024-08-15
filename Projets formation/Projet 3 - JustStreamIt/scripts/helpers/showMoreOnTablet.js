export function showMoreOnTablet(categoryBoxId) {
    for (let i = 5; i < 7; i++) {
        let box = document.getElementById("img" + categoryBoxId + `Movie${i}`).parentNode
        box.classList.remove("hideOnTablet")
    }
    let categoryBox = document.getElementById("img" + categoryBoxId + "Movie1").parentNode.parentNode
    categoryBox.classList.remove("categoryBox")
    categoryBox.classList.add("categoryBoxShowMore")   
}

export function showLessOnTablet(categoryBoxId) {
    for (let i = 5; i < 7; i++) {
        let box = document.getElementById("img" + categoryBoxId + `Movie${i}`).parentNode
        box.classList.add("hideOnTablet")
    }
    let categoryBox = document.getElementById("img" + categoryBoxId + "Movie1").parentNode.parentNode
    categoryBox.classList.add("categoryBox")
    categoryBox.classList.remove("categoryBoxShowMore")  
}