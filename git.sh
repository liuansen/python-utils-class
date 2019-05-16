unset msg
read -p "请输入commit提交描述：" msg
git add .
git commit -m $msg
git push 
expect "Username for 'https://gitee.com'"
send -- "443877461@qq.com\n"
expect "PassWord for 'https://443877461@qq.com@gitee.com'"
send -- ".dzalw962464\n"
git status

