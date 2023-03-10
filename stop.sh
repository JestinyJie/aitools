if [ -f "gunicorn.pid" ];then
  echo "killed `cat gunicorn.pid`"
  kill `cat gunicorn.pid`
  sleep 3
fi
