odoo.define('cs_web_x2many_checkbox.relational_fields', function (require) {
"use strict";

var FieldX2Many = require('web.relational_fields').FieldX2Many;
var ListRenderer = require('web.ListRenderer');
var BasicController = require('web.BasicController');
var data_manager = require('web.data_manager');
var Sidebar = require('web.Sidebar');
var core = require('web.core');
var qweb = core.qweb;
var SearchPanel = require('web.SearchPanel');

ListRenderer.include({
    init: function (parent, state, params) {
        this._super.apply(this, arguments);
        if (parent.value && parent.value.getContext().is_abc){
            this.hasSelectors = true;
            this.withSearchPanel = true;
        }
    },
});

FieldX2Many.include({

    init: function (parent, name, record, options) {
        this.parent = parent;
        this.SearchPanel = SearchPanel;
        this._super.apply(this, arguments);
    },


    _createSearchPanel: async function (parent, params) {
        var spParams = _.extend({}, this.searchPanelParams, {
            classes: params.classes || [],
        });
        var searchPanel = new this.SearchPanel(parent, spParams);
        await searchPanel.appendTo(self.$el);
        return searchPanel;
    },

});

});
