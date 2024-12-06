if (performance.navigation.type === 1) { // if reload send signal /reload to server.js file
    fetch('/reload', { method: 'POST' })
        .then(response => response.json())
        .then(data => console.log('reload ', data))
        .catch(error => console.error('error ', error));
}

function feO() {
    fetch('/output') // get output from output file
        .then(response => response.text())
        .then(data => {
            document.getElementById('output').innerText = data;
        })
        .catch(error => {
            document.getElementById('output').innerText = error.message;
        });
}

// every send get output from output file
setInterval(feO, 1000);

// on submit class button being pressed, send in user input
document.getElementById('inF').addEventListener('submit', (event) => {
    event.preventDefault();
    const usI = document.getElementById('usI').value;

    fetch('/update-python', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input: usI })
    })
    .then(response => response.json())
    .then(data => {
        console.log("i have no idea what im doing");
    })
    .catch(error => {
        console.error(error.message);
    });
});
