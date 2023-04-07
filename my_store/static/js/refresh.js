$(document).ready(function (){
    function refresh(){
      $.ajax({
        url: "/store/",
        success: function (data){
          $('.item-contents').replaceWith($('.item-contents', data));
        }
      });
    }
    var seconds = 30;
    setInterval(refresh, seconds*1000)
});
