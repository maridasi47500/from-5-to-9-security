

$(function(){
    if ($("#quelestcetitre").length > 0) {
    $("#quelestcetitre").submit(function(){
        var ok=$(this)[0];
    $.ajax({url: ok.action,data:$(this).serialize(), type: ok.method, success:function(data){
            console.log(data);
            if (data.length > 0) {
                $('.dialog').hide();
                $(".monresultat").html(data);
            }else{
                 $('.dialog').show();
                 $(".monresultat").html("");
            }
    }
});
return false;
});
    }
});