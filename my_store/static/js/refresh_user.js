$(document).ready(function (){
    function refresh(){
      $.ajax({
        url: "/user/profile/",
        success: function (data){
          $('.refresh-table').replaceWith($('.refresh-table', data));
        }
      });
    }
    var seconds = 30;
    setInterval(refresh, seconds*1000)
});
