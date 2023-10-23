set_highjump={"李朋","王宇","张锁","刘松山","白旭","李晓亮"}
set_longjump={"王宇","唐英","刘松山","白旭","刘小雨","宁成"}

set_name=set_highjump | set_longjump
print(set_name)
set_double=set_highjump & set_longjump
print(set_double)
set_highjump_only=set_highjump-set_longjump
set_longjump_only=set_longjump-set_highjump
print(set_highjump_only)
print(set_longjump_only)
set_only=set_highjump ^ set_longjump
print(set_only)
