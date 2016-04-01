drop table Person;
create table `Person`(`Id` int ,`email` varchar(255));
insert into `Person` (Id,email) values (2,'john@example.com');
insert into `Person` (Id,email) values (3,'bob@example.com');
insert into `Person` (Id,email) values (1,'john@example.com');

delete from Person where Id not in (select * from (select min(Id) from Person group by email) tbltmp);

