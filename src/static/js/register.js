$(document).ready(function(){
    // on click signup  hide the login page and show the registration page
    $("#signup").click(function(){
        $("#first").slideUp("slow",function(){
            $("#second").slideDown("slow");
        })
    });
    
    
    $("#signin").click(function(){
        $("#second").slideUp("slow",function(){
            $("#first").slideDown("slow");
        })
    })
    });
    
    var ifclicked= document.getElementById("Clicked")
    if(ifclicked){
    window.location.href = "upload_image.html";
    }