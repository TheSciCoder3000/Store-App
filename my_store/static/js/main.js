const hideOrderCount = document.querySelector('.check');
const orderSettings = document.querySelector('.order-settings');
orderSettings.style.display = "none";

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
    var seconds = 14400;
    setInterval(refresh, seconds*1000)
});

$('#prod_table').DataTable();

hideOrderCount.addEventListener('change', function(event){
  if(hideOrderCount.checked){
    orderSettings.style.display = "block";
  }else {
    orderSettings.style.display = "none";
  }
});
