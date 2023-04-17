// Fetches and lists the title for all movies
// by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
const swapiAPI = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.getJSON(swapiAPI).done((data) => {
  $.each(data.results, (_, result) => {
    $('UL#list_movies').append(`<li>${result.title}</li>`);
  });
});
