$(document).ready(function () {
    // Init Sidebar
    $(".sidebar.top").sidebar({side: "top"});
    $(".sidebar.bottom").sidebar({side: "bottom"});
    $(".sidebar.right").sidebar({side: "right"});

    // Click Handler
    $(".trigger[data-action]").on("click", function () {
        var $this = $(this);
        var action = $this.attr("data-action");
        var side = $this.attr("data-side");
        $(".sidebar." + side).trigger("sidebar:" + action);
        return false;
    });
});