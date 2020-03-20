odoo.define('cs_web_x2many_tree_table.fields_tree_table', function (require) {
"use strict";

var FieldX2Many = require('web.relational_fields').FieldX2Many;
var AbstractField = require('web.AbstractField');
var registry = require('web.field_registry');
var core = require('web.core');
var qweb = core.qweb;

var fields_tree_table = AbstractField.extend({
    // template: 'fields_tree_table',

    init: function (parent, name, record, options) {
        var self = this;
        this.insTb = undefined;
        var date = new Date()
        this.table_data = [{
            id: "1",
            name: date.getMilliseconds(),
            state: 0,
            createTime: "2019/11/18 10:44:00",
            children: [{
                id: "1_1",
                name: "xxx",
                state: 0,
                createTime: "2019/11/18 10:44:00",
                children: [{
                        id: "1_1_1",
                        name: "xxx",
                        state: 0,
                        createTime: "2019/11/18 10:44:00",
                        children: []
                    }, {
                        id: "1_1_2",
                        name: "xxx",
                        state: 0,
                        createTime: "2019/11/18 10:44:00",
                        children: []
                    }, {
                        id: "1_1_3",
                        name: "xxx",
                        state: 0,
                        createTime: "2019/11/18 10:44:00",
                        children: []
                    }]
                }]
            }];

        this._super.apply(this, arguments);
    },


    start: function () {
        var self = this;
        return this._super.apply(this, arguments).then(function () {
            console.log($('#FieldsTreeTable'));
            self.render_table();
        });
    },

    _render: function () {
        this.$table = $(qweb.render('fields_tree_table'));
        this.$el.html(this.$table);
    },


    render_table: function () {
        var self = this;
        this.table_options = {
            elem: '#FieldsTreeTable',
            table_node: this.$el,
            data: this.table_data,
            tree: {
                iconIndex: 2
            },
            cols: [
                {type: 'numbers'},
                {type: 'checkbox'},
                {field: 'id', title: 'ID'},
                {field: 'name', title: 'name', width: 160},
                {title: '状态', width: 100},
                {align: 'center', title: '操作', width: 120}
            ],
            style: 'margin-top:0;',

            done: function () {
                //关闭加载
                layer.closeAll('loading');
            }

        }
        layui.use(['layer', 'util', 'treeTable'], function () {
            var $ = layui.jquery;
            var layer = layui.layer;
            var util = layui.util;
            self.treeTable = layui.treeTable;
            // 渲染表格
            self.insTb = self.treeTable.render(self.table_options);
    
        });
    },

});

registry.add('fields_tree_table', fields_tree_table);

return fields_tree_table;

});
