$(function() {
  $.get('/tag/list', function(tags) {
    $.each(tags, function(tag) {
      var articleLink = $('<a>').attr({
        href: '/?tag=' + tag
      }).append(tag);
      var $li = $('<li>').append(articleLink);
      $('#tag ul').append($li);
    });
  });
});
