from functools import wraps
from core.tools import *
from core.processer import execute

def Select(sql=""):
	def doDecorator(func):
		@wraps(func)
		def run(*args,**kwargs):
			argList = getVariables(sql)
			vars = {}
			for arg in argList:
				index = getParamID(func,arg)
				#print(arg+":"+str(args[index]))
				vars[arg] = str(args[index])
			#print(vars)
			return execute(renderSql(sql,vars))
		return run
	return doDecorator
	
def Insert(sql=""):
	def doDecorator(func):
		@wraps(func)
		def run(*args,**kwargs):
			argList = getVariables(sql)
			vars = {}
			for arg in argList:
				index = getParamID(func,arg)
				#print(arg+":"+str(args[index]))
				vars[arg] = str(args[index])
			#print(vars)
			return execute(renderSql(sql,vars))
		return run
	return doDecorator
	
def Update(sql=""):
	def doDecorator(func):
		@wraps(func)
		def run(*args,**kwargs):
			argList = getVariables(sql)
			vars = {}
			for arg in argList:
				index = getParamID(func,arg)
				#print(arg+":"+str(args[index]))
				vars[arg] = str(args[index])
			#print(vars)
			return execute(renderSql(sql,vars))
		return run
	return doDecorator
	
def Delete(sql=""):
	def doDecorator(func):
		@wraps(func)
		def run(*args,**kwargs):
			argList = getVariables(sql)
			vars = {}
			for arg in argList:
				index = getParamID(func,arg)
				#print(arg+":"+str(args[index]))
				vars[arg] = str(args[index])
			#print(vars)
			return execute(renderSql(sql,vars))
		return run
	return doDecorator

