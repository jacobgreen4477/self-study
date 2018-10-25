#### [정리]

<br>

#### search vs match 
a = "123abc" <br>
re.match("[a-z]+",a).group() <br>

> AttributeError: 'NoneType' object has no attribute 'group'<br>

re.search("[a-z]+",a).group()<br>

> 'abc' <br>

<br>

#### 정규표현식 코마 & 마침표 두개 사용
s = '100,000.000' <br>
regex_pattern = r"[.,]"  <br>

<br>

#### itertools
product(A, B) returns the same as ((x,y) for x in A for y in B). <br>

<br>

#### MySQL
select distinct city from station where id%2=0; <br>
select count(CITY) - count(distinct CITY) from STATION; <br>
select city, length(city) from station where length(city)=(select min(length(city)) from station) order by city limit 1; <br>

> order by(defalut) is ascending <br>

select distinct city from station where lower(substr(city,1,1)) in ('a','e','i','o','u'); <br>
select distinct city from station where lower(substr(city,-1)) in ('a','e','i','o','u'); <br>
select distinct city from station where city regexp '^[aeiou].*[aeiou]$'; <br>

> first ^, last $

select distinct city from station where city regexp '^[^aeiou]'; <br>

> do not start with vowel [^] <- not의 의미 

select name from students where marks > 75 order by right(name,3), id asc; <br>

> rank() <br>

select continent, name, rank() over(partition by continent order by gdp desc) as rank  from world <br>
group by continent,name <br>
order by continent desc, rank  <br>

> case when then else end <br>

select name,  <br>
case  <br>
when area > 500 then 1  <br>
else 0  <br>
end as tag  <br>
from world  <br>
