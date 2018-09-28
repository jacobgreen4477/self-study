#### [self-study]

#### search vs match 
a = "123abc" <br>

* re.match("[a-z]+",a).group() <br>
AttributeError: 'NoneType' object has no attribute 'group'<br>

* re.search("[a-z]+",a).group()<br>
'abc' <br>
