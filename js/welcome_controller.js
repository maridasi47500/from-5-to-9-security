function randomChar(){
var index=Math.floor(Math.random() * 62);
if (index < 10){
return String(index);
}else if (index < 36){
return String.fromCharCode(index + 55);
}else {
return String.fromCharCode(index + 61);
}
}
function  randomString(length){
var result="a";
while (length > 0){
result +=randomChar();
length--;
}
return result;
}

function on(e) {
	e.preventDefault();
  document.getElementById("overlay").style.display = "block";
	return false;
}

function off() {
  document.getElementById("overlay").style.display = "none";
} 
$(function(){
	$(".closemenu").click(function(e){
        e.preventDefault();
        e.stopPropagation();
  document.getElementById("overlay").classList.add("closeme");
setTimeout(() => {
  console.log("Delayed for 1 second.");
  document.getElementById("overlay").style.display = "none";
  document.getElementById("overlay").classList.remove("closeme");
}, "1000");


});
	$(".navbar-toggler.ijijijkijiji").click(function(e){
        e.preventDefault();
        e.stopPropagation();
  document.getElementById("overlay").style.display = "block";

});


function init() {
	"use strict";
        
        var minduration=0;
	var posSlider = document.getElementById("myRange");
	var volSlider = document.getElementById("myVol");
	window.audio1=new Audio();
	$(posSlider).on('input',function (e) {
            e.preventDefault();
		window.audio1.currentTime = posSlider.value;


	});
	$(posSlider).on('change',function (e) {

            e.preventDefault();
		posSlider.value = window.audio1.currentTime;


	});

	var goBut = document.getElementById("goButton");
	var playPic = "/img/play.png";
	var pausePic = "/img/pause.png";
        var paspremier=false;
                    window.audio1.src="/uploads/shakira-acrostico.mp3";
               if (window.audio1 && !window.audio1.paused){
                    window.audio1.pause();
               }
                    window.audio1.play();
			goBut.src = pausePic;
       
                    if (!paspremier){
                    window.audio1.addEventListener('loadedmetadata',setMax);


        function setMax() {
            //e.preventDefault();
            console.log(Number(window.audio1.duration));
		posSlider.max= window.audio1.duration; posSlider.setAttribute('min', 0);
                //console.log(minduration);
                window.audio1.currentTime = 0;
                   if (!window.audio1.paused){
                    window.audio1.pause();
                   }

                window.audio1.play();
                //posSlider.value = minduration;
	};
                window.audio1.addEventListener("timeupdate", voirmusique);
	function voirmusique() {
            console.log("tyui CURRENTIME",window.audio1.currentTime);
		//posSlider.value = 0;
		posSlider.value = window.audio1.currentTime;
		if (window.audio1.ended || window.audio1.max === window.audio1.duration) {
			posSlider.value = 0;
			window.audio1.currentTime = 0;
		}
	};
        paspremier=true;
        }
	$(goBut).click(function (e) {
            e.preventDefault();
		if (!window.audio1 || window.audio1.paused) {
			
                            minduration=window.audio1.duration;


                   if (!window.audio1.paused){
                    window.audio1.pause();
                   }
                    window.audio1.play();
			goBut.src = pausePic;
                            }else{
                       //console.log("none");
                    window.audio1.pause();
                    //window.audio1=new Audio();
			goBut.src = playPic;
                            }
            
                        
	});




	$(volSlider).on('input',function (e) {
            e.preventDefault();
		window.audio1.volume = volSlider.value / 100;
                $.ajax({type:"get",url:"/songs/playmusique1",data:{myvol: $("#myVol").val()},
        success:function(data){
console.log(data);
        }
        });
	});
     
        $.ajax({url:"/songs/musique",
        success:function(data){
            if (data.ok === "1"){
                //console.log(data.myvol)
                $(goBut).click();
                $("#myVol")[0].value=(parseInt(data.myvol));
                window.audio1.volume = volSlider.value / 100;
            }
        }
        });
};

init();

});
