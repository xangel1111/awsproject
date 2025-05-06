// js/api.js

const getAuthToken = () => {
    return localStorage.getItem('authToken');
};

const fetchData = async (url) => {
    const token = getAuthToken();
    if (!token) {
        window.location.href = '/login.html'; // Redirigir si no hay token
        return;
    }

    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
        }
    });

    if (response.ok) {
        return await response.json();
    } else {
        alert('Acceso denegado o sesión expirada.');
        window.location.href = '/login.html'; // Redirigir si la sesión expira
    }
};

export { fetchData };
