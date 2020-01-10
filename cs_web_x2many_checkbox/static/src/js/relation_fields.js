odoo.define('cs_web_x2many_checkbox.relational_fields', function (require) {
"use strict";

var FieldX2Many = require('web.relational_fields').FieldX2Many;
var ListRenderer = require('web.ListRenderer');
var BasicController = require('web.BasicController');
var data_manager = require('web.data_manager');
var Sidebar = require('web.Sidebar');
var core = require('web.core');
var qweb = core.qweb;

BasicController.include({
    _onSidebarDataAsked: function (ev) {
        var sidebarEnv = this._getSidebarEnv();
        var env = ev.target.env;
        if (env.context.is_abc) {
            sidebarEnv = env;
        }
        ev.data.callback(sidebarEnv);
    },
});

ListRenderer.include({
    init: function (parent, state, params) {
        this._super.apply(this, arguments);
        if (parent.value && parent.value.getContext().is_abc){
            this.hasSelectors = true;
        }
    },
});

FieldX2Many.include({

    events: _.extend({}, FieldX2Many.prototype.events, {
        'click button.o_button_import': '_bindImport',
    }),

    custom_events: _.extend({}, FieldX2Many.prototype.custom_events, {
        selection_changed: '_onSelectionChanged',
    }),

    init: function (parent, name, record, options) {
        this.selectedRecords = [];  // 选择的记录 初始为 []
        this.sidebar = null;  // sidebar 初始为null
        this._super.apply(this, arguments);
    },

    _render: function () {
        var self = this;
        var result = self._super.apply(this, arguments);
        if (self.value.getContext().is_abc){
            var model = self.field.relation;
            data_manager.
            load_views({'model': model, 'views_descr':[[false, 'list']]}, {'toolbar': true}).
            then(function (result) {
                var toolbar = result.list.toolbar;
                self.sidebar = new Sidebar(self, {
                    env: self._getSidebarEnv(),
                    actions: toolbar,
                });
                var $node = $('<div style="text-align:center;margin-bottom:10px;">');
                var $buttons = $(qweb.render('ImportView.import_button', {widget: {importEnabled: true}}));
                $buttons.appendTo($node);
                self.sidebar.appendTo($node).then(function() {
                    self._toggleSidebar();
                });
                self.$el.prepend($node);
            });
        }
        return result;
    },

    _toggleSidebar: function () {
        if (this.sidebar) {
            this.sidebar.do_toggle(this.selectedRecords.length > 0);
        }
    },

    _onSelectionChanged: function (ev) {
        this.selectedRecords = ev.data.selection;
        this._updateEnv();
        this._toggleSidebar();
    },

    getSelectedIds: function () {
        var self = this;
        var selected_ids = [];
        self.value.data.forEach(record=>{
            if(self.selectedRecords.indexOf(record.id) > -1) {
                selected_ids.push(record.res_id);
            }
        });
        return selected_ids;
    },

    _getSidebarEnv: function () {
        return {
            context: this.value.getContext(),
            activeIds: this.getSelectedIds(),
            model: this.field.relation,
        };
    },

    _updateEnv: function () {
        if (this.sidebar) {
            var sidebarEnv = this._getSidebarEnv();
            this.sidebar.updateEnv(sidebarEnv);
            console.log(this.sidebar.env)
        }
    },

    _bindImport: function () {
        var self = this;
        self.do_action({
            type: 'ir.actions.client',
            tag: 'import',
            params: {
                model: self.field.relation,
                context: self.value.getContext(),
            }
        });
    }
});

});
