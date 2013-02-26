$(document).ready(function (){
	$(".scrollLink").bind('click.smoothscroll', function (evt){
		id = this.hash;
		// $('body').animate({ scrollTop: $(id).offset().top }, 1500, function(){ window.location.hash = id; });
		$.smoothScroll({
			scrollTarget: id,
			afterScroll: function(){ window.location.hash = id; },
			easing: "swing",
			speed: 1750,
		});
		evt.preventDefault();
	});
});

$(window).scroll(function(e){
	// parallax scrolling
	var scrolled = $(window).scrollTop();
	scrollLayer("Background", .1, scrolled);
	scrollLayer("Back", .3, scrolled);
	scrollLayer("Middle", .5, scrolled);
	scrollLayer("Front", .7, scrolled);
	scrollLayer("Fast", 2, scrolled);
});

function scrollLayer(layer, factor, scrolled) {
	$("img" ,"#layer" + layer).each(function (evt){
		newTop = (- scrolled * factor) + "px";
		$(this).css("top", newTop);
	});
}
