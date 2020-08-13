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
  console.log('Show me');

  if (item_checkbox.checked){
    item_settings.style.display = "block";
  }else {
    item_settings.style.display = "none";
  }
}

function check_price(this_item, item_thresh, item_discount){
  var item_price = document.querySelector("#"+this_item+"-price").innerHTML;
  var item_count = document.querySelector("#form-"+this_item+"-counter").value;

  if (item_thresh == null){
    console.log("Threshold is Null");
  } else if (item_count > item_thresh){
    document.getElementById(this_item+"-price").innerHTML = parseInt(item_price)*(1-item_discount);
    console.log(parseInt(item_price)*(1-item_discount));
  }
}
