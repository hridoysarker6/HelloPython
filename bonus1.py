filenames = ['1.hello','2.hi','3.bye']

filenames = [item.replace('.','-')+'.txt' for item in filenames]

print(filenames)