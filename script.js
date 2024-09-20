document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === 'spieler1' && password === 'passwort123') {
        alert('Login erfolgreich!');
        // Hier kannst du den Spieler zu einer anderen Seite weiterleiten, wo er seine Daten einsehen kann.
        window.location.href = 'spieler-daten.html';
    } else {
        document.getElementById('loginError').textContent = 'Falscher Benutzername oder Passwort!';
        document.getElementById('loginError').style.display = 'block';
    }
});
