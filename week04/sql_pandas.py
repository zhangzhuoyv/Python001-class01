# pandas +excel  等价 SQL 的操作  , 本地EXCEL 名 为 data.xlsx
import pandas as pd
from pandas import DataFrame

# 1. SELECT * FROM data; # 从表格中 data中获取所有数据

# 字典形式的数据：
data = {'这里是是一大堆 字典形式的数据'}

table1 = {'这里是是一大堆 字典形式的数据'}

table2 = {'这里是是一大堆 字典形式的数据'}

df = pd.DataFrame(dict=data)

print(df)


#2. SELECT * FROM data LIMIT 10;   # 从表格中 data中获取前10条数据


print(df.head(10))

#3. SELECT id FROM data;  //id 是 data 表的特定一列   # 从data 中 获取 名为 id 的列 的数据

data_id = df['id']
print(data_id)

# 4. SELECT COUNT(id) FROM data;   # 计数 列 id 有多少行


count_id = data_id.count()
print(count_id)

# 5. SELECT * FROM data WHERE id<1000 AND age>30;  获取  id<1000 AND age>30 的数据

df[df['id']>1000 & df['age']<30]

print(a)


# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;  # 从 table1 中找出所有 id 和 不同的order_id的计数，并用 id 进行聚合

data_id = df['id']

oder_id_count =df['oder_id'].count()

df.groupby('id').agg({'oder_id':set(oder_id_count)})

# 7 SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;  # 找到 表table1里 的字表t1 和 table2 中的子表 t2，各自 列 'id' 相同 的 内容


pd.merge(table1,table2,on='id')


# 8. SELECT * FROM table1 UNION SELECT * FROM table2; # 合并 从table1 和 table2 里的搜索到的内容进行合并

pd.concat(table1,table2)

# 9. DELETE FROM table1 WHERE id=10;  # 删除 table1 里， id 列 值为 10 的 数据

df.drop([df[df['id'] == 10]],axis=0)

# 10. ALTER TABLE table1 DROP COLUMN column_name;  删除 table1 中 ，铭文 column_name 的列

df.drop('column_nam',axis=1)



