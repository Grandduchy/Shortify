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
				if (!data["success"]) {
					console.log("Failure detected");
					console.log(data["message"]);
				}
				else {
					console.log(data["url"]);
				}
			},
			error : function(jqXHR, txtStatus, err) {
				console.log("Fail ajax");
			}
		});

	});

});


