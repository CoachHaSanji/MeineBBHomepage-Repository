// Event Listener für das Absenden des Formulars hinzufügen
document.getElementById('loginForm').addEventListener('submit', function(event) {
    // Verhindert das automatische Absenden des Formulars und das Neuladen der Seite
    event.preventDefault();

    // Speichern der Benutzer-Eingaben in den Variablen username und password
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Fehlermeldung standardmäßig ausblenden, bevor die Überprüfung beginnt
    document.getElementById('loginError').style.display = 'none';

    // Überprüfen, ob der Benutzername und das Passwort korrekt sind
    if (username === 'spieler1' && password === '123') {
        // Login erfolgreich: Benutzer informieren
        alert('Login erfolgreich!');
        // Weiterleitung zur Seite, auf der der Spieler seine Daten einsehen kann
        window.location.href = 'spieler-daten.html';
    } else {
        // Fehlermeldung anzeigen, wenn Benutzername oder Passwort falsch sind
        document.getElementById('loginError').textContent = 'Falscher Benutzername oder Passwort!';
        document.getElementById('loginError').style.display = 'block';
    }
});
