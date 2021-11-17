0、由于公司电脑会加密，所以使用文本形式写说明文档

1、目录结构：
	code：代码存放路径
		运行：
			运行 apriori.py脚本，即可生成数据文档
			提示：建议先删除output_data_file路径下的文件，然后运行脚本。因为这些文件是用公司电脑生成，已经被加密了
		配置：
			配置head.py 脚本中.file_type变量，通过此标志位设置文件组合形式
				sum：四个文件合并-----------------> sum_confidence.xls
				g_s：GitHub与StackOverflow合并----> g_s_confidence.xls
				u_d：Userguide与docstring合并-----> u_d_confidence.xls
	input_data_file：运行脚本前需要的文档
	output_data_file：运行脚本后输出的文档
	
2、其他注意事项：
	1、生成文件时，当前文件必须要关系，否则会报错
	2、系统提示缺少某些库时，按提示安装相应的库。如:sudo pip install xxx
		
		
		