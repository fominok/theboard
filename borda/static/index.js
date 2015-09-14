function main() {
    $(".thread_name")
        .mouseenter(function(){
            $(this).addClass("thread_name_focus")
    })
        .mouseleave(function(){
            $(this).removeClass("thread_name_focus")
    });
}

$(document).ready(main)