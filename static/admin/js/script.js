// Ejecutar función en el evento click
document.getElementById("btn_open").addEventListener("click", open_close_menu);

// Declaramos variables
var side_menu = document.getElementById("menu_side");
var btn_open = document.getElementById("btn_open");
var body = document.getElementById("body");

// Evento para mostrar y ocultar menú
function open_close_menu() {
  body.classList.toggle("body_move");
  side_menu.classList.toggle("menu__side_move");
}

// Si el ancho de la página es menor a 760px, ocultará el menú al recargar la página
if (window.innerWidth < 760) {
  body.classList.add("body_move");
  side_menu.classList.add("menu__side_move");
}

// Haciendo el menú responsive (adaptable)
window.addEventListener("resize", function() {
  if (window.innerWidth > 760) {
    body.classList.remove("body_move");
    side_menu.classList.remove("menu__side_move");
  }

  if (window.innerWidth < 760) {
    body.classList.add("body_move");
    side_menu.classList.add("menu__side_move");
  }
});


// Obtén una referencia al botón "Descargar reporte"
var descargarBoton = document.querySelector('.btn.btn-primary');

// Agrega un evento de clic al botón
descargarBoton.addEventListener('click', function() {
  // Obtiene el contenido HTML del elemento "content"
  var contenidoHTML = document.getElementById('content').innerHTML;

  // Crea un objeto Blob con el contenido HTML
  var blob = new Blob([contenidoHTML], { type: 'text/html' });

  // Crea una URL para el Blob
  var url = URL.createObjectURL(blob);

  // Crea un enlace para descargar el archivo
  var enlaceDescarga = document.createElement('a');
  enlaceDescarga.href = url;
  enlaceDescarga.download = 'reporte.html';
  enlaceDescarga.style.display = 'none';

  // Agrega el enlace al documento
  document.body.appendChild(enlaceDescarga);

  // Simula un clic en el enlace de descarga
  enlaceDescarga.click();

  // Remueve el enlace del documento
  document.body.removeChild(enlaceDescarga);

  // Libera el objeto Blob
  URL.revokeObjectURL(url);
});