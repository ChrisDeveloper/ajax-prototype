function ajaxScript() {
    var input = $("#input").val();
    $.ajax({
        type: "POST",
        url: "/",
        data: JSON.stringify({
            "name": input
        }),
        dataType: "json"
    })
        .done(function(jsonResponse) {
            $("#error").html(jsonResponse.message);
        });
}
