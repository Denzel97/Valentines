// Display the modal
document.getElementById('modal-overlay').style.display = 'block';
document.getElementById('modal').style.display = 'block';

// Function to close the modal and show the appropriate message
function closeModal(response) {
    document.getElementById('modal-overlay').style.animation = 'fadeOutOverlay 0.5s ease-out';
    document.getElementById('modal').style.animation = 'fadeOutModal 0.5s ease-out';
    setTimeout(() => {
        document.getElementById('modal-overlay').style.display = 'none';
        document.getElementById('modal').style.display = 'none';

        // Show the alert box
        document.getElementById('alert-overlay').style.display = 'block';
        document.getElementById('alert-box').style.display = 'block';

        // Set the alert message based on the response
        const alertMessage = response.toLowerCase() === 'yes' ?
            "Yay! Happy Valentine's Day, Babyy! I LOVE U Im so Happy ❤️🌹" :


            document.getElementById('alert-message').innerHTML = alertMessage;

        // Show thanks message if response is 'yes'
        if (response.toLowerCase() === 'yes') {
            document.getElementById('thanks-message').innerHTML = "Thanks for accepting to be my Valentine Babyy! I'm glad You Said YES . I cant wait to see you soon 💕 I LOVE U";
        }
    }, 500);
}

// Function to close the alert box
function closeAlert() {
    document.getElementById('alert-overlay').style.animation = 'fadeOutOverlay 0.5s ease-out';
    document.getElementById('alert-box').style.animation = 'fadeOutAlert 0.5s ease-out';
    setTimeout(() => {
        document.getElementById('alert-overlay').style.display = 'none';
        document.getElementById('alert-box').style.display = 'none';
    }, 500);
}

// Function to show a sad message when user clicks "No"
function showSadMessage() {
    document.getElementById('modal-overlay').style.animation = 'fadeOutOverlay 0.5s ease-out';
    document.getElementById('modal').style.animation = 'fadeOutModal 0.5s ease-out';
    setTimeout(() => {
        document.getElementById('modal-overlay').style.display = 'none';
        document.getElementById('modal').style.display = 'none';

        // Show the sad message
        document.getElementById('alert-overlay').style.display = 'block';
        document.getElementById('alert-box').style.display = 'block';

        // Set the sad message
        const sadMessage = "Oh, that's okay. 😢 If you change your mind, I'll be here. Have a wonderful day! 💔";

        document.getElementById('alert-message').innerHTML = sadMessage;
    }, 500);
}