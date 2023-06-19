document.getElementById("analyze-button").addEventListener("click", function() {
    checkPassword();
});

function checkPassword() {
    var password = document.getElementById("password-input").value;
    var score = 0;
    var lowercase = false;
    var uppercase = false;
    var punctuation = false;
    var number = false;
    var length = false;

    // Check for characters
    for (var i = 0; i < password.length; i++) {
        var character = password[i];
        if (/[a-z]/.test(character)) {
            lowercase = true;
        } else if (/[A-Z]/.test(character)) {
            uppercase = true;
        } else if (/[0-9]/.test(character)) {
            number = true;
        } else if (/[!@#$%^&*(),.?":{}|<>]/.test(character)) {
            punctuation = true;
        }
    }

    // At least 8 characters long
    if (password.length > 8) {
        length = true;
    } else {
        length = false;
    }

    // Score
    if (lowercase && uppercase) {
        score += 10;
    }
    if (lowercase && uppercase && number) {
        score += 10;
    }
    if (punctuation) {
        score += 10;
    }
    if (length) {
        score += 10;
    }

    // Progress bar
    var progress = document.getElementById("progress");
    if (score <= 10) {
        progress.style.width = "25%";
        progress.style.backgroundColor = "red";
    } else if (score <= 20) {
        progress.style.width = "50%";
        progress.style.backgroundColor = "yellow";
    } else if (score <= 30) {
        progress.style.width = "75%";
        progress.style.backgroundColor = "lightgreen";
    } else if (score <= 40) {
        progress.style.width = "100%";
        progress.style.backgroundColor = "green";
    }
}