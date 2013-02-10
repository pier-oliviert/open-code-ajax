// Avoid `console` errors in browsers that lack a console.
(function() {
    var method;
    var noop = function () {};
    var methods = [
        'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
        'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
        'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
        'timeStamp', 'trace', 'warn'
    ];
    var length = methods.length;
    var console = (window.console = window.console || {});

    while (length--) {
        method = methods[length];

        // Only stub undefined methods.
        if (!console[method]) {
            console[method] = noop;
        }
    }
}());

var todos = function(){
    return {
        init: function(){
            console.log("todos.init()");

            $("form input[type=submit]").click(function(){
                console.log("input[type=submit].click !");

                if ($("#title").val() !== "") {
                    $.ajax({
                        url:"/create",
                        type: "PUT",
                        data: $("form").serialize(),
                        complete : function(response){
                            console.log(response);
                            // eval(response.responseText);
                        }
                    });
                }
                return false;
            });

            $("#todos input[type=checkbox]").live("mousedown", function(){
                console.log("input[type=checkbox].mousedown !");

                var id = $(this).attr("id").replace("todo_", "")

                $.ajax({
                    url:"/done/" + id,
                    type: "DELETE",
                    complete : function(response){
                        console.log(response);
                        // eval(response.responseText);
                    }
                });
                return false;
            });
        }
    }
}();

$(document).ready(function(){
    todos.init();
});