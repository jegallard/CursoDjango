//Variable que mantiene el estado visible del carrito
var carritoVisible = false;

//Esperar que todos los elementos de la pagina carguen para ejecutar el script
if(document.readyState="loading"){
	document.addEventListener("DOMContentLoaded",ready);
} else {
	ready();
}

function ready(){
	//Funcionalidad del botón eliminar del carrito
	let botonesEliminarItem = document.getElementsByClassName("btn-eliminar");
	for(let i = 0; i < botonesEliminarItem.length; i++){
		let boton = botonesEliminarItem[i];
		boton.addEventListener("click",eliminarItemCarrito);		
	}

	//Funcionalidad sumar cantidad
	let botonesSumarCantidad = document.getElementsByClassName("sumar-cantidad")[0];
	for(let i = 0; i < botonesSumarCantidad.length; i++){
		let boton = botonesSumarCantidad[i];
		boton.addEventListener("click",sumarCantidad);
	}

	//Funcionalidad restar cantidad
	let botonesRestarCantidad = document.getElementsByClassName("restar-cantidad")[0];
	for(let i = 0; i < botonesRestarCantidad.length; i++){
		let boton = botonesRestarCantidad[i];
		boton.addEventListener("click",restarCantidad);
	}

}

//Borrar item seleccionado
function eliminarItemCarrito(event){
	let botonClikeado = event.target;
	botonClikeado.parentElement.remove();

	//Actualizar el total del carrito cuando se elimina un item
	actualizarTotalCarrito();

	//Ver si hay elementos en el carrito, si no hay elementos se oculta el carrito
	ocultarCarrito()
}

//Actualiza el total del carrito
function actualizarTotalCarrito(){
	//Seleccionar el contenedor del carrito
	let carritoContenedor = document.getElementsByClassName("carrito")[0];
	let carritoItems = document.getElementsByClassName("carrito-item");
	let total = 0;

	//Recorrer cada item de carrito items
	for(let i = 0; i < carritoItems.length; i++){
		let item = carritoItems[i];
		let precioItem = item.getElementsByClassName("carrito-item-precio")[0];
		let precio = parseFloat(precioItem.innerHTML.replace("$","").replace(".","").replace(",","."));
		let cantidadItem = item.getElementsByClassName("carrito-item-cantidad")[0];
		let cantidad = cantidadItem.value;
		
		total = total + (precio * cantidad);
	}
	total = Math.round(total*100)/100;
	document.getElementsByClassName("carrito-precio-total")[0].innerText= total;
}

//oculta el carrito cuando no hay elementos
function ocultarCarrito(){
	let carritoItems = document.getElementsByClassName("carrito-items")[0];
	
	if(carritoItems.childElementCount==0){
		let carrito = document.getElementsByClassName("carrito")[0];
		carrito.style.marginRight = "-100%";
		carrito.style.opacity = "0";
		carritoVisible = false;

		//maximizar el contenedor de los items
		let items = document.getElementsByClassName("contenedor-items")[0];
		items.style.width = "100%";
		
	}	
}

//Aumento de la cantidad de elemento seleccionado
function sumarCantidad(event){

}

function restarCantidad(event){
	
}