
import codecs
fi=codecs.open("test.txt","r",encoding='utf-8')
f=fi.read()
fi.close()
f=f.split("\n")
fi=codecs.open("output.txt","a+",encoding='utf-8')
for i in f:
	i=i.split('", ')[1]
	i=i.replace(",","")
	#i=i.replace('"',"")
	fi.write(i+",\n")
fi.close()