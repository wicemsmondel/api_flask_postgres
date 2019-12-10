
$(document).ready(function () {
  showAll();
  postPutain()
});


////////////////////  GET   ////////////////////  

function showAll() {
  $.get('http://localhost:5000/data', function (data) {
    data = JSON.parse(data)
    $('#List').empty()
    console.log(data)
    for (var i = 0; i < data.length; i++) {
      $('#List').append("<tr>")
      $('#List').append("<th>" + "#" + data[i].Id + "</th>")
      $('#List').append("<td>" + data[i].Name + "</td>")
      $('#List').append("<td>" + data[i].Owner + "</td>")
      $('#List').append("<td>" + data[i].User + "</td>")
      $('#List').append("<td>" + data[i].Password + "</td>")
      $('#List').append("<td>" + data[i].Namespace + "</td>")
      $('#List').append("<td>" + "<button  id='deleterow' iddb=" + data[i].Id + " type='button' " + "onclick='deleteDB(this)'" + "class='btn btn-danger'>Delete</button></td></tr>")
      $('#List').append("</tr>")
    }
  });
}


////////////////////  POST   ////////////////////  

function postPutain() {
  $('#post-data').click(function () {
    var formData = {};
    $('#create-database').serializeArray().map(function (x) { formData[x.name] = x.value; });
    console.log(formData)
    $.ajax({
      type: "POST",
      url: "http://localhost:5000/data",
      data: JSON.stringify(formData),
      dataType: "json",
      contentType: "application/json"
    });
    // setTimeout(function () { location.reload() }, 600);
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
    url: durl
  });
  $(ctl).parents("tr").remove();
  setTimeout(function () { location.reload() }, 600);
};

