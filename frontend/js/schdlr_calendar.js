$(document).ready(function() {

    // page is now ready, initialize the calendar...

    $('#calendar').fullCalendar({
        dayClick: function() {
            alert('a day has been clicked!');
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

    var x = getData() ;
   $('#calendar').fullCalendar( 'renderEvent', x);






});