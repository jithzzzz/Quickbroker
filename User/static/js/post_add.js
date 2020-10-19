$(".tab-1").click(function(){
    $(".conntent").removeClass('visible_div');
    $(".conntent").removeClass('hidden');
    $(".conntent").addClass('hidden');
    $(".content-tab-1").removeClass('hidden');
    $(".content-tab-1").addClass('visible_div');
});
$(".tab-2").click(function(){
    $(".conntent").removeClass('visible_div');
    $(".conntent").removeClass('hidden');
    $(".conntent").addClass('hidden');
    $(".content-tab-2").removeClass('hidden');
    $(".content-tab-2").addClass('visible_div');
});

$(".tab-3").click(function(){
    $(".content-tab-3").removeClass('visible_div');
    $(".content-tab-3").addClass('hidden');
    $(".conntent").addClass('hidden');
    $(".content-tab-3").removeClass('hidden');
    $(".content-tab-3").addClass('visible_div');
});

$(".tab-4").click(function(){
    $(".content-tab-4").removeClass('visible_div');
    $(".content-tab-4").addClass('hidden');
    $(".conntent").addClass('hidden');
    $(".content-tab-4").removeClass('hidden');
    $(".content-tab-4").addClass('visible_div');
});

$(".tab-5").click(function(){
    $(".content-tab-5").removeClass('visible_div');
    $(".content-tab-5").addClass('hidden');
    $(".conntent").addClass('hidden');
    $(".content-tab-5").removeClass('hidden');
    $(".content-tab-5").addClass('visible_div');
});


$(".tab-6").click(function(){
    $(".content-tab-6").removeClass('visible_div');
    $(".content-tab-6").addClass('hidden');
    $(".conntent").addClass('hidden');
    $(".content-tab-6").removeClass('hidden');
    $(".content-tab-6").addClass('visible_div');
});

$(".tab-7").click(function(){
    $(".content-tab-7").removeClass('visible_div');
    $(".content-tab-7").addClass('hidden');
    $(".conntent").addClass('hidden');
    $(".content-tab-7").removeClass('hidden');
    $(".content-tab-7").addClass('visible_div');
});

$("#Property_Details_btn").click(function(){
    console.log("*** Propert details submit ***");
    var Apartment_Type = $("#Apartment_Type").val();
    var BHK_Type = $("#BHK_Type").val();
    var Ownership_Type = $("#Ownership_Type").val();
    var Built_Up_Area = $("#Built_Up_Area").val();
    var Property_Age = $("#Property_Age").val();
    var Facing = $("#Facing").val();
    var Floor_Type = $("#Floor_Type").val();
    var Floor = $("#Floor").val();
    var Total_Floor = $("#Total_Floor").val();

    $.ajax({
        url: '/property-details-submit',
        type: 'POST',
        data:{
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            Apartment_Type : Apartment_Type,
            BHK_Type : BHK_Type,
            Ownership_Type : Ownership_Type,
            Built_Up_Area : Built_Up_Area,
            Property_Age : Property_Age,
            Facing : Facing,
            Floor_Type : Floor_Type,
            Floor : Floor,
            Total_Floor : Total_Floor
            
        },
        success:function(data){
            console.log(data);            
        },
        error:function(res){
            console.log(res)
        }
    });

});

