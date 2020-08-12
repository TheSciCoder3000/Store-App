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

function hide_me(this_item){
  var item_checkbox = document.querySelector("#"+ this_item +"-checkbox");
  var item_settings = document.querySelector("#"+ this_item +"-order");

  if (item_checkbox.checked){
    item_settings.style.display = "block";
  }else {
    item_settings.style.display = "none";
  }
}
