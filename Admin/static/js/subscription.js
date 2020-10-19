$("#submit_subscription_form").click(function(){
    console.log("** Subscription Form **")
    var plan_name = $("#plan_name").val();
    var status = $("#status").val();
    var active_time = $("#active_time").val();
    var no_post_month = $("#no_post_month").val();
    var c_25 = $("#c_25").val();
    var c_more_25 = $("#c_more_25").val();
    var c_more_50 = $("#c_more_50").val();
    var sub_price = $("#sub_price").val();
    var service_charge = $("#service_charge").val();
    var chat_support = $("#chat_support").val();
    var phone_support = $("#phone_support").val();

    $.ajax({
        url: '/submit-subscription-plan',
        type: 'POST',
        data:{
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            plan_name: plan_name,
            status: status,
            active_time: active_time,
            no_post_month: no_post_month,
            c_25: c_25,
            c_more_25: c_more_25,
            c_more_50: c_more_50,
            sub_price: sub_price,
            service_charge: service_charge,
            chat_support: chat_support,
            phone_support: phone_support
        },
        success:function(data){
            console.log(data);
            if(data.Status == true)
            {
                
            }
        },
        error:function(res){
            console.log(res)
        }
    });

});