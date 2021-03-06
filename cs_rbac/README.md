# RBAC

## 表结构

角色组表
角色表
菜单权限控制表
规则表

角色表：

| 角色名称  | 用户组（M2O）|  是否启用 |  菜单权限控制（O2M）|  用户（O2M）|

菜单权限控制：

|===========|========|========|  模型        +        R/W/C/U      ----->    访问权限           |========================================|
|===========|========|========|  模型        +        R/W/C/U        +        规则   ----->      记录规则    |=============================|
| 菜单（M2O）| 菜单显隐 | 菜单动作| 菜单模型 | perm_read | perm_write | perm_create  | perm_unlink  | 规则（O2M）| 访问权限（M2O）| 记录规则（O2M）|

规则表：

| 规则名称 |  domain_force |

## 操作

角色：
    1.后台创建一个用户组并与之绑定关系。
    2.用户添加到对应的用户组。
    3.菜单权限控制
        1.创建访问权限（ir.model.access） 和 记录规则 (ir.rule)，并与菜单权限控制绑定关系。
        2.将访问权限和记录规则添加到用户组。
        3.最底级菜单才能选择R/W/C/U，并且 菜单隐藏 为显示。
        4.除了最底级菜单，其余父菜单只能控制显示隐藏。R/W/C/U/规则/ 只读。
    4.是否启用：
        1.启用：将用户添加到用户组。
        2.不启用：将用户从用户组移除。
