function getCurrentCardEle() {
    return document.getElementById(`card-${window.currentCard}`)
}

function changeCurrentCard(card_id) {
    prevCard = getCurrentCardEle()
    if (prevCard) {
        prevCard.classList.remove("active")
        prevCard.classList.remove("flipped")
    }
    window.currentCard = card_id
    card = document.getElementById(`card-${card_id}`)
    if (!card) return
    card.classList.add("active")
}

function nextCard() {
    if (window.currentCard == document.getElementsByClassName("card").length) return
    changeCurrentCard(window.currentCard+1)
}

function prevCard() {
    if (window.currentCard == 1) return
    changeCurrentCard(window.currentCard-1)
}

function flipCurrentCard() {
    getCurrentCardEle().classList.toggle("flipped")
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".card").forEach((cardEle) => {
        cardEle.addEventListener("click", flipCurrentCard)
    })
    document.querySelector(".next-button").addEventListener("click", nextCard)
    document.querySelector(".prev-button").addEventListener("click", prevCard)
    changeCurrentCard(1)
})