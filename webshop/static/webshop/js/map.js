function init() {
  let map = new ymaps.Map('map', {
    center: [50.537541572976686,36.583728500000014],
    zoom: [16],
  });

  let placemark = new ymaps.Placemark([50.53770567310452,36.583728500000014], {
    iconCaption: 'Карандаш',
    balloonContent: 'Наш магазин',
  }, {
    preset: 'islands#orangeDotIconWithCaption',
  })

  map.controls.remove('geolocationControl');
  map.controls.remove('searchControl');
  map.controls.remove('trafficControl');
  map.controls.remove('typeSelector');
  map.controls.remove('fullscreenControl');
  // map.controls.remove('zoomControl');
  map.controls.remove('rulerControl');
  map.behaviors.disable(['scrollZoom']);

  map.geoObjects.add(placemark);
}

ymaps.ready(init);