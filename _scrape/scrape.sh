echo 'begin'
python /home/ec2-user/names2018/names.py
echo 'python run, temp name data created. remove previous name_data'
rm /home/ec2-user/names2018/fruithandler_regional.csv
echo 'change name of temp to fruithandler_regional.csv'
mv /home/ec2-user/names2018/fruithandler_regional_temp.csv /home/ec2-user/names2018/fruithandler_regional.csv
echo 'transfer file to s3'
/home/ec2-user/bin/s3cmd put /home/ec2-user/names2018/fruithandler_regional.csv s3://energy2/social/
echo 'process complete'