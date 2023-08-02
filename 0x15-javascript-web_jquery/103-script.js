$(document).ready(function () {
  // Click event handler for the #btn_translate button
  $('INPUT#btn_translate').click(translate);

  // Keypress event handler for the #language_code input field
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        // Enter key is pressed, fetch the translation
        translate();
      }
    });
  });
});

function translate() {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    // Display the translation in the #hello div
    $('DIV#hello').html(data.hello);
  });
}
