create database Hotelmsys;
use Hotelmsys;
show tables;
select * from hmsapp_bookorder;
desc hmsapp_bookorder;
desc hmsapp_menu;
select * from hmsapp_menu;
delete from hmsapp_menu where id=1;
select * from auth_user;
select * from auth_permission;
select * from auth_user_user_permissions;
show tables;
select * from auth_group;
select * from auth_group_permissions;
select * from auth_user_groups;
truncate table hmsapp_bookorder;
select * from hmsapp_bookorder;
select * from django_session;
truncate table django_session;