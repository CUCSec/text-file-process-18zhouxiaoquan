
import re
f=open("D:/360安全浏览器下载/材料/text-file-process-18zhouxiaoquan-master/text-file-process/log_files/201811113032.log",encoding="utf8")
number_text=f.read()
f.close()
number=re.split(r"[,;\s:]",number_text)
dic={"201811113032":0}
for word in number:
	if word in dic:
		dic[word]+=1
print(dic["201811113032"])