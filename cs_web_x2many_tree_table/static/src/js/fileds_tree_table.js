odoo.define('cs_web_x2many_tree_table.fields_tree_table', function (require) {
"use strict";

var FieldX2Many = require('web.relational_fields').FieldX2Many;
var AbstractField = require('web.AbstractField');
var registry = require('web.field_registry');
var core = require('web.core');
var qweb = core.qweb;

var fields_tree_table = FieldX2Many.extend({
    specialData: "_fetchSpecialRelation",
    supportedFieldTypes: ['one2many', 'many2many'],

    init: function (parent, name, record, options) {
        var self = this;
        this.insTb = undefined;  // treetable实例
        this.tableData = [];  // treetable数据
        this.tableOptions = {};  // treetable 参数
        this.cols = [];  // 列
        this.timeFields = [];
        this._super.apply(this, arguments);
        this.x2mValues = this.record.specialData[this.name];
    },

    _onChange: function () {
        console.log('变化了');
    },

    get_edit: function(field_obj) {  // 获取当前列的编辑类型

        if (this.mode !== 'edit') {
            return
        }
        if (field_obj.type === 'float' || field_obj.type === 'integer') {
            return 'number'
        } else {
            return 'text'
        }
    },

    get_templet: function(field_obj, field_name) {  // 获取当前列的编辑类型

        if (this.mode !== 'edit') {
            return
        }
        var util = layui.util;
        if (field_obj.type === 'date' || field_obj.type === 'datetime'){
            var dateType = field_obj.type === 'date' ? 'yyyy-MM-dd' : 'yyyy-MM-dd hh:mm:ss';
            return function (d) {
                return '<div lay-date="' + d.id + '">' + util.toDateString(d[field_name], 'yyyy-MM-dd') + '</div>';
            }
        }
    },

    set_cols: function() {  // 设置列
        /** col 参数
         *  参数	     类型	 说明	                        示例值
            field	    String	设定字段名	                    'username'
            title	    String	设定标题名称	                用户名
            width	    Number	设定列宽，若不填写，则自动分配	 150、20%(数字和百分比)
            minWidth	Number	单元格的最小宽度	            100(数字)
            type	    String	设定列类型	                    checkbox复选框、radio单选框、numbers序号列、space空列
            edit	    String	单元格编辑类型	                text（输入框）、number(数字输入框)
            style	    String	自定义单元格样式	            color: red;
            class	    String	自定义单元格class	            class: 'pd-tb-0';
            align	    String	单元格排列方式	                center居中、right居右
            templet	    String	自定义列模板	                详见自定义列模板
            toolbar	    String	绑定工具条模板	                详见行工具事件
            singleLine	Boolean	是否单行显示，溢出悬浮展开	     true/false
        */
        var self = this;
        var X2M_allFields = this.value.fields;  // X2M字段对应模型的所有字段
        var fieldsInfo = this.value.fieldsInfo.list;  //fieldsInfo
        this.cols = [{type: 'numbers', title: '序号', width:60}, {type: 'checkbox'}]
        for (var field in fieldsInfo) {
            
            var fieldOption = {};
            if (field.fieldOption) {
                fieldOption = eval('(' + field.fieldOption + ')');;  // xml视图中字段设置的option
            }

            var field_obj = X2M_allFields[field]; // 字段对象
            if (field_obj.type === 'date' || field_obj.type === 'datetime'){
                this.timeFields.push(field);
                fieldOption.class = 'lay-field-date';
                
            } else if (field.type === 'm2o' || field.type === 'o2m' || field.type === 'm2m') {

            }
            
            var col_option = {
                field: field,
                title: field_obj.string,
                width: fieldOption.width,
                minWidth: fieldOption.minWidth,
                type: fieldOption.type,
                edit: this.get_edit(field_obj),
                style: fieldOption.style,
                class: fieldOption.class,
                align: fieldOption.align,
                templet: this.get_templet(field_obj, field),
                toolbar: fieldOption.toolbar,
                singleLine: fieldOption.singleLine,
            }

        
            this.cols.push(col_option);
        }

        var def = [];
        // var def = this._rpc({
        //     model: 'account.online.provider',
        //     method: 'callback_institution',
        //     args: []
        // }).then(function (result) {
        //     self.do_action(result);
        //     // self.result = result;
        // });
        
    },

    dela: function () {

    },

    set_data: function() {  // 设置数据
        var X2M_recordData = this.value.data; // X2M字段所有的数据
        for (const data of X2M_recordData) {
            for (var timeField of this.timeFields) {
                data.data[timeField] = data.data[timeField].toJSON();
            }
            if (!data.data['parent_id']) {
                data.data['parent_id'] = 0;
            } else {
                data.data['parent_id'] = data.data['parent_id'].res_id;
            }
            this.tableData.push(data.data);
        }
    },

    set_tree: function() {  // 设置tree 
        var treeOption = {};
        if (this.attrs.treeOption) {
            treeOption = eval('(' + this.attrs.treeOption + ')');
        }
        this.tableOptions = {
            elem: '#FieldsTreeTable',
            table_node: this.$el,
            data: this.tableData,
            tree: {
                iconIndex: treeOption.iconIndex ? treeOption.iconIndex:2,  // 折叠图标显示在第几列
                isPidData: true,  // 是否是pid形式数据
                pidName: treeOption.pidName ? treeOption.pidName :'parent_id', //设定pid的字段名,自定义标识是否还有子节点的字段名称
                idName: treeOption.idName ? treeOption.idName :'id',  // 自定义id字段的名称
            },
            cols: this.cols,
            style: treeOption.style ? treeOption.style :'margin-top:0;',
            done: function () {
                //关闭加载
                layer.closeAll('loading');
            }

        }
    },

    willStart: function() {  // 获取相关参数以及数据
        var self = this;
        var recordData = this.recordData;  // 当前页面的记录数据 
        var X2M_fieldName = this.name;  // 当前X2M字段名  this.name
        this.set_cols();
        this.set_data();
        var def = [];
        // var def = this._rpc({
        //     model: 'account.online.provider',
        //     method: 'callback_institution',
        //     args: []
        // }).then(function (result) {
        //     self.do_action(result);
        //     // self.result = result;
        // });
        return Promise.all([this._super.apply(this, arguments), def]);
    },


    start: function () {
        var self = this;
        return this._super.apply(this, arguments).then(function () {    
            self.set_tree();
            self.render_table();
        });
    },

    _render: function () {
        this.$table = $(qweb.render('fields_tree_table'));
        this.$el.html(this.$table);
    },


    render_table: function () {  // 渲染tree table
        var self = this;
        layui.use(['layer', 'util', 'laydate', 'form', 'treeTable'], function () {
            var $ = layui.jquery;
            var layer = layui.layer;
            var util = layui.util;
            var laydate = layui.laydate;
            var form = layui.form;
            self.treeTable = layui.treeTable;
            // 渲染表格
            self.insTb = self.treeTable.render(self.tableOptions);

            // 渲染laydate
            function renderLayDate() {
                console.log(self.$el.find('[lay-date]'));
                self.$el.find('[lay-date]').each(function () {
                    laydate.render({
                        elem: this,
                        trigger: 'click',
                        done: function (value, date, endDate) {
                            var id = $(this.elem).attr('lay-date');
                            layer.msg('日期' + value + '，当前行ID：' + id);
                        }
                    });
                });
            }

            renderLayDate();
            
            // 监听单元格编辑事件
            self.treeTable.on('edit(FieldsTreeTable)', function (obj) {
                console.log('监听单元格编辑事件');
                layer.msg('修改了字段，当前行ID：' + obj.data.id);
            });

            // 监听复选框选择
            self.treeTable.on('checkbox(FieldsTreeTable)', function(obj){
                console.log('监听复选框选择');
                console.log(obj.checked);  // 当前是否选中状态
                console.log(obj.data);  // 选中行的相关数据
                console.log(obj.type);  // 如果触发的是全选，则为：all，如果触发的是单选，则为：one
            });

            // 监听行单击事件
            self.treeTable.on('row(FieldsTreeTable)', function(obj){
                console.log('监听行单击事件');
                console.log(obj.tr); //得到当前行元素对象
                console.log(obj.data); //得到当前行数据
                // obj.del(); // 删除当前行
                // obj.update(fields) // 修改当前行数据
            });
            
            // 监听行双击事件
            self.treeTable.on('rowDouble(FieldsTreeTable)', function(obj){
                console.log('监听行双击事件');
                // obj 同上
            });

            // 监听单元格单击事件
            self.treeTable.on('cell(FieldsTreeTable)', function(obj){
                console.log('监听单元格单击事件');
                console.log(obj.field); //当前单元格的字段名
                console.log(obj.data); // 得到当前行数据
            });
            
            // 监听单元格双击事件
            self.treeTable.on('cellDouble(FieldsTreeTable)', function(obj){
                console.log('监听单元格双击事件');
                // obj 同上
            });
        });
    },

});

registry.add('fields_tree_table', fields_tree_table);

return fields_tree_table;

});
