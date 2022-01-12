"""
文件说明：
    1、初始化读写路径与字典
"""	
# 备注：通过此标志位设置文件组合形式
# sum：四个文件合并
# g_s：GitHub与StackOverflow合并
# u_d：Userguide与docstring合并
file_type = 'g_s'

path_confidence = ".\\output_data_file\\confidence.txt"
path_support = ".\\output_data_file\\support.txt"
path_source = ".\\output_data_file\\source.txt"

# excel_suffix = ".\\output_data_file\\"
excel_suffix = ""

input_path_u = ".\\input_data_file\\userguide_co.csv"
input_path_d = ".\\input_data_file\\docstring_co.csv"
input_path_g = ".\\input_data_file\\github_co.csv"
input_path_s = ".\\input_data_file\\stackoverflow_co.csv"


dict_source = {
	'Performance Attribute' : 'Performance Attributes' ,
	'Performance Attributes' : 'Performance Attributes' ,
	'attributes' : 'Performance Attributes' ,
	'perf attributes' : 'Performance Attributes',

	'functionality desc' : 'Functionality & Behavior' ,
	'Functionality & Behavior' : 'Functionality & Behavior' ,
	'functionality' : 'Functionality & Behavior' ,
 
	'Implementation Details' : 'Implementation or Internal Aspects' ,
	'impl' : 'Implementation or Internal Aspects' ,
	'Implementation or Internal Aspects' : 'Implementation or Internal Aspects' ,
	'impl details' : 'Implementation or Internal Aspects' ,

	'Purpose & Rationale' : 'Purpose & Rationale'   ,
	'rationale' : 'Purpose & Rationale'   ,
	'purpose & rationale' : 'Purpose & Rationale'   ,

	'Alternatives' : 'Alternatives'   ,
	'alternatives' : 'Alternatives'   ,
	'comparison with alternatives' : 'Alternatives'   ,
	'Comparison w/ Alternatives' : 'Alternatives'   ,

	'usage practice' : 'Usage Practice'   ,
	'practice' : 'Usage Practice'   ,
	'Usage Practice' : 'Usage Practice'   ,
    
	'Concept' : 'Concepts'   ,
	'concepts' : 'Concepts'   ,
    
	'Directives' : 'Directives'   ,
	'directives' : 'Directives'   ,
     
	'Environment' : 'Environment'   ,
	'environment' : 'Environment'   ,
    
	'Directives' : 'Directives'   ,
	'directives' : 'Directives'   ,
    
	'Misc' : 'Miscellaneous'   ,
	'misc' : 'Miscellaneous'   ,
    
	'references' : 'References'   ,
	'Reference' : 'References'   ,
	'ref' : 'References'   ,
	'Ref' : 'References'  
    }

dict_char2num = {
    'Performance Attributes': 1 ,
    'Alternatives':2 ,
    'Concepts':3 ,
    'Directives':4 ,
    'Environment':5 ,
    'Functionality & Behavior':6 ,
    'Implementation or Internal Aspects':7 ,
    'Miscellaneous':8 ,
    'Purpose & Rationale':9 ,
    'References':10 ,
    'Usage Practice':11
    }

dict_num2char = {
    1 : 'Performance' ,
    2 : 'Alternatives' ,
    3 : 'Concepts' ,
    4 : 'Directives' ,
    5 : 'Environment' , 
    6 : 'Functionality' ,
    7 : 'Implementation' ,
    8 : 'Miscellaneous' ,
    9 : 'Purpose' ,
    10 : 'References' ,
    11 : 'Practice'
    }

def set_file_type():
    global excel_suffix

    if file_type == 'sum':
        excel_suffix = ".\\output_data_file\\sum_confidence.xls"
    elif file_type == 'g_s':
        excel_suffix = ".\\output_data_file\\g_s_confidence.xls"
    elif file_type == 'u_d':
        excel_suffix = ".\\output_data_file\\u_d_confidence.xls"
    else:
        excel_suffix = ".\\output_data_file\\sum_confidence.xls"
