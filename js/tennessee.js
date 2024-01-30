function hey(){

}
$(function(){
if ($('form.youbankforminscription').length  > 0){
$('form.youbankforminscription').on('submit', function () {
  var password = my_password.value
  if (password.length < 8){
    alert("mauvais mot de passe");
    return false;
  }
  var amajuscule=/[A-Z]/.test(password);
  var aminuscule=/[a-z]/.test(password);
  var anombre=/\d/.test(password);
  var anonalpha=/\W/.test(password);
  if (amajuscule + aminuscule + anombre + anonalpha < 3){
    alert("mauvais mot de passe");
    return false;
  }
  if (window.filesize > 1024*5) {
    alert('max upload size is 5k');
    return false;
  }
  $.ajax({
    // Your server script to process the upload
    url: $(this).attr("action"),
    type: 'POST',

    // Form data
    data: new FormData($(this)[0]),

    // Tell jQuery not to process data or worry about content-type
    // You *must* include these options!
    cache: false,
    contentType: false,
    processData: false,

    // Custom XMLHttpRequest
    success: function (data) {
	    console.log("HEY")
	    console.log(JSON.stringify(data))
	    console.log(JSON.stringify(data.redirect))
	    if (data.redirect){
	    window.location=data.redirect;
	    }else{
	    window.location="/welcome";
	    }
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
  };
if (window.location.pathname.includes("/fill_in_inbox")){
$.ajax({url:"/check_mailbox",
success:function(data){
var email,emails=data.emails;
$('.nbemails').html(Number($('.nbemails').html()) + emails.length);
for (var i = 0;i<emails.length;i++){
email=emails[i];
$(".inboxmail").append("<li>"+email.subject+"<a href=\"javascript:void(0)\" onclick=\"$.ajax({url:'/voiremail/"+String(email.id)+"',success:function(data){$('#text').html(data);overlay.style.display='block';}});\">lire email</a></li>");
};
},
error:function(){
}
});
}
});
