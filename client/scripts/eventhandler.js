(function()
{
    "use strict";
    
    var cbt =
    {
    	"loggedin": function(message)
    	{
    		W.Username = message.user;
    		W.Userid = message.uid;
    		W.GamePage.Show();
    	},
    	
    	"look": function(message)
    	{
    		W.GamePage.LookEvent(message);
    	},

    	"actions": function(message)
    	{
    		W.GamePage.ActionsEvent(message);
    	},
    	
    	"arrived": function(message)
    	{
    		W.GamePage.ArrivedEvent(message);
    	},
    	
    	"departed": function(message)
    	{
    		W.GamePage.DepartedEvent(message);
    	},
    	
    	"moved": function(message)
    	{
    		W.GamePage.MovedEvent(message);
    	},
    	
    	"speech": function(message)
    	{
    		W.GamePage.SpeechEvent(message);
    	},
    	
    	"activity": function(message)
    	{
    		W.GamePage.ActivityEvent(message);
    	},
    	
    	"realms": function(message)
    	{
    		W.GamePage.RealmsEvent(message);
    	},
    	
    	"authfailed": function(message)
    	{
    		W.LoginPage.AuthenticationFailedEvent(message);
    	},
    	
    	"creationfailed": function(message)
    	{
    		W.RegisterPage.CreationFailedEvent(message);
    	},
    	
    	"error": function(message)
    	{
			W.GamePage.ErrorEvent(message);
    	},

    	"changepasswordresult": function(message)
    	{
			W.GamePage.ChangePasswordResultEvent(message);
    	},

    	"roomdata": function(message)
    	{
    	    W.GamePage.RoomDataEvent(message);
    	},

    	"scriptcompilationfailure": function(message)
    	{
    	    W.GamePage.ScriptCompilationFailureEvent(message);
    	},

    	"roomchanged": function(message)
    	{
    	    W.RoomEditor.RoomChangedEvent(message);
    	}
    };
    
    W.OnMessageReceived = function(s)
    {
    	var messagetype = s.event;
    	if (!messagetype)
    		return;
		console.log("<message ", messagetype, ": ", $.toJSON(s));
    	var handler = cbt[messagetype];
    	if (!handler)
    	{
    		console.log("unrecognised message type!"); 
    		return;
    	}
    	
    	handler(s);
    };
}
)();
