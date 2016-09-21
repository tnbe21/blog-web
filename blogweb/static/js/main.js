$(function() {
  $.get('/article_tag/list', function(err, res) {
    if (err) {
      console.log(err);
      return;
    }
    console.log("success: " + JSON.stringify(res));
  });
});
