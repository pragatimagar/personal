with open('sample.txt') as f:
    content = f.read()

content = content.replace('python','#######')

with open('sample.txt','w') as f:
    f.write(content)   
