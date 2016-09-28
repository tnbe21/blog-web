$(function() {
  $.get('/tag/list', function(res) {
    console.log("success: " + JSON.stringify(res));
  });
});
