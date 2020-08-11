$(document).ready(function (){

    function refresh(){
      console.log('Refreshing 1');
      $.ajax({
        url: "",
        success: function (data){
          $('#store-body').replaceWith($('#store-body', data));
        }
      });
    }
    var seconds = 60;
    setInterval(refresh, seconds*1000)
});
