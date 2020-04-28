odoo.define('cs_web_graph_zoom_pan.GraphView', function (require) {
"use strict";

var GraphView = require('web.GraphView');


GraphView.include({

    init: function (viewInfo, params) {
        this.jsLibs.push('/cs_web_graph_zoom_pan/static/lib/chart.js@2.9.1.js');
        this.jsLibs.push('/cs_web_graph_zoom_pan/static/lib/hammerjs@2.0.8.js');
        this.jsLibs.push('/cs_web_graph_zoom_pan/static/lib/chartjs-plugin-zoom@0.7.4.js');
        this._super.apply(this, arguments);
    },
});

});
