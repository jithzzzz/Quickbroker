$("#login-submit").click(function(){
    console.log("*** Admin Login ***");
    var login_email = $("#login-email").val();
    var login_password =  $("#login-password").val();
    $.ajax({
        url: '/admin-login',
        type: 'POST',
        data:{
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            login_email:login_email,
            login_password:login_password
        },
        success:function(data){
            console.log(data);
            if(data == 'Error')
            {

            }
            else if(data == 'login')
            {

            }
            else
            {
                window.location.href = "http://127.0.0.1:8005/Dashboard";
            }
            
        },
        error:function(res){
            console.log(res)
        }
    });
})