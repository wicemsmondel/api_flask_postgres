
$(document).ready(function () {
  showAll();
  postPutain()
});


////////////////////  GET  ////////////////////  

function showAll() {
  $.get('http://a3e47cd6c1a6611ea9df302af6eaa18b-1254097968.eu-west-1.elb.amazonaws.com/data', function (data) {
    data = JSON.parse(data)
    $('#List').empty()
    console.log(data)
    data.forEach(data => {
      $('#List').append("<tr>")
      $('#List').append("<th>" + "#" + data.Id + "</th>")
      $('#List').append("<td>" + data.Name + "</td>")
      $('#List').append("<td>" + data.Owner + "</td>")
      $('#List').append("<td>" + data.User + "</td>")
      $('#List').append("<td>" + data.Password + "</td>")
      $('#List').append("<td>" + data.Namespace + "</td>")
      $('#List').append("<td>" + "<button  id='deleterow' iddb=" + data.Id + " type='button' " + "onclick='deleteDB(this)'" + "class='btn btn-danger'>Delete</button></td>")
      // $('#List').append("</tr>")
    });  
  });
}


////////////////////  POST  ////////////////////  

function postPutain() {
  $('#post-data').click(function () {
    var formData = {};
    $('#create-database').serializeArray().map(function (x) { formData[x.name] = x.value; });
    console.log(formData)
    $.ajax({
      type: "POST",
      url: "http://a3e47cd6c1a6611ea9df302af6eaa18b-1254097968.eu-west-1.elb.amazonaws.com/data",
      data: JSON.stringify(formData),
      dataType: "json",
      contentType: "application/json"
    });
    setTimeout(function () { location.reload() }, 600);
  });
};


////////////////////  DELETE ////////////////////  

function deleteDB(ctl) {
  console.log($(ctl).attr('iddb'))
  var Id = $(ctl).attr('iddb')
  var durl = "http://a3e47cd6c1a6611ea9df302af6eaa18b-1254097968.eu-west-1.elb.amazonaws.com/data/" + Id
  console.log(durl)
  $.ajax({
    type: 'DELETE',
    url: durl
  });
  $(ctl).parents("tr").remove();
  setTimeout(function () { location.reload() }, 600);
};

