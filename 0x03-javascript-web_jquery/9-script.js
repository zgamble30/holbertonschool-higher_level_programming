// Fetches from https://fourtonfish.com/hellosalut/?lang=fr
// and displays the value of hello from that fetch in the HTML’s tag DIV#hello
const fourtonfish = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.getJSON(fourtonfish).done((data) => $('DIV#hello').text(data.hello));
