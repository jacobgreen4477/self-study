#### [파이썬 정리]

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

#### MySQL
select distinct city from station where id%2=0; <br>
select count(CITY) - count(distinct CITY) from STATION; <br>
select city, length(city) from station where length(city)=(select min(length(city)) from station) order by city limit 1; <br>

> order by(defalut) is ascending <br>



