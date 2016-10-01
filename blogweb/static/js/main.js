$(function() {
  $.get('/current_title_list', function(articles) {
    if (!articles) {
      $('#current').html('');
      return;
    }
    $.each(articles, function(i, article) {
      var articleLink = $('<a>').attr({
        href: '/article/' + article.id
      }).append(article.title);
      var $li = $('<li>').append(articleLink);
      $('#current ul').append($li);
    });
  });

  $.get('/tag/list', function(tags) {
    if (!tags) {
      $('#tag').html('');
      return;
    }
    $.each(tags, function(i, tag) {
      var articleLink = $('<a>').attr({
        href: '/?tag=' + tag.name
      }).append(tag.name + '(' + tag.articleCount + ')');
      var $li = $('<li>').append(articleLink);
      $('#tag ul').append($li);
    });
  });
});
