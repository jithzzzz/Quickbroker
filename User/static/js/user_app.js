$(document).ready(function(){
    $("div.user_dash_search_inputs > input.serach_input").focusin(function(){
        var BHK = '<select class="serch_bhk_select"><option value="0">BHK Type</option><option value="1 BHK">1 BHK</option><option value="2 BHK">2 BHK</option><option value="3 BHK">3 BHK</option><option value="4 BHK">4 BHK</option><option value="4+ BHK">4+ BHK</option></select>';
        var propert_status = '<select class=""><option value="0">Property Status</option><option value="Under Construction">Under Construction</option><option value="Ready to Move">Ready to Move</option></select>';
        $("#addition_filter_elements").empty();

        $("#addition_filter_elements").append(BHK);
        $("#addition_filter_elements").append(propert_status);
        $("#addition_filter_elements").slideDown(1000, function() {
            $("#addition_filter_elements").css({'display':'block'})

        });
    })
    /*
     $("div.user_dash_search_inputs > input.serach_input, div#addition_filter_elements .serch_bhk_select").focusout(function(){
        $("#addition_filter_elements").slideUp(1000, function() {
            $("#addition_filter_elements").css({'display':'none'})
            $("#addition_filter_elements").empty();
        });
        
        
     });
     */
});