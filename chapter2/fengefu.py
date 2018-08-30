line = 'asdf fsdlsjfl; adfd, fafdl      foo'
import re
result = re.split(r'[;,\s]\s*', line)
print(result)