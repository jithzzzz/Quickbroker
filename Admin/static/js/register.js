$("#finish_processs").click(function(){
    alert("Lets");
    var name = $("#Full-Name").val();
    var email = $("#inputEmail4").val();
    var mobile = $("#Mobile-No").val();
    var gender = $("#inputgender").val();
    var password = $("#inputpassword").val();
    console.log(name);
    console.log(email);
    console.log(mobile)
    console.log(gender);
    console.log(password)

    $.ajax({
        url: '/admin-register',
        type: 'POST',
        data:{
            csrfmiddlewaretoken: window.CSRF_TOKEN,
            name:name,
            email:email,
            mobile:mobile,
            gender:gender,
            password:password
        },
        success:function(data){
            console.log(data);
            if(data == 'OK')
            {
                $("#Registration-confirmation-model").modal('show');
            }
            else
            {
                new Noty({
                    type: 'error',
                    layout: 'topRight',
                    theme: 'metroui',
                    text: data + ' 🤖',
                    timeout: '4000',
                    progressBar: true,
                    closeWith: ['click'],
                    killer: true,
     
                 }).show();
            }
        },
        error:function(res){
            console.log(res)
        }
    });

});
