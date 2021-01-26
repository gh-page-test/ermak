// Анимация окна приветствия
$(window).load(function(){
	document.querySelector('.bg-grad').classList.add('active');
	let transTime = 3000;
	let numBgColors = $('.bg-grad').length;
	let bgtrans = setInterval(function(){
		if($('.bg-grad.active').index() == ($('.bg-grad').length-1)){
			$('.bg-grad.active').removeClass('active');
			$('.bg-grad').eq(0).addClass('active');
		}else{
			let curIndex = $('.bg-grad.active').index();
			$('.bg-grad.active').removeClass('active');
			$('.bg-grad').eq(curIndex+1).addClass('active');
		}
	},transTime);
});
 
// Закрытие окна приветствия 
$('#start-btn').on('click', function(){

	$('.bg-wrapper').toggleClass('wrapper-disactive');
	$('.btn-start').toggleClass('wrapper-disactive');

	$('header').toggleClass('watch');
	$('main').toggleClass('watch');
	$('footer').toggleClass('watch');
	$('.up').toggleClass('watch');
	if ( $('.photos').length == 9 ) {
		$('.show_more').toggleClass('watch');
	}
});