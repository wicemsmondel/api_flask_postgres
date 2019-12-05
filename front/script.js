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
  $.get('http://0.0.0.0:5000/data', function (data) {
    console.log("wwwwwwwwwwwwww")
    data = JSON.parse(data)
    console.log(data[1].Namespace)
    $("List").empty()
    console.log(data)
    for (var i = 0; i < data.length; i++) {
      $("List").append("<tr>")
      $("List").append("<td>" + data[i].Name + "</td>")
      $("List").append("<td>" + data[i].Owner + "</td>")
      $("List").append("<td>" + data[i].Namespace + "</td>")
      $("List").append("<td>" + data[i].User + "</td>")
      $("List").append("<td>" + data[i].Password + "</td>")
      $("List").append("<td type='hidden' value='" + data[i].Id + "'></td>")
      $("List").append("<td type='hidden' value='" + data[i].Id + "'></td>")
      $("List").append("</tr>")
    }
  });
}
