$(document).ready(function (){
    function refresh(){
      $.ajax({
        url: "/store/admin_orders",
        success: function (data){
          $('.refresh-table').replaceWith($('.refresh-table', data));
          console.log('Refresh Admin')
        }
      });
    }
    var seconds = 30;
    setInterval(refresh, seconds*1000)
});
