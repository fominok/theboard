function main(){
    $("#resp_button").click(function(){
        if ($("#post_maker").is(":hidden")){
            $("#post_maker").slideDown("fast");
            $("#resp_button").text("[Скрыть форму]");
        } else {
            $("#post_maker").slideUp("fast");
            $("#resp_button").text("[Ответить в тред]");
        }
    })
}

$(document).ready(main)