function hey(){

}
$(function(){
$.ajax({url:"/check_mailbox",
success:function(data){
var email,emails=data.emails;
$('.nbemails').html(Number($('.nbemails').html()) + emails.length);
for (var i = 0;i<emails.length;i++){
email=emails[i];
};
},
error:function(){
}
});
});
