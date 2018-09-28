#### [self-study]

#### search vs match 
a = "123abc"
* re.match("[a-z]+",a).group() 
AttributeError: 'NoneType' object has no attribute 'group'
* re.search("[a-z]+",a).group()
# 'abc'
