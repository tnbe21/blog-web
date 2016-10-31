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
      $('#current > ul').append($li);
    });
  });


  $.get('/archive_list', function(maps) {
    if (!maps) {
      $('#archive').html('');
      return;
    }
    $('#archive').append($('<ul />'));
    $.each(maps, function(year, map) {
      var $yearElem = $('<li />').addClass('archive_year_on').append(year).append($('<ul />'));
      $.each(map, function(month, size) {
        var $monthLink = $('<a />').attr('href', '/?year=' + parseInt(year) + '&month=' + parseInt(month)).append(year + '-' + month + '(' + size + ')');
        var $monthElem = $('<li />').append($monthLink);
        $monthElem.click(function(e) {
          e.stopPropagation();
        });
        $yearElem.find('ul').append($monthElem);
      });
      $('#archive > ul').append($yearElem);
    });
    $('#archive > ul > li').each(function(i, yearElem) {
      if (i !== 0) {
        $(yearElem).removeClass('archive_year_on').addClass('archive_year_off');
        $(yearElem).find('ul').toggle();
      }
      $(yearElem).click(function() {
        $(this).find('ul').toggle(function() {
          if ($(this).is(':visible')) {
            $(yearElem).removeClass('archive_year_off');
            $(yearElem).addClass('archive_year_on');
          } else {
            $(yearElem).removeClass('archive_year_on');
            $(yearElem).addClass('archive_year_off');
          }
        });
      });
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
