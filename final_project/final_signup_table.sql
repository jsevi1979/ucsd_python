--table will store user data entered

drop table final_signup_table
create table final_signup_table(
id integer primary key,
firstname varchar(100),
lastname varchar(100),
age int
)


--insert user data
insert into final_signup_table(firstname, lastname, age)
values('Fred','Flinstone',75);

insert into final_signup_table(firstname, lastname, age)
values('Barney','Rubble',60);

insert into final_signup_table(firstname, lastname, age)
values('Dino','Dog',30);

--check data
select *
from final_signup_table


