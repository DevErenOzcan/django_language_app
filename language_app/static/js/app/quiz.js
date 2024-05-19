document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('quiz-form');
    const answers = {}; // Keep track of selected answers

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Collect form data
        const formData = new FormData(form);
        const answerData = [];

        // Combine selected answers with form data
        Object.keys(answers).forEach(question => {
            formData.append(question, answers[question]);
        });

        // Convert form data to JSON object
        formData.forEach((value, key) => {
            answerData.push({
                question: key,
                answer: value
            });
        });

        // Send answer data to server
        fetch('/language_app/quiz/', {
            method: 'POST',
            body: JSON.stringify({ answer_data: answerData }),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Include CSRF token
            }
        })
        .then(response => response.json())
        .then(data => {
            // Handle response data
            console.log(data);
            // You can update UI based on the response if needed
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Listen for changes in radio button selection
    form.addEventListener('change', function(event) {
        const target = event.target;
        if (target.tagName === 'INPUT' && target.type === 'radio') {
            const question = target.name;
            const answer = target.value;
            answers[question] = answer;
        }
    });
});

// Function to get CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Get CSRF token
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
