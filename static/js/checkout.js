$(document).ready(function() {
     $.getJSON("/static/js/eg.json", function(data) {
        for(var i = 0; i < data.length; i++) {
            $("#cities").append('<option value="' + data[i].city_name_ar + '">' + data[i].city_name_ar + '</option');
        }
       
    });
$(document).on('change','#cities',function(){
    var city_id=$(this).val();
    $.getJSON("/static/js/eg.json", function(data) {
        for(var i = 0; i < data.length; i++) {
            if(data[i].city_name_ar==city_id){
                //console.log(data[i].lat)
                var myNumbers=parseFloat(data[i].costShaping).toFixed(2);
                $('#myid').text(myNumbers);
                var all = document.getElementById("helper").getAttribute("data-name");
                $('#totalpay').text(+all + +myNumbers);
            }
            
            
        }
       
    });
})

    });
