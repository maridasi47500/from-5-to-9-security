$(function(){
$("#mysum").on('submit', function () {
$.ajax({url: "/mysum",
    data: new FormData($('#mysum')[0]),
    cache: false,
    contentType: false,
    processData: false,
type:"post",
success:function(data){
$("#result").html(String(data["mysum"])+"$");
}});
return false;
});
$(".close").on('click', function () {
  document.getElementById("overlay").style.display = "none";
});
$("#button1").on('click', function () {
$("#result").html(String(0)+"$");
  document.getElementById("overlay").style.display = "block";

$.ajax({url: "/dates",
success:function(data){
var option=$("#select1")[0];
var mydates=data.dates;
option.innerHTML="<option>sélectionner une date</option>";
for (var x=0;x<mydates.length;x++){

option.innerHTML+="<option value=\""+String(mydates[x].date)+"\">"+String(mydates[x].date)+"</option>";
}
}});
return false;
});
$("[name='image']").on('change', function () {
  var file = this.files[0];
  window.filesize=file.size;

  if (window.filesize > 1024*5) {
    alert('max upload size is 5k');
  }

  // Also see .name, .type
});
$('#myform').on('submit', function () {
  if (window.filesize > 1024*5) {
    alert('max upload size is 5k');
return false;
  }
  $.ajax({
    // Your server script to process the upload
    url: '/create',
    type: 'POST',

    // Form data
    data: new FormData($('#myform')[0]),

    // Tell jQuery not to process data or worry about content-type
    // You *must* include these options!
    cache: false,
    contentType: false,
    processData: false,

    // Custom XMLHttpRequest
    success: function (data) {
window.location="/myshop";
},
    xhr: function () {
      var myXhr = $.ajaxSettings.xhr();
      if (myXhr.upload) {
        // For handling the progress of the upload
        myXhr.upload.addEventListener('progress', function (e) {
          if (e.lengthComputable) {
            $('progress').attr({
              value: e.loaded,
              max: e.total,
            });
          }
        }, false);
      }
      return myXhr;
    }
  });
	return false;
});
});
