create database data;
use data;

drop table if exists user;
create table user (
  id integer auto_increment primary key,
  username varchar(255) unique not null,
  password varchar(255) not null
);
