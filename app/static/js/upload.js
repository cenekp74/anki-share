function randomHexString(length) {
    let result = '';
    while (result.length < length) {
        result += Math.random().toString(16).slice(2);
    }
    return result.slice(0, length);
}

let userSecret = localStorage.getItem("user_secret")
if (!userSecret) {
    userSecret = randomHexString(64);
    localStorage.setItem("user_secret", userSecret)
}
document.cookie = `user_secret=${userSecret}; path=/; samesite=lax`

FilePond.setOptions({
    server: {
        process: {
            headers: {
                'X-User-Secret': userSecret
            },
            url: '/upload',
            method: 'POST',
            onload: (response) => {
                return response;
            },
        },
    },
    labelIdle: 'Drag & Drop your apkg file or <span class="filepond--label-action"> Browse </span>',
});

FilePond.create(
    document.querySelector('input'),
    {
        instantUpload: true,
    }
);

document.querySelector(".filepond").addEventListener("FilePond:processfile", (e) => {
    if (e.detail.error) return
    let response = e.detail.file.serverId
    window.location.href = "/deck/"+response
})