import return_file_path
import return_file_csv_list
import csv

numfour = return_file_path.numfour_return_file_path()
numfive = return_file_path.numfive_return_file_path()

for i in range(len(numfour)):
  origin_list = return_file_csv_list.return_file_csv_data_list(numfour[i])
  try:
    plus_list = return_file_csv_list.return_file_csv_data_list(numfour[i+1])
  except:
    break
  
  for plus_list_row in range(4,245):
   write_data = origin_list 
   write_data.append(plus_list[plus_list_row])
  
  file_path = '/Users/yota/1103_kishimoto/plus_file4/' + return_file_path.numfour_plus_file_path()[i]
  with open(file_path, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(write_data)

for i in range(len(numfive)):
  origin_list = return_file_csv_list.return_file_csv_data_list(numfive[i])
  try:
    plus_list = return_file_csv_list.return_file_csv_data_list(numfive[i+1])
  except:
    break
  
  for plus_list_row in range(4,245):
   write_data = origin_list 
   write_data.append(plus_list[plus_list_row])
   
  file_path = '/Users/yota/1103_kishimoto/plus_file5/' + return_file_path.numfive_plus_file_path()[i]
  with open(file_path, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(write_data)