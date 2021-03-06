//var host = "http://localhost"
var host = "http://162.243.62.74";
var port = "8000";
var baseCalendarUrl = host + ':'+port+'/calendarevent/';
var baseLocationsUrl = host + ':'+port+'/location/';
var baseDisciplinesUrl = host + ':'+port+'/discipline/';
var baseEventDetailsUrl = host + ':'+port+'/event/';

$(document).ready(function() {
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
		},
        dayClick: function() {
            $('#AddNewEventModal').modal('show');
        },
        eventClick: function(calEvent, jsEvent, view) {

//        alert('Event: ' + calEvent.title);
//        alert('Coordinates: ' + jsEvent.pageX + ',' + jsEvent.pageY);
//        alert('View: ' + view.name);
        
            console.log(calEvent);
            $('#AddNewEventModal').modal('show');
            getEventDetails(calEvent);
        }
	});

	$.get(baseLocationsUrl, function(data) {
		var select = $('#location').empty();
		console.log(data);
		$.each(data, function(i, item){
			select.append("<option value='" + item.id + "'>" + item.location_name + "</option>");
		});
	}, 'json');    

	$.get(baseDisciplinesUrl, function(data) {
		var select = $('#discipline').empty();
		console.log(data);
		$.each(data, function(i, item){
			select.append("<option value='" + item.id + "'>" + item.name + "</option>");
		});
	}, 'json');    
    
    
    
    $("#add-event-btn").on("click", function(){
        $.ajax({
              type: "PUT",
              url: "/event",
              data: { event_name: "John",
                  setup_start: "Boston",
                  setup_end: "Boston",
                  event_start: "Boston",
                  event_end: "Boston",
                  teardown_start: "Boston",
                  teardown_end: "Boston",
                  needed_reasources: "Boston",
                  status: "Boston",
                  visibility: "Boston",
                  location: "Boston",
                  contact_name: "Boston",
                  contact_phone_number: "Boston",
                  contact_email: "Boston",
                  discipline: "Boston"
              }
            })
              .done(function( msg ) {
                alert( "new event created");
              });
    })
    
    
});


var getEventDetails = function(calEvent){
    var eventDetailsLink = baseEventDetailsUrl+calEvent.id+"/";
    console.log(eventDetailsLink);
    
    $.get(eventDetailsLink, function(item) {
		console.log(item);
            $("#inputEventName").val(item.event_name);
            $("#inputEventStartTime").val(item.event_start);
            $("#inputEventEndTime").val(item.event_end);
            $("#makeEventPrivate").prop('checked', true);
            $("#inputCustomerName").val(item.contact_name);
            $("#inputCustomerPhone").val(item.contact_phone_number);
            $("#inputCustomerEmailAddress").val(item.contact_email);
            $("#inputLocationId").find('option:[value='+"'room2'"+']').attr('selected',1);
	}, 'json'); 
}
