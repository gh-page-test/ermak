// Анимация меню
$('.btn-span').on('click', function(){
	if ($(window).width() > 750) {
	    $('.open').toggleClass('menu-disactive');
	    $('.close').toggleClass('close-active');
	    $('.link-nav').toggleClass('link-nav-active');
	} else {
		$('nav').toggleClass('link-nav-active');
	}
});

// Якорное меню
$(document).ready(function(){ 

		$('.link-page').on("click", function (event) {
		//отменяем стандартную обработку нажатия по ссылке
		event.preventDefault();

		if ($(window).width() <= 750) { $('nav').removeClass('link-nav-active'); }
		//забираем идентификатор бока с атрибута href
		var id  = $(this).attr('href'),
		//узнаем высоту от начала страницы до блока на который ссылается якорь
		top = $(id).offset().top;		
		//анимируем переход на расстояние - top за 1500 мс
		$('body,html').animate({scrollTop: top}, 500);
	});
});


