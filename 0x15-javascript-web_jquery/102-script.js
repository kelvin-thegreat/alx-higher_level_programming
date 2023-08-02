// script that fetches and prints how to say “Hello” 
$(document).ready(function () {
  // API URL
  const url = 'https://www.fourtonfish.com/hellosalut/?';

  // Click event handler for the #btn_translate button
  $('INPUT#btn_translate').click(function () {
    // Get the language code entered by the user
    const languageCode = $('INPUT#language_code').val();

    // Make an AJAX GET request to the API
    $.get(url + $.param({ lang: languageCode }), function (data) {
      // Display the translation in the #hello div
      $('DIV#hello').html(data.hello);
    });
  });
});
