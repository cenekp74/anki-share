document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".card").forEach((cardEle) => {
        cardEle.addEventListener("click", () => {
            cardIndex = cardEle.id.split("-")[1]
            document.location.href = document.location.href.replace("/browse", `?card=${cardIndex}`)
        })
    })
})