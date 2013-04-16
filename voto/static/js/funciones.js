$(document).on("ready",inicio);
function inicio () {
	// aqui va el codigo para manipular el DOM
	alert("pruebas");
}

function callback(data){
	popup_show(data.mensaje);
}
function popup_show(data){
	var pago = $('#pago');
	var overlay = pago.find(".overlay");
	var panel = pago.find(".panel");

	pago.addClass("show");
	overlay.addClass("fadeIn");
	panel.addClass("bounceInDown");
	$("#can_img").attr('src', "/static/img/"+data+".jpg");
}