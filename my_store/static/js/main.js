
$('#prod_table').DataTable();
$('#user-table').DataTable();
$('#admin-table').DataTable();

var use_ajax = true;
function deactivate_me(btn_id){
  if(!$(btn_id).hasClass("submitted")){
    $(btn_id).addClass("submitted");
    $.ajax({
      type: "GET",
      url: '/deactivate_btn/',
      dataType: 'json',
      success: function (data){
        if (data.msg == 'success'){
          $(btn_id).removeClass("submitted");
        }
      }

    });
  }
}   //Deactivate the button to avoid double ordering

function updateQuantity(){
  var quantityItems = document.querySelectorAll(".item-quantity");
  var quantityCounter = document.querySelectorAll(".item-quantity-counter > input[type='number']");
  var btn_id = document.getElementById("update-btn");
  var update_btns = document.getElementById("update-buttons");
  for (i = 0; i < quantityItems.length; i++) {
    if (quantityItems[i].classList.contains("hidden")){
      quantityItems[i].classList.remove("hidden");
      quantityCounter[i].style.display = "none";
      btn_id.style.display = "block";
    }else{
      quantityItems[i].classList.add("hidden");
      quantityCounter[i].style.display = "block";
      btn_id.style.display = "none";
      update_btns.classList.remove("hidden");
    }
  }

}

function cancelUpdate(){
  var update_btns = document.getElementById("update-buttons");
  update_btns.classList.add("hidden");
  updateQuantity();
}

function hide_me(this_item, id){
  var item_checkbox = document.querySelector("#"+ this_item +"-checkbox");
  var item_settings = document.querySelector("#"+ this_item +"-order");
  var IS_select = item_settings.childNodes[1];
  var IS_counter = item_settings.childNodes[3];

  if (item_checkbox.checked){
    IS_select.value = id.toString();
    IS_counter.style.display = "block";
    IS_counter.value = "1.00";
  }else {
    IS_select.value = "";
    IS_counter.style.display = "none";
    IS_counter.value = "";
  }
}   //Hide the number input of each item

function check_price(this_item, item_thresh, item_discount){
  var item_price = document.querySelector("#"+this_item+"-price").innerHTML;
  var item_count = document.querySelector("#form-"+this_item+"-counter").value;

  if (item_thresh == null){
  } else if (item_count > item_thresh){
    document.getElementById(this_item+"-price").innerHTML = parseInt(item_price)*(1-item_discount);
  }
}
