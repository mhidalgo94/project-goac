let ColorActive = "#3298dc;";
let ColorInactive = "#7a7a7a";
let tileProvider = '//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';


// let iconConfig = L.divIcon({
// 	    className: "fas fa-map-marker-alt",
// 	  	iconSize: [25, 41],
// 	  	iconAnchor: [12, 41],
// 	  	popupAnchor: [1, -34],
// 	  	shadowSize: [41, 41],
// 	  	html: `<i />`
// 	});

/*
	Terminar condicionales que defina el color de marker con bulma y font awesome

*/
function ChangeColorMarkets (estado){
	let colorClass =  estado === 'ACTIVO' ? 'fas fa-map-marker-alt has-text-info' : 'fas fa-map-marker-alt has-text-grey-light';

	let iconConfig = L.divIcon({
	    className: colorClass,
	  	iconSize: [25, 41],
	  	iconAnchor: [12, 41],
	  	popupAnchor: [1, -34],
	  	shadowSize: [41, 41],
	  	html: `<i  /> `,
	  	// draggable:true,
	});

	return iconConfig
}




function showMap(data){
	//{ zoomControl: false }
	let myMap = L.map('map',).setView([21.521757,-79.781167],7);
	myMap.scrollWheelZoom.disable()
	
	L.tileLayer(tileProvider,{
	    maxZoom: 18,
	    attribution: "Mapa estaciones de Cuba",

	}).addTo(myMap);
	var myPopup  = [];
	for(let i=0;i<data.length;i++){
		let {codigo,estacion,altura,estado,latitud,longitud,provincia,tipo} = data[i];

		let iconConfig = ChangeColorMarkets(estado);
		console.log({"icon":iconConfig, "provincia":provincia});
		
		L.marker([latitud, longitud], {draggable:true,title:`${provincia}`,icon:iconConfig,})
		.addTo(myMap);
		// .bindPopup('<h1>Provincia</h1> <p>Esta es la descripcion </p>');

	}
	// let p = document.querySelectorAll("#popup");
	// console.log(p);
	//let cmw = L.marker([21.421, -77.871], {title:"Camaguey"}).addTo(myMap);
}


const GetEstaciones = async ()=> {

$.ajax({
        url: window.location.pathname,
        type: 'POST',
        headers:{
            'X-CSRFToken':csrftoken,
        },
        data: {
            'action': "map_estaciones",
        },
        dataType: 'json',
    }).done(function (data) {
        if (!data.hasOwnProperty('error')) {
            showMap(data)
            return false;
        }
        console.log("Ha ocurrido un error en las estaciones")
    }).fail(function (data) {
    }).always(function (data) {

    });

}


GetEstaciones();


