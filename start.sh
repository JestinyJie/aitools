mkdir -p logs

bash stop.sh
gunicorn -c gunicorn_config.py main:app --log-level=debug
echo "started server"