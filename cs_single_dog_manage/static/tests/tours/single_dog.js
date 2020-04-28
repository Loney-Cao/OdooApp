odoo.define('single_dog_tour_test', function(require) {
    "use strict";

    var core = require('web.core');
    var tour = require('web_tour.tour');

    var _t = core._t;

    tour.register('single_dog_tour_test', {
        test: true,
        url: "/web",
    },[
        {
            trigger: '.o_app[data-menu-xmlid="cs_single_dog_manage.single_dog_manage_root_menu"]',
            content: '进入系统',
            run: 'click',
        },
        {
            trigger: '.o_list_button_add',
            content: '创建记录',
            run: 'click',
        },
        {
            trigger: 'input[name="name"]',
            content: '单身狗名字',
            run: 'text 小明',
        },
        {
            trigger: '.o_form_button_save',
            content: '保存单据',
            run: 'click',
        },
        {
            trigger: '.o_form_button_edit',
            content: 'wait the save',
            run: function(){},
        },
        // {
        //     trigger: 'button[name="action_test"]',
        //     content: '测试按钮',
        //     run: 'click',
        //     // run: function(){
        //     //     $('button[name="action_test"]').click();

        //     //     var $button = $('.o_dialog_error > button');
        //     //     if($button.length) {
        //     //             $button.click();
        //     //             var $error = $button.next();
        //     //             $error.scrollTo($error.children('pre').last().height());
        //     //             console.error('出错');
        //     //         }
                
        //     // },
        // },
        // {
        //     trigger: '.o_form_button_edit',
        //     extra_trigger: '.o_dialog_error',
        //     content: '检查错误',
        //     auto: true,
        //     run: function (actions){
                
        //         var $button = $('.o_dialog_error > button');
        //         if($button.length) {
        //                 $button.click();
        //                 var $error = $button.next();
        //                 $error.scrollTo($error.children('pre').last().height());
        //                 console.error('出错');
        //             }
        //     },
        // },
        

    ]);

});
