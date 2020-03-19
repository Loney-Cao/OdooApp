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
        // this.$el.html(this.$table);
    },


    render_table: function () {
        var self = this;
        layui.use(['layer', 'util', 'treeTable'], function () {
            var $ = layui.jquery;
            var layer = layui.layer;
            var util = layui.util;
            var treeTable = layui.treeTable;
            var data = [{
                id: "1",
                name: "xxx",
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
                }, {
                    id: "1_2",
                    name: "xxx",
                    state: 0,
                    createTime: "2019/11/18 10:44:00",
                    children: [{
                        id: "1_2_1",
                        name: "xxx",
                        state: 0,
                        createTime: "2019/11/18 10:44:00",
                        children: []
                    }, {
                        id: "1_2_2",
                        name: "xxx",
                        state: 0,
                        createTime: "2019/11/18 10:44:00",
                        children: []
                    }, {
                        id: "1_2_3",
                        name: "xxx",
                        state: 0,
                        createTime: "2019/11/18 10:44:00",
                        children: []
                    }]
                }, {
                    id: "1_3",
                    name: "xxx",
                    state: 0,
                    createTime: "2019/11/18 10:44:00",
                    children: []
                }]
                }, {
                    id: "2",
                    name: "xxx",
                    state: 0,
                    createTime: "2019/11/18 10:44:00",
                    children: [{
                        id: "2_1",
                        name: "xxx",
                        state: 0,
                        createTime: "2019/11/18 10:44:00",
                        children: [{
                            id: "2_1_1",
                            name: "xxx",
                            state: 0,
                            createTime: "2019/11/18 10:44:00",
                            children: []
                        }, {
                            id: "2_1_2",
                            name: "xxx",
                            state: 0,
                            createTime: "2019/11/18 10:44:00",
                            children: []
                        }, {
                            id: "2_1_3",
                            name: "xxx",
                            state: 0,
                            createTime: "2019/11/18 10:44:00",
                            children: []
                        }]
                    }, {
                        id: "2_2",
                        name: "xxx",
                        state: 0,
                        createTime: "2019/11/18 10:44:00",
                        children: []
                    }, {
                        id: "2_3",
                        name: "xxx",
                        state: 0,
                        createTime: "2019/11/18 10:44:00",
                        children: []
                    }]
                }, {
                    id: "3",
                    name: "xxx",
                    state: 0,
                    createTime: "2019/11/18 10:44:00",
                    children: [{
                        id: "3_1",
                        name: "xxx",
                        state: 0,
                        createTime: "2019/11/18 10:44:00",
                        children: []
                    }, {
                        id: "3_2",
                        name: "xxx",
                        state: 0,
                        createTime: "2019/11/18 10:44:00",
                        children: []
                    }, {
                        id: "3_3",
                        name: "xxx",
                        state: 0,
                        createTime: "2019/11/18 10:44:00",
                        children: []
                    }]
                }, {
                    id: "4",
                    name: "xxx",
                    state: 0,
                    createTime: "2019/11/18 10:44:00",
                    children: []
                }, {
                    id: "5",
                    name: "xxx",
                    state: 0,
                    createTime: "2019/11/18 10:44:00",
                    children: []
                }
            ];
            // 渲染表格
            var insTb = treeTable.render({
                elem: '#FieldsTreeTable',
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
                    {title: '状态', width: 100},
                    {align: 'center', title: '操作', width: 120}
                ],
                style: 'margin-top:0;',

                done: function () {
                    //关闭加载
                    layer.closeAll('loading');
                }
    
            });
            self.insTb = insTb;

            treeTable.on('tool(FieldsTreeTable)', function (obj) {
                var event = obj.event;
                if (event == 'del') {
                    layer.msg('点击了删除', {icon: 1});
                } else if (event == 'edit') {
                    layer.msg('点击了修改', {icon: 1});
                    obj.update({name: 'newname'});
                }
            });
    
        });
    },

});

registry.add('fields_tree_table', fields_tree_table);

return fields_tree_table;

});
