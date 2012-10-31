(function() {
{% load captureas %}

{% if form.is_valid %}
	{% captureas partial %}{% include "todos/todo.html" with todo=form.instance %}{% endcaptureas %}
	$("#todos").append($("{{partial|escapejs}}"))
	$("form .uiErrors").html("")
	$("form input[type=text]").val("")
{% else %}
	ul = $("form .uiErrors").html($("{{form.errors.title|escapejs}}"))
{% endif %}

})()