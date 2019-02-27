$(document).ready(function() {
	$('.list-title').click(function(event) {
		$(this).siblings('ul').slideToggle(200);
		var tri = $(this).children('.tri');
		if(tri.hasClass('tri-open')){
			tri.removeClass('tri-open').addClass('tri-close');
		}else{
			tri.removeClass('tri-close').addClass('tri-open');
		}
	});
	

	var sidebarList = $('.list-type2');
	var orderList = $('.order-list');
	var address = $('.address'); 
	var purchase = $('.purchase');
	sidebarList.each(function(index, el) {
		$(this).click(function(event) {
			var listIndex = $(this).attr('index');
			// console.log(listIndex);
			$('.panel').eq(listIndex).show().siblings().hide();
			$(this).addClass('active').siblings().removeClass('active');
		});
	});

	$('.m-btn').each(function(index, el) {
		$(this).click(function(event) {
			$(this).addClass('active').siblings().removeClass('active');
		});
	});

	$('.list-title-top').each(function(index, el) {
		$(this).click(function(event) {
			$(this).addClass('active').siblings().removeClass('active');
			var tit = $(this).siblings('.list-title-bottom').children('.list-tit');

			var content = $(this).parent('.center-list-title').siblings('.order-list-content').children('div');
			tit.eq($(this).index()).show().siblings('.list-tit').hide();
			content.eq($(this).index()).show().siblings().hide();
		});
	});

	$('.a-tablist ul li').each(function(index, el) {
		$(this).click(function(event) {
			$('.reset').eq($(this).index()).show().siblings('.reset').hide();
			

		});
	});
	$('.binding').click(function(event) {
		$(this).parents('.panel').hide().siblings('.binding-buyer').show();
	});


	$('#h1').blur(function () {
	    var password=$('#h1');
		var $span= $('#msg');

		$.ajax({
			url:"/games_deal/person_center/",
            type:'POST',
			dataType:'json',
            data:{
                // 'csxfmiddlewaretoken':$('[name="csxfmiddlewaretoken"]').val(),
                'password':password.val(),

            },
            success:function (data) {
                var status=data.status;
                if (status == '900') {
                	$span.css('color','green').html(data.msg);

				}else if (status =='901'){
                	$span.css('color','red').html(data.msg);
				}
                }
        })
    });
	$('#h3').blur(function () {

		var newpwd=$('#h2');
		var newpwd2=$('#h3');
		var $span1= $('#ass');

		$.ajax({
			url:"/games_deal/person_center/",
            type:'POST',
			dataType:'json',
            data:{
                // 'csxfmiddlewaretoken':$('[name="csxfmiddlewaretoken"]').val(),
                'newpwd':newpwd.val(),
				'newpwd2':newpwd2.val()

            },
            success:function (data) {
                var status=data.status;
                if (status== '200') {
                	$span1.css('color','green').html(data.ass);

				}else if (status=='902'){
                	$span1.css('color','red').html(data.ass);
				}
                }
        })
    });
	$('#h5').click(function () {
		var password=$('#h1');
		var newpwd=$('#h2');
		var newpwd2=$('#h3');
		var h0=$('#h0');

		$.ajax({
			url:"/games_deal/person_center/",
            type:'POST',
			dataType:'json',
            data:{
                // 'csxfmiddlewaretoken':$('[name="csxfmiddlewaretoken"]').val(),
                'newpwd':newpwd.val(),
				'newpwd2':newpwd2.val(),
				'password':password.val(),

            },
            success:function (data) {
                var status=data.status;
                if (status== '201') {
                	h0.css('color','green').html(data.sss);

				}else if (status=='903'){
                	h0.css('color','red').html(data.sss);
				}
                }
        })
    })
});