$(document).ready(function() {

    // page is now ready, initialize the calendar...

    var getDataForReal = function(){
        $().get()
    }


    $('#calendar').fullCalendar({
        dayClick: function() {
            $('#AddNewEventModal').modal('show');
             
            //alert('a day has been clicked!');
        }
    });


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






});