with open('filename.txt', 'r') as f: 

   d = {} 

   for line in f:
       line = line.split('x') 
       key = line[0].strip()
       value = line[1].strip() 

       if key in d: 

          d[key].append(value) 

       else: 

         d[key] = [value] 

         print(d)