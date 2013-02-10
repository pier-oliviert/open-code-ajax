(function() {
/* {% if form.validate() %} */
	$("#todos").append("{{ todo_html }}");
	$("form .uiErrors").html("");
	$("form input[type=text]").val("");
/* {% else %} */
	ul = $("form .uiErrors").html($("{{form.errors.title|e}}"))
/* {% endif %} */
})();