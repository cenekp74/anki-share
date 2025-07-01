function getCurrentCardEle() {
    return window.cards[window.currentCard]
}

function changeCurrentCard(card_index) {
    if (getCurrentCardEle()) {
        getCurrentCardEle().classList.remove("active")
        getCurrentCardEle().classList.remove("flipped")
    }
    window.currentCard = card_index
    card = window.cards[card_index] 
    if (!card) return
    card.classList.add("active")
    updateDeckStatus()
    if (getCurrentCardEle().querySelector(".card-front").querySelector("audio")) {
        getCurrentCardEle().querySelector(".card-front").querySelector("audio").play()
    }
}

function nextCard() {
    if (window.currentCard == window.cards.length-1) {
        changeCurrentCard(0)
        return
    }
    changeCurrentCard(window.currentCard+1)
}

function prevCard() {
    if (window.currentCard == 0) {
        changeCurrentCard(window.cards.length-1)
        return
    }
    changeCurrentCard(window.currentCard-1)
}

function correct() {
    getCurrentCardEle().classList.remove("active")
    getCurrentCardEle().classList.remove("flipped")
    window.cards.splice(window.currentCard, 1)
    if (window.currentCard == window.cards.length) {
        window.currentCard = 0
    }
    changeCurrentCard(window.currentCard)
}

function incorrect() {
    nextCard()
}

function flipCurrentCard() {
    getCurrentCardEle().classList.toggle("flipped")
    if (getCurrentCardEle().classList.contains("flipped")) {
        if (getCurrentCardEle().querySelector(".card-back").querySelector("audio")) {
            getCurrentCardEle().querySelector(".card-back").querySelector("audio").play()
        }
    } else {
        if (getCurrentCardEle().querySelector(".card-front").querySelector("audio")) {
            getCurrentCardEle().querySelector(".card-front").querySelector("audio").play()
        }
    }
}

function updateDeckStatus() {
    document.querySelector(".deck-status").innerHTML = `Learning: ${window.currentCard+1}/${window.cards.length}`
}

document.addEventListener("DOMContentLoaded", () => {
    window.cards = []
    document.querySelectorAll(".card").forEach((cardEle) => {
        cardEle.addEventListener("click", flipCurrentCard)
        window.cards.push(cardEle)
    })
    document.querySelector(".next-button").addEventListener("click", nextCard)
    document.querySelector(".prev-button").addEventListener("click", prevCard)
    document.querySelector(".correct-button").addEventListener("click", correct)
    document.querySelector(".incorrect-button").addEventListener("click", incorrect)
    document.addEventListener("keydown", (e) => {
        switch (e.key) {
            case "ArrowLeft":
                prevCard()
                break
            case "ArrowRight":
                nextCard()
                break
            case "1":
                if (getCurrentCardEle().classList.contains("flipped")) incorrect()
                else flipCurrentCard()
                break
            case "2":
                if (getCurrentCardEle().classList.contains("flipped")) correct()
                else flipCurrentCard()
                break
            case " ":
                flipCurrentCard()
                break
        }
    })
    urlParams = new URLSearchParams(window.location.search);
    firstCard = urlParams.get("card")
    if (firstCard) {
        firstCard = parseInt(firstCard)
        if (!window.cards[firstCard]) {
            firstCard = 0
        }
    } else {
        firstCard = 0
    }
    changeCurrentCard(firstCard)
})