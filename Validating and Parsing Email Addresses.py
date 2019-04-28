import email.utils
import re
n=int(input())
regex = re.compile('[!#$%^&*()<>?/\|}{~:]')
rege = re.compile('.')
for x in range(n):
    st=email.utils.parseaddr(input())
    gmail=st[1]
    if gmail[0].isalpha():
        if regex.search(gmail) == None:
            if gmail.count("@") == 1 and 0<gmail.count(".")<3:
                a_index = gmail.index("@")
                user = gmail[0:a_index]
                temp = gmail[a_index:]
                b_index = temp.index(".")
                domain = temp[0:b_index]
                extension = temp[b_index:]
                if len(extension) > 4 or not extension[1:].isalpha():
                    continue
                elif not domain[1:].isalpha():
                    continue
                elif not user.isalnum():
                    if "-" not in user:
                        if "." not in user:
                            if "_" not in user:
                                continue
            else:
                continue
        else:
            continue
    else:
        continue
    print (email.utils.formataddr(st))






