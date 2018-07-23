
console.log("JS FUNCTION.......")

var wsbroker = "192.168.43.33";  //mqtt websocket enabled broker
var wsport = 9001; // port for above
var obj;
var client = new Paho.MQTT.Client(wsbroker, wsport,
"myclientid_" + parseInt(Math.random() * 100, 10));

client.onConnectionLost = function (responseObject) {
	console.log("connection lost: " + responseObject.errorMessage);
};		    
var options = {
		timeout: 3,
		onSuccess: function () {
		console.log("mqtt connected");

		client.subscribe('bT-App', {qos: 1});

		},

		onFailure: function (message) {
		console.log("Connection failed: " + message.errorMessage);
		}
};          

client.onMessageArrived = function (message) {
		console.log(message.destinationName, ' -- ', message.payloadString);
		var obj = JSON.parse(message.payloadString);
		console.log(obj);


		if (obj["subtype"] == "busCount"){

			var totalbusNumber = 4;
			var addedvalue = (obj['Message']['inCount']+obj['Message']['outCount']);
			var unused = totalbusNumber - addedvalue;

			var t = $('#dataTables1-example').DataTable();

			$("#col0").html(totalbusNumber);
			$("#col1").html(obj['Message']['inCount']);
			$("#col2").html(obj['Message']['outCount']);
			$("#col3").html(unused);
		
        // t.row.add( [
        //     totalbusNumber,
        //     obj['Message']['inCount'],
        //     obj['Message']['outCount'],
        //     unused
        // ]).draw( false );



        }

        // bus wise and day wise stats will go here.

        if (obj["subtype"] == "dayWiseStats"){

	        var t = $('#dataTables2-example').DataTable();
	        t.clear();
	        // t.row.add( [
		       //  	null,	
		       //      null,
		       //      null,
		       //      null,
		       //      ]).draw( false );

	        var s_no = 0;

	        console.log(Object.keys(obj["Message"]));

	        var messageKeys = Object.keys(obj["Message"]);

	        for (i=0; i<messageKeys.length;i++){
	        	
	        	var mesg = obj["Message"][messageKeys[i]];	
	        	
	        	for (j=0;j<mesg.length;j++){
	        		s_no=s_no+1;

	    //     		$("#col00").html(s_no);
					// $("#col01").html(messageKeys[i]);
					// $("#col02").html(mesg[j][0]);
					// $("#col03").html(mesg[j][1]);	        		
		        	
		        	t.row.add( [
		        	s_no,	
		            messageKeys[i],
		            mesg[j][0],
		            mesg[j][1],
		            ]).draw( false );
		


	        	}
	        		
	        		

	        }
	        

        }


};
