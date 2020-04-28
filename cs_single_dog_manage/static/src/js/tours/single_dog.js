odoo.define('single_dog.tour', function(require) {
"use strict";

var core = require('web.core');
var tour = require('web_tour.tour');

var _t = core._t;

tour.register('single_dog_tour', {
    url: "/web",
    }, [tour.STEPS.SHOW_APPS_MENU_ITEM, 
        {
            trigger: '.o_app[data-menu-xmlid="cs_single_dog_manage.single_dog_manage_root_menu"]',
            content: _t('单身狗，戳我，快来吧。'),
            position: 'right',
            edition: 'community'
        }, {
            trigger: '.o_app[data-menu-xmlid="cs_single_dog_manage.single_dog_manage_root_menu"]',
            content: _t('单身狗，戳我，快来吧。'),
            position: 'bottom',
            edition: 'enterprise'
        }, {
            trigger: '.o_list_button_add',
            content: _t('快来创建你的信息'),
            position: 'bottom',
        }, {
            trigger: 'input[name="name"]',
            content: _t('单身狗大名🐶'),
            position: 'right',
        }, {
            trigger: '.o_form_button_save',
            content: '保存信息，开撩吧！',
            position: 'bottom',
        },
    ]);

});
