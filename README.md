#### [self-study]

#### search vs match 
a = "123abc" <br>
re.match("[a-z]+",a).group() <br>
AttributeError: 'NoneType' object has no attribute 'group'<br>
re.search("[a-z]+",a).group()<br>
'abc' <br>

#### 정규표현식 코마 & 마침표 두개 사용
s = '100,000.000'
regex_pattern = r"\.|,"	
regex_pattern = r"[.,]" 
