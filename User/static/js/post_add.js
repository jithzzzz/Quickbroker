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
            $(".Location_Details_btn").attr('id', data.id);
            $(".Resale_Details_btn").attr('id', data.id);
            $(".Amenities_btn").attr('id', data.id);
            $(".Additional_Information_btn").attr('id', data.id);
            $(".Schedule_btn").attr('id', data.id);
            $(".Additional_Information_btn").attr('id', data.id);

            $(".conntent").removeClass('visible_div');
            $(".conntent").removeClass('hidden');
            $(".conntent").addClass('hidden');
            $(".content-tab-2").removeClass('hidden');
            $(".content-tab-2").addClass('visible_div');            
        },
        error:function(res){
            console.log(res)
        }
    });

});


$(".Location_Details_btn").click(function(){
    console.log("*** Location details submit ***");
    var District = $("#District").val();
    var Pin_Code = $("#Pin_Code").val();
    var Address = $("#Address").val();
    var Near_By = $("#Near_By").val();

    $.ajax({
        url: '/location-details-submit',
        type: 'POST',
        data:{
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            District : District,
            Pin_Code : Pin_Code,
            Address : Address,
            Near_By : Near_By,
            ads_id:$(this).attr('id')
        },
        success:function(data){
            console.log(data);
            $(".content-tab-3").removeClass('visible_div');
            $(".content-tab-3").addClass('hidden');
            $(".conntent").addClass('hidden');
            $(".content-tab-3").removeClass('hidden');
            $(".content-tab-3").addClass('visible_div');            
        },
        error:function(res){
            console.log(res)
        }
    });

});


$(".Resale_Details_btn").click(function(){
    console.log("*** Resale Details submit ***");
    var Expected_Price = $("#Expected_Price").val();
    var Maintenance_Cost = $("#Maintenance_Cost").val();
    var Available_From = $("#Available_From").val();
    var Kitchen_Type = $("#Kitchen_Type").val();
    var Furnishining = $("#Furnishining").val();
    var Parking = $("#Parking").val();
    var Description = $("#Description").val();
    
    $.ajax({
        url: '/resale-details-submit',
        type: 'POST',
        data:{
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            Expected_Price : Expected_Price,
            Maintenance_Cost : Maintenance_Cost,
            Available_From : Available_From,
            Kitchen_Type : Kitchen_Type,
            Furnishining : Furnishining,
            Kitchen_Type : Kitchen_Type,
            Parking : Parking,
            Description : Description,
            ads_id:$(this).attr('id')
        },
        success:function(data){
            console.log(data);
            $(".content-tab-4").removeClass('visible_div');
            $(".content-tab-4").addClass('hidden');
            $(".conntent").addClass('hidden');
            $(".content-tab-4").removeClass('hidden');
            $(".content-tab-4").addClass('visible_div');         
        },
        error:function(res){
            console.log(res)
        }
    });

});


$(".Amenities_btn").click(function(){
    console.log("*** Resale Details submit ***");
    var Bathroom = $("#Bathroom").val();
    var Balcony = $("#Balcony").val();
    var Water_supply = $("#Water_supply").val();
    var Gym = $("#Gym").val();
    var Power_Backup = $("#Power_Backup").val();
    var Gated_security = $("#Gated_security").val();
    var Who_will_show_the_house = $("#Who_will_show_the_house").val();
    var Secondry_Number = $("#Secondry_Number").val();
    var Club_House = $('#Club_House').is(':checked'); 
    var Swimming_Pool = $('#Swimming_Pool').is(':checked');
    var Lift = $('#Lift').is(':checked');
    var Security = $('#Security').is(':checked'); 
    var Children_Play_Area = $('#Children_Play_Area').is(':checked'); 
    var Intercom = $('#Intercom').is(':checked'); 
    var Shoping_Center = $('#Shoping_Center').is(':checked'); 
    var Park = $('#Park').is(':checked'); 
    var Gas_Pipeline = $('#Gas_Pipeline').is(':checked'); 
    var Internet_Provider = $('#Internet_Provider').is(':checked'); 
    var Fire_Safety = $('#Fire_Safety').is(':checked'); 

    $.ajax({
        url: '/amenities-submit',
        type: 'POST',
        data:{
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            Bathroom : Bathroom,
            Balcony : Balcony,
            Water_supply : Water_supply,
            Gym : Gym,
            Power_Backup : Power_Backup,
            Gated_security : Gated_security,
            Who_will_show_the_house : Who_will_show_the_house,
            Secondry_Number : Secondry_Number,
            Club_House : Club_House, 
            Swimming_Pool : Swimming_Pool,
            Lift : Lift,
            Security : Security,
            Children_Play_Area : Children_Play_Area, 
            Intercom : Intercom, 
            Shoping_Center : Shoping_Center, 
            Park : Park,
            Gas_Pipeline : Gas_Pipeline, 
            Internet_Provider : Internet_Provider,
            Fire_Safety : Fire_Safety,
            ads_id:$(this).attr('id')
        },
        success:function(data){
            console.log(data);
            $(".content-tab-5").removeClass('visible_div');
            $(".content-tab-5").addClass('hidden');
            $(".conntent").addClass('hidden');
            $(".content-tab-5").removeClass('hidden');
            $(".content-tab-5").addClass('visible_div');       
        },
        error:function(res){
            console.log(res)
        }
    });
    
});


$(".Additional_Information_btn").click(function(){
    console.log("*** Additional Information submit ***");
    var I_want_to_get_my_property_painte = $("#I_want_to_get_my_property_painte").val();
    var I_want_to_get_my_property_cleaned = $("#I_want_to_get_my_property_cleaned").val();
    var Do_you_have_all_document = $("#Do_you_have_all_document").val();
    var Have_you_paid_property_tax = $("#KitcheHave_you_paid_property_taxn_Type").val();
    
    $.ajax({
        url: '/additional-information-submit',
        type: 'POST',
        data:{
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            I_want_to_get_my_property_painte : I_want_to_get_my_property_painte,
            I_want_to_get_my_property_cleaned : I_want_to_get_my_property_cleaned,
            Do_you_have_all_document : Do_you_have_all_document,
            Have_you_paid_property_tax : Have_you_paid_property_tax,
            ads_id:$(this).attr('id')
        },
        success:function(data){
            console.log(data);
            $(".content-tab-6").removeClass('visible_div');
            $(".content-tab-6").addClass('hidden');
            $(".conntent").addClass('hidden');
            $(".content-tab-6").removeClass('hidden');
            $(".content-tab-6").addClass('visible_div');        
        },
        error:function(res){
            console.log(res)
        }
    });

});


$(".Schedule_btn").click(function(){
    console.log("*** Schedule Information submit ***");
    var Availablity = $("#Availablity").val();
    var Start_Time = $("#Start_Time").val();
    var End_Time = $("#End_Time").val();
    
    $.ajax({
        url: '/Schedule-information-submit',
        type: 'POST',
        data:{
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            Availablity : Availablity,
            Start_Time : Start_Time,
            End_Time : End_Time,
            ads_id:$(this).attr('id')
        },
        success:function(data){
            console.log(data);
            $(".content-tab-7").removeClass('visible_div');
            $(".content-tab-7").addClass('hidden');
            $(".conntent").addClass('hidden');
            $(".content-tab-7").removeClass('hidden');
            $(".content-tab-7").addClass('visible_div');     
        },
        error:function(res){
            console.log(res)
        }
    });

});