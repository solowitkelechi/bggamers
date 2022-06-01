$(document).ready(function(){
    $("#addgame").submit(function(e){
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/addgame/",
            headers: {
                'X-CSRFToken': document.getElementById('csrf').querySelector('input').value
            },
            data: $(this).serialize(),
            dataType: 'json',
            success: function(response){
                $("#gameFormErrors").append("<span>Game added successfully.</span>")
                $("#gameFormErrors").show()
            },
            error: function (response){
                if (response["responseJSON"]["error"] !== "failed"){
                    response["responseJSON"]["error"]["__all__"].forEach(function(element){
                        $("#gameFormErrors").append("<span>"+element+"</span>")
                        $("#gameFormErrors").show()
                    });
                }
            }
        });
    })
    $("#closeGameErrors").click(function(){
        $("#gameFormErrors").hide()
        $('#gameFormErrors').children().not("#closeGameErrors").remove();
    })

    $("#addwinners").submit(function(e){
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/addwinners/",
            headers: {
                'X-CSRFToken': document.getElementById('csrf').querySelector('input').value
            },
            data: $(this).serialize(),
            dataType: 'json',
            success: function(response){
                $("#winnerFormErrors").append("<span>Player added to the winners list.</span>")
                $("#winnerFormErrors").show()
            },
            error: function (response){
                if (response["responseJSON"]["error"] === "failed"){
                    $("#winnerFormErrors").append("<span>Player already in this game's winner list</span>")
                    $("#winnerFormErrors").show()
                }
                if (response["responseJSON"]["error"] !== "failed"){
                    response["responseJSON"]["error"]["__all__"].forEach(function(element){
                        $("#winnerFormErrors").append("<span>"+element+"</span>")
                        $("#winnerFormErrors").show()
                    });
                }
            }
        });
    })
    $("#closeWinnerErrors").click(function(){
        $("#winnerFormErrors").hide()
        $('#winnerFormErrors').children().not("#closeWinnerErrors").remove();
    })

    $("#addplayer").submit(function(e){
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/addplayer/",
            headers: {
                'X-CSRFToken': document.getElementById('csrf').querySelector('input').value
            },
            data: $(this).serialize(),
            dataType: 'json',
            success: function(response){
                $("#playerFormErrors").append("<span>Discord Id added successfully.</span>")
                $("#playerFormErrors").show()
            },
            error: function (response){
                if (response["responseJSON"]["error"] === "failed"){
                    $("#playerFormErrors").append("<span>Discord Id already exist.</span>")
                    $("#playerFormErrors").show()
                }
                if (response["responseJSON"]["error"] !== "failed"){
                    response["responseJSON"]["error"]["__all__"].forEach(function(element){
                        $("#playerFormErrors").append("<span>"+element+"</span>")
                        $("#playerFormErrors").show()
                    });
                }
            }
        });
    })
    $("#closePlayerErrors").click(function(){
        $("#playerFormErrors").hide()
        $('#playerFormErrors').children().not("#closePlayerErrors").remove();
    })

    $("#playerstogame").submit(function(e){
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/playerstogame/",
            headers: {
                'X-CSRFToken': document.getElementById('csrf').querySelector('input').value
            },
            data: {
                "gameid": $("#game").val(),
                "players": $("#players").val().toString(),
            },
            dataType: 'json',
            success: function(response){
                $("#pgFormErrors").append("<span>player(s) added successfully.</span>")
                $("#pgFormErrors").show()
            },
            error: function (response){
                $("#pgFormErrors").append("<span>Error adding player(s)</span>")
                $("#pgFormErrors").show()
            }
        })
    })
    $("#closePgErrors").click(function(){
        $("#pgFormErrors").hide()
        $('#pgFormErrors').children().not("#closePgErrors").remove();
    })
})