with open('./2018_Central_Park_Squirrel_Census.csv') as f:
    sq_data = f.readlines()
    sq_colors ={}   
    for row in sq_data[1:]:
        color = row.split(',')[8]
        if color not in sq_colors:
           sq_colors[color] = 1
        else:
            
            sq_colors[color]+=1 

with open('sq_summary.csv','a') as f:
    idx = 0
    for k, v in sq_colors.items():
        appends = (str(idx) ,k, str(v))
        appends = ','.join([i for i in appends])
    
        f.write(appends)
        f.write('\n')
        idx += 1




      