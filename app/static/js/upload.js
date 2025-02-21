FilePond.setOptions({
    server: {
        process: {
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
    
})