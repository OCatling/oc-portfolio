$(document).ready(function () {
    // Init Sidebar
    $(".sidebar.right").sidebar({side: "right"});

    // Click Handler
    $(".trigger[data-action]").on("click", function () {
        var $this = $(this);
        var action = $this.attr("data-action");
        var side = $this.attr("data-side");
        $(".sidebar." + side).trigger("sidebar:" + action);
        var w = $(".main.wrapper").css("width").replace(/[^-\d\.]/g, ''); // Gets Wrapper Width
        $(".sidebar.right").on("sidebar:opened", function () {
            $(".main.wrapper").width(w - 0.1);
        });

        $(".sidebar.right").on("sidebar:closed", function () {
            $(".main.wrapper").width(w + 0.1);
        });


        /*var w = $(".wrapper").css("width").replace(/[^-\d\.]/g, ''); // Gets Wrapper Width
        $(".wrapper").width(w - 1);*/
        return false;
    });

    $("#about").on("click", function () {
        $("#contact_form").hide();
        $("#about_section").show();
    });


    $("#contact").on("click", function () {
        $("#about_section").hide();
        $("#contact_form").show();
    });
});