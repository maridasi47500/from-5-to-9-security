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
	var audio1=new Audio();
	$(posSlider).on('input',function (e) {
            e.preventDefault();
		audio1.currentTime = posSlider.value;
	});
	$(posSlider).on('change',function (e) {

            e.preventDefault();
		audio1.currentTime = posSlider.value;
	});
        /*$.ajax({url:"/songs/jouerunechanson",success:function(data){
        audio1=new Audio('/uploads/'+data.song.filename);*/

	var goBut = document.getElementById("goButton");
	var playPic = "/img/play.png";
	var pausePic = "/img/pause.png";
        var paspremier=false;
	var mydata;
                    audio1.src="/uploads/shakira-acrostico.mp3";
               if (audio1 && !audio1.paused){
                    audio1.pause();
               }
                    audio1.play();
			goBut.src = pausePic;
       
	$(goBut).click(function (e) {
            e.preventDefault();
		if (!audio1 || audio1.paused) {
                     $.ajax({type:"get",url:"/songs/playmusique",data:{play:1},
        success:function(data){
console.log(data);
        }
        });
			
                        $.ajax({url:"/songs/jouerunechanson",success:function(data){
//console.log(JSON.stringify(data)+"azertyui"+(data.song));
                            minduration=audio1.duration;
                            mydata=data;
                            if(data.song){
var xxxxx=randomString(10);
                    $.ajax({url:"/somecss",data:{myid: xxxxx},success:function(data){
console.log("heure de passage ")
$('head').append("<style>"+data+"</style>");
$('body').append("<div class=\"noel\" id=\""+xxxxx+"\"></div>");
$("#"+xxxxx).addClass("xmas");
                        }});
                    audio1.src=('/uploads/'+data.song.filename);

                    if (!paspremier){
                    audio1.addEventListener('loadedmetadata',setMax);

                    $.ajax({url:"/passage",data:{title: audio1.src},success:function(data){
console.log("heure de passage ")
                        }});

        function setMax() {
            //e.preventDefault();
            console.log(Number(audio1.duration));
		posSlider.max= audio1.duration; posSlider.setAttribute('min', 0);
                //console.log(minduration);
                audio1.currentTime = 0;
                audio1.play();
                $(".precedent").html("<h6>précédente</h6><span>"+(mydata.song.artist_prec|| "")+"</span><span>"+(mydata.song.title_prec|| "")+"</span>");
                $(".encours").html("<h6>Maintenant</h6><span>"+(mydata.song.artist|| "")+"</span><span>"+(mydata.song.title|| "")+"</span>");
                $(".avenir").html("<h6>Suivante</h6><span>"+(mydata.song.artist_suiv|| "")+"</span><span>"+(mydata.song.title_suiv|| "")+"</span>");
                //posSlider.value = minduration;
	};
                audio1.addEventListener("timeupdate", voirmusique);
	function voirmusique() {
            console.log("tyui CURRENTIME",audio1.currentTime);
		//posSlider.value = 0;
		posSlider.value = audio1.currentTime;
		if (audio1.ended || audio1.max === audio1.duration) {
                    $.ajax({url:"/songs/jouerunechanson",success:function(data){
//console.log(JSON.stringify(data))
                                    minduration=audio1.duration;
                                    mydata=data;
                                    if(data.song){
                            audio1.src='/uploads/'+data.song.filename;
                                    }else{


			audio1.pause();
                            audio1=new Audio();
			goBut.src = playPic;
                                    }
                        }});
			posSlider.value = 0;
			audio1.currentTime = 0;
			//goBut.src = playPic;
			//audio1.pause();
		}
	};
        paspremier=true;
        }
                    audio1.play();
			goBut.src = pausePic;
                            }else{
                       //console.log("none");
                    audio1.pause();
                    audio1=new Audio();
                            }
                }});
            
                        
		} else {
			audio1.pause();
			audio1=new Audio();
			goBut.src = playPic;
                          $.ajax({type:"get",url:"/songs/playmusique",data:{play:0},
        success:function(data){
console.log(data);
        }
        });
		}
	});




	$(volSlider).on('input',function (e) {
            e.preventDefault();
		audio1.volume = volSlider.value / 100;
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
                audio1.volume = volSlider.value / 100;
            }
        }
        });
            /*}});*/
};

init();

});
