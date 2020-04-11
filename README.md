## bootstrapyourself
使用 bootstrap 的风格格式化 md 文件对应的 html 代码。

```python
import markdown
from bum import BootStrapExtension

mdstr = """|**会话一**|**会话二**|**会话三**|
|---------|---------|---------|
|create table t(x int primary key);| | |
|start transaction;|||
|insert into t(x) values(1024);|||
||insert into t(x) values(1024);|insert into t(x) values(1024);|
|rollback|commit successful|ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction|
"""

htmltext = markdown.markdown(
    mdstr, extensions=['markdown.extensions.toc', 'legacy_attrs', 'markdown.extensions.fenced_code', 'markdown.extensions.tables', BootStrapExtension()], output_format="html5")

print(htmltext)

```
table 会得到如下效果。

```html
<table class="table table-striped">
<thead>
<tr>
<th><strong>会话一</strong></th>
<th><strong>会话二</strong></th>
<th><strong>会话三</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>create table t(x int primary key);</td>
<td></td>
<td></td>
</tr>
<tr>
<td>start transaction;</td>
<td></td>
<td></td>
</tr>
<tr>
<td>insert into t(x) values(1024);</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>insert into t(x) values(1024);</td>
<td>insert into t(x) values(1024);</td>
</tr>
<tr>
<td>rollback</td>
<td>commit successful</td>
<td>ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction</td>
</tr>
</tbody>
</table>
```

---