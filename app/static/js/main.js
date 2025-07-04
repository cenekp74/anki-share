/** vyuziva se pri skryvani flash alertu po kliknuti na krizek */
function setParentDisplayNone(element) {
    element.parentNode.style.display = 'none';
}

/** vytvori HTML element ze stringu - pouziva fce showFlashAlert */
function createElementFromHTML(htmlString) {
    let div = document.createElement('div');
    div.innerHTML = htmlString.trim();
    return div.firstChild;
}

/** prida na stranku flash alert s obsahem message a tridou alert-$category */
function showFlashAlert(message, category='', timeout=5000) {
    let eleString = `<div class="alert alert-${category}">
            ${message} <i onclick="setParentDisplayNone(this)" class="fa fa-xmark"></i>
        </div>`
    let ele = createElementFromHTML(eleString)
    let content = document.getElementsByClassName('content')[0]
    content.insertBefore(ele, content.firstChild)
    setTimeout(function() { // tahle monstrozita je tu aby po chvili alert zmizel a aby mizel postupne
        ele.style.opacity = '0'
        setTimeout(function() {
            ele.style.display = 'none'
        }, timeout*1/3)
    }, timeout*2/3)
}

/** used by deck.js to shuffle cards */
function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

if (document.querySelector(".share-deck-button")) {
    document.querySelector(".share-deck-button").addEventListener("click", () => {
        if (navigator.share) {
            navigator.share({
                title: `anki-share deck - ${document.querySelector(".deck-info > h1").innerHTML}`,
                url: window.location.href
            })
        }
        else {
            navigator.clipboard.writeText(document.location.href.replace("/browse", ""));
            showFlashAlert("Link copied to clipboard")
        }
    })
}
