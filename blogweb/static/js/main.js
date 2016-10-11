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


  $.get('/yearly_map', function(yearlyMap) {
    if (!yearlyMap) {
      $('#archive').html('');
      return;
    }
    $('#archive').append('<ul />');
    $.each(yearlyMap, function(year, monthlyMap) {
      var $li = $('<li />').append('▶' + year).append('<ul />');
      $.each(monthlyMap, function(yearMonth, list) {
        $li.find('ul').append($('<li />').append(yearMonth + '(' + list.length + ')'));
      });
      $('#archive ul').append($li);
    });
    $('#archive ul li').each(function(i, el) {
      $(el).toggle();
      if (i === 0) {
      }
    });
  });

  $.get('/tag/list', function(tags) {
    if (!tags) {
      $('#tag').html('');
      return;
    }
    $.each(tags, function(i, tag) {
      var $articleLink = $('<a>').attr({
        href: '/?tag=' + tag.name
      }).append(tag.name + '(' + tag.articleCount + ')');
      var $li = $('<li>').append($articleLink);
      $('#tag ul').append($li);
    });
  });
});
