
var internalServerError = function(jsonObj) {
	if ($("#url-result").hasClass("hide"))
		$("#url-result").removeClass("hide");

	$("#output").empty();
	$("#output").append(jsonObj["message"]);
	$("#info-output").empty();
	$("#info-output").append("An Internal server error has occured : ");

}

var connectionError = function(errObj) {
	if ($("#url-result").hasClass("hide"))
		$("#url-result").removeClass("hide");

	$("#output").empty();
	$("#info-output").empty();

	var message;
	if (errObj.responseText)
		message = errObj.responseText;
	else
		message = "Unkown error in connection to server";

	$("#output").append(message);
	$("#info-output").append("An error in connecting to the server occured : ");
}

var success = function(jsonObj) {
	if ($("#url-result").hasClass("hide"))
		$("#url-result").removeClass("hide");

	$("#output").empty();
	$("#info-output").empty();
	$("#output").append(jsonObj["url"]);
	$("#info-output").append("Url successfully created, located at : ");
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


