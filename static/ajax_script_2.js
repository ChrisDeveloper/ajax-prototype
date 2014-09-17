function ajaxScript2() {
    var input = document.getElementById("input").value;
    var data = JSON.stringify({
        "name": input
    });
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/", true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var jsonResponse = JSON.parse(xhr.responseText);
            document.getElementById("error").innerHTML = jsonResponse.message;
        }
    };
    xhr.send(data);
}
