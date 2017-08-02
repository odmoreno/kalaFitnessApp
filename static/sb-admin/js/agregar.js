$("#add").on("click", function(){
  $('#rutinas > tbody:last-child').append('<tr><td>'+$("#nombre").val()+'</td><td>'+$("#detalle").val()+'</td><td>'+$("#series").val()+'</td><td>'+$("#repeticiones").val()+'</td><td>'+$("#descanso").val()+'</td><td>'+$("#enlace").val()+'</td></tr>');
});