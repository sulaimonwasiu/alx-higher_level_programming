// Fetches and replaces the name of the API data then replaces the name
// of the character in the DIV#character tag text

let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.getJSON(url)
  .done(function (data) {
    console.log("I am here");
    $('div#character').text(data.name);
  });
