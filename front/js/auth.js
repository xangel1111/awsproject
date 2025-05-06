// js/auth.js

document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://ec2-18-188-97-25.us-east-2.compute.amazonaws.com:8000/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('authToken', data.token);  // Guardar el JWT
            window.location.href = '/clients.html'; // Redirigir a la página de clientes
        } else {
            alert('Credenciales incorrectas');
        }
    } catch (error) {
        console.error('Error de red', error);
    }
});
