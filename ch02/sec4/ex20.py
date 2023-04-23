# ch2 > sec4 > ex20.py

keydata="김민선 박정용 배한구 왕세영 이태석 조원철 홍원준 김기태"
data= "김민선-박정용-배한구-왕세영-이태석-조원철-홍원준-김기태"
para="""김기태
장보고
홍길동
광개토대왕
단군할아버지
박혁거세"""
lst0=keydata.split(" ")
lst1=data.split("-")
lst2=para.split("\n")
print("원본:",keydata)
print("결과:",lst0)
print("원본:",data)
print("결과:",lst1)
print("원본:",para)
print("결과:",lst2)

print("="*30)

# 리스트를 문자열로 변환(join)
st0=' '.join(lst0)
st1='-'.join(lst1)
st2='\n'.join(lst2)
print("원본1:",lst0)
print("결과1:",st0)
print("원본2:",lst1)
print("결과2:",st1)
print("원본3:",lst2)
print("결과3:",st2)