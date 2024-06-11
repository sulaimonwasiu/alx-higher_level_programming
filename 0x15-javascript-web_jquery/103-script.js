$(document).ready(function() {
  $('#btn_translate').click(function() {
    fetchHello();
  });

  $('#language_code').keypress(function(event) {
    if (event.which == 13) {
      fetchHello();
    }
  });
});

function fetchHello() {
  var languageCode = $('#language_code').val();
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode,
    type: 'GET',
    success: function(data) {
      $('#hello').text(data.hello);
    },
    error: function() {
      $('#hello').text('Error fetching translation');
    }
  });
}
