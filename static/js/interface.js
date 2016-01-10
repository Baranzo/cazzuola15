var doc_tag = '<a href="#"></a>';
var li_tag = '<li></li>'

window.onload = function()
{
    var doc_list = [];

    $.ajax({
        url: 'get_doc_list',
        success: function(data) {
            fill_doc_list( data );
        }
    });

    console.log(doc_list);
}

/*
 * Prende i dati del server relativi alla lista dei documenti e li inserisce nella pagina
 */
var fill_doc_list = function (data)
{
    for( var document in data )
    {
        var tag = $( doc_tag );

        tag.attr('href', '#'+document);
        tag.html(data[document]['title']);

        list_elem = $( li_tag );
        list_elem.append(tag);

        $( '#doc_list' ).append( list_elem );
    }

    $( $( '#doc_list' ).children()[0] ).attr( 'class', 'active' );
}