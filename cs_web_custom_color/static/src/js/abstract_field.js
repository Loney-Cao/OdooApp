odoo.define('web_custom_color.AbstractField', function (require) {
"use strict";

var AbstractField = require('web.AbstractField');
var ColorpickerDialog = require('web.ColorpickerDialog');
require("web.zoomodoo");

AbstractField.include({

    _onMyColorClick: function () {
        if (this.mode === 'readonly') {
            var self = this;
            var defaultColor = self.attrs.bg_color || '#fcfcfc' ;
            const dialog = new ColorpickerDialog(self, {
                defaultColor: defaultColor,
                noTransparency: true,
            }).open();
            dialog.on('colorpicker:saved', self, function (ev) {
                self.attrs.bg_color = ev.data.hex;
                self.$el.css('background-color', ev.data.hex);
            });
        }
    },

    start: function () {
        var self = this;
        self.$el.on('click', self._onMyColorClick.bind(self));
        return this._super.apply(this, arguments);
    },

    _render: function () {
        this.$el.css('background-color', this.attrs.bg_color || '#fcfcfc');
        return this._super.apply(this, arguments);
    },

});

});
