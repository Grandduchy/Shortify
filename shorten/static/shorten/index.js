$(document).ready(function() {
	var formData = {n : "N+", a:"A-"};
	$("#gen-link-btn").on("click", () => {

		$.ajax({
			url : "http://127.0.0.1:8000/api/post",
			type : "POST",
			data : formData,
			success : function(data, txtStatus, jqXHR) {
				console.log("Success ajax, returned : " + data);
			},
			error : function(jqXHR, txtStatus, err) {
				console.log("Fail ajax");
			}
		});

	});

});


