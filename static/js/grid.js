// Оформление плитки  
var wdth = document.body.clientWidth; // Ширина экрана

window.addEventListener("load",function() { 
	var photo_array = document.querySelectorAll('.photo');  // Список фотографий для плитки
	formatting_photos(photo_array);
});

function formatting_photos ( photo_array ) 
{
	let length_c = photo_array.length; // Длина массива фотографий
	let position = 'r';                // Позиция изображения ( r - справа, l - слева )
 	let pos = 0

	Array.from(photo_array).forEach(function(item, i, c) {

		if ( (item.offsetWidth < item.offsetHeight) || (item.offsetWidth == item.offsetHeight) ) { 
		// Если оринтация вертикальная или квадратная

			if (length_c != i+1) { // Если элемент не последний

				var second_item = c[i+1]; // Взять следующий элемент массива

				// Соотношение сторон для первого и второго фото
				var item_k = item.offsetWidth/item.offsetHeight; 
				var second_item_k = second_item.offsetWidth/second_item.offsetHeight; 

				var summ_k = item_k + second_item_k; // Сумма соотношений

				// Коофициэнты для расчета ширины для первого и второго фото
				var k1 = (item_k * 100)/summ_k; 
				var k2 = (second_item_k * 100)/summ_k;

				// Подсчет ширины для первого и второго фото
				var w1 = (wdth-20) * (k1/100);
				var w2 = (wdth-20) * (k2/100);

				// Присваивание размеров 
				item.style.width = w1 + "px";
				second_item.style.width = w2 + "px";

				if (position == 'r'){ // Если фото нужно расположить справа 

					item.parentNode.style.order = pos + 1; // Горизонтальное фото справа
					second_item.parentNode.style.order = pos; // Вертикальное фото слева
					pos = pos+1;

					position = 'l'; // Запоминаем, что следущее фото будет расспологаться слева

				} else { // Если фото нужно рассположить слева

					item.parentNode.style.order = pos; // Вертикальное фото слева
					second_item.parentNode.style.order = pos + 1; // Горизонтальное фото справа
					pos = pos+1;

					position = 'r'; // Запоминаем, что следущее фото будет расспологаться справа
					
				}

				// Удаление следующего (видоизмененного) элемента
				a=i+1;
				c.splice(a, 1);

			} else {
				item.style.width = (wdth-10) + "px"; // Оставляем место для рамок вокруг фото
				item.parentNode.style.order = pos; 
			}

		} else { // Если фото горизонтальной ориентации

			item.style.width = (wdth-10) + "px"; // Оставляем место для рамок вокруг фото
			item.parentNode.style.order = pos; 
			pos = pos+1;
		}
	});

	return photo_array;
}