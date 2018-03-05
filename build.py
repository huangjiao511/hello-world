#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,os,xmlrpclib,zipfile,time,datetime

stream_info={}

def unzip_file(zipfilename, unziptodir):
	if not os.path.exists(unziptodir): os.makedirs(unziptodir)
	zfobj = zipfile.ZipFile(zipfilename)
	for name in zfobj.namelist():
		name = name.replace('\\','/')
		if name.endswith('/'):
			os.makedirs(os.path.join(unziptodir, name))
		else:            
			ext_filename = os.path.join(unziptodir, name)
			ext_dir= os.path.dirname(ext_filename)
			if not os.path.exists(ext_dir) : os.makedirs(ext_dir)
			with open(ext_filename, 'wb') as outfile:
				outfile.write(zfobj.read(name))
				
def delete_file_folder(src):
	if True:
        tttt = 1
	if os.path.isfile(src):  
		try:  
			os.remove(src)  
		except:  
			pass 
	elif os.path.isdir(src):  
		for item in os.listdir(src):  
			itemsrc=os.path.join(src,item)  
			delete_file_folder(itemsrc)  
		try:  
			os.rmdir(src)  
		except:  
			pass 
			
def main_input(stream_name):
	current_path=sys.path[0]
#download build script...
	proxy = xmlrpclib.ServerProxy("http://codecc.oa.com:8080/", allow_none=True)	
#	proxy = xmlrpc.client.ServerProxy("http://localhost:8080/", allow_none=True)	
	print "download coverity build scritp..."
	try:
		bak_folder = current_path+"/bak"
		if os.path.exists(bak_folder): delete_file_folder(bak_folder)
		if not os.path.exists(bak_folder): os.makedirs(bak_folder)
		with open(bak_folder+"/bin.zip", "wb") as handle:
			handle.write(proxy.download().data)
	except Exception as e:
		print e
		exit(1)
#backup bin folder..
	bin_folder = current_path + "/bin"
	if os.path.exists(bin_folder):
		print "backup current bin folder..."
#		if os.path.exists(bak_folder+"/bin.bak"):
#			delete_file_folder(bak_folder+"/bin.bak")
		current_date = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
		os.rename(bin_folder, bak_folder+"/bin.bak_"+current_date)

#unzip bin.zip...
	print  "unzip bin folder..."
	unzip_file(bak_folder+"/bin.zip", current_path)

#trigger main.py to build
	print "trigger the build for "+stream_name+"..."
	os.chdir(bin_folder)
	os.system("python main.py "+stream_name)

def upload_zip_file(stream_name):
	current_path=sys.path[0]
#download build script...
	proxy = xmlrpclib.ServerProxy("http://codecc.oa.com:8080/", allow_none=True)	
#	proxy = xmlrpc.client.ServerProxy("http://localhost:8080/", allow_none=True)	
	print "download coverity build scritp..."
	try:
		bak_folder = current_path+"/bak"
		if os.path.exists(bak_folder): delete_file_folder(bak_folder)
		if not os.path.exists(bak_folder): os.makedirs(bak_folder)
		with open(bak_folder+"/bin.zip", "wb") as handle:
			handle.write(proxy.download().data)
	except Exception as e:
		print e
		exit(1)
#backup bin folder..
	bin_folder = current_path + "/bin"
	if os.path.exists(bin_folder):
		print "backup current bin folder..."
#		if os.path.exists(bak_folder+"/bin.bak"):
#			delete_file_folder(bak_folder+"/bin.bak")
		current_date = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
		os.rename(bin_folder, bak_folder+"/bin.bak_"+current_date)

#unzip bin.zip...
	print  "unzip bin folder..."
	unzip_file(bak_folder+"/bin.zip", current_path)

#trigger main.py to build
	print "trigger the build for "+stream_name+"..."
	os.chdir(bin_folder)
	os.system("python main.py upload "+stream_name)

def update_properties(stream_info, stream_name):
	current_path=sys.path[0]
	stream_properties=current_path+"/"+stream_name+".properties"
	with open(stream_properties, "rU+") as properties:
		lines = properties.readlines()
		for index,line in enumerate(lines):
			if not "#" in line and "PROJECT_BUILD_COMMAND" in line and not stream_info['PROJECT_BUILD_COMMAND'] == "":
					lines.remove(line)
					lines.insert(index, 'PROJECT_BUILD_COMMAND='+stream_info['PROJECT_BUILD_COMMAND']+'\n')
					lines_str = ''.join(lines).strip()
					properties.seek(0)
					properties.truncate()
					properties.write(lines_str)
					break

def create_properties(stream_info, stream_name):
	current_path=sys.path[0]
	stream_properties=current_path+"/"+stream_name+".properties"
	if os.path.isfile(stream_properties):
		os.remove(stream_properties)
	with open(stream_properties, "w") as properties:
			for key in stream_info.keys():
				line = str(key+"="+stream_info[key])
				properties.write(line+'\n')

def delete_properties(stream_name):
	current_path=sys.path[0]
	stream_properties=current_path+"/"+stream_name+".properties"
	if os.path.isfile(stream_properties):
		os.remove(stream_properties)
					
if __name__ == "__main__" :
	if len(sys.argv) == 2:
		main_input(sys.argv[1])
	elif len(sys.argv) == 3 and sys.argv[1] == "upload" :
		upload_zip_file(sys.argv[2])
	elif len(sys.argv) == 3 and "=" in sys.argv[2] and "-DPROJECT_BUILD_COMMAND" in sys.argv[2]:
		tmp = sys.argv[2].split("=",1)
		stream_info[tmp[0].replace("-D","")] = tmp[1].replace("\n", "")
		update_properties(stream_info, sys.argv[1])
		main_input(sys.argv[1])
	elif len(sys.argv) > 3:
		for i in range(len(sys.argv)-2):
			if not "=" in sys.argv[i+2] or not "-D" in sys.argv[i+2]:
				print "Usage python %s [stream_name] -Dxxx=xxx" % sys.argv[0]
				sys.exit()
#	and "=" in sys.argv[2] and "-DPROJECT_BUILD_COMMAND" in sys.argv[2]:
		for i in range(len(sys.argv)-2):
			tmp = sys.argv[i+2].split("=",1)
			stream_info[tmp[0].replace("-D","")] = tmp[1].replace("\n", "")
		create_properties(stream_info, sys.argv[1])
		main_input(sys.argv[1])
		delete_properties(sys.argv[1])
	else:
		print "Usage python %s [stream_name]" % sys.argv[0]
		print "stream_name is  stream name such as xxx_result of xxx"
		sys.exit()