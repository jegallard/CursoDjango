
//Variable que mantiene el estado visible del carrito
var carritoVisible = false;
/*
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
	let botonesSumarCantidad = document.getElementsByClassName("sumar-cantidad");
	for(let i = 0; i < botonesSumarCantidad.length; i++){
		let boton = botonesSumarCantidad[i];
		boton.addEventListener("click",sumarCantidad);
	}

	//Funcionalidad restar cantidad
	let botonesRestarCantidad = document.getElementsByClassName("restar-cantidad");
	for(let i = 0; i < botonesRestarCantidad.length; i++){
		let boton = botonesRestarCantidad[i];
		boton.addEventListener("click",restarCantidad);
	}

	//funcionalidad para agregar al carrito
	let botonesAgregarCarrito = document.getElementsByClassName("boton-item");
	for(let i = 0; i < botonesAgregarCarrito.length; i++){
		let boton = botonesAgregarCarrito[i];
		boton.addEventListener("click",agregarCarritoClick);
	}

	//Funcionalidad para pagar
	document.getElementsByClassName("btn-pagar")[0].addEventListener("click",pagarClick);
}

//Borrar item seleccionado
function eliminarItemCarrito(event){
	let botonClikeado = event.target;
	botonClikeado.parentElement.parentElement.remove();

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
*/
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

//Hacer visible el carrito
function hacerVisibleCarrito(){
	carritoVisible = true;
	let carrito = document.getElementsByClassName("carrito")[0];
	carrito.style.marginRight = "0";
	carrito.style.opacity = "1";
	let items = document.getElementsByClassName("contenedor-items")[0];
	items.style.width = "60%";	
}

//Aumento de la cantidad de elemento seleccionado
function sumarCantidad(event){
	let botonClikeado = event.target;
	let selector = botonClikeado.parentElement;
	let cantidadActual = selector.getElementsByClassName("carrito-item-cantidad")[0].value;
	cantidadActual++;
	selector.getElementsByClassName("carrito-item-cantidad")[0].value = cantidadActual;
	//Actualizar el total
	actualizarTotalCarrito();
}

function restarCantidad(event){
	let botonClikeado = event.target;
	let selector = botonClikeado.parentElement;
	let cantidadActual = selector.getElementsByClassName("carrito-item-cantidad")[0].value;
	cantidadActual--;
	//controlar que catidad nunca sea menor a 1
	if(cantidadActual>=1){
		selector.getElementsByClassName("carrito-item-cantidad")[0].value = cantidadActual;
		//Actualizar el total
		actualizarTotalCarrito();
	}	
}

//Toma los datos del elemento
function agregarCarritoClick(event){
	let botonClikeado = event.target;
	let item = botonClikeado.parentElement;
	let titulo = item.getElementsByClassName("titulo-item")[0].innerHTML;
	let precio = item.getElementsByClassName("precio-item")[0].innerHTML;
	let imagenSrc = item.getElementsByClassName("img-item")[0].src;
	
	//Agregar el elemento al carrito
	agregarItemCarrito(titulo, precio, imagenSrc);

	//Hacer visible el carrito
	hacerVisibleCarrito();
}

function agregarItemCarrito(titulo, precio, imagenSrc){
	let item = document.createElement("div");
	item.classList.add = "item";
	let itemCarrito = document.getElementsByClassName("carrito-items")[0];
	
	//Controlar que el item no se encuentre en el carrito
	let nombresItemsCarrito = itemCarrito.getElementsByClassName("carrito-item-titulo");
	for(let i = 0; i < nombresItemsCarrito.length; i++){
		if(nombresItemsCarrito[i].innerHTML==titulo){
			alert("El producto seleccionado ya se encuentra en el carrito");
			return;
		} 
	}
	let itemCarritoContenido = `
	<div class="carrito-item">
		<img src="${imagenSrc}" alt="" width="80px">
		<div class="carrito-item-detalle">
			<span class="carrito-item-titulo">${titulo}</span>
			<div class="selector-cantidad">
				<i class="fa-solid fa-minus restar-cantidad"></i>
				<input type="text" value="1" class="carrito-item-cantidad" disabled>
				<i class="fa-solid fa-plus sumar-cantidad"></i>
			</div>
			<span class="carrito-item-precio">${precio}</span>
		</div>
		<span class="btn-eliminar"><i class="fa-solid fa-trash"></i></span>
	</div>	
	`
	item.innerHTML = itemCarritoContenido;
	itemCarrito.append(item);
	item.getElementsByClassName("btn-eliminar")[0].addEventListener("click",eliminarItemCarrito);
	item.getElementsByClassName("sumar-cantidad")[0].addEventListener("click",sumarCantidad);
	item.getElementsByClassName("restar-cantidad")[0].addEventListener("click",restarCantidad);

	actualizarTotalCarrito();
}

function pagarClick(){
	alert("Gracias por su compra");
	let carritoItems = document.getElementsByClassName("carrito-items")[0];
	while(carritoItems.hasChildNodes()){
		carritoItems.removeChild(carritoItems.firstChild)
	}
	actualizarTotalCarrito();

	//ocultar el carrito
	ocultarCarrito()
}

