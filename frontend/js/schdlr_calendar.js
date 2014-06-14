$(document).ready(function() {

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

    //var getData = function(){
    //    return [{
    //        events: [
    //            {
    //                title: 'Event1',
    //                start: '2014-06-13'
    //            },
    //            {
    //                title: 'Event2',
    //                start: '2014-06-14'
    //            }
    //        ],
    //        color: 'yellow',
    //        textColor: 'black'
    //    }]
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



    //$(".filter-btn").on("click", function(){
    //   getAllCalendarEventsForReal();
    //});

	$('#calendar').fullCalendar({
		header: {
			left: 'prev,next today',
			center: 'title',
			right: 'month,agendaWeek,agendaDay'
		},
		defaultDate: '2014-06-14',
		editable: true,
		events: {
			url: 'http://localhost:8000/calendarevent/',
			error: function() {
				$('#script-warning').show();
			}
		},
		loading: function(bool) {
			$('#loading').toggle(bool);
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
