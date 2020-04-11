import markdown

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
