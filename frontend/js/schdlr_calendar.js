$(document).ready(function() {

    // page is now ready, initialize the calendar...

    var getAllCalendarEventsForReal = function(){
        var schdlrAPI = "http://162.243.62.74/calendarevent";
        $.getJSON( schdlrAPI, function( data ) {
            var items = [];
            $.each( data, function( key, val ) {
                alert(key + " -- " + val);
            });
          });
    }
    var getDataForReal = function(){
        var discipline = $(".discipline").val();
        var location = $(".location").val();
        var schdlrAPI = "http://162.243.62.74/calendarevent?location="+locaiton+"&discipline=" + discipline;
        $.getJSON( schdlrAPI, function( data ) {
            var items = [];
            $.each( data, function( key, val ) {
                alert(key + " -- " + val);
//              items.push( "<li id='" + key + "'>" + val + "</li>" );
            });
            
//            $( "<ul/>", {
//              "class": "my-new-list",
//              html: items.join( "" )
//            }).appendTo( "body" );
          });
    }

    var getData = function(){

        return [{
            events: [
                {
                    title: 'Event1',
                    start: '2014-06-13'
                },
                {
                    title: 'Event2',
                    start: '2014-06-14'
                }
            ],
            color: 'yellow',
            textColor: 'black'
        }]
    }
    
    
    
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        dayClick: function() {
            alert('a day has been clicked!');
        }
    });
    

    var x = getData() ;
   $('#calendar').fullCalendar( 'renderEvent', x);



    $(".filter-btn").on("click", function(){
       getAllCalendarEventsForReal(); 
    });
    

});