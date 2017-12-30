import optparse
import zipfile
from threading import Thread

global zname,dname
def extract_zip(zfile,password):
    try:
        zfile.extractall(pwd=password)
        print "[*] Passsord Found :" + password +'\n'
    except:
        pass

def main():
     parser= optparse.OptionParser("usage %prog "+ " -f <zipfile> -d <dictionary>")
     parser.add_option('-f',dest = 'zname',type = 'string', help='specify zip file')
     parser.add_option('-d',dest = 'dname',type ='string', help='specify the dictionary file')
     (options,arg)= parser.parse_args()
     if (options.zname == None) | (options.dname == None):
         print parser.usage
     else:
         zname = options.zname
         dname = options.dname

     zfile= zipfile.ZipFile(zname)
     passFile=open(dname,'r')
    
     for line in passFile.readlines():
         password = line.strip("\n")
         t=Thread(target = extract_zip,args=(zfile,password))
         t.start()
if __name__=='__main__':
    main() 
