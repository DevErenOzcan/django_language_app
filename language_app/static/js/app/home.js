document.getElementById("quizButton").addEventListener("click", function() {
    window.location.href = "http://localhost:8080/language_app/quiz/"; // Buraya gitmek istediğiniz URL'yi yazın
});

document.getElementById("addWordButton").addEventListener("click", function() {
    window.location.href = "http://localhost:8080/language_app/add_word/"; // Buraya gitmek istediğiniz URL'yi yazın
});

document.getElementById("settingsButton").addEventListener("click", function() {
    window.location.href = "http://localhost:8080/language_app/settings/"; // Buraya gitmek istediğiniz URL'yi yazın
});

document.getElementById("analiseReportButton").addEventListener("click", function() {
    var csrftoken = getCookie('csrftoken');

    $.ajax({
      type: 'POST',
      url: '/language_app/',
      headers: { "X-CSRFToken": csrftoken }, // CSRF token'ını istek başlığı olarak ekleyin
      success: function(response){
          console.log(response);
      },
      error: function(xhr, status, error) {
        console.error(error); // Hata durumunda konsola yazdır
      }
    });
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Çerez adı csrftoken ise, değerini al
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
