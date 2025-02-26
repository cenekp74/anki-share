if (document.querySelector(".share-deck-button")) {
    document.querySelector(".share-deck-button").addEventListener("click", () => {
        if (navigator.share) {
            navigator.share({
                title: `anki-share deck - ${document.querySelector(".deck-info > h1").innerHTML}`,
                url: window.location.href
            })
        }
    })
}
