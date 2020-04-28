odoo.define('cs_web_view_dynamic_dispaly_button.FormController', function (require) {
"use strict";

    var core = require('web.core');
    var _t = core._t;
    var FormController = require('web.FormController');
    FormController.include({
        /**
         * 根据表达式处理按钮 ``edit`` 和 ``create`` 的显示或隐藏
         * 在 ``<form />`` 中添加属性 ``edit_invisible="invisible"`` 或 ``create_invisible="invisible"``
         * 其中 ``invisible`` 为表达式，如 ``state=='draft'``
         * @private
         */
        _updateButtons: function () {
            this._super.apply(this, arguments);
            if (this.mode === 'readonly' && this.$buttons && this.hasButtons) {
                var self = this;
                var attrs = this.renderer.arch.attrs;
                var actions = ['edit', 'create'];
                _.each(actions, function (action) {
                    var invisible = attrs[action + '_invisible'];
                    var act_res = invisible ? self._evalActionExpr(invisible) : !self.activeActions[action];
                    self.$buttons.find('.o_form_button_' + action).toggleClass('o_hidden', act_res);
                });
            }
        },

        /**
         * 根据表达式处理按钮 ``delete`` 和 ``duplicate`` 的显示或隐藏
         * 在 ``<form />`` 中添加属性 ``delete_invisible="invisible"`` 或 ``duplicate_invisible="invisible"``
         * 其中 ``invisible`` 为表达式，如 ``state=='draft'``
         * @private
         */
        _updateSidebar: function () {
            this._super.apply(this, arguments);
            if (this.sidebar) {
                this.sidebar.do_toggle(this.mode === 'readonly');
                var self = this;
                var attrs = this.renderer.arch.attrs;
                var actions = ['delete', 'duplicate'];
                var otherItems = [];
                _.each(actions, function (action) {
                    var invisible = attrs[action + '_invisible'];
                    var act_res = invisible ? !self._evalActionExpr(invisible) : self.activeActions[action];
                    var capAct = _.string.capitalize(action);
                    var t_label = _t(capAct);
                    if (!act_res) {
                        otherItems.push(t_label)
                    }
                });
                this.sidebar.items.other = this.sidebar.items.other.filter(function(item){
                    return otherItems.indexOf(item.label) == -1
                });
            }
        },

        // 判断表达式的值
        _evalActionExpr: function (expr) {
            return py.PY_isTrue(py.evaluate(py.parse(py.tokenize(expr)), this.renderer.state.evalContext));
        }
    });
});
