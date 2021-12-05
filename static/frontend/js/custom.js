$(document).ready(function() {
    "use strict";
    /*
      ============================================================
           Page Loader Javascript
      ============================================================
    */
    $(window).load(function() {
        $("body").imagesLoaded(function() {
            $(".loader-cont").fadeOut();
            $("#loader-overflow").delay(200).fadeOut(700);
        });
    });
    /*
      ============================================================
           Main Banner Javascript
      ============================================================
    */
    if ($('.slider').length) {
        $('.slider').on('init', function(e, slick) {
            var $firstAnimatingElements = $('.slick-slide:first-child').find('[data-animation]');
            doAnimations($firstAnimatingElements);
        });
        $('.slider').on('beforeChange', function(e, slick, currentSlide, nextSlide) {
            var $animatingElements = $('.slick-slide[data-slick-index="' + nextSlide + '"]').find('[data-animation]');
            doAnimations($animatingElements);
        });
        $('.slider').slick({
            autoplay: true,
            autoplaySpeed: 5000,
            dots: false,
            fade: true
        });
    }
    /*
      ============================================================
           popup Javascript
      ============================================================
    */
    if ($('.popup-gallery').length) {
        $('.popup-gallery').magnificPopup({
            delegate: 'a',
            type: 'image',
            tLoading: 'Loading image #%curr%...',
            mainClass: 'mfp-3d-unfold',
            removalDelay: 500, //delay removal by X to allow out-animation
            callbacks: {
                beforeOpen: function() {
                    // just a hack that adds mfp-anim class to markup 
                    this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
                    // this.st.mainClass = this.st.el.attr('data-effect');
                }
            },
            gallery: {
                enabled: true,
                navigateByImgClick: true,
                preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
            },
            image: {
                tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
                /*titleSrc: function(item) {
                  return item.el.attr('title') + '<small>by Marsel Van Oosten</small>';
                }*/
            }
        });
    }
    if ($('.lightbox').length) {
        $('.lightbox').magnificPopup({
           // delegate: 'a',
            type: 'image',
            mainClass: 'mfp-3d-unfold',
            removalDelay: 500, //delay removal by X to allow out-animation
            callbacks: {
            beforeOpen: function() {
              // just a hack that adds mfp-anim class to markup 
               this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
              // this.st.mainClass = this.st.el.attr('data-effect');
            }
            },
            closeOnContentClick: true,
            midClick: true // allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source.
        });
    }
    if ($('.popup-youtube, .popup-vimeo, .popup-gmaps').length) {
        $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
            //disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        });
    }
    /*
      ============================================================
           Masonry Gallery Javascript
      ============================================================
    */
    if ($('.masonry').length) {
        $(".masonry").imagesLoaded(function() {
            $(".masonry").masonry();
        });
    }
    if ($('.items-grid').length) {
        var fselector = 0,
            itemsGrid = $(".items-grid");
        (function($) {
            "use strict";
            var isotopeMode;
            if (itemsGrid.hasClass("masonry")) {
                isotopeMode = "masonry";
            } else {
                isotopeMode = "fitRows"
            }
            itemsGrid.imagesLoaded(function() {
                itemsGrid.isotope({
                    itemSelector: '.mix',
                    layoutMode: isotopeMode,
                    filter: fselector
                });
            });
            $(".port-filter").on('click', '.filter', function() {
                $(".filter").removeClass("active");
                $(this).addClass("active");
                fselector = $(this).attr('data-filter');
                itemsGrid.isotope({
                    itemSelector: '.mix',
                    layoutMode: isotopeMode,
                    filter: fselector
                });
                return false;
            });
        })(jQuery);
    }
    if ($('#items-grid2').length) {
        var fselector = 0,
            itemsGrid = $("#items-grid2");
        (function($) {
            "use strict";
            var isotopeMode;
            if (itemsGrid.hasClass("masonry")) {
                isotopeMode = "masonry";
            } else {
                isotopeMode = "fitRows"
            }
            itemsGrid.imagesLoaded(function() {
                itemsGrid.isotope({
                    itemSelector: '.mix',
                    layoutMode: isotopeMode,
                    percentPosition: true,
                    filter: fselector
                });
            });
            $(".port-filter").on('click', '.filter', function() {
                $(".filter").removeClass("active");
                $(this).addClass("active");
                fselector = $(this).attr('data-filter');
                itemsGrid.isotope({
                    itemSelector: '.mix',
                    layoutMode: isotopeMode,
                    filter: fselector
                });
                return false;
            });
        })(jQuery);
    }
    if ($('js-height-fullscr').length) {
        $(".js-height-fullscr").height($(window).height());
    }
    /*
      ============================================================
           Count Down Javascript
      ============================================================
    */
    if ($('.countdown').length) {
        $('.countdown').downCount({
            date: '8/8/2018 12:00:00',
            offset: +1
        });
    }
    /*
      ============================================================
           Counter Javascript
      ============================================================
    */
    if ($('.counter').length) {
        $('.counter').counterUp({
            delay: 10,
            time: 1000
        });
    }
    /*
      ============================================================
           Testimonial Slider Javascript
      ============================================================
    */
    if ($('.travel-testimonial-slider').length) {
        $('.travel-testimonial-slider').slick({
            slidesToShow: 2,
            dots: false,
            autoplay: true,
            centerMode: false,
            responsive: [{
                breakpoint: 992,
                settings: {
                    arrows: true,
                    slidesToShow: 2
                }
            }, {
                breakpoint: 768,
                settings: {
                    arrows: true,
                    slidesToShow: 1
                }
            }, {
                breakpoint: 481,
                settings: {
                    arrows: true,
                    slidesToShow: 1
                }
            }]
        });
    }
    /*
      ============================================================
          Hotel Testimonial Slider Javascript
      ============================================================
    */
    if ($('.hotel-testimonial').length) {
        $('.hotel-testimonial').slick({
            slidesToShow: 2,
            dots: false,
            autoplay: true,
            centerMode: false,
            responsive: [{
                breakpoint: 992,
                settings: {
                    arrows: true,
                    slidesToShow: 2
                }
            }, {
                breakpoint: 768,
                settings: {
                    arrows: true,
                    slidesToShow: 1
                }
            }, {
                breakpoint: 481,
                settings: {
                    arrows: true,
                    slidesToShow: 1
                }
            }]
        });
    }
    /*
      ============================================================
           Room Slider Javascript
      ============================================================
    */
    if ($('.chr-roomslider').length) {
        $('.chr-roomslider').slick({
            slidesToShow: 3,
            dots: false,
            autoplay: true,
            centerMode: true,
            arrows: true,
            responsive: [{
                breakpoint: 992,
                settings: {
                    arrows: true,
                    slidesToShow: 2
                }
            }, {
                breakpoint: 768,
                settings: {
                    arrows: true,
                    slidesToShow: 1
                }
            }, {
                breakpoint: 481,
                settings: {
                    arrows: true,
                    slidesToShow: 1
                }
            }]
        });
    }
    /*
      ============================================================
           Staff Slider Javascript
      ============================================================
    */
    if ($('.chr-staff-slider').length) {
        $('.chr-staff-slider').slick({
            slidesToShow: 4,
            dots: true,
            autoplay: true,
            centerMode: false,
            arrows: false,
            responsive: [{
                breakpoint: 992,
                settings: {
                    arrows: true,
                    slidesToShow: 3
                }
            }, {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    slidesToShow: 1
                }
            }, {
                breakpoint: 481,
                settings: {
                    arrows: false,
                    slidesToShow: 1
                }
            }]
        });
    }
    /*
      ============================================================
           Special Room Slider Javascript
      ============================================================
    */
    if ($('.special-room-slider').length) {
        $('.special-room-slider').slick({
            arrows: false,
            fade: false,
            dots: true,
        });
    }
    /*
      ============================================================
           Blog Slider Javascript
      ============================================================
    */
    if ($('.blog-slider').length) {
        $('.blog-slider').slick({
            arrows: true,
            fade: false,
            dots: false,
        });
    }
    /*
      ============================================================
           Room Detail Slider Javascript
      ============================================================
    */
    if ($('.slider-for').length) {
        $('.slider-for').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: true,
            fade: true,
            dots: false,
            asNavFor: '.slider-nav'
        });
    }
    if ($('.slider-nav').length) {
        $('.slider-nav').slick({
            slidesToShow: 6,
            slidesToScroll: 1,
            arrows: false,
            dots: false,
            centerMode: true,
            focusOnSelect: true,
            asNavFor: '.slider-for'
        });
    }
    /*
      ============================================================
           Testimonial Slider Javascript
      ============================================================
    */
    if ($('.chr-testimonial-1.arrows').length) {
        $('.chr-testimonial-1.arrows').slick({
            arrows: true
        });
    }
    /*
      ============================================================
           Fancy Effect Slider Javascript
      ============================================================
    */
    if ($('.fancy-effect').length) {
        $(".fancy-effect").hover3d({
            selector: ".fancy-thumb"
        });
    }
    /*
      ============================================================
           Custom Select Menu Slider Javascript
      ============================================================
    */
    if ($('select').length) {
        $('select').each(function() {
            var $this = $(this),
                numberOfOptions = $(this).children('option').length;
            $this.addClass('hidden');
            $this.wrap('<div class="text"></div>');
            $this.after('<div class="styledselect"></div>');
            var $styledselect = $this.next('div.styledselect');
            $styledselect.text($this.children('option').eq(0).text());
            var $list = $('<ul />', {
                'class': 'options'
            }).insertAfter($styledselect);
            for (var i = 0; i < numberOfOptions; i++) {
                $('<li />', {
                    text: $this.children('option').eq(i).text(),
                    rel: $this.children('option').eq(i).val()
                }).appendTo($list);
            }
            var $listItems = $list.children('li');
            $styledselect.click(function(e) {
                e.stopPropagation();
                $('div.styledselect.active').each(function() {
                    $(this).removeClass('active').next('ul.options').hide();
                });
                $(this).toggleClass('active').next('ul.options').toggle();
            });
            $listItems.click(function(e) {
                e.stopPropagation();
                $styledselect.text($(this).text()).removeClass('active');
                $this.val($(this).attr('rel'));
                $list.hide();
            });
            $(document).click(function() {
                $styledselect.removeClass('active');
                $list.hide();
            });
        });
    }
    /*
      ============================================================
           Brand Slider Javascript
      ============================================================
    */
    if ($('.brnd-slider').length) {
        $('.brnd-slider').slick({
            slidesToShow: 5,
            dots: false,
            autoplay: true,
            centerMode: true,
            arrows: true,
            responsive: [{
                breakpoint: 768,
                settings: {
                    arrows: false,
                    slidesToShow: 1
                }
            }, {
                breakpoint: 481,
                settings: {
                    arrows: false,
                    slidesToShow: 1
                }
            }]
        });
    }
    /*
      ============================================================
           Responsive Menu Javascript
      ============================================================
    */
    if (typeof($.fn.dlmenu) == 'function') {
        $('#mg-responsive-navigation').each(function() {
            $(this).find('.dl-submenu').each(function() {
                if ($(this).siblings('a').attr('href') && $(this).siblings('a').attr('href') != '#') {
                    var parent_nav = $('<li class="menu-item mg-parent-menu"></li>');
                    parent_nav.append($(this).siblings('a').clone());
                    $(this).prepend(parent_nav);
                }
            });
            $(this).dlmenu();
        });
    }
    /*
      ============================================================
           Twetter Tweet Javascript
      ============================================================
    */
    if ($("#twitter-feeds").length) {
        $("#twitter-feeds").tweet({
            count: 3,
            avatar_size: false,
            username: "OscarThemes",
            modpath: './js/twitter/',
            loading_text: "loading tweets..."
        });
    }
    /*
      ============================================================
           Flickr Feed Javascript
      ============================================================
    */
    if ($("#flickr-feeds").length) {
        $('#flickr-feeds').jflickrfeed({
            limit: 12,
            qstrings: {
                id: '152623543@N06'
            },
            itemTemplate: '<li>' + '<a class="lightbox" rel="prettyphoto" href="{{image}}" title="{{title}}">' + '<img src="{{image_s}}" alt="{{title}}" />' + '</a>' + '</li>'
        });
    }
    /*
    =======================================================================
        NEWSLETTER
    =======================================================================
    */
    $(function() {
        'use strict';
        var $form = $('#mc-embedded-subscribe-form');

        $('#mc-embedded-subscribe').on('click', function(event) {
            if (event) event.preventDefault();
            register($form);
        });
    });
    function register($form) {
        $.ajax({
            type: $form.attr('method'),
            url: $form.attr('action'),
            data: $form.serialize(),
            cache: false,
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
            error: function(err) {
                $('#notification_container').html('<div id="nl-alert-container"  class="alert alert-info alert-dismissible fade in bounceIn" role="alert" ><button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>Could not connect to server. Please try again later.</div>');
            },
            success: function(data) {

                if (data.result != "success") {
                    var message = data.msg;
                    $('#notification_container').html('<div id="nl-alert-container"  class="alert alert-info alert-dismissible fade in bounceIn" role="alert" ><button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>' + message + '</div>');
                } else {
                    var message = data.msg;
                    $('#notification_container').html('<div id="nl-alert-container"  class="alert alert-info alert-dismissible fade in bounceIn" role="alert" ><button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>' + message + '</div>');
                }
            }
        });
    }
    /*
    =======================================================================
         Header Sticky Script Library
    =======================================================================
    */
    if ($('.sticky-header').length) {
        if (window.matchMedia("(min-width: 768px)").matches) {
            $(function() {
                var header = $(".sticky-header");
                $(window).scroll(function() {
                    var scroll = $(window).scrollTop();

                    if (scroll >= 10) {
                        header.removeClass('affix-top').addClass("affix");
                    } else {
                        header.removeClass("affix").addClass('affix-top');
                    }
                });
            });
        }
    }
    /*
    =======================================================================
         Onepage Script Library
    =======================================================================
    */
    if ($('#opg-nav').length) {
        $('#opg-nav').onePageNav({
            currentClass: 'active',
            changeHash: false,
            scrollSpeed: 750
        });
    }
    /*
    =======================================================================
         Safari Navigation Script 
    =======================================================================
    */
    if ($('.safari').length) {
        $( ".safari .navigation li ul.children" ).removeClass( "children" );
        $( ".safari .navigation li ul" ).addClass( "safari-children" );
    }

    /*
    =======================================================================
         Js Not Function on Mobile Script
    =======================================================================
    */
    if( mobileDetect == false ) {
        /*
        =======================================================================
             Parallax Script
        =======================================================================
        */
        if ( $('.parallax-section').length ){
            $.stellar({
                horizontalScrolling: false,
                responsive: true
            }); 
        }; 

    }//END JS NOT FOR MOBILE
    if($('#map-canvas').length){
      google.maps.event.addDomListener(window, 'load', initialize);
    }
   
});


function initialize() {
  var MY_MAPTYPE_ID = 'custom_style';
  var map;
  var brooklyn = new google.maps.LatLng(40.6743890, -73.9455);
  var featureOpts = [
    {
      stylers: [
      { hue: '#f9f9f9' },     
      { visibility: 'simplified' },
      { gamma: 0.7 },
      { saturation: -200 },
      { lightness: 45 },
      { weight: 0.6 }
      ]
    },
    {
    featureType: "road",
      elementType: "geometry",
      stylers: [
      { lightness: 200 },
      { visibility: "simplified" }
      ]
    },
    {
      elementType: 'labels',
      stylers: [      
      { visibility: 'on' }
      ]
    },
    {
      featureType: 'water',
      stylers: [
      { color: '#ffffff' }
      ]
    }
  ];  

  var mapOptions = {
    zoom: 15,
    scrollwheel: false,
    center: brooklyn,
    mapTypeControlOptions: {
      mapTypeIds: [google.maps.MapTypeId.ROADMAP, MY_MAPTYPE_ID]
    },
    mapTypeId: MY_MAPTYPE_ID
  };

  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  var styledMapOptions = {
    name: 'Custom Style'
  };

  var customMapType = new google.maps.StyledMapType(featureOpts, styledMapOptions);

  map.mapTypes.set(MY_MAPTYPE_ID, customMapType);
    var marker=new google.maps.Marker({
      position:brooklyn,
      icon:'extra-images/map.png'
  });

  marker.setMap(map);
}