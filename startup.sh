echo "FLASK_ENV:"
read env_mode
echo "FLASK_APP:"
read entry_point


export FLASK_ENV=$env_mode
export FLASK_APP=$entry_point


if [ $entry_point == "server.py" ]; then
    flask run
elif [ $entry_point == "shell_context.py" ]; then
    flask shell
else 
    echo "Unknow entry_point; $entry_point"
fi
