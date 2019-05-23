Welcome to spark_for_python!
===================
    1.下载spark2.2.2

    2.创建spark文件夹
        sudo mkdir /usr/share/spark

    3.解压spark
        sudo tar -zxvf spark-2.2.2-bin-hadoop2.7.tgz -C /usr/share/spark

    4.配置
        sudo vim /etc/profile
        # spark environment
        export SPARK_HOME=/usr/share/spark/spark-2.2.2-bin-hadoop2.7
        export PATH=${SPARK_HOME}/bin:$PATH
        export PYSPARK_PYTHON={你python环境的地址}

    5.生效环境变量
        source /etc/profile

    6.测试
        pyspark 进入spark命令行

    7.在python代码中使用spark
        cd /usr/share/spark/spark-2.2.2-bin-hadoop2.7/python/lib
        sudo cp py4j-0.10.7-src.zip ../
        cd ../
        sudo unzip py4j-0.10.7-src.zip

    8.配置要使用spark对应的python环境
        sudo vim /etc/profile
        export PYTHONPATH=/usr/share/spark/spark-2.2.2-bin-hadoop2.7/python:{你的python环境的地址}

    9.生效环境变量
        source /etc/profile

    10.测试python中使用spark
        #在python虚拟环境下执行
        pip install pyspark
        #运行python命令行
        import pyspark
        #没有报错则成功安装
        
**项目运行**
- 启动程序
   1. python manage.py runserver 0.0.0.0:8000
   2. 登录：http://127.0.0.1:8000/spark/login/?&app_name=spark_web2
   3. 执行：http://127.0.0.1:8000/spark/execute/
    