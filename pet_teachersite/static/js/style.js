$(document).ready(function() {
    $('.nav_burger').click(function(event) {
        $('.nav_burger, .nav_burger_line, .nav_main').toggleClass('active');
    });
});

document.getElementById('SignForm').addEventListener('submit'), 
function(event) {
    var f_name = this.querySelection('[f_name="f_name"]').value;
    var l_name = this.querySelection('[l_name="l_name"]').value;
    var datetime_local = this.querySelection('[datetime_local="datetime_local"]').value;
}