$(document).ready(function (){

    function refresh(){
      console.log('Refreshing');
      $.ajax({
        url: "",
        success: function (data){
          $('#store-body').replaceWith($('#store-body', data));
        }
      });
    }
    setInterval(refresh, 10000)
});
