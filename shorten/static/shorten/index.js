
var internalServerError = function(jsonObj) {
	if (!$(".url-success").hasClass("hide"))
		$(".url-success").addClass("hide");
	if ($(".url-error").hasClass("hide"))
		$(".url-error").removeClass("hide");

	$("#error-output").empty();
	$("#error-output").append(jsonObj["message"]);

}

var connectionError = function(errObj) {
	if (!$(".url-success").hasClass("hide"))
		$(".url-success").addClass("hide");
	if ($(".url-error").hasClass("hide"))
		$(".url-error").removeClass("hide");

	$("#error-output").empty();

	var message;
	if (errObj.responseText)
		message = errObj.responseText;
	else
		message = "Unkown error in connection to server";

	$("#error-output").append(message);
}

var success = function(jsonObj) {
	if (!$(".url-error").hasClass("hide"))
		$(".url-error").addClass("hide");
	if ($(".url-success").hasClass("hide"))
		$(".url-success").removeClass("hide");

	$("#success-output").empty()
	$("#success-output").append(jsonObj["url"]);
}


$(document).ready(function() {
	$("#gen-link-btn").on("click", () => {
		// Get url from user
		var enteredUrl = $("#urlInput").val();
		var formData = {
			url: enteredUrl
		};
		$.ajax({
			url : "http://127.0.0.1:8000/api/post",
			type : "POST",
			data : formData,
			success : function(data, txtStatus, jqXHR) {
				if (data["success"])
					success(data);
				else
					internalServerError(data);
			},
			error : function(jqXHR, txtStatus, err) {
				connectionError(err);
			}
		});

	});

});


