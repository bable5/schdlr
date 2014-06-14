$(document).ready(function() {
    var baseCalendarUrl = 'http://localhost:8000/calendarevent/';

    //function getAllCalendarEventsForReal(){
    //    var schdlrAPI = "http://162.243.62.74/calendarevent";
    //    $.getJSON( schdlrAPI, function( data ) {
    //        var items = [];
    //        $.each( data, function( key, val ) {
    //            alert(key + " -- " + val);
    //        });
    //      });
    //}
    //function getDataForReal(){
    //    var discipline = $(".discipline").val();
    //    var location = $(".location").val();
    //    var schdlrAPI = "http://localhost:8000/calendarevent/?location="+locaiton+"&discipline=" + discipline;
    //    $.getJSON( schdlrAPI, function( data ) {
    //        var items = [];
//  //          $( "<ul/>", {
//  //            "class": "my-new-list",
//  //            html: items.join( "" )
//  //          }).appendTo( "body" );
    //      });
    //}

    
    
    
    //$('#calendar').fullCalendar({
    //    header: {
    //        left: 'prev,next today',
    //        center: 'title',
    //        right: 'month,agendaWeek,agendaDay'
    //    },
    //    dayClick: function() {
    //        alert('a day has been clicked!');
    //    }
    //});
    

   // var x = getData() ;
   //$('#calendar').fullCalendar( 'renderEvent', x);

    getSelectLocationIDs = function () {
        ids = new Array();

        $( 'select option:selected' ).each(function() {
          ids.push( $(this).attr('value') );
        });
        return ids;
    };

    filterCalendarByLocation = function(locationIds) {
        var eventUrl;
        if (locationIds.length === 0) {
            eventUrl = baseCalendarUrl;
        } else {
            eventUrl = baseCalendarUrl.substr(0, baseCalendarUrl.length-1) + '?location='
            $(locationIds).each(function() {
                eventUrl += this + ',';
            });

            // trim the last comma
            eventUrl = eventUrl.substr(0, eventUrl.length - 1);
        }
        return eventUrl;
    }

    updateEventSource = function(eventSource) {
        var cal = $('#calendar');
        cal.fullCalendar('removeEvents');
        cal.fullCalendar('addEventSource', eventSource);
    }

    $("#locations").submit(function(event){
        event.preventDefault();
        ids = getSelectLocationIDs();
        var eventSource = filterCalendarByLocation(ids);
        updateEventSource(eventSource);
    });

	$('#calendar').fullCalendar({
		header: {
			left: 'prev,next today',
			center: 'title',
			right: 'month,agendaWeek,agendaDay'
		},
		defaultDate: '2014-06-14',
		editable: false,
		events: {
			url: baseCalendarUrl,
			error: function() {
				$('#script-warning').show();
			}
		},
		loading: function(bool) {
			$('#loading').toggle(bool);
		},
		eventRender: function(event, el) {
			if (event.start.hasZone()) {
				el.find('.fc-event-title').after(
					$('<div class="" style="margin-left: 10px;"/>').text("("+event.location_name+")")
				);
			}
		}
	});

	$.get('http://localhost:8000/location/', function(data) {
		var select = $('#location').empty();
		console.log(data);
		$.each(data, function(i, item){
			select.append("<option value='" + item.id + "'>" + item.location_name + "</option>");
		});
		
	}, 'json');

});
