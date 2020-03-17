odoo.define('cs_web_x2many_tree_table.fields_tree_table', function (require) {
"use strict";

var FieldX2Many = require('web.relational_fields').FieldX2Many;

var registry = require('web.field_registry');

var fields_tree_table = FieldX2Many.extend({
    var load_layui = function () {
        layui.config({
            base: '../lib/'
        }).extend({
            treeTable: 'treeTable/treeTable'
        }).use(['layer', 'util', 'treeTable'], function () {
            var $ = layui.jquery;
            var layer = layui.layer;
            var util = layui.util;
            var treeTable = layui.treeTable;
            var data = [];
            // 渲染表格
            var insTb = treeTable.render({
                elem: '#demoTreeTable1',
                data: data,
                tree: {
                    iconIndex: 2
                },
                cols: [
                    {type: 'numbers'},
                    {type: 'checkbox'},
                    {field: 'id', title: 'ID'},
                    {field: 'name', title: 'name', width: 160},
                    {
                        field: 'createTime', title: '创建时间', templet: function (d) {
                            return util.toDateString(d.createTime);
                        }, width: 180
                    },
                    {templet: '#demoTreeTableState1', title: '状态', width: 100},
                    {align: 'center', toolbar: '#demoTreeTableBar1', title: '操作', width: 120}
                ],
                style: 'margin-top:0;'
            });
    
        });
    }

});

registry.add('fields_tree_table', fields_tree_table);

return fields_tree_table;

});
