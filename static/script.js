document.getElementById('conversion-form').addEventListener('submit', function(e) {
    e.preventDefault();  // Evita que el formulario se envíe de manera normal

    const formData = new FormData(this);
    const params = new URLSearchParams(formData);

    fetch('/convert', {
        method: 'POST',
        body: params
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').innerText = data.error;
        } else {
            document.getElementById('result').innerText = `Resultado: ${data.result}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error en la conversión.';
    });
});
