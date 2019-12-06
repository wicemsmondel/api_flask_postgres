// $(document).ready(function () {
//   // notre code ici
//   var $loadBalancer = $('Load-balancer'),
//     $name = $('#Name'),
//     $owner = $('#Owner'),
//     $user = $('#User'),
//     $password = $('#Password'),
//     $namespace = $('#Namespace')
//     $champ = $('.champ');
// });
$(document).ready(function () {
  showAll();
  
});

function showAll() {
  $.get('http://localhost:5000/data', function (data) {
    console.log("wwwwwwwwwwwwww")
    data = JSON.parse(data)
    console.log(data[1].Namespace)
    $('#List').empty()
    console.log(data)
    for (var i = 0; i < data.length; i++) {
      $('#List').append("<tr>")
      $('#List').append("<th>" + data[i].Id + "</th>")
      $('#List').append("<th>" + data[i].Name + "</th>")
      $('#List').append("<th>" + data[i].Owner + "</th>")
      $('#List').append("<th>" + data[i].User + "</th>")
      $('#List').append("<th>" + data[i].Password + "</th>")
      $('#List').append("<th>" + data[i].Namespace + "</th>")
      $('#List').append("<th>" + "<button  id='deleterow' iddb=" + data[i].Id + " type='button' " + "onclick='deleteDB(this)'" + "class='btn btn-danger'>Delete</button>" + "</th>")
                    //  "<th>" + "<button  id='deleterow' iddb=" + item.ID + " type='button' " + "onclick='deleteDB(this);' " + "class='btn btn-default'>delete</button>"

      // $('#List').append("<th type='hidden' value='" + data[i].Id + "'></th>")
      // $('#List').append("<th type='hidden' value='" + data[i].Id + "'></th>")      
      $('#List').append("</tr>")
    }
  });
}

// GET
// function showAll() {
//   $.ajax({
//     type: 'GET',
//     url: 'http://127.0.0.1:5000/data',
//     timeout: 3000,
//     success: function (data) {
//       //console.log(data);
//       response = $.parseJSON(data);
//       //$('#records_table').empty()
//       //console.log(response);
//       $.each(response, function (i, item) {
//         var ind = i;
//         //"<input type='hidden' id='sql) '>")
//         //console.log(hidden)
//         var $tr = $("<tr>").append(
//           $("<th>").text(item.Id),
//           $('<th>').text(item.Name),
//           $('<th>').text(item.Owner),
//           $('<th>').text(item.User),
//           $('<th>').text(item.Password),
//           $('<th>').text(item.Namespace),
//           "<th>" + "<button  id='deleterow'  iddb=" + item.ID + " type='button' " + "onclick='deleteDB(this);' " + "class='btn btn-default'>delete</button>"
//         ).appendTo('#records_table');
//         //console.log($tr.wrap('<p>').html());
//         console.log(ind);
//         console.log(i);
//       });
//     },
//     error: function () {
//       alert('La requête n\'a pas abouti');
//     }
//   });
// };


// POST
function createDB() {
  $('#post').click(function () {
    var text = $('#create-database').find('input[name="post-data"]').val();
    $.ajax({
      type: 'POST',
      url: 'http://localhost:5000/data',
      data: text,
      dataType: 'json',
      contentType: 'application/json',
      timeout: 3000,
      success: function (data) {
        alert(data);
      },
    });
    window.location.reload(true);
  });
};


//DELETE
function deleteDB(ctl) {
  console.log($(ctl).attr('iddb'))
  var Id = $(ctl).attr('iddb')
  var durl = "http://localhost:5000/data/" + Id
  console.log(durl)
  $.ajax({
    type: 'DELETE',
    url: durl,
  });
  $(ctl).parents("tr").remove();
};

