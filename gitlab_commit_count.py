url = 'http://192.168.1.229/'  # gitlab安装地址
private_token = 'dfsdfadJZr7ZDMtsn9REC'  # gitlab 就是上面我们获取的那个

# 登录 获取gitlab操作对象gl
gl = gitlab.Gitlab(url, private_token)

start_time = '2020-05-25T00:00:00Z'
end_time = '2020-05-26T00:00:00Z'

projects = gl.projects.list(all=True)#先把所有项目查出来
for project in projects:#遍历每一个项目
	branches = project.branches.list()#把每个项目下面的所有分支查出来
	for branch in branches:#然后再遍历每一个分支
		commits = project.commits.list(all=True,query_parameters={'since': start_time,'until':end_time, 'ref_name': branch.name})#根据时间、分支名遍历该分支下面所有的提交记录
		for commit in commits:#然后再遍历每个提交记录，查询每个提交记录的人和量
			com = project.commits.get(commit.id)
