var doc_tag = '<a href="#"></a>';
var li_tag = '<li></li>'

var doc_array;
var current_doc;


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken;

window.onload = function()
{
    var doc_list = [];

    csrftoken = getCookie('csrftoken');

    $.ajax({
        url: 'get_doc_list',
        success: function(data) {
            doc_array = data;
            fill_doc_list( data );
        }
    });

    console.log(doc_list);
}

var doc_request = function ( doc_n )
{
    var doc_url = doc_array[ doc_n ][ 'url' ];

    $.ajax({
        url: 'doc_request',
        method: 'POST',
        data: {'url': doc_url },
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: doc_viewer
    });
}


var doc_viewer = function ( data )
{
    data = JSON.parse(data);
    $( '#doc_viewer' ).empty();
    $( '#doc_viewer' ).append( '<h1>' + data['title'] + '</h1>' );
    $( '#doc_viewer' ).append( data['body'] );
}


/*
 * Prende i dati del server relativi alla lista dei documenti e li inserisce nella pagina
 */
var fill_doc_list = function (data)
{
    $( '#doc_list' ).empty();

    for( var document in data )
    {
        var tag = $( doc_tag );

        tag.html(data[document]['title']);

        list_elem = $( li_tag );
        list_elem.attr('id', document );
        list_elem.append(tag);

        $( '#doc_list' ).append( list_elem );
    }

    $( $( '#doc_list' ).children()[0] ).attr( 'class', 'active' );
    current_doc = 0;
    doc_request( current_doc );

    $( '#doc_list li' ).on( 'click', function() {
        $( '#' + current_doc ).attr('class', '');
        $( this ).attr( 'class', 'active' );
        current_doc = $( this ).attr( 'id' );

        doc_request( current_doc );
    });
}