odoo.define("cs_search_what_you_want.search", function(require) {
    "use strict";

    var core = require("web.core");
    var dataset = require("web.data");
    var Widget = require("web.Widget");
    var AbstractAction = require('web.AbstractAction');
    var _t = core._t;

    var search_you_want_widget = AbstractAction.extend({
        template: "SearchGrid",
        events: {
            'click .confirm_search_button': 'get_search_data',
        },

        start: function(){
            var self = this;
            self._rpc({
                        model: 'search',
                        method: 'get_models_data',
                        args: [[]],
                    })
                    .then(function(models_data) {
                        $('#select_model').select2({
                            language: "zh-CN",
                            width :"200px",  //字符串  支持固定数值和百分比
                            data: models_data,
                        });
                    })
        },

        get_search_data: function () {
            var data = $('#select_model').select2('data');
            if (data) {
                var self = this;
                self._rpc({
                        model: 'search',
                        method: 'get_search_data_html',
                        args: [[], data.id],
                    })
                    .then(function(html) {
                        var table = $('#table_search_result');
                        table[0].innerHTML = html;
                        table.DataTable();
                    })
            } else {
                alert('请选择查询的单据');
            }

        }

    });

    core.action_registry.add("search_you_want", search_you_want_widget);  /* 把视图 注册在odoo里面方便展示  */

    return search_you_want_widget;

});
