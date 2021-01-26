
$(window).load(function(){

	const URL = "http://127.0.0.1:8000/api/series_of_photos/start=";

	const button = document.querySelector('.show_more'); // Кнопка
	let photos = document.querySelectorAll('.photo');    // Массив фото

	console.log(photos.length);

	if ( photos.length == 9 ) {

		let count_photo = photos.length;               // Количество фото на странице
		const parent = document.querySelector('main'); // Элемент контейнер для вставки фото

		button.addEventListener( "click" , async function () { // При нажатии на кнопку

			let code = ""; // Код для вставки

			let response = await fetch(URL + count_photo);
			let data = await response.json(); // Получение ответа
			let data_length = data.length;

			if ( data_length != 0 ) 
			{
				data.forEach(function (photoset) {

					code += "\
					<a href=\"/photoset/" + photoset.pk + "/\" class=\"photo\">\
						<img src=" + photoset.cover + " alt=\"\">\
						<div class=\"photo-info\">\
							<p class=\"title\">\"" + photoset.title + "\"</p>\
							<p class=\"info\">" + photoset.city + ", " + photoset.date.split('-')[0] + "\
						</div>\
					</a>";
	
				});

				parent.insertAdjacentHTML("beforeEnd", code);

			} 

			if ( data_length < 9 ) 
			{
				button.classList.remove('watch');
			}

		});

	} else {
		button.classList.remove('watch');
	}
});