import re

line = "this hdr-biz model server"
lines =['n. (Job)人名；(英)乔布；(法、葡)若布；(?-1605)约伯〈俄〉俄罗斯正教会莫斯科牧首。；(德、塞、捷、荷、意)约布',
        'n. (Job)；(英)乔布；(法、葡)若布；(?-1605)']
pattern = r"人名"
for i in lines:
    m = re.search(pattern, i)
    if not m:
        print(m)