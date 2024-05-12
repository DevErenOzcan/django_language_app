$(document).ready(function() {
  // Login butonuna tıklanınca
  $('button[type="button"]').click(function() {
    // CSRF token'ini al
    var csrftoken = getCookie('csrftoken');

    // Form verilerini al
    var username = $('#username').val();
    var password = $('#password').val();

    // Ajax isteğini yap
    $.ajax({
      type: 'POST',
      url: '/login/',
      headers: { "X-CSRFToken": csrftoken }, // CSRF token'ini istek başlığı olarak ekleyin
      data: {
        'username': username,
        'password': password
      },
      success: function(response, status, xhr){
        // Başarılı yanıt kontrolü
        if (xhr.getResponseHeader('content-type').indexOf('text/html') !== -1) {
          // Yönlendirme yapıldıysa sayfayı yeniden yükle
          window.location.replace('/language_app/');
        } else {
          console.log(response); // Başarılı yanıtı konsola yazdır
        }

      },
      error: function(xhr, status, error) {
        console.error(error); // Hata durumunda konsola yazdır
      }
    });
  });
});

// CSRF token'ini çerezden alma fonksiyonu
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
