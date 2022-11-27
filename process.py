import re
from tqdm import tqdm

re_front=re.compile(r"\d")
re_back=re.compile(r"[A-Za-z]+")

with open("example.txt","r",encoding="utf-8") as f1:
    texts=f1.readlines()
    with open("result.txt","w",encoding="utf-8") as f2:
        with tqdm(total=len(texts)) as pbar:
            _=0
            while _<len(texts):
                if texts[_][0]=="未":
                    _+=1
                    continue

                if re_front.match(texts[_]):
                    if re_back.search(texts[_]):
                        texts[_]=re_back.search(texts[_]).group()
                    #texts[_]=texts[_].rstrip("\n")
                        texts[_]+=","
                        f2.write(texts[_])
                elif re_back.match(texts[_]):
                    if _ <len(texts)-1:
                        if  re_front.match(texts[_+1]) or texts[_+1][0]=="未":
                            
                            f2.write(texts[_])
                        else:
                            texts[_]=texts[_].rstrip("\n")
                            texts[_]+=" "
                            texts[_]+=texts[_+1]
                            f2.write(texts[_])
                            _+=1
                _+=1
                pbar.update(1)
