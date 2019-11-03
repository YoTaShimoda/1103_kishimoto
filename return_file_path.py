import glob

def numfour_return_file_path():
    numfour = glob.glob('/Users/yota/1103_kishimoto/csv_data/active_rate/active_no4/*')
    numfour = sorted(numfour)
    return numfour

def numfive_return_file_path():
    numfive = glob.glob('/Users/yota/1103_kishimoto/csv_data/active_rate/active_no5/*')
    numfive = sorted(numfive)
    return numfive

def numfour_plus_file_path():
  plus_file_path_list = []
  numfour = numfour_return_file_path()

  for file_path in numfour:
    plus_file_path = file_path.replace('/Users/yota/1103_kishimoto/csv_data/active_rate/active_no4/', '') 
    plus_file_path_list.append(plus_file_path)
  return plus_file_path_list

def numfive_plus_file_path():
  plus_file_path_list = []
  numfive = numfive_return_file_path()

  for file_path in numfive:
    plus_file_path = file_path.replace('/Users/yota/1103_kishimoto/csv_data/active_rate/active_no5/', '') 
    plus_file_path_list.append(plus_file_path)
  return plus_file_path_list
