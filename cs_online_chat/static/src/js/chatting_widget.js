odoo.define("cs_online_chat.chatting", function(require) {
    "use strict";

    var core = require("web.core");
    var dataset = require("web.data");
    var Widget = require("web.Widget");
    var AbstractAction = require('web.AbstractAction');
    var _t = core._t;

    var Chatting = AbstractAction.extend({
        template: "Chatting",
        events: {
            'click #send_message': 'sendMsg',
        },

        start: function(){
            var uid = this.controlPanelParams.context.uid;
            this.ws = new WebSocket("ws://127.0.0.1:2222/chat?" + "&uid="+ uid);
            this.ws.onmessage = function(e) {
                $("#contents").append("<p>" + e.data + "</p>");
            };
        },
        sendMsg: function () {
            // var uid = this.controlPanelParams.context.uid;
            var msg = $("#msg").val();
            this.ws.send(msg);
            $("#msg").val("");
        }
    });

    core.action_registry.add("chatting", Chatting);  /* 把视图 注册在odoo里面方便展示  */

    return Chatting;

});
