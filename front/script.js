// Create a request variable and assign a new XMLHttpRequest object to it.
//var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
//request.open('GET', 'http://0.0.0.0:5000/v1/hello-world', true)

//request.onload = function() {
  // Begin accessing JSON data here
//}

// Send request
//request.send()

$(document).ready(function() {
    showAll();

});

function showAll(){
  $.get('http://0.0.0.0:5000/database', function( data ) {
     //$('#result').html( data );
     console.log("It's OK")
     data = JSON.parse(data)
     console.log(data[0].Namespace)
     $("#liste").empty()
     for(var i= 0; i < data.length; i++){
       $("#liste").append("<tr>")
       $("#liste").append("<td>"+data[i].Name+"</td>")
       $("#liste").append("<td>"+data[i].Owner+"</td>")
       $("#liste").append("<td>"+data[i].Namespace+"</td>")
       $("#liste").append("<td>"+data[i].User+"</td>")
       $("#liste").append("<td>"+data[i].Password+"</td>")
       $("#liste").append("<td type='hidden' value='"+data[i].Id+"'></td>")
       $("#liste").append("<td type='hidden' value='"+data[i].Id+"'></td>")
       $("#liste").append("</tr>")
     }
  });
}

function deleteDataBase(id){
     //$('#result').html( data );
     console.log("deleteeeeeee")
  $.ajax({
                type: 'DELETE',
                url: 'http://0.0.0.0:5000/database/'+id,
                dataType: 'json',
                encode: true
            }).done(function(data) {
                showAll();
            });
  event.preventDefault();
     }

$("#create").submit(function( event ) {
    var donnees=$("#createForm").serialize();
    //console.log(donnees)
    //data = JSON.parse(data)
  $.ajax({  // AJAX SUPPRESSION
                type: 'POST',
                url: 'http://0.0.0.0:5000/database',
                data: donnees,
                dataType: 'json',
                encode: true
            }).done(function(data) {
                console.log(data)
                showAll();
            });
  event.preventDefault();
});

