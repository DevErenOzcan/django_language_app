document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Formun normal submit işlemini engelliyoruz

        var email = document.getElementById('email').value;
        var password = document.getElementById('password').value;

        if (!email || !password) {
            alert('Email and password are required!');
            return;
        }

        var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/login/', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.setRequestHeader('X-CSRFToken', csrfToken); // CSRF tokenini header olarak gönderiyoruz
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    // Sunucudan gelen yanıtı işleyebilirsiniz
                    console.log(response);
                } else {
                    console.error('Request failed:', xhr.status);
                }
            }
        };
        xhr.send(JSON.stringify({ email: email, password: password }));
    });
});