from setuptools import setup


setup(name='bootstrap-your-markdown',  # 软件包的名字
      version='0.0.1',  # 版本
      description='返回当前是今年的第几周',  # 描述信息
      author="Neeky",  # 作者
      author_email="neeky@live.com",  # 邮件
      maintainer='Neeky',  # 作者
      maintainer_email='neeky@live.com',  # 邮件
      scripts=['bin/week-of-year'],  # 软件也要导出的命令
      packages=['wofy'],  # 软件包要导出的“包”
      url='https://github.com/Neeky/wofy',  # 项目地址
      python_requires='>=3.6.*',  # 版本要求
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8']
      )
