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

    $("#submit_link").click(function(){
        if ($("#post_input_field").val().length < 20) {
            alert("Напиши хоть 20 символов что ли");
        } else {
            $("#form").submit()
        }
    })
}

$(document).ready(main)
