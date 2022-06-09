

//OBTENER INFO POR MEDIO DE AJAX

var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function(){
    if (xhr.readyState===4 && xhr.status===200) {
        let response = JSON.parse(xhr.responseText);
        //console.log(response);
    
        marker(response)
  git 


        
    }
}

document.addEventListener('DOMContentLoaded', function(){
    xhr.open("GET", '../cgi-bin/infoMapas.py');
    xhr.send();
})


// config map
let config = {
    minZoom: 7,
    maxZoom: 18,
  };
  // magnification with which the map will start
  let zoom = 1;
  // cordinadas de comuna de santiago
  let lat_sant = -33.4500000;
  let lng_sant = -70.6666667;
  
  // calling map
  let map = L.map("map", config).setView([lat_sant, lng_sant], zoom);
  
  // Used to load and display tile layers on the map
  // Most tile servers require attribution, which you can set under `Layer`
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

//'https://www.seekpng.com/png/full/101-1015810_leaflet-marker-rotate-leaflet-marker-icon-png.png',


//[lat_sant, lng_sant]

function marker(info){
  for (let [key, value] of Object.entries(info)) {
    v = [parseFloat(value[1]),parseFloat(value[0])] 
    L.marker(v).addTo(map);
    console.log(value);
  }
}