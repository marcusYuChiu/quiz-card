#echo "FLASK_ENV:"
#read env_mode
#echo "FLASK_APP:"
#read entry_point
#
#
#export FLASK_ENV=$env_mode
#export FLASK_APP=$entry_point
#
#
#if [ $entry_point == "server.py" ]; then
#    flask run
#elif [ $entry_point == "shell_context.py" ]; then
#    flask shell
#else 
#    echo "Unknow entry_point; $entry_point"
#fi

echo "Choose the one:\n server\n shell\n test"
read answer


if [ $answer == "server" ];then
    export FLASK_ENV=development
    export FLASK_APP=server.py
    flask run
elif [ $answer == "shell" ];then
    export FLASK_ENV=development
    export FLASK_APP=shell_context.py
    flask shell
elif [ $answer == "test" ];then
    echo "not set yet"
else
    echo "Unknow option: $answer"
fi
